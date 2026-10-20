# Autotrasporti Giolo Idamer: home finale "Verde Giolo"

Pagina: `sito/index.html` (statica, si apre anche con file:///). Immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh`, che lancia `finale_img.py` (immagini), copia `finale_index.html` in `sito/index.html`, copia caratteri e logo, e lancia `finale_shoot.mjs` (screenshot). La prova di tastiera, tocco e contrasto è `finale_tasti.mjs`; `finale_larghezze.mjs` misura lo scorrimento da 320 a 2560 px e i collegamenti; `finale_piede.mjs` le colonne del piede e la foto "Oggi" già caricata.

Altezza: 5418 px a 1440, piede compreso (prima di questo passaggio 5138 px). A 390 è alta 6607 px con il piede chiuso.

## Idea

La livrea è l'identità, e il mestiere è l'ultimo metro. Nella prima schermata c'è un solo oggetto: il convoglio di oggi (Volvo FH, semirimorchio ribassato e autogru elettrica Ormig T40 indoor), scontornato sulla carta, verde con la scritta GIOLO gialla, a tutta la griglia. Tre legende con filetti sottili salgono dalle parti del convoglio verso il titolo, come in una tavola tecnica, con le misure vere della scheda (DIN 40 t, braccio 13 m, ingombro 2,20 × 2,39 m). La stampa d'archivio dei cinque autocarri, con l'interruttore "Allora / Oggi", è scesa in una sezione storia a metà pagina. Il resto è un archivio d'impresa ordinato:
- i cinque servizi in un indice a righe, chiuso da una frase sulle tre polizze;
- il parco mezzi in un indice a righe;
- la storia, con la stampa d'archivio e l'interruttore;
- i tre lavori con le didascalie;
- la chiusura con la foto delle origini.

Con il nome di un concorrente la pagina non regge: convoglio, colori e scritte sulle portiere sono solo loro.

## Prime due schermate

**1440 x 900**
- Testata chiara: il logo sulla sua targa verde, quattro voci (Servizi, Parco mezzi, Lavori, Contatti) e il telefono a destra.
- Il titolo "Dal 1961 spostiamo i macchinari delle aziende che non possono fermarsi" sta sulle prime 7 colonne, su tre righe a 72 px, in Hubot Sans 580 stretto all'84 %.
- Sotto: la riga "Spostamento di macchinari industriali, autogru con operatore e trasporti eccezionali. A Saonara, in provincia di Padova." e "Richiedi un preventivo" (sottolineato verde) con "o chiama lo 049 640544".
- Il convoglio scontornato occupa le 12 colonne, 1312 x 324 px, da 539 a 863 px: tutto dentro la finestra, con la carta intorno. Nessuna foto rettangolare a fondo pieno nella prima schermata.
- Le legende: "Ormig T40 indoor" e "Semirimorchio ribassato" salgono nelle colonne libere a destra del titolo (filetti da 300 e 156 px), "Volvo FH" sta sopra la cabina.
- Seconda schermata: "Cinque servizi, nessun subappalto", la riga sull'azienda di famiglia e l'indice dei cinque servizi.

**390 x 844**
- Il logo, il telefono e il bottone "Menu" (aria-expanded).
- Il titolo su quattro righe a 41 px (34 px a 320), la riga, "Richiedi un preventivo" e "o chiama lo 049 640544".
- Il convoglio al vivo, nel taglio sull'Ormig con il gancio a circa 45 px dal bordo sinistro, e sotto le legende in elenco (solo le parti che si vedono nel taglio).

**1024 e 768**: titolo, riga e preventivo; il convoglio intero a tutta la griglia; sotto, le tre legende in un elenco a tre colonne con un filetto sopra. Le legende sull'immagine ci sono solo da 1181 px in su.

## Cosa è cambiato in questo passaggio (giudizio cieco 56,5 su 80)

- **Apertura rifatta**: via la scansione d'archivio, che era morbida e veniva ingrandita a 2x. L'oggetto della prima schermata è il convoglio scontornato, raddrizzato di 1,0 gradi (misurato sul fondo di sette ruote nella maschera, `finale_img.py`), con le legende che salgono verso il titolo. Il gesto non è più "titolo sopra e foto rettangolare sotto".
- **Interruttore "Allora / Oggi"** spostato nella sezione storia ("Siamo partiti con mezzi semplici e tanta voglia di fare", frase loro dalla pagina `azienda`):
  - la stampa sta sulle prime 8 colonne e non supera 864 px CSS (massimo 890), così il file da 1780 px basta anche a 2x;
  - "Oggi" è rifilata sulle cabine in primo piano (due Scania, una Scania e la Volvo Globetrotter), 1080 x 540, con la fila delle calandre a metà altezza come in "Allora";
  - le due foto hanno lo stesso trattamento finale: nero vero, saturazione 0,95, maschera di contrasto;
  - a 1440 didascalia e interruttore stanno nella colonna a destra, in basso; da 1180 px in giù stanno nella stessa riga sotto la foto (didascalia a sinistra, interruttore da 220 px a destra); a 640 e meno l'interruttore va sopra la foto, a tutta larghezza;
  - la foto "Oggi" passa a loading=eager dopo l'evento load: al primo clic è già pronta (verificato: complete, 864 px).
- **Scansione "Allora"**: niente più ombre alzate. Il nero va a 6-7 (prima 20-22), l'1 % più scuro dei pixel sta sotto 9, maschera di contrasto con raggio 1,2 e quantità 60 %.
- **Preventivo**: "Richiedi un preventivo" ora è nella prima schermata e nella chiusura, sotto gli orari, oltre che nel piede.
- **Polizze**: una frase sola in inchiostro, grande quanto i titoli dei servizi, sulle colonne 1-8: "Ogni carico ha tre polizze distinte: RC Vettore, All Risks sul valore reale e Al Gancio, che lo copre anche mentre è appeso." Sotto, il link alle coperture. La riga sull'art. 1696 c.c. passa alla pagina `assicurazioni.html`.
- **Trattori**: "fino a 3,00 m di larghezza e 4,30 m di altezza, o 25 m di lunghezza", come dice la fonte.
- **Titolo**: "Dal 1961 spostiamo i macchinari delle aziende che non possono fermarsi" (la logica di prima era storta).
- **Piede**: Facebook e Instagram sono nella riga legale, prima di Privacy e Cookie; la colonna Contatti è larga 3 colonne e la PEC sta sulla riga dell'etichetta. Le cinque colonne a 1440 sono alte uguali (237 px).
- **Respinto**: limitare la foto seppia della chiusura a 500 px CSS. Il committente vuole nella chiusura una foto grande; il file da 1000 px a 760 px CSS è nitido a 1x e appena morbido a 2x. Va a tutta altezza quando arriva la scansione a 600 dpi (LEGGIMI).

## Caratteri e colori

**Caratteri**
- Hubot Sans: titoli, interruttore e titoletti del piede, stretto (84-92 %) e semigrassetto (580-650).
- Mona Sans: testi, numeri, telefono e misure.
- Sono una superfamiglia di GitHub con Degarism Studio, distribuita da Google Fonts con licenza SIL Open Font License 1.1. I testi della licenza sono in `sito/fonts/OFL-Hubot-Sans.txt` e `sito/fonts/OFL-Mona-Sans.txt`, scaricati da github.com/google/fonts. I file woff2 sono serviti dalla pagina (`sito/fonts/`). "Hubot" e "Mona" sono nomi riservati: i file non vanno modificati e poi ripubblicati con quei nomi.
- Perché questi: Hubot ha le forme squadrate e meccaniche delle lettere del logo GIOLO e dei titoli stretti di Liebherr e Scania (riferimenti in `01-analisi.md`, sez. 7). Cabinet Grotesk, proposto nell'analisi, è nella lista b della guida.
- Numeri: le cifre di Hubot hanno lo zero barrato, che fa codice. Per questo misure, portate e telefono sono in Mona Sans con cifre allineate proporzionali ("3,00 × 4,30 m o 25 m").

**Colori**
- carta #F4F2EC, inchiostro #161A17 (15,7:1), grigio dei testi secondari #4B504C (7,4:1);
- verde livrea #0F5A32: solo il piede è un fondo pieno; è anche il colore di link e telefono della chiusura (7,4:1 su carta);
- giallo del logo #FFDC1B, solo sul verde (6,1:1);
- testo chiaro del piede #DCE3D9 su verde (6,3:1);
- il verde del logo #2BA041 è solo nella cornice del logo.

## Interazione

- "Allora / Oggi", nella sezione storia, sono due bottoni veri con aria-pressed. Clic, tocco, Tab e Invio, e le frecce sinistra e destra cambiano la foto e la didascalia di netto, senza dissolvenza (verificato con `finale_tasti.mjs`: l'interruttore resta fermo nei due stati, bottoni da 174 x 44 px a 390). L'unica transizione è il colore del bottone toccato (0,12 s), tolta con prefers-reduced-motion.
- Non ci sono animazioni allo scorrere né effetti sul cursore.
- A 390 il menu è un bottone con aria-expanded.
- Il piede si apre a fisarmonica: quattro bottoni da 52 px con aria-expanded e aria-controls. Senza JavaScript le colonne restano aperte.

## Sezioni

1. **Apertura**: il convoglio scontornato con le tre legende, il titolo e il preventivo.
2. **Servizi**: "Cinque servizi, nessun subappalto". L'indice a righe con filetti dei cinque servizi, ogni riga è un link a `servizi/*.html`. Sotto, la frase sulle tre polizze e il link alle coperture.
3. **Parco mezzi**: "Tre autogru elettriche per lavorare dentro i reparti", con un indice a righe e link a `mezzi/*.html`: Motrici con gru Cormach, da 5 a 33 t, 5 mezzi / Autogru elettriche Ormig, 25, 35 e 40 t, 3 mezzi / Trattori per trasporti eccezionali, fino a 3,00 m di larghezza e 4,30 m di altezza, o 25 m di lunghezza, 2 mezzi.
4. **Storia**: "Siamo partiti con mezzi semplici e tanta voglia di fare", la stampa d'archivio 2:1 con la didascalia e l'interruttore "Allora / Oggi".
5. **L'ultimo metro**: tre foto con lo stesso taglio 4:3 (700 x 525), la stessa luce media e la stessa saturazione, mai sopra i 700 px dell'originale. Le didascalie dicono luogo e operazione, senza tonnellate perché nessuna è confermata.
6. **Chiusura "b con foto"**:
   - la foto seppia è a filo del bordo sinistro (7/12) e la didascalia è allineata al margine della griglia;
   - a destra, la frase loro "Dopo 65 anni, la nostra storia parla per noi" e "Siamo sempre pronti a raccontartela di persona." (dalla pagina `azienda`);
   - poi i recapiti: il telefono verde a 44 px con tel:, "PEC" con mailto:, l'indirizzo con il link a Google Maps, gli orari e "Richiedi un preventivo".
7. **Piede**:
   - il logo con una riga su chi sono e "Richiedi un preventivo";
   - quattro colonne: Servizi, Parco mezzi, Azienda, Contatti;
   - la riga legale: ragione sociale, P.IVA e C.F., REA, poi Facebook, Instagram (in parole), Privacy e Cookie (iubenda). Non c'è capitale sociale, perché è una snc.
   - **Niente newsletter**: Giolo lavora per aziende che chiamano quando hanno un macchinario da spostare. Non va a fiere, non ha cataloghi né clienti privati, e le quattro notizie del sito sono guide scritte per Google, non novità da mandare per email.

## Foto

Sono tutte dell'azienda, da `assets/originali/`, scaricate da giolo.it. Non ci sono foto di repertorio né immagini generate. I diritti vanno confermati con l'azienda (vedi LEGGIMI). Il trattamento è uno solo, in `finale_img.py`: bianco verso la carta, nero vero (niente ombre alzate sulle due foto della storia), saturazione appena ridotta tenendo il verde, maschera di contrasto leggera, nessuna grana.

| In pagina | Originale | Misure pubblicate |
|---|---|---|
| Convoglio, apertura (`convoglio-*.webp`) | `IMG_4057.jpeg`, 1920x1440 | raddrizzato di 1,0 gradi, scontornato (maschera di `proto_b_mask.py`), 1000/1400/1870 (1312 px CSS a 1440); taglio Ormig per il telefono 640/960 |
| Allora (`allora-*`, `allora-q-*`) | `300---Foto-giolo-aut.jpg`, scansione 1920x1340 | 2:1 a 760/1100/1780 (al massimo 864 px CSS); quadrato a 600/780/1100 |
| Oggi (`oggi-*`, `oggi-q-*`) | `IMG_1226-3.jpeg`, 1920x900, dall'alto | 2:1 sulle cabine a 760/1080; quadrato 540 |
| Lavori (`lavoro-*`) | `4196854194---…` (Padova), `196---…` (bobina), `319---…` (reparto), tutte 700x600 | 4:3 a 480/700 |
| Chiusura (`origine-*`) | `7361166001---…`, 1000x600, seppia | 520/760/1000 |

La foto della chiusura non compare altrove nella pagina. È dell'azienda, quindi non è usata in nessun'altra home della campagna.

## Controlli

- **Scorrimento orizzontale**: scrollWidth uguale a innerWidth a 320, 360, 390, 414, 480, 640, 641, 768, 900, 901, 1024, 1180, 1181, 1280, 1440, 1680, 1920 e 2560 px (`finale_larghezze.mjs`). `finale_shoot.mjs` non trova elementi fuori finestra a 320, 390, 768, 1024, 1440 e 1920.
- **Guardati a pezzi**: 1440 e 390 a pagina intera, 1024, 768, 320 e 1920, la prima schermata a 1200 (le legende non toccano il preventivo), lo stato "Oggi" a 1440 e 390, il menu e il piede aperti a 390. Nessuna sovrapposizione.
- **Interazione** (`finale_tasti.mjs`): frecce destra e sinistra, Tab e Invio, tocco a 390 cambiano stato, aria-pressed e didascalia; l'interruttore resta alla stessa altezza nei due stati. Menu e fisarmonica del piede con aria-expanded; senza JavaScript le colonne del piede restano aperte.
- **Collegamenti**: tel:+39049640544, mailto:gioloautotrasporti@pec.it e il link a Google Maps per via Irpinia 65 (8 collegamenti in tutto tra testata, apertura, chiusura e piede).
- **Lineetta lunga U+2014**: assente in pagina, negli script, in questa nota e nel LEGGIMI. `build_finale.sh` si ferma se la trova.
- **`segnali.sh`** (kit, a 1440): 17 soglie su 18 sono a posto.
  - L'area foto è al 20,8 % contro una soglia del 35 % (prima 25,3 %). È voluto: il convoglio scontornato conta solo per la sua sagoma, e le altre foto vere esistono quasi tutte a 700 px; la scansione d'archivio regge fino a circa 890 px CSS. Allargarle vorrebbe dire ingrandirle oltre l'originale, cioè l'errore segnalato dal giudice. Quando arriveranno le foto rifatte dal vero (LEGGIMI), i lavori e la storia potranno salire a tutta larghezza.
  - Il resto: tre misure di H2, nessun titolo a sinistra con il paragrafo a destra, 14 filetti, 0 frecce, 0 numeri giganti, 0 numerazioni, due fasce di fondo, superfamiglia unica (Mona 78 %, Hubot 22 %).
- **Divieti del committente**: nessun gradiente, nessuna emoji, niente Inter, nessuna card con bordo colorato, niente vetro, nessun badge sopra il titolo, nessuna icona Lucide, niente dissolvenze allo scorrere o effetti sul cursore, nessun corsivo serif.
- **Contrasto AA** verificato su tutte le coppie (sopra, in Colori): inchiostro 15,7, grigio 7,35, verde su carta 7,42, chiaro su verde 6,34, giallo su verde 6,13.
- **Dati**: tutti da `01-analisi.md` e dal crawl. Nuovi in pagina: l'ingombro della Ormig T40 "2.20 x 2.39 m" (scheda `i-nostri-mezzi`), la frase "Siamo partiti con mezzi semplici e tanta voglia di fare" (pagina `azienda`), "fino a 3.00 mt. di larghezza e 4.30 di altezza oppure 25 mt. di lunghezza" (home). Le cose da confermare sono nel LEGGIMI.
