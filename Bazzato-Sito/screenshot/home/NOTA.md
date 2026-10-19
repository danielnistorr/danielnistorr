# Bazzato, home finale: "Il ponte"

Costruita sulla bozza B, quella scelta dal committente. Restano l'idea, la prima schermata, il trattamento delle foto, il carattere e i colori della bozza; sono cambiati l'esecuzione, i dati, il telefono, i dettagli. Pagina: `sito/index.html`. Si rifà tutto con `bash _prova/script/build_finale.sh`.

Screenshot: `home-1440.jpg` (5917 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (5699 px), `home-390-prima-schermata.jpg`. Sono fatti con l'ora fissata a martedì 20/10/2026 alle 10.30 (`?ora=2026-10-20T10:30`). Senza il parametro la pagina usa l'ora vera di Vigonovo.

## Idea

L'officina com'è, chiara e dritta: un'auto alzata sul ponte, il pavimento a piastrelle, la luce dei neon. Il resto della pagina mantiene quello che Bazzato già promette sul suo sito, "Prezzi chiari, sconti chiari": che lavori fanno, quanto costano, quanto ci vuole e dove sono. In testata c'è l'unica cosa da sapere prima di chiamare, cioè se l'officina è aperta adesso.

## Le prime due schermate

- **1440, prima schermata.**
  - In testata, su cemento chiaro: "Bazzato Autofficina", tre voci di menu, lo stato "Aperto, chiude alle 12.00" con il punto azzurro e il telefono.
  - Sotto, la foto dell'officina a tutta larghezza fino al fondo dello schermo.
  - Sul pavimento chiaro, in basso a sinistra, il titolo "Officina multimarca a Tombelle" (General Sans 500, 117 px, spaziatura -0,04em, interlinea 0,93). Sotto, due righe sui servizi e l'indirizzo, il bottone nero "Chiama 049 9830115", "Scrivi su WhatsApp" e "Foto indicativa" nell'angolo.
  - Il parafango bianco sfocato in basso a sinistra non c'è più: al suo posto è stato ricostruito il pavimento.
- **1440, seconda schermata.**
  - Una frase su chi sono: "L'officina di Andrea e Paolo Bazzato a Tombelle, tra Padova e Venezia, per auto di ogni marca. Prima il preventivo, alla fine il resoconto di ogni operazione fatta."
  - Quattro fatti in due colonne larghe, con il filetto nero sopra e senza icone: Eurorepar Car Service, GPL Landi, Revisione in sede, Auto sostitutiva. Nella bozza erano quattro colonne strette.
- **390.** Taglio verticale della stessa foto, con l'auto in alto e il titolo su tre righe sul pavimento. Sotto, il bottone nero e WhatsApp. Nella testata lo stato è in forma corta, "Aperto fino alle 12.00", e si tocca per vedere gli orari. A 320 la foto sale di 64 px e il testo si stringe, così il titolo non copre il ponte.
- **Poi:**
  - la foto delle mani sulla ruota (2:1), che apre il foglio bianco;
  - il listino "Prezzi chiari, sconti chiari", sette righe con il prezzo, o "a preventivo" dove manca;
  - la revisione in sede, con la scheda Prezzo / Pre-revisione / Appuntamenti / Prima revisione / Poi;
  - la foto dell'auto intera sul ponte (2:1, la stessa altezza delle mani);
  - dove siamo, con gli orari e i contatti;
  - il piede con ragione sociale, P.IVA e REA.

## Caratteri e colori

- **General Sans** di Indian Type Foundry (Fontshare), nei pesi 400, 500 e 600: una sola famiglia.
  - I file woff2 vengono dal pacchetto ufficiale (`_prova/crawl/fontshare/zip/GeneralSans_Complete/`), non sono modificati e la pagina li serve da `sito/fonts/`.
  - Licenza: ITF Free Font License 2.0 (`sito/fonts/FFL.txt`). L'uso commerciale è gratuito, anche con i file ospitati sul proprio server (sezione 01). I file però non si modificano e non si cedono a terzi (sezione 02): chi pubblica il sito per Bazzato scarica la sua copia da fontshare.com.
- **Perché General Sans**: è un grottesco sobrio, né tecnico né di moda. Il titolo corto, grande e chiaro, in basso sulla foto luminosa, viene da Lunaz (un oggetto vero in luce morbida, un titolo corto in basso a sinistra) e da Polestar (testo diretto in italiano, carattere sobrio).
- **Scala**: titolo 117 px; titoli di sezione 80 e 56 px; frase d'apertura 41 px; testo 18-19 px; didascalie 13-14 px. Spaziatura negativa sui titoli.
- **Cifre**: General Sans non ha le cifre tabellari, quindi nella colonna dei prezzi le cifre sono messe a larghezza uguale da poche righe di script, senza toccare il file del carattere.
- **Colori**:
  - cemento #E9E8E4 per la pagina, un solo foglio bianco #FFFFFF che va dalla foto delle mani alla fine del listino (l'unica variazione di fondo);
  - nero #111111 per il testo, grigio #56554F per il testo secondario (contrasto 6,1 sul cemento e 7,5 sul bianco), filetti #C9C7C1;
  - l'azzurro del loro logo, #00C3EF, solo nel punto dello stato "aperto";
  - il bottone è nero e al passaggio diventa petrolio pieno #00667E (6,6 con il bianco), subito, senza dissolvenza.

## Interazione

Il gesto è uno solo: lo stato dell'officina in testata, calcolato con l'ora di Roma.
- **Cosa dice**: "Aperto, chiude alle 12.00", "Pausa, riapre alle 14.00", "Chiuso, riapre lunedì alle 08.00", "Chiuso per ferie, riapre il 24 agosto".
- **Chiusure**: legge un elenco modificabile in cima allo script, con le ferie (oggi c'è quella del 6-21 agosto 2026 presa dal sito), i festivi nazionali e Pasquetta, che si calcola da sola. Così ad agosto non dice "Aperto". Se una chiusura inizia entro 45 giorni, il pannello degli orari la annuncia.
- **Il pannello**: lo stato è un bottone che apre il pannello degli orari di officina e uffici, con il numero. Si apre con clic, dito, Invio o Spazio; si chiude con Esc (il fuoco torna al bottone) o toccando fuori.
- **Niente movimento**: nessuna transizione, nessuna animazione allo scorrimento, nessun effetto che segue il cursore.
- **Prove** (`_prova/script/prova_stato.mjs`): 13 orari e giorni diversi (prima delle 8, pausa, venerdì sera, sabato, Ognissanti di domenica, vigilia di Natale, Pasquetta 2027, ferie), più tastiera e dito a 390. Tutte giuste.

## Foto: origine e licenza

Nessuna foto dell'azienda regge (voti da 1 a 5 su 10 in `_prova/inventario-immagini.json`). Le tre foto sono segnaposto con licenza libera, verificata sulla pagina di ogni foto, e nessuna è usata in un'altra home della campagna. In pagina portano l'etichetta "Foto indicativa".

| In pagina | Origine | Licenza | Lavoro fatto |
|---|---|---|---|
| Apertura, officina con l'auto sul ponte | Renee Razumov, Pexels 33814736 | Pexels License | tolti SKODA, SUPERB, WURTH e MIRKA; tolto il parafango in primo piano ricostruendo il pavimento in prospettiva; gialli smorzati; velatura chiara sul pavimento; taglio largo e verticale |
| Mani sulla ruota | Jimmy Nilsson Masth, Unsplash 9uHal2Dd9aE | Unsplash License | tolto il marchio sul guanto; ombre aperte; 2:1 e quadrato |
| Auto bianca sul ponte | Artem Podrez, Pexels 8986138 | Pexels License | tolti SUBARU, FORESTER e BRIDGESTONE; saturazione ridotta; 2:1 e quadrato |

Trattamento comune: luce neutra appena fredda, saturazione ridotta, neri non chiusi. JPEG progressivi in più larghezze con `srcset` (`_prova/script/finale_img.py`). Dettagli in `assets/CREDITI.md`.

## Le ispirazioni del committente

- **Pelletteria Graziella: non usata.** Nero pieno, serif enorme con il corsivo d'accento: è il registro di una pelletteria che lavora per le maison, ed è sbagliato per un'officina di paese.
- **Studio N19: un solo tratto.** Il titolo grande e sicuro in grottesco su un fondo chiaro, con tanta aria. Niente sfocature né parole in movimento.
- **Perché così poco**: Bazzato non è moda né lusso, è un servizio di fiducia. Qui l'alta gamma è la luce, l'ordine e i prezzi detti chiari.

## Cosa è cambiato rispetto alla bozza B

- **Foto**:
  - tolto il parafango bianco sfocato dall'apertura;
  - tolta la banda delle bussole;
  - le mani sono più chiare e meno alte (2:1 invece di 1,76:1);
  - aggiunta l'auto intera sul ponte, della stessa altezza delle mani: due bande uguali, non tre di altezze diverse;
  - la larghezza più grande dell'apertura ora esiste davvero (2280 px; la bozza chiamava un file a 2400 px che mancava).
- **Dati**:
  - tolto "Dal 2005 Andrea e Paolo Bazzato riparano auto", perché l'anno della snc non è verificato e non dice nulla sulle persone;
  - "Dal 2017 tutte le auto nuove usano questo gas" ora è la frase della fonte;
  - "prezzo anche al telefono" invece di "si confronta al telefono";
  - "servono" invece di "bastano" per il preventivo del tagliando;
  - orari col trattino corto (08.00-12.00), appuntamenti scritti per esteso.
- **Stato in testata**: gestisce ferie e festivi da un elenco modificabile.
- **Esecuzione**:
  - nessuna transizione (la bozza ne aveva sul bottone e sulla freccina);
  - quattro fatti in due colonne invece di quattro;
  - menu visibile fino a 960 px;
  - "Scrivi su WhatsApp" anche in fondo;
  - filetti a tutta larghezza anche a 1920;
  - grigio del testo un poco più scuro;
  - il titolo a 320 non copre più il ponte.
- **Dalla bozza A**: nessuna immagine. Solo la frase della fonte sul gas R1234yf e la cura per i dati incerti.

## Controlli

- **Larghezze**: 1440, 390, 320, 768, 1024 e 1920, guardate a pezzi. Nessuno scorrimento orizzontale, nessun testo fuori dalla finestra, nessuna sovrapposizione fra testata, titolo, testo e bottoni (`finale_scatti.mjs`).
- **Altezza a 1440**: 5917 px.
- **Segnali da IA** (`kit/segnali.sh`, 1440): 0 soglie bloccanti su 10. Foto sul 39,2 % della pagina, General Sans al 100 %, nessun monospazio, nessuna etichetta maiuscola, nessun titolo col punto, 4 fasce di fondo, 20 filetti. Resta da guardare solo "misure degli H2: 2 (80 e 56 px)": è voluto, perché l'indirizzo è più piccolo dei titoli di sezione.
- **Divieti del committente**: nessun gradiente, nessuna emoji, niente Inter, nessuna card col bordo colorato, nessun vetro sfocato, nessuna icona, nessun badge, nessuna animazione allo scorrimento, nessun effetto sul cursore, nessun bottone che sbiadisce, nessun corsivo d'accento.
- **Caratteri vietati**: nessuna lineetta lunga U+2014 né media U+2013 nella pagina, negli script, in questa nota e nel LEGGIMI.
- **Note di lavorazione**: nessuna in pagina; la build controlla le parole "provvisori", "da rifare", "proposta", "segnaposto".
