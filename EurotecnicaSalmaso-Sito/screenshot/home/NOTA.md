# Home finale Eurotecnica Salmaso, "Il giorno dell’evento" (seconda versione, rifinita il 2 novembre 2026)

Pagina: `sito/index.html` (statica, si apre anche da file), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini, pagina, screenshot e controlli); i controlli finali sono in `_prova/script/controlli.mjs`. Base: prototipo B scelto dal giudice, con gli innesti di A; questa versione sostituisce quella del 24 ottobre per la richiesta del committente ("più alta gamma, meno uguali tra loro") ed è rifinita sul giudizio cieco del 2 novembre (62/80, passa).

Altezza: 6997 px a 1440 con il piede, 8119 px a 390.

## L’idea

Il radiomicrofono sta sull’asse della pagina e divide il titolo come uno spazio fra le parole: "Il | giorno / dell’ | evento". Il suo cavo scende fino alla linea dei tre giorni del noleggio, dove l’anello petrolio segna il giorno dell’evento: a sinistra il ritiro, a destra il reso. È la loro regola vera ("Quotiamo solo il/i giorno/i di effettivo utilizzo e non quello di consegna e di reso") disegnata con il loro oggetto. L’asse torna dove serve: il filo verticale fra le due colonne del service e delle sale, i tre giorni del calcolo a sinistra, al centro e a destra, le due foto del service ai due lati dell’asse, la sala consiliare simmetrica della chiusura con il lampadario sull’asse.

Con il nome di un concorrente la pagina non regge: la linea è la loro regola del noleggio, i testi sono i loro (sistemi per conferenze fatti a Padova, MePA OS 30, Via Lussemburgo).

### Rispetto alla richiesta del 2 novembre

