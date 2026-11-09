# Edera Country House: analisi del sito di oggi

Sito analizzato: https://ederacountry.it, scaricato il 9 novembre 2026 in `originale/`.

- Server: nginx su Plesk (`x-powered-by: PleskLin`). La home è del 6 novembre 2026 (`last-modified`).
- Non ci sono `robots.txt`, `sitemap.xml` né favicon: rispondono 404. Le cartelle `img/` e `fonts/` non sono elencabili (403).
- Statistiche, mappe incorporate, Google Fonts, servizi esterni: nessuno. Tutto è ospitato sul sito.

## La copia in `originale/`

| File | Peso | Note |
|---|---|---|
| `index.html` | 43 KB | one page; CSS e JS dentro il file |
| `privacy.html` | 20 KB | informativa, `noindex` |
| `cookie.html` | 4,5 KB | pagina cookie, `noindex` |
| `servizi-aggiuntivi.pdf` | 175 KB | una pagina: spazi, dotazioni, servizi extra con prezzi |
| `fonts/` | 4 file, 285 KB | Newsreader (latin, latin-ext), Jost, Bodoni Moda |
| `img/` | 20 file WebP, 1,9 MB | tutte le misure di `src`, `srcset` e del `preload` |

La copia servita in locale (`python3 -m http.server`) è identica al sito pubblicato: le schermate a pagina intera a 390 e a 1440 px hanno **0 pixel diversi**.

Foto (larghezza x altezza): apertura 1500x1001, 1100x734, 760x507; apertura per il telefono 750x1001, 520x694; casa 1250x1000, 900x720, 620x496; meeting 573x429; celebrazioni e teambuilding 900x675, 620x465; piscina-sera 1093x1367, 760x951; sala 1500x1000, 1100x733, 760x507; giardino 800x1001, 560x701.

## Sezioni, testi e misure

Altezze delle sezioni (px), misurate nel browser:

