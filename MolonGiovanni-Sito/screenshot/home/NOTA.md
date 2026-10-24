# Home finale, "Il pettine" (Molon Giovanni)

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, logo con `finale_logo.py`, pagina da `pagina.html`, screenshot con `finale_shot.mjs`). Prove della prima schermata con `prove_apertura.mjs`, controlli finali con `controlli_finali.mjs`. Altezza a 1440: 5517 px, piede compreso; a 390: 6690 px.

## L'idea
Il ranghinatore frontale a cinghie, scontornato e nitido sulla carta color fieno, è l'unico protagonista, e si misura: scegliendo il modello la macchina cambia larghezza in scala sopra una sola linea di terra quotata da 0 a 320 cm, con la barra rossa del lavoro e quella grigia della larghezza massima. È la loro tabella dei frontali (190, 210, 230, 250, 260, 300 PRO) resa visibile sul loro oggetto: con il nome di un altro costruttore la scala e i numeri non tornano più.

## Le prime due schermate
1. A 1440: testata con il logo MOLON in SVG, cinque voci, telefono e lingue. Titolo "Ranghinatori a cinghie" a 112 px su una riga. Sotto, a sinistra, la frase sulle tre operazioni e il bottone rosso "Chiama 049 900 0103"; in basso a sinistra la scelta del modello (sei numeri in cifre tabellari, Versione PRO, gEnio) con la riga "280 cm di lavoro, 320 massima, 16 pettini"; a destra la macchina sulla linea di terra. All'apertura è scelto il 300 PRO, il più largo. Nessuna legenda a filetti, nessuna riga "luogo, dal anno".
2. "Nove frontali per trattore, da 190 a 280 cm di lavoro": i sei dati del modello scelto (si aggiornano con la scelta in alto) e le quattro parti in una riga di testo con filetto sopra (denti doppi, pettini su cinghie trapezoidali, bandella fermafieno, ruote ballon), poi la nota su PRO e gEnio e su come è riportata la foto. Poi la gamma 2x2, la storia con l'archivio a filo, la riga dei rivenditori, la chiusura con la foto in campo, il piede.
A 390: testata con logo, telefono e bottone "Menu"; titolo su due righe, frase, bottone rosso, scelta del modello, la macchina sulla linea di terra: tutto dentro gli 844 px. Da 960 a 1439 la prima schermata scala anche con l'altezza della finestra (a 1366x768 e 1280x720 bottone e linea di terra restano sopra la piega); sotto i 960 si impila.

## Caratteri e colori, con i riferimenti
- Sofia Sans (Lettersoup, Google Fonts), una famiglia sola, file variabile latino servito dalla pagina (`sito/fonts/sofia-sans-latin-var.woff2`). Licenza SIL Open Font License 1.1, testo in `sito/fonts/OFL-Sofia-Sans.txt`: uso commerciale libero. Titoli 380 con spaziatura da -0,025 a -0,035em, testo 400, etichette e titoletti 500; cifre tabellari per modelli, misure e telefono. Motivo: è la scelta della guida per macchine e industria (c1, riferimenti Festool e Metzner), un impianto DIN con più calore, vicino alle scritte delle targhette delle macchine.
- Carta #F3F0E7 (lo stesso fondo su cui sono moltiplicati gli scontornati), piede #E2DDCF con un filetto in cima, inchiostro #1E1D1A, grigio #5D5950 (6,1:1 sulla carta, 5,1:1 sul piede), rosso Molon #C8231B solo per il bottone, il tratto del modello attivo e la barra del lavoro (bianco sul rosso 5,6:1). Riferimenti: Sneeboer (un solo rosso del marchio), Reform (il rosso coerente con le macchine), Pöttinger (la macchina riconoscibile prima di tutto); la pulizia chiara dalle home amate di Mario Agnoletto e Hambro.

## Interazione
Un gesto solo, "Scegli il modello": radio veri (frecce della tastiera, focus visibile, dito), più due caselle. Al cambio la macchina e le due barre cambiano larghezza in 0,18 s (niente con prefers-reduced-motion), si aggiornano la riga sotto i numeri (annunciata con aria-live) e i sei dati della sezione seguente. Versione PRO si spegne dove non esiste (190, 210), è fissa sul 300 PRO e altrove torna com'era stata scelta dal visitatore (variabile separata, provata). gEnio aggiunge 60 kg. Valori della tabella del sito (11-16 pettini, doppi denti 4, 4, 4-5, 5-6 sul PRO, pesi da 210 a 350 kg). Il menu a 390 e il piede a fisarmonica a 390 usano veri bottoni con aria-expanded; sopra i 640 i titoli del piede sono testo semplice, fuori dall'ordine di tabulazione. Nessuna comparsa allo scorrimento, nessun effetto sul cursore, hover a colore pieno.

