# Dieffepiu: il sito completo in WordPress

La home è quella della proposta, non ridisegnata. Le sono state aggiunte le pagine interne, nello stesso stile: stessa griglia, stessi caratteri, stessi colori.

Il tema contiene tutto: pagine, notizie, immagini, caratteri, moduli e installatore. Non servono plugin, né Elementor, né Contact Form 7.

## Cosa c'è

| File o cartella | A cosa serve |
|---|---|
| `wordpress/dieffepiu-tema.zip` | Il tema da caricare su WordPress (3,4 MB). |
| `wordpress/dieffepiu/` | Lo stesso tema scompattato, da caricare via FTP se il pannello rifiuta lo zip. |
| `wordpress/redirect-301.csv` | Rimanda i vecchi indirizzi di dieffepiu.it alle pagine nuove: si importa nel plugin Redirection al passaggio online. |
| `anteprima/` | Lo stesso sito in HTML. Si apre con doppio clic su `anteprima/index.html`, anche senza internet. È il piano B per l'appuntamento. |
| `_sorgente/` | Il generatore. `python3 _sorgente/build.py` rifà anteprima, tema e zip. |
| `sito/index.html` | La home originale della proposta, lasciata com'era. |

## Le pagine

13 pagine e 5 notizie:

- **Home** `/`
- **Sistemi** `/sistemi/`, l'indice delle sei famiglie, che sono:
  - **Sistema in kit** `/sistemi/kit/`: FLEXAL KIT e KIT TRANSFORMER
  - **Sistema a misura** `/sistemi/a-misura/`: FLEXAL DIM, FLEXAL PLATINUM, ROLLY STYLE 1, ROLLY STYLE WOOD, ROLLY STYLE 3 e CIVIKA 50
  - **Sistema carrarmato** `/sistemi/carrarmato/`: TANK® 2.0 e TANK REVOLUTION®
  - **Sistema plissé** `/sistemi/plisse/`: PLIXI®
  - **Sistema battente** `/sistemi/battente/`: AMERIKA 35 e schermi fissi ed apribili
  - **Componenti universali** `/sistemi/componenti/`: rallentatori, molle, catenelle, fettucce, reti ed espositore
- **Macchine** `/macchine/`: 12 macchine e il kit pneumatico, ognuna con descrizione, dati tecnici e ricambi
- **Azienda** `/azienda/`
- **Fiere e novità** `/news/`: le 5 fiere dal 2021 al 2026, scritte come articoli di WordPress. Ogni notizia sta in `/news/<titolo>/`.
- **Contatti** `/contatti/`, con il modulo
- **Area riservata** `/area-riservata/`, con il modulo per chiedere l'accesso
- **Pagina non trovata**, la 404

Ogni famiglia di sistemi ha:
- per ogni linea, la tabella delle varianti con altezza e larghezza massime, cassonetto, tubo rete e pagina del catalogo;
- la tavola esplosa con i codici;
- i profili in alluminio con pesi e misure, dove il catalogo li dà.

Tutti i numeri vengono dalle schede "Dati Tecnici" del catalogo generale 2023, con la pagina indicata accanto.

## Installare (10 minuti)

