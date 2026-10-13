# 03. Mappa delle pagine

Il sito attuale ha cinque voci (Home, L'Albergo, Camere e Listino, Servizi, Dove Siamo), la stessa struttura sotto `/en/` (in gran parte ancora in italiano o con il testo finto del template), due articoli del 2014 e una galleria di 28 schede "Foto 01... Foto 27". Il nuovo sito ha sei pagine, costruite su un'idea sola: **l'albergo mostrato un oggetto alla volta, grande sul bianco, con una frase che dice al cliente cosa ottiene** (la chiave, la casa, il letto, l'insegna accesa, il corridoio). Specifica completa in `_prova/spec.md`.

| Sito attuale | Nuovo sito | Slug | Perché |
|---|---|---|---|
| Home | **Home** | `/` | la home approvata dal committente (prototipo "l'oggetto") |
| L'Albergo | **L'albergo** | `/albergo/` | la casa, la facciata e l'atrio, e i servizi |
| Servizi | dentro **L'albergo** (`#servizi`) | | sei servizi senza foto proprie farebbero una pagina sottile di box; il vecchio URL porta alla sezione |
| Camere e Listino | **Camere e prezzi** | `/camere/` | la camera alla sua misura e il listino per tipo di camera, in righe |
| Dove Siamo | **Dove siamo** | `/dove-siamo/` | l'insegna accesa e le indicazioni dal casello, dalle stazioni, dagli aeroporti, per la Fiera |
| "book now" (motore Ericsoft spento) | **Prenota** | `/prenota/` | oggi dal sito non si può prenotare: una pagina con il modulo di richiesta e il telefono |
| `/en/...` | **English** | `/en/` | una pagina in inglese con i fatti delle pagine italiane; tiene vivi i vecchi URL inglesi |
| Articoli e offerte del 2014, galleria, archivi, feed | nessuna pagina | | contenuti fermi al 2014; reindirizzati (vedi sotto) |

Più due blocchi comuni, globali con il plugin gratuito Ultimate Addons for Elementor: **Header** (logo monocromo ardesia, menu in maiuscolo piccolo, telefono, bottone rosso "Prenota"; tendina "Menu" su tablet e telefono, con il telefono come prima voce) e **Footer** bianco (indirizzo, contatti, pagine, English, Privacy, Cookie; riga legale con A.L.P. S.r.l., P.IVA, REA, capitale sociale, PEC e CIN sotto l'unico filetto del sito).

## Sezioni per pagina

### Home
1. **La chiave**: "La tua chiave a Padova Est" a 104 px sopra i portachiavi in cuoio rosso con il monogramma GH, a tutta larghezza; sotto, una frase con indirizzo, casello, parcheggio e colazione, e telefono ed email a destra. A 390 la foto viene prima del titolo.
2. **Uscita Padova Est**: la facciata all'imbrunire con l'insegna accesa, a filo del bordo sinistro; accanto, il dettaglio dell'insegna in controluce, la strada dal casello, i 50 posti auto, le distanze dalla Fiera e dal Palasport, "Come arrivare".
3. **Dalla singola alla quadrupla**: la camera matrimoniale con la parete blu, a filo del bordo destro; accanto, i sei tipi di camera, cosa c'è in camera e cosa è compreso, "Camere e prezzi"; in basso il dettaglio del bagno.
4. **Prenoti senza carta di credito e paghi in hotel**: l'unico campo rosso, le lingue parlate, telefono ed email, "Scrivi una richiesta"; a destra le statue del corridoio sul rosso delle pareti.

### L'albergo
1. Apertura: "Via San Marco 63, Ponte di Brenta" e una frase su chi ci viene (turismo e lavoro, tra l'A4 e la Fiera).
2. **La striscia**: facciata di giorno e atrio con il lucernario, affiancati a tutta larghezza, senza margine.
3. **Colazione e parcheggio sono compresi** (`#servizi`): colazione a buffet, parcheggio privato gratuito, WiFi, in camera, senza barriere architettoniche, lingue; in una colonna, accanto ai fiori bianchi del 2019.
4. Banda rossa "Prenota".

### Camere e prezzi
1. Apertura: "Camere da una a quattro persone" e cosa è compreso nel prezzo.
2. **La camera alla sua misura**: la matrimoniale con la parete blu a 1024 px, a filo del bordo sinistro, e il bagno con la doccia.
3. **Prezzi a camera** (`#prezzi`): sei righe con nome, per quante persone e prezzo "da... a... euro", la nota su cosa è compreso, "Chiedi il prezzo per le tue date". Listino da confermare con il cliente.
4. Banda rossa "Prenota".

### Dove siamo
1. **Mezzo chilometro dal casello Padova Est**: la facciata di sera con l'insegna accesa a filo del bordo destro; accanto, indirizzo, telefono, email e il link al percorso su Google Maps (nessuna mappa incorporata prima del consenso).
2. **Indicazioni** in una colonna sull'asse della foto: in auto, in treno, in autobus, dagli aeroporti, Fiera e Palasport (`#fiera`).
3. Banda rossa "Prenota".

### Prenota
1. **Scrivici le date del soggiorno**: niente carta di credito, paghi in hotel; il telefono per chi preferisce chiamare; il modulo **Richiesta di prenotazione** (Contact Form 7: arrivo, partenza, persone, camere, tipo di camera, nome, email, telefono, ora di arrivo, note, consenso privacy); accanto il corridoio con le statue. Nel fallback HTML, al posto del modulo, un'email già impostata.

### English
1. **Your key at Padova Est** sopra i portachiavi.
2. **Padova Est exit**: la facciata di sera, come arrivare, parcheggio, distanze.
3. **From single to quadruple rooms**: la camera e le sei righe dei prezzi.
4. **Book without a credit card and pay at the hotel**: campo rosso, telefono, email, "Write to us".

## Navigazione

Menu (WordPress "Menu principale", widget Navigation Menu di Ultimate Addons): L'albergo, Camere e prezzi, Dove siamo, English. Nella testata, fuori dal menu: il telefono (nascosto tra 1025 e 1279 px perché il menu stia su una riga) e il bottone "Prenota" verso `/prenota/`. Voce attiva in rosso pompeiano e sottolineata. Su tablet e telefono il menu diventa una tendina a tutta larghezza; accanto restano "Prenota" e "Menu".

Privacy e Cookie stanno nel piede e portano a `/privacy/` e `/cookie/`, pagine con i testi del cliente (il sito attuale non ne ha).

## Vecchi URL

Redirect 301 (plugin Redirection, `plugin/redirect-301.csv`): `/camere-e-listino/` verso `/camere/`; `/servizi/` verso `/albergo/#servizi`; tutte le pagine `/en/...` verso `/en/`; l'offerta fiere del 2014 verso `/dove-siamo/#fiera`; l'articolo "HOTEL ***" verso `/camere/#prezzi`; archivi, categorie, autore e feed verso la home; galleria e 28 schede foto verso `/albergo/`. `/`, `/albergo/`, `/dove-siamo/` ed `/en/` restano uguali.
