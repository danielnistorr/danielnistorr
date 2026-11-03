# Servalli Padova: proposta di nuova homepage

Proposta non richiesta di una nuova home per Servalli Padova sas (servalli.net), solo la home. Non è stata contattata l'azienda né pubblicato nulla.

- Pagina: `sito/index.html`, con immagini in `sito/img/` e caratteri in `sito/fonts/`. Si apre con il browser come file locale.
- Screenshot e nota del progetto: `screenshot/home/` (`NOTA.md`, sezione "Livello professionale": struttura, esito delle 15 regole, compiti della scheda, controlli, caratteri e licenze).
- Rifare tutto: `bash _prova/script/build_finale.sh` (immagini, pagina, caratteri, screenshot, controlli).
- Analisi con le fonti: `01-analisi.md`. Scheda d'uso e d'identità: `_prova/uso/SCHEDA.md`.
- Ultimo passaggio (3 novembre 2026), "livello professionale": la home è rifatta sull'uso (negozio, alberghi, rivenditori) e sulle regole dello studio; niente più foto di repertorio. La versione 1 di prima (il Tabriz al centro) è in `_prova/versione-1-originale/`.
- Ritocco finale (3 novembre 2026): in apertura la Giardiniera "Manifatture Tessili Servalli" del 1967 al posto della trapunta SINFONIA (foto Molina, tolta); categorie e prodotti come indice e listino tipografici invece di schede senza foto; le guide subito sotto i prezzi; i numeri in grande su nero; una sola cronologia; testo descrittivo a 17 px; dopo "Prepara l'email" il testo resta pronto da copiare. Esito regola per regola in `screenshot/home/NOTA.md`.

## Da chiedere o confermare con l'azienda

**Dati in pagina da confermare**
- **Prezzi**: FIORDO 90 1p 178,12 euro, M.B. 2P 329,40, ISLANDA 597,80, PIETRA 80x150 29,10, Tabriz ghali 6.191,50 (letti sul negozio online, riportati in pagina "al 3 novembre 2026"). Nel sito vero vanno letti dal negozio Ecwid, non scritti a mano.
- **Spedizione gratuita sopra i 150 euro** (escluse isole, laguna di Venezia e alcune zone) e **reso entro 14 giorni**: dalle condizioni del negozio; che siano ancora così.
- **Codice BENVE10**: non è in pagina. Se è ancora valido, si può aggiungere sotto il bottone del negozio.
- **Consegna in tutta Italia** e **"Vasto assortimento sempre pronto"**: valgono anche per le strutture fuori regione? Tempi di consegna: non pubblici, non scritti; se vogliono, una riga ("in X giorni lavorativi dagli articoli pronti").
- **Festivi e chiusure**: in pagina l'ufficio risulta aperto lun-ven 9:00-17:30; nei festivi nazionali la pagina scrive solo "oggi è festivo". Vanno chiesti: chiusi nei festivi? Chiusura estiva o di Natale? Il 13 giugno (Sant'Antonio)?
- **Chi può venire in sede**: in pagina c'è solo "Ai privati vendiamo solo online". Se la sede riceve rivenditori e strutture (su appuntamento o negli orari), si scrive accanto all'indirizzo. Le condizioni Ecwid parlano di ritiro "presso un punto vendita del Gruppo Servalli": testo di modello, da verificare.
- **Metodi di pagamento** del negozio: non verificati, quindi non scritti accanto alla spedizione. Se ci dicono quali sono (carta, PayPal, bonifico), una riga breve sotto "Reso entro 14 giorni".
- **Il motto "da quattro secoli"**: in pagina è spiegato con le loro parole ("l'attività affonda le radici nel Seicento", il paramento con lo stemma al Museo della Basilica di Gandino). Che la spiegazione vada bene a loro.
- **Ragione sociale**: "Servalli Padova sas di Servalli Francesco e Alessandro" (VIES). Chi sono oggi i soci, e se sono la quarta generazione.
- **REA e PEC**: non trovati, da aggiungere alla riga legale.
- **Anni e racconti**: firma "dal 1895" (titolo del sito) o "fine del 1800" (pagina storia); il motto "da quattro secoli" è un racconto di famiglia (il paramento del Seicento a Gandino), non l'età dell'azienda. Le date della pagina (1949 MADIVAL, 1967 Padova, 1982 Servalli Padova, 1994 Alans, 2022 online) e "Franco Servalli fondatore del Centro Grossisti" vengono dalla loro pagina `storia`.
- **"Circa 20.000 articoli"** (pagina `informazioni`): che sia ancora il numero giusto.
- **Serline**: in pagina i marchi sono solo i tre registrati (Servalli, Alans, Colorcasa). Che cos'è Serline e se va citato.