1. Nessuna legenda sull’oggetto: il microfono non ha etichette, solo il cavo che porta ai giorni.
2. Il fondo viene dal marchio: il petrolio del logo (#257B82) appena accennato, #E9F1EF, e un tono più pieno, #D7E6E3, solo nella sezione del noleggio, quella da usare. Lo stesso petrolio è nel logo in testata, nell’anello della griglia del microfono (portato dall’azzurro della foto al petrolio del logo), nel 1967 e, scurito, nel piede (#123E42, come il piede petrolio del loro sito di sempre).
3. Una scelta d’impaginazione che nelle altre home della campagna non c’è (controllate le copertine di Grisignano e le prime schermate delle altre cartelle: tutte hanno titolo a sinistra e oggetto a destra o sotto): composizione simmetrica sull’asse, con il titolo spezzato dall’oggetto, che a quella scala si legge come una lettera del titolo.

## Rifinitura sul giudizio cieco (2 novembre)

Applicato:
- **Fondo**: da #D7E6E3 ovunque a #E9F1EF per la pagina, #D7E6E3 solo per il noleggio (fascia piena da bordo a bordo). Contrasti rifatti: inchiostro 15,3:1, testo secondario #43514F 7,2:1, petrolio #1A5E63 6,5:1 (5,8:1 sul noleggio), #257B82 4,3:1 solo nel 1967 a 212 px.
- **Foto del service**: le due foto del 2024 da telefono ora sono tagli 3:2 larghi 420 px, ai due lati dell’asse con 24 px fra loro; la regia è tagliata prima del monitor di controllo, così il testo sullo schermo resta fuori. A 601-900 restano affiancate, a 390 una sotto l’altra.
- **Colonne a specchio**: tolto l’allineamento a destra della colonna sinistra; entrambe le colonne a sinistra, il filo verticale fa da divisorio. Il difetto di "Videoconferenza" veniva dalle righe interne del `li` in griglia che si allungavano: ora `align-self:start`, le coppie partono alla stessa altezza.
- **Ritmo**: "Impianti che restano in sala" a sinistra sul margine, a 92 px, appoggiato a 28 px sulla foto del teatro; il paragrafo va sotto la foto. Nella chiusura tolto il paragrafo d’introduzione: restano la loro frase e il telefono. Il paragrafo del service ridotto a una riga.
- **Teatro**: dall’originale più grande (3600x2395, stessa foto Unsplash) tagli 16:9 in cinque larghezze fino a 2880; a 1440 nessun ingrandimento né a 1x né a 2x.
- **Chiusura**: dall’originale 3200x4800 (stessa foto) tagli 3:2 fino a 2520 px, centrati sull’asse del tavolo; i cordoni rossi del museo e il visitatore dietro la vetrata tolti con un ritocco per diffusione (`ritocca_rosso` in `finale_img.py`), le fasce che legano le tende restano. A 2x il lato utile è 2520 su 2880 richiesti (ingrandimento 1,14): oltre non si può senza riprendere i cordoni.
- **Giorni feriali**: ritiro e reso solo dal lunedì al venerdì finché non sappiamo se sabato e domenica sono aperti; la pagina parte dal primo giovedì fra almeno due giorni (oggi: ritiro mer 4, evento gio 5, reso entro ven 6). Un evento di lunedì dà "Il venerdì prima", uno di sabato "il lunedì successivo".
- **Telefono** scritto 049 760348 dappertutto (6 link `tel:+39049760348`).
- **Paragrafo dell’apertura**: parte dal margine a 72 px come il logo e "Ritiro", tre righe; a 768 parte da 38 px, largo al massimo 300 px, alzato di circa 100 px.
- **Cavo del noleggio**: spesso come quello dell’apertura (4 px, stesso riflesso #5d6a6b), fermo sui margini del contenuto.
- **Piede**: indirizzo su due righe e "Apri la mappa" a parte; nella colonna Azienda "MePA e pubblica amministrazione" al posto di "Contatti" (duplicato); a 390 una colonna sola per tutti e quattro i gruppi, fra 601 e 1000 due per riga; l’indirizzo della riga legale non si spezza.
- **Preload dei caratteri** tolti (aperti come file:// davano errori CORS): console a zero errori. Da rimettere con il sito in http.
- **Menu del telefono**: pannello a tutta altezza, il telefono grande in fondo, la pagina sotto ferma, "Chiudi", Esc chiude, una voce chiude e porta alla sezione.
- **Storia**: la foto sale a sette colonne (fino a 818 px) e il testo ha 40 px d’aria dal bordo della foto; serve anche a tenere le foto sopra il 35 % della pagina dopo aver rimpicciolito quelle del service.

Respinto: nessun difetto respinto del tutto. Per la chiusura a 2x il limite di 2520 px è spiegato sopra.

## Le prime due schermate

1. **Apertura** (1440x900). Testata con il logo, il menu centrato sopra il microfono e il telefono. Il microfono alto 650 px sull’asse; il titolo in General Sans 500 a 178 px diviso dal microfono; sotto, a sinistra dal margine le tre righe che dicono il mestiere ("Impianti audio e video per teatri, sale congressi, aule e chiese: li progettiamo e li installiamo. Per convegni ed eventi li portiamo in sala o li noleggiamo. Da Padova, dal 1967."), a destra il bottone "Chiama 049 760348" e il link "Impianti per le sale". In basso la linea dei tre giorni a tutta larghezza, con "Si quota solo il giorno dell’evento." sotto l’anello. Tutta la linea porta al calcolo.
   A 390 (390x844): l’asse si sposta al 39 % perché le due metà del titolo stiano nella larghezza; microfono, titolo diviso, linea dei tre giorni, le tre righe, bottone e link: tutto nei primi 844 px.
2. **Cosa portiamo in sala**: titolo centrato e una riga, le due foto vere del 2024 piccole ai due lati dell’asse con didascalia, poi le sei voci del service in due colonne con il filo in mezzo.

Poi: il noleggio sul suo fondo (il gesto), gli impianti con il titolo a sinistra sul teatro a tutta larghezza e le quattro sale, la storia con la foto a sinistra fino al bordo e il 1967 a destra, la chiusura con la sala consiliare a tutta larghezza, il piede.

## Caratteri

- **General Sans 400 e 500** (Indian Type Foundry, Fontshare, licenza ITF Free Font License: uso commerciale e web gratuito) per titoli, date e numeri grandi. Riferimenti: d&b audiotechnik (grotesk geometrica, frase breve su fondo chiaro) e Genelec (titolo grande accanto a un solo prodotto vero). Spaziatura -0,045em nel titolo, interlinea 0,92.
- **Host Grotesk** variabile (Element Type, Google Fonts, SIL Open Font License 1.1) per testo, telefono, P.IVA e date dei comandi, con cifre tabellari.
- I file sono serviti dalla pagina (`sito/fonts/`, licenze in `sito/fonts/LICENZE.md` e `OFL-host-grotesk.txt`). Nessun carattere delle liste b della guida, nessun monospazio, niente corsivi. `text-rendering: geometricPrecision` evita i vuoti dopo la f che Chromium apriva con la spaziatura negativa.
- Apostrofo tipografico ’ in tutta la pagina, titolo compreso; la build si ferma se trova un apostrofo dritto nel testo.

## Colori

Fondo #E9F1EF (petrolio del logo appena accennato), noleggio #D7E6E3, piede #123E42 (petrolio scurito). Inchiostro #141A1C (15,3:1), testo secondario #43514F (7,2:1), link e accenti #1A5E63 (6,5:1), #257B82 solo in grande (1967, 4,3:1). Nel piede testo #E3EFED (9,9:1) e titoletti #A9C8C5 (6,6:1). Il rosso del velluto, l’oro e il giallo delle tende stanno solo dentro le foto.

## L’interazione (una sola)

"Quotiamo solo i giorni di effettivo utilizzo": comandi centrati su una riga (giorno dell’evento con frecce e calendario nativo, durata 1, 2 o 3 giorni, ritiro in sede o consegna e montaggio). La linea dei tre giorni sotto, sul cavo, mostra ritiro o consegna nel giorno feriale prima, i giorni quotati, il reso o il ritiro a fine evento o nel primo giorno feriale dopo, con le frasi del loro sito; lo stesso stato si aggiorna nella linea dell’apertura. Nessun prezzo. Bottoni veri (`aria-pressed`, `aria-live` sui risultati), provati con tastiera e tocco. Transizioni di 150 ms solo sui colori di bottoni e link; nessuna animazione allo scorrere, nessun effetto che segue il cursore. Il cavo è un SVG di poche righe che parte dal pressacavo del microfono (posizione scritta dalla build in `cavo.json`) e si ridisegna al cambio di misura.

## Foto, origine e licenza

- **Microfono**: DESIGNECOLOGIST, Unsplash hvgd0ygXuQQ, Unsplash License. Lavorato con PIL in `_prova/script/finale_img.py`: tolta la scritta "SPEAK UP", sfumate le scritte sul connettore, scontornato (WebP con trasparenza, 150, 220 e 289 px di larghezza), anello della griglia portato al petrolio del logo, cavo vero tolto sotto il pressacavo. Segnaposto.
- **Service**: due foto dell’azienda dallo slider del 2024 (`2024-05-1.jpg`, `2024-05-3.jpg`), scatti da telefono 1600x616: tagli 3:2 (924x616) a 420 px, nitidezza smorzata. Diritti da chiarire.
- **Impianti**: Valentin Karisch, Unsplash igNLOmbJBhg (palchi della Staatsoper di Vienna), Unsplash License; originale 3600 px, 16:9 a tutta larghezza.
- **Storia**: Daniel Emale, Unsplash zBZZfr8_0ME (unità per conferenze in un’aula consiliare, come i sistemi che progettavano a Padova), Unsplash License, a sinistra fino al bordo.
- **Chiusura**: Nguyen Dang, Unsplash ft2Gpg_fNVY (sala consiliare ovale con i microfoni a collo di cigno, simmetrica), Unsplash License; originale 3200 px, 3:2 a tutta larghezza, cordoni del museo ritoccati via.
- Licenze rilette il 2/11/2026 sulle pagine di Karisch e Dang ("Free to use under the Unsplash License"). Nessuna di queste foto è usata in un’altra home della campagna (ID cercati in tutti i `*-Sito/assets/CREDITI.md`). Nessuna immagine generata dall’IA.
- Trattamento unico: neri sollevati verso il petrolio, saturazione all’82-86 %, JPEG progressivi in più larghezze con `srcset`.

## Chiusura e piede

Chiusura "b con foto", testo sopra e foto a tutta larghezza sotto: la loro frase "Avete bisogno di un consiglio o di una consulenza tecnica?" come titolo, telefono a 64 px sottolineato con `tel:`, info@ e service@ con `mailto:`, indirizzo con "Apri la mappa". Nessun orario: non è pubblicato.
Piede petrolio scuro: logo chiaro (bozza SVG fedele, ricolorata), una riga su chi sono, colonne Azienda, Impianti, Service e noleggi, Contatti (indirizzo su due righe, "Apri la mappa" a parte); riga legale con Eurotecnica Salmaso S.R.L., P.IVA 01353510280, indirizzo, Privacy, Cookie. A 390 una colonna sola, in ordine.
Niente newsletter: il sito non pubblica notizie, fiere o cataloghi, il lavoro è a progetto per enti, scuole e parrocchie e una squadra di quattro persone non la alimenterebbe; per i privati del noleggio basta il telefono. Niente "Seguici": nessun profilo social trovato.

## Controlli (2 novembre, dopo la rifinitura)

- `_prova/script/controlli.mjs`: scrollWidth uguale a innerWidth a 320, 360, 390, 414, 600, 601, 768, 900, 901, 1024, 1180, 1280, 1440, 1680, 1920, 2560 (a 901 il piede sforava di 46 px: corretto con due colonne per riga fino a 1000); console a 0 errori aperta come file://; 6 link `tel:` tutti +39049760348, 5 `mailto:` coerenti, 2 link alla mappa; nessun U+2014; telefono scritto sempre uguale.
- Nitidezza a 1440: teatro, storia e service a 1x e 2x senza ingrandimento; chiusura 1x senza, 2x 1,14 (vedi sopra).
- Gesto: tastiera a 1440 (Invio sulle frecce, Tab fino a "3 giorni", Invio, Tab, Spazio su "Consegna e montaggio"), tocco a 390 (2 giorni, consegna, freccia); giorni feriali verificati su un evento di lunedì e uno di sabato; la linea dell’apertura segue. Menu a 390: pannello 68-844 px, pagina ferma, `aria-expanded`, Esc e voce chiudono.
- Screenshot a 320, 390, 768, 1024, 1440, 1920 guardati a pezzi: nessun testo fuori finestra, il titolo non tocca il microfono.
- `segnali.sh` (kit): 0 soglie bloccanti, 0 da guardare. Foto al 35,6 % della pagina a 1440; 4 misure di H2 (64, 92, 42, 62 px); 4 fasce di fondo; 4 filetti larghi; 2 famiglie (Host Grotesk 87,5 %, General Sans 12,5 %); un solo numero grande (1967); nessuna etichetta maiuscola sopra i titoli; nessuna freccia; nessun titolo a sinistra con paragrafo a destra. Uscite in `_prova/segnali-finale/`.
- Nessun carattere U+2014 nella pagina, negli script e nei .md di questo compito.
- Dati in pagina tutti da `01-analisi.md`.
