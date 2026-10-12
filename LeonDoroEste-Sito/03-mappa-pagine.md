# 03. Mappa delle pagine

Il sito attuale ha otto pagine italiane, sette inglesi e un'informativa (01, "Pagine esistenti"). Il nuovo sito tiene quello che il
cliente usa davvero e lo porta in sette pagine, una per ogni motivo per cui si arriva al Leon d'Oro: dormire, mangiare, andare in
bici sui Colli, assistere un ricoverato a Schiavonia, trovare la porta, prenotare. Specifica completa per sezione in
`_prova/spec.md`.

| Sito attuale | Nuovo sito | Slug | Perché |
|---|---|---|---|
| Home page | **Home** | `/` | la home approvata dal committente: la facciata, la targa, la sala, la cartolina, i Colli, le camere |
| Albergo e camere | **Camere** | `/camere/` | camere, listino 2026, servizi; il listino è il dato per cui si sceglie |
| Ristorante e cucina | **Ristorante** | `/ristorante/` | il menù di ogni giorno e quello del venerdì, scritti per intero (oggi sono chiusi in una scatola che ne nasconde il 76 %) |
| Bike Hotel Colli Euganei | **Bike hotel** | `/bike-hotel/` | garage, ciclovia E2, Transeuganea, Team Este Bike |
| Albergo per ospedale unico | **Per l'ospedale** | `/ospedale-schiavonia/` | nessun concorrente ne parla; la pagina attuale è ferma al 2022 ("nuovo polo ospedaliero") |
| Cosa visitare e Dove Siamo | **Dove siamo** | `/dove-siamo/` | indirizzo, come arrivare e cosa c'è intorno in una pagina sola; niente mappa incorporata senza consenso |
| Prenotazioni camere | **Prenota** | `/prenota/` | oggi c'è solo "scrivete una email": diventa un modulo con date, persone, trattamento e garage |
| Informativa Privacy e Cookie | **Privacy**, **Cookie** | `/privacy/`, `/cookie/` | testi del consulente del cliente; la vecchia informativa è un modello da negozio online |
| Versione inglese (7 pagine) | rimandi alle pagine italiane | | finché la famiglia non decide la versione inglese (Polylang gratuito) |

Più due blocchi comuni, globali con il plugin gratuito Ultimate Addons for Elementor: **Header** bianco (logo verde col leone, menu
in minuscolo, telefono, bottone verde "Prenota"; sotto 820 px logo, "Chiama" e "Menu") e **Footer** verde (ragione sociale,
indirizzo, chiusura del ristorante, telefono, fax, email, P.IVA, REA, CIN, link a Privacy, Cookie, Facebook, Instagram).

Ogni pagina si apre con una foto sola e un titolo maiuscolo di due o tre parole, e si chiude sul campo giallo della facciata con
il telefono e l'email.

## Sezioni per pagina

### Home
1. **Resta a cena**: la facciata di sera a tutta larghezza, col nome dipinto e l'insegna del leone, e il titolo a 144 px.
2. **La targa**: la targa in ceramica ALBERGO al centro, sola, e una frase: dove siamo e cosa si trova.
3. **Cucina veneta**: la sala con le travi a filo sinistro, il dettaglio della tavola, i quattro piatti, il pesce del venerdì, la
   chiusura della domenica, il link al menù.
4. **Con alloggio**: la cartolina della Trattoria al Leon d'Oro in bianco e nero a tutta larghezza, la storia in tre righe.
5. **Sui Colli Euganei**: la strada bianca con le due maglie gialle, il garage, l'anello di 70 km, il Team Este Bike, il link al
   bike hotel.
6. **Tredici camere** (campo giallo): i prezzi del 2026 in una frase, chi va all'ospedale, email e telefono; la camera.

### Camere
1. **Camera e colazione**: il titolo, una frase, la camera con le travi a filo destro.
2. **Listino 2026**: quattro righe, come una carta (l'unica tabella del sito).
3. **In albergo**: servizi in camera, parcheggio e garage, consigli al banco; il salottino con le poltrone verdi.
4. **Prenota una camera** (campo giallo): cosa scrivere, email, telefono, link al modulo; il banco della reception.

### Ristorante
1. **Senza rivisitazioni**: titolo e frase centrati.
2. La padella sul fuoco a tutta larghezza.
3. **Ogni giorno** (`#menu`): il menù tipo in tre colonne (antipasti, primi, secondi), i contorni, chi cucina.
4. **Il venerdì, pesce** (`#pesce`): il menù di pesce accanto alla sala col vino.
5. **Prenota un tavolo** (campo giallo): chiusura della domenica, il venerdì, telefono; la cantinetta.

### Bike hotel
1. **Bike hotel**: la strada fra le vigne dal drone a tutta larghezza, il titolo e una frase sotto.
2. **La maglia** gialla e nera col nome Leon d'Oro, al centro, con la frase sul Team Este Bike.
3. **Da Este**: ciclovia E2, Transeuganea, ritrovo in piazza, consigli al banco.
4. **Una camera e il garage** (campo giallo): prezzi, garage, email, telefono; le due mountain bike.

### Per l'ospedale
1. **Per l'ospedale**: l'ospedale di Schiavonia, nome e data, una camera per chi assiste un ricoverato.
2. **Come arrivare**: in navetta, in taxi, il centralino.
3. **Una camera vicina** (campo giallo): prezzi, telefono, email; la reception di sera.

### Dove siamo
1. **Viale Fiume 20**: Este dall'alto con il titolo sul cielo.
2. **Come arrivare** (`#come-arrivare`): dove siamo, parcheggio, navetta, indirizzo, link a Google Maps.
3. **Intorno** (`#cosa-vedere`): a Este, sui Colli, in giornata.
4. **Alla porta col leone** (campo giallo): come riconoscere la porta, indirizzo, chiusura, telefono, email; la porta di sera.

### Prenota
1. **Prenota**: la targa con la chiave, il titolo, una frase.
2. **Scriveteci** (campo giallo, `#richiesta`): telefono, email, fax e il modulo **Richiesta camera** (Contact Form 7: nome e
   cognome, email, telefono, arrivo, partenza, adulti, bambini, camera, trattamento, garage per la bici, note, consenso privacy).
   Nel fallback HTML, al posto del modulo, un bottone che apre un'email già impostata.
3. **Un tavolo**: per il ristorante basta una telefonata.

## Navigazione

Menu: camere, ristorante, bike hotel, per l'ospedale, dove siamo (menu WordPress "Menu principale", widget Navigation Menu di
Ultimate Addons), in minuscolo, voce attiva in verde sottolineata; a destra il telefono e il bottone "Prenota" verso `/prenota/`.
Sotto 820 px il menu si chiude nel bottone "Menu" e apre un pannello bianco a tutta larghezza con le cinque voci, il telefono e
"Prenota"; in testata restano il logo e "Chiama".

Dalla home alle pagine: "Il menù" porta a `/ristorante/#menu`, "Il bike hotel" a `/bike-hotel/`, "le indicazioni per arrivarci" a
`/ospedale-schiavonia/`. I vecchi indirizzi `.html` e le pagine inglesi arrivano alle nuove con redirect 301
(`plugin/redirect-301.csv`, specifica paragrafo 14).
