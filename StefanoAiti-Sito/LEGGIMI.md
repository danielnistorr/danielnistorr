# Stefano Aiti (AIT Studio): proposta di nuova home

Proposta non richiesta, solo la home. Non è stata pubblicata né inviata, e l'azienda non è stata contattata.

## Dove sono le cose

- `sito/index.html`: la home finale (statica, si apre con file:///), con `sito/img/` e `sito/fonts/`.
- `screenshot/home/`:
  - home-1440.jpg, home-1440-prima-schermata.jpg, home-390.jpg, home-390-prima-schermata.jpg, chiusura-1440.jpg;
  - NOTA.md, con l'idea, i caratteri, i colori, le foto e i controlli.
- `_prova/script/build_finale.sh`: rifà immagini, pagina e screenshot. Usa `finale_img.py`, `finale_index.html` (il modello della pagina) e `finale_shoot.mjs`.
- `01-analisi.md`: i fatti con le fonti. `_prova/home/a` e `_prova/home/b` sono i due prototipi; la finale parte da A.

## Pagine che il sito nuovo deve avere (link del piede)

- `corporate/`: fotografia corporate. Il portfolio di oggi ha la voce Corporate.
- `studio/`: Stefano Aiti, chi è, lo studio di Mestrino.
- `costruzioni/`: Aiti Studio per strade e costruzioni (reportage di cantiere, fotografia aziendale, livree dei mezzi, video, siti web).
- `clienti/`: i lavori per cliente.
- `privacy/` e `cookie/`.

Gli altri link vanno alle sezioni della home (#apertura, #architettura, #cantieri, #studio, #contatti). Matrimoni porta a https://www.weddgraphy.it.

## Dati da confermare prima di mandarla

- **Identità e dominio.** La home tiene insieme l'autore (still life e architettura, stefanoaiti.com) e lo studio dei cantieri (aitistudio.it). Vanno confermati:
  - quale dominio resta;
  - il marchio: "AIT Studio", "Aiti Studio" o "Stefano Aiti Fotografo";
  - se il link a Weddgraphy va nel piede.
- **Clienti che si possono nominare e diritti d'uso delle foto**:
  - in apertura: Calearo, Marijke, Superoro, Pianegonda (il marchio è inciso sull'anello), Lago (foto di catalogo);
  - in architettura: Banca Prealpi con Artufficio, Studio 4 Marmicolor, Fornace Morandi;
  - nel cantiere: Salima (camion Scania in primo piano);
  - in chiusura: Calegaro;
  - nell'elenco in testo: Luceplan, Bellissima Vodka, Trek, Goppion Caffè, Saip, Girardini, Martini Silvestro.
- **Didascalie da far confermare** (materiale, cliente, luogo):
  - "Calearo, antenna"; "Marijke, vaso di cubetti metallici"; "Superoro, anello in oro rosa"; "Pianegonda, anello in argento"; "Lago, tavolo";
  - "Banca Prealpi, arredo Artufficio";
  - "Studio 4 Marmicolor, scala a chiocciola in marmo";
  - "Fornace Morandi, la ciminiera e la facciata": il cliente è Bruno Stocco?
  - "Salima, cantiere stradale all'alba": il nome del file dice CAV Mirano;
  - "Calegaro, ciotola in argento".
- **La frase "Banche e casse rurali arredate da Artufficio"**: viene dal portfolio, dove Artufficio ha sei pagine di banche e casse rurali. È stata tolta la parte "con gli uffici tra i mattoni", che veniva solo dalla descrizione delle foto.
- **Citazioni.** La citazione di Aiti Studio («Ideazione, realizzazione ed editing vengono svolti totalmente da noi e con la nostra attrezzatura») è riportata con la maiuscola iniziale; nell'originale è dentro una frase più lunga. Le due frasi del titolo e della chiusura sono prese dalla sua frase su sa.com/about e divise in due.
- **Recapiti.** Va confermato se info@aitistudio.it resta un recapito del sito nuovo. Il telefono di Giulia Morandin non è in pagina: su ais.it ha una cifra di troppo, e serve il suo consenso.
- **TAU Visual.** Va chiesto se è ancora socio; non è in pagina.
- **Ragione sociale nel piede.** "Stefano Aiti Fotografo, ditta individuale" va confermata. La P.IVA e la PEC vengono dal piede di stefanoaiti.com. Il codice fiscale personale non è stato ripetuto.

## Foto da chiedere o rifare dal vero

Il materiale è buono, ma i file web sono piccoli: le copertine sono a 1900 px, il resto a 1200 px.

- **Originali ad alta risoluzione**, almeno 2000 px sul lato lungo per gli still life e 3000 px per le foto a tutta larghezza.
  - In apertura l'oggetto è largo 835 px a 1440: a 2x ne servono 1700.
  - Nei tagli di oggi l'antenna Calearo ha 984 px utili, il Marijke 625 (e allo zoom si vede), il Superoro 947, il Lago 928; il vaso Marijke viene da un file di 1200x800.
  - Servono anche Banca Prealpi, la scala, la Fornace e la ciotola di Calegaro (che oggi è a 1200 px).
- **Antenna Calearo con l'ombra di contatto vera.** Il file web è uno scontorno su bianco puro senza ombra. Serve:
  - l'originale non scontornato, oppure uno scatto nuovo su limbo bianco;
  - luce morbida dall'alto e un pannello di schiarita, così che sotto la base resti una piccola ombra morbida;
  - camera all'altezza della base o appena sopra, con un'inquadratura che lasci aria sopra l'oggetto.
  - Lo stesso vale per gli altri still life dell'indice: stesso limbo, stessa luce, stessa altezza di camera, così il cambio sul fondale resta omogeneo.
- **La sala di posa di Mestrino**, per la pagina Studio: orizzontale 16:10, luce bianca, i fari dello studio e il banco.
- **Un ritratto nuovo**: quello di oggi è del 2016, piccolo (667x1000).
- **Architettura più recente del 2017**, se c'è: il portfolio è fermo al 2017-2018.

## Licenze

- **Caratteri**: Switzer (Indian Type Foundry, Fontshare), ITF Free Font License, uso commerciale gratuito. I woff2 sono in `sito/fonts/`. Prima della messa online va riletto il punto sull'incorporazione nel sito.
- **Foto**: tutte di Stefano Aiti (vedi `assets/CREDITI.md`). I segnaposto Pexels in `assets/esterne/` non sono usati nella home finale.

## Loghi

- Il logo nella testata e nel piede è `sito/img/logo-ait-studio.svg`, tracciato dal favicon da 512 px di stefanoaiti.com (nero #040000, grigio #AAAEAD) e confrontato con l'originale a 900 e a 120 px.
- Non ho trovato un vettoriale ufficiale: va chiesto lo SVG o l'AI originale e sostituito.
- Nessun logo di clienti in pagina: i clienti sono scritti come testo.
