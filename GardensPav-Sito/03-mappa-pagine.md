# 03. Mappa delle pagine

Versione del 13 ottobre 2026, dopo la home finale (`_prova/home-finale/`, screenshot in `screenshot/home/`). Sostituisce la mappa
del 6 ottobre (conservata in `_prova/03-mappa-pagine-6-ottobre.md`).

Il sito attuale ha 82 pagine italiane: un menu alto (L'Azienda, Prodotti, Dove siamo, News, Contatti), un menu prodotti con tre
famiglie e una pagina per ogni manufatto, per ogni modello di piattaforma e per ognuno dei 36 cantieri. Il nuovo sito le raccoglie
in sette pagine, una per compito di chi visita. Ogni vecchia scheda diventa un'ancora dentro la pagina della sua famiglia, così
nessun dato si perde e i vecchi indirizzi si reindirizzano uno per uno (`plugin/redirect-301.csv`).

**L'idea del sito.** Ogni pezzo si vede intero, nel posto dove lavora e con le sue misure vere, e da ogni misura si arriva in un
clic all'ufficio tecnico che fa il prezzo. In home è la sezione del piazzale di un autolavaggio (la pista sopra, le vasche sotto);
nelle altre pagine ritorna come disegno in sezione o come tabella delle taglie, il documento che l'ufficio tecnico manderebbe a
un'impresa.

| Sito attuale | Nuovo sito | Slug | Compito di chi visita | Documento del mestiere |
|---|---|---|---|---|
| Home (slider, nessun testo) | **Home** | `/` | capire cosa produce l'azienda, trovare la famiglia giusta, chiamare | sezione quotata del piazzale; schede delle famiglie con due numeri veri |
| Piattaforme per autolavaggi + 15 pagine (modelli, caratteristiche, posa, isola, personalizzazioni) | **Piattaforme per autolavaggi** | `/piattaforme-autolavaggi/` | il gestore o il costruttore di autolavaggi sceglie il modello e legge cosa è compreso | schede degli otto modelli; distinta della fornitura; tabella d'attrito |
| Vasche prefabbricate monoblocco + 3 schede | **Vasche** | `/vasche/` | l'impresa trova la vasca per volume, legge ingombro e pesi per scavo e autogru | gamma delle 17 vasche alla stessa scala; tabella delle misure |
| Depurazione + 7 schede | **Depurazione** | `/depurazione/` | il progettista parte dal dato (AE, l/s, m², posti auto) e trova taglia e norma | indice "dal dato alla taglia"; sette tabelle delle taglie |
| Realizzazioni + 36 pagine di galleria | **Realizzazioni** | `/realizzazioni/` | il gestore vede piste posate vicino a sé e per un'attività come la sua | elenco delle referenze con luogo, tipo, modelli e foto |
| L'Azienda (testo distrutto), PDF | **Azienda** | `/azienda/` | l'ufficio acquisti o la direzione lavori verifica il fornitore | scheda fornitore: calcestruzzo, norme, brevetto, dati societari |
| Dove siamo + Contatti | **Contatti** | `/contatti/` | chiedere prezzo e consegna con i dati giusti, trovare la sede | modulo di richiesta d'offerta; recapiti per tipo di richiesta |
| News (una voce vuota) | nessuna | | | una sola notizia senza data che porta a una pagina vuota: si riapre se il cliente la tiene aggiornata |
| Privacy, Cookie | Privacy, Cookie | `/privacy/`, `/cookie/` | | testo del cliente |

Più due blocchi comuni, globali con il plugin gratuito Ultimate Addons for Elementor, uguali alla home finale:
- **Testata** bianca e fissa: logo, menu, telefono 049 641591 con gli orari dell'ufficio tecnico, "Chiedi un'offerta". Sotto i 1340
  px il menu va nell'hamburger con la ricerca "Nome o taglia"; sotto i 768 px resta il telefono e in basso compare la barra "Chiama"
  e "Chiedi un'offerta".
- **Piede** #F2F1EE: logo, prodotti, azienda, ufficio tecnico, riga legale completa (ragione sociale, sede, P.IVA e C.F., Registro
  Imprese di Padova, REA, capitale sociale, PEC, link a Privacy e Cookie).

