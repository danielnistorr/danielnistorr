# B.C.M. Enologia: proposta di nuova home

È una proposta non richiesta: una nuova homepage per B.C.M. Enologia S.r.l. di Saonara (PD), torchi, martinetti DAVID, gabbie, pompe e pigiatrici. Riguarda solo la home.

- **Pagina**: `sito/index.html`. È statica, si apre con un doppio clic. Le immagini sono in `sito/img/` e i caratteri in `sito/fonts/`.
- **Screenshot e nota**: `screenshot/home/`. La nota (`NOTA.md`) spiega l’idea, i caratteri, i colori, il gesto e i controlli.
- **Rifare tutto**: `bash _prova/script/build_finale.sh`. Rifà immagini, controlli e screenshot. I controlli dell'ultimo passaggio (larghezze da 320 a 2560, tastiera, tocco, link) si rifanno con `node _prova/script/controlli_finali.mjs`.
- **Analisi con le fonti**: `01-analisi.md`. Prototipi in `_prova/home/a` (scelto) e `_prova/home/b`.

Nessun contatto con l’azienda, nessun modulo inviato, niente pubblicato.

## Dati da confermare con BCM prima di inviare

- **Stato della società**: un estratto la diceva cessata, mentre aziende.it la dà "Attiva" e reportaziende pubblica ricavi 2025. Va verificato per primo.
- **Ragione sociale da scrivere**: in pagina c’è "B.C.M. Enologia S.r.l." (registro). Il sito dice "BCM srl", i cataloghi "BCM Enologia s.r.l.".
- **Civico**: 10 (sito) o 10-12 (cataloghi e registro). In pagina c’è 10-12.
- **Brevetto DAVID**: in pagina c’è solo "progettato e brevettato negli anni 80, oggi marchio registrato". Non c’è scritto che il brevetto sia in vigore.
- **"Costruiti a Saonara"**: confermare che forgiatura dei perni, gabbie e montaggio sono tutti in casa, e che il faggio è ancora "evaporato".
- **Didascalia dell’officina**: "Meccanismi in ghisa e ottone sul banco dell’officina, 2022". Va chiesto se sono corpi del DAVID o teste dei torchi a cricco, e se la foto è di Saonara. Se sono DAVID, la didascalia può dirlo.
- **Ricambi per le macchine vecchie**: in pagina c’è la loro frase "compatibilità con il passato" (brochure martinetti). Un esempio concreto, come un torchio degli anni 70 rimesso in funzione, la renderebbe più forte.
- **SIMEI 2026** (Fiera Milano, 17-20 novembre 2026): se ci vanno, la riga "In fiera" va aggiornata con date e padiglione.
- **Newsletter**: chi la scrive e quante volte. In pagina c’è "una volta l’anno", da confermare.
- **Clienti tipo e paesi di spedizione**: cantine piccole, hobbisti, rivenditori, estero.
- **PEC e fax** (bcmenologia@pec.it, 049 5018355): non sono in pagina e vanno confermati prima di metterli.
- **Settori "caseario, oleario, miele, glasse"**: lavori reali o solo possibili? Oggi non sono in pagina.
- **Vite del modello 45**: la brochure del torchio idraulico dà 45 mm, il catalogo generale 50 mm. In pagina c'è 45 (brochure): va chiesto quale vale.
- **Torchio in scala nel selettore**: la foto è del modello 60 e viene riscalata sull'altezza della gabbia (da 60 a 105 cm). Vite, martinetto e carrello non crescono davvero in proporzione: la didascalia lo dice ("Foto del modello 60, in proporzione alla gabbia del…"). Con le foto nuove servirebbe uno scatto per ogni misura, o almeno del 45, del 60 e del 90, alla stessa distanza.

## Pagine del sito nuovo

Oggi i link della home portano alle sezioni della home stessa (`#macchine`, `#martinetti`, `#ricambi`, `#storia`, `#contatti`) o alle pagine del sito attuale bcmenologia.com: le sei linee (`/it/prodotti/linea-torchi`, `linea-martinetti`, `linea-gabbie`, `linea-pompe-standard`, `linea-pigiatrici-e-pigiadiraspatrici`, `linea-frutta`), `/it/download`, `/it/gallery/in-fiera`, `/it/privacy-policy` e `/it/cookies`. Nel sito nuovo diventano le pagine qui sotto, con gli stessi percorsi o con un redirect.

