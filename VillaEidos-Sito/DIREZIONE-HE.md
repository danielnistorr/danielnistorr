# Villa Eidos, direzione artistica

Scritta il 17 novembre 2026, prima del codice, seguendo `_metodo/highend/SISTEMA.md` (punto 3, vincoli della sezione 2 e lezioni della sezione 8). Sito nuovo: villaeidos.it oggi mostra la pagina di parcheggio di Aruba.

**Fonti dei fatti**, le sole ammesse: il testo del cliente (`villaeidos.it.doc`, convertito in `testo/villaeidos.it.txt`), il logo e le cinque foto degli interni. Nel `.doc` c'è anche una schermata satellitare di Google Maps: serve a noi per capire il posto, non va sul sito (le immagini sono di Google). Niente numeri di posti, metri quadri, servizi, orari, anni o nomi che il testo non dà.

Il sito è per aziende che cercano una sede o una sala: elegante e sobrio, non un sito di eventi.

## 1. La cosa vera

Una villa storica e un'ampia barchessa in un giardino centenario, riqualificate per funzioni direzionali conservando i caratteri originali, a pochi minuti dalla Tangenziale di Padova e dal casello Padova Sud della A13. La villa ospita uffici e sedi di rappresentanza; la barchessa sale riunioni di diverse dimensioni e una grande sala conferenze.

L'idea in una riga: **il luogo scritto come un'iscrizione.** Mancano le foto della villa, della barchessa e del giardino, che sono il vero argomento: la pagina allora nomina il luogo in grande (Villa, Barchessa, Giardino, Parcheggi) con un serif classico, e lascia in apertura un fregio di pietra con le stesse parole, al posto esatto dove andrà la fotografia della facciata. Quando arriva la foto si cambia con un clic in Elementor e la pagina non va ridisegnata.

## 2. Riferimenti guardati

Aperti con Playwright il 17/11/2026 a 1440x900: prima schermata e due scorrimenti (schermate di lavoro nella cartella temporanea, non nel repository). Awwwards.com non risponde dal nostro ambiente: i due premiati vengono da `_metodo/professionale/alto/awwwards.md`, dove i premi sono già verificati.

**Ville e sedi direzionali**

1. **Villa Erba** (villaerba.it), centro congressi in una villa storica sul lago di Como.
   - Mossa 1: l'apertura è una foto dal drone della villa nel parco. Da noi: il posto della foto d'apertura è una fascia larga come una facciata, pronta per la foto dal drone o della facciata (è la prima foto da chiedere).
   - Mossa 2: gli spazi si scelgono per uso (fiere, meeting e convention, eventi corporate). Da noi: "per chi è" ordinato per uso (rappresentanza, riunioni, convegni e formazione, networking).
   - Da non prendere: il titolo in corsivo serif, il bottone "Play video" sulla foto, le tessere con le foto colorate dei padiglioni.
2. **The Office Group** (theofficegroup.com), uffici flessibili in edifici storici a Londra.
   - Mossa 1: un titolo grande su una riga, chiuso da un filetto, e la foto in una cornice media sotto, non a tutta pagina. Da noi: le foto degli interni in cornici medie, mai oltre 1,25 volte la loro misura.
   - Mossa 2: ogni sede con il suo indirizzo sotto il nome. Da noi: i tre ingressi, ognuno con la via e il link alla mappa.
   - Da non prendere: le schede con le etichette in riquadro, il carosello, il banner dei cookie.
3. **Fora** (foraspace.com), uffici e sale riunioni a Londra.
   - Mossa 1: un solo campo pieno, verde scuro, con il testo chiaro accanto alla foto della sala riunioni. Da noi: il verde scuro del logo è l'unico campo pieno, sulla sezione "per chi è".
   - Mossa 2: le sale riunioni si prenotano anche senza essere membri: l'invito è chiaro e solo. Da noi: un invito ("Richiedi disponibilità") e il telefono a vista.
   - Da non prendere: il titolo bianco sopra la foto, le foto di persone di repertorio.
4. **Kilometro Rosso** (kilometrorosso.com), distretto direzionale e dell'innovazione, Bergamo.
   - Mossa 1: "Come raggiungerci" sta nella testata, tra le prime voci. Da noi: "Come arrivare" è una voce del menu e una sezione con i collegamenti scritti per esteso.
   - Mossa 2: il rosso del marchio è l'unico colore forte. Da noi: il verde del logo come accento, non dappertutto.
   - Da non prendere: la fascia rossa sopra la testata, le schede grigie delle notizie, il pannello dei cookie a tutta pagina.

**Premiati su Awwwards in settori vicini**

5. **Arc** (arcprojects.build), ristrutturazioni d'architetto, Sydney, Menzione d'onore 1/10/2025.
   - Mossa 1: il nome grande e un solo filetto in tutta la pagina. Da noi: nessun filetto decorativo, lo spazio separa.
   - Mossa 2: la didascalia a due voci, il nome in nero e il dettaglio in grigio. Da noi: sotto ogni foto il nome dello spazio e una riga del testo del cliente.
   - Da non prendere: la foto a tutta pagina che qui non abbiamo, il menu minuscolo in alto a sinistra.
