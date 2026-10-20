# Autotrasporti Giolo Idamer: home finale "Verde Giolo"

Pagina: `sito/index.html` (statica, si apre anche con file:///). Immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh`, che lancia `finale_img.py` (immagini), copia `finale_index.html` in `sito/index.html`, copia caratteri e logo, e lancia `finale_shoot.mjs` (screenshot). La prova di tastiera, tocco e contrasto è `finale_tasti.mjs`.

Altezza: 5138 px a 1440, piede compreso (il prototipo B era alto 5235 px). A 390 è alta 6101 px con il piede chiuso.

## Idea

La livrea è l'identità. La flotta di Giolo era già verde quarant'anni fa, con "Idamer GIOLO" scritto sulle portiere, e oggi è verde vivo con la scritta GIOLO gialla. Nella prima schermata c'è una sola foto, la stampa d'archivio dei cinque autocarri, presentata come una stampa conservata bene con la carta intorno. Accanto ci sono la didascalia e un solo interruttore, "Allora / Oggi", che passa di netto alla flotta di oggi nella stessa inquadratura 2:1. Il resto della pagina è un archivio d'impresa ordinato:
- i cinque servizi in un indice a righe;
- il convoglio di oggi scontornato, con le legende;
- i tre lavori con le didascalie;
- la chiusura con la foto delle origini.

Con il nome di un concorrente la pagina non regge, perché foto, colori e scritte sulle portiere sono solo loro.

## Prime due schermate

**1440 x 900**
- Testata chiara: il logo sulla sua targa verde, quattro voci (Servizi, Parco mezzi, Lavori, Contatti) e il telefono a destra.
- Il titolo "Dal 1961 spostiamo quello che le aziende non possono fermare" va su due righe a 88 px, in Hubot Sans 580 stretto all'84 %.
- Sotto, una riga: "Spostamento di macchinari industriali, autogru con operatore e trasporti eccezionali. A Saonara, in provincia di Padova."
- La stampa d'archivio:
  - non è più al vivo: sta sulle prime dieci colonne della griglia, 1088 x 544 px (2:1), allineata al titolo;
  - è tutta dentro la finestra (da 344 a 888 px) e la carta resta libera intorno;
  - la scansione non supera mai i 1088 px CSS: i file sono a 760, 1100 e 1780 px, e 1780 è la misura nativa del ritaglio;
  - nelle due colonne di destra (192 px), dall'alto: un filetto, la didascalia "Allora" e sotto l'interruttore. L'interruttore resta fermo a 516 px nei due stati, perché le due didascalie occupano la stessa cella.
- Seconda schermata: "Cinque servizi, nessun subappalto", la riga sull'azienda di famiglia e l'indice dei cinque servizi.

**390 x 844**
- Il logo, il telefono e il bottone "Menu" (aria-expanded).
- Il titolo su tre righe a 41 px, la riga, l'interruttore a tutta larghezza (bottoni da 174 x 44 px).
- La foto in taglio quadrato al vivo e la didascalia. Ha lo stesso trattamento colore del 1440.
- Lo stato "Oggi" ha un quadrato sulle cabine, con poco asfalto.

**Cosa cambia rispetto al prototipo B**
- L'apertura non è più "titolo sopra e fascia a tutta larghezza" (il gesto di Bertolin Antonio e 3Esse). Ora è una stampa con i margini, con la didascalia e il comando sul lato.
- La dominante gialla della scansione è tolta (`finale_img.py`):
  - curva per canale fissata su punti misurati: il cielo da 251/236/191 diventa 238/236/228, la ghiaia da 237/212/167 diventa 224/221/210;
  - le ombre sono un poco alzate e non c'è grana.
- La foto "Oggi" è ritagliata 2:1 sulla sola fila delle cabine: niente carrello elevatore a sinistra, niente metà bassa di asfalto.

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

- "Allora / Oggi" sono due bottoni veri con aria-pressed. Clic, tocco, Tab e Invio, e le frecce sinistra e destra cambiano la foto e la didascalia di netto, senza dissolvenza (verificato con `finale_tasti.mjs`). L'unica transizione è il colore del bottone toccato (0,12 s), tolta con prefers-reduced-motion.
- Non ci sono animazioni allo scorrere né effetti sul cursore.
- A 390 il menu è un bottone con aria-expanded.
- Il piede si apre a fisarmonica: quattro bottoni da 52 px con aria-expanded e aria-controls. Senza JavaScript le colonne restano aperte.

## Sezioni

1. **Apertura**: la stampa d'archivio con l'interruttore.
2. **Servizi**: "Cinque servizi, nessun subappalto". L'indice a righe con filetti dei cinque servizi, ogni riga è un link a `servizi/*.html`. Sotto ci sono le tre polizze e la riga verificata nella pagina delle assicurazioni: "Per legge la RC Vettore risarcisce al massimo 1 euro per ogni chilo di merce (art. 1696 c.c.): per una pressa non basta", con il link alle coperture.
3. **Parco mezzi**: "Tre autogru elettriche per lavorare dentro i reparti".
   - Il convoglio Volvo FH, ribassato e Ormig T40 è scontornato, con tre legende.
   - Sotto, al posto delle tre colonne di testo, un indice a righe con link a `mezzi/*.html`: Motrici con gru Cormach, da 5 a 33 t, 5 mezzi / Autogru elettriche Ormig, 25, 35 e 40 t, 3 mezzi / Trattori per trasporti eccezionali, 3,00 × 4,30 m o 25 m, 2 mezzi.
4. **L'ultimo metro**: il titolo con il paragrafo sotto, non a destra. Tre foto con lo stesso taglio 4:3 (700 x 525), la stessa luce media e la stessa saturazione, mai sopra i 700 px dell'originale. Le didascalie dicono luogo e operazione, senza tonnellate perché nessuna è confermata.
5. **Chiusura "b con foto"**:
   - la foto seppia è a filo del bordo sinistro (7/12) e la didascalia è allineata al margine della griglia;
   - a destra, la frase loro "Dopo 65 anni, la nostra storia parla per noi" e "Siamo sempre pronti a raccontartela di persona." (dalla pagina `azienda`);
   - poi i recapiti: il telefono verde a 44 px con tel:, "PEC" con mailto:, l'indirizzo con il link a Google Maps e gli orari.
6. **Piede**:
   - il logo con una riga su chi sono e "Richiedi un preventivo";
   - quattro colonne: Servizi, Parco mezzi, Azienda, Contatti. Contatti contiene anche "Seguici" con Facebook e Instagram scritti in parole;
   - la riga legale: ragione sociale, P.IVA e C.F., REA, Privacy e Cookie (iubenda). Non c'è capitale sociale, perché è una snc.
   - **Niente newsletter**: Giolo lavora per aziende che chiamano quando hanno un macchinario da spostare. Non va a fiere, non ha cataloghi né clienti privati, e le quattro notizie del sito sono guide scritte per Google, non novità da mandare per email.

## Foto

Sono tutte dell'azienda, da `assets/originali/`, scaricate da giolo.it. Non ci sono foto di repertorio né immagini generate. I diritti vanno confermati con l'azienda (vedi LEGGIMI). Il trattamento è uno solo, in `finale_img.py`: bianco verso la carta, ombre un poco alzate, saturazione appena ridotta tenendo il verde, nessuna grana.

| In pagina | Originale | Misure pubblicate |
|---|---|---|
| Allora (`allora-*`, `allora-q-*`) | `300---Foto-giolo-aut.jpg`, scansione 1920x1340 | 2:1 a 760/1100/1780; quadrato a 600/780/1100 |
| Oggi (`oggi-*`, `oggi-q-*`) | `IMG_1226-3.jpeg`, 1920x900, dall'alto | 2:1 a 760/1100/1420; quadrato a 600/720 |
| Convoglio (`convoglio-*.webp`) | `IMG_4057.jpeg`, 1920x1440 | scontornato (maschera di `proto_b_mask.py`), 1000/1400/1870; taglio Ormig 600/842 |
| Lavori (`lavoro-*`) | `4196854194---…` (Padova), `196---…` (bobina), `319---…` (reparto), tutte 700x600 | 4:3 a 480/700 |
| Chiusura (`origine-*`) | `7361166001---…`, 1000x600, seppia | 520/760/1000 |

La foto della chiusura non compare altrove nella pagina. È dell'azienda, quindi non è usata in nessun'altra home della campagna.

## Controlli

- **Scorrimento orizzontale e sovrapposizioni**: nessuno scorrimento a 320, 390, 768, 1024, 1440 e 1920 (`finale_shoot.mjs` misura scrollWidth ed elementi fuori finestra). Ho guardato a pezzi 1440, 390, 768, 1024 e 1920, gli stati "Oggi" a 1440 e 390, il menu e il piede aperti a 390: nessuna sovrapposizione.
- **Lineetta lunga U+2014**: assente in pagina, negli script, in questa nota e nel LEGGIMI. `build_finale.sh` si ferma se la trova.
- **`segnali.sh`** (kit, a 1440): 17 soglie su 18 sono a posto.
  - L'area foto è al 25,3 % contro una soglia del 35 %. È voluto: le foto vere esistono quasi tutte a 700 px, e la scansione d'archivio regge solo fino a circa 1100 px. Allargarle vorrebbe dire ingrandirle oltre l'originale, cioè l'errore che il giudice ha segnalato nel prototipo. Quando arriveranno le foto rifatte dal vero (LEGGIMI), i lavori potranno salire a due colonne grandi.
  - Il resto: tre misure di H2, nessun titolo a sinistra con il paragrafo a destra, 11 filetti, 0 frecce, 0 numeri giganti, 0 numerazioni, due fasce di fondo, superfamiglia unica (Mona 84 %, Hubot 16 %).
- **Divieti del committente**: nessun gradiente, nessuna emoji, niente Inter, nessuna card con bordo colorato, niente vetro, nessun badge sopra il titolo, nessuna icona Lucide, niente dissolvenze allo scorrere o effetti sul cursore, nessun corsivo serif.
- **Contrasto AA** verificato su tutte le coppie (sopra, in Colori).
- **Dati**: tutti da `01-analisi.md` e dal crawl. "Zona industriale sud di Padova" è stata sostituita con la frase loro "a Saonara, in provincia di Padova". "Cinque Iveco" è diventato "cinque autocarri con gru", perché i primi due da sinistra hanno una calandra diversa. Le cose da confermare sono nel LEGGIMI.
