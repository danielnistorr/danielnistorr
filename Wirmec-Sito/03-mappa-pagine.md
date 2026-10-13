# 03. Mappa delle pagine

Il sito attuale ha 42 schede prodotto in sei famiglie, una pagina Azienda di due paragrafi, una pagina News vuota ("0 news") e Contatti. Il nuovo sito raggruppa le famiglie per **come lavora la macchina** (in linea automatica, in banco, applicatore, controllo), che è il modo in cui un cablatore cerca quello che gli serve. Ogni codice ha un'ancora nella sua pagina: i 42 indirizzi vecchi portano dritti alla riga giusta (redirect in `_prova/spec.md`, paragrafo 15).

| Brief (impianto PMF) | Wirmec | Slug | Perché |
|---|---|---|---|
| Home | **Home** | `/` | la AM460 Sintesi in apertura, le sei linee, le dodici lavorazioni sul cavo, una scheda per linea, contatti |
| Chi siamo | **Azienda** | `/azienda/` | chi è Wirmec, le sei linee con tutti i codici, i nove distributori in Europa, i brevetti dichiarati, i dati del Registro delle Imprese |
| Team | dentro **Contatti** ("In Italia, un referente per zona") | | le persone pubbliche sono i tre referenti commerciali: nome, zona, cellulare; nessun ritratto (brief fotografico nel LEGGIMI) |
| Prototipi/moto | **Automatiche**, **Da banco**, **Applicatori**, **Controllo qualità** | `/automatiche/`, `/da-banco/`, `/applicatori/`, `/controllo-qualita/` | il prodotto di Wirmec sono le macchine: quattro pagine, una per modo di lavorare, con tutte le schede del sito attuale |
| Sponsor | non c'è | | Wirmec non ha marchi rivenduti né sponsor; i nove distributori stanno in Azienda e in Contatti |
| News | non c'è | | oggi "0 news" in entrambe le categorie; una pagina vuota peggiora il sito. Si aggiunge quando Wirmec ha notizie da pubblicare |
| Contatti | **Contatti** | `/contatti/` | richiesta di offerta con modulo, referenti per regione, distributori all'estero, come arrivare |

Più due blocchi comuni, globali con il plugin gratuito Ultimate Addons for Elementor: **Testata** bianca (logo, menu, telefono della sede, "Richiedi offerta"; su tablet e telefono "Chiama" e menu a scomparsa) e **Piè di pagina** notte (prodotti, pagine, sede, contatti, P.IVA, REA, capitale sociale, Privacy e Cookie).

## Sezioni per pagina

### Home
1. **Apertura** (Hermle, Universal Robots, Salvagnini): la AM460 Sintesi scontornata sul grigio studio, "Macchine per tagliare, spelare e aggraffare il cavo", due pulsanti; sotto la macchina il codice e quattro valori (stazioni, sezione, velocità, aggraffatrici); in fondo alla fascia le sei linee con il numero di modelli.
2. **Una stazione, una lavorazione sul cavo** (Komax): le dodici lavorazioni delle brochure WirAM nei disegni Wirmec del cavo rosso, tutti alla stessa scala.
3. **WirAM** (fascia ardesia, Schleuniger): la AM310 quattro e i sette modelli con un dato ciascuno.
4. **W 1500** (Hermle, Universal Robots): il codice scritto grande accanto alla pressa, i dati in righe, gli altri modelli da banco in una riga.
5. **WirTool** (grigio studio): WB 10 e WPB 10 sul grigio delle loro foto, i dati comuni degli applicatori.
6. **WirTest** (Hermle "Applications"): il terminale aggraffato sul righello e la sezione al micrografo, con W200 e W100.
7. **Richiedi un'offerta**: il telefono della sede grande, i tre referenti per zona, i distributori in una riga.

