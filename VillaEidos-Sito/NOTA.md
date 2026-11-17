# Villa Eidos: nota di consegna

17 novembre 2026. Sito nuovo per villaeidos.it (oggi pagina di parcheggio di Aruba). Niente è stato pubblicato e nessuno è stato contattato.

## Cosa c'è

| Percorso | Cosa |
|---|---|
| `DIREZIONE-HE.md` | La direzione artistica, scritta prima del codice: idea, riferimenti guardati, caratteri, colori, movimento, ritmo. |
| `anteprima/` | Il sito statico: `index.html`, `privacy.html`, `cookie.html`, `assets/`. Si apre servendo il repository (`python3 -m http.server`). |
| `wordpress/villaeidos-tema.zip` | Il tema WordPress (647 KB), con l'installatore (*Aspetto > Installa Villa Eidos*). |
| `wordpress/villaeidos/` | Lo stesso tema scompattato, per l'FTP. |
| `wordpress/installa-su-server.sh` | Installazione con WP-CLI, per un server con SSH. |
| `wordpress/LEGGIMI.md` | Come installare WordPress su Aruba, caricare il tema, cambiare testi e foto, mettere la foto della villa. |
| `_sorgente/` | Tutto quello che genera tema e anteprima: `build.py`, `pagine.py` (pagine Elementor con i testi del cliente), `immagini.py`, `fregio/`, `logo/`, `tema/`. |
| `assets/web/` | Foto web, fregio, logo vettoriale (SVG) e PNG trasparenti. Gli originali del cliente stanno in `assets/originali/`, fuori da git (`.gitignore`). |
| `screenshot/` | Prime schermate ferme (390, 768, 1440, 1920), fogli dei fotogrammi a 1440 e 390, prove in `prove/`. I video `scorrimento-*.mp4` e i fotogrammi singoli restano sul disco, fuori da git. |

Si rifà tutto con `python3 -I VillaEidos-Sito/_sorgente/build.py`. Il controllo dei testi ferma la costruzione se in Home compare una frase che non viene dal testo del cliente (`pagine.FONTE`) o dall'elenco degli adattamenti con la loro fonte (`pagine.ADATTATI`).

## Il materiale e come l'ho trattato

- **Testo**: `villaeidos.it.doc`, accenti corretti dalla codifica Windows-1252. Sono gli unici fatti in pagina. Nel `.doc` c'è anche una schermata satellitare di Google Maps: non è usata (le immagini sono di Google), ma conferma che serve una foto dal drone.
- **Logo**: JPEG CMYK 2010 x 2184 con profilo Coated FOGRA39. Convertito in sRGB con il profilo (colorimetrico relativo con compensazione del nero): verde **#4A8C46** e verde acqua **#5EC1C9**; il provino di oggi li mostrava più accesi perché ignorava il profilo. Poi separato nei due inchiostri e vettorializzato con potrace (`_sorgente/logo/`), alleggerito con SVGO: logo intero, versione orizzontale per la testata (gli stessi tracciati accostati), marchio, versione bianca; PNG trasparenti per l'icona del sito (`villaeidos-icona-512.png`) e per l'uso esterno. Il disegno tracciato coincide con l'originale a vista.
- **Foto** (cinque, tutte dal telefono), un trattamento unico per tutte: bianco riportato verso il neutro, saturazione all'88 %, un filo di calore, contrasto morbido, nitidezza leggera alla misura vera, grana fine uguale. Nessun ingrandimento nei file; sul sito mai oltre 1,25 volte la misura vera, in cornici medie.
  - *sale riunioni* (1600 x 1200): ritagliata a 1080 x 810. Via la scritta "HONOR 400" e anche la tigre del murale, che porta un simbolo disegnato sul casco poco adatto a una pagina d'affari.
  - *uffici*: ritagliata a 480 x 360, via il cestino giallo e lo scatolone.
  - *sale d'attesa*: raddrizzata secondo l'EXIF (orientamento 6), intera.
  - *sala conferenze* e *reception*: intere, 640 x 480.
- **Il posto della foto della villa**: in apertura c'è un'Immagine di Elementor che oggi mostra un fregio di pietra con "Villa · Barchessa · Giardino" in maiuscole romane (reso con il carattere del sito, 3200 px, 22 KB; versione 5:4 per il telefono). Si cambia con un clic: provato nel WordPress locale, la foto nuova riempie la fascia 12:5 al computer e 5:4 al telefono (`screenshot/prove/foto-villa-sostituita.jpg`).

## Caratteri e colori

