# 03. Mappa delle pagine

Il sito attuale ha 82 pagine italiane: un menu alto (L'Azienda, Prodotti, Dove siamo, News, Contatti), un menu prodotti con tre famiglie e una pagina per ogni manufatto, per ogni modello di piattaforma e per ognuno dei 36 cantieri. Il nuovo sito raccoglie tutto in sette pagine. Ogni vecchia scheda diventa un'ancora dentro la pagina della sua famiglia, così nessun dato si perde e i vecchi indirizzi si reindirizzano uno per uno (`plugin/redirect-301.csv`).

| Sito attuale | Nuovo sito | Slug | Perché |
|---|---|---|---|
| Home (slider, nessun testo) | **Home** | `/` | le due linee di prodotto dette nel titolo, il catalogo in breve, la tavola delle piattaforme, i cantieri |
| Vasche prefabbricate monoblocco + 3 schede | **Vasche** | `/vasche/` | rettangolari, circolari e resinate stanno bene in una pagina sola: hanno le stesse misure |
| Depurazione + 7 schede | **Depurazione** | `/depurazione/` | sette schede con la loro tabella, in un indice numerato |
| Piattaforme per autolavaggi + 15 pagine (modelli, caratteristiche, posa, isola, personalizzazioni) | **Piattaforme per autolavaggi** | `/piattaforme-autolavaggi/` | è il prodotto che nessun concorrente vicino fa: la pagina più ricca |
| Realizzazioni + 36 pagine di galleria | **Realizzazioni** | `/realizzazioni/` | una mappa e 36 schede con foto e lightbox, un'ancora per cantiere |
| L'Azienda (testo distrutto), PDF | **Azienda** | `/azienda/` | testo ricostruito dalle versioni DE e FR, il calcestruzzo, le norme, i dati societari |
| Dove siamo + Contatti | **Contatti** | `/contatti/` | recapiti, modulo per l'ufficio tecnico, mappa di Legnaro e mappa di Google solo al clic |
| News (una voce vuota) | nessuna | | oggi c'è una sola notizia, senza data, che porta a una pagina vuota: si riapre se il cliente vuole tenerla aggiornata |
| Privacy, Cookie | Privacy, Cookie | `/privacy/`, `/cookie/` | pagine WordPress semplici con il testo del cliente |

Più due blocchi comuni, globali con il plugin gratuito Ultimate Addons for Elementor:
- **Testata** bianca, una riga sola: logo, menu, telefono in monospazio (sopra i 1280 px) e "Richiedi informazioni". Su tablet e telefono: logo, "Chiama" e hamburger.
- **Piede** grafite: logo chiaro, prodotti, azienda, recapiti, riga legale completa (ragione sociale, sede, P.IVA e C.F., Registro Imprese di Padova, REA, capitale sociale, link a Privacy e Cookie).

In fondo a ogni pagina tranne Contatti c'è il blocco **Ufficio tecnico**: "Portate più grandi o misure fuori tabella: chiedete all'ufficio tecnico", telefono, email e PEC, orari, sede. Viene dalla frase che il sito ripete in quasi tutte le schede: "PER PORTATE SUPERIORI CONTATTARE IL NOSTRO UFFICIO TECNICO".

Il segno comune a tutte le pagine è il **capo di sezione**: etichetta in monospazio, nota di servizio a destra e sotto un filetto con le stanghette di una quota, preso dai disegni quotati dell'azienda.

## Sezioni per pagina

### Home
1. **Apertura** (Jensen, Escofet): titolo su due righe, "Vasche e impianti per il trattamento delle acque. / Piattaforme prefabbricate per autolavaggi."; la vasca col logo dipinto appesa all'autogru (la foto più nitida del sito); accanto il testo e l'indice del catalogo con i conteggi veri (17 misure, 7 impianti, 8 modelli, 36 cantieri). Sotto, il **cartiglio** a quattro celle (sede, telefono e orari, trasporto e posa, paesi dei cantieri), come la tabella in fondo ai disegni dell'azienda.
2. **Vasche monoblocco** (fondo calcestruzzo): il render della vasca 550 con la sua quota "550 cm" e la riga dei dati; accanto "Undici misure rettangolari e sei circolari, da 2,30 a 50 mc."
3. **Depurazione** (Jensen "Find Products Fast", Escofet "Highlights"): sette impianti in due colonne chiuse da filetti, render in sezione, un dato in monospazio; l'ottava cella manda all'ufficio tecnico.
4. **Piattaforme per autolavaggi** (fondo grafite, Forterra, Rieder): la pianta quotata della pista self 450 in arancio, la tabella degli otto modelli, i due numeri dell'attrito (0,88 sul bagnato, 0,40 il limite di legge), il brevetto.
5. **Il calcestruzzo**: C35/45, XC4 · XS1-XD2 · XF1 · XA2, B450C, S4 in quattro celle.
6. **Realizzazioni** (Jensen, Godelmann): una foto di Altivole, "36 cantieri, da Aosta ad Avetrana. Cinque oltre confine." e la distinta dei luoghi con la sigla.
7. **Ufficio tecnico**.

### Vasche
1. Apertura con la foto del piazzale di vasche circolari a filo del margine destro e un indice a tre voci.
2. **Rettangolari**: la gamma delle 11 vasche disegnate in scala sceglie la riga della tabella e ne legge le misure; accanto la vasca 1050 in posa, segnata "in foto" nella tabella.
3. **Circolari**: render e tabella delle 6 misure.
4. **Con resine epossidiche** (fondo grafite): le due foto degli interni rossi, la tabella delle 15 misure in un riquadro apribile.
5. Calcestruzzo e armature: il testo delle schede e le quattro classi di esposizione.
6. Ufficio tecnico.

### Depurazione
1. Apertura con l'indice numerato 01-07 e la foto di una vasca con pozzetto in cantiere.
2. Sette schede, a fondi e lati alterni: 01 dissabbiatore statico, 02 separatore grassi (UNI EN 1825-1), 03 vasca Imhoff, 04 separatore oli con filtro a coalescenza, 05 separatore oli per autorimesse e garage (tabella a due schede: acque superficiali e Laguna di Venezia), 06 impianti di prima pioggia (a tutta larghezza, con i tre passaggi: scolmatore, accumulo 48 ore, separatore oli), 07 depuratori biologici (tabella a due schede, BIO e BIO L). Ogni scheda: render o foto, testo dell'azienda corretto, tabella completa.
3. Ufficio tecnico.

### Piattaforme per autolavaggi
1. Apertura con la pista sotto le spazzole a filo del margine sinistro, "La pista di lavaggio arriva in pannelli e si posa in poche ore", brevetto.
2. **Caratteristiche e vantaggi**: i cinque scopi scritti dall'azienda e la tabella d'attrito oggi chiusa in un'immagine (gomma 4S e cuoio, asciutto e bagnato, limite D.M. 236/1989).
3. **Com'è fatta** (fondo grafite): la pianta quotata della pista self 450 con pannelli, vasca di raccolta, grigliato, calcestruzzo.
4. **Gli otto modelli**: i disegni in pianta dell'azienda, tre piste self e cinque portali, con misure, pannelli e pesi; un'ancora per modello.
5. **Fornitura**: le sette voci comprese, cosa è su richiesta (trasporto, autogru), cosa è escluso (opere edili).
6. **Esempio di posa**: la sezione a strati con le didascalie portate in HTML.
7. **Personalizzazione**: quattro colori del calcestruzzo, isola di aspirazione, trave di rialzo, riscaldamento a pavimento.
8. **Piattaforme posate**: striscia a scorrimento di nove cantieri, con regione e modelli.
9. Ufficio tecnico.

### Realizzazioni
1. Apertura con la mappa (le linee arancio partono da Legnaro e arrivano ai 36 cantieri) e l'elenco dei luoghi, che accende il punto sulla mappa.
2. **I cantieri**, divisi per regione e paese: foto di copertina (lightbox), luogo e sigla, tipo di attività dal titolo del sito, modelli citati nelle didascalie del sito, numero di foto. Nessun nome di cliente.
3. Ufficio tecnico.

### Azienda
1. Apertura: chi è Gardens Pav (testo dell'azienda), foto delle vasche caricate.
2. **Il calcestruzzo** (fondo grafite): "C35/45" grande, l'impianto computerizzato, Rck 45, S4, B450C, copriferro 3 cm.
3. **Norme di riferimento** [elenco da confermare col cliente].
4. **Dati societari**: ragione sociale, sede, P.IVA e C.F., REA, capitale, PEC, codice SDI, recapiti.
5. Ufficio tecnico.

### Contatti
1. Recapiti col telefono grande, e il modulo **Richiesta informazioni** (Contact Form 7: nome, azienda, email, telefono, manufatto, dato di dimensionamento, comune di posa, note, disegno allegato, consenso privacy). Nel fallback HTML, al posto del modulo, un pulsante che apre un'email.
2. **Dove siamo**: la mappa di Legnaro disegnata dai dati OpenStreetMap e la mappa di Google che si carica solo se la si chiede.

## Navigazione

Menu: Vasche, Depurazione, Piattaforme per autolavaggi, Realizzazioni, Azienda, Contatti (menu WordPress "Menu principale", widget Navigation Menu di Ultimate Addons). Voce attiva in arancio scuro con sottolineatura arancio. Su tablet e telefono diventa un menu a tendina a tutta larghezza; accanto restano "Chiama" e, dentro la tendina, telefono, email e "Richiedi informazioni".

Per `ciclo.sh`:
```
PAGINE="/:01-home /vasche/:02-vasche /depurazione/:03-depurazione /piattaforme-autolavaggi/:04-piattaforme-autolavaggi /realizzazioni/:05-realizzazioni /azienda/:06-azienda /contatti/:07-contatti"
MENU="vasche,depurazione,piattaforme-autolavaggi,realizzazioni,azienda,contatti"
```

La specifica completa (token, misure a 1440, 1024 e 390, testi esatti, foto, elementi dinamici, redirect) è in `_prova/spec.md`.
