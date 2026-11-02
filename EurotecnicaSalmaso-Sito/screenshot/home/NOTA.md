# Home finale Eurotecnica Salmaso, "Il giorno dell'evento"

Pagina: `sito/index.html` (statica, si apre anche da file), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini, pagina, screenshot). Base: prototipo B scelto dal giudice, con la prima schermata ripensata (K0 era 6) e gli innesti del prototipo A.

Altezza: 5878 px a 1440 con il piede, 7830 px a 390.

## L'idea

Il radiomicrofono appeso al muro azzurro, e il suo cavo che scende, piega e diventa la linea dei tre giorni del noleggio: ritiro, evento, reso. Il cavo nero con gli anelli (grigi per ritiro e reso, petrolio per il giorno dell'evento, come l'anello sulla griglia del microfono) porta in apertura la loro regola vera, "Quotiamo solo il/i giorno/i di effettivo utilizzo e non quello di consegna e di reso". Lo stesso cavo torna, a tutta larghezza, nel calcolo del noleggio: è l'unico segno grafico della pagina, nato dall'oggetto e non disegnato accanto.

Con il nome di un concorrente la pagina non regge: la linea è la loro regola del noleggio, i testi sono i loro (sale storiche, sistemi per conferenze fatti a Padova, MePA OS 30, Via Lussemburgo).

## Le prime due schermate

1. **Apertura** (1440x900). Fondo #E5ECF0 che è il muro stesso della foto: nessun riquadro, il microfono sta sulla pagina. A sinistra il titolo "Il giorno dell'evento" in General Sans 500 a 128 px, poi le tre righe che dicono tutto il mestiere: "Impianti audio e video per teatri, sale congressi, aule e chiese: li progettiamo e li installiamo. Per convegni ed eventi li portiamo in sala o li noleggiamo. Da Padova, dal 1967." Un solo bottone (Chiama 049 760348) e un link (Impianti per le sale). In basso il cavo del microfono piega a sinistra e corre fino al bordo: sopra, le tre tappe di un noleggio tipo calcolate sul prossimo sabato (ritiro ven, evento sab, reso entro dom) e "Si quota solo il giorno dell'evento"; tutta la linea porta al calcolo. Didascalia piccola a destra.
   A 390 (390x844): titolo su due righe, le tre righe di testo, il microfono intero a destra subito sotto il testo, bottone e link a sinistra del microfono, il cavo che piega in basso con le tre tappe. Tutto nei primi 844 px.
