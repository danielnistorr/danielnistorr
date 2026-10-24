# De Checchi Luciano: proposta di nuova home

Proposta non richiesta: c'è solo la homepage. Non è pubblicata e l'azienda non è stata contattata. Fatti e fonti sono in `01-analisi.md`; idea, caratteri, colori, gesto e controlli sono in `screenshot/home/NOTA.md`.

## File

- `sito/index.html`: la home, statica, si apre anche come file:///.
- `sito/img/`: solo le immagini usate, in WebP in più larghezze, più il logo SVG.
- `sito/fonts/`: SUSE woff2 latin e la sua licenza OFL.
- `screenshot/home/`:
  - `home-1440.jpg`, `home-1440-prima-schermata.jpg`;
  - `home-390.jpg`, `home-390-prima-schermata.jpg`;
  - `chiusura-1440.jpg`;
  - `NOTA.md`.
- `_prova/script/build_finale.sh` rifà tutto. Gli script che chiama:
  - `finale_maschera.py`: maschera del profilo d'apertura (con le due scanalature ripulite);
  - `finale_img.py`: immagini (il taglio d'apertura 1040x826 e il foglio 2400x1100 per i desktop);
  - `finale_quote.py`: la quota 82 mm e 13 mm in coordinate del taglio, con frecce ed etichette in tre misure;
  - `finale_pagina.py`: scrive la pagina dal modello `finale_index.tpl.html`;
  - `finale_gesto.mjs`: prova del selettore e della fisarmonica;
  - `finale_controlli.mjs` (a parte): scorrimento orizzontale da 320 a 2560, quota visibile, caratteri di Menu e campo email, menu mobile, collegamenti;
  - `finale_scatti.mjs` e `finale_jpeg.py`: screenshot JPEG 85, i PNG temporanei vengono cancellati.
- I prototipi giudicati sono in `_prova/home/a` (scelto) e `_prova/home/b`.

## Pagine del sito nuovo linkate dalla home

Le pagine linkate da menu, indice e piede non esistono ancora e vanno fatte:
- `azienda.html` (storia dal 1957);
- `lavorazioni.html` (tecnologia, verniciatura, hot coating, stampa 3D-DEC);
- `cataloghi.html`, `notizie.html` (notizie e fiere), `contatti.html` (come arrivare);
- `privacy.html`, `cookie.html`;
- `en/` (versione inglese);
- otto pagine prodotto in `prodotti/`: `legno.html` (Essenza, Rivestwood, Trattline), `carte-e-monostrati.html` (Promonwood, Promonwood Plus, Cemento 45, Prolamin), `laccati.html` (Pregio, Modern Plus, Laccati), `3d-dec.html` (HDF-3D-DEC, PVC 3D-DEC), `alluminio.html` (Allurivest, Allurivest-K, Duallwood), `woodled24.html` (Woodled24, Battiscopa porta LED), `wall-dec.html`, `accessori.html` (Isolwood, Decoquick, dl-FixClip, DL45, Terdech).

Link esterni: unydeco.it, il canale YouTube, Google Maps per le due sedi. Il bottone "Richiedi il catalogo" apre una email a info@ con l'oggetto già scritto.

## Newsletter

C'è, perché ha senso:
- pubblicano notizie dal 2010;
- vanno a 3-4 fiere l'anno;
- il catalogo di oltre 350 pagine si chiede per email;
- escono prodotti nuovi ogni anno.

Il modulo "Novità, fiere e catalogo" (email, Iscriviti, consenso privacy) oggi controlla solo i campi e non iscrive nessuno. Va collegato a un servizio di invio (per esempio Brevo, MailerLite o Mailchimp) con doppio consenso: email di conferma prima dell'iscrizione, registro dei consensi e link di disiscrizione in ogni invio. Va aggiornata anche l'informativa privacy.

## Dati da confermare

- **Le sei sagome disegnate (Q, QC, I, BC, S, B) sono indicative**, tracciate a mano su 82×13 mm. Servono i profili veri (DXF o PDF del catalogo) di ogni sagoma e le misure di ogni linea.
- **La foto d'apertura**:
  - quale linea è (la faccia sembra un tranciato o un decoro su supporto chiaro);
  - se il profilo è davvero un 82×13: la quota in pagina lo fa intendere, e la linea del pavimento è disegnata sul fondo della foto, dove il taglio esce dall'inquadratura;
  - se è una foto o un render (l'inventario la dava come possibile render);
  - chi l'ha scattata e se esiste l'originale ad alta risoluzione.
- **L'anno**: in pagina non c'è il 1957. La notizia del "65° anniversario" del 2018 porterebbe al 1953. Il 1988 e l'82×13 vengono da `storia-de-checchi`.
- **Clienti**: "per chi vende, posa e sceglie pavimenti" riassume distributori, posatori e utenti finali (il sito dice "come distributore o utente finale"). Vendono davvero anche ai privati, o il privato passa sempre dal rivenditore?
- **Recapiti**:
  - email da usare: in pagina c'è info@dechecchiluciano.com, i depliant usano amministrazione@;
  - orari di uffici e magazzino: non pubblicati, quindi assenti;
  - il fax 049 87 90 513 è ancora in uso? In pagina è piccolo e si può togliere.
- **Dati societari**:
  - capitale sociale 100.000 euro: è interamente versato?
  - la PEC viene da aziende.it, non dal sito;
  - il REA PD-308399 viene da aziende.it.
- **Social**: in pagina c'è solo YouTube. L'icona Facebook del sito porta alla pagina di Cliplist (Unydeco). LinkedIn compare nelle ricerche ma non è verificato. Instagram non c'è.
- **De Checchi o Unydeco**: quali linee sono di De Checchi e quali di Unydeco (Cliplist, Unycer; Duallwood e Allurivest sono in alluminio)? Come presentare le due aziende?
- **Date**: la riga delle quattro date è stata tolta (portava le fiere 2025 in una pagina dell'ottobre 2026). Il premio Amici della Zip 2010 è nella riga Woodled24 dell'indice. Per il sito vero servono le fiere 2026 con padiglione e stand, per la pagina Notizie e fiere e per la newsletter. Il titolo del Corriere del Veneto del 2011 ("25 km di battiscopa al giorno") non è più in pagina: servirebbe il dato di oggi.
- **Fuori pagina, da chiedere prima di usarli**: ISO 9001 (citata solo da terzi), dipendenti, metri quadri, paesi serviti oggi, deposito di Kiev e dlprofiles.eu, brevetto Woodled e dominio woodled.com in vendita.

## Foto da rifare dal vero

Il materiale del sito è piccolo (le foto vere più forti sono di 900 px) e in parte di render. Per il sito vero servono una giornata di still life e mezza giornata in reparto.
Densità delle foto di oggi nella proposta: apertura 1,61 a 1440 con DPR 2; Trattline circa 1,0 a 1440 con DPR 1; reparto (830 px) e Woodled24 (900 px) reggono a DPR 1 fino a 1440, a 1920 il reparto è appena ingrandito (circa 900 px CSS). Su schermi retina restano morbide: per questo servono gli scatti nuovi.

1. **Apertura**:
   - soggetto: la testa di un Rivestwood-BC 82×13 in rovere, appena tagliato;
   - su carta o cartoncino caldo senza giunte, luce di finestra da destra con un pannello bianco a sinistra;
   - macchina in diagonale a circa 30 gradi, fuoco su tutto il taglio (diaframma chiuso o più scatti uniti), almeno 6000 px di lato lungo;
   - lasciare spazio vuoto a sinistra per il titolo, e far appoggiare il piede del taglio sul bordo basso dell'inquadratura (lì la pagina disegna la linea del pavimento).
2. **Le sei sagome**: le sei teste in fila viste di fronte, stessa luce, una per scatto, per sostituire i disegni o affiancarli.
3. **Campioni**: i campioni Trattline dall'alto su fondo chiaro, luce diffusa, 6000 px; sostituiscono la slide di oggi, che ha il fondo in pietra scura.
4. **Reparto e magazzino**:
   - reparti di via Lombardia con luce naturale o luci di reparto uniformi, senza lampade colorate in campo;
   - il magazzino di via Irpinia con gli scaffali di profili visti di testa;
   - 4000 px almeno, cavalletto.
5. **Woodled24**: un corridoio vero al buio con la striscia accesa, dal cavalletto, esposizioni a forcella, almeno 4000 px, e lo stesso scatto a luce spenta.

## Licenze

- **Carattere**: SUSE, Google Fonts, SIL Open Font License 1.1, uso commerciale libero. Il file e la licenza sono in `sito/fonts/`.
- **Foto**: tutte di De Checchi Luciano, dal loro sito (elenco in `assets/CREDITI.md`, voce "Home finale"). Chi le ha scattate e i diritti di riuso sono da confermare con l'azienda. Le foto Unsplash e Pexels scaricate per i prototipi (`assets/esterne/`) non sono usate nella home finale.
- **Nessuna immagine generata dall'IA.**

## Logo

`sito/img/logo-dechecchi.svg` è ricostruito senza ridisegnare dai tracciati del depliant Woodled24 (PDF del 2020, p. 4), con i colori del PNG del sito (#1D1D1B, #E84E0E, #F39200). Manca la riga "SKIRTING AND PROFILES" del logo del sito. Va chiesto il vettoriale ufficiale, con un eventuale manuale dei colori.

## Note sui segnali

`segnali.sh` dà 0 soglie bloccanti e una riga da guardare, "titolo a sinistra e paragrafo a destra". Lo strumento conta le colonne del piede; l'unica sezione vera è "Due stabilimenti", dove titolo e testo stanno nella stessa colonna accanto alla foto.
