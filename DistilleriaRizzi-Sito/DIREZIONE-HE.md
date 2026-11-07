# Distilleria Rizzi, direzione artistica della home HE

Scritta il 7 novembre 2026 seguendo `_metodo/highend/SISTEMA.md` (punto 3) e le lezioni dei piloti (sezione 8). Pagina: `sito-he/index.html`. La `sito/` di oggi non si tocca. Fonti dei fatti: `01-analisi.md`, `LEGGIMI.md`, le note in `screenshot/` e il sito di oggi (testi delle pagine riletti il 7/11/2026 dall'API di WordPress: home, about-us, contact, amari, prodotti-per-pasticceria, spritz, apertura-spaccio, le schede prodotto, gli articoli). Quello che `01-analisi.md` (sezione 9) e il `LEGGIMI.md` danno da confermare resta fuori: il 1850 e il marchio Genzial, la festa del centenario, i cognomi dei titolari, gli orari fissi dello spaccio, Felsina, Fernet e Garofano (in vendita oggi?), le etichette per terzi, i clienti con il nome, il negozio online. Mai "distillare": è un liquorificio.

## 1. La cosa vera

Sulle loro bottiglie c'è ancora la grafica di casa (la fascia RIZZI in un Clarendon a filo, il "Bitter" in corsivo, il LEONE con la corona, l'abete del Pinalpe) e la gamma va, scheda per scheda, dall'Aperizzi a 11% vol. alla Vodka a 70° per la pasticceria. Le frasi che reggono la pagina sono loro: "I nostri liquori, oggi come una volta" (pagina `amari`) e "facciamo tutto noi, dall'inizio alla fine" (pagina `spritz`).

L'idea in una riga: **oggi come una volta, scritto in grande accanto a una bottiglia vera; poi la gamma messa in scala, ogni bottiglia sul suo grado.**

## 2. Riferimenti guardati

Aperti con Playwright il 7/11/2026 (`_prova/he/script/riferimenti.mjs`, con il cancello dell'età e i cookie superati dove si poteva): prima schermata a 1440x900 e a 390x844, tre scorrimenti da 900 px a 1440. Schermate in `_prova/he/riferimenti/<nome>-1440-prima-schermata.jpg`, `-1440-scorrimento-1/2/3.jpg`, `-390-prima-schermata.jpg`; i fogli in `_prova/he/lavoro/rif/`. Mancino apre un video in sovrimpressione che copre tutto, Select tiene il cancello dei 21 anni sullo schermo grande (passa solo a 390): non li conto.

**Liquori, amari, distillati**

1. **Amaro Montenegro** (amaromontenegro.com).
   - Mossa 1: la bottiglia da sola al centro della scena, con accanto un titolo grande di quattro parole ("Dal 1885, diamo forma ad un gusto unico"). Da noi: il Bitter alto quanto la finestra accanto a "Oggi come una volta" in Besley a 166 px.
   - Mossa 2: una frase per schermata, il resto tace. Da noi: ogni sezione ha un solo titolo e una sola immagine che lo prova.
   - Da non prendere: il fondo scuro da spot, i bottoni a filo con l'icona play, i titoli in maiuscolo condensato.
2. **Nonino** (grappanonino.it).
   - Mossa 1: la famiglia come prova (le tre sorelle tra le botti) e la citazione della stampa con la testata e la data (New York Times, 1997). Da noi: la frase di Maddalena e Alessandro sui ricettari del fondatore con "La Difesa del Popolo, 16 marzo 2025".
   - Mossa 2: il timbro "125 anni di distillazione" come segno d'archivio, piccolo e preciso. Da noi: la data esatta del subentro, "Dal 14 dicembre 2022", nel titolo della sezione.
   - Da non prendere: il paragrafo lungo centrato sulla foto, il menu ad hamburger anche sul computer, il modulo della newsletter con il captcha.
3. **Marolo** (marolo.com).
   - Mossa 1: l'etichetta fotografata da vicino come apertura, con il nome grande sopra. Da noi: la cornice che parte stretta sull'etichetta del Bitter (fascia RIZZI e corsivo) prima di mostrare la bottiglia.
   - Mossa 2: il mosaico di foto di misura diversa con una citazione del fondatore in mezzo. Da noi: il dittico dell'alcolato, due foto della stessa misura sulla stessa base, con la frase loro accanto (secondo giro).
   - Da non prendere: lo slider con le frecce, il logo minuscolo al centro della testata grigia.
4. **Braulio** (braulio.it).
   - Mossa 1: il numero come grafica ("150" in rosso sulla bottiglia). Da noi: i gradi in Besley sotto ogni bottiglia, "11%", "40%", "70°".
   - Mossa 2: il tempo come ingrediente ("il tempo è l'ingrediente più prezioso", la produzione). Da noi: l'alcolato di fiori di sambuco in due becher. Nel secondo giro tolte le didascalie "poche ore" e "due settimane": le due foto sono scattate a 5 minuti di distanza (nomi dei file), quindi si descrive solo cio' che si vede.
   - Da non prendere: le parole in maiuscolo spaziato sopra le foto, il banner dei cookie che copre metà pagina.
5. **Strega** (strega.it).
   - Mossa 1: il prodotto scontornato su bianco, piccolo e centrato, tra due colonne di testo. Da noi: le bottiglie scontornate direttamente sulla carta, senza tessere né ombre finte.
   - Mossa 2: la firma corsiva "G. Alberti Benevento" come segno della casa. Da noi: la scritta a pennello "Distilleria Rizzi" (loro, in PNG) in testata e nel piede, mai rifatta.
   - Da non prendere: la foto di repertorio con la modella, i bottoni gialli a filo, il testo grigio piccolissimo.
6. **Nardini** (nardini.it).
   - Mossa 1: le illustrazioni d'archivio usate come fondo dei blocchi (la cena dell'Ottocento). Da noi nessuna illustrazione: l'archivio è la grafica delle etichette, e resta sulle bottiglie.
   - Mossa 2: le pagine dei prodotti divise per famiglia (grappe, liquori, mixology). Da noi: la pasticceria in tre famiglie, una riga ciascuna, i gusti chiusi in un `<details>`.
   - Da non prendere: i banner promozionali in apertura, il carosello, il nero della testata con le voci minuscole.
