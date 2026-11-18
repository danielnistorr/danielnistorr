# Albergo Ristorante Leon d'Oro: nuovo sito per WordPress + Elementor

Sito completo in 7 pagine (Home, Camere, Ristorante, Bike hotel, Per l'ospedale, Dove siamo, Prenota) più testata e piede, in due formati:
- **Formato A (primario):** template Elementor `.json` da importare con *Template > Template salvati > Importa template*.
- **Formato B (fallback):** la stessa pagina in HTML+CSS autosufficiente, una sezione per file, da incollare in un widget HTML di Elementor.

Tutti i file sono stati **importati e provati davvero** su un WordPress di prova (vedi "Collaudo fatto"). Le immagini delle pagine sono in `screenshot/`.

L'idea del sito: le cose vere della casa, una alla volta, grandi su molto bianco. Ogni pagina si apre con una foto sola e un titolo maiuscolo di due o tre parole, e si chiude sul giallo della facciata, dove si prenota. Nella home la prima schermata è la facciata di sera con **RESTA A CENA** a 144 px. Un carattere solo, Libre Franklin (dalle maiuscole della cartolina e del logo), tre colori presi dalla casa: il bianco delle tovaglie, il verde delle persiane, il giallo del muro. I riferimenti reali (Bouillon Chartier, St. JOHN, Trattoria Masuelli, Salvatori) e il perché di ogni scelta sono in `02-competitor-e-riferimenti.md` e in `_prova/spec.md` (la specifica, fuori dal repository).

## Cosa c'è nella cartella

| Cartella / file | Contenuto |
|---|---|
| `01-analisi-sito-attuale.md` | pagine, testi reali numerati, immagini e problemi misurati del sito attuale, dati aziendali con le fonti |
| `02-competitor-e-riferimenti.md` | 4 concorrenti a Este e Monselice, 7 riferimenti reali, le tre accoppiate di caratteri e colori |
| `03-mappa-pagine.md` | mappa delle pagine e delle sezioni |
| `MAIL-PROPOSTA.md`, `allegati-mail/` | osservazioni sul sito attuale e bozza della mail di proposta (la invia il committente) |
| `elementor-json/` | **Formato A**: `ldo-00-header.json`, `ldo-99-footer.json` (tipo *sezione*) e le 7 pagine `ldo-01-home.json` ... `ldo-07-prenota.json` (tipo *pagina*, solo il corpo) |
| `elementor-json/pagine-complete-senza-pro/` | le stesse 7 pagine con testata e piede già dentro e modello *Canvas* |
| `elementor-json/testi-alternativi-immagini.txt` | testi alternativi da incollare nella libreria media (Elementor li perde all'import) |
| `html-fallback/` | **Formato B**: una cartella per pagina, un file `.html` per sezione, più `00-header/` e `99-footer/` |
| `anteprima/` | le 7 pagine complete in HTML, da aprire nel browser: doppio clic su `anteprima/index.html` |
| `plugin/contact-form-7-richiesta-camera.txt` | il modulo "Richiesta camera Leon d'Oro" da incollare in Contact Form 7 (campi, email, risposta automatica, messaggi) |
| `plugin/redirect-301.csv` | 18 regole di redirect dagli indirizzi del sito attuale, da importare nel plugin Redirection |
| `assets/web/` | le 29 immagini preparate per il sito (28 usate, `colli-alto.jpg` di riserva) e `ritagli.json` (sorgente, ritaglio, bilanciamento di ognuna) |
| `assets/originali/`, `assets/esterne/` | le immagini scaricate dal sito attuale, dal video "Emozioni & Sapori", dalla Regione Veneto e dal blog della cartolina; fuori dal repository, con `manifest.json` per riscaricarle |
| `screenshot/elementor/`, `screenshot/fallback/` | le 7 pagine dopo l'import in Elementor e nel fallback HTML, a 1440, 1024 e 390 px (21 + 21 file) |
| `screenshot/home/` | la home approvata (prototipo del giro 2, "l'oggetto") |
| `_sorgente/` | il generatore: `contenuti.py` (testi e pagine), `motore.py`, `build.py`, `prepara_immagini.py` |

## Vedere il sito subito

Senza installare niente: scarica il ramo `claude/benvegnu-sito` (su GitHub: *Code > Download ZIP*), scompatta e apri con doppio clic `LeonDoroEste-Sito/anteprima/index.html`. Le 7 pagine sono collegate tra loro e le immagini sono quelle della cartella `assets/web`, quindi funziona anche senza internet (serve solo Google Fonts per Libre Franklin; senza rete il testo esce in Arial).

Se preferisci un indirizzo `localhost`: apri un terminale nella cartella `LeonDoroEste-Sito` e lancia `python3 -m http.server 8000`, poi vai su http://localhost:8000/anteprima/

L'anteprima è la versione HTML (Formato B): a vista è uguale a quella Elementor, con una differenza. Al posto del modulo Contact Form 7, nella pagina Prenota c'è un bottone che apre un'email già indirizzata a prenotazioni@leondoroeste.it con le voci da compilare (date, persone, camera, trattamento). I link "Privacy" e "Cookie" del piede portano a pagine che il cliente deve ancora scrivere.

## Versioni e plugin

**Target dichiarato: Elementor 4.3.3, versione gratuita**, con WordPress 7.1 e tema Hello Elementor 3.5.1. Plugin gratuiti usati, tutti dal catalogo di WordPress.org:

| Plugin | Versione provata | A cosa serve | Obbligatorio? |
|---|---|---|---|
| Ultimate Addons for Elementor (slug `header-footer-elementor`) | 2.9.5 | testata e piede su tutto il sito senza Elementor Pro | **sì**, oppure si usano le pagine complete (vedi sotto) |
| Contact Form 7 | 6.1.7 | modulo "Richiesta camera Leon d'Oro" nella pagina Prenota | no: senza, al posto del modulo resta lo shortcode come testo |
| Redirection | 5.10.1 | redirect 301 dagli indirizzi del sito attuale | consigliato al momento della messa online |
| Honeypot for Contact Form 7 | non provato | campo nascosto contro lo spam, al posto di reCAPTCHA (che mette cookie di Google) | consigliato, da confermare con il cliente |

Il JSON è scritto nel modo più conservativo possibile:
- solo **contenitori flexbox** e **widget classici gratuiti**: Titolo, Testo, Immagine, HTML, Shortcode;
- nessun widget o chiave Pro, nessun elemento "atomico" della v4, nessun riferimento ai colori e font globali del kit (`__globals__`), nessuna animazione d'ingresso, nessun effetto di movimento;
- colori, font e misure scritti in chiaro su ogni elemento; quello che Elementor gratuito non sa scrivere (proporzioni delle foto, ritocchi solo per il telefono) sta in un widget HTML con il solo stile, alla fine di ogni sezione;
- il menu della testata è un widget HTML (markup, stile e poche righe di script), identico nel fallback: il widget di Ultimate Addons cambia solo a 767 o 1024 px e non può mettere il telefono e "Prenota" nel pannello del telefono;
- formato del file uguale a quello che Elementor produce con "Esporta template".

Su versioni 3.x recenti (dalla 3.16) dovrebbe funzionare, ma **non l'ho provato**: l'unica versione collaudata è la 4.3.3.

## Come importare (Formato A)

Prima di iniziare:
1. Accedi come **Amministratore** (gli altri ruoli non possono importare JSON, e senza il permesso "unfiltered_html" WordPress toglie stili e script dai widget HTML: il menu e i ritocchi delle sezioni smetterebbero di funzionare).
2. *Elementor > Impostazioni > Funzionalità*: **Contenitore = Attivo** (è il valore predefinito). Se è disattivato, l'import riesce ma la pagina resta **vuota, senza errori**.
3. Il sito deve poter scaricare file da Internet: le immagini arrivano durante l'import (vedi "Immagini").
4. Installa e attiva **Ultimate Addons for Elementor** e **Contact Form 7** (*Plugin > Aggiungi nuovo*).

### 1. Impostazioni del sito, prima di costruire
Il kit di Elementor nasce con Roboto e Roboto Slab. *Elementor > Impostazioni del sito > Tipografia globale*: Primario Libre Franklin 800, Secondario Libre Franklin 600, Testo Libre Franklin 400, Accento Libre Franklin 600. *Colori globali*: Verde `#263F40`, Giallo `#D3AB45`, Inchiostro `#1B201F`, Bianco `#FFFFFF`, Chiaro `#E4EAE9`, Grigio `#5A615F`. Poi *Elementor > Impostazioni > Avanzate > Carica i Google Fonts localmente*: **attivo**, così il sito non chiama Google senza il consenso. I miei elementi non dipendono dal kit, ma così i blocchi aggiunti a mano nascono coerenti.

### 2. Pagine e menu
1. *Pagine > Aggiungi pagina* per ognuna, con questo titolo e questo **slug** esatto (i link interni puntano a questi indirizzi):

| Titolo | Slug |
|---|---|
| Home | (pagina iniziale) |
| Camere | `camere` |
| Ristorante | `ristorante` |
| Bike hotel | `bike-hotel` |
| Per l'ospedale | `ospedale-schiavonia` (WordPress propone `per-lospedale`: va cambiato a mano) |
| Dove siamo | `dove-siamo` |
| Prenota | `prenota` |

2. *Impostazioni > Lettura > La homepage mostra: una pagina statica > Home*.
3. Le voci del menu della testata (camere, ristorante, bike hotel, per l'ospedale, dove siamo, più il bottone "Prenota") sono scritte nel widget HTML della testata, non nel menu di WordPress: per cambiarle si modifica quel widget, oppure `VOCI_MENU` in `_sorgente/contenuti.py` e si rigenera. Un menu "Menu principale" con le cinque pagine è comunque utile per il piede di altri temi e per la mappa del sito.

### 3. Modulo di contatto
*Contatto > Aggiungi nuovo*, titolo esatto **Richiesta camera Leon d'Oro**, poi copia nelle schede "Modulo", "Mail", "Mail (2)" e "Messaggi" il contenuto di `plugin/contact-form-7-richiesta-camera.txt`. La pagina Prenota richiama il modulo per titolo (`[contact-form-7 title="Richiesta camera Leon d'Oro"]`): se il titolo è diverso, il modulo non compare. Per consegnare davvero le email serve un plugin SMTP (per esempio WP Mail SMTP) configurato con la casella aziendale.

### 4. Testata e piede su tutto il sito (senza Pro)
1. *Template > Template salvati > Importa template*: importa `ldo-00-header.json` e `ldo-99-footer.json`. Se compaiono gli avvisi "i file JSON possono essere pericolosi" e "upload non filtrati", scegli **Continua** e poi **Importa senza abilitare**.
2. *UAE > Header & Footer > Create New*: titolo "Header", *Type of Template* **Header**, *Display On* **Entire Website**, pubblica; *Modifica con Elementor* > icona cartella > *I miei template* > inserisci "Leon d'Oro: Header". Salva.
3. Ripeti per il piede (*Type of Template* **Footer**, template "Leon d'Oro: Footer").

### 5. Le pagine
1. Importa le 7 pagine da `elementor-json/` (solo il corpo).
2. Apri ogni pagina con Elementor > icona cartella > *I miei template* > inserisci il template della pagina. Quando l'editor chiede se applicare le impostazioni della pagina, rispondi **Applica** (modello "Elementor a larghezza piena", titolo nascosto). Salva.

**Alternativa con Elementor Pro:** al punto 4 usa *Template > Theme Builder* (Header e Footer con condizione *Intero sito*) al posto di Ultimate Addons.

**Alternativa senza testata globale:** i file in `elementor-json/pagine-complete-senza-pro/` hanno testata e piede già dentro ogni pagina e modello *Canvas*. Funzionano, ma ogni modifica alla testata va ripetuta su 7 pagine.

### 6. Redirect dal sito attuale
Al momento della messa online: installa **Redirection**, *Strumenti > Redirection > Import/Export > Importa* e carica `plugin/redirect-301.csv`. Le 18 regole mandano con un 301 le 9 pagine italiane e le 7 inglesi del sito attuale alla pagina nuova corrispondente ("Cosa visitare" va a `/dove-siamo/#cosa-vedere`, l'informativa a `/cookie/`), e le vecchie cartelle `/foto/` e `/images/` alla home. Le pagine inglesi vanno all'italiano finché la versione inglese non c'è. Oggi rispondono sia `leondoroeste.it` sia `www.leondoroeste.it`: il redirect da uno all'altro si imposta dal pannello dell'hosting, non in Redirection.

## Immagini e testi alternativi

Ogni immagine nel JSON punta a un indirizzo pubblico su GitHub (`raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/LeonDoroEste-Sito/assets/web/...`). **Durante l'import Elementor scarica ogni immagine e la carica nella tua libreria media**: dopo l'import le immagini sono sul tuo sito e il link a GitHub non serve più. Il ramo GitHub deve però esistere al momento dell'import.

Ogni immagine ha un ID numerico fisso: reimportando lo stesso template Elementor riconosce le immagini già scaricate e **non crea doppioni**. Il rovescio: se rigeneri un'immagine **con lo stesso nome** e reimporti, Elementor riusa quella vecchia. Per aggiornare una foto, cancellala prima dalla libreria media (oppure sostituiscila lì).

**Testi alternativi:** Elementor li perde all'import. Vanno compilati nella libreria media, uno per immagine, dall'elenco pronto in `elementor-json/testi-alternativi-immagini.txt` (24 righe). Le foto con il titolo sopra (la facciata, la cartolina, i Colli, Este dall'alto) sono sfondi di contenitore: hanno accanto una descrizione per chi usa la sintesi vocale, scritta nella pagina e nascosta alla vista.

Se preferisci non dipendere da GitHub: carica la cartella `assets/web/` sul tuo server (per esempio in `wp-content/uploads/leondoro/`) e rigenera i file con
`python3 _sorgente/build.py --base https://TUO-DOMINIO/wp-content/uploads/leondoro/`

Nessuna foto è mostrata più grande del file, a nessuna larghezza da 390 a 2560 px: oltre 1680 px la facciata resta a 1680 con i lati nel nero della foto, i Colli, Este e le vigne si fermano a 1920, la cartolina a 2400, la padella a 1600, il salottino a 1024.

## Cosa potrebbe non reggere l'import (tieni pronto il fallback)

1. **Versione diversa da 4.3.3.** Su versioni 3.x vecchie (prima della 3.16) i contenitori non ci sono: il template risulta vuoto. Su versioni future un controllo che cambia nome **non dà errore**, viene solo ignorato.
2. **Contenitore disattivato** nelle funzionalità: pagina vuota senza avviso.
3. **Ultimate Addons non attivo**: testata e piede non compaiono. Usa le pagine complete.
4. **Immagini non scaricabili** (sito senza accesso a Internet, firewall, GitHub irraggiungibile): al loro posto compare il **riquadro grigio di Elementor**, senza errori. Controlla ogni pagina dopo l'import.
5. **Testi alternativi persi** all'import: vedi sopra.
6. **Utente senza "unfiltered_html"**: WordPress toglie `<style>` e `<script>` dai widget HTML. Si perdono il menu del telefono, le proporzioni delle foto con il titolo sopra e i ritocchi del telefono. Importa sempre da amministratore.
7. **Font**: se il kit resta in Roboto i miei elementi non cambiano (il font è scritto su ognuno), ma i blocchi nuovi sì. Con "Carica i Google Fonts localmente" spento, Libre Franklin arriva da Google: per il GDPR va acceso.
8. **Sfondi vuoti**: le sezioni con una foto di sfondo (facciata, cartolina, Colli, Este) hanno la classe `e-no-lazyload` sul contenitore esterno. Se la togli, Elementor carica lo sfondo solo quando la sezione entra nella finestra, e a volte resta vuoto. La prima sezione di ogni pagina ha l'ancora `content`: è il bersaglio del link "Vai al contenuto".
9. **Plugin di ottimizzazione** che rimandano o uniscono gli script in linea: escludi il widget HTML della testata e controlla il menu a 390 px. Senza JavaScript il menu non si rompe: le voci restano visibili in colonna sotto il logo.
10. **Larghezze della testata**: il menu si chiude nel bottone "Menu" da 900 px in giù e il telefono in testata compare da 1181 px (la specifica diceva 820 e 1100: misurata, la riga intera chiede 878 px senza il telefono e 1123 con il telefono). Se aggiungi una voce di menu, le due soglie vanno rifatte in `CSS_NAV` di `contenuti.py`.
11. **Stili del tema**: con un tema diverso da Hello Elementor, titoli e link possono ereditare margini o colori. Ho scritto colori espliciti per riposo, hover e fuoco su ogni link e bottone (Hello colora di rosa link e bottoni); il modulo Contact Form 7 ha il suo CSS in un widget HTML della pagina Prenota.
12. **Larghezze su mobile**: Elementor non eredita la larghezza mobile dei contenitori da quella tablet. L'ho scritta su tutti i breakpoint; se modifichi un blocco dall'editor, controlla anche tablet e telefono.
13. **Link interni** relativi (`/camere/`): funzionano se WordPress è nella radice del dominio. Altrimenti: `python3 _sorgente/build.py --url-sito https://www.leondoroeste.it`.
14. **Nessuna mappa incorporata**: la pagina Dove siamo ha il link "Apri in Google Maps" (coordinate del sito attuale). Una mappa incorporata metterebbe cookie di terzi prima del consenso.
15. **ID degli elementi**: Elementor li rigenera all'import. Non è un problema, ma non puoi riferirti agli ID del file.

Se un template non entra o arriva rotto, usa il Formato B per quella pagina.

## Come usare il Formato B (fallback HTML)

1. Crea la pagina e aprila con Elementor; nelle impostazioni pagina scegli il modello **Elementor Canvas**.
2. Per ogni file della cartella della pagina, nell'ordine (`00-header/01-header.html`, poi per esempio `03-ristorante/01-apertura.html`, `02-cucina.html` ... `05-prenota.html`, infine `99-footer/01-footer.html`): aggiungi un **contenitore a larghezza piena con padding 0 e spaziatura 0**, dentro un widget **HTML**, incolla il contenuto del file.
3. Ogni file è autosufficiente: carica il proprio font, ha il CSS con un prefisso unico (`.ldo-...`) che non tocca il resto del sito e resiste agli stili del tema.

Differenze rispetto al Formato A: i testi si modificano solo nel codice; al posto del modulo Contact Form 7 c'è il bottone che apre un'email già impostata. Le immagini puntano all'indirizzo GitHub: per la pubblicazione definitiva conviene rigenerare con `--base` verso le immagini caricate sul tuo sito.

## Collaudo fatto

WordPress 7.1.3 in locale (italiano, SQLite), Elementor 4.3.3, Hello Elementor 3.5.1, Ultimate Addons 2.9.5, Contact Form 7 6.1.7, Redirection 5.10.1, PHP 8.3.6. Nel WordPress di prova il kit di Elementor è in Libre Franklin e i Google Fonts sono caricati in locale.
- **Import** dei 9 template con la stessa funzione del pulsante *Importa template*, libreria media svuotata prima: tutti entrati, **281 elementi salvati uguali a quelli dei file**, 29 immagini scaricate (28 diverse), nessun riquadro grigio. Nella prova le immagini arrivavano dal server locale, non da GitHub: l'import con le immagini da GitHub non è stato provato su questo sito.
- **Pagine** create inserendo i template, testata e piede globali con Ultimate Addons.
- **Controllo automatico** (scorrimento orizzontale, immagini rotte o ingrandite, elementi che escono a destra, link interni verso pagine inesistenti, trattini lunghi) su 7 pagine x 2 versioni (Elementor e fallback) x 4 larghezze (390, 768, 1024, 1440): **nessun problema**. I link a `/privacy/` e `/cookie/` sono le sole pagine mancanti, e sono del cliente.
- **Scala delle foto** misurata su tutte le pagine a 8 larghezze (390, 768, 820, 1024, 1280, 1440, 1920, 2560), anche per gli sfondi: nessuna foto oltre 1,00. Il salottino a 1920 px diventava 1,09: ora si ferma alla misura del file.
- **Testata**: menu su una riga a tutte le 12 larghezze provate da 390 a 1920 px, mai pezzi tagliati; a 390 il bottone "Menu" apre il pannello bianco che copre la pagina, il fuoco resta nel pannello, Esc e il clic fuori lo chiudono, `aria-expanded` segue; senza JavaScript le voci restano visibili in colonna; "Vai al contenuto" compare al primo Tab, uno solo in tutte e due le versioni; voce attiva sottolineata nelle cinque pagine del menu.
- **Segnali da IA** (`segnali.sh` della guida `_metodo/CARATTERI-E-SEGNALI-IA.md`, pagina a 1440, uguale su anteprima e WordPress):

| Pagina | Foto | Misure di H2 | Fasce di fondo | Filetti | Soglie bloccanti non passate | Da guardare |
|---|---|---|---|---|---|---|
| Home | 58 % | 3 (36, 40, 44) | 3 | 0 | nessuna | nessuna |
| Camere | 35,4 % | 3 | 3 | 4 (il listino, l'unica tabella del sito: 4 righe) | nessuna | nessuna |
| Ristorante | 35,5 % | 3 | 3 | 0 | nessuna | data: c'è un nome, "la signora Annalisa Brugin" |
| Bike hotel | 45,7 % | 2 | 3 | 0 | nessuna | H2, data: c'è un nome, "Team Este Bike" |
| Per l'ospedale | 19,1 % | 1 | 3 | 0 | foto | H2 |
| Dove siamo | 42,7 % | 2 | 3 | 0 | nessuna | H2 |
| Prenota | 6 % (4 % con il modulo) | 2 | 4 | 0 | foto | H2, data |

  In tutte: Libre Franklin 100 %, monospazio 0, etichette sopra i titoli 0, titoli col punto 0, titolo a sinistra e paragrafo a destra 0, frecce 0, numeri grandi 0, numerazioni 0, didascalie 0, divieti 0. Perché le righe "da guardare" e le due soglie non passate restano così: Per l'ospedale e Prenota sono pagine di servizio (come arrivare, il modulo) e la specifica le prevede sotto il 35 % di foto; le pagine interne hanno un titolo grande (h1 a 72 px) e pochi H2 per scelta, uno per momento della pagina; in Prenota la quarta fascia è il campo giallo grande che contiene il modulo. Ogni screenshot è stato guardato a pezzi: nessuna parola in corsivo o in colore, nessun badge, nessun box con icona, nessun hero con due bottoni, nessuna didascalia, nessuna foto di piatto fatta col telefono.
- **Elementor e fallback** confrontati pixel per pixel alle tre larghezze: differenze solo di 1 px e di antialiasing, salvo il modulo di Prenota (voluta).
- **Modulo** Contact Form 7 creato dal file in `plugin/` (destinatario di prova `prova@example.com`, non l'indirizzo dell'albergo), con la risposta automatica a chi scrive; mostrato nella pagina Prenota. Nessuna email è stata inviata.
- **Redirect**: le 18 regole importate in Redirection, verificato il 301 su 7 indirizzi vecchi (`/index.html`, camere, ospedale, cosa visitare, una pagina inglese, una foto in `/foto/`, l'informativa).
- **Anteprima da file** (`file://`, senza server): 7 pagine, tutte le immagini e gli sfondi caricati, tutti i link tra le pagine esistono, voce attiva del menu giusta.

### Scelte diverse dalla specifica, con la ragione
- **Menu** come widget HTML e non come Navigation Menu di Ultimate Addons (vedi "Versioni e plugin"); soglie della testata a 900 e 1181 px (punto 10 sopra).
- **Ristorante**: la carta di ogni giorno è in due colonne al centro (antipasti e primi, secondi e contorni) e non in tre: quattro antipasti accanto a diciotto secondi lasciavano un buco. La sala del venerdì è a destra, con il titolo accanto in basso, e la carta del pesce sotto in tre colonne. Nella foto della sala il cameriere, tagliato alla testa dal fotogramma, resta fuori (ritaglio fino a 1080 px).
- **Bike hotel**: la maglia gialla e nera non c'è. Il fotogramma è sfocato, la mano copre la L di Leon e "(Padova)" finisce sotto il marchio del video. Al suo posto i due ciclisti con la maglia del Leon d'Oro sulla strada alberata con la torre. Il titolo del campo giallo è "Camera e garage" (tre parole: l'800 maiuscolo regge solo titoli brevi).
- **Dove siamo**: prima di "Intorno" i Colli dal drone con il borgo e i vigneti (dal video del cliente); il titolo del campo giallo è "L'insegna col leone" (tre parole invece di quattro). La frase sull'ufficio IAT dice quello che dice il sito attuale (informazioni sui luoghi e sui prodotti, come la Ceramica Estense) e gli opuscoli li dà l'albergo (testo 35).

## Da confermare con il cliente prima di pubblicare

Nel sito di prova compaiono, segnati qui perché possono essere superati:
1. **CIN** IT028037A1GWJ7NDDS nel piede (dalla Regione Veneto): attualità e obbligo di indicarlo sul sito proprio (art. 13-ter del D.L. 145/2023), da chiedere al consulente.
2. **Team Este Bike**: la collaborazione e le uscite sono ancora attive? Ritrovo in piazza alle 8.30 d'estate e alle 9 d'inverno (home, bike hotel).
3. **Navetta per l'ospedale** dalla stazione delle corriere di Este, 4,80 € andata e ritorno (dato del 2022; il PDF degli orari non esiste più); **Taxi Este** 339 5040502; **centralino** dell'ospedale 0429 714111.
4. **La signora Annalisa Brugin** in cucina (fonte: Regione Veneto e blog Micro Storie del Commercio, 2015).
5. **Menù di pesce**: la grafia di "granseola o granzoporro" (il sito scrive "GRANSIPORO") e la lettura di "BACCALA :VICENTINA, INSALATA" (scritto "Baccalà alla vicentina o in insalata").
6. **Il dettaglio della tavola** in home: sono salumi interi; se sono sopresse, l'alt va scritto "sopresse".
7. **Cartolina d'epoca** della Trattoria al Leon d'Oro: è la riproduzione pubblicata dal blog Micro Storie del Commercio (2015). Serve l'originale del cliente, a risoluzione più alta.
8. **Fotogrammi del video "Emozioni & Sapori"**: permesso scritto di NEON produzione immagini, e il consenso delle persone riprese (la coppia in sala, le persone davanti alla porta, i ciclisti).
9. **Logo vettoriale**: quello del sito è ricavato da un'immagine di 311 x 231 px (il leone a tratto e la scritta, estratti dalla foto della torre).
10. **Il colore del muro**: il giallo `#D3AB45` è misurato in ombra su una foto; va confrontato con la facciata vera.

Non sono nel sito di prova perché non sono pubblicati da nessuna parte; servono per completarlo:
11. **PEC** (non trovata in chiaro): va nel piede quando c'è.
12. Pagine **Privacy** e **Cookie** (linkate nel piede e nel consenso del modulo), con il testo del consulente del cliente; titolare del trattamento la società. Banner dei cookie con "Accetta" e "Rifiuta" allo stesso livello.
13. **Versione inglese** (il link "English" è tolto finché non c'è; i redirect `en_*` vanno spostati quando arriva).
14. **Listino**: il prezzo è a notte? La tassa di soggiorno è compresa? Il sito dice solo "stagione unica".
15. **Camere**: orari della colazione, di arrivo e di partenza; animali (la Regione dice di no); lingue parlate; parcheggio gratuito (lo dice Google, non il sito).
16. **Ristorante**: giorni e orari di pranzo e cena; prezzi dei piatti e del menù.
17. **Per l'ospedale**: la tariffa per chi assiste un ricoverato ("prezzi unici e servizi riservati" sul sito attuale) e la distanza in km e in minuti.
18. **Dove siamo**: uscita autostradale consigliata, distanza dalla stazione dei treni; indirizzo dell'ufficio IAT (il link del sito attuale non funziona).
19. **Bici**: il percorso dell'Atestina Superbike (il sito ufficiale non esiste più) e le tracce GPX da scaricare; un profilo altimetrico si mette solo con un tracciato vero.
20. **Generazioni e anno**: il sito dice quarta generazione, la Regione e il blog terza; nessun anno preciso di apertura. Il nuovo sito dice solo "dai primi del Novecento" e "dagli anni Cinquanta della famiglia Rubini".
21. **Modulo**: destinatario `prenotazioni@leondoroeste.it`, plugin SMTP con la casella aziendale, Honeypot contro lo spam. La richiesta non conferma la prenotazione: la conferma la dà una persona.

## Foto da fare (brief breve)

Oggi il sito regge su 9 foto professionali del 2021 (fino a 1200 px) e sui fotogrammi del video del cliente (fino a 1920 px, morbidi). Le prime da rifare sono quelle che aprono le pagine:
1. **Facciata all'ora blu**, almeno 2400 px di lato lungo, cavalletto: il muro acceso, la scritta "Albergo ★★ Leon d'Oro" leggibile per intero (oggi "d'Oro" è sempre dietro le foglie: serve un punto dove l'albero non la copre), l'insegna nera col leone accesa, la porta aperta, nessuna auto davanti. Un'inquadratura orizzontale con cielo e alberi a destra (lì va il titolo) e una verticale per il telefono.
2. **La targa ALBERGO** con la chiave e le due stelle, foto ferma con luce del giorno radente, almeno 1600 px: oggi è un fotogramma (home e Prenota).
3. **Sala apparecchiata con le tovaglie gialle**, di sera, senza bottiglie di plastica né piatti in tavola, dalla stessa posizione della foto del 2021; e un dettaglio della tavola (vino dei Colli, pane, un salume).
4. **Un piatto**: baccalà con polenta sulla tovaglia gialla, luce naturale da una finestra, niente flash, piatto bianco, almeno 2400 px. Le foto dei piatti del sito attuale sono fatte col telefono e col flash: nel nuovo sito non ci sono.
5. **La cucina con il cuoco al lavoro** (la padella sul fuoco del video è il gesto giusto, va rifatto fermo e nitido).
6. **Una camera** rifatta di recente, luce del giorno, almeno 2000 px; e gli originali del servizio del 2021 (la fotocamera scatta 5760 x 3840).
7. **Il garage con le bici** e **la colazione apparecchiata**: oggi sono solo parole.
8. **La maglia gialla e nera** del Leon d'Oro, foto ferma: la pagina bike hotel la voleva al centro, sola, come la targa in home.

Le foto vanno a colori come sono, senza viraggi: il giallo delle tovaglie e del muro è già il colore della casa. Quando arrivano, si sostituiscono in `prepara_immagini.py` (ritaglio e bilanciamento per ogni file) senza toccare l'impaginazione.

## Rigenerare i file

Serve Python 3 con Pillow (`pip install pillow`).
```
python3 -I _sorgente/prepara_immagini.py     # rifà assets/web/ dalle immagini originali (servono assets/originali e assets/esterne)
python3 _sorgente/build.py                   # rifà elementor-json/, html-fallback/, anteprima/
```
Opzioni di `build.py`: `--base URL` (dove sono le immagini), `--url-sito URL` (link interni assoluti), `--out CARTELLA`.
I testi si cambiano in `_sorgente/contenuti.py`: i dati aziendali e il listino (`LISTINO`, un punto solo, che alimenta la home, le camere, il bike hotel e la pagina dell'ospedale) sono in cima al file. Il build si ferma se trova un trattino lungo, una parola dell'elenco `PAROLE_VIETATE` di `build.py`, un valore di stile non valido, un'immagine senza testo alternativo o un link dentro un blocco già cliccabile. `plugin/redirect-301.csv` è scritto a mano dall'elenco degli indirizzi vecchi di `01-analisi-sito-attuale.md`.
