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

- `still-life/`: gli still life (Calearo, Marijke, Superoro, Pianegonda, Lago, Calegaro e gli altri). Il portfolio di oggi ha la voce Still Life.
- `corporate/`: fotografia corporate. Il portfolio di oggi ha la voce Corporate.
- `studio/`: Stefano Aiti, chi è, lo studio di Mestrino.
- `costruzioni/`: Aiti Studio per strade e costruzioni (reportage di cantiere, fotografia aziendale, e qui anche livree dei mezzi, video e siti web, tolti dalla home).
- `clienti/`: i lavori per cliente.
- `privacy/` e `cookie/`.

Gli altri link vanno alle sezioni della home (#architettura, #cantieri, #studio, #contatti). Il link a Weddgraphy (matrimoni) è stato tolto dal piede finché il titolare non dice se lo vuole.

## Dati da confermare prima di mandarla

- **Identità e dominio.** La home tiene insieme l'autore (still life e architettura, stefanoaiti.com) e lo studio dei cantieri (aitistudio.it). Vanno confermati:
  - quale dominio resta;
  - il marchio: "AIT Studio", "Aiti Studio" o "Stefano Aiti Fotografo";
  - se il link a Weddgraphy (https://www.weddgraphy.it) va rimesso nel piede, nella colonna Studio.
- **Clienti che si possono nominare e diritti d'uso delle foto**:
  - in apertura: Calegaro, Marijke, Artufficio (Credito Cooperativo di Brendola), Gregorianum (la pagina del portfolio è "camillo-bianchi-gregorianum": va chiesto se il cliente è Camillo Bianchi e se si può nominare);
  - in architettura: Banca Prealpi con Artufficio, Studio 4 Marmicolor, Fornace Morandi;
  - nel cantiere: Salima (camion Scania in primo piano);
  - in chiusura: Superoro;
  - nell'elenco in testo: Luceplan, Bellissima Vodka, Trek, Goppion Caffè, Saip, Girardini, Martini Silvestro.
- **Didascalie da far confermare** (materiale, cliente, luogo):
  - in apertura: "Calegaro, ciotole in argento smaltato"; "Marijke, vaso di cubetti metallici"; "Artufficio, Credito Cooperativo di Brendola"; "Gregorianum, frangisole in mattoni";
  - "Banca Prealpi, arredo Artufficio";
  - "Studio 4 Marmicolor, scala a chiocciola in marmo";
  - "Fornace Morandi, la ciminiera e la facciata": il cliente è Bruno Stocco?
  - "Salima, cantiere stradale all'alba": il nome del file dice CAV Mirano;
  - "Superoro, gioielli in oro rosa".
- **La frase "Banche e casse rurali arredate da Artufficio"**: viene dal portfolio, dove Artufficio ha sei pagine di banche e casse rurali. È stata tolta la parte "con gli uffici tra i mattoni", che veniva solo dalla descrizione delle foto.
- **Citazioni.** La citazione di Aiti Studio («Ideazione, realizzazione ed editing vengono svolti totalmente da noi e con la nostra attrezzatura») è riportata con la maiuscola iniziale; nell'originale è dentro una frase più lunga. Le due frasi del titolo e della chiusura sono prese dalla sua frase su sa.com/about e divise in due.
- **Recapiti.** Va confermato se info@aitistudio.it resta un recapito del sito nuovo. Il telefono di Giulia Morandin non è in pagina: su ais.it ha una cifra di troppo, e serve il suo consenso.
- **TAU Visual.** Va chiesto se è ancora socio; non è in pagina.
- **Ragione sociale nel piede.** "Stefano Aiti Fotografo, ditta individuale" va confermata. La P.IVA e la PEC vengono dal piede di stefanoaiti.com. Il codice fiscale personale non è stato ripetuto.

## Foto da chiedere o rifare dal vero

Il materiale è buono, ma i file web sono piccoli: le copertine sono a 1900 px, il resto a 1200 px.

- **Originali ad alta risoluzione**, almeno 3000 px sul lato lungo per le foto a tutta larghezza e per l'apertura.
  - In apertura la foto è larga 1328 px a 1440 e 1808 px a 1920: oggi viene da copertine da 1900 px, che bastano a 1x ma non agli schermi 2x (ne servono circa 2700 a 1440). Vale per Calegaro, Marijke, Brendola e Gregorianum.
  - Lo stesso per Banca Prealpi e lo Scania (a tutta larghezza, oggi 1900 px), e per la scala, la Fornace e i gioielli Superoro (oggi 1900 e 1200 px).
  - Se arrivano gli originali basta metterli al posto dei file in `assets/originali/` e rilanciare `build_finale.sh`, aggiungendo le larghezze 2400 e 2800 in `finale_img.py`.
- **Una scelta di scatti per l'indice d'apertura.** Oggi sono quattro copertine del portfolio del 2017. Con il titolare va scelta una serie di quattro o cinque fotografie orizzontali, ciascuna con la sua luce, che regga il taglio 2:1 e quello quadrato del telefono; meglio se ci sono anche lavori recenti.
- **La sala di posa di Mestrino**, per la pagina Studio: orizzontale 16:10, luce bianca, i fari dello studio e il banco.
- **Un ritratto nuovo**: quello di oggi è del 2016, piccolo (667x1000).
- **Architettura più recente del 2017**, se c'è: il portfolio è fermo al 2017-2018.

## Licenze

- **Caratteri**: Switzer (Indian Type Foundry, Fontshare), ITF Free Font License, uso commerciale gratuito. I woff2 sono in `sito/fonts/`. Prima della messa online va riletto il punto sull'incorporazione nel sito.
- **Foto**: tutte di Stefano Aiti (vedi `assets/CREDITI.md`). I segnaposto Pexels in `assets/esterne/` non sono usati nella home finale.

## Loghi

- In testata c'è `sito/img/logo-ait.svg`, il solo segno AIT senza la riga STUDIO (a 58 px quelle lettere sarebbero alte 5 px); nel piede il logo completo a 96 px.
- Il logo completo è `sito/img/logo-ait-studio.svg`, tracciato dal favicon da 512 px di stefanoaiti.com (nero #040000, grigio #AAAEAD) e confrontato con l'originale a 900 e a 120 px.
- Non ho trovato un vettoriale ufficiale: va chiesto lo SVG o l'AI originale e sostituito.
- Nessun logo di clienti in pagina: i clienti sono scritti come testo.