**Cose che mancano e servirebbero (regole 9, 10 e 11 dello studio)**
- **Recensioni** con nome e comune (Google, negozio online): non ne abbiamo trovate. Se ne hanno, una fascia di tre.
- **Clienti con il nome**: tre o quattro alberghi, SPA o catene serviti, con il permesso di citarli.
- **Forniture con il nome**: tre lavori per strutture, ognuno con cliente o luogo, anno, articoli e quantità (per esempio "Hotel X, Abano, 2025: 400 teli doccia e 200 accappatoi con logo ricamato"), e una foto di ciascuno.
- **Certificazioni dell'azienda**: non ne risultano (OEKO-TEX Standard 100 e NOMITE sono dei prodotti). Se ne hanno, vanno nel piede.
- **Social veri**: oggi le icone del sito puntano alle home generiche; nel piede non c'è una colonna social.

## Modulo di contatto (da collegare)

Il modulo in fondo alla home ("Scriveteci") oggi **compone un'email** con `mailto:` a info@servalli.net: oggetto "tipo di richiesta, nome (società)" e nel testo tipo, nome, società, ruolo, partita IVA, telefono, email e messaggio. Controlla che ci siano tipo, nome, email valida e messaggio. Non invia nulla da solo: il visitatore manda l'email dal suo programma, e un'email aperta così non porta allegati (il logo e l'elenco delle quantità si allegano a mano, lo dice la riga sotto il modulo). Per chi non ha un programma di posta (webmail in ufficio), dopo "Prepara l'email" compare sotto il modulo lo stesso testo, con destinatario e oggetto, e il bottone "Copia il testo".

Va **collegato a un servizio** che riceva i campi e mandi l'email all'azienda, con un allegato (logo, elenco in PDF o Excel), per esempio Formspree, Getform, il modulo del costruttore del sito o un piccolo script sul server, con il controllo anti-spam e la riga sulla privacy. Il tipo di richiesta va tenuto come primo campo (serve a smistare: strutture, rivenditori, privati).

La newsletter della versione 1 è stata tolta: non inviava nulla. Se la vogliono, si rimette nel piede collegata a un servizio di invio (Brevo, Mailchimp, MailerLite) con doppia conferma.

## Foto da fare dal vero