Ogni pagina interna tranne Contatti finisce con la **chiusura comune** "Prezzo e consegna, dall'ufficio tecnico": orari, cosa tenere
pronto per quella pagina, telefono grande e "Chiedi un'offerta" con il prodotto già scelto nel modulo.

## Sezioni per pagina

### Home
La home finale del 13 ottobre, senza cambiamenti di testo e di ordine.
1. **Apertura con la sezione del piazzale** (Mall Umweltsysteme, Hauraton): "Piattaforme per autolavaggi e vasche per il trattamento
   delle acque", la sezione in scala con pista self Mod. 450, vasca sottopista, dissabbiatore e separatore oli, otto didascalie che
   portano alle schede, compreso, su richiesta ed escluso.
2. **Piattaforme per autolavaggi e vasche per l'acqua** (Jensen Precast, "Find Products Fast"): 4 schede delle piattaforme e 8 delle
   vasche e degli impianti, con render, sottoprodotti, due righe di numeri veri e "Chiedi un'offerta"; la riga delle prove (brevetto,
   attrito 0,88, 36 cantieri); le foto della consegna.
3. **Prima pioggia, dal piazzale allo scarico** (Hauraton, percorso dell'acqua): render in sezione, quattro passi, esempio per 2.000 m².
4. **Misure, pesi e posa delle piattaforme**: la pista sotto il portale, la tabella degli otto modelli (4 righe), la posa in quattro
   fasi disegnata e fotografata.
5. **Piattaforme posate in 36 cantieri** (SW Umwelttechnik, Referenzbücher): mosaico di 16 foto, cantieri per regione, la posa ad
   Avetrana.
6. **Prezzo e consegna, dall'ufficio tecnico**: due ingressi col telefono, recapiti, modulo "Richiesta d'offerta".

### Piattaforme per autolavaggi
1. **Apertura**: "Piattaforme prefabbricate per autolavaggi", come si compongono (due pannelli per la pista self, quattro o sei per il
   portale), quattro fatti (brevetto, superficie a rombi, senza casseforme, smontabile), un bottone "Chiedi un'offerta"; a destra le
   piazzole posate prima degli impianti.
2. **Gli otto modelli** (Jensen): griglia 4×2 di schede con la pianta disegnata dall'azienda e una tabellina di quattro righe
   (piazzola, pannelli, peso del pannello, raccolta); un'ancora per modello (`#mod-450` ... `#mod-5`).
3. **Fornitura** (Mall, la sezione con i pezzi sotto terra): la sezione della pista grande con le didascalie e accanto la distinta di
   quello che è compreso, su richiesta ed escluso.
4. **La posa di un portale Mod. 1 a Crema**: le quattro fasi del disegno e sei foto in sequenza dal cantiere vero (giuntoplasto,
   piastre, sigillatura, grigliati, piattaforma finita).
5. **Superficie e attrito**: la superficie a rombi in foto, la tabella d'attrito oggi chiusa in un'immagine (gomma 4S e cuoio,
   asciutto e bagnato, limite D.M. 236/1989), le righe del volantino delle piste.
6. **Colori, riscaldamento e accessori**: le quattro piante colorate dell'azienda (rosso, verde, giallo, marrone); riscaldamento a
   pavimento, isola di aspirazione, trave di rialzo con spessore e peso.
7. **Piste posate**: quattro cantieri con le foto migliori a 1600 px (Altivole, Milano, San Lazzaro di Savena, Cornate d'Adda).
8. Chiusura comune.

### Vasche
1. **Apertura con la gamma in scala**: "Vasche monoblocco in calcestruzzo armato vibrato", usi e gamma in una frase, e le 17 vasche
   disegnate di lato alla stessa scala sotto la linea del terreno; ogni vasca porta alla sua riga della tabella.
2. **Vasche rettangolari**: render, la 1050 calata con l'autogru, tabella di 11 misure (misure esterne, peso vasca, peso coperchio,
   volume) con le note sulle solette.
3. **Vasche circolari**: render, foto, tabella di 6 misure.
4. **Con resine epossidiche**: le due foto degli interni rossi; le 15 misure sono quelle delle tabelle sopra, scritto in una frase.
5. **Calcestruzzo e armatura**: C35/45, S4, le quattro classi di esposizione spiegate, B450C, copriferro, getto in cassero vibrato.
6. Chiusura comune.

### Depurazione
1. **Apertura: dal dato del progetto alla taglia**: la tabella-indice che parte dal dato (m², m³, l/s, posti auto, AE) e porta
   all'impianto e alla sua gamma.
2. **Acque dei piazzali e delle autorimesse**, nell'ordine del percorso dell'acqua: impianti di prima pioggia (render lungo, quattro
   passi, 17 taglie), dissabbiatore statico (15 misure), separatore oli con filtro a coalescenza (5 taglie, UNI EN 858-1), separatore
   oli per autorimesse (due tabelle: acque superficiali e Laguna di Venezia).
3. **Acque delle cucine**: separatore grassi (UNI EN 1825-1, dove si usa, 5 taglie).
4. **Acque nere domestiche**: vasca Imhoff (i due comparti, 7 taglie da 5 a 70 AE), depuratori biologici (due tabelle, BIO e BIO L).
   Ogni scheda ha la stessa impaginazione: render in sezione a sinistra con "si sceglie su" e norma, testo e tabella a destra.
5. Chiusura comune.

### Realizzazioni
1. **Apertura con la mappa**: "36 cantieri con le piattaforme Gardens Pav", chi sono i clienti per tipo, le regioni con il numero;
   la mappa con Legnaro e i punti dei cantieri.
2. **Le piste posate**: filtro per regione e griglia di 36 schede (copertina, luogo e provincia, regione e tipo, modelli citati
   dal sito, numero di foto); le foto si aprono nella lightbox. Nessun nome di cliente.
3. Nota sui cantieri citati dal sito senza foto (Poprad, Brendola, Alessandria, Olbia).
4. Chiusura comune.

### Azienda
1. **Apertura**: "Gardens Pav S.r.l., Legnaro (PD)", cosa produce, sede e stabilimento sulla SS516, iscrizione al Registro Imprese
   dal 2005, le due linee di prodotto; la vasca calata nello scavo.
2. **Il calcestruzzo**: l'impianto computerizzato, Rck 45, S4, B450C, copriferro 3 cm.
3. **Norme, brevetto e certificazione**: tabella delle norme, brevetto n° 275.271; ISO 9001 solo dopo il rinnovo.
4. **Dati per l'anagrafica fornitori**: ragione sociale, sede, P.IVA, REA, capitale, PEC, codice SDI, ATECO, recapiti.
5. Chiusura comune.

### Contatti
1. **Recapiti e modulo**: "Richiesta d'offerta e contatti", telefono e orari dell'ufficio tecnico, tre ingressi per tipo di richiesta
   (piattaforme, vasche e impianti, amministrazione e ordini), come mandare un disegno; accanto il modulo **Richiesta d'offerta**
   (Contact Form 7: prodotto, il vostro dato, quantità, comune di posa, trasporto, nome, azienda, telefono, email, note, consenso),
   lo stesso della home, precompilato dalle altre pagine. Nel fallback HTML un bottone che apre un'email.
2. **Dove siamo**: Via Romea 154/A sulla SS516, la mappa dei dintorni disegnata dai dati OpenStreetMap e la mappa di Google che si
   carica solo se la si chiede.

## Navigazione

Menu: Piattaforme per autolavaggi, Vasche, Depurazione, Realizzazioni, Azienda, Contatti (lo stesso ordine della home finale; menu
WordPress "Menu principale"). Voce attiva con il filetto grafite sotto; al passaggio il filetto diventa arancio. Sotto i 1340 px il
menu va nella tendina dell'hamburger con la ricerca; accanto restano il telefono e, sotto i 768 px, la barra in basso "Chiama" e
"Chiedi un'offerta".

Per `ciclo.sh`:
```
PAGINE="/:01-home /piattaforme-autolavaggi/:02-piattaforme-autolavaggi /vasche/:03-vasche /depurazione/:04-depurazione /realizzazioni/:05-realizzazioni /azienda/:06-azienda /contatti/:07-contatti"
MENU="piattaforme-autolavaggi,vasche,depurazione,realizzazioni,azienda,contatti"
```

La specifica completa (token, misure a 1440, 1024 e 390, testi esatti, foto, elementi dinamici, modulo, redirect, segnali evitati,
cose da confermare) è in `_prova/spec.md`.
