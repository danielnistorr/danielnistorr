# Benvegnù S.r.l.: nuovo sito per WordPress + Elementor

Sito completo in 7 pagine (Home, Azienda, Catalogo, Vibram, Marchi, Novità, Contatti) più header e footer, in due formati:
- **Formato A (primario):** template Elementor `.json` da importare con *Template > Template salvati > Importa template*.
- **Formato B (fallback):** la stessa pagina in HTML+CSS autosufficiente, una sezione per file, da incollare in un widget HTML di Elementor.

Tutti i file sono stati **importati e provati davvero** su un WordPress di test (vedi "Collaudo"). Le immagini delle pagine sono in `screenshot/`.

Direzione grafica: bianco e nero, foto vere del magazzino e della sede in bianco e nero, prodotti a colori, Barlow Condensed e Barlow, il rosso storico di Benvegnù solo in piccolo. I riferimenti reali (Gruppo Mastrotto, Santoni, Rubelli, Vibram, Oerlikon Riri) e il perché di ogni scelta sono in `02-competitor-e-riferimenti.md`.

## Cosa c'è nella cartella

| Cartella / file | Contenuto |
|---|---|
| `01-analisi-sito-attuale.md` | pagine, testi reali, immagini e problemi del sito attuale |
| `02-competitor-e-riferimenti.md` | 14 concorrenti, riferimenti premium e funzionali, pattern ripresi dal PMF |
| `03-mappa-pagine.md` | mappa finale delle pagine e sezioni |
| `elementor-json/` | **Formato A**: `bvg-00-header.json`, `bvg-99-footer.json` (tipo *sezione*) e le 7 pagine `bvg-01-home.json` ... `bvg-07-contatti.json` (tipo *pagina*, solo il corpo) |
| `elementor-json/pagine-complete-senza-pro/` | le stesse 7 pagine con header e footer già dentro e modello *Canvas* |
| `elementor-json/testi-alternativi-immagini.txt` | testi alternativi da incollare nella libreria media (Elementor li perde all'import) |
| `html-fallback/` | **Formato B**: una cartella per pagina, un file `.html` per sezione, più `00-header/` e `99-footer/` |
| `anteprima/` | le 7 pagine complete in HTML, da aprire nel browser: doppio clic su `anteprima/index.html` (vedi "Vedere il sito subito") |
| `plugin/contact-form-7-richiesta-disponibilita.txt` | il modulo "Richiesta disponibilità" da incollare in Contact Form 7 (campi ed email) |
| `plugin/redirect-301.csv` | 14 regole di redirect dal sito attuale, da importare nel plugin Redirection |
| `plugin/benvegnu-installer.zip` | plugin che installa e configura tutto il sito su un WordPress pulito (vedi "Installazione automatica") |
| `assets/web/` | le 53 immagini preparate per il sito (foto in bianco e nero, prodotti a colori, loghi) |
| `assets/originali/` | tutte le immagini scaricate dal sito attuale, con `manifest.json` |
| `screenshot/` | le pagine dopo l'import in Elementor e il fallback HTML, a 1440, 1024 e 390 px |
| `_sorgente/` | il generatore: `contenuti.py` (testi e pagine), `motore.py`, `build.py`, `prepara_immagini.py`, `redirect.py` |

## Vedere il sito subito

Senza installare niente: scarica il ramo `claude/benvegnu-sito` (su GitHub: *Code > Download ZIP*), scompatta e apri con doppio clic `BenvegnuSrl-Sito/anteprima/index.html`. Le 7 pagine sono collegate tra loro e le immagini sono quelle della cartella `assets/web`, quindi funziona anche senza internet (servono solo i font Google e la mappa).

Se preferisci un indirizzo `localhost`: apri un terminale nella cartella `BenvegnuSrl-Sito` e lancia `python3 -m http.server 8000`, poi vai su http://localhost:8000/anteprima/

L'anteprima è la versione HTML (Formato B): a vista è uguale a quella Elementor, con tre differenze. Al posto del modulo Contact Form 7 c'è un pulsante che apre un'email già compilata; la lista "Ultime novità" è fissa; il menu su telefono è un elenco semplice invece della tendina di Ultimate Addons.

## Installazione automatica su un WordPress pulito

`plugin/benvegnu-installer.zip` fa tutto il lavoro del paragrafo "Come importare" da solo. È così che il sito è stato messo su https://benvegnu.evoxconsulting.it (sito di prova, non indicizzato) il 5 ottobre 2026.
1. Su un WordPress appena installato: *Plugin > Aggiungi nuovo > Carica plugin*, scegli lo zip, *Installa*, *Attiva*.
2. *Strumenti > Installa Benvegnù*: apri i passi uno alla volta, nell'ordine (plugin e tema, prima attivazione, impostazioni, i 9 template, pagine, header/footer e menu, modulo, articoli di esempio, verifica). Ogni passo stampa cosa ha fatto.
3. Alla fine disattiva ed elimina il plugin di installazione.

Il passo "impostazioni" imposta il sito come **non indicizzabile** (va bene per la prova): per la messa online definitiva togli la spunta in *Impostazioni > Lettura*. Il passo "articoli di esempio" crea due articoli per la pagina Novità: sul sito definitivo saltalo. Per rigenerare lo zip dopo una modifica: `python3 _sorgente/build.py` e poi `python3 _sorgente/crea_installer.py`.

## Versioni e plugin

**Target dichiarato: Elementor 4.3.3, versione gratuita** (l'ultima stabile al 4 ottobre 2026), con WordPress 7.1.2 e tema Hello Elementor 3.5.1. Plugin gratuiti usati, tutti dal catalogo di WordPress.org:

| Plugin | Versione provata | A cosa serve | Obbligatorio? |
|---|---|---|---|
| Ultimate Addons for Elementor (slug `header-footer-elementor`) | 2.9.5 | header e footer su tutto il sito senza Elementor Pro; widget "Navigation Menu" con menu a scomparsa su tablet e telefono | **sì**: il menu dell'header è un suo widget |
| Contact Form 7 | 6.1.7 | modulo "Richiesta disponibilità" nella pagina Contatti | no: senza, al posto del modulo resta lo shortcode come testo (vedi sotto) |
| Redirection | 5.10.1 | redirect 301 dagli indirizzi del sito attuale | consigliato al momento della messa online |

Il JSON è scritto nel modo più conservativo possibile:
- solo **contenitori flexbox** e **widget classici gratuiti**: Titolo, Testo, Immagine, Pulsante, Divisore, Google Maps, HTML, Shortcode, "Articoli recenti" di WordPress, più "Navigation Menu" di Ultimate Addons;
- nessun widget o chiave Pro, nessun elemento "atomico" della v4, nessun riferimento ai colori e font globali del kit (`__globals__`), nessuna animazione;
- colori, font e misure scritti in chiaro su ogni elemento;
- formato del file uguale a quello che Elementor produce con "Esporta template" (`content`, `page_settings`, `version: "0.4"`, `title`, `type`).

Su versioni 3.x recenti (dalla 3.16, quando i contenitori sono diventati stabili) dovrebbe funzionare, ma **non l'ho provato**: l'unica versione collaudata è la 4.3.3.

## Come importare (Formato A)

Prima di iniziare:
1. Accedi come **Amministratore** (gli altri ruoli non possono importare JSON, e senza il permesso "unfiltered_html" WordPress ripulisce stili e iframe).
2. *Elementor > Impostazioni > Funzionalità*: **Contenitore = Attivo** (è il valore predefinito dalla 3.16). Se è disattivato, l'import riesce ma la pagina resta **vuota, senza errori**.
3. Il sito deve poter scaricare file da Internet: le immagini arrivano durante l'import (vedi "Immagini").
4. Installa e attiva **Ultimate Addons for Elementor** e **Contact Form 7** (*Plugin > Aggiungi nuovo*).

### 1. Pagine e menu
1. *Pagine > Aggiungi pagina* per ognuna: Home, Catalogo, Vibram, Marchi, Azienda, Novità, Contatti, con **slug** esatto `catalogo`, `vibram`, `marchi`, `azienda`, `novita`, `contatti`. I link interni puntano a questi indirizzi.
2. *Aspetto > Menu*: crea un menu chiamato **Menu principale** con le 6 pagine in quest'ordine: Catalogo, Vibram, Marchi, Azienda, Novità, Contatti. Il widget del menu nell'header cerca questo menu; se lo chiami diversamente, dopo l'import aprilo nell'editor e scegli il menu giusto dal campo "Menu".
3. *Impostazioni > Lettura > La homepage mostra: una pagina statica > Home*.

### 2. Modulo di contatto
*Contatto > Aggiungi nuovo*, titolo esatto **Richiesta disponibilità**, poi incolla nelle schede "Modulo" e "Mail" il contenuto di `plugin/contact-form-7-richiesta-disponibilita.txt`. La pagina Contatti richiama il modulo per titolo (`[contact-form-7 title="Richiesta disponibilità"]`): se il titolo è diverso, il modulo non compare.

### 3. Header e footer su tutto il sito (senza Pro)
1. *Template > Template salvati > Importa template*: importa `bvg-00-header.json` e `bvg-99-footer.json`. Se compaiono gli avvisi "i file JSON possono essere pericolosi" e "upload non filtrati", scegli **Continua** e poi **Importa senza abilitare**.
2. *UAE > Header & Footer > Create New*: titolo "Header", *Type of Template* **Header**, *Display On* **Entire Website**, pubblica; *Modifica con Elementor* > icona cartella > *I miei template* > inserisci "Benvegnù: Header". Salva.
3. Ripeti per il footer (*Type of Template* **Footer**, template "Benvegnù: Footer").

### 4. Le pagine
1. Importa le 7 pagine da `elementor-json/` (solo il corpo).
2. Apri ogni pagina con Elementor > icona cartella > *I miei template* > inserisci il template della pagina. Quando l'editor chiede se applicare le impostazioni della pagina, rispondi **Applica** (modello "Elementor a larghezza piena", titolo nascosto). Salva.

**Alternativa con Elementor Pro:** al punto 3 usa *Template > Theme Builder* (Header e Footer con condizione *Intero sito*) al posto di Ultimate Addons. Il widget del menu resta quello di Ultimate Addons, quindi il plugin serve comunque.

**Alternativa senza header globale:** i file in `elementor-json/pagine-complete-senza-pro/` hanno header e footer già dentro ogni pagina e modello *Canvas*. Funzionano, ma ogni modifica all'header va ripetuta su 7 pagine: usali solo se non puoi installare Ultimate Addons come header globale.

### 5. Redirect dal sito attuale
Al momento della messa online: installa **Redirection**, *Strumenti > Redirection > Import/Export > Importa* e carica `plugin/redirect-301.csv`. Le 14 regole coprono tutte le 1067 pagine trovate nel sito attuale (prodotti, famiglie, pagine in italiano e inglese) e le mandano alla pagina nuova corrispondente con un 301.

### Novità
La lista "Ultime novità" usa il widget gratuito di WordPress "Articoli recenti": mostra gli ultimi articoli del blog. Per pubblicare un avviso (chiusura per ferie, nuovo arrivo) basta scrivere un articolo in *Articoli > Aggiungi articolo*. Nel test ho creato due articoli di esempio: "Il nuovo sito di Benvegnù è online" e "Il catalogo online: 874 articoli in 10 famiglie".

## Immagini

Ogni immagine nel JSON punta a un indirizzo pubblico su GitHub (`raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/...`). **Durante l'import Elementor scarica ogni immagine e la carica nella tua libreria media**: dopo l'import le immagini sono sul tuo sito e il link a GitHub non serve più. Il ramo GitHub deve però esistere al momento dell'import.

Ogni immagine ha un ID numerico fisso: reimportando lo stesso template Elementor riconosce le immagini già scaricate e **non crea doppioni**. Il rovescio: se rigeneri un'immagine **con lo stesso nome** e reimporti, Elementor riusa quella vecchia già in libreria. Per aggiornare una foto, cancellala prima dalla libreria media (oppure sostituiscila lì).

Se preferisci non dipendere da GitHub: carica la cartella `assets/web/` sul tuo server (per esempio in `wp-content/uploads/benvegnu/`) e rigenera i file con
`python3 _sorgente/build.py --base https://TUO-DOMINIO/wp-content/uploads/benvegnu/`

## Cosa potrebbe non reggere l'import (tieni pronto il fallback)

Il formato dei template Elementor ha ID e versioni dei widget che Elementor genera da sé. Ho scritto i file come li esporta Elementor e li ho importati sulla 4.3.3, ma sul tuo sito queste cose possono andare diversamente:

1. **Versione diversa da 4.3.3.** Su versioni 3.x vecchie (prima della 3.16) i contenitori non ci sono: il template risulta vuoto. Su versioni future qualche controllo può cambiare nome: un nome sconosciuto **non dà errore**, viene solo ignorato (il risultato è uno stile predefinito al posto del mio).
2. **Contenitore disattivato** nelle funzionalità: pagina vuota senza avviso.
3. **Ultimate Addons non attivo**: il widget del menu sparisce dall'header senza errori; logo, "Chiama" e "Chiedi disponibilità" restano.
4. **Immagini non scaricabili** (sito senza accesso a Internet, firewall, GitHub irraggiungibile, timeout): al loro posto compare il **riquadro grigio di Elementor**, senza errori. Controlla ogni pagina dopo l'import.
5. **Testo alternativo delle immagini**: Elementor lo perde all'import. L'alt va compilato nella libreria media (elenco pronto in `elementor-json/testi-alternativi-immagini.txt`). Le foto dell'apertura e dei blocchi del catalogo sono sfondi di contenitore: non hanno alt per natura, il testo accanto le descrive.
6. **Stili in linea nei testi**: se importi con un utente senza "unfiltered_html", WordPress toglie gli stili scritti dentro i testi. Ho evitato di dipenderne (l'indice del catalogo, per esempio, è fatto di widget separati); si perderebbe solo lo spessore della sottolineatura dei link.
7. **ID degli elementi**: Elementor li rigenera sempre all'import e all'inserimento. Non è un problema, ma non puoi riferirti agli ID del file.
8. **Font**: Barlow e Barlow Condensed sono caricati da Google Fonts da Elementor. Per il GDPR conviene attivare *Elementor > Impostazioni > Avanzate > Carica i Google Fonts localmente*; dopo, controlla che i titoli siano ancora condensati.
9. **Stili del tema**: con un tema diverso da Hello Elementor, titoli e link possono ereditare margini o colori del tema. Ho messo colori espliciti ovunque; il widget "Articoli recenti", il modulo Contact Form 7 e il menu hanno un piccolo CSS dedicato dentro un widget HTML.
10. **Kit globale**: i miei elementi non usano i colori e i font globali. Conviene comunque impostare in *Impostazioni del sito* i colori Nero `#111111`, Bianco `#FFFFFF`, Grigio `#F3F3F1`, Testo secondario `#5A5A5A`, Rosso `#9F2E29` e i font Barlow Condensed e Barlow, così i nuovi elementi aggiunti a mano nascono coerenti.
11. **Larghezze su mobile**: Elementor non eredita la larghezza mobile dei contenitori da quella tablet. L'ho scritta esplicitamente su tutti i breakpoint; se modifichi un blocco dall'editor, controlla anche le viste tablet e mobile.
12. **Link interni** relativi (`/catalogo/`): funzionano se WordPress è nella radice del dominio. Se è in una sottocartella o vuoi link assoluti: `python3 _sorgente/build.py --url-sito https://www.benvegnusrl.it`.
13. **Mappa Google** (widget gratuito, iframe, resa in grigio con un filtro CSS): imposta cookie di terze parti. Va gestita con il banner cookie del sito.
14. **Il PDF delle condizioni di vendita** punta ancora al sito attuale: caricalo nella libreria media e aggiorna il link (Footer, Azienda, Contatti, Home).
15. **Striscia "Dal catalogo" in Home**: è fatta di normali contenitori Elementor (le foto entrano nella libreria media come le altre); lo scorrimento, le frecce e la barra rossa stanno in un widget HTML con poco CSS e JavaScript. Senza JavaScript la striscia scorre lo stesso e le frecce restano nascoste. Se un plugin di ottimizzazione rimanda o unisce gli script in linea, escludi quel widget e controlla che le frecce funzionino.
16. **Sovrapposizioni in Home**: la foto Vibram che esce dalla fascia nera e il titolo "Vieni al banco" sopra la facciata funzionano finché a quei contenitori non si dà un indice z o "Overflow nascosto". Se modifichi quelle sezioni dall'editor, lascia questi due campi vuoti.

Se un template non entra o arriva rotto, usa il Formato B per quella pagina.

## Come usare il Formato B (fallback HTML)

1. Crea la pagina e aprila con Elementor; nelle impostazioni pagina scegli il modello **Elementor Canvas**.
2. Per ogni file della cartella della pagina, nell'ordine (`00-header/01-header.html`, poi `01-home/01-apertura.html`, `02-catalogo.html`..., infine `99-footer/01-footer.html`): aggiungi un **contenitore a larghezza piena con padding 0 e spaziatura 0**, dentro un widget **HTML**, incolla il contenuto del file.
3. Ogni file è autosufficiente: carica i propri font, ha il CSS con un prefisso unico (`.bvg-home-catalogo` ecc.) che non tocca il resto del sito e resiste agli stili del tema.

Differenze rispetto al Formato A: i testi si modificano solo nel codice; il menu su telefono è un elenco a scomparsa senza JavaScript; la lista "Ultime novità" è statica; al posto del modulo Contact Form 7 c'è un pulsante che apre un'email già impostata con le voci della richiesta. Le immagini puntano all'indirizzo GitHub: per la pubblicazione definitiva conviene rigenerare con `--base` verso le immagini caricate sul tuo sito.

## Collaudo fatto

WordPress 7.1.2 in locale (italiano), Elementor 4.3.3, Hello Elementor 3.5.1, Ultimate Addons 2.9.5, Contact Form 7 6.1.7, Redirection 5.10.1, PHP 8.3.
- Import dei 9 template con la stessa funzione del pulsante *Importa template* (`Source_Local::import_template`), libreria media svuotata prima: tutti entrati, **elementi salvati uguali a quelli del file**, **tutte le immagini scaricate**, nessun riquadro grigio.
- Striscia della Home provata a 1440 e 390 px, in Elementor e nel fallback: ogni freccia sposta di una scheda, la barra segue, le frecce si spengono agli estremi, la pagina non scorre mai di lato; senza JavaScript le frecce spariscono e lo scorrimento resta.
- Header e footer globali creati con Ultimate Addons dai template importati; menu "Menu principale" con 6 voci; menu orizzontale su desktop, a scomparsa su tablet e telefono (aperto e fotografato).
- Modulo Contact Form 7 creato dal file in `plugin/` e mostrato nella pagina Contatti.
- Redirect: le 14 regole importate in Redirection, verificato il 301 su indirizzi vecchi di prodotti e famiglie.
- Pagine fotografate a 1440, 1024 e 390 px, controllate senza scorrimento orizzontale: `screenshot/elementor/`.
- Fallback HTML fotografato alle stesse larghezze: `screenshot/fallback/`.
- Import dal pulsante vero dell'interfaccia (Playwright, con i due avvisi "Continua" e "Importa senza abilitare") di `bvg-01-home.json` così com'è nel repository: 155 elementi su 155, le 15 immagini scaricate da GitHub nella libreria media, nessun riquadro grigio, nessun link residuo a GitHub.

## Da confermare con il cliente prima di pubblicare

1. **"Dal 1980"**: è la data dichiarata dall'azienda; la S.r.l. risulta iscritta il 24/10/1990. La tabella "Le date" in Azienda riporta entrambe.
2. **"Rivenditore autorizzato Vibram"**: è scritto sul sito attuale; serve la conferma e il permesso scritto per usare il logo Vibram (i marchi Vibram, ottagono giallo compreso, sono registrati).
3. Loghi Gütermann (quello attuale è la versione vecchia: chiedere il logo A&E Gütermann a A&E Gütermann Italy, Torino), Girba, Fratelli Zucchini: permesso d'uso e file aggiornati. Nel sito sono in scala di grigi: va bene anche per i marchi?
4. **Orari**: lun-ven 8:30-12:30 e 14:30-18:30 (Google e sito attuale); alcune directory dicono chiusura alle 19:00.
5. **Parcheggio clienti davanti al negozio**: citato nelle recensioni Google.
6. **Spedizione con corriere** e condizioni di vendita del 2014 (minimo d'ordine 200 euro + IVA, bonifico anticipato, 7 giorni lavorativi): sono ancora valide?
7. **Email di riferimento**: il sito usa `commerciale@benvegnusrl.it`, anche come destinatario del modulo; nei PDF compaiono anche `info@` e `mail@`.
8. **Sede legale a Padova** (Piazzetta Primo Modin 12) nel footer: confermare. Esiste ancora un punto vendita a Padova, Via S. Salvatore 37?
9. Famiglie non online (lacci, cerniere, chiodi, occhielli, rinforzi, adesivi Zucchini): sono ancora a magazzino?
10. Logo **vettoriale** (oggi c'è solo un PNG 295x72) e le foto originali dei banner a risoluzione più alta.
11. Pagine **Privacy** e **Cookie** (linkate nel footer e nel consenso del modulo) da scrivere.
12. **"Molti dei nostri clienti producono per i marchi del lusso"** (Home, "Per chi lavoriamo"): è un'affermazione pubblica, va approvata dal cliente.
13. **Codici nella striscia della Home** (14932, 9978, 15752, 14563, 7995, 15531): sono i codici del catalogo online; confermare che al banco si usano gli stessi. Confermare anche le unità in mm del coltello C.Dick (270 x 20) e delle etichette (28 x 8).
14. **Foto dell'espositore Vibram** (Home, "Vibram al banco"): l'unica disponibile è un ritaglio di 470 px, mostrato a circa 800 px; serve una foto dell'espositore di almeno 1600 px sul lato corto. Lo stesso vale per la foto del banco nella pagina Vibram.

## Foto da fare (brief breve)

Oggi ci sono solo una foto esterna e 9 foto del magazzino a 750 px: reggono, ma sono il limite più evidente del sito su schermi grandi. Per farlo crescere servono 15-20 scatti in una giornata: pile di lastre Vibram viste di taglio, coni di filo Gütermann in fila, utensili sul banco (forbici, trincetti, lesine, punzoni), latte di colla e flaconi Girba, scaffali con i cartellini, il banco con un cliente, mani che misurano una lastra, l'ingresso con il parcheggio. Luce naturale o flash diffuso laterale, niente luce gialla; ogni scatto deve funzionare in bianco e nero; per i soggetti principali sia orizzontale 3:2 sia verticale 4:5, almeno 2400 px sul lato lungo. Le foto prodotto restano a colori su fondo bianco.

## Rigenerare i file

Serve Python 3 con Pillow (`pip install pillow`).
```
python3 _sorgente/prepara_immagini.py        # rifà assets/web/ dalle immagini originali
python3 _sorgente/build.py                   # rifà elementor-json/, html-fallback/, anteprima/
python3 _sorgente/redirect.py                # rifà plugin/redirect-301.csv
```
Opzioni di `build.py`: `--base URL` (dove sono le immagini), `--url-sito URL` (link interni assoluti), `--out CARTELLA`.
I testi si cambiano in `_sorgente/contenuti.py` (dati aziendali in cima al file). Il build si ferma se trova un trattino lungo, una parola da evitare ("eccellenza", "leader", "passione"...), un valore di stile non valido, un'immagine senza testo alternativo o un link dentro un blocco già cliccabile.
