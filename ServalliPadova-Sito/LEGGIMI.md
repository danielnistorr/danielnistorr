# Servalli Padova: proposta di nuova homepage

Proposta non richiesta di una nuova home per Servalli Padova sas (servalli.net), solo la home. Non è stata contattata l'azienda né pubblicato nulla.

- Pagina: `sito/index.html`, con immagini in `sito/img/` e caratteri in `sito/fonts/`. Si apre con il browser come file locale.
- Screenshot e nota del progetto: `screenshot/home/` (`NOTA.md` spiega idea, caratteri, colori, interazione, foto e controlli).
- Rigenerare tutto: `bash _prova/script/build_finale.sh` (immagini, pagina, caratteri, screenshot).
- Analisi con le fonti: `01-analisi.md`. Prototipi: `_prova/home/a` e `_prova/home/b` (scelto B).

## Dati da confermare con l'azienda

- **Titolo**. In pagina c'è "Tessile casa dal 1895", la riga del loro logo. In alternativa si può usare "Quattro secoli di tessile", il loro slogan ("da quattro secoli", "quattrocento anni"), solo se lo confermano: il Seicento è un racconto di famiglia (il paramento di Gandino), mentre l'azienda nasce nel 1895.
- **Firma 1895 o "fine del 1800"** (testo di `storia`). Le frasi sul Lanificio Testa e sul Seicento "tra Venezia e Bergamo" restano racconto dell'azienda, citato tra virgolette.
- **Foto dei telai**: che sia del 1910 (l'anno viene solo dall'alt del sito). Che la Giardiniera sia davanti al negozio di Padova (il nome del file dice 1967).
- **Serline**: che cos'è, perché non è tra i marchi registrati (Servalli, Alans, Colorcasa). Va chiarito anche quanto producono e quanto importano o distribuiscono.
- **Ragione sociale nel piede**: in pagina c'è "Servalli Padova sas di Servalli Francesco e Alessandro" (VIES: "SERVALLI PADOVA - S.A.S. DI SERVALLI FRANCESCO E ALESSANDRO"). Chi sono oggi i soci e se sono la quarta generazione.
- **REA e PEC**: non trovati, da aggiungere alla riga legale.
- **Condizioni riservate**: la pagina dice "Rivenditori, grossisti e alberghi hanno condizioni riservate" (testo di Partners). La GDO compare solo per gli articoli personalizzati: da confermare se va citata.
- **Consegna in tutta Italia**: se vale anche per gli ordini online dei privati (oggi lo dice la pagina `informazioni` in generale).
- **Showroom**: se quello di Via Portogallo riceve anche i privati.
- **BENVE10 e spedizione gratuita sopra i 150 euro**: non sono in home. Se restano validi possono andare nel negozio.
- **Newsletter**: il servizio di invio, la base giuridica del consenso e i testi di Privacy e Cookie.
- **Social**: se ne hanno uno vero. Oggi le icone puntano alle home generiche di Facebook, Instagram, Pinterest e Twitter, quindi nel piede non c'è una colonna Seguici.

## Newsletter (da collegare)

Nel piede ci sono il campo email, il bottone "Iscriviti" e la casella del consenso (obbligatoria). **Non funziona finché non si collega a un servizio di invio** da scegliere con loro, per esempio Brevo, Mailchimp o MailerLite, con doppia conferma dell'iscrizione. Oggi il modulo controlla email e consenso e mostra solo il messaggio "la newsletter non è ancora attiva in questa proposta". Il testo dice solo "Offerte e nuovi prodotti del negozio online", senza promettere una frequenza.

## Pagine a cui puntano i link del piede

Il sito nuovo avrà queste pagine. Nella proposta i link sono percorsi relativi, perché le pagine non esistono ancora; i link della testata portano alle sezioni della home.

- Azienda: Storia (`storia/`), Riconoscimenti (`riconoscimenti/`), Marchi (`marchi/`: Servalli, Alans, Colorcasa), Arte tessile (`arte-tessile/`, gli 8 articoli di oggi).
- Prodotti, le 6 categorie del negozio:
  - Lenzuola e copripiumini (`negozio/lenzuola-e-copripiumini/`);
  - Piumini e trapunte (`negozio/piumini-e-trapunte/`);
  - Bagno (`negozio/bagno/`);
  - Tappeti (`negozio/tappeti/`);
  - Articoli da bambino (`negozio/bambino/`);
  - Mare (`negozio/mare/`).