Nella pagina ci sono solo foto vere del loro sito e del negozio; dove non ce n'erano che reggessero (categorie, prodotti, alberghi) la pagina si regge sulla tipografia. In apertura oggi c'è la Giardiniera del 1967 (1024 x 768, l'originale del sito): va chiesta la stampa o una scansione più grande. Per arrivare al livello dei riferimenti servono, nell'ordine:

1. **Apertura definitiva: persone e magazzino** (regola 3). È la foto che sostituirà la Giardiniera in apertura (la Giardiniera torna nell'archivio). Una o due persone della famiglia o del magazzino tra gli scaffali della biancheria al Centro Grossisti, o al banco mentre piegano o mostrano un piumino; luce naturale o un grande pannello morbido, nessun flash diretto; orizzontale, almeno 3000 px sul lato lungo. Le persone guardano la merce, non l'obiettivo.
2. **Still life per le 6 categorie e i 4 prodotti** (regola 9): stesso fondo (un piano bianco o un lino naturale), stessa luce laterale di finestra, stesso taglio quadrato, macchina alla stessa altezza per tutta la serie. Piumino piegato, lenzuola in pila, accappatoio, tappeto arrotolato, telo mare, un tappeto da bambino. Così le tessere e le schede dei prodotti prendono la foto, tutte uguali per misura.
3. **Spugna con un logo ricamato da loro** per il blocco alberghi: due o tre asciugamani d'albergo piegati, il ricamo a fuoco in luce radente; più, se c'è, un articolo ignifugo con l'etichetta.
4. **Il Tabriz e due o tre tappeti Alans, dall'alto**: tappeto steso, macchina in bolla sulla verticale, obiettivo 35-50 mm, luce radente da un lato per il vello; più il retro con i nodi e il frangiato. Oggi il ritaglio del Tabriz è solo 749 px.
5. **Archivio**: scansioni a 600 dpi delle stampe originali (telai, Giardiniera 1967, oggi 1024 px, Persia, MADIVAL, oggi la foto di una stampa con i riflessi), più il tappeto con la scritta SERVALLI annodata, oggi troppo piccolo.

## Licenze e permessi

- **Foto in pagina**: solo materiale del loro sito e del negozio (vedi `assets/CREDITI.md`).
  - Tabriz ghali (marca Alans): foto del negozio online, che può essere del fornitore. **I diritti vanno chiariti.** La trapunta SINFONIA (marca Molina) non è più in pagina.
  - Archivio (Giardiniera 1967 in apertura, telai, camion MADIVAL) e Persia ("© Franco Servalli", firma lasciata): della famiglia, **va chiesto il permesso**.
- **Nessuna foto di repertorio** e nessuna immagine generata o disegnata in pagina. Le foto Unsplash e Pexels scaricate per le versioni precedenti restano in `assets/esterne/` ma non sono più usate.
- **Caratteri**: Libre Caslon Display e Golos Text, da Google Fonts, SIL Open Font License 1.1, serviti dalla pagina in `sito/fonts/`.

## Loghi

- Usato: `assets/originali/logo-servalli-stemma.png` (1920 x 823), dal sito. Il bianco è reso trasparente lasciando intatti i colori dello stemma; in testata stemma e SERVALLI senza la sottoriga, nel piede e nella fascia dei marchi il logo intero con la scritta in bianco.
- Alans e Colorcasa: le versioni bianche del piede del sito di oggi (393 x 110 e 392 x 180), mostrate alla stessa altezza degli altri due (56 px, 36 a 390). Colorcasa a quella misura è debole: va chiesto il vettoriale.
- Va chiesto il **logo vettoriale** Servalli e il valore esatto dell'oro e dell'arancio dello stemma (in pagina #D86C30 e #E4B448, campionati sul PNG).

## Pagine a cui puntano i link

I link usano i percorsi del sito di oggi, che esistono: `negozio/` e le sue categorie e schede (Ecwid), `negozio/cart`, `negozio/pages/terms`, `storia`, `premi-e-riconoscimenti`, `informazioni`, `alberghi`, `partners`, `blog` e gli articoli (`100-piuma-cosa-intendi-piuma-piumino-e-piumetta`, `piumini-classi-en-12934`, `formato-tappeto-poshti-zaronim-ghali`), `informazioni-legali`. Da creare: `privacy/` e `cookie/`. Da togliere dal sito di oggi: le tre pagine orfane del modello (`living-room`, `Bedroom-Camera`, `copia-di-camera-da-letto`).

## Altre fonti delle righe in pagina

Oltre a `01-analisi.md`, `_prova/uso/SCHEDA.md` e questo file, alcune righe della home vengono dalle pagine del sito di oggi salvate in `_prova/crawl/`:
- `_prova/crawl/sitemap.xml`: i nomi di categorie e prodotti del negozio usati nell'indice e nel listino (FIORDO, M.B. oca bianca, SIBERIA, ISLANDA, completi copripiumino in raso di cotone, accappatoi in spugna cimata jacquard, tappeti Disney top line, teli mare e fouta in cotone jacquard, PIETRA) e dei tappeti (Tabriz, Azlah, tibetani in lana e seta, Gabbeh);
- `_prova/crawl/100-piuma-cosa-intendi-piuma-piumino-e-piumetta.html`, `_prova/crawl/piumini-classi-en-12934.html` e `_prova/crawl/formato-tappeto-poshti-zaronim-ghali.html` (con `_prova/crawl/blog.html`): titoli, date (29 ottobre 2025, 13 maggio 2020, 9 giugno 2020) e le frasi tra virgolette dei tre articoli.

