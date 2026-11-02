# San Marco Timbri: proposta di nuova home

Proposta non richiesta di una nuova homepage per San Marco Timbri di Tosato Andrea (sanmarcotimbri.it, Padova). Solo la home.

## Dove sono le cose

- `sito/index.html`: la home finale (si apre con file:///). `sito/img/`: solo le immagini usate, JPEG e WebP in più larghezze. `sito/fonts/`: Encode Sans e la sua licenza (`OFL.txt`).
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, e `NOTA.md` (idea, schermate, caratteri, colori, interazione, foto, controlli).
- `_prova/script/build_finale.sh`: rifà tutto (scontorno del timbro, immagini, pagina, caratteri, screenshot). Gli altri script `fin_*` sono i suoi pezzi; `index.sorgente.html` è la pagina.
- `01-analisi.md`: fatti con le fonti. `assets/CREDITI.md`: origine e licenza di ogni immagine. `_prova/home/a` e `b`: i due prototipi.

## Dati da confermare (in pagina non c'è nulla di dubbio)

- **Indirizzo**: in pagina c'è via G. A. Longhin 91, 35129 Padova (sito e registri). Molti elenchi (coobiz, 2gis, trovainitalia) danno ancora via Domenico Turazza 42, 35128 Padova con lo stesso telefono: va chiesto quale delle due è la vecchia sede e, se serve, aggiornata la scheda di Google.
- **Orari** del laboratorio e se si riceve al banco o su appuntamento: oggi non ci sono; vanno nella chiusura, sotto la riga "Laboratorio".
- **Anno di inizio** dell'attività (la P.IVA risulta attiva da 11-20 anni; il sito dice solo "da molti anni"): con l'anno la chiusura può diventare "Da molti anni nel mercato" con la data, e la pagina avrebbe il contenuto datato che oggi manca.
- **Macchine vere** (marca e tipo della CNC, della fresa, del laser, della stampante digitale): la sezione "I file li prepariamo noi" usa solo la loro frase generica.
- Se **plexiglass, insegne luminose e casellari** si fanno in laboratorio o si comprano e si personalizzano.
- Che le **lettere in ottone brunito** e la **targa in corten** siano lavori loro e il permesso di usarle (in pagina le didascalie dicono solo cosa sono, non "un nostro lavoro"); per la targa, il nome del cliente e l'anno, se si possono dire.
- Il **WhatsApp** da mostrare (oggi 376 167 3361) e gli eventuali **social** veri: oggi le icone del vecchio piede non portano a nulla, quindi nel piede non c'è "Seguici".
- **PEC e REA**, se vogliono metterli nella riga legale (un'impresa individuale non ha capitale sociale).
- Se vogliono la **newsletter**, chi la scrive e con quale servizio (sotto).
- Se le 16 pagine "timbri-a-<comune>" vanno tenute.

## Newsletter: va collegata

Nel piede c'è "Novità e promozioni" con campo email, bottone "Iscriviti" e casella del consenso privacy. Oggi **non invia nulla**: controlla solo email e consenso e scrive un messaggio di cortesia. Per farla funzionare va collegata a un servizio (Brevo, Mailchimp, MailerLite o il modulo del CMS) con doppia conferma, e l'informativa privacy deve citare il servizio scelto. Se la newsletter non interessa, si toglie il blocco `.news` e il piede resta in ordine.

## Pagine del sito nuovo richiamate dalla home

Dalla home e dal piede partono link a queste pagine, da creare:
- `lavorazioni/targhe/`, `lavorazioni/incisioni/`, `lavorazioni/segnaletica/`, `lavorazioni/insegne/`, `lavorazioni/casellari-postali/`, `lavorazioni/premiazioni/`, `lavorazioni/pulsantiere/`, `lavorazioni/vetrinistica/`, `lavorazioni/plexiglass/`;
- `idee-regalo/calligrafia/`, `idee-regalo/ceralacca/`, `idee-regalo/penne-timbro/`;
- `chi-siamo/`, `novita/` (Promozioni e novità), `privacy/`, `cookie/`.
Timbri, Come lavoriamo e Contatti portano alle sezioni della home (`#timbri`, `#metodo`, `#contatti`).

## Foto da rifare dal vero

Una giornata di still life su carta avorio con luce laterale morbida (finestra o softbox da sinistra, pannello bianco a destra), fotocamera su cavalletto, almeno 3000 px sul lato lungo, fuoco su tutta la testa del timbro (diaframma chiuso o più scatti uniti):
1. **Apertura** (sostituisce la foto di Pauline Raw, che è un sigillo da ceralacca): un loro timbro in metallo con montatura in legno e ottone, appena sollevato, e accanto la sua impronta vera d'inchiostro sulla carta. Orizzontale 3:2, il timbro nella metà destra con il manico che esce dall'inquadratura a destra, la carta libera nel terzo sinistro per il titolo; meglio ancora un fondo carta da scontornare. L'impronta vera allora prende il posto di quella disegnata.
2. **Le lettere in ottone brunito** in macro, stessa luce (oggi la foto è da 1000 px).
3. **Il banco di via Longhin** con la CNC o il laser al lavoro e le mani di Andrea Tosato su un pezzo appena inciso: sostituisce le presse di repertorio della fascia (formato 3:1, la macchina al centro).
4. **La targa in corten in opera** rifatta più grande, o un'altra targa loro montata, per la chiusura; oppure la vetrina o la porta del laboratorio.
5. Utili per le pagine interne: un punzone in ottone con il suo segno a caldo, il leone "LEO" traforato, una pulsantiera in pietra, una targa in plexiglass sabbiato.

## Licenze

- Foto di repertorio (Pexels License, verificata sulla pagina di ogni foto il 24/10/2026): Pauline Raw (apertura), Dana Sredojevic (fascia). Dettagli e link in `assets/CREDITI.md`. Le foto loro (lettere in ottone, targa in corten) e i loghi vengono dal loro sito: vanno confermati prima di pubblicare.
- Carattere: Encode Sans, SIL Open Font License 1.1 (uso commerciale libero), servito dalla pagina; testo della licenza in `sito/fonts/OFL.txt`.

## Loghi

Esistono solo raster: `logo-orizzontale-641x114.jpg` (testata, mostrato a 36 px di altezza, circa 3x) e `logo-verticale-256x200.png` (piede, mostrato a 128 px, 2x), con il bianco reso trasparente. Il leone di San Marco con il libro "TARGHE" non si può ricostruire in SVG in modo fedele a questa risoluzione: serve l'originale vettoriale (e il nome del carattere della scritta, che somiglia a Comfortaa). Anche le icone del sito (favicon) vanno rifatte da lì.