2. **Cosa portiamo in sala**: titolo, una riga di presentazione, le due foto vere del 2024 affiancate a mezza larghezza (regia del convegno in sala storica, palco sull'acqua) con didascalia, poi le sei voci del service in righe singole con filetto (64 px a riga).

Poi: il noleggio (il gesto), gli impianti con una sola sala grande a tutta larghezza (palchi di teatro) e le quattro sale in due colonne, il 1967 con MePA e sede, la chiusura con foto, il piede.

## Caratteri

- **General Sans 400 e 500** (Indian Type Foundry, Fontshare, licenza ITF Free Font License: uso commerciale e web gratuito) per titoli, date e numeri grandi. Riferimenti: d&b audiotechnik (grotesk geometrica pulita, Mark Pro, frase breve su bianco) e Genelec (titolo grande sopra un solo prodotto vero).
- **Host Grotesk** variabile (Element Type, Google Fonts, SIL Open Font License 1.1) per testo, telefono, P.IVA e date dei comandi: cifre tabellari di serie (tutte a 650 unità), quindi numeri allineati senza `tnum`. Ha preso il posto di Switzer, che si vedeva rotta.
- I file sono serviti dalla pagina (`sito/fonts/`, licenze in `sito/fonts/LICENZE.md` e `OFL-host-grotesk.txt`). Nessun carattere delle liste b della guida, nessun monospazio, niente corsivi.
- Difetto trovato e corretto: in Chromium su Linux, con la spaziatura negativa, General Sans apriva un vuoto dopo la f ("Amplif icazione", "eff ettivo"), lo stesso tipo di errore che rompeva Switzer nel prototipo. Si toglie con `text-rendering: geometricPrecision` sul corpo della pagina; controllato a 1440, 390 e 320.
- Apostrofo tipografico ’ in tutta la pagina, titolo compreso; la build si ferma se trova un apostrofo dritto nel testo.

## Colori

Un solo fondo per tutte le sezioni, #E5ECF0 (il muro della foto, luce fredda come Genelec); piede #D6E0E5. Inchiostro #141A1C, testo secondario #475256, petrolio del logo scurito #1F6A70 per link e accenti, #257B82 solo in grande (1967). Il rosso del velluto e l'oro stanno solo dentro le foto. Contrasti misurati nella chiusura e nel piede: minimo 5,24:1 (link "Apri la mappa"), titoletti grigi del piede su #D6E0E5 6,0:1.

## L'interazione (una sola)

"Quotiamo solo i giorni di effettivo utilizzo": comandi su una riga (giorno dell'evento con frecce e calendario nativo, durata 1, 2 o 3 giorni, ritiro in sede o consegna e montaggio). La linea dei tre giorni sotto, sul cavo, mostra ritiro o consegna il giorno prima, i giorni quotati, il reso o il ritiro a fine evento o il giorno dopo, con le frasi del loro sito; lo stesso stato si aggiorna nella linea dell'apertura. Nessun prezzo. Bottoni veri (`aria-pressed`, `aria-live` sui risultati), provati con tastiera e con tocco (`_prova/script/prova_interazione.mjs`). Transizioni di 150 ms solo sui colori di bottoni e link; sui telefoni niente stato di passaggio appiccicato. Nessuna animazione allo scorrere, nessun effetto che segue il cursore. Il cavo è disegnato in SVG da poche righe di script sulle coordinate dell'attacco nella foto (scritte dalla build), e si ridisegna al cambio di misura.

## Foto, origine e licenza

- **Apertura**: DESIGNECOLOGIST, Unsplash hvgd0ygXuQQ, Unsplash License (`assets/CREDITI.md`). Lavorata con PIL in `_prova/script/finale_img.py`: tolta la scritta "SPEAK UP" dal corpo, sfumate le scritte piccole sul connettore, muro reso uniforme del colore della pagina, cavo vero tolto sotto il pressacavo (lo ridisegna la pagina). Segnaposto, da rifare dal vero.
- **Service**: due foto dell'azienda dallo slider del 2024 (`2024-05-1.jpg`, `2024-05-3.jpg`), scatti da telefono 1600x616: tagli 2:1 a mezza larghezza (densità circa 1,9x), nitidezza smorzata, mai a tutta larghezza. Diritti da chiarire (vedi LEGGIMI).
- **Impianti**: Valentin Karisch, Unsplash igNLOmbJBhg (palchi della Staatsoper di Vienna), Unsplash License, taglio 5:2 a tutta larghezza.
- **Chiusura**: Nguyen Dang, Unsplash ft2Gpg_fNVY (sala consiliare ovale con microfoni a collo di cigno, eco dell'apertura e dei loro sistemi per conferenze), Unsplash License, a destra fino al bordo, alta quanto il testo. Non compare altrove nella pagina.
- Nessuna di queste foto è usata in un'altra home della campagna (controllati gli ID in tutti i `CREDITI.md`). Nessuna immagine generata dall'IA.
- Trattamento unico: neri sollevati verso il blu del muro, saturazione all'86 %, JPEG progressivi in 2 o 4 larghezze con `srcset`.

## Chiusura e piede

Chiusura "b con foto": la loro frase "Avete bisogno di un consiglio o di una consulenza tecnica?" come titolo, "Il nostro team di esperti è a vostra disposizione." (refuso "e" corretto), telefono a 56 px sottolineato con `tel:`, info@ e service@ con `mailto:`, indirizzo con "Apri la mappa"; foto a destra fino al bordo.
Piede: logo (bozza SVG fedele), una riga su chi sono, colonne Azienda, Impianti, Service e noleggi, Contatti (indirizzo con link alla mappa); riga legale con Eurotecnica Salmaso S.R.L., P.IVA 01353510280, indirizzo, Privacy, Cookie. A 390 le colonne si impilano in ordine (due per riga, Contatti a tutta larghezza).
Niente newsletter: il sito non pubblica notizie, fiere o cataloghi, il lavoro è a progetto per enti, scuole e parrocchie e una squadra di quattro persone non la alimenterebbe; per i privati del noleggio basta il telefono. Niente "Seguici": nessun profilo social trovato.

## Controlli

- Larghezze 320, 390, 768, 1024, 1440, 1920: nessuno scorrimento orizzontale (scrollWidth uguale alla finestra), nessuna sovrapposizione dopo le correzioni (a 1920 la foto d'apertura si adatta all'altezza e il muro continua nel fondo; sotto 1180 la nota della linea si nasconde perché toccava il cavo; sotto 380 l'apertura si allunga a 800 px perché il microfono non tocchi il testo).
- `segnali.sh` (kit): 0 soglie bloccanti, 0 da guardare. Foto al 35,4 % della pagina a 1440; 18 filetti; 3 misure di H2; 2 famiglie (Host Grotesk 88 %, General Sans 12 %); un solo numero grande (1967); nessuna etichetta maiuscola sopra i titoli; nessuna freccia. Uscite in `_prova/segnali-finale/`.
- Nessun carattere U+2014 nella pagina, negli script e nei .md di questo compito.
- Dati in pagina tutti da `01-analisi.md`; tolti "cerimonie" e "aule magne" del prototipo, e due dettagli del noleggio che non stanno nelle fonti (consegna "la mattina dell'evento", ritiro di domenica da concordare).
