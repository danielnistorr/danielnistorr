# Gardens Pav S.r.l.: nuovo sito per WordPress + Elementor

Sito completo in 7 pagine (Home, Vasche, Depurazione, Piattaforme per autolavaggi, Realizzazioni, Azienda, Contatti) più testata e piede, in due formati:
- **Formato A (primario):** template Elementor `.json` da importare con *Template > Template salvati > Importa template*.
- **Formato B (fallback):** la stessa pagina in HTML+CSS autosufficiente, una sezione per file, da incollare in un widget HTML di Elementor.

Tutti i file sono stati **importati e provati davvero** su un WordPress di prova (vedi "Collaudo fatto"). Le immagini delle pagine sono in `screenshot/`.

Direzione grafica "La misura": la disciplina dei cataloghi tecnici di Escofet e Rieder (un grottesco pieno, Archivo; un monospazio per i dati, IBM Plex Mono; filetti sottili; foto vere a dimensione nativa), il bianco, il grigio calcestruzzo `#EBECEB` dei render e una sola fascia grafite per pagina. L'arancio del logo compare solo dove ha già un significato: le quote, il pulsante, la vasca scelta. Il segno che lega tutte le pagine è il **capo di sezione** con le stanghette di una quota, preso dai disegni quotati dell'azienda. Riferimenti e motivi delle scelte in `02-competitor-e-riferimenti.md`, mappa delle pagine in `03-mappa-pagine.md`.

## Cosa c'è nella cartella

