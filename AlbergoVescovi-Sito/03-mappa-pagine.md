# 03. Mappa delle pagine

Il sito attuale ha 10 pagine (01): Home, Camere con tre sottopagine (Doppia, Tripla, Quadrupla), Ristorante, Centro benessere, Contatti e due pagine dei contributi pubblici. Il nuovo sito tiene le stesse voci, toglie `/index.php/` dagli indirizzi, porta le tre schede camera dentro una pagina sola (sono tre righe di dati, non tre pagine) e riunisce i due contributi in una pagina. La specifica completa, sezione per sezione, è in `_prova/spec.md`.

| Sito attuale | Nuovo sito | Slug | Perché |
|---|---|---|---|
| Home | **Home** | `/` | il prototipo approvato ("Sulla Piana Ave"), con le correzioni della specifica |
| Camere, Doppia, Tripla, Quadrupla | **Camere** | `/camere/` | tre tipi, ognuno con superficie, persone e una frase; ancore `#doppia`, `#tripla`, `#quadrupla` per i vecchi indirizzi; i servizi in camera in fondo |
| Ristorante | **Ristorante** | `/ristorante/` | oggi c'è solo il "Lorem ipsum": cucina tradizionale, le due sale, i piatti in foto |
| Centro benessere | **Centro benessere** | `/centro-benessere/` | orario e prezzo come titolo, il secchio tirolese, l'elenco di cosa c'è e come si prenota |
| Contatti | **Contatti** | `/contatti/` | il panorama della Piana con l'albergo in mezzo al prato, recapiti, richiesta di disponibilità, come arrivare |
| Progetto POR FESR, CSR 2023-2027 | **Contributi** | `/contributi/` | pubblicità dei due contributi, testi ripuliti, loghi; ancore `#csr-2023-2027` e `#por-fesr` |
| (nessuna) | Privacy, Cookie | `/privacy/`, `/cookie/` | pagine WordPress semplici col testo del cliente, non generate da `build.py` (nel LEGGIMI) |

Più due blocchi comuni, globali con Ultimate Addons for Elementor: **Header** bianco e fisso in alto (logo tondo, quattro voci in minuscolo, telefono, "Prenota" verso il motore Persefone) e **Footer** (fascia verde con telefono, email e indirizzo; sotto, su bianco, recapiti, voci, dati societari, CIN e loghi dei contributi). A telefono, una barra fissa in basso con "Chiama" e "Prenota".

## L'idea, pagina per pagina

La casa gialla in mezzo al prato della Piana Ave, a 900 metri dal centro di Asiago. La home si apre con "Sulla Piana Ave" scritto grande sull'erba davanti all'albergo e si chiude sullo stesso prato d'inverno; le pagine interne si chiudono tutte sul panorama della Piana, con l'albergo in mezzo al prato e il paese dietro; i Contatti si aprono su quel panorama.

## Sezioni per pagina

### Home (`/`)
1. **Apertura**: la casa sul prato d'estate fino in fondo alla finestra, "Sulla Piana Ave" a 164 px sull'erba, accanto una riga: l'edificio giallo in mezzo al prato, 900 metri dal centro.
2. **Riga delle date**: "Quando arrivate?", il bottone "Scegli le date" verso il motore Persefone, "oppure chiamate lo 0424 462614".
3. **Camere**: la camera in abete a tutta larghezza, sotto "Doppie, triple e quadruple, alcune col balcone sui prati" e il link alla pagina.
4. **Ristorante**: la tavola con i prati alla finestra a filo del bordo destro, accanto la cucina tradizionale in quattro piatti e il link.
5. **Centro benessere**: la sauna a filo del bordo sinistro, "Dalle 15 alle 19, sauna e bagno turco", il secchio tirolese, il prezzo.
6. **Inverno**: lo stesso prato sotto la neve, "D'inverno, lo stesso prato", l'apertura per stagioni.