### Automatiche (WirAM e Accessori macchina)
1. Apertura con la AM400 quattro e l'indice di tutti i codici della pagina.
2. **Sette modelli**: righe con foto, descrizione dalle schede e sei dati in colonne fisse (stazioni, sezione, spelatura, velocità, peso, ingombro); brochure e richiesta per ogni modello.
3. **La AM310 quattro in pianta**: il disegno della brochure con le quote 3000 e 1400 mm e la legenda delle stazioni A1-B3.
4. **Dal pannello si prepara la lavorazione** (fascia ardesia): la postazione dell'operatore.
5. **Accessori**: le dieci unità con foto, disegno della lavorazione che fanno e dati.
6. Brochure (cinque PDF, in inglese).
7. Richiedi un'offerta.

### Da banco (WirPress e WirStrip)
1. Apertura: le cinque presse in fila sopra il loro codice e la loro forza.
2. **Presse da banco**: tabella con i cinque modelli in colonna.
3. **Spela aggraffa**: la WSC 15 e la tabella delle quattro WSC; i due brevetti della WSC 21; la WSC 31.
4. **WirStrip**: troncatrice e due sguainatrici con i dati.
5. Brochure (quattro PDF).
6. Richiedi un'offerta.

### Applicatori (WirTool)
1. Apertura: WB 10 e WPB 10 grandi sul grigio, i dati comuni, l'indice dei dieci codici.
2. **Dieci applicatori, per tipo di terminale**: side feed, end feed, ferrules, splice, contatti torniti, bus bar.
3. **Dove si montano**: la fila di applicatori sul banco e le macchine su cui lavorano.
4. Richiedi un'offerta.

### Controllo qualità (WirTest)
1. Apertura su ardesia: la micrografia di un'aggraffatura mostrata 1:1, con le tre letture scritte grandi.
2. **W200, laboratorio di micrografia**: taglio, lucidatura, fotografia; la penna W202.
3. **Dinamometri**: tabella del W100, il W125 da 2500 N.
4. **Il terminale, da vicino**: la foto della scheda AM210 futura.
5. Richiedi un'offerta.

### Azienda
1. Apertura senza foto: chi è Wirmec in tre paragrafi, accanto "Wirmec in breve" con i dati del Registro delle Imprese.
2. **Sei linee, 42 macchine e unità**: per ogni linea cosa fa e tutti i codici, ciascuno link alla sua scheda.
3. **Nove distributori** (Zünd, LEMO): la mappa d'Europa con un filo da Ponte San Nicolò a ogni città, elenco numerato.
4. **Brevetti dichiarati**: righe codice, fatto, fonte.
5. Richiedi un'offerta.

### Contatti
1. **Richiedi un'offerta**: telefono grande, email, fax, PEC, sede; accanto il modulo **Richiesta offerta** (Contact Form 7: nome, azienda, email, telefono, provincia o paese, linea, modello, terminale e cavo, quantità, messaggio, allegato, consenso privacy). La linea e il modello si preselezionano dal pulsante della pagina di provenienza. Nel fallback HTML, al posto del modulo, un pulsante che apre un'email già impostata.
2. **In Italia, un referente per zona**: "In che regione lavori?" evidenzia il referente giusto; tre righe con una piccola Italia, nome, regioni, cellulare.
3. **All'estero, nove distributori**: indirizzi completi in griglia.
4. **Come arrivare** (fascia ardesia): la mappa della zona disegnata da OpenStreetMap, le distanze da casello, stazione e centro di Padova, i link a Google Maps e OpenStreetMap. Nessuna mappa Google incorporata.

## Navigazione

Menu: Automatiche, Da banco, Applicatori, Controllo qualità, Azienda, Contatti (menu WordPress "Menu principale", widget Navigation Menu di Ultimate Addons). A destra il telefono della sede e "Richiedi offerta". Su tablet e telefono il menu diventa a scomparsa a tutta larghezza; accanto restano "Chiama" e il pulsante del menu.

Stringhe per `ciclo.sh`:
```
PAGINE="/:01-home /automatiche/:02-automatiche /da-banco/:03-da-banco /applicatori/:04-applicatori /controllo-qualita/:05-controllo-qualita /azienda/:06-azienda /contatti/:07-contatti"
MENU="automatiche,da-banco,applicatori,controllo-qualita,azienda,contatti"
```

Specifica completa (token, impaginazione a 1440, 1024 e 390, testi, foto, redirect, cose da confermare): `_prova/spec.md`.
