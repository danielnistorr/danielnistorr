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

Più due blocchi comuni: **Header** (barra orari e telefono, logo, menu, pulsante "Chiama") e **Footer** (indirizzo, contatti, pagine, dati societari).

## Sezioni per pagina

### Home
1. **Apertura**: "Forniture per calzaturifici, pelletterie e calzolai", una riga su cosa si vende e dove, pulsanti "Sfoglia il catalogo" e "Come arrivare"; a destra l'esterno della sede in bianco e nero.
2. **Il catalogo** (blocchi foto come navigazione): 01 Vibram, 02 Utensili, 03 Tomaia e modelleria, 04 Cura, esposizione e imballo, ciascuno con famiglie e numero di articoli.
3. **Vibram al banco** (fondo nero): suole, lastre, mezzesuole e tacchi con i conteggi, pulsante alla pagina Vibram.
4. **Come si lavora con noi** (processo in fasi): 4 passi numerati.
5. **I marchi**: Vibram, Gütermann, Girba, Fratelli Zucchini con la famiglia di prodotto.
6. **Vieni al banco** (unico blocco rosso): indirizzo, orari, parcheggio, telefono grande, email, Google Maps.

### Azienda
1. Apertura "Dal 1980 a Vigonovo" con il testo istituzionale ripulito e la foto della sede a tutta larghezza.
2. Cosa vendiamo: le 15 famiglie dichiarate dall'azienda, anche quelle non online.
3. **Dal 1980** (pattern risultati): 1980 inizio attività, 1990 nasce la S.r.l., 2014 catalogo online, 2026 nuovo sito.
4. Nel distretto della Riviera del Brenta: fatti con fonte (oltre 500 imprese, circa 20 milioni di paia l'anno).
5. Per chi lavoriamo: calzaturifici, pelletterie, calzolai, stilisti e modellisti, negozi di calzature.
6. Condizioni di vendita (PDF).
7. Vieni al banco.

### Catalogo
1. Apertura con indice a salti delle 10 famiglie.
2. **Indice numerato delle 10 famiglie**: numero, foto prodotto, nome, sottocategorie con i conteggi, 3 articoli reali con codice, numero di articoli, "Chiedi disponibilità" (email già impostata con la famiglia nell'oggetto). Ogni famiglia ha un'ancora (`/catalogo/#utensili` ecc.) usata dai blocchi della Home.
3. Al banco c'è anche quello che non è online: lacci, cerniere, chiodi, occhielli, rinforzi, adesivi Fratelli Zucchini...
4. Vieni al banco.

### Vibram
1. Apertura su fondo nero: rivenditore autorizzato, 329 articoli, "Chiedi disponibilità" (email con modello, misura, colore, quantità) e "Chiama".
2. Suole: 6 modelli reali con foto (2600 Liverpool, 0056C Winter City, 2603 Gumblock, 2609 Athena Gumlite, 4303 Betulla tranciata, V.0121P Fourà PU).
3. Lastre: 7106 Crepe, 7107 Crepe cardata, 7130 New Boulder.
4. Mezzesuole e tacchi: 2023 Wellness, 2025 Sebastian, 1100T Montagna.
5. Per chi produce / per chi ripara.
6. Blocco rosso "Chiedi un modello Vibram".

### Marchi
1. Apertura.
2. 4 schede marchio: logo, cosa si trova, numero di articoli dove c'è, link alla famiglia nel catalogo e al sito ufficiale.
3. Altri marchi presenti negli articoli (Olfa, Mozart, Lariz, Kai, Wiss, C.Dick, Norton, 3M...).
4. Vieni al banco.

### Novità
1. Apertura.
2. Avviso fisso: orari del banco, dove si pubblicano le chiusure.
3. Ultime novità: widget gratuito "Articoli recenti" (in Elementor) che mostra gli articoli del blog; nel fallback HTML un elenco statico.
4. Vieni al banco.

### Contatti
1. Apertura.
2. Dati (indirizzo, orari, telefono, fax, email, PEC, parcheggio) e mappa Google.
3. Richiesta di disponibilità (blocco rosso): il pulsante apre un'email già impostata con le voci che servono.
4. Dati societari e condizioni di vendita.

## Navigazione

Menu: Catalogo, Vibram, Marchi, Azienda, Novità, Contatti. Su telefono le voci vanno su due righe sotto il logo (niente menu a scomparsa, che nella versione gratuita di Elementor non c'è); il telefono resta nella barra in alto.