- **Macchine**: Torchi, Martinetti DAVID, Gabbie, Pompe e inverter (con gli optional e l’inverter universale), Pigiatrici, Presse per frutta.
- **BCM**: Dal 1960 (chi siamo), Ricambi e assistenza (pagina nuova: oggi è solo una frase ripetuta nelle schede), Cataloghi (download), In fiera (galleria).
- **Contatti, Privacy, Cookie**.
- **Versione inglese**: i PDF ci sono già in quattro lingue. Oggi `/en/` dà errore 404.

## Newsletter

Il modulo del piede (email, bottone "Iscriviti", casella del consenso privacy) **non invia nulla finché non si collega a un servizio**, per esempio Brevo, Mailchimp o MailerLite, con doppio consenso e l’informativa aggiornata.
- Ha senso per BCM: cataloghi in quattro lingue, fiere, vendita anche a chi fa il vino in casa, una stagione precisa. Una lettera prima della vendemmia, con ricambi, cataloghi e fiere.
- Se nessuno la scriverà, meglio toglierla.

## Foto da rifare dal vero

Oggi le foto coprono il 29,5 % della pagina a 1440, contro il 35 % che la guida chiede. Il motivo è che BCM non ha foto grandi: le più larghe sono scatti da telefono di 1.920 px, il resto è scontornato dal sito. Gli scatti qui sotto risolvono anche questo: con una chiusura e un'officina vere a 4.000 px le due fasce possono andare a tutta larghezza e più alte.

Le foto in pagina sono tutte di BCM e vengono dal loro sito. Reggono per una proposta, non per il sito vero. Basta una giornata di scatti:

1. **Torchio idraulico 60 per l’apertura**:
   - intero, su fondo carta neutro, con luce da finestra laterale da sinistra e un pannello bianco a destra;
   - fotocamera ad altezza gabbia, obiettivo 70-100 mm per non deformare;
   - almeno 45 MP, file da 4.000 px di altezza (oggi il torchio regge fino a circa 900 px a schermo, e il bordo dello scontorno è duro);
   - uno scatto con e uno senza ombra a terra.
2. **Le sei macchine** (torchio a cricco, DAVID, gabbia, pompa Volumex, pigiatrice, pressafrutta):
   - stessa luce, stesso fondo, stessa altezza di ripresa del torchio, così la griglia è omogenea;
   - oggi pompe e pigiatrici hanno riflessi duri da catalogo.
3. **Officina**:
   - la fila di meccanismi sul banco con luce naturale, pavimento pulito, niente neon né teli colorati;
   - un orizzontale largo (rapporto 2:1) e un verticale 3:2 per il telefono;
   - macro del faggio, dei perni forgiati, del manometro e della targhetta.
4. **Chiusura**:
   - i torchi pronti in magazzino, come la foto di oggi (wa0000), con la stessa luce del pomeriggio ma senza imballi in plastica e scatole, in orizzontale largo (almeno 2:1, 4.000 px) e in un taglio 16:10 per il telefono; oggi la foto è rifilata in alto per togliere la plastica, e a 2560 px di schermo risulta ingrandita;
   - meglio ancora un torchio BCM al lavoro in una cantina vera durante la vendemmia, con il nome della cantina se acconsente.

## Licenze

- **Foto**: tutte dell’azienda (`assets/originali/`, scaricate dal sito bcmenologia.com). Va chiesto a BCM di confermarne i diritti.
  - Le foto di repertorio di `assets/esterne/` (licenze in `assets/CREDITI.md`) non sono usate nella home finale. L’uva di David Köhler (Unsplash) era solo nel prototipo.
  - Le slide di uva del sito di oggi sembrano di repertorio, con diritti da chiarire: non sono usate.
- **Caratteri** (serviti dalla pagina da `sito/fonts/`):
  - Zodiak (Indian Type Foundry, Fontshare, ITF Free Font License, uso commerciale gratuito);
  - Sofia Sans e Sofia Sans Condensed (Lettersoup, Google Fonts, SIL Open Font License 1.1).

## Logo

- Il logo in pagina è il PNG bianco del sito (170x96), ricolorato in inchiostro: in testata a 85x48 (2x), nel piede a 128x72 (1,33x, perché a 85x48 la riga "MACCHINE ENOLOGICHE" non si legge). Non l’ho ricostruito in SVG per non tradirlo.
- Va chiesto il file vettoriale, e quale versione usano oggi: quella bianca del sito ("BCM" con grazie e "MACCHINE ENOLOGICHE") o quella rossa dei cataloghi 2022 ("BCM Enologia s.r.l." in Times bold).
- Manca anche una favicon decente: oggi è 16x16.