- Servizi: Alberghi e contract (`alberghi-e-contract/`, oggi Forniture alberghiere), Rivenditori e grossisti (`rivenditori/`, oggi Partners), Negozio online (`negozio/`), Contatti (`contatti/`).
- Legali: Privacy (`privacy/`), Cookie (`cookie/`), Condizioni di vendita (`condizioni-di-vendita/`).
- Da togliere dal sito di oggi: le tre pagine orfane del modello (`living-room`, `Bedroom-Camera`, `copia-di-camera-da-letto`).

## Foto da rifare dal vero

Le tre foto esterne sono segnaposto e vanno sostituite prima di qualsiasi uso pubblico. Serve mezza giornata di still life in magazzino, su un fondo neutro caldo (carta o lino écru), con luce di finestra o un softbox grande da un lato, senza flash diretto. Scatti in RAW ad almeno 3000 px sul lato lungo.

1. **Il Tabriz o un altro tappeto loro, dall'alto** (sostituisce la foto del negozio nella prima schermata):
   - tappeto steso a terra, macchina in bolla sulla verticale (scala o braccio), obiettivo 35-50 mm, tutto il tappeto con le frange e un margine di fondo;
   - luce radente da un lato, perché si veda il vello;
   - più un dettaglio del retro con i nodi e uno del frangiato.
2. **Le lenzuola loro, bianche, piegate in pila** (sostituisce Pinales): tre o quattro pezzi piegati con cura, vista frontale leggermente dall'alto, bianco tenuto senza bruciare le luci.
3. **La spugna con un logo ricamato da loro** (sostituisce Araujo): due o tre asciugamani d'albergo piegati, con il ricamo in primo piano, messo a fuoco e in luce radente.
4. **Tre o quattro tappeti piegati in pila nello showroom** (sostituisce Moradian nella chiusura): vista di taglio, i bordi a vista, fondo pulito.
5. **Archivio**: le scansioni ad alta risoluzione (600 dpi) delle stampe originali di telai, MADIVAL, Giardiniera 1967 (oggi solo 1024 px), Persia e Tehran 1994, più il tappeto con la scritta SERVALLI annodata, oggi troppo piccolo.

## Licenze

- **Foto esterne** (dettagli e pagine delle foto in `assets/CREDITI.md`), licenze lette il 24/10/2026:
  - juan pinales, Pexels 31902663: licenza Pexels, uso commerciale libero, attribuzione non obbligatoria;
  - Antonio Araujo, Unsplash d0RbiJeEMQI: licenza Unsplash;
  - bahareh moradian, Unsplash NvdxYHt5CHM: licenza Unsplash.

  Nessuna immagine è generata dall'IA e nessuna è usata in altre home della campagna.
- **Tabriz** (`negozio/4126147316.jpg`): è un articolo loro (marchio Alans), ma la foto può essere del fornitore. **I diritti vanno chiariti**.
- **Foto d'archivio e di Persia**: della famiglia, firmate "© Franco Servalli". Va chiesto il **permesso** di usarle; la firma resta.
- **Caratteri**: Libre Caslon Display e Golos Text, da Google Fonts, SIL Open Font License 1.1, serviti dalla pagina in `sito/fonts/`.

## Loghi

- Usato: `assets/originali/logo-servalli-stemma.png` (1920 x 823), dal sito. Il bianco è reso trasparente con un "colore verso alfa" che lascia intatti i colori dello stemma, poi è esportato in WebP a 2x:
  - in testata stemma e SERVALLI, senza la sottoriga "TESSILE CASA DAL 1895", che a quella misura era illeggibile;
  - nel piede il logo intero.
- Non ricostruito in SVG: lo stemma è un disegno dorato a colori. Va chiesto il **logo vettoriale** e il valore esatto dell'oro.
- `logo-servalli-house.svg` (marchio del gruppo, ricalcato male) non è usato.