7. **Cocchi** (cocchi.it).
   - Mossa 1: la fila delle bottiglie sulla stessa linea di base, con il nome sotto. Da noi: la scala dei gradi, tutte in piedi sul righello.
   - Mossa 2: il piede con i dati completi dell'azienda (ragione sociale, indirizzo, telefono, P.IVA). Da noi: il piede con ragione sociale, via, P.IVA, PEC, avvertenza sugli alcolici, Privacy e Cookie.
   - Da non prendere: le schede delle notizie in griglia, le frecce gialle, il giallo pieno del piede.

**Premiati su Awwwards in settori vicini** (premi letti in `_metodo/professionale/alto/awwwards.md`)

8. **Don Molinico** (donmolinico.es), conserve di peperoni, Navarra, Site of the Day 25/4/2026.
   - Mossa 1: il campo crema per tutta la pagina e un solo colore della casa, il rosso, usato pieno solo dove serve. Da noi: la carta delle etichette per tutta la pagina e un solo campo pieno, il blu delle etichette, sulla pasticceria.
   - Mossa 2: "Desde 1987" e "Nueva tradición" come una coppia di parole: tradizione e oggi nella stessa frase. Da noi: "Oggi come una volta", la frase loro.
   - Da non prendere: le foto inclinate a ventaglio, il titolo in maiuscolo nero pesante, il blocco dei cookie.
9. **The Olly** (theolly.it), panetteria e pasticceria, Como, dal 1956, Menzione d'onore 12/9/2024.
   - Mossa 1: la frase della casa in grande su un campo pieno, con il filetto verticale che lega un blocco all'altro. Da noi: il campo pieno è uno solo (pasticceria) e la frase grande è un titolo nel carattere del testo, sotto i 30 px quando supera le 30 parole.
   - Mossa 2: le schede dei negozi con indirizzo, telefono e tabella degli orari, giorni a sinistra e ore a destra. Da noi: "Orari" con Ufficio e Spaccio a sinistra e le ore a destra, in cifre tabellari.
   - Da non prendere: il sipario col timbro tondo, le parole che si colorano scorrendo, il testo rosso su rosso.

