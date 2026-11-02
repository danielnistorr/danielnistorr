# Fratelli Ruffatti: proposta di nuova homepage

Proposta non richiesta di una nuova home per ruffatti.com (solo la home). Non è stata inviata, pubblicata o mostrata all'azienda.

## Dove sono le cose

- **Home finale**: `sito/index.html`, con `sito/img/` (solo le immagini usate, JPEG in più larghezze) e `sito/fonts/` (Gambetta e Switzer in woff2). Si apre con file:///, senza server.
- **Screenshot**: `screenshot/home/`, cioè home-1440.jpg, home-1440-prima-schermata.jpg, home-390.jpg, home-390-prima-schermata.jpg e chiusura-1440.jpg. Idea, caratteri, colori, foto e controlli sono in `screenshot/home/NOTA.md`.
- **Rifare tutto**: `sh _prova/script/build_finale.sh`. Rifà le immagini (`finale_img.py`), controlla U+2014 e le immagini mancanti o inutili, prova il gesto e lo scorrimento a sette larghezze (`finale_prova.mjs`) e rifà gli screenshot (`finale_shot.mjs`).
- **Materiali di lavoro**: analisi con le fonti in `01-analisi.md`, prototipi A e B in `_prova/home/a` e `_prova/home/b`, inventario e voti delle foto in `_prova/inventario-immagini.json`, testi scaricati in `_prova/crawl/`, crediti in `assets/CREDITI.md`.

## Dati da confermare con l'azienda

In pagina c'è solo ciò che ha una fonte. Restano da chiedere:

1. **Ragione sociale completa** con forma giuridica, REA, capitale sociale e PEC: non trovati. Per questo la riga in fondo al piede ha solo "Fratelli Ruffatti" e la P.IVA.
2. **Numeri di oggi.** "Oltre 500 organi in Italia" e "oltre 50 negli Stati Uniti" vengono da testi del 2016, e sono in pagina così. Vale lo stesso per "oltre un centinaio" di restauri e "da mezzo secolo" (altrove il sito dice "più di quarant'anni"). Quanti sono oggi, e quanti organi in tutto?
3. **Buckfast**: in pagina "consegnato tra il 2017 e il 2018" (container arrivati nell'aprile 2017). Servono la data dell'inaugurazione, la conferma che la foto mostra l'organo in cantoria e la disposizione finale: "cento file di canne, due consolle" viene da un testo del 2016 scritto al futuro, per questo in pagina non c'è più.
4. **Boteå**: l'anno di consegna; si sa solo il contratto, agosto 2015. Per questo in pagina non c'è l'anno. Va confermato anche se i tiranti in fibra di carbonio sono stati davvero realizzati (la notizia del 2015 dice "saranno utilizzati"): finché non lo confermano, in pagina non ci sono.
5. **Le parti della canna**: noce, canaletto e piede sono la mia lettura della foto `xtrompette3`, e anche le tre fasce che il gesto lascia piene (noce dal 10 al 38 % dell'altezza, canaletto dal 38 al 74 %, piede dal 78 %). Va fatta controllare a loro. La frase iniziale accanto alla canna unisce la loro "Costruire canne ad ancia è diventata attività rara per gli organari" (pagina Canne ad ancia) con "Le nostre nascono in laboratorio, parte per parte", che riassume "costruiamo ogni componente possibile in laboratorio": va approvata.
6. **Indirizzo e mappa**: Homo Faber scrive "Address upon request" e "By appointment only". Va confermato che via Facciolati 166 e il link alla mappa si possono pubblicare. "Su appuntamento" va aggiunto sotto l'indirizzo solo se lo confermano.
7. **Orari**: non pubblici, quindi non ci sono.
8. **Le trombe en chamade della chiusura** (`xOrgan064modif`): in quale chiesa sono? Il luogo va in didascalia.
9. **La foto delle maestranze**: l'anno (il nome di un file dice 1960).
10. **Newsletter**: è ancora attiva? L'ultimo numero è del 2020. Con quale servizio la mandano?
11. **Maestri d'Arte e Mestiere 2020**: va chiesto il permesso di citarlo; il marchio della Fondazione Cologni non è usato.
12. **La citazione di Michela Ruffatti** (Rockit, 13/05/2026): conferma che si può usare come titolo della sezione Opere.

## Foto da rifare dal vero

Le foto in pagina sono tutte loro, ma quasi tutte sono a 800 px. Per prima cosa vanno chiesti gli originali ad alta risoluzione: le foto a 800 px sono riduzioni dei file `P1…` e `DSC…`.

| Foto | Problema | Come rifarla |
|---|---|---|
| Canna ad ancia aperta (apertura) | 595x800 dopo la rotazione; in pagina è mostrata alla sua misura vera (mai ingrandita a 1x da 1024 px in su, ridotta sotto), ma sugli schermi retina è 2 volte, quindi morbida. È l'immagine che regge l'idea | Still life su carta avorio (o fondo bianco caldo), luce morbida da sinistra con un pannello di rimbalzo a destra. Canna intera in verticale, noce tornita e canaletto a fuoco (focus stacking se serve), almeno 4000 px sul lato lungo. Ombra corta e morbida, nessun riflesso di lampade sul metallo |
| Registro di Tromba (seconda sezione) | taglio 800x800, in pagina al massimo 800 px (1 volta), morbida a 2x; il terzo alto del file originale è sfocato | Le canne ad ancia di un registro sul somiere, in laboratorio, con luce naturale da una finestra laterale e senza flash; ottica lunga, diaframma 4-5,6; almeno 4000 px |
| Trombe en chamade (chiusura) | 600x600 dal file da 800x600, in pagina circa 676x780, ingrandita 1,3 volte | Chiedere l'originale di `xOrgan064modif` e il luogo, oppure rifarla nella chiesa con la luce del giorno, dal basso, con la parete chiara dietro |
| Maestranze (archivio) | 900x575, ingrandita 1,16 volte | Scansione dell'originale cartaceo a 1200 dpi |
| Buckfast | il file da 800 px è un ingrandimento 1,4 volte del taglio da 568 px | File originale della reflex (`756A…`) o le foto del fotografo dell'abbazia, con il permesso |
| Davies Symphony Hall | 800x1085, buona a 1x | Originale o foto del committente, con il permesso |

## Colore di fondo

Il fondo della pagina è #E7E8E2, il grigio chiaro della lega di stagno delle canne (lo stesso tono del metallo della canna in apertura e delle canne di facciata nelle foto delle opere); il piede è #DCDDD7, la lastra appena più scura. Sostituisce la carta avorio #F4F1EA della prima versione. Se l'azienda preferisce un fondo caldo, l'alternativa coerente col mestiere è il legno chiaro del somiere, non un beige generico.

## Licenze

- **Caratteri**: Gambetta e Switzer di Indian Type Foundry, da Fontshare, con licenza ITF Free Font License (uso commerciale gratuito, anche sul web). Sono serviti dalla pagina in `sito/fonts/`.
- **Foto**: tutte della Fratelli Ruffatti o dei committenti dei loro strumenti, prese dalla libreria media di ruffatti.com. Nella home finale non c'è nessuna foto di repertorio: la foto Pexels di Rene Terp del prototipo A è stata tolta. Le foto esterne in `assets/esterne/` restano solo come materiale dei prototipi (licenze in `assets/CREDITI.md`). Nessuna immagine è generata dall'IA. Va confermato chi ha i diritti delle foto delle installazioni (Buckfast, Davies, forse di fotografi terzi).

## Logo

- In testata e nel piede c'è il logo corsivo "Fratelli Ruffatti" nel bordeaux storico #6A0C10. È un PNG a 2x e 3x (`sito/img/logo-360.png`, `logo-640.png`), ricavato dalla maschera a 1 bit da 5024 px della newsletter 2020 (`assets/originali/logo-newsletter2020-1bit-5024.png`).
- Non l'ho vettorializzato: qui non c'è potrace, e un SVG fatto a mano non sarebbe fedele sulle code delle lettere. Va chiesto il file vettoriale originale e chi l'ha disegnato.

## Newsletter

Nel piede c'è un modulo con email, bottone "Iscriviti" e casella del consenso privacy. Ha senso tenerla: esiste già, con l'archivio 2017-2020, e hanno notizie da mandare (nuovi strumenti, incisioni, il concorso biennale di Miami).

**Il modulo oggi non fa nulla** (`action="#"`, invio bloccato). Va collegato a un servizio di invio (per esempio Brevo o Mailchimp, oppure al modulo che usano ora), con doppio consenso e un link all'informativa privacy vera.

## Pagine che il sito nuovo deve avere (link del menu e del piede)

Nella proposta tutti i link sono "#" oppure ancore della home. Servono queste pagine:
- **Azienda**: La nostra storia, La famiglia Ruffatti, La ricerca, Dicono di noi.
- **Organi**:
  - Come costruiamo; Le canne, con Canne ad ancia e Lastre per canne.
  - Realizzazioni: l'elenco delle opere significative, con il filtro per numero di tastiere (6, 5, 4, 3, 2, 1) e per Paese del prototipo B, che filtra senza ricaricare e mostra il conteggio, per esempio "7 strumenti a cinque tastiere". Il conteggio "86 strumenti in 14 Paesi" va dichiarato come conteggio dell'elenco "Alcune opere significative".
  - Il restauro, con Gli organi restaurati.
- **Notizie**: Ultime notizie, Concorso di Miami, CD DVD e video, Newsletter (archivio e iscrizione).
- **Servizio e lingue**: Privacy (oggi manca), Cookie, versioni EN e RU (IT EN RU sono in testata a 1440 e nel piede).
- **Da decidere**: la pagina `prova`, pubblicata per errore, e la pagina della petizione per S. Sofia.