6. **Cedar Springs** (cedarsprings.net), giardini, Oakville, Menzione d'onore 20/11/2025.
   - Mossa 1: un titolo grande e leggero accanto a un paragrafo breve e a un solo link. Da noi: il titolo d'apertura in un serif leggero, sotto una frase sola e due azioni.
   - Mossa 2: le parole del luogo usate come titoli ("fire, water & alfresco"). Da noi: Villa, Barchessa, Giardino, Parcheggi a 150 px.
   - Da non prendere: il titolo in minuscolo che sparisce nella foto, le stelle "5 star".

## 3. Carattere

- **Display: Brygada 1918** (The Brygada 1918 Project Authors, progetto di Borys Kosmynka; SIL Open Font License 1.1, Google Fonts; file variabile da `@fontsource-variable/brygada-1918` 5.3.0, 22 KB), peso 400, mai corsivo. Un serif classico, da iscrizione, con le maiuscole romane che vanno bene per il fregio e le cifre allineate per il telefono. Solo tre momenti forti: il titolo d'apertura (118 px a 1440, 44 a 390), le quattro parole del luogo (150 px a 1440, 60 a 390), il telefono della richiesta (118 px a 1440, 52 a 390).
- **Testo: Pontano Sans** (The Pontano Sans Project Authors, disegno di Vernon Adams; SIL Open Font License 1.1, Google Fonts; file variabile da `@fontsource-variable/pontano-sans` 5.3.0, 23 KB), 400 e 500. Un bastone geometrico ma morbido, vicino alle lettere tonde della scritta "villa EIDOS" del logo senza rifarle. Testo, `h2` di servizio (fino a 44 px), testata, didascalie, modulo e piede.
- Nessuna etichetta sopra i titoli, nessun numero davanti alle sezioni, nessun corsivo. Il maiuscolo solo nel fregio (è un'iscrizione).
- Registro: riga in `_metodo/professionale/alto/REGISTRO-CARATTERI.md`. Brygada 1918 e Pontano Sans non sono in nessuna home della campagna né nelle liste di `_metodo/CARATTERI-E-SEGNALI-IA.md`.

## 4. Colore (dal logo e dalla pietra)

Il logo è CMYK con il profilo Coated FOGRA39: i due inchiostri, convertiti in sRGB con il profilo, sono **verde #4A8C46** (C74 M23 Y88 K7) e **verde acqua #5EC1C9** (C61 Y24). Il provino di oggi li mostrava più accesi perché ignorava il profilo.

| Nome | Valore | Da dove | Dove |
|---|---|---|---|
| Carta | #F3F1EC | l'intonaco chiaro degli interni | fondo della pagina |
| Pietra | #E4DED2 | la pietra delle ville venete | il fregio d'apertura, il piede |
| Inchiostro | #1E231F | | testo, titoli |
| Grigio | #5B5F59 (6,0:1 sulla carta) | | testi secondari, didascalie |
| Verde del logo | #4A8C46 | il logo | accento: il segno della pagina attiva, il filetto di un link, il fuoco della tastiera |
| Verde scuro | #2E6A33 (6,4:1 con il bianco) | il verde del logo scurito | il bottone "Richiedi disponibilità" |
| Verde notte | #1F3A23 | il verde del logo nel buio | **l'unico campo pieno: "per chi è"** |
| Verde acqua | #5EC1C9 | il logo | solo nel logo e nel fuoco della tastiera sul verde notte |

Niente crema con terracotta, niente nero con verde acido.

## 5. Movimento

Due movimenti del kit HE, si spengono da *Aspetto > Personalizza > Movimenti*, e con "riduci movimento" la pagina è ferma e completa:
- **il titolo d'apertura sale riga per riga** (`data-he-split`, subito): è il gesto, perché in apertura la notizia è il titolo;
- **le due foto più grandi** (sale riunioni e sala conferenze) **si scoprono con un taglio netto** dal basso quando entrano (`data-he-wipe`).

Niente dissolvenze, niente scala d'apertura (con la fascia di pietra sarebbe solo un cambio di sfondo), niente testata che si nasconde: la testata resta ferma in alto, con il telefono, anche sul telefono.

## 6. Ritmo

| Sezione | Scheletro | Note |
|---|---|---|
| Apertura | titolo d'apertura su quattro righe, largo quasi tutta la pagina; sotto, a sinistra la frase sul posto e a destra le due azioni; poi la fascia larga del fregio (la futura foto della facciata) | prima schermata ferma: logo in testata, titolo, azioni, l'inizio del fregio |
| Il luogo | **sezione firma**: frase d'apertura, poi quattro righe con la parola a 150 px a sinistra e il fatto a destra sulla stessa linea | il culmine tipografico: Villa, Barchessa, Giardino, Parcheggi |
| Gli spazi | griglia sfalsata di due colonne di larghezza diversa: le foto in cornici medie, il nome e una riga sotto | foto alla misura vera o poco più |
| Per chi è | campo verde notte, titolo a sinistra, quattro usi in due colonne | l'unico colore pieno |
| Come arrivare | tre colonne: titolo e mappa, i collegamenti in tre gruppi, i tre ingressi | la mappa è un link a Google Maps, nessuna mappa incorporata |
| Richiesta di disponibilità | il telefono a 118 px su tutta la riga, sotto a sinistra titolo, nota ed email, a destra il modulo che prepara la mail | il modulo non manda dati al sito |
| Piede | su pietra: logo, indirizzi, recapiti, privacy e cookie, il segnaposto dei dati legali | |

Su telefono: testata compatta con il logo, "Chiama" e il menu; nessuna sezione fissata; le foto una sotto l'altra alla loro misura.