## 3. Carattere

- **Display: Besley** (Owen Earl, Indestructible Type; SIL Open Font License 1.1, Google Fonts, file variabile), peso 400, mai corsivo. È un Clarendon: la stessa famiglia di lettere della fascia RIZZI sull'etichetta del Bitter, del LEONE e della scritta RIZZI del vecchio marchio. Solo tre momenti: "Oggi come una volta" nell'apertura (166 px a 1440, 72 a 390), "Da 11 a 70 gradi" nella firma (171 px a 1440, 66 a 390, con i gradi delle bottiglie a 37 px), il telefono nei contatti (135 px a 1440, 51 a 390).
- **Testo: Excon** (Indian Type Foundry, Fontshare, ITF Free Font License 2.0), 400 e 500: un grottesco asciutto, il compagno classico di un Clarendon. Testo, `h2` di servizio, testata, didascalie, recapiti, piede.
- File in `sito-he/fonts/` (woff2 ufficiali, non modificati), licenze `OFL-Besley.txt` e `FFL-ITF.txt`.
- Nessuna etichetta sopra i titoli, nessun numero davanti alle sezioni, nessun corsivo; il maiuscolo non c'è.
- Registro: riga aggiunta a `_metodo/professionale/alto/REGISTRO-CARATTERI.md`. Besley ed Excon non sono in nessuna home della campagna né nelle liste di `_metodo/CARATTERI-E-SEGNALI-IA.md`. Escono Zodiak e Switzer della versione di oggi.

## 4. Colore (dalle etichette)

| Nome | Valore | Da dove | Dove |
|---|---|---|---|
| Carta | #F2EDE4 | la carta avorio delle etichette | fondo della pagina; il bianco delle foto diventa questo |
| Inchiostro | #1B1714 | il nero della scritta a pennello | testo, bottoni, piede; i neri delle foto finiscono qui |
| Blu etichetta | #1D2536 | la cornice del Bitter, il fondo del LEONE, il blu del vecchio marchio | **l'unico campo pieno: la pasticceria** |
| Rosso Bitter | #B3211E (5,7:1 sulla carta) | il rosso del Bitter e della fascia RIZZI | fuoco della tastiera, passaggio sul telefono e sui link, pressione dei bottoni |
| Grigio | #5E564E (6,2:1 sulla carta) | | didascalie, fonti |

## 5. Movimento

- **Gesto d'apertura, "dall'etichetta alla bottiglia"** (`data-he-scale`): la cornice parte sull'etichetta del Bitter accanto al motto (secondo giro: bordo alto sulla cima della "O" di "Oggi", bordo basso con il fondo del biglietto, bordo destro sul margine; ingrandimento circa 2,6 a 1440x900, la fascia RIZZI nel terzo alto e il tondo "casa fondata nel 1850" sotto il bordo), e scorrendo si allarga fino alla bottiglia intera: si scopre il liquore rosso rubino, il collo, il tappo, e arriva la didascalia "Bitter, 25% vol. «Liquore da aperitivo tradizionale padovano»". La cornice si misura sulla bottiglia come la impagina il CSS, nella pagina, prima che parta il kit (nessun lampo). Sul telefono nessun fissaggio: motto, bottiglia e mestiere in una composizione ferma.
- **Sostegno 1, i titoli**: il motto sale riga per riga all'apertura (`data-he-split data-he-subito`) e "Da 11 a 70 gradi" quando entra (due split su tre).
- **Sostegno 2, i tagli**: l'alcolato ambrato si scopre dal basso (`data-he-wipe="su"`). La foto di Maddalena e Alessandro e' tolta nel secondo giro.
- Testata che si nasconde scendendo da 900 px in su; sul telefono resta, con "Chiama 049 900 0053".
- Niente galleria orizzontale fissata, racconto, indice, prima e dopo, parallasse, nastro, sipario. La scala dei gradi è ferma: sul telefono si sfoglia di lato con il dito.
- L'apertura fissata usa `pinType: "transform"` (impostato prima di `he.js`), come Argenteria e Tacchificio: CLS 0.

