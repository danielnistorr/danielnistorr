# Home finale Eurotecnica Salmaso, "Il giorno dell’evento" (seconda versione, 2 novembre 2026)

Pagina: `sito/index.html` (statica, si apre anche da file), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini, pagina, screenshot e controlli). Base: prototipo B scelto dal giudice, con gli innesti di A e le indicazioni del giudizio; questa versione sostituisce quella del 24 ottobre per la nuova richiesta del committente ("più alta gamma, meno uguali tra loro").

Altezza: 6802 px a 1440 con il piede, 7880 px a 390.

## L’idea

Il radiomicrofono sta sull’asse della pagina e divide il titolo come uno spazio fra le parole: "Il | giorno / dell’ | evento". Il suo cavo scende fino alla linea dei tre giorni del noleggio, dove l’anello petrolio segna il giorno dell’evento: a sinistra il ritiro, a destra il reso. È la loro regola vera ("Quotiamo solo il/i giorno/i di effettivo utilizzo e non quello di consegna e di reso") disegnata con il loro oggetto. L’asse centrale torna in tutta la pagina: titoli di sezione centrati, le voci del service e delle sale a specchio ai due lati di un filo verticale, i tre giorni del calcolo a sinistra, al centro e a destra, la sala consiliare simmetrica della chiusura con il lampadario sull’asse. È l’asse di una sala, di un teatro, di un tavolo da consiglio: il luogo dove lavorano.

Con il nome di un concorrente la pagina non regge: la linea è la loro regola del noleggio, i testi sono i loro (sistemi per conferenze fatti a Padova, MePA OS 30, Via Lussemburgo).

### Cosa cambia rispetto alla prima versione (richiesta del 2 novembre)

