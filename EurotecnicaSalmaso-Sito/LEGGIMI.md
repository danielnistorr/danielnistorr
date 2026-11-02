# Eurotecnica Salmaso: proposta di nuova home

Proposta non richiesta di una nuova homepage per Eurotecnica Salmaso S.R.L. (Padova). Solo la home; le altre pagine sono quelle che il sito nuovo avrà (elenco sotto).

- Pagina: `sito/index.html` (statica, si apre con un doppio clic), immagini in `sito/img/`, caratteri in `sito/fonts/`.
- Screenshot e nota di progetto: `screenshot/home/` (`NOTA.md` spiega idea, caratteri, colori, interazione, foto e controlli).
- Rifare tutto: `bash _prova/script/build_finale.sh` (immagini, pagina, screenshot, controlli a 320, 768, 1024, 1920). `IMMAGINI=0` salta le immagini, `CONTROLLI=0` i controlli.
- Analisi con le fonti: `01-analisi.md`. Crediti delle foto: `assets/CREDITI.md`.
- Versione del 2 novembre 2026: sostituisce quella del 24 ottobre (stessa idea, fondo nel petrolio del marchio, microfono scontornato sull’asse che divide il titolo, chiusura e piede rifatti).

## Pagine linkate dalla home (da costruire)

| Indirizzo | Contenuto |
|---|---|
| `impianti/` con le ancore `#sale-congressi`, `#teatri`, `#aule`, `#chiese`, `#evacuazione` | impianti per tipo di sala, dai testi della pagina Impianti di oggi |
| `service/` con `#amplificazione`, `#traduzione`, `#video`, `#streaming` | le sei voci del service |
| `noleggi/` | elenco del materiale a noleggio e la regola dei giorni |
| `azienda/` con `#partner` | storia dal 1967 e lavoro con impiantisti, rivenditori e manutentori |
| `contatti/` | recapiti, mappa, modulo |
| `privacy/`, `cookie/` | informative (oggi c’è solo la privacy, pagina e PDF) |

Le sezioni della home hanno le ancore `#service`, `#noleggio`, `#impianti`, `#azienda`, `#contatti`. L’indirizzo apre Google Maps con una ricerca (`Eurotecnica Salmaso Via Lussemburgo 48 35127 Padova`): da sostituire con il link della loro scheda, se ne hanno una.

## Da confermare con l’azienda (non è in pagina)

- Codice fiscale 01871990238 stampato nel piede del sito di oggi: diverso dalla P.IVA e con codice d’ufficio di Verona. Refuso o vero? In pagina c’è solo la P.IVA 01353510280.
- REA, PEC e capitale sociale (atoka dice 10.000 euro): non pubblicati sul sito, quindi non in pagina. Se vanno nella riga legale, dal Registro Imprese.
- Anno di costituzione della srl (circa 40 anni secondo atoka) e legame con il 1967 dei fratelli Salmaso: la home dice "dal 1967" come il loro sito.
- Orari dell’ufficio e del ritiro noleggi: non pubblicati, la chiusura non li mostra.
- Il negozio "emporio dell’audio": aperto al pubblico? Con quali orari? Il dominio emporiodellaudio.it è in vendita. In pagina non compare.
- Le sale delle foto del 2024 (sala storica con soffitto dorato, palco sull’acqua): dove sono e se i committenti accettano di essere nominati. Le didascalie oggi non dicono il luogo.
- Se gli elenchi di Service e Impianti sono attuali (Skype e Lync superati; in pagina "programmi di largo utilizzo").
- Nel calcolo del noleggio: se il ritiro e il reso di domenica sono possibili (il sito dice "il giorno antecedente" e "il giorno successivo" senza eccezioni) e se consegna e montaggio avvengono il giorno prima, come la linea mostra (il sito dice solo che si possono chiedere).
- Marchi che vogliono mostrare (oggi un’immagine con 11 loghi): servono gli accordi; la home non ne mostra.

## Foto da rifare dal vero

Tutte le foto esterne sono segnaposto (licenze in `assets/CREDITI.md`): vanno sostituite prima di pubblicare.

1. **Apertura, il microfono**: un loro radiomicrofono a impugnatura, verticale, griglia in alto, su fondo chiaro uniforme (cartoncino o muro chiaro, poi scontornato), luce morbida di finestra da destra, macchina su cavalletto alla stessa altezza del microfono per non deformarlo, almeno 4000 px di altezza, il cavo tolto o tenuto dritto verso il basso. Senza marchi leggibili, o con il loro consenso. Se il microfono ha un anello colorato, meglio petrolio o grigio.
2. **Storia**: una delle unità per conferenze che progettavano a Padova (base con microfono o con votazione), se ne esiste ancora una, sul banco di un’aula consiliare vera; luce naturale, fondo sfocato, taglio quasi quadrato.
3. **Una sala per tipo** (teatro, sala consiliare, aula, chiesa) con i loro impianti, vuota, luce naturale, macchina sull’asse della sala (la home è costruita sulla simmetria): la chiusura vuole una sala simmetrica ripresa dal centro.
4. **Service**: la regia durante un convegno e un palco all’aperto, con una reflex o una mirrorless e non con il telefono; orizzontali, almeno 3000 px.
5. Diritti delle sei foto del 2024: l’EXIF riporta il copyright di un fotografo di repertorio (probabilmente ereditato da un modello di Photoshop). Da chiarire prima di usarle.

## Licenze

- Foto esterne: Unsplash License (DESIGNECOLOGIST hvgd0ygXuQQ, Valentin Karisch igNLOmbJBhg, Daniel Emale zBZZfr8_0ME, Nguyen Dang ft2Gpg_fNVY), lette sulle pagine delle foto il 24/10/2026. Nessuna immagine generata dall’IA.
- Caratteri: General Sans (Fontshare, ITF Free Font License, uso commerciale ammesso) e Host Grotesk (Google Fonts, SIL Open Font License 1.1), serviti dalla pagina; testi in `sito/fonts/`.

## Logo

- In testata e nel piede c’è `assets/logo-ricostruito-bozza.svg`, tracciato da me dal PNG bianco 366x101 del loro sito: fedele nelle forme, con piccole differenze negli angoli. Nel piede la stessa bozza ricolorata #E3EFED (`sito/img/logo-chiaro.svg`).
- Da chiedere: il vettoriale originale del logo (SVG, PDF o AI) e il nome del carattere; con l’originale si sostituiscono i due file e basta.
- Favicon: la stessa bozza; meglio il monogramma "ES" originale in SVG.

## Newsletter e social

Nessuna newsletter: il sito non pubblica notizie, fiere o cataloghi e il lavoro è a progetto. Nessun profilo social trovato, quindi nessuna colonna "Seguici". Se aprono un profilo, si aggiunge come parola nella colonna Contatti.
