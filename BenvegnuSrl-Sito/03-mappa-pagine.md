# 03. Mappa delle pagine

La mappa del brief (home, chi siamo, team, prototipi/moto, news, sponsor, contatti) era pensata per un team studentesco. Per un grossista con banco è adattata così:

| Brief (impianto PMF) | Benvegnù | Slug | Perché |
|---|---|---|---|
| Home | **Home** | `/` | |
| Chi siamo | **Azienda** | `/azienda/` | storia, tabella "Dal 1980", distretto, per chi lavoriamo |
| Team | dentro **Azienda** ("Per chi lavoriamo") | | non ci sono persone pubbliche né foto del personale; i ritratti del banco si aggiungono solo con consenso (brief fotografico in LEGGIMI) |
| Prototipi/moto | **Catalogo** e **Vibram** | `/catalogo/`, `/vibram/` | il "prodotto" di Benvegnù sono le 10 famiglie del catalogo; Vibram (329 articoli) è il differenziale e merita una pagina |
| Sponsor | **Marchi** | `/marchi/` | i marchi rivenduti, cosa si trova di ciascuno |
| News | **Novità** | `/novita/` | avvisi datati (chiusure, nuovi arrivi), con gli articoli del blog WordPress |
| Contatti | **Contatti** | `/contatti/` | banco, orari, mappa, richiesta di disponibilità |

Più due blocchi comuni, globali con il plugin gratuito Ultimate Addons for Elementor: **Header** (barra nera con orari, telefono ed email; testata bianca con logo, menu, "Chiedi disponibilità" su desktop e "Chiama" su tablet e telefono) e **Footer** nero (indirizzo, contatti, pagine, dati societari).

## Sezioni per pagina

### Home
1. **Apertura divisa** (Mastrotto, Santoni): pannello nero con "Forniture per calzaturifici, pelletterie e calzolai", una riga su cosa si vende e dove, pulsanti "Sfoglia il catalogo" e "Come arrivare"; a destra la sede in bianco e nero a tutta altezza.
2. **Il catalogo** (blocchi foto come navigazione, 2x2): Vibram, Utensili, Tomaia e modelleria, Cura esposizione e imballo, con conteggio, famiglie e "Vedi →" sopra la foto.
3. **Dal catalogo, striscia scorrevole** (Valextra, Edward Green): una fila di 12 articoli reali tra filetti neri, aperta da una cella nera "Col codice facciamo prima"; parte allineata alla griglia e sborda a destra. Si scorre col dito, col trackpad o con le due frecce; una barra rossa sottile mostra il punto. Ogni scheda: foto a colori, famiglia, nome, un dettaglio verificato sul catalogo (varianti, misure, codice dove esiste).
4. **Vibram al banco** (Edward Green, Gruppo Mastrotto): fascia nera, la foto dell'espositore esce 40 px sopra e sotto la fascia; un solo numero grande (329), "Articoli Vibram al banco", tre righe a puntini Suole 177, Lastre 94, Mezzesuole e tacchi 58, pulsante alla pagina Vibram.
5. **Per chi lavoriamo** (Lampo): "Molti dei nostri clienti producono per i marchi del lusso", chi sono i clienti, e accanto "I marchi al banco" in una griglia 2x2 con filetti interni (Vibram, Gütermann, Girba, Fratelli Zucchini), ogni marchio porta alla sua famiglia.
6. **Vieni al banco** (Mastrotto, Ernest Wright): il titolo grande si appoggia sul cielo della facciata; sotto, quattro colonne con filetto: indirizzo e Google Maps, orari, telefono, email e condizioni di vendita. È l'unico punto della home con tutti i recapiti.

Rispetto alla versione precedente: "Come si lavora con noi" passa nella pagina Contatti; le liste con i numeri rossi sono sparite dalla home; indirizzo, orari e telefono non si ripetono più in tre blocchi.

### Azienda
1. Apertura "Dal 1980 a Vigonovo" con il testo istituzionale ripulito e la foto della sede a tutta larghezza.
2. Cosa vendiamo: le 15 famiglie dichiarate dall'azienda, anche quelle non online.
3. **Le date** (pattern risultati): 1980 inizio attività, 1990 nasce la S.r.l., 2014 catalogo online, 2026 nuovo sito.
4. Nel distretto della Riviera del Brenta (fondo nero, foto del magazzino): fatti con fonte (oltre 500 imprese, circa 20 milioni di paia l'anno).
5. Per chi lavoriamo: calzaturifici, pelletterie, calzolai, stilisti e modellisti, negozi di calzature.
6. Condizioni di vendita (PDF).
7. Vieni al banco.

### Catalogo
1. Apertura con indice a salti delle 10 famiglie.
2. **Indice numerato delle 10 famiglie**: numero, foto prodotto, nome, sottocategorie con i conteggi, 3 articoli reali con codice, numero di articoli, "Chiedi disponibilità" (email già impostata con la famiglia nell'oggetto). Ogni famiglia ha un'ancora (`/catalogo/#utensili` ecc.) usata dai blocchi della Home.
3. Al banco c'è anche quello che non è online: lacci, cerniere, chiodi, occhielli, rinforzi, adesivi Fratelli Zucchini...
4. Vieni al banco.

### Vibram
1. Apertura divisa nero + foto del banco: rivenditore autorizzato, 329 articoli, "Chiedi disponibilità" (email con modello, misura, colore, quantità) e "Chiama".
2. Suole: 6 modelli reali con foto (2600 Liverpool, 0056C Winter City, 2603 Gumblock, 2609 Athena Gumlite, 4303 Betulla tranciata, V.0121P Fourà PU).
3. Lastre: 7106 Crepe, 7107 Crepe cardata, 7130 New Boulder.
4. Mezzesuole e tacchi: 2023 Wellness, 2025 Sebastian, 1100T Montagna.
5. Per chi produce / per chi ripara.
6. "Chiedi un modello Vibram" (blocco visita su fondo grigio chiaro).

### Marchi
1. Apertura.
2. 4 schede marchio: logo su riquadro grigio, numero, cosa si trova, numero di articoli dove c'è, link alla famiglia nel catalogo e al sito ufficiale.
3. Altri marchi presenti negli articoli (Olfa, Mozart, Lariz, Kai, Wiss, C.Dick, Norton, 3M...).
4. Vieni al banco.

### Novità
1. Apertura.
2. Avviso fisso: orari del banco, dove si pubblicano le chiusure.
3. Ultime novità: widget gratuito "Articoli recenti" (in Elementor) che mostra gli articoli del blog; nel fallback HTML un elenco statico.
4. Vieni al banco.

### Contatti
1. Apertura.
2. Dati (indirizzo, orari, telefono, fax, email, PEC, parcheggio) e mappa Google in grigio; accanto il modulo **Richiesta di disponibilità** (Contact Form 7: nome, azienda, email, telefono, articolo, colore e misura, quantità, ritiro o spedizione, note, consenso privacy). Nel fallback HTML, al posto del modulo, un pulsante che apre un'email già impostata.
3. **Come si lavora con noi** (processo in fasi): quattro colonne con filetto, Fase 1-4, testo sempre visibile, nessuna icona e nessun numero rosso.
4. Dati societari e condizioni di vendita.

## Navigazione

Menu: Catalogo, Vibram, Marchi, Azienda, Novità, Contatti (menu WordPress "Menu principale", widget Navigation Menu di Ultimate Addons). Su tablet e telefono diventa un menu a scomparsa a tutta larghezza; accanto restano "Chiama" e, nella barra in alto, il telefono.