1. Nessuna legenda sull’oggetto: il microfono non ha etichette, solo il cavo che porta ai giorni.
2. Il fondo non è più il grigio azzurro del muro della foto: è il petrolio del loro marchio (#257B82) schiarito, #D7E6E3. La ragione si vede: lo stesso petrolio è nel logo in testata, nell’anello della griglia del microfono (portato dall’azzurro della foto al petrolio del logo), nel 1967 e, scurito, nel piede (#123E42, come il piede petrolio del loro sito di sempre).
3. Una scelta d’impaginazione che nelle altre home della campagna non c’è (controllate le copertine di Grisignano e le prime schermate delle altre cartelle: tutte hanno titolo a sinistra e oggetto a destra o sotto): composizione simmetrica sull’asse, con il titolo spezzato dall’oggetto. Il microfono è scontornato e sta fra le parole, a una scala che lo fa leggere come una lettera del titolo.

## Le prime due schermate

1. **Apertura** (1440x900). Testata con il logo, il menu centrato sopra il microfono e il telefono. Il microfono alto 650 px sull’asse; il titolo in General Sans 500 a 178 px diviso dal microfono; sotto, a sinistra le tre righe che dicono tutto il mestiere ("Impianti audio e video per teatri, sale congressi, aule e chiese: li progettiamo e li installiamo. Per convegni ed eventi li portiamo in sala o li noleggiamo. Da Padova, dal 1967."), a destra il bottone "Chiama 049 760348" e il link "Impianti per le sale". In basso la linea dei tre giorni a tutta larghezza (ritiro ven, evento sab, reso entro dom, calcolati sul prossimo sabato), con "Si quota solo il giorno dell’evento." sotto l’anello. Tutta la linea porta al calcolo.
   A 390 (390x844): l’asse si sposta al 39 % perché le due metà del titolo stiano nella larghezza; microfono, titolo diviso, linea dei tre giorni, le tre righe, bottone e link: tutto nei primi 844 px.
2. **Cosa portiamo in sala**: titolo e riga centrati, le due foto vere del 2024 affiancate a mezza larghezza (regia del convegno in sala storica, palco sull’acqua) con didascalia, poi le sei voci del service a specchio ai due lati di un filo verticale.

Poi: il noleggio (il gesto), gli impianti con il teatro a tutta larghezza e le quattro sale a specchio, la storia con la foto a sinistra fino al bordo e il 1967 a destra, la chiusura con la sala consiliare a tutta larghezza, il piede.

## Caratteri

- **General Sans 400 e 500** (Indian Type Foundry, Fontshare, licenza ITF Free Font License: uso commerciale e web gratuito) per titoli, date e numeri grandi. Riferimenti: d&b audiotechnik (grotesk geometrica, frase breve su fondo chiaro) e Genelec (titolo grande accanto a un solo prodotto vero). Spaziatura -0,045em nel titolo, interlinea 0,92.
- **Host Grotesk** variabile (Element Type, Google Fonts, SIL Open Font License 1.1) per testo, telefono, P.IVA e date dei comandi, con cifre tabellari.
- I file sono serviti dalla pagina (`sito/fonts/`, licenze in `sito/fonts/LICENZE.md` e `OFL-host-grotesk.txt`). Nessun carattere delle liste b della guida, nessun monospazio, niente corsivi. `text-rendering: geometricPrecision` evita i vuoti dopo la f che Chromium apriva con la spaziatura negativa.
- Apostrofo tipografico ’ in tutta la pagina, titolo compreso; la build si ferma se trova un apostrofo dritto nel testo.

## Colori

Fondo unico #D7E6E3 (petrolio del logo schiarito) per tutte le sezioni; piede #123E42 (petrolio scurito). Inchiostro #141A1C (13,7:1), testo secondario #43514F (6,5:1), link e accenti #1A5E63 (5,8:1), #257B82 solo in grande (1967, 3,9:1, testo grande). Nel piede testo #E3EFED (9,9:1) e titoletti #A9C8C5 (6,6:1). Il rosso del velluto, l’oro e il giallo delle tende stanno solo dentro le foto.

## L’interazione (una sola)

"Quotiamo solo i giorni di effettivo utilizzo": comandi centrati su una riga (giorno dell’evento con frecce e calendario nativo, durata 1, 2 o 3 giorni, ritiro in sede o consegna e montaggio). La linea dei tre giorni sotto, sul cavo, mostra ritiro o consegna il giorno prima, i giorni quotati, il reso o il ritiro a fine evento o il giorno dopo, con le frasi del loro sito; lo stesso stato si aggiorna nella linea dell’apertura. Nessun prezzo. Bottoni veri (`aria-pressed`, `aria-live` sui risultati), provati con tastiera e tocco (`_prova/script/prova_interazione.mjs`). Transizioni di 150 ms solo sui colori di bottoni e link; nessuna animazione allo scorrere, nessun effetto che segue il cursore. Il cavo è un SVG di poche righe che parte dal pressacavo del microfono (posizione scritta dalla build in `cavo.json`) e si ridisegna al cambio di misura.

## Foto, origine e licenza

- **Microfono**: DESIGNECOLOGIST, Unsplash hvgd0ygXuQQ, Unsplash License. Lavorato con PIL in `_prova/script/finale_img.py`: tolta la scritta "SPEAK UP", sfumate le scritte sul connettore, scontornato come solido di rotazione (WebP con trasparenza, 150, 220 e 289 px di larghezza), anello della griglia portato al petrolio del logo, cavo vero tolto sotto il pressacavo. Segnaposto.
- **Service**: due foto dell’azienda dallo slider del 2024 (`2024-05-1.jpg`, `2024-05-3.jpg`), scatti da telefono 1600x616: tagli 2:1 a mezza larghezza, nitidezza smorzata, mai a tutta larghezza. Diritti da chiarire.
- **Impianti**: Valentin Karisch, Unsplash igNLOmbJBhg (palchi della Staatsoper di Vienna), Unsplash License, 2:1 a tutta larghezza.
- **Storia**: Daniel Emale, Unsplash zBZZfr8_0ME (unità per conferenze in un’aula consiliare, come i sistemi che progettavano a Padova), Unsplash License, a sinistra fino al bordo.
- **Chiusura**: Nguyen Dang, Unsplash ft2Gpg_fNVY (sala consiliare ovale con i microfoni a collo di cigno, simmetrica), Unsplash License, 3:2 a tutta larghezza; il taglio parte da x 96 per lasciare fuori due visitatori dietro la vetrata. Non compare altrove nella pagina; sopra di lei c’è la foto di Emale, diversa.
- Nessuna di queste foto è usata in un’altra home della campagna (ID cercati il 2/11/2026 in tutti i `*-Sito/assets/CREDITI.md`). Nessuna immagine generata dall’IA.
- Trattamento unico: neri sollevati verso il petrolio, saturazione all’82-86 %, JPEG progressivi in 2, 3 o 4 larghezze con `srcset`.

## Chiusura e piede

Chiusura "b con foto", testo sopra e foto a tutta larghezza sotto: la loro frase "Avete bisogno di un consiglio o di una consulenza tecnica?" come titolo, "Il nostro team di esperti è a vostra disposizione." (refuso "e" corretto), telefono a 64 px sottolineato con `tel:`, info@ e service@ con `mailto:`, indirizzo con "Apri la mappa". Nessun orario: non è pubblicato.
Piede petrolio scuro: logo chiaro (bozza SVG fedele, ricolorata), una riga su chi sono, colonne Azienda, Impianti, Service e noleggi, Contatti (indirizzo con link alla mappa); riga legale con Eurotecnica Salmaso S.R.L., P.IVA 01353510280, indirizzo, Privacy, Cookie. A 390 le colonne si impilano in ordine (due per riga, poi Service e Contatti).
Niente newsletter: il sito non pubblica notizie, fiere o cataloghi, il lavoro è a progetto per enti, scuole e parrocchie e una squadra di quattro persone non la alimenterebbe; per i privati del noleggio basta il telefono. Niente "Seguici": nessun profilo social trovato.

## Controlli

- Larghezze 320, 390, 768, 1024, 1440, 1920 guardate a pezzi: nessuno scorrimento orizzontale (scrollWidth uguale alla finestra, `_prova/script/misura.mjs`), nessun testo fuori finestra, il titolo non tocca il microfono (a 768 e 1024 il varco è stato allargato dopo la prima prova).
- `segnali.sh` (kit): 0 soglie bloccanti, 0 da guardare. Foto al 35,1 % della pagina a 1440; 3 filetti larghi; 3 misure di H2; 2 famiglie (Host Grotesk 88 %, General Sans 12 %); un solo numero grande (1967); nessuna etichetta maiuscola sopra i titoli; nessuna freccia; nessun titolo a sinistra con paragrafo a destra. Uscite in `_prova/segnali-finale/`.
- Nessun carattere U+2014 nella pagina, negli script e nei .md di questo compito.
- Dati in pagina tutti da `01-analisi.md`.