| Cartella / file | Contenuto |
|---|---|
| `01-analisi-sito-attuale.md` | pagine, testi reali, immagini, problemi misurati e dati aziendali del sito attuale |
| `02-competitor-e-riferimenti.md` | concorrenti, riferimenti premium, cosa si riprende da ognuno, accoppiate di caratteri e colori |
| `03-mappa-pagine.md` | le 7 pagine, le sezioni di ogni pagina, la navigazione |
| `elementor-json/` | **Formato A**: `gpv-00-header.json`, `gpv-99-footer.json` (tipo *sezione*) e le 7 pagine `gpv-01-home.json` ... `gpv-07-contatti.json` (tipo *pagina*, solo il corpo) |
| `elementor-json/pagine-complete-senza-pro/` | le stesse 7 pagine con testata e piede già dentro e modello *Canvas* |
| `elementor-json/testi-alternativi-immagini.txt` | i testi alternativi delle 81 immagini, da incollare nella libreria media (Elementor li perde all'import) |
| `html-fallback/` | **Formato B**: una cartella per pagina, un file `.html` per sezione, più `00-header/` e `99-footer/` |
| `anteprima/` | le 7 pagine complete in HTML, da aprire nel browser: doppio clic su `anteprima/index.html` |
| `plugin/contact-form-7-richiesta-informazioni.txt` | il modulo "Richiesta informazioni" da incollare in Contact Form 7 (campi ed email) |
| `plugin/redirect-301.csv` | 74 regole di redirect dal sito attuale, da importare nel plugin Redirection |
| `assets/web/` | le 81 immagini preparate per il sito (foto, render, disegni, campioni di colore, copertine dei 36 cantieri, loghi) |
| `assets/originali/` | le immagini scaricate dal sito attuale, con `manifest.json` (fuori dal repository: si riscaricano dalle fonti del manifest) |
| `screenshot/` | le pagine dopo l'import in Elementor (`elementor/`) e il fallback HTML (`fallback/`), a 1440, 1024 e 390 px |
| `_sorgente/` | il generatore: `contenuti.py` (testi e pagine), `motore.py`, `build.py`, `prepara_immagini.py`, `redirect.py`, e in `dati/` le tabelle ripulite delle schede, i 36 cantieri e le due mappe SVG |

## Vedere il sito subito

Senza installare niente: scarica il ramo (su GitHub: *Code > Download ZIP*), scompatta e apri con doppio clic `GardensPav-Sito/anteprima/index.html`. Le 7 pagine sono collegate tra loro e le immagini sono quelle della cartella `assets/web`, quindi funziona anche senza internet (servono solo i font Google e, se la si chiede, la mappa di Google).

Se preferisci un indirizzo `localhost`: apri un terminale nella cartella `GardensPav-Sito` e lancia `python3 -m http.server 8000`, poi vai su http://localhost:8000/anteprima/

L'anteprima è la versione HTML (Formato B): a vista è uguale a quella Elementor, con due differenze. Al posto del modulo Contact Form 7 c'è un pulsante che apre un'email già impostata con le voci della richiesta; il menu su telefono è un elenco a scomparsa senza JavaScript invece della tendina di Ultimate Addons. I link a `/privacy/` e `/cookie/` non funzionano nell'anteprima: sono pagine che scrive il cliente.

## Versioni e plugin

**Target dichiarato: Elementor 4.3.3, versione gratuita**, con WordPress 7.1.3 e tema Hello Elementor 3.5.1. Plugin gratuiti usati, tutti dal catalogo di WordPress.org:

| Plugin | Versione provata | A cosa serve | Obbligatorio? |
|---|---|---|---|
| Ultimate Addons for Elementor (slug `header-footer-elementor`) | 2.9.5 | testata e piede su tutto il sito senza Elementor Pro; widget "Navigation Menu" con menu a scomparsa su tablet e telefono | **sì**: il menu della testata è un suo widget |
| Contact Form 7 | 6.1.7 | modulo "Richiesta informazioni" nella pagina Contatti | no: senza, al posto del modulo resta lo shortcode come testo |
| Redirection | 5.10.1 | redirect 301 dagli indirizzi del sito attuale | consigliato al momento della messa online |
| WP Mail SMTP (o simile) | non provato | consegna delle email del modulo dalla casella aziendale | sì, se si usa il modulo |

Il JSON è scritto nel modo più conservativo possibile:
- solo **contenitori flexbox** e **widget classici gratuiti**: Titolo, Testo, Immagine, Pulsante, HTML, Shortcode, più "Navigation Menu" di Ultimate Addons;
- nessun widget o chiave Pro, nessun elemento "atomico" della v4, nessun riferimento ai colori e font globali del kit (`__globals__`), nessuna animazione;
- colori, font e misure scritti in chiaro su ogni elemento;
- formato del file uguale a quello che Elementor produce con "Esporta template" (`content`, `page_settings`, `version: "0.4"`, `title`, `type`).

Su versioni 3.x recenti (dalla 3.16, quando i contenitori sono diventati stabili) dovrebbe funzionare, ma **non l'ho provato**: l'unica versione collaudata è la 4.3.3.

## Come importare (Formato A)

Prima di iniziare:
1. Accedi come **Amministratore** (gli altri ruoli non possono importare JSON, e senza il permesso "unfiltered_html" WordPress ripulisce stili, script e SVG dei widget HTML).
2. *Elementor > Impostazioni > Funzionalità*: **Contenitore = Attivo** (è il valore predefinito dalla 3.16). Se è disattivato, l'import riesce ma la pagina resta **vuota, senza errori**.
3. Il sito deve poter scaricare file da Internet: le immagini arrivano durante l'import (vedi "Immagini e testi alternativi").
4. Installa e attiva **Ultimate Addons for Elementor** e **Contact Form 7** (*Plugin > Aggiungi nuovo*).

### 1. Pagine e menu
1. *Pagine > Aggiungi pagina* per ognuna: Home, Vasche, Depurazione, Piattaforme per autolavaggi, Realizzazioni, Azienda, Contatti, con **slug** esatto `vasche`, `depurazione`, `piattaforme-autolavaggi`, `realizzazioni`, `azienda`, `contatti`. I link interni e le ancore (`/vasche/#circolari`, `/realizzazioni/#altivole` ...) puntano a questi indirizzi.
2. *Aspetto > Menu*: crea un menu chiamato **Menu principale** con le 6 pagine in quest'ordine: Vasche, Depurazione, Piattaforme per autolavaggi, Realizzazioni, Azienda, Contatti. Il widget del menu nella testata cerca questo menu; se lo chiami diversamente, dopo l'import aprilo nell'editor e scegli il menu giusto dal campo "Menu".
3. *Impostazioni > Lettura > La homepage mostra: una pagina statica > Home*.
4. Crea anche le pagine **Privacy** (`/privacy/`) e **Cookie** (`/cookie/`) con il testo del cliente: il piede, il modulo e i redirect le richiamano.

### 2. Modulo di contatto
*Contatto > Aggiungi nuovo*, titolo esatto **Richiesta informazioni**, poi incolla nelle schede "Modulo" e "Mail" il contenuto di `plugin/contact-form-7-richiesta-informazioni.txt` (destinatario `info@gardenspav.it`, allegato `[progetto]` nel campo "Allegati file"). La pagina Contatti richiama il modulo per titolo (`[contact-form-7 title="Richiesta informazioni"]`): se il titolo è diverso, il modulo non compare. L'aspetto del modulo (due colonne di campi, angoli vivi, pulsante arancio) sta in un piccolo CSS dentro la pagina.

### 3. Testata e piede su tutto il sito (senza Pro)
1. *Template > Template salvati > Importa template*: importa `gpv-00-header.json` e `gpv-99-footer.json`. Se compaiono gli avvisi "i file JSON possono essere pericolosi" e "upload non filtrati", scegli **Continua** e poi **Importa senza abilitare**.
2. *UAE > Header & Footer > Create New*: titolo "Header", *Type of Template* **Header**, *Display On* **Entire Website**, pubblica; *Modifica con Elementor* > icona cartella > *I miei template* > inserisci "Gardens Pav: Header". Salva.
3. Ripeti per il piede (*Type of Template* **Footer**, template "Gardens Pav: Footer").

### 4. Le pagine
1. Importa le 7 pagine da `elementor-json/` (solo il corpo).
2. Apri ogni pagina con Elementor > icona cartella > *I miei template* > inserisci il template della pagina. Quando l'editor chiede se applicare le impostazioni della pagina, rispondi **Applica** (modello "Elementor a larghezza piena", titolo nascosto). Salva.

**Alternativa con Elementor Pro:** al punto 3 usa *Template > Theme Builder* (Header e Footer con condizione *Intero sito*) al posto di Ultimate Addons. Il widget del menu resta quello di Ultimate Addons, quindi il plugin serve comunque.

**Alternativa senza testata globale:** i file in `elementor-json/pagine-complete-senza-pro/` hanno testata e piede già dentro ogni pagina e modello *Canvas*. Funzionano, ma ogni modifica alla testata va ripetuta su 7 pagine.

### 5. Redirect dal sito attuale
Al momento della messa online: installa **Redirection**, *Strumenti > Redirection > Import/Export > Importa* e carica `plugin/redirect-301.csv`. Le 74 regole mandano con un 301 tutti gli 82 indirizzi italiani del sito attuale alla pagina nuova e, dove c'era una scheda, alla sua ancora (le 7 schede di depurazione, gli 8 modelli di piattaforma, i 36 cantieri). Restano uguali solo `/` e `/contatti/`. Nessuna regola colpisce un indirizzo del sito nuovo, quindi non ci sono redirect in loop.
I sottodomini `eng.`, `deu.` e `fra.gardenspav.it` (pagine in inglese, e in tedesco e francese ancora in italiano) vanno reindirizzati alla home a livello di DNS o di server: vedi "Da confermare".

## Immagini e testi alternativi

Ogni immagine nel JSON punta a un indirizzo pubblico su GitHub (`raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/GardensPav-Sito/assets/web/...`). **Durante l'import Elementor scarica ogni immagine e la carica nella tua libreria media**: dopo l'import le immagini sono sul tuo sito. Il ramo GitHub deve però esistere al momento dell'import.

Ogni immagine ha un ID numerico fisso: reimportando lo stesso template Elementor riconosce le immagini già scaricate e **non crea doppioni**. Il rovescio: se rigeneri un'immagine **con lo stesso nome** e reimporti, Elementor riusa quella vecchia già in libreria. Per aggiornare una foto, cancellala prima dalla libreria media (oppure sostituiscila lì).

Se preferisci non dipendere da GitHub: carica la cartella `assets/web/` sul tuo server (per esempio in `wp-content/uploads/gardenspav/`) e rigenera i file con
`python3 _sorgente/build.py --base https://TUO-DOMINIO/wp-content/uploads/gardenspav/`

Le 81 immagini di `assets/web/` sono tutte dell'azienda, prese dal sito attuale, mai ingrandite oltre la loro misura (`prepara_immagini.py`): foto a colori fino a 1.600 px; render ritagliati sul pezzo e, dove stanno su una fascia grigia, portati a `#EBECEB` nel file; i disegni in pianta delle piattaforme e l'esempio di posa copiati tali e quali; i quattro campioni di colore ritagliati dalle piante colorate; 36 copertine 4:3 dei cantieri al massimo di 1.000 px.
A 1440 px quasi tutte le foto sono a 2x o più (nitide anche su schermi retina). Sotto 2x, quindi nitide su schermo normale e un po' morbide su retina: il render della vasca 550 (1,44x), il render della vasca circolare (1,7x), i render delle sette schede di Depurazione (da 1,7x a 2x), il disegno della pista self 500 doppia griglia (1,5x), l'esempio di posa (1,1x), alcune copertine dei cantieri che sul sito attuale sono a 800 px (da 1,9x).

**Testo alternativo**: Elementor lo perde all'import. Va compilato nella libreria media, l'elenco è pronto in `elementor-json/testi-alternativi-immagini.txt`. Le mappe sono SVG dentro widget HTML e hanno già titolo e descrizione.

## Cosa potrebbe non reggere l'import (tieni pronto il fallback)

1. **Versione diversa da 4.3.3.** Su versioni 3.x vecchie (prima della 3.16) i contenitori non ci sono: il template risulta vuoto. Su versioni future qualche controllo può cambiare nome: un nome sconosciuto **non dà errore**, viene solo ignorato.
2. **Contenitore disattivato** nelle funzionalità: pagina vuota senza avviso.
3. **Ultimate Addons non attivo**: il widget del menu sparisce dalla testata senza errori; logo, "Chiama", telefono e "Richiedi informazioni" restano.
4. **Immagini non scaricabili** (sito senza accesso a Internet, firewall, GitHub irraggiungibile, timeout): al loro posto compare il **riquadro grigio di Elementor**, senza errori. Controlla ogni pagina dopo l'import.
5. **Utente senza "unfiltered_html"**: WordPress toglie dai widget HTML gli script e gli SVG. Si perderebbero la gamma delle vasche in scala (resta la tabella), le schede a tab di Depurazione (restano le due tabelle una sotto l'altra), le frecce della striscia dei cantieri, le due mappe e la mappa di Google al clic. Importa sempre come Amministratore.
6. **Script in linea.** Gamma delle vasche, schede a tab, striscia dei cantieri, mappa dei cantieri e mappa di Google stanno ognuno in un widget HTML con il suo piccolo script, senza librerie. Se un plugin di ottimizzazione rimanda o unisce gli script in linea, escludi quei widget e riprova: ogni pezzo è fatto per funzionare anche senza JavaScript (la gamma resta ferma sulla 1050, le tabelle restano visibili, la striscia scorre a mano, la mappa resta statica, il riquadro di Google sparisce e resta il link "Apri in Google Maps").
7. **Lightbox delle Realizzazioni.** Le 36 copertine aprono la foto nella lightbox gratuita di Elementor (*Impostazioni del sito > Lightbox* attiva, è il valore predefinito). Il link della lightbox punta allo stesso indirizzo da cui è stata importata l'immagine: se rigeneri con `--base` verso il tuo server, punta lì; altrimenti in Elementor cambia il link di ogni immagine in "File multimediale".
8. **Font**: Archivo e IBM Plex Mono sono caricati da Google Fonts da Elementor. Per il GDPR conviene attivare *Elementor > Impostazioni > Avanzate > Carica i Google Fonts localmente*; dopo, controlla che le etichette in monospazio siano ancora in IBM Plex Mono.
9. **Stili del tema**: con un tema diverso da Hello Elementor, titoli, pulsanti e tabelle possono ereditare margini o colori del tema. Colori espliciti ovunque; tabelle, modulo, menu e componenti dinamici hanno un CSS dedicato con il prefisso `gpv-`.
10. **Kit globale**: i miei elementi non usano i colori e i font globali. Conviene comunque impostare in *Impostazioni del sito* i colori Grafite `#1D1E1F`, Bianco `#FFFFFF`, Calcestruzzo `#EBECEB`, Testo secondario `#58585A`, Arancio scuro `#A6470A` (link), Arancio `#F38239` (pulsanti, mai per testo su fondo chiaro) e i font Archivo e IBM Plex Mono, così i nuovi elementi aggiunti a mano nascono coerenti.
11. **Larghezze su mobile**: Elementor non eredita la larghezza mobile dei contenitori da quella tablet. L'ho scritta esplicitamente su tutti i breakpoint; se modifichi un blocco dall'editor, controlla anche le viste tablet e mobile.
12. **Sezioni a filo pagina** (Vasche e Piattaforme in apertura, Dove siamo in Contatti, la striscia dei cantieri): sono contenitori a larghezza piena con un piccolo CSS che riallinea il testo alla griglia da 1280 px. Se nell'editor cambi la larghezza del contenitore in "In box", la foto smette di toccare il bordo.
13. **Link interni** relativi (`/vasche/`): funzionano se WordPress è nella radice del dominio. Se è in una sottocartella o vuoi link assoluti: `python3 _sorgente/build.py --url-sito https://www.gardenspav.it`.
14. **Mappa di Google** nella pagina Contatti: si carica solo quando il visitatore preme "Mostra la mappa di Google" (prima non parte nessuna richiesta a Google). Va comunque citata nell'informativa cookie.
15. **Allegati del modulo**: il campo "Disegno o progetto" accetta pdf, jpg, png e dwg fino a 10 MB; serve la cartella `wp-content/uploads` scrivibile e l'allegato `[progetto]` impostato nella scheda Mail.

Se un template non entra o arriva rotto, usa il Formato B per quella pagina.

## Come usare il Formato B (fallback HTML)

1. Crea la pagina e aprila con Elementor; nelle impostazioni pagina scegli il modello **Elementor Canvas**.
2. Per ogni file della cartella della pagina, nell'ordine (`00-header/01-header.html`, poi `02-vasche/01-apertura.html`, `02-rettangolari.html`..., infine `99-footer/01-footer.html`): aggiungi un **contenitore a larghezza piena con padding 0 e spaziatura 0**, dentro un widget **HTML**, incolla il contenuto del file.
3. Ogni file è autosufficiente: carica i propri font, ha il CSS con un prefisso unico (`.gpv-vasche-rettangolari` ecc.) che non tocca il resto del sito e resiste agli stili del tema. I componenti comuni (tabelle, righe-link, capo di sezione) sono nel file della testata: incollala sempre.

Differenze rispetto al Formato A: i testi si modificano solo nel codice; il menu su telefono è un elenco a scomparsa senza JavaScript; al posto del modulo Contact Form 7 c'è un pulsante che apre un'email già impostata con le voci della richiesta; le copertine dei cantieri aprono il file della foto invece della lightbox. Le immagini puntano all'indirizzo GitHub: per la pubblicazione definitiva conviene rigenerare con `--base` verso le immagini caricate sul tuo sito.

## Collaudo fatto

WordPress 7.1.3 in locale (italiano), Elementor 4.3.3, Hello Elementor 3.5.1, Ultimate Addons 2.9.5, Contact Form 7 6.1.7, Redirection 5.10.1, PHP 8.3, il 6 ottobre 2026.
- Import dei 9 template con la stessa funzione del pulsante *Importa template* (`Source_Local::import_template`), libreria media svuotata prima: tutti entrati, **1317 elementi salvati su 1317**, **94 immagini su 94 scaricate**, nessun riquadro grigio.
- Testata e piede globali creati con Ultimate Addons dai template importati; menu "Menu principale" con 6 voci; voce attiva evidenziata su ogni pagina; menu orizzontale su desktop, a scomparsa su tablet e telefono, si chiude anche con Esc.
- Modulo Contact Form 7 creato dal file in `plugin/` (destinatario di prova, non quello dell'azienda) e mostrato nella pagina Contatti.
- Controllo automatico a **390, 768, 1024 e 1440 px**, Elementor e fallback, su tutte le 7 pagine: nessuno scorrimento orizzontale, nessuna immagine rotta o non caricata, **nessuna immagine ingrandita oltre la sua misura**, nessun link interno verso pagine inesistenti (a parte `/privacy/` e `/cookie/`), nessun trattino lungo. Ogni ancora usata dai link (`#rettangolari`, `#mod-450`, `#altivole` ...) esiste nella pagina di arrivo.
- Altezze delle pagine (Elementor; il fallback differisce di 0-2 px, tranne Contatti dove al posto del modulo c'è il pulsante email):

| Pagina | 1440 | 1024 | 390 |
|---|---|---|---|
| Home | 6.927 | 6.812 | 9.644 |
| Vasche | 4.986 | 5.271 | 7.391 |
| Depurazione | 8.936 | 8.582 | 12.512 |
| Piattaforme per autolavaggi | 8.300 | 8.803 | 12.056 |
| Realizzazioni | 7.565 | 8.638 | 8.748 |
| Azienda | 4.247 | 4.138 | 6.072 |
| Contatti | 2.554 (fallback 2.172) | 2.990 (2.630) | 4.188 (3.220) |

- Elementi dinamici provati a 1440 e 390 px, in Elementor e nel fallback: un clic sulla vasca 550 della gamma aggiorna la misura grande e sposta l'evidenziazione sulla riga 550 della tabella, la freccia destra passa alla 650; le schede "Acque superficiali" / "Laguna di Venezia" si scambiano col clic e con le frecce; la freccia della striscia dei cantieri sposta di una scheda (432 px a 1440, 314 a 390) e accende la freccia indietro; il fuoco su "Aosta" nell'elenco accende il punto e la linea sulla mappa; "Mostra la mappa di Google" crea la mappa solo al clic; il `<details>` delle 15 misure si apre.
- Con JavaScript spento: le due tabelle a schede si vedono una sotto l'altra col loro titolo, le frecce della striscia e il riquadro di Google spariscono, la gamma resta ferma sulla 1050 con la riga "IN FOTO" evidenziata.
- Redirect: le 74 regole importate in Redirection; gli 82 indirizzi italiani del sito attuale rispondono 301 verso la pagina o l'ancora giusta, tranne `/` e `/contatti/` che restano uguali (200).
- Anteprima aperta da file (`file://`, senza rete): 7 pagine, tutte le immagini caricate dalla cartella `assets/web`, tutti i link tra le pagine verso file esistenti.
- Pagine fotografate a 1440, 1024 e 390 px e guardate a pezzi: `screenshot/elementor/` e `screenshot/fallback/`.

## Da confermare con il cliente prima di pubblicare

1. **Certificazione ISO 9001**: il certificato pubblicato sul sito attuale è scaduto il 20/10/2025. Finché non c'è il rinnovo, il sito nuovo non la cita e non mostra il marchio.
2. **Brevetto n° 275.271** (scritto così sul sito attuale; il sito inglese cita la domanda PD2011A000169): stato e data. Il sito nuovo lo riporta come "depositato".
3. **Trasporto con gru e posa con personale proprio**: sul sito valgono per le piattaforme. Nel cartiglio della Home ("Trasporto e posa") il trasporto è scritto in generale: vale anche per le vasche?
4. **Norme di riferimento** (Azienda): l'elenco è ricostruito dai numeri leggibili della pagina italiana danneggiata. Serve l'elenco aggiornato.
5. **Dati societari**: capitale sociale 100.000 euro (versato?), codice destinatario SDI J6URRTW e PEC gardenspav@legalmail.it vengono da una fonte secondaria (aziende.it). Ragione sociale scritta "Gardens Pav S.r.l." (sul sito attuale ci sono sei grafie diverse); "Gardens-Pav" resta solo nel logo.
6. **Orari** lun-ven 8-12 e 14-18, sabato e domenica chiuso: vengono dalla scheda Google, sul sito attuale non ci sono.
7. **Foto**: "Vasca 1050 in posa" viene dal nome del file originale ("FOTO 1050_3.JPG"; sulla vasca si legge "V5"); le vasche circolari "sul piazzale": è il piazzale di Legnaro?
8. **Piattaforme**: numero di vasche di raccolta della pista self Mod. 500 doppia griglia (il sito nuovo scrive "vasche di raccolta" senza numero); per il Portale Mod. 4 i supporti porta grigliato sono compresi nella fornitura? (sul sito attuale quella riga è stata sostituita da testo estraneo).
9. **Prima pioggia, riga 10.000 mq**: il sito attuale scrive pozzetto "Ø 148x20h"; nel sito nuovo è Ø 148×206 h come nelle righe 8.000 e 9.000.
10. **"Vantaggi" delle piattaforme** (sei voci): l'italiano è perso, sono tradotte dal sito inglese. Da rileggere.
11. **Ufficio tecnico**: la frase "Indicate il manufatto e il dato che lo dimensiona: portata in litri al secondo, abitanti equivalenti o superficie scolante in metri quadri. Per le piattaforme, il modello e il luogo di posa." e i campi del modulo "Dato di dimensionamento" e "Comune e provincia di posa" sono una proposta presa dalle tabelle: va bene così?
12. **Realizzazioni**: anno e modello di ogni cantiere (il sito attuale ha solo le foto); il sito nuovo non nomina i clienti: servono i consensi per farlo; le località delle due realizzazioni in Francia; Cornate d'Adda è in provincia di Monza e Brianza (il sito attuale scrive BG, il sito nuovo MB). Sul sito attuale ogni cantiere ha una galleria di 2-15 foto: il sito nuovo ne mostra una per cantiere (le altre sono in `assets/originali/`).
13. **Supporti per recinzioni**: citati nelle versioni tedesca e francese, "in fase di aggiornamento" ovunque. Sono ancora in produzione? Oggi sono fuori dal sito nuovo.
14. **Versione inglese** (`eng.gardenspav.it`): tenerla? Se sì, va tradotta a parte; se no, i sottodomini `eng.`, `deu.` e `fra.` vanno reindirizzati alla home.
15. **File di qualità migliore**: logo vettoriale (oggi c'è solo un PNG 358×75); i render della vasca 550 e della vasca circolare a 3.000 px; l'esempio di posa ridisegnato in vettoriale (oggi è un'immagine di 623 px con le scritte dentro, per questo nel sito nuovo le voci sono ripetute in HTML accanto).
16. **Privacy e Cookie**: le due pagine sono da scrivere; il banner cookie del sito attuale considera consenso il "continuare la navigazione" e non ha un pulsante per rifiutare.

## Foto da fare (brief breve)

Le foto del sito attuale reggono quasi tutte a 2x, ma sono poche e scattate in cantiere in momenti diversi. Per far crescere il sito servono 15-20 scatti in una giornata: lo stabilimento e il piazzale dall'alto (da un cestello o da un drone), il getto e la vibratura in cassero, una vasca calata dall'autogru con luce buona, una piattaforma finita con un'auto sopra, la superficie a rombi in macro (radente, per leggere il rilievo antiscivolo), un interno resinato rosso e uno azzurro, i quattro campioni di colore veri, e qualche ritratto per ruolo (ufficio tecnico, produzione, posa) solo con il consenso delle persone. Luce naturale, colori fedeli (il grigio del calcestruzzo non deve virare), almeno 2.400 px sul lato lungo, per ogni soggetto principale sia orizzontale 3:2 sia verticale 4:5.

## Rigenerare i file

Serve Python 3 con Pillow (`pip install pillow`).
```
python3 _sorgente/prepara_immagini.py        # rifà assets/web/ dalle immagini originali (assets/originali/)
python3 _sorgente/build.py                   # rifà elementor-json/, html-fallback/, anteprima/
python3 _sorgente/redirect.py                # rifà plugin/redirect-301.csv
```
Opzioni di `build.py`: `--base URL` (dove sono le immagini), `--url-sito URL` (link interni assoluti), `--out CARTELLA`.
I testi si cambiano in `_sorgente/contenuti.py` (dati aziendali in cima al file); i dati delle tabelle e dei cantieri in `_sorgente/dati/`. Il build si ferma se trova un trattino lungo, una parola della lista `PAROLE_VIETATE` di `build.py` (il copy generico da evitare), un valore di stile non valido, un'immagine senza testo alternativo o un link dentro un blocco già cliccabile.
