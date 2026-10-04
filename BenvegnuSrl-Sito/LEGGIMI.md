# Benvegnù S.r.l.: nuovo sito per WordPress + Elementor

Sito completo in 7 pagine (Home, Azienda, Catalogo, Vibram, Marchi, Novità, Contatti) più header e footer, in due formati:
- **Formato A (primario):** template Elementor `.json` da importare con *Template > Template salvati > Importa template*.
- **Formato B (fallback):** la stessa pagina in HTML+CSS autosufficiente, una sezione per file, da incollare in un widget HTML di Elementor.

Tutti i file sono stati **importati e provati davvero** su un WordPress di test (vedi "Collaudo"). Le immagini sono in `screenshot/`.

## Cosa c'è nella cartella

| Cartella / file | Contenuto |
|---|---|
| `01-analisi-sito-attuale.md` | pagine, testi reali, immagini e problemi del sito attuale |
| `02-competitor-e-riferimenti.md` | 14 concorrenti, 14 siti di riferimento, pattern ripresi dal PMF |
| `03-mappa-pagine.md` | mappa finale delle pagine e sezioni |
| `elementor-json/` | **Formato A**: `bvg-00-header.json`, `bvg-99-footer.json` (tipo *sezione*) e le 7 pagine `bvg-01-home.json` ... `bvg-07-contatti.json` (tipo *pagina*, solo il corpo) |
| `elementor-json/pagine-complete-senza-pro/` | le stesse 7 pagine con header e footer già dentro e modello *Canvas*: la via più semplice senza Elementor Pro |
| `html-fallback/` | **Formato B**: una cartella per pagina, un file `.html` per sezione, più `00-header/` e `99-footer/` |
| `anteprima/` | le 7 pagine complete in HTML, da aprire nel browser con doppio clic |
| `assets/web/` | le 32 immagini usate dal sito (foto in bianco e nero, prodotti, loghi) |
| `assets/originali/` | tutte le immagini scaricate dal sito attuale, con `manifest.json` |
| `screenshot/` | le pagine come le mostra Elementor dopo l'import (desktop, tablet, mobile) e il confronto con il fallback |
| `_sorgente/` | il generatore: `contenuti.py` (testi e pagine), `motore.py`, `build.py` |

## Versione di Elementor