1. Serve un WordPress pulito (6.4 o più recente, PHP 7.4 o più) e l'accesso come amministratore.
2. *Aspetto > Temi > Aggiungi tema > Carica tema*, scegli `dieffepiu-tema.zip`, poi *Installa ora* e *Attiva*.
   - Se WordPress risponde che il file è troppo grande (l'hosting accetta file più piccoli di 3,4 MB), carica via FTP o dal file manager dell'hosting la cartella `wordpress/dieffepiu/` dentro `wp-content/themes/`, poi attivala da *Aspetto > Temi*.
3. *Aspetto > Installa Dieffepiu*.
   - Nel campo "I moduli arrivano a" lascia il tuo indirizzo per la prova.
   - Lascia le due spunte e premi *Installa il sito*.
4. Fatto. In un colpo l'installatore:
   - crea le pagine e le notizie;
   - crea il menu della testata;
   - imposta la home e la pagina delle notizie;
   - imposta gli indirizzi (/sistemi/, /news/<notizia>/ ...), l'italiano e il fuso orario;
   - mette nel cestino la pagina e l'articolo di esempio di WordPress;
   - nasconde il sito ai motori di ricerca.

Si può rilanciare quando vuoi: non crea doppioni. Se togli la spunta "Riscrivi il contenuto", lascia i testi che hai già cambiato.

## Collaudo fatto il 3 novembre 2026

Il collaudo è su WordPress 7.1.4 appena installato, con il tema caricato dal pannello come al punto 2.
- **Installazione**: caricamento, attivazione, avviso e installatore funzionano. Le 14 pagine rispondono 200, l'indirizzo sbagliato dà la 404 del tema.
- **Moduli**: i due moduli inviati davvero (in locale l'email è stata intercettata, non spedita).
  - Contenuto: l'email arriva con tutti i campi e con "Rispondi a" impostato su chi scrive.
  - Invii rifiutati con messaggio: invio vuoto, senza consenso, senza email valida.
  - Protezioni: controllo anti-robot nascosto, nonce di WordPress, un invio ogni 30 secondi dallo stesso indirizzo.
- **Schermi** a 320, 390, 768, 1024 e 1440 px, su anteprima e WordPress: niente scorrimento orizzontale, niente errori di script.
- **Home**: confrontata pixel per pixel con quella della proposta. Le uniche differenze sono quelle elencate qui sotto.

## Che cosa cambia nella home rispetto alla proposta

- **Link**: menu e piede portano alle pagine vere invece che alle sezioni.
- **Lingue**: il selettore IT EN DE è tolto, perché le pagine EN e DE non ci sono ancora e i link sarebbero rotti. Torna con le traduzioni (Polylang o WPML).
- **Tre link nuovi**: "Le sei famiglie di sistemi" sotto l'indice delle linee, "Tutte le macchine, con le schede" sotto il selettore, "Fiere e novità" nel paragrafo delle fiere.

## Modificare

- **Testi delle pagine**: *Pagine*, poi la pagina. Ogni sezione è un blocco "HTML personalizzato".
  - `{{tema}}` e `{{casa}}` sono segnaposto per gli indirizzi di immagini e pagine: non vanno cancellati. Così il sito funziona anche se cambia dominio.
  - Nell'editor le immagini non si vedono, sul sito sì.
- **Pagine nuove**: una pagina scritta nell'editor con paragrafi normali prende da sola titolo e colonna di testo nello stile del sito. Si può usare anche Elementor: la pagina fatta con Elementor viene lasciata a tutta larghezza.
- **Menu della testata**: *Aspetto > Menu*, "Menu della testata".
- **Notizie**: *Articoli > Aggiungi articolo*, categoria Fiere. La lista le mostra in ordine di data.
- **Testata e piede**: sono i file `parti/testata.html` e `parti/piede.html` del tema.
- **Rigenerare il tema**: `python3 _sorgente/build.py` (serve Pillow). Le foto originali e il catalogo stanno in `assets/originali/`, fuori da git: le foto si riscaricano da `https://dieffepiu.it/image/<id>` (elenco in `_sorgente/immagini.py`), il catalogo da https://dieffepiu.it/catalogo.pdf.

## Prima della messa online

1. **Moduli**: in *Aspetto > Installa Dieffepiu* metti info@dieffepiu.it (o l'indirizzo che sceglie l'azienda) e togli "Riscrivi il contenuto".
   - Le email partono con la funzione di posta del server. Perché non finiscano nello spam conviene un plugin SMTP (per esempio WP Mail SMTP) con la casella dell'azienda.
2. **Motori di ricerca**: togli la spunta "Nascondi il sito ai motori di ricerca".
3. **Catalogo PDF**: tutti i link puntano a `https://dieffepiu.it/catalogo.pdf`. Quando il dominio passa al sito nuovo, il PDF va rimesso allo stesso indirizzo: caricalo via FTP nella cartella principale del sito, accanto a `wp-config.php`. Altrimenti i link si rompono.
4. **Vecchi indirizzi**: installa Redirection e importa `wordpress/redirect-301.csv` (/home, /aziende, /news, /login, /privati, /prodotti/...).
5. **Privacy e cookie**:
   - I link restano sull'informativa iubenda dell'azienda, che però deve citare i due moduli (contatti e accesso) e la newsletter.
   - Il tema non usa cookie, non carica Google Fonts né mappe incorporate e non ha statistiche: così com'è non serve il banner. Se l'azienda rimette Google Analytics o Tag Manager (il sito di oggi li ha), il banner torna obbligatorio.
6. **Newsletter del piede**: come nella home, non è collegata a nessun servizio e lo dice a chi si iscrive. Va collegata (Brevo, Mailchimp) o tolta.
7. **Area riservata**: oggi la pagina raccoglie le richieste di accesso, ma un login non c'è. Va deciso se tenere il portale attuale (per esempio su un sottodominio) o usare un plugin per le aree riservate.

## Dati da confermare con l'azienda

Valgono tutti quelli del `LEGGIMI.md` della home. In più, per le pagine interne:
- **Famiglie**: l'assegnazione delle 14 linee alle sei famiglie del sito di oggi l'ho fatta io. Il catalogo divide in kit e a misura solo i componenti.
- **Catalogo 2023**: quali linee e quali macchine sono ancora in produzione, e se i dati sono cambiati.
- **Testi del catalogo che non tornano**: in pagina c'è la scelta indicata, ma va chiesto.
  - ATT012 ha la stessa descrizione della ATT035-3BM: in pagina solo nome e dati.
  - ATT015 ha un titolo ("saldatrice automatica per tubi rete") che non corrisponde alla descrizione (un banco di taglio e saldatura): in pagina solo nome, dati e "Brevetto depositato".
  - ATT001-B: il testo dice 1.500 mm di saldatura utile, la tabella 1.560. In pagina la tabella.
  - FLEXAL DIM laterale doppia: larghezza massima 3.000 mm nella scheda italiana, 1.500 in quella inglese. In pagina 3.000.
  - DFTK005 si chiama "Guida superiore" a p. 91 e "Tubo rete" a p. 99. In pagina tutti e due, come stampati.
  - Alcuni codici sono scritti in modo diverso tra la tavola esplosa e la pagina accessori (CR112R e CR1112R, CR1105 e CR1105R, CR1147 e CR1147S). In pagina come nella tavola.
- **TANK® 2.0**: il catalogo dice "sistema brevettato da Dieffepiu S.r.l.: Bi-Convex" e porta il timbro "PATENT PENDING" (Italia, Europa, Cina). La pagina dice solo "il sistema Bi-Convex di Dieffepiu", finché non si sa lo stato del brevetto.
- **Rallentatore viscodinamico**: il testo della pagina Componenti è riassunto da p. 192 del catalogo; il catalogo dice anche "sistema brevettato".
- **Fiere**: date della MADE expo 2021, e le prossime fiere (se ci sono, vanno aggiunte come notizie).
- **Area riservata**: che cosa succede dopo la richiesta (chi risponde, che cosa si manda).
- **Immagini**:
  - Le pagine interne usano i disegni e i render del catalogo, rasterizzati a 120 dpi: sono mostrati alla loro misura vera, mai ingranditi.
  - Le foto vere sono quelle del sito di oggi: il kit TANK, la rete plissettata, i rotoli e le testate.
  - Per le macchine servono foto vere, come già scritto per la home: oggi ci sono solo i render arancio del catalogo.