## 6. Ritmo (ogni sezione ha uno scheletro diverso)

1. **Apertura, "Oggi come una volta"** (carta, a tutta altezza): manifesto. Il motto su due righe a sinistra, la bottiglia del Bitter alta 86% della finestra al 72% della larghezza, il mestiere e il telefono in basso a sinistra, la didascalia a destra della bottiglia.
2. **Laboratorio, "Facciamo tutto noi, dall'inizio alla fine."** (carta): a sinistra il dittico dell'alcolato (due foto uguali sulla stessa base), a destra il titolo loro (h2 di servizio, Excon 400, al massimo 44 px), la frase delle ricette dei fondatori e l'estrattore e l'essiccatore.
3. **Firma, "Da 11 a 70 gradi"** (carta): grafico a tutta larghezza. Otto bottiglie vere sul righello dei gradi, ciascuna sul suo grado (dominio da 8 a 42 sull'80% della larghezza, interruzione, 70 al 92%), con il grado in Besley e il nome sotto. Nessun prezzo, nessun bottone d'acquisto; il link al catalogo sta fuori dal grafico.
4. **Pasticceria** (blu etichetta, l'unico campo pieno): testo a sinistra (titolo, frase loro, tre famiglie in una riga ciascuna con i gusti chiusi, telefono e email), i quattro bottiglioni da laboratorio a destra, appoggiati sul bordo basso del campo.
5. **Chi siamo** (carta, due colonne, secondo giro): a sinistra la frase sui ricettari del fondatore a 28 px (una volta), a destra "Dal 14 dicembre 2022 Distilleria Rizzi prosegue con Maddalena e Alessandro" (oggi), lo spaccio del 29 settembre 2024 e i mobili della sartoria Vogue 80. Nessuna foto.
6. **Spaccio e contatti** (carta): il telefono in Besley a tutta misura, sotto tre colonne (indirizzo con la mappa, orari in tabella, email, cellulari e PEC) e la foto degli scaffali dello spaccio.
7. **Piede** (inchiostro): scritta a pennello chiara, link, social, dati legali, avvertenza sugli alcolici, Privacy, Cookie.

La sezione firma è la 3: un'idea (la gamma è una scala, dalle loro schede) con la prova fotografica (otto bottiglie vere, alla stessa scala, dal 100 cl al Pinalpe da 75 cl).

## 7. Foto

Riscaricate il 7/11/2026 dalla libreria media di WordPress (`wp-json/wp/v2/media`, 123 voci) in `assets/originali/` (fuori da git), provando per ogni voce il nome senza `-scaled` e senza il suffisso `-e<numero>` delle immagini ritagliate in WordPress. **Gli scontornati "piccoli" di `01-analisi.md` (alti 500 px) hanno l'originale grande**: Aperizzi 490x1884, Bitter classico 498x2010, Carciofo 765x2802, Leone 944x3767, Bayern 1024x3471, Old Manhattan 1083x4178, Harrington 1137x4322, Amaretto 1075x4283, Vodka in tanica 1286x1932; e le foto "-scaled" hanno l'originale da 4624x2084 e 2084x4624 (l'alcolato di sambuco). Il vecchio marchio col leone esiste solo a 392x153 e porta "casa fondata nel 1850": non è in pagina.

Trattamento unico (`_prova/he/script/immagini.py`): toni portati tra inchiostro e carta, nitidezza del telefono calmata (0,5 px prima della riduzione), grana fine cotta nei pixel; scontornati con il bordo stretto di 1 px, nessuna ombra aggiunta. Secondo giro: le bottiglie della scala hanno anche lo stesso tono (bianco neutro e livelli comuni) e lo stesso taglio piano dei tappi. Nessuna foto oltre 1,25 volte il file sugli schermi normali: l'etichetta all'inizio del gesto è a 1,02 a 1440x900 e a 1,20 a 1920x1080 (sul retina circa il doppio, quindi morbida); a fine gesto la bottiglia intera è sotto 0,5.