- **Brygada 1918** (SIL OFL) per i tre momenti forti: titolo d'apertura (118 px a 1440), Villa, Barchessa, Giardino, Parcheggi (150 px), il telefono della richiesta (118 px). **Pontano Sans** (SIL OFL) per tutto il resto, `h2` di servizio a 44 px. Tutti e due nel tema, 22 e 23 KB. Riga aggiunta in `_metodo/professionale/alto/REGISTRO-CARATTERI.md`: nessuna delle due è in altre home o nelle liste della guida.
- Carta #F3F1EC e pietra #E4DED2 per quasi tutta la pagina, inchiostro #1E231F; il verde del logo solo come accento (fuoco, passaggio sui link), il verde scurito #2E6A33 per il bottone, il verde notte #1F3A23 per l'unico campo pieno ("per chi è").

## Prove (WordPress 7.1.4, Elementor 4.4.1 gratuito, SQLite, PHP 8.3, in locale)

- **Installazione** con `installa-su-server.sh` su un WordPress vuoto: tema, Elementor da WordPress.org, 7 immagini, 3 pagine in Elementor, Home iniziale, `/privacy/` e `/cookie/`. Rilanciata: nessun doppione. Bottone *Installa il sito* del pannello: stesso esito. Una pagina modificata a mano resta com'era; con "riscrivi" torna quella del tema. Lanciato da WP-CLI senza utente, prima Elementor rifiutava il salvataggio: l'installatore ora lavora come il primo amministratore.
- **Editor di Elementor**: la Home si apre con 40 contenitori e 52 widget, le sezioni hanno un nome nel pannello Struttura, clic sul titolo apre il pannello Titolo, clic sul fregio apre il pannello Immagine con "Scegli l'immagine". Nessun errore di console (`screenshot/prove/editor-elementor.jpg`).
- **Anteprima uguale a WordPress**: pagina ferma, a 390, 768, 1440 e 1920 stesse altezze (8363, 8478, 7449, 8201 px) e circa 110 pixel diversi su milioni (una riga di 1 px nel modulo).
- **Scorrimento laterale ed errori**: Home, Privacy e Cookie a 390, 768, 1024, 1440 e 1920, con il movimento, con "riduci movimento" e senza JavaScript: nessuno scorrimento orizzontale, nessun errore, nessuna richiesta fallita. Con "riduci movimento" la pagina è completa e ferma (`screenshot/prove/riduci-movimento-1440.jpg`); senza JavaScript anche.
- **Modulo**: si ferma sul nome, sull'email e sulla presa visione dell'informativa; compilato prepara la mail per eidos@eco-management.it con oggetto "Richiesta di disponibilità, Sala conferenze, Prova S.r.l." e la data in formato italiano. Dopo aver visitato le tre pagine e usato il modulo: zero cookie, niente in `localStorage` e `sessionStorage`.
- **Pesi al primo caricamento** (senza compressione, come li dà `php -S`; il browser di prova carica anche le foto pigre entro circa 3000 px, quindi i numeri sono per eccesso):

| | 1440 | 1440, schermo doppio | 390 | 390, schermo triplo |
|---|---|---|---|---|
| WordPress | 795 KB | 858 KB | 761 KB | 873 KB |
| Anteprima | 401 KB | | 367 KB | 479 KB |

  Limiti chiesti: 1,5 MB a 1440 e 1 MB a 390. In WordPress 444 KB sono script, quasi tutti di Elementor (jQuery compreso) e 121 KB del kit dei movimenti.
- **Video** con `_metodo/highend/kit/registra.mjs`, 1440 e 390, nessun errore di script: `screenshot/foglio-1440.jpg`, `foglio-390.jpg`. Guardando i fotogrammi a piena misura ho corretto: la discendente della "g" di "convegni" tagliata dalla maschera delle righe a fine movimento (ora le maschere si allungano e niente si sposta), la mia variabile `--gap` che Elementor azzerava, il telefono della testata attaccato alla parola "Chiama", i titoli grandi del luogo che uscivano nel carattere del testo.
- **Segnali** (`_metodo/kit/segnali.sh` sulla Home in WordPress): una soglia bloccante su dieci, l'**area delle foto: 19,4 %** contro il 35 % (mancano le foto della villa: è la prima cosa da chiedere). Da guardare: una sola misura di `h2` (le quattro parole del luogo sono `h3` a 150 px) e nessun contenuto datato (il testo non ha date). Tutto il resto OK: nessun carattere delle liste, nessun monospazio, nessuna etichetta sopra i titoli, nessuna freccia, 15 filetti, nessuna dissolvenza.

## Voto onesto (griglia del punto 7 di `SISTEMA.md`)