## Foto, origine e licenza
Tutte dell'azienda, da molonmachinery.com (`assets/originali/`, vedi `assets/CREDITI.md`); nessuna foto di repertorio, nessuna immagine generata, nessuna foto già usata in un'altra home della campagna.
- `macchina-*`: `2017_10_230_5-scont.jpg` (2048x1536, fondo bianco), moltiplicato sulla carta con ombre di contatto; a 1440 è larga al massimo 880 px, quindi la variante da 1780 px basta anche a 2x. Per gli altri modelli la stessa foto è riportata in proporzione alla larghezza massima, e la pagina lo dice nella nota.
- `gamma-*`: `2017_10_RANGHINATORE-POST09noEtichette.jpg`, `2018_01_MAJOR160_sf.jpg` (fondo grigio riportato a bianco), `2017_10_380-2.jpg`, `2017_10_SCOPA-lamiera.jpg`: ritagliate sul loro ingombro (ignorando i puntini isolati), allineate a sinistra come i titoli, stessa linea di terra e stessa ombra; la scala sta a metà tra stessa area e stessa altezza, così il girello piatto e la scopatrice piena pesano uguale.
- `archivio-*`: `2017_10_foto4.jpg`, virata sul tono della carta, tagliata meno di prima.
- `chiusura-*`: `2017_10_11.08_10ritoc.jpg` (3264x2448, la foto migliore dell'inventario, voti 7/7), taglio 4:5 a sinistra: la macchina, l'andana e i due alberi sul crinale. Del portattrezzi restano lo specchio e un pezzo di cabina sul bordo destro, senza marchi leggibili.
- `logo-molon.svg`: ricostruito dal logo piatto grigio, confrontato al 400 % con l'originale.

## Piede
Logo e una riga su chi sono; colonne Prodotti (cinque famiglie e Ricambi), Azienda (Chi siamo, Storia, Rivenditori), Contatti (telefono, fax, email, indirizzo, mappa), Lingua; ultima riga con ragione sociale, indirizzo, P.IVA, Privacy, Cookie, ©. Fondo #E2DDCF con filetto, nessuna ombra, nessuna icona. Nessuna colonna Seguici finché i canali YouTube non sono confermati come ufficiali.
Newsletter: non c'è, perché vendono tramite rivenditori in Italia e all'estero, la pagina News è vuota dal 2017, le fiere non vengono comunicate e il cliente finale compra dal rivenditore; al suo posto la riga dei rivenditori con il telefono.

## Cosa è cambiato nella rifinitura finale (giudizio cieco in `_prova/cieco.json`)
- Prima schermata rifatta dentro la stessa idea: tolte le quattro legende numerate a filetti e la riga "Arlesega di Mestrino (PD), dal 1936" accanto al bottone; il selettore è salito nella prima schermata e la macchina cambia larghezza in scala sopra la linea di terra quotata. Le parti sono scese in una riga di testo sotto la piega.
- Prima schermata scalata anche sull'altezza (`--u` con `100svh`): niente sovrapposizioni tra 1100 e 1366 (provate 960, 1024, 1100, 1200, 1280, 1366, 1440, 1920), bottone sopra la piega a 1366x768 e 1280x720.
- Bug PRO corretto: dal 300 al 260 il PRO si spegne se il visitatore non l'ha scelto; la sua scelta resta passando per 190, 210 e 300.
- "Scegli il modello" al posto di "Scegli la larghezza di lavoro"; la riga sotto i numeri dice i cm veri (300 PRO = 280 cm di lavoro).
- Gamma: scontornati ritagliati e allineati a sinistra, masse pareggiate, righe più vicine; sezione di circa 1100 px a 1440.
- Storia: "2025" diventa "Oggi"; i rivenditori escono dalla colonna e diventano una riga a tutta larghezza con cinque nomi; colonna di testo allineata al fondo della foto.
- Chiusura con la foto 7/7 dell'inventario al posto di quella da telefono.
- Piede: fondo più scuro con filetto; titoli di colonna non più bottoni sul desktop.
- A 390 zone toccabili di almeno 44 px (modelli, caselle, link del piede e dei recapiti, logo), niente riquadro azzurro al tocco.
- Testi: h2 della gamma "Le altre macchine Molon" (non ripete più la frase d'apertura), sottotitolo riscritto; tolti gli indici 01-04 dalle parti.

## Controlli
- Screenshot guardati a pezzi: 1440 intera e prima schermata, 390 intera e prima schermata, chiusura e piede a 1440, più 320x640, 768x1024, 1024x768, 1920x1080 e le prove a 960, 1100, 1200, 1280, 1366 con il 190 e il 300. Larghezza del documento uguale alla finestra a 320, 360, 390, 640, 768, 900, 1024, 1099, 1100, 1280, 1366, 1440, 1920 e 2560.
- Interazione provata con Playwright: frecce e spazio sui radio, spazio sulla casella PRO, sequenze 300-260, 260 PRO-300-260, 190-230; tocco sui modelli a 390; menu con Esc; fisarmonica del piede. Nessun errore in console.
- Link: `tel:+390499000103`, `mailto:info@molonmachinery.com`, Google Maps su "Via Mestrina 10 35035 Arlesega Mestrino PD".
- `segnali.sh` a 1440: 0 soglie da correggere su 10, 0 da guardare su 8; foto al 35,1 %, una famiglia, 14 filetti larghi, 2 fasce di fondo (pagina e piede), H2 in 4 misure. L'unico gradiente sono le tacche della linea di terra.
- Nessun carattere U+2014 nella pagina, negli script, in questa nota e nel LEGGIMI.
