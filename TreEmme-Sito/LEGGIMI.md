# Tre Emme Manufatti: proposta di nuova home

Proposta non richiesta di una nuova homepage per Tre Emme Manufatti S.r.l., Saonara (PD). Solo la home.

- Pagina: `sito/index.html` (statica, si apre con file:///). Immagini in `sito/img/`, carattere in `sito/fonts/`.
- Screenshot e nota di progetto: `screenshot/home/` (`NOTA.md`, `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`).
- Per rifare tutto: `sh _prova/script/build_finale.sh` (con `controlli` anche le misure 320, 768, 1024, 1280, 1920 in `_prova/controlli/`). Sorgente della pagina: `_prova/script/finale/index.html`. Prove dell'interazione e delle larghezze: `node _prova/script/prova_finale.mjs file:///.../sito/index.html <cartella>`; misure del codice nell'apertura: `node _prova/script/misura_codice.mjs file:///.../sito/index.html`.
- Analisi con le fonti: `01-analisi.md`. Prototipi e voto del giudice: `_prova/home/a/` (scelto) e `_prova/home/b/`.

## Da confermare con l'azienda

Nulla di questo è scritto in pagina come fatto incerto; sono le cose da chiedere prima di pubblicare.

- **Codici e pesi**: DYHB-12,7+S599BEPS+AAL24 e le altre quattro varianti Dynamic Happy, 1,45 kg; Dynamic-X Light DYX-12,7+S595NEPSX+OAL24, 1,50 kg, portata 100 kg. Sono quelli del listino di oggi? Le foto mostrano davvero il corrimano AAL24 a 6 linguette e lo pneumatico indicato?
- **Righe sotto il codice** ("Raggi blu / 12 × Ø3,5", "Cuscinetti / Ø12,7 mm", "Pneumatico blu e nero / antiforatura EPS", "Corrimano / 6 linguette"): sono ricavate dalla scheda Dynamic Happy; vanno bene così o preferiscono i nomi del listino? In particolare: il 12,7 del codice è il diametro dei cuscinetti (colonna "Ø Cuscin." della scheda)? Per le varianti rossa, nera e bianca la scheda dice "nero EPS+Reflex": la banda riflettente va nominata?
- **Ruote anteriori**: la foto è la ruotina 125 mm in alluminio con gomma TPU (12524/12532ALPU); la riga dice "con anello in poliuretano, con pneumatico o con gomma TPU", dalle schede di oggi.
- **Garanzie**: 3-6 mesi per le aziende, 2 anni per i privati, 10 anni sui difetti (pagina Condizioni di vendita). Sono ancora queste?
- **Famiglia**: la frase dice che con Gianfranco Berto ci sono Laura, Sara e Manola Berto (pagina Contatti) e che l'idea fu "di un giovanissimo Gianfranco Berto e di sua moglie" (pagina Azienda). Va bene nominarli così? Il nome della moglie si può aggiungere?
- **Anno**: 1981 è la fondazione (pagina Azienda); il Registro Imprese dà l'iscrizione al 30/09/1993. In pagina c'è solo 1981.
- **ISO 9001**: non è scritta in pagina. Se è valida (ente, numero, scadenza, su quali prodotti: Emiplegico Light e ruote a dischi in alluminio con pneumatico) può entrare come prova nella sezione della famiglia.
- **Clienti e mercati**: chi sono (produttori di carrozzine, ortopedie, privati), si possono nominare, dove esportano. Una storia di un cliente con nome sarebbe la prova più forte.
- **Orari** e se ricevono privati in sede: oggi non sono pubblicati, quindi la chiusura non li ha.
- **YouTube**: il canale @BIRBA0507 ("Tre Emme Manufatti srl") è quello ufficiale? È l'unico social nel piede; Facebook, Instagram e LinkedIn non risultano.
- **Logo**: serve il vettoriale originale e il nome del carattere della scritta (sembra Ubuntu Bold) e del corsivo "Wheels for life!".
- **Newsletter "Novità dall'officina"**: va collegata a un servizio (Brevo, Mailchimp o simili) con doppio consenso e registro dei consensi. Finché non si collega il modulo non invia nulla: ha `data-collegato="no"` e dopo l'invio risponde "Iscrizione non ancora attiva: scrivi a info@3emme.com per ricevere le novità" (con il link `mailto:`). Quando è collegato si mette `data-collegato="si"` e si sostituisce il gestore di invio con la chiamata al servizio. Testo dell'informativa da far rivedere.
- **Testi del sito di oggi da sistemare comunque**: refusi ("Rehabilitazione", "Ruotea dischi", "Emipligico"), sitemap con 39.973 indirizzi spam, pagine d'errore IIS pubbliche, cambio lingua in errore 500.

## Pagine del sito nuovo a cui puntano i link

Menu e piede puntano a sezioni della home (`#ruote`, `#azienda`, `#contatti`) e a queste pagine, da fare:

- Ruote: `ruote/a-raggi/`, `ruote/anteriori/`, `ruote/10-16/`, `ruote/carrozzine-elettroniche/`, `ruote/fat-wheel/`, `ruote/golf-wheel/`, `ruote/poliuretano/`
- Componenti: `componenti/` (indice), `componenti/freni/` (con i freni anti-ritorno), `componenti/forcelle/`, `componenti/mozzi/` (mozzi e corrimano), `componenti/assi-sgancio-rapido/` (assi e boccole), `componenti/differenziali/`, `ricambi/`, `altre-applicazioni/`
- Per ordinare: `come-ordinare/`, `note-tecniche/`, `condizioni-di-vendita/`, `area-riservata/` (oggi `/Geweb/Autentica.asp`), `pagamento/` (oggi `/pay.asp`)
- Azienda: `azienda/`, `news/`
- Legali: `privacy/`, `cookie/`

## Foto da rifare dal vero

Le foto prodotto di oggi reggono la proposta (voti 6-8 su 10), ma per il sito vero conviene una giornata di scatti, tutti sullo stesso fondo grigio chiaro uniforme (carta senza fine, niente pieghe), luce morbida da sinistra e un pannello di schiarita, obiettivo 100 mm macro, f/11, stampa in RAW.

1. **Dynamic Happy nei cinque colori** per il gesto dell'apertura: stessa ruota, stesso cavalletto, stessa angolazione (tre quarti, 15° circa), camera fissa sul treppiede, si cambia solo la ruota. Oggi il mozzo si sposta di qualche millimetro tra un colore e l'altro e al cambio di colore la ruota "salta" un poco.
2. **Mozzo Dynamic-X** da vicino: lo scatto di oggi (2130 px) è morbido già a 1:1 e ha la flangia dietro fuori fuoco, per questo in pagina è tagliato sulla flangia davanti e mostrato a 966 px. Da rifare con più profondità di campo (focus stacking su 5-8 scatti) perché anche la flangia posteriore sia nitida, almeno 4000 px di lato, luce meno bruciata sull'alluminio, cavi a 12 e a 18.
3. **Le tre famiglie** (ruota a raggi, anteriore, a dischi) e la 200×45 in poliuretano: ruote in piedi, appoggiate sul fondo, stessa altezza della camera, così l'ombra vera è uguale per tutte.
4. **Reparto**: torni, stampaggio del poliuretano, montaggio dei raggi e la famiglia Berto al lavoro, in luce naturale. Servono per la sezione della famiglia, che oggi è solo testo.
5. **Chiusura**: un cliente vero in carrozzina con ruote Tre Emme, all'aperto, con liberatoria, in verticale o quasi quadrata. Prende il posto della foto di repertorio del lago: oggi è tagliata in alto perché la carrozzina di altra marca resti fuori quadro, e sotto ha la didascalia "Foto indicativa".

## Licenze

- Carattere: Saira (Omnibus-Type), SIL Open Font License 1.1, servito dalla pagina (`sito/fonts/saira-var-latin.woff2`, licenza in `sito/fonts/OFL.txt`, copia in `assets/fonts-licenze/`). La scritta del logo è in tracciati da Ubuntu Bold (Ubuntu Font Licence 1.0, scaricato da Google Fonts in `_prova/crawl/esterni/font-ubuntu/`).
- Foto dell'azienda: da http://www.3emme.com/, restano di Tre Emme Manufatti; usate solo in questa proposta a loro indirizzata.
- Foto della chiusura: Zachary Kyra-Derksen, Unsplash, Unsplash License (pagina e verifica in `assets/CREDITI.md`). La persona è riconoscibile; la carrozzina, di altra marca, è tagliata fuori. Sotto la foto c'è la didascalia "Foto indicativa", e va sostituita prima di pubblicare.
- Nessuna immagine generata dall'IA, nessun marchio concorrente leggibile in primo piano.

## Loghi

- `sito/img/logo-testata.svg` e `logo-piede.svg`: il marchio a mezza ruota è il PNG originale del sito (`assets/originali/logo-marchio-184.png`, ritagliato a 176x106 px, colori originali) incorporato nell'SVG; la scritta "Tre Emme Manufatti" ("S.r.l." nel piede) è in tracciati da Ubuntu Bold, blu #0A3F94. Nella testata il marchio è alto 40 px (2,6x), nel piede 52 px (2x). Con il vettoriale vero dell'azienda si sostituisce tutto e il marchio diventa nitido a qualunque misura.
- `sito/img/favicon-48.png` e `favicon-180.png`: dal marchio originale. Il favicon di oggi alla radice del loro sito è l'icona di default di IIS.
- Il motto "Wheels for life!" non è ricostruito come corsivo rosso: sta in testo nella riga del piede.