| Voce | Peso | Voto | Perché |
|---|---|---|---|
| Design | 40 % | 7 | Tipografia forte e pulita (il titolo d'apertura, le quattro parole a 150 px), palette sobria presa dal logo e dalla pietra, griglia coerente, un solo campo pieno. Ma la pagina è quasi tutta testo: le uniche foto sono cinque interni dal telefono, piccoli e con oggetti d'ufficio, e in apertura c'è un fregio al posto della villa. |
| Creatività | 25 % | 6 | L'idea del luogo scritto come un'iscrizione regge e non somiglia a un modello, ma la sezione firma non ha la sua prova fotografica e il gesto d'apertura è solo il titolo che sale. |
| Usabilità | 25 % | 8,5 | Si capisce in cinque secondi cosa offre e dove; telefono in testata e in apertura, un tocco sul telefono; modulo semplice; telefono progettato, non rimpicciolito; pagina ferma e completa con "riduci movimento". |
| Contenuto | 10 % | 6 | Fatti veri e solo del cliente, ma pochi: niente capienze, servizi, orari, nomi o date. |
| **Media pesata** | | **7,0** | |

Il costruttore tende a darsi 0,7 in più del giudice: il voto atteso di un estraneo è **intorno a 6,5**. Sotto la soglia di 8. **Almeno il 60 % della distanza dipende dalle foto**: con la facciata, la barchessa e il giardino in apertura e nella sezione firma il sito passa da "bel sito tipografico" a "sede in villa", senza ridisegnare niente.

I cinque interventi che valgono di più, in ordine:
1. La foto della facciata (o dal drone) nella fascia d'apertura: un clic in Elementor.
2. Una foto della barchessa e una del giardino accanto alle parole "Barchessa" e "Giardino" della sezione firma.
3. Rifare gli interni senza oggetti estranei (scatoloni, cestino, sedia da gioco) e la sala conferenze piena, con luce di giorno.
4. Due o tre fatti in più dal cliente: capienza delle sale, servizi compresi, orari.
5. Un fatto datato o con un nome (l'epoca della villa, un convegno che c'è stato, un'azienda che ha sede lì) per la sezione firma.

## Foto da chiedere

Tutte orizzontali, a piena risoluzione (almeno 3000 px di lato lungo), file originali e non mandati via WhatsApp, giornata di sole o luce piena coperta, nessuna persona riconoscibile senza liberatoria.

1. **Facciata della villa**, frontale, da qualche metro di distanza, con il giardino davanti: è la foto d'apertura (fascia 12:5, soggetto al centro).
2. **Barchessa**, l'esterno intero: le arcate o le finestre ad arco che si vedono dall'interno della sala conferenze.
3. **Giardino**: gli alberi centenari, un vialetto, la villa che si vede tra il verde.
4. **Drone**: villa, barchessa, giardino e parcheggi insieme, da circa 40-60 m (con un pilota autorizzato): fa capire in un colpo la proprietà e la posizione.
5. **Sala conferenze piena** durante un convegno vero (con il permesso dell'organizzatore), dal fondo della sala.
6. **Parcheggi**: un'immagine larga che mostri quanto sono ampi.
7. In più, se si può: sale riunioni con il tavolo apparecchiato per una riunione, un ufficio pronto per un inquilino (senza oggetti personali), la reception con la luce accesa, dettagli architettonici (soffitti, pavimenti, colonne).

## Domande per il cliente

1. **Foto esterne**: avete foto della villa, della barchessa, del giardino e dei parcheggi? Possiamo organizzare un servizio fotografico e una ripresa con il drone?
2. **Ragione sociale e partita IVA** della società che gestisce Villa Eidos (vanno nel piede e nell'informativa privacy). Anche la sede legale e i fornitori di hosting e posta, per completare l'informativa.
3. **Capienza delle sale**: quante persone stanno nella sala conferenze e in ogni sala riunioni? Quante sale riunioni ci sono?
4. **Servizi inclusi**: wifi, proiettore o schermi, impianto audio e microfoni, videoconferenza, catering o coffee break, pulizie, reception presidiata?
5. **Uffici**: si affittano a lungo termine? Anche come sede legale o domiciliazione? Arredati?
6. **Orari**: di apertura della struttura e della reception; le sale si prenotano anche la sera o nel fine settimana?
7. **Referente**: c'è una persona da indicare per le richieste (nome, ruolo, telefono diretto)?
8. **I tre indirizzi**: Via Battaglia 67, via Colombo 2 e via Colombo 6A sono tre ingressi? A cosa porta ciascuno (villa, barchessa, parcheggi)?
9. **Un fatto con una data o un nome**: l'epoca o il nome storico della villa, un evento ospitato, un'azienda che ha sede lì (con il permesso).
10. **Hosting**: il dominio è su Aruba; c'è già un piano di hosting (Linux o WordPress) o va attivato? Chi gestirà il sito dopo la consegna?
