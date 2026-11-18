# Villa Eidos: nota di consegna

17 novembre 2026, seconda direzione. Sito nuovo per villaeidos.it (oggi pagina di parcheggio di Aruba). Niente è stato pubblicato e nessuno è stato contattato.

La prima versione (serif su carta e pietra, fregio d'apertura) è stata scartata dal committente ("più professionale, moderno") ed è nel commit c33d072a. Questa è la versione in chiave business moderna: un grottesco solo, bianco e un neutro freddo, il verde del logo come unico accento, apertura divisa con la foto della sala conferenze, schede degli spazi.

## Cosa c'è

| Percorso | Cosa |
|---|---|
| `DIREZIONE-HE.md` | La direzione: idea, carattere, colori, movimento, ritmo delle sezioni. |
| `anteprima/` | Il sito statico: `index.html`, `privacy.html`, `cookie.html`, `assets/`. Si apre servendo il repository (`python3 -m http.server`). |
| `wordpress/villaeidos-tema.zip` | Il tema WordPress (455 KB), con l'installatore (*Aspetto > Installa Villa Eidos*). |
| `wordpress/villaeidos/` | Lo stesso tema scompattato, per l'FTP. |
| `wordpress/installa-su-server.sh` | Installazione con WP-CLI, per un server con SSH. |
| `wordpress/LEGGIMI.md` | Come installare WordPress su Aruba, caricare il tema, cambiare testi e foto, mettere la foto della villa. |
| `_sorgente/` | Tutto quello che genera tema e anteprima: `build.py`, `pagine.py` (le pagine Elementor con i testi del cliente), `immagini.py`, `logo/`, `tema/`. |
| `assets/web/` | Foto web, logo vettoriale (SVG) e PNG trasparenti. Gli originali del cliente stanno in `assets/originali/`, fuori da git. |
| `screenshot/` | Prime schermate ferme (`prima-schermata-390/768/1440/1920.jpg`), pagine intere con le foto caricate (`pagina-intera-1440.jpg`, `pagina-intera-390.jpg`), fogli dei fotogrammi (`foglio-1440.jpg`, `foglio-390.jpg`), prove in `prove/`. Video e fotogrammi singoli restano sul disco, fuori da git. |

Si rifà tutto con `python3 -I VillaEidos-Sito/_sorgente/build.py`. Il controllo dei testi ferma la costruzione se in Home compare una frase che non viene dal testo del cliente (`pagine.FONTE`) o dall'elenco degli adattamenti con la loro fonte (`pagine.ADATTATI`).

## Il materiale

- **Testo**: `villaeidos.it.doc`, accenti corretti dalla codifica Windows-1252. Sono gli unici fatti in pagina. La schermata satellitare di Google Maps nel `.doc` non è usata (immagini di Google).
- **Logo**: CMYK con profilo Coated FOGRA39, convertito in sRGB con il profilo (verde #4A8C46, verde acqua #5EC1C9), separato nei due inchiostri e vettorializzato con potrace, alleggerito con SVGO. Versioni: intero, orizzontale (testata), marchio, bianco; PNG trasparenti per l'icona del sito.
- **Foto**, un trattamento unico (bianco verso il neutro, saturazione all'88 %, contrasto morbido, grana fine), mai ingrandite nei file, sul sito al massimo 1,25 volte:
  - *sala conferenze*, due inquadrature della stessa foto perché non si ripeta uguale: in apertura in verticale con le finestre ad arco della barchessa (384 x 480, mostrata a 480 x 600), nella scheda le colonne e il fondo della sala (440 x 330, mostrata fino a 550);
  - *sale riunioni*: 1080 x 810, via la scritta "HONOR 400" e la tigre del murale con il simbolo sul casco;
  - *uffici*: 480 x 360, via il cestino e lo scatolone;
  - *reception*: intera;
  - *sale d'attesa*: raddrizzata (EXIF 6). In questa direzione non è in pagina: le schede sono tutte 4:3 e la foto è verticale. Le versioni web restano in `assets/web/foto/`.
- **La foto della villa**: la foto d'apertura è un'Immagine di Elementor. Provato in locale: scelta un'altra foto dalla libreria, la cornice 4:5 la ritaglia al centro senza toccare altro (`screenshot/prove/foto-villa-sostituita.jpg`).

## Prove (WordPress 7.1.4, Elementor 4.4.1 gratuito, SQLite, PHP 8.3, in locale, database rifatto da zero)

- **Installazione** con `installa-su-server.sh` su un WordPress vuoto: tema, Elementor da WordPress.org, 5 immagini, 3 pagine, Home iniziale, `/privacy/` e `/cookie/`. Rilanciata: nessun doppione (5 allegati, 3 pagine). Bottone *Aggiorna il sito* del pannello: stesso esito. Una pagina modificata a mano resta com'era; con "riscrivi" torna quella del tema. Registro degli errori di WordPress vuoto.
- **Editor di Elementor**: la Home si apre con 47 contenitori e 68 widget; clic sul titolo apre "Modifica Titolo" con il testo, clic sulla foto d'apertura apre "Modifica Immagine" con "Scegli l'immagine" e `apertura-conferenze-384.webp`, clic sulla scheda grande mostra `sala-conferenze-440.webp`. Nessun errore di console (`screenshot/prove/editor-elementor.jpg`).
- **Anteprima uguale a WordPress**, pagina ferma: a 390, 768, 1440 e 1920 stesse altezze (8357, 6171, 5488, 5556 px) e circa 117 pixel diversi. Durante il confronto ho trovato e corretto: la regola di Elementor `max-width:100%` sui widget che annullava i limiti della foto d'apertura e di un paragrafo (ora i limiti sono sulle immagini e sui paragrafi), e `justify-self` che Chromium oggi applica anche ai blocchi (la foto d'apertura finiva a destra sotto i 900 px).
- **Matrice**: Home, Privacy e Cookie in WordPress e la Home dell'anteprima, a 390, 768, 1024, 1440 e 1920, con il movimento, con "riduci movimento" e senza JavaScript (60 casi): nessuno scorrimento orizzontale, nessun errore, nessuna richiesta fallita; a movimento finito la foto d'apertura è intera. Con "riduci movimento" la pagina è completa e ferma (`screenshot/prove/riduci-movimento-1440.jpg`).
- **Modulo**: il link "Richiedi una sala riunioni" porta al modulo e sceglie "Sala riunioni"; il modulo si ferma sul nome, sull'email e sull'informativa; compilato prepara la mail per eidos@eco-management.it con oggetto "Richiesta di disponibilità, Sala conferenze, Prova S.r.l." e la data in formato italiano. Zero cookie, niente in `localStorage` e `sessionStorage`.
- **Pesi al primo caricamento**, senza compressione (il browser di prova carica anche le foto pigre vicine, quindi i numeri sono per eccesso):

| | 1440 | 1440, schermo doppio | 390 | 390, schermo triplo |
|---|---|---|---|---|
| WordPress | 619 KB | 690 KB | 611 KB | 690 KB |
| Anteprima | 223 KB | | | 294 KB |

  Limiti: 1,5 MB a 1440 e 1 MB a 390. In WordPress 309 KB sono gli script di Elementor (jQuery compreso); il kit GSAP non si carica più.
- **Video** con `_metodo/highend/kit/registra.mjs`, 1440 e 390, nessun errore di script: `screenshot/foglio-1440.jpg`, `foglio-390.jpg`.
- **Segnali** (`_metodo/kit/segnali.sh` sulla Home in WordPress): una soglia bloccante su dieci, **l'area delle foto: 12,7 %** contro il 35 % (cinque interni dal telefono, mostrati al massimo a 1,25 volte: senza foto più grandi non si può alzare). Da guardare: una sola misura di `h2` (scelta: una scala sobria), 6 fasce di fondo (le conta anche bianche: in realtà due fasce di superficie e una scura), nessun contenuto datato. Tutto il resto OK: Fustat al 100 % del testo, niente lista b, niente etichette sopra i titoli, niente frecce, 18 filetti, nessuna dissolvenza.

## Voto onesto (griglia del punto 7 di `SISTEMA.md`)

| Voce | Peso | Voto | Perché |
|---|---|---|---|
| Design | 40 % | 7 | Pulito, coerente, professionale: un carattere, un accento, griglia ordinata, schede uguali, un solo campo scuro. Ma le foto sono interni dal telefono, piccoli, con il murale e gli oggetti d'ufficio, e manca la villa. |
| Creatività | 25 % | 5,5 | Volutamente sobrio: è la grammatica dei business center moderni, quindi poco riconoscibile. L'unico segno proprio sono le due inquadrature della barchessa. |
| Usabilità | 25 % | 9 | In cinque secondi si capisce cosa offre, dove e come chiedere; azione principale in testata e in apertura; "Richiedi" su ogni scheda che sceglie lo spazio nel modulo; telefono in un tocco; telefono progettato, non rimpicciolito. |
| Contenuto | 10 % | 6 | Fatti veri e solo del cliente, ma pochi: niente capienze, servizi, orari, nomi o date. |
| **Media pesata** | | **7,0** | |

Voto atteso di un estraneo intorno a **6,5-7**: il sito ora "sembra una sede d'affari" ma la soglia di 8 non si raggiunge senza le foto. **Almeno il 60 % della distanza dipende dalle foto.**

I cinque interventi che valgono di più:
1. La foto della facciata o dal drone nella cornice d'apertura (un clic in Elementor).
2. Rifare gli interni con luce di giorno e senza oggetti estranei, in orizzontale e in alta risoluzione: le schede crescono subito.
3. La sala conferenze piena durante un convegno vero, per la scheda grande.
4. Capienza delle sale e servizi compresi: sono le prime cose che cerca chi organizza.
5. Un fatto con una data o un nome (l'epoca della villa, un evento ospitato).

## Rimasto aperto

- La sala conferenze compare due volte (apertura e scheda grande), anche se in due inquadrature diverse: si risolve appena c'è la foto della villa per l'apertura.
- La foto delle sale d'attesa non è in pagina (verticale, le schede sono 4:3).
- La scheda "Reception e sale d'attesa" ha il link "Richiedi informazioni" senza tipo di spazio: nel modulo non c'è una voce adatta e il testo non dice se si affittano.
- Copernico e Talent Garden, indicati come riferimento, non li ho riaperti in questo giro.

## Foto da chiedere

Tutte a piena risoluzione (almeno 3000 px di lato lungo), file originali e non da WhatsApp, giornata di sole o luce piena coperta, nessuna persona riconoscibile senza liberatoria.

1. **Facciata della villa**: per l'apertura, meglio in verticale o con il soggetto al centro (la cornice è 4:5).
2. **Barchessa**, l'esterno intero, con le arcate.
3. **Giardino**: gli alberi centenari, un vialetto, la villa tra il verde.
4. **Drone**: villa, barchessa, giardino e parcheggi insieme, da circa 40-60 m (pilota autorizzato).
5. **Sala conferenze piena** durante un convegno vero (con il permesso dell'organizzatore).
6. **Parcheggi**, larga.
7. Interni rifatti in orizzontale: sale riunioni pronte per una riunione, un ufficio vuoto pronto per un inquilino, la reception con la luce accesa.

## Domande per il cliente

1. **Foto esterne**: ci sono foto della villa, della barchessa, del giardino e dei parcheggi? Si può organizzare un servizio con il drone?
2. **Ragione sociale e partita IVA** (piede e informativa privacy), sede legale, fornitori di hosting e posta.
3. **Capienza**: quante persone nella sala conferenze e in ogni sala riunioni; quante sale riunioni ci sono.
4. **Servizi inclusi**: wifi, proiettore o schermi, audio e microfoni, videoconferenza, catering o coffee break, pulizie, reception presidiata.
5. **Uffici**: si affittano a lungo termine? Anche come sede legale o domiciliazione? Arredati?
6. **Orari**: della struttura e della reception; le sale si prenotano anche la sera o nel fine settimana?
7. **Referente** per le richieste: nome, ruolo, telefono diretto.
8. **I tre indirizzi**: Via Battaglia 67, via Colombo 2 e 6A sono tre ingressi? A cosa porta ciascuno?
9. **Reception e sale d'attesa**: sono a servizio degli uffici o si prenotano anche da sole?
10. **Un fatto con una data o un nome** per il sito.
11. **Hosting**: c'è già un piano Aruba (Linux o WordPress) o va attivato? Chi gestirà il sito dopo la consegna?