**Target dichiarato: Elementor 4.3.3, versione gratuita** (l'ultima stabile al 4 ottobre 2026), con WordPress 7.1.2 e tema Hello Elementor 3.5.1.

Il JSON è scritto nel modo più conservativo possibile:
- solo **contenitori flexbox** e **widget classici gratuiti**: Titolo, Testo, Immagine, Pulsante, Divisore, Google Maps, HTML, "Articoli recenti" di WordPress;
- nessun widget o chiave Pro, nessun elemento "atomico" della v4, nessun riferimento ai colori e font globali del kit (`__globals__`), nessuna animazione;
- colori, font e misure scritti in chiaro su ogni elemento;
- formato del file uguale a quello che Elementor produce con "Esporta template" (`content`, `page_settings`, `version: "0.4"`, `title`, `type`).

Su versioni 3.x recenti (dalla 3.16, quando i contenitori sono diventati stabili) dovrebbe funzionare, ma **non l'ho provato**: l'unica versione collaudata è la 4.3.3.

## Come importare (Formato A)

Prima di iniziare:
1. Accedi come **Amministratore** (gli altri ruoli non possono importare JSON, e senza il permesso "unfiltered_html" Elementor ripulisce stili e iframe).
2. *Elementor > Impostazioni > Funzionalità*: **Contenitore = Attivo** (è il valore predefinito dalla 3.16). Se è disattivato, l'import riesce ma la pagina resta **vuota, senza errori**.
3. Il sito deve poter scaricare file da Internet: le immagini arrivano durante l'import (vedi "Immagini").

### Strada 1: senza Elementor Pro (consigliata se non hai Pro)
1. *Template > Template salvati > Importa template*, scegli un file da `elementor-json/pagine-complete-senza-pro/`, *Importa ora*. Se compaiono gli avvisi "i file JSON possono essere pericolosi" e "upload non filtrati", scegli **Continua** e poi **Importa senza abilitare**.
2. Ripeti per le 7 pagine (oppure comprimi la cartella in uno .zip e importala in un colpo: in quel caso conta che i template importati siano 7, perché Elementor salta in silenzio i file dello ZIP che non vanno).
3. *Pagine > Aggiungi pagina*, titolo (es. "Catalogo") e **slug** esatto: `catalogo`, `vibram`, `marchi`, `azienda`, `novita`, `contatti`. I link interni puntano a questi indirizzi.
4. *Modifica con Elementor* > icona cartella > *I miei template* > inserisci il template della pagina. Quando l'editor chiede se applicare le impostazioni della pagina, rispondi **Applica** (imposta il modello Canvas e nasconde il titolo).
5. Per la Home: *Impostazioni > Lettura > La homepage mostra: una pagina statica > Home*.

### Strada 2: con Elementor Pro
1. Importa `bvg-00-header.json` e `bvg-99-footer.json`.
2. *Template > Theme Builder*: crea un Header e un Footer, inserisci dentro i due template, condizione *Intero sito*.
3. Importa le 7 pagine da `elementor-json/` (solo il corpo, modello "Elementor a larghezza piena") e inseriscile come sopra.

### Novità
La lista "Ultime novità" usa il widget gratuito di WordPress "Articoli recenti": mostra gli ultimi articoli del blog. Per pubblicare un avviso (chiusura per ferie, nuovo arrivo) basta scrivere un articolo in *Articoli > Aggiungi articolo*. Nel test ho creato due articoli di esempio: "Il nuovo sito di Benvegnù è online" e "Il catalogo online: 874 articoli in 10 famiglie".

## Immagini

Ogni immagine nel JSON punta a un indirizzo pubblico su GitHub (`raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/...`). **Durante l'import Elementor scarica ogni immagine e la carica nella tua libreria media**: dopo l'import le immagini sono sul tuo sito e il link a GitHub non serve più. Il ramo GitHub deve però esistere al momento dell'import.

Ogni immagine ha un ID numerico fisso: reimportando lo stesso template Elementor riconosce le immagini già scaricate e **non crea doppioni** (verificato: 32 immagini, 32 file nella libreria anche dopo tre import).

Se preferisci non dipendere da GitHub: carica la cartella `assets/web/` sul tuo server (per esempio in `wp-content/uploads/benvegnu/`) e rigenera i file con
`python3 _sorgente/build.py --base https://TUO-DOMINIO/wp-content/uploads/benvegnu/`

## Cosa potrebbe non reggere l'import (tieni pronto il fallback)

Il formato dei template Elementor ha ID e versioni dei widget che Elementor genera da sé. Ho scritto i file come li esporta Elementor e li ho importati sulla 4.3.3, ma sul tuo sito queste cose possono andare diversamente:

1. **Versione diversa da 4.3.3.** Su versioni 3.x vecchie (prima della 3.16) i contenitori non ci sono: il template risulta vuoto. Su versioni future qualche controllo può cambiare nome: un nome sconosciuto **non dà errore**, viene solo ignorato (il risultato è uno stile predefinito al posto del mio).
2. **Contenitore disattivato** nelle funzionalità: pagina vuota senza avviso.
3. **Immagini non scaricabili** (sito senza accesso a Internet, firewall, GitHub irraggiungibile, timeout di 5 secondi superato): al loro posto compare il **riquadro grigio di Elementor**, senza errori. Controlla ogni pagina dopo l'import.
4. **Testo alternativo delle immagini**: Elementor lo perde all'import. Le immagini hanno nomi descrittivi, ma l'alt va compilato nella libreria media (elenco pronto in `elementor-json/testi-alternativi-immagini.txt`).
5. **ID degli elementi**: Elementor li rigenera sempre all'import e all'inserimento. Non è un problema, ma non puoi riferirti agli ID del file.
6. **Font**: Barlow e Barlow Condensed sono caricati da Google Fonts da Elementor. Se il sito blocca Google Fonts o usa "Carica i Google Fonts in locale", controlla che i titoli siano ancora condensati. Per il GDPR conviene attivare *Elementor > Impostazioni > Avanzate > Carica i Google Fonts localmente*.
7. **Stili del tema**: con un tema diverso da Hello Elementor, titoli e link possono ereditare margini o colori del tema. Ho messo colori espliciti ovunque e sottolineature inline nei link dei testi; il widget "Articoli recenti" ha un piccolo CSS dedicato dentro un widget HTML.
8. **Kit globale**: i miei elementi non usano i colori e i font globali. Conviene comunque impostare in *Impostazioni del sito* i colori Nero `#111111`, Bianco `#FFFFFF`, Rosso `#9F2E29` e i font Barlow Condensed e Barlow, così i nuovi elementi aggiunti a mano nascono coerenti.
9. **Larghezze su mobile**: Elementor non eredita la larghezza mobile dei contenitori da quella tablet. L'ho scritta esplicitamente su tutti i breakpoint; se modifichi un blocco dall'editor, controlla anche la vista mobile.
10. **Lazy load degli sfondi** (attivo di default): non ci sono immagini di sfondo nei contenitori, solo immagini normali, quindi non dovrebbe incidere.
11. **Link interni** relativi (`/catalogo/`): funzionano se WordPress è nella radice del dominio. Se è in una sottocartella o vuoi link assoluti: `python3 _sorgente/build.py --url-sito https://www.benvegnusrl.it`.
12. **Mappa Google** (widget gratuito, iframe): imposta cookie di terze parti. Va gestita con il banner cookie del sito.
13. **Il PDF delle condizioni di vendita** punta ancora al sito attuale: caricalo nella libreria media e aggiorna il link (Footer, Azienda, Contatti).

Se un template non entra o arriva rotto, usa il Formato B per quella pagina.

## Come usare il Formato B (fallback HTML)

1. Crea la pagina e aprila con Elementor; nelle impostazioni pagina scegli il modello **Elementor Canvas**.
2. Per ogni file della cartella della pagina, nell'ordine (`00-header/01-header.html`, poi `01-home/01-apertura.html`, `02-catalogo.html`..., infine `99-footer/01-footer.html`): aggiungi un **contenitore a larghezza piena con padding 0 e spaziatura 0**, dentro un widget **HTML**, incolla il contenuto del file.
3. Ogni file è autosufficiente: carica i propri font, ha il CSS con un prefisso unico (`.bvg-home-catalogo` ecc.) che non tocca il resto del sito e resiste agli stili del tema.

Differenze rispetto al Formato A: nel fallback i testi si modificano solo nel codice; la lista "Ultime novità" è statica; la mappa è un iframe Google semplice. Le immagini nel fallback puntano all'indirizzo GitHub: per la pubblicazione definitiva conviene rigenerare con `--base` verso le immagini caricate sul tuo sito (vedi "Immagini").

## Collaudo fatto

WordPress 7.1.2 in locale (italiano), Elementor 4.3.3, Hello Elementor 3.5.1, PHP 8.3.
- Import di tutti i 16 file con la stessa funzione del pulsante *Importa template* (`Source_Local::import_template`): tutti entrati, **elementi salvati uguali a quelli del file** (Home 140, Catalogo 139, Vibram 109...), **tutte le immagini scaricate**, nessun riquadro grigio.
- Import da interfaccia con il pulsante vero (Playwright).
- Pagine create dai template e fotografate a 1440, 1024 e 390 px: `screenshot/elementor-test/`.
- Fallback HTML incollato in widget HTML dentro Elementor e confrontato con il Formato A: `screenshot/fallback/`.

## Da confermare con il cliente prima di pubblicare

1. **"Dal 1980"**: è la data dichiarata dall'azienda; la S.r.l. risulta iscritta il 24/10/1990. La tabella "Dal 1980" in Azienda riporta entrambe le date.
2. **"Rivenditore autorizzato Vibram"**: è scritto sul sito attuale; serve la conferma e il permesso scritto per usare il logo Vibram (i marchi Vibram, ottagono giallo compreso, sono registrati).
3. Loghi Gütermann (quello attuale è la versione vecchia: chiedere il logo A&E Gütermann a A&E Gütermann Italy, Torino), Girba, Fratelli Zucchini: permesso d'uso e file aggiornati.
4. **Orari**: lun-ven 8:30-12:30 e 14:30-18:30 (Google e sito attuale); alcune directory dicono chiusura alle 19:00.
5. **Parcheggio clienti davanti al negozio**: citato nelle recensioni Google.
6. **Spedizione con corriere** e condizioni di vendita del 2014 (minimo d'ordine 200 euro + IVA, bonifico anticipato, 7 giorni lavorativi): sono ancora valide?
7. **Email di riferimento**: il sito usa `commerciale@benvegnusrl.it`; nei PDF compaiono anche `info@` e `mail@`.
8. **Sede legale a Padova** (Piazzetta Primo Modin 12) nel footer: confermare. Esiste ancora un punto vendita a Padova, Via S. Salvatore 37?
9. Famiglie non online (lacci, cerniere, chiodi, occhielli, rinforzi, adesivi Zucchini): sono ancora a magazzino?
10. Logo **vettoriale** (oggi c'è solo un PNG 295x72) e le foto originali dei banner a risoluzione più alta.
11. Pagine **Privacy** e **Cookie** (linkate nel footer) da scrivere.

## Foto da fare (brief breve)

Oggi ci sono solo una foto esterna e 9 foto del magazzino a 750 px. Per far crescere il sito servono 15-20 scatti in una giornata: pile di lastre Vibram viste di taglio, coni di filo Gütermann in fila, utensili sul banco (forbici, trincetti, lesine, punzoni), latte di colla e flaconi Girba, scaffali con i cartellini, il banco con un cliente, mani che misurano una lastra, l'ingresso con il parcheggio. Luce naturale o flash diffuso laterale, niente luce gialla; ogni scatto deve funzionare in bianco e nero; per i soggetti principali sia orizzontale 3:2 sia verticale 4:5. Le foto prodotto restano a colori su fondo bianco.

## Rigenerare i file

Serve Python 3 con Pillow (`pip install pillow`).
```
python3 _sorgente/prepara_immagini.py        # rifà assets/web/ dalle immagini originali
python3 _sorgente/build.py                   # rifà elementor-json/, html-fallback/, anteprima/
```
Opzioni di `build.py`: `--base URL` (dove sono le immagini), `--url-sito URL` (link interni assoluti), `--out CARTELLA`.
I testi si cambiano in `_sorgente/contenuti.py` (dati aziendali in cima al file). Il build si ferma se trova un trattino lungo, una parola da evitare ("eccellenza", "leader", "passione"...) o un valore di stile non valido.