### Camere (`/camere/`)
1. **Apertura**: titolo "Camere doppie, triple e quadruple", il balcone sulla Piana e la scelta fra mansarda e camera classica; sotto, il letto contro la parete in abete a tutta larghezza.
2. **Le tre camere**: Doppia, Tripla, Quadrupla con metri quadri, persone e una frase; accanto la camera con la parete in pietra a filo del bordo destro.
3. **Bagno e famiglie**: due foto affiancate a tutta larghezza (il bagno in pietra, la camera con il letto aggiunto), sotto due frasi.
4. **In camera e in albergo**: i servizi in righe brevi e la tabella di tre righe con superficie e persone.
5. **Riga delle date**.
6. **Chiusura comune**: "Sulla Piana Ave, a 900 metri dal centro" e il panorama.

### Ristorante (`/ristorante/`)
1. **Apertura**: la stube con la stufa a tutta larghezza subito sotto la testata, poi "Cucina tradizionale" e i piatti per nome.
2. **La sala grande**: le vetrate sui prati a filo del bordo sinistro, accanto due righe sulle due sale.
3. **A tavola**: due foto verticali affiancate (pasta, pane e vino dall'alto; la cantinetta dei vini), senza testo.
4. **Riga delle date**.
5. **Chiusura comune**.

### Centro benessere (`/centro-benessere/`)
1. **Apertura**: la sauna in verticale a filo del bordo sinistro; accanto "Dalle 15 alle 19, su prenotazione" e cosa c'è.
2. **Il secchio tirolese**: il dettaglio in bianco e nero e la frase sulla catenella.
3. **Cosa c'è e come funziona**: due elenchi brevi (le sette cose del centro benessere; orario, per chi, supplemento, prenotazione).
4. **Riga delle date**.
5. **Chiusura comune**.

### Contatti (`/contatti/`)
1. **Apertura**: "A 900 metri dal centro di Asiago", il panorama della Piana a tutta larghezza, la didascalia che dice dov'è l'albergo.
2. **Recapiti e richiesta**: telefono, email, fax, PEC, "Prenota online"; accanto il modulo "Richiesta di disponibilità" (Contact Form 7).
3. **Come arrivare**: la reception col banco in abete a filo del bordo sinistro; accanto indirizzo, garage e parcheggio, coordinate e il link a Google Maps (nessuna mappa incorporata).

### Contributi (`/contributi/`)
1. **Apertura**: titolo "Contributi pubblici".
2. **Complemento regionale per lo sviluppo rurale 2023-2027** (`#csr-2023-2027`): loghi e le sette voci del contributo.
3. **POR FESR 2014-2020, Altopiano Active Tours** (`#por-fesr`): banner, asse e azione, il progetto, i 12 partecipanti e i 7 obiettivi.
4. **Chiusura comune**.

## Navigazione

Menu: camere, ristorante, centro benessere, contatti (menu WordPress "Menu principale", widget Navigation Menu di Ultimate Addons), in minuscolo come nel prototipo approvato. Voce attiva in verde bosco con la sottolineatura. Da 1024 px in giù il menu passa all'icona a tre linee e si apre a tutta larghezza; a 1024 e a 768 restano a destra il telefono e "Prenota", sotto 768 restano il logo e l'icona, e "Chiama" e "Prenota" passano nella barra fissa in basso.

Piede: Camere, Ristorante, Centro benessere, Contatti, Contributi, Privacy, Cookie, Facebook (`facebook.com/AlbergoVescovi`, l'indirizzo del sito attuale).

Prenotazioni: ogni "Prenota" e "Scegli le date" porta direttamente a `https://www.booking-engine.it/Scripts/index.pl?hotel_id=53`, il motore Persefone che l'albergo usa oggi, senza passare dal vecchio indirizzo http di `phpbookinghotel.it`.

Vecchi indirizzi: tutti in `plugin/redirect-301.csv` (elenco completo nella specifica, paragrafo 13).
