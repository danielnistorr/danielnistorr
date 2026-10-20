# Ferridea, nuova home: versione finale "Ferro sul muro"

Pagina: `sito/index.html` (statica, si apre con file:///). Immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini, controlli, screenshot, segnali).

Misure: 5928 px a 1440 compreso il piede, 6818 px a 390. Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1440 e 1920.

## L'idea

La pagina è il muro di calce, e sul muro c'è un lavoro loro: la scala a sbalzo di Ferridea (foto `P1020524` del loro sito).
- Ho scontornato i gradini a mano, con poligoni ricavati dagli spigoli veri, e ho tolto cucina, finestra, soffitto in legno e una piastra.
- Il muro intorno ora è esattamente il fondo della pagina, #F2F0EB. Sul muro restano solo le ombre vere sotto le testate dei gradini.
- La foto è raddrizzata di 2,6 gradi (le verticali della finestra pendevano). Le alte luci dei piani lucidi sono recuperate e la dominante blu è tolta.
- Cinque blocchi scuri escono dal muro uno sopra l'altro: si legge come una scala a sbalzo e come un oggetto di ferro.

Il colore d'accento è il minio dell'antiruggine. In tutta la pagina non c'è nessuna foto di repertorio: sono tutte foto di lavori Ferridea.

## Le prime due schermate

- **1440, prima schermata.** In alto a destra la scala a sbalzo, larga il 60 % della pagina e a filo del bordo destro, senza riquadro. Accanto, la didascalia "Scala a sbalzo, lavoro Ferridea". In basso c'è una fascia sola di parole:
  - a sinistra il titolo "Ferro su misura, dal 1959" (Archivo semi-esteso 500, 110 px), con la data dentro il titolo come Capoferri;
  - a destra, colonne 9-12, sulla stessa linea di base, la riga su cosa fanno, il bottone "Chiama 049 879 2451" e l'email.
- **Seconda schermata.** "I lavori": quattro foto loro su due righe di altezza uguale (5+7 e 7+5 colonne), ognuna con nome, una riga e il link alla pagina. Le foto sono Cancelli (portone ad arco), Parapetti e ringhiere, Capottine e Scale. Sotto c'è una riga per serramenti, serrature, saldature e riparazioni.
- **390.** La scala a tutta larghezza, la didascalia, il titolo su tre righe, la riga e il bottone del telefono a tutta larghezza. Sta tutto in 844 px.
- **Resto della pagina:**
  1. il selettore Ferro battuto / Lamiera / Inox;
  2. "Nel settore dal 1959" con i tre passi in elenco verticale;
  3. la chiusura;
  4. il piede.

## Caratteri e colori

- **Archivo** di Omnibus-Type (Google Fonts, licenza SIL Open Font License 1.1, uso commerciale libero). È variabile in larghezza (62-125) e peso. I file woff2 latin e latin-ext stanno in `sito/fonts/` e li serve la pagina.
  - Titoli: larghezza 112, peso 500, spaziatura da -0,03 a -0,04 em.
  - Testo: 400 a 19 px, interlinea 1,6.
  - Marchio: larghezza 125, peso 600, maiuscolo spaziato.
  - Telefoni: cifre tabellari.
- **Perché Archivo.** Il grottesco largo è quello delle targhe e delle insegne d'officina. È asciutto come il carattere di Secco Sistemi e come le didascalie di Bisca. Una famiglia sola, niente monospazio, niente etichette.
- **Colori**, con il contrasto misurato:

| Ruolo | Colore | Contrasto |
|---|---|---|
| Fondo | calce #F2F0EB | |
| Testo | ferro #222426 | 13,7:1 |
| Testo secondario | mica #5E6266 | 5,4:1 sulla calce, 4,9:1 sul piede |
| Accento: bottone, link, scheda scelta, numeri dei passi | minio #AD3C19 | 5,4:1 sulla calce, 4,9:1 sul piede |
| Bianco sul bottone minio | | 6,1:1 |
| Piede | #E8E5DE | |

- Il piede è l'unico cambio di fondo della pagina.
- **Riferimenti.** Per la prima schermata, Hambro e Mario Agnoletto in chiaro: un oggetto vero grande, sul fondo dello stesso colore, titolo grande, tanta aria. La data nel titolo viene da Capoferri ("since 1894"). Lo scontorno del metallo sul bianco con l'ombra viene da De Castelli. Nome e riga sotto le realizzazioni vengono da Secco Sistemi.

## Interazione

Il selettore "Ferro battuto, Lamiera, Inox" usa tre parole del loro testo ("cancelli in ferro battuto e lamiera", "acciaio inox"). Sono tre parole grandi che fanno da schede.
- Al clic o al tocco la foto a 2,2:1 e la riga sotto cambiano di netto, senza dissolvenza:
  - Ferro battuto: la fascia a volute del cancello della loro home;
  - Lamiera: il pannello traforato a raggiera;
  - Inox: la scala con la ringhiera a bacchette.
- Sotto c'è la riga "E serramenti in alluminio".
- Su telefono le foto sono tagli quadrati sul dettaglio, serviti con `<picture>`.
- È un tablist ARIA: si scorre con frecce, Home e Fine, il fuoco è visibile, e senza JavaScript resta la prima scheda.
- Le transizioni durano 0,12 s, solo su colore e sottolineatura. Nessuna animazione allo scorrere, nessun effetto sul cursore, nessun cambio di opacità.

## Foto: origine e licenza

Tutte le foto vengono dal sito attuale ferridea.com (`assets/originali/`) e sono lavori dell'azienda. L'uso va confermato con loro (vedi LEGGIMI).

| In pagina | File in `sito/img/` | Originale | Lavorazione |
|---|---|---|---|
| Apertura | `scala-sbalzo-*` | `scale--P1020524.jpg` | scontorno a poligoni, muro portato a #F2F0EB, ombre di contatto vere, raddrizzata, alte luci recuperate |
| Cancelli | `cancelli-*` | `cancelli--DSCN0383_.jpg` | ritaglio sotto il mascherone, rumore ridotto |
| Parapetti | `parapetti-*` | `parapetti--Parapetti-San-Giacomo-014.jpg` | bianco del muro neutralizzato a metà (il muro è color crema) |
| Capottine | `capottine-*` | `capottine--P1030303.jpg` | ritaglio sulla struttura bianca: fuori la casa arancione e i bidoni |
| Scale | `scale-*` | `scale--Scala-Treviso-011.jpg` | raddrizzata di 0,4 gradi |
| Ferro battuto | `ferro-battuto-*` | `home--P1030186.jpg` | fascia bassa a volute |
| Lamiera | `lamiera-*` | `parapetti--P1030315.jpg` | pannello a raggiera |
| Inox | `inox-*` | `scale--Scala-Treviso-016.jpg` | raddrizzata di 0,5 gradi |
| Chiusura | `chiusura-*` | `parapetti--Sand-20-07-2008-007.jpg` | ritaglio sulla scala, fuori i quadri e il lume |

- **Trattamento comune** (`_prova/script/build_img.py`), a colori e senza seppia:
  - il muro di riferimento diventa neutro e tende alla calce della pagina;
  - riduzione del rumore delle compatte;
  - curva a S leggera e alte luci compresse invece che bruciate;
  - saturazione all'80 % e contrasto 1,04 su tutte;
  - nitidezza leggera alla misura finale.
- Ogni foto è in JPEG in tre o quattro larghezze, con `srcset`.
- **Niente repertorio.** Le foto Unsplash di `assets/esterne/` (Wegelius, Gomez Angel, Prouzet, Henman e le altre) non sono usate nella versione finale. Niente immagini generate dall'IA, niente marchi.
- **Chiusura.** Ho scelto la scala con il parapetto a cavi, una foto loro, luminosa e diversa da tutte quelle sopra. Così la pagina non ha nessuna foto indicativa. Non è la foto dell'officina: quella va scattata (LEGGIMI).

## Chiusura e piede

- **Chiusura** ("b con foto"):
  - a sinistra la frase loro "Dallo studio alla realizzazione, e anche dopo", da "a partire dallo studio e sviluppo di soluzioni personalizzate fino alla realizzazione delle stesse, e anche successivamente";
  - sotto, i recapiti: 049 879 2451 grande con `tel:` (telefono e fax), il cellulare con `tel:`, l'email con `mailto:`, l'indirizzo con "Apri la mappa";
  - a destra la foto fino al bordo;
  - niente orari, perché non sono pubblicati.
- **Piede:**
  - la scritta FERRIDEA, che è una proposta e non un logo, con la riga "Carpenterie metalliche e infissi a Saonara, nel settore dal 1959";
  - tre colonne con i titoletti a 15 px in grigio mica: Lavori, Ferridea (con "Dal 1959" che punta a `/azienda/`) e Contatti (con `tel:`, `mailto:` e la mappa);
  - la riga legale con ragione sociale, ditta individuale, indirizzo, P.IVA, Privacy e Cookie;
  - a 390 le colonne si impilano nell'ordine Lavori, Ferridea, Contatti.
- **Newsletter: no.** Ferridea non comunica novità, fiere, cataloghi né collezioni, e il sito è fermo al 2016. Chi compra un cancello o una scala lo fa una volta in vent'anni, quindi una newsletter resterebbe vuota. Niente Seguici, perché i social non esistono.

## Controlli fatti

- **Screenshot** guardati a pezzi a 1440 (intera e prima schermata), 390 (intera e prima schermata), 320, 768, 1024 e 1920. Ho controllato anche le schede Lamiera e Inox a 1440 e a 390.
- **Correzioni fatte durante i controlli:**
  - a 1024 la foto d'apertura entra nel flusso, così non si sovrappone al titolo;
  - a 1920 e con finestre basse la larghezza della foto è legata all'altezza della finestra;
  - a 390 le schede vanno a capo se serve.
- **Segnali da IA** (`kit/segnali.sh`, uscita in `_prova/segnali-finale/`): 0 soglie da correggere e 0 da guardare.
  - Foto al 41,5 % della pagina, una sola famiglia di caratteri, nessuna etichetta maiuscola, nessuna numerazione 01/02.
  - Una sola sezione con titolo a sinistra e paragrafo a destra ("I lavori").
- **Divieti del committente:** niente gradienti, niente card con bordo colorato, niente icone, niente badge, niente tre box in fila, niente dissolvenze, niente corsivo.
- **Testo:** nessun carattere U+2014 in pagina, negli script e nei .md della cartella.
- **Immagini:** quelle usate in pagina e quelle presenti in `sito/img/` coincidono (controllo in `build_finale.sh`).
- **Dati in pagina:** telefono, fax, cellulare, email, indirizzo, ragione sociale, ditta individuale, 1959 e "padovana" vengono tutti da `01-analisi.md`. La P.IVA viene da un elenco pubblico ed è nella lista da confermare. "Con il vetro" e "in officina dal 1959" sono stati tolti.