| Sezione | ancora | 390 | 768 | 1440 |
|---|---|---|---|---|
| Testata (sopra l'apertura, non fissa) | | 76 | 96 | 96 |
| Apertura | | 860 | 900 | 900 |
| La location | `#location` | 1300 | 1259 | 908 |
| Eventi (i formati) | `#eventi` | 1609 | 1992 | 839 |
| Gallery | `#gallery` | 1498 | 2415 | 1214 |
| Fascia verde | | 455 | 405 | 388 |
| Preventivo flash | `#preventivo` | 2575 | 2093 | 1608 |
| Domande frequenti | `#faq` | 975 | 738 | 778 |
| Contatti | `#contatti` | 835 | 674 | 624 |
| Piede | | 988 | 733 | 381 |
| **Pagina intera** | | **11095** | **11208** | **7641** |

Griglia: colonna di `min(1200px, 100% - 2 x gutter)`, gutter `clamp(20px, 4vw, 56px)`. Sezioni con `padding: clamp(80px, 10vw, 136px) 0`; fondo alternato crema `#f5f2eb` e carta `#faf8f3`. Punti di rottura: 1400 (numeri di sezione 01-06 a sinistra, solo da 1400), 1080, 900, 760, 360.

1. **Apertura**: foto a tutta pagina (`<picture>`: dal telefono una versione verticale, sotto 760 px), alta `clamp(660px, 100svh, 920px)` (sul telefono `clamp(620px, 100svh, 860px)`), con tre sfumature scure sopra.
   - Titolo h1 "Gli eventi / che lasciano il segno." in due righe (due `<span>` a blocco; da 761 px non vanno a capo), `clamp(48px, 5.9vw, 86px)`, peso 300.
   - Sottotitolo "Un contesto distintivo ad Albettone, nel Vicentino, per incontri aziendali, convention, team building e serate da ricordare."
   - Bottoni "Calcola il tuo preventivo" (pieno crema) e "Scopri la location" (testo sottolineato).
   - Riga in basso: "Albettone · Vicenza" e "Rustico, serra, piscina, spazio esterno".
2. **La location** (`#location`): "Il luogo giusto per dare spazio alle idee.", tre paragrafi, l'elenco dei quattro spazi con la capienza (Rustico 50, Serra 70, Piscina 30 "anche mezza giornata", Spazio esterno 120), la foto del giardino la sera con didascalia. Due colonne; la foto scende di `clamp(0px, 9vw, 150px)`.
3. **Eventi** (`#eventi`): "Un format per ogni occasione." e tre schede con foto 4:3 (3:2 sotto 900 px): Meeting & convention, Celebrazioni, Team building.
4. **Gallery** (`#gallery`): "Ogni spazio ha la sua atmosfera.", tre foto sfalsate su 12 colonne (piscina la sera 4:5 a sinistra, sala 3:2 e giardino 4:5 a destra), con didascalia.
5. **Fascia verde**: "La tua idea parte da qui.", paragrafo, riga "Meeting · Convention · Team building · Celebrazioni", bottone "Vai al preventivo flash ↓".
6. **Preventivo flash** (`#preventivo`): "Una prima stima, in pochi passaggi." e il calcolatore (sotto).
7. **Domande frequenti** (`#faq`): catering libero, piscina (massimo 30 persone, bagnino con brevetto obbligatorio), parcheggio privato.
8. **Contatti** (`#contatti`): "Il prossimo evento può iniziare qui.", scheda con indirizzo (link a Google Maps e "Indicazioni stradali ↗"), email, telefono, bottone "Richiedi una stima".
9. **Piede**: marchio, descrizione, indirizzo; tre colonne di link (La location, Eventi, Contatti); riga legale "© 2026 Edera Country House · Via Palù Massara, 10 · Albettone (VI) · C.F. e P.IVA 04722030287" (l'anno lo aggiorna lo script), link a Informativa privacy e Cookie.

Dati: Via Palù Massara, 10, Albettone (VI); edera@ederacountry.it; 349 473 1515 (`tel:+393494731515`); titolare EGO ITALY srl, Via dell'Industria 1, Grisignano di Zocco (VI), P.IVA 04722030287.

Titolo della home: "Edera Country House | Eventi aziendali ad Albettone, Vicenza". Descrizione: "Edera Country House ad Albettone, Vicenza: location per eventi aziendali, meeting, convention, cene e team building." Precarica `img/apertura-1500.webp` da 761 px.

## Colori e caratteri

Home (variabili CSS): inchiostro `#17251f`, inchiostro tenue `#4f5b54`, verde `#294b3b`, verde scuro `#1d3529`, notte `#12201a`, muschio `#75866a`, crema `#f5f2eb`, carta `#faf8f3`, sabbia `#e5dfd2`, filo `#d9d2c3`, oro `#c3a66b`, oro chiaro `#d6bf8c`, oro scuro `#7f6534`.

Pagine legali (un altro stile, probabilmente rimasto da una versione precedente): calcare `#ECE6DC`, sabbia `#E2D9CB`, corteccia `#4A3B2C` e `#6B5A48`, oliva `#5E5D48`, filo `#877866`.

| Carattere | Uso | File | Licenza |
|---|---|---|---|
| Newsreader (Production Type) | titoli della home, variabile 200-800 con dimensione ottica | `newsreader-latin.woff2`, `newsreader-latin-ext.woff2` | SIL Open Font License 1.1 |
| Jost (Indestructible Type) | testo di tutte le pagine, variabile 100-900 | `jost.woff2` | SIL Open Font License 1.1 |
| Bodoni Moda (Indestructible Type) | titoli delle pagine legali, variabile 400-900 | `bodoni-moda.woff2` | SIL Open Font License 1.1 |

La licenza OFL è scritta nei file stessi (campo licenza del font) e permette di ospitarli nel tema: nel tema c'è `assets/fonts/LICENZE.txt`.

## Il calcolatore "Preventivo flash"

Tutto nel browser, nello script in fondo a `index.html`. Nessun dato va al server.

- **Spazi**: caselle Rustico (già spuntato), Serra, Piscina, Spazio esterno. Non si possono togliere tutte: l'ultima si rispunta da sola.
- **Prezzo di ogni spazio**, con `n` partecipanti:
  - Rustico: `400 + max(0, min(n, 50) - 20) x 15`
  - Serra: `250 + max(0, min(n, 70) - 20) x 5`
  - Piscina: 400 euro la giornata intera, 300 la mezza (non dipende dalle persone)
  - Spazio esterno: `350 + max(0, min(n, 120) - 20) x 2,5`
- **Partecipanti**: il massimo è la somma delle capienze degli spazi scelti (scritto sotto il campo, "Con gli spazi scelti, fino a N persone."). Un numero più alto torna al massimo, anche nel campo. Campo vuoto o 0: la stima usa 20 e scrive "Partecipanti (esempio)". Un numero negativo vale 1. I decimali passano (25,5 persone: Rustico 482,5 euro).
- **Durata**: giornata intera (valore 1.5) o mezza (valore 1). La mezza si può scegliere solo se c'è la piscina; togliendo la piscina torna la giornata intera. La nota sotto cambia di conseguenza.
- **Stagione**: con una data da ottobre a marzo (mese 10, 11, 12, 1, 2, 3) il **primo spazio scelto** nell'ordine della pagina costa 125 euro in più. Senza data niente supplemento.
- **Totale**: somma delle voci, in euro con `Intl.NumberFormat('it-IT')`, senza decimali se non servono e senza separatore delle migliaia sotto 10.000 ("1350 €", "1137,5 €").
- **Elenco della stima**: una riga per spazio con il suo prezzo, poi partecipanti e durata.
- Casi limite visti nel codice: lo stesso supplemento va sul primo spazio anche se è la piscina; gli spazi diversi dalla piscina non cambiano prezzo con la mezza giornata; il valore del campo partecipanti non è arrotondato.

## Dove finisce la richiesta

**Nessun modulo viene inviato al sito.** "Prepara la richiesta" controlla che ci siano i partecipanti e il consenso privacy (messaggi del browser: "Indica il numero di partecipanti.", "Serve il consenso per inviare la richiesta."), poi mostra un riepilogo e due bottoni:
- "Invia per email": un link `mailto:edera@ederacountry.it` con oggetto "Richiesta di preventivo, <azienda>" e il riepilogo nel testo; la mail parte dal programma di posta di chi scrive.
- "Copia il riepilogo": copia il testo negli appunti.

Per questo in WordPress non serve Contact Form 7: il calcolatore replica lo stesso mailto.

## Banner cookie

Non c'è, e la pagina cookie lo dice: "Questo sito non utilizza cookie. Per questo non è presente un banner e non Le viene chiesto alcun consenso." Anche in WordPress il sito pubblico non usa cookie (WordPress li mette solo a chi entra nel pannello), quindi il banner resta assente.

## Testata e menu sul telefono

- Testata in `position: absolute` sopra la foto d'apertura, testo bianco, alta 96 px (76 sotto 760 px). Scorre via con la pagina: non è fissa.
- Da 761 px: voci La location, Eventi, Gallery, Contatti e il bottone "Preventivo flash ↗".
- Fino a 760 px: solo il marchio e il bottone "Menu". Il menu è un pannello a tutto schermo verde scuro (`role="dialog"`), voci in Newsreader 34 px, indirizzo, email e telefono in fondo; si chiude con "Chiudi", con Esc o scegliendo una voce.
- Fino a 760 px c'è anche una **barra fissa in basso** con "Preventivo flash" e "Chiama": compare dopo l'apertura e si nasconde quando sono a schermo il preventivo o i contatti (IntersectionObserver, senza animazioni).

## Pagine legali

`privacy.html` e `cookie.html`: testata semplice (marchio in Bodoni Moda e "Tornare al sito"), etichetta "Note legali", titolo, riquadro sabbia iniziale, testo su una colonna di 760 px, data "Ultimo aggiornamento: 6 novembre 2026.", piede con la ragione sociale. La privacy spiega anche il mailto del preventivo.

## Note per il passaggio

- Nel CSS c'è una regola non usata dall'HTML (`.spazi-nota`): portata così com'è.
- Il campo data mostra il formato della lingua del browser (`mm/dd/yyyy` nel browser di prova): è il comportamento normale dei campi data.
