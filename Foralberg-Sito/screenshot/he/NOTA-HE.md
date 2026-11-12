# Foralberg, home HE (5 novembre 2026, secondo giro)

Pagina: `sito-he/index.html`, con il kit copiato in `sito-he/kit/` (he.css e he.js identici a `_metodo/highend/kit/`, vendor senza Flip; le due eccezioni di questa pagina sono scritte nel suo `<style>`), caratteri in `sito-he/fonts/`, immagini WebP in `sito-he/img/`. La `sito/` di oggi non è toccata. Direzione artistica: `DIREZIONE-HE.md` (scritta prima del primo giro: dove dice altro, vale questa nota).

In questa cartella: `scorrimento-1440.mp4` e `scorrimento-390.mp4` (registrati con `_metodo/highend/kit/registra.mjs`, repository servito con `python3 -m http.server 8742`, ora simulata martedì 3/11/2026 alle 10.00 con `?ora=2026-11-03T10:00`), `foglio-1440.jpg` (35 fotogrammi) e `foglio-390.jpg` (31), i fotogrammi uno al secondo, `prima-schermata-1440.jpg` e `-390.jpg`, `riduci-movimento-1440-prima-schermata.jpg` e `-390`. Pagine intere ferme e prime schermate a 768, 1024 e 1920 in `_prova/he/prove/`; script delle prove e delle immagini in `_prova/he/script/` (`immagini.py` rifà tutte le foto, `controlli.mjs` le prove, `scala.mjs` la misura vera di ogni foto, `prima.mjs` le prime schermate, `catalogo_capitoli.py` la prova del catalogo per capitoli).

## Secondo giro: i cinque interventi del giudice (voto 7,4)

1. **Sezione firma (`#su-misura`)**. Tolti il logo ingrandito e il piatto a rilievo di p. 8 (smentiva "piatti bianchi lisci"). Ora: il titolo è l'h2 a 96 px con `data-he-split`, "La nostra firma viaggiava sul cassone del Lupetto. Sui vostri piatti può stare la vostra." (senza "Nel 1963"); sotto, il dittico 4:5 su 5+5 colonne (dalla 2 alla 11): a sinistra la firma dipinta sul cassone (`firma-cassone`, ritaglio 1590x1988 dalla foto d'archivio a 4205 px), a destra il piatto piano ovale Steelite in porcellana bianca liscia della p. 103, la pagina della personalizzazione ("dedicato esclusivamente ai piatti bianchi con superficie liscia"), ritagliato da `assets/originali/catalogo/estratte/p103-000.jpg` (1418x1366, la sua misura nel PDF) a 1049x1311. Didascalie "La nostra firma" e "Qui va la vostra" a 24 px, con la fonte sotto in piccolo. "Il vostro biglietto da visita? Un piatto su misura." è testo da 24 px sotto il piatto, con le tecniche e i due link. Resta l'unica sezione a colore pieno. Sul telefono il dittico resta in coppia, 169 px per foto.
2. **Un solo trattamento**. Tutte le foto, archivio e catalogo, passano per la stessa funzione (`bn()` in `immagini.py`): bianco e nero neutro, neri a 20, luci a 244, grana del kit (`.he-grana`) su ogni cornice, anche sulle stampe della storia che prima non l'avevano. Le foto del catalogo sono ritagliate strette sull'oggetto in 4:5 (indice, chi siamo, piatto). La copertina di "Oggi" è in bianco e nero con gli stessi punti ma senza allargare i toni (il blu diventa un grigio, la copertina resta riconoscibile): il primo blu pieno della pagina è la sezione firma. Misurato con `scala.mjs`: nessuna foto oltre 1,04 volte la sua larghezza nativa (la cartolina di via San Fermo a 1920); tutte le altre a 0,8 o meno.
3. **Storia (`#storia`)**. `.he-storia-media` su 8 colonne, alta `calc(100vh - testata - 6vh)`, foto intera e centrata in verticale (856 px a 1440 invece di 746, 1036 a 1920); i passi su 3 colonne dalla 10, 48 px sotto il titolo. Solo in questa pagina, sopra il kit: la foto cambia con un taglio netto (`transition:none; transform:none`), nessuna dissolvenza né ingrandimento. Ogni stampa ha una larghezza fissata dal suo rapporto (`--r`), così non c'è spostamento del layout quando arriva l'immagine. Tolti la foto della XXXVI Fiera (anno da confermare: 1953 sul sito, 1958 nel catalogo) e il passo del furgone al 1963 (anno e sede da confermare: il cassone porta "via Trieste 11"). Il 1953 resta nella frase sotto il titolo, senza foto. Passi: 1960, 1962, 1964, Oggi. Con riduci movimento ogni stampa sta accanto alla sua data, su 8+3 colonne.
4. **Progetti (`#progetti`)**. Tolti i gradini 01-04. Protagonista "Mandateci la planimetria" a 104 px; sotto, le fasi in una riga e i cinque punti di "Che cosa guardiamo" in due colonne; a destra il testo, "Allegatela alla richiesta" (apre il modulo su "Progetto o impianto") e "Chiamate 049 760955". Le fasi sono "ascolto e studio, progetto e rendering, installazione e collaudo, assistenza post vendita": "sopralluogo" non è nelle fonti (catalogo p. 5: "Dall'ascolto, studio e ricerca alla progettazione, render e disegno tecnico dell'area, fino all'installazione e alla gestione con assistenza post-vendita"), quindi non l'ho scritto.
5. **Testo e vincoli**.
   - Bottoni `.b` e varianti senza transizione: al passaggio si invertono di colpo (colore e filetto), solo dove c'è un puntatore (`@media (hover:hover)`), così sul telefono il tocco non lascia il bottone invertito; alla pressione un grigio acciaio netto. Tolta anche la transizione delle scelte del modulo.
   - "Showroom e orari" e l'h2 della PA sotto i 1100 px (dove salgono sopra il titolo) hanno la classe `sr-stretto`: nascosti alla vista, letti dai lettori di schermo. Nella PA, sotto i 1100, la frase sull'abilitazione viene prima dei portali, così la lista non resta senza contesto.
   - Solo il voi: "Il vostro biglietto da visita", "Chiamate", "Scegliete un file", "Preparate la richiesta", "Copiate il testo"; il bottone del menu dice sempre "Menu" (aperto: sottolineato e `aria-expanded`), il salto dice "Al contenuto principale". "La vostra idea" non c'è più perché i gradini sono tolti.
   - Tolti "Ci piace pensare di essere più di un semplice fornitore" (chi siamo ora è "Dal 1953 consulenti dell'ospitalità."), "Fatti sorprendere", "Sempre tutto sotto controllo" e "11 agenti e commerciali" (le cifre sono tre: 800 m², 30.000, 6.000).
   - Indirizzo nella prima schermata: sul telefono "via Cile 2, a Padova" nella riga sotto la foto è un link alle indicazioni di Google Maps; anche le due sedi sotto i bottoni aprono la mappa.
   - Catalogo per capitoli: **non usato**. qpdf e ghostscript non sono installati; ho diviso e ricompresso con pypdf (via i metadati XMP, foto ricampionate e ricompresse in JPEG). Esito, capitolo più grande (Porcellana, pp. 10-181) e totale dei 13 capitoli: 110 ppi 9,6 e 30,0 MB; 96 ppi 7,8 e 24,8 MB; 72 ppi 5,6 e 18,3 MB. La Porcellana non scende mai sotto 4 MB (solo testo e grafica vettoriale fanno 1,6 MB), quindi, come da regola, ogni riga apre il PDF intero alla sua pagina e la misura è scritta accanto: in testa all'elenco "Pagina, nel PDF intero (56 MB)", nella frase sopra e nei link "(PDF, 56 MB)". Nessun file in `sito-he/catalogo/`.
   - Sipario d'ingresso **tolto**: la firma vive nel dittico della sezione firma (quella vera, dipinta sul cassone), e la pagina non aspetta più 1,7 s. Il gesto d'apertura resta il titolo che sale e il furgone che si allarga a tutta pagina.

Ritocchi dopo aver guardato il nuovo foglio: le maschere dei titoli riga per riga tagliavano le discendenti (la g di "alberghiere" nella prima schermata): ora ogni riga ha 0,18 em di margine sotto; il titolo della firma andava a capo con "vostra." da sola a 1440 e 1920 (SplitText ignora lo spazio indivisibile): "stare la vostra." è tenuto insieme; i passi della storia hanno il testo in alto, così la data è a metà schermo quando cambia la foto; le righe dell'indice non restano blu dopo il tocco sul telefono.

## Idea

**Firmato Foralberg.** La firma corsiva del logo di oggi è la stessa dipinta a mano sul cassone dell'OM Lupetto 30 delle prime consegne, e sulla portiera dello stesso furgone ci sono già i capitoli del catalogo: "porcellane, cristallerie, posaterie, art. vari cucina". La pagina segue la firma: è dipinta sul furgone che riempie la pagina, dà il titolo all'indice del catalogo e nel culmine passa al cliente, accanto a un piatto bianco liscio, perché Foralberg personalizza i piatti con il marchio del locale (catalogo p. 103).

## Carattere e colore

- **Jost** (Indestructible Type, Google Fonts, SIL OFL 1.1) 400 e 500 per titoli, cifre e interfaccia; **Source Serif 4** (Adobe, Google Fonts, SIL OFL 1.1) per il testo. La firma è sempre il disegno del logo o la foto del cassone, mai un carattere. Niente corsivi, niente maiuscolo spaziato.
- Porcellana #F4F3EF (fondo), inchiostro #131415 (progetti, piede), blu #00719F pieno **solo sulla sezione firma** (bianco 5,4:1, fonti in #E6F1F7 4,7:1), acciaio #5D6166, verde #1C7A3D solo per "Aperto ora". Tutte le foto in bianco e nero: l'unico colore delle immagini è quello della pagina.

## Movimento

- **Apertura**: il titolo sale riga per riga (`data-he-split data-he-subito`), il furgone è incorniciato sulla cabina con la portiera "porcellane, cristallerie, posaterie, art. vari cucina" e scorrendo si allarga a tutta pagina (`data-he-scale`) fino alla firma sul cassone; entra la didascalia. Nessun sipario.
- **Sostegno**: titoli riga per riga su tre testi (apertura, chi siamo, firma); indice con anteprima ferma (`data-he-index`, sopra i 900 px); storia con la foto ferma e il taglio netto (`data-he-story`, quattro date). Testata che si nasconde scendendo (`data-he-header`).
- **Riduci movimento** (provato con `reducedMotion: 'reduce'` a 390, 768, 1024, 1440, 1920): apertura ferma con il furgone incorniciato e la didascalia, storia come serie di stampe con la data accanto, tutto il resto uguale. Pagina completa.
- Sotto i 900 px: nessuna sezione fissata; la storia mette ogni stampa sopra la sua data; l'indice ha una miniatura per riga e non carica le anteprime grandi.

## Sezioni (scheletri diversi)

1. **Apertura**: titolo a 147 px, la riga sul mestiere con via Cile 2 che apre la mappa, i bottoni, le due sedi con lo stato; la cornice sul furgone che diventa la pagina.
2. **Chi siamo**: "Dal 1953 consulenti dell'ospitalità." su sette colonne, testo spostato, foto 4:5 della p. 4 più in basso; tre cifre su filetto.
3. **Indice del catalogo**: le quattro voci della portiera come titolo; 14 righe (capitolo, marchi, pagina del PDF intero da 56 MB) con l'anteprima ferma in bianco e nero.
4. **Progetti** (inchiostro): "Mandateci la planimetria" a 104 px, le fasi, i cinque punti in due colonne, testo e bottoni a destra.
5. **Storia**: stampa intera su 8 colonne, date a 104 px su 3 colonne: 1960, 1962, 1964, Oggi.
6. **Sezione firma, culmine** (blu pieno): titolo a 96 px, dittico "La nostra firma" e "Qui va la vostra", il biglietto da visita a 24 px.
7. **Showroom e orari**: "via Cile 2" e "via Vigonovese 93" a 104 px (link alle indicazioni), stato, orari, bottoni.
8. **Richiesta**: il modulo della versione professionale.
9. **Acquisti PA**: sei portali, la frase sull'abilitazione, "Chiedete l'abilitazione".
10. **Piede** (inchiostro): logo bianco, dati legali, recapiti, Privacy, Cookie, Note legali.

Funzioni mantenute: 12 link `tel:`, 6 `mailto:`, 7 link alle indicazioni su Google Maps (prima 4), 18 link ai PDF col peso scritto, stato aperto o chiuso sull'ora di Roma con i festivi, La Vetrinetta, modulo, dati legali, JSON-LD dei due negozi.

## Foto usate

| In pagina | File originale (in `assets/originali/`) | Ritaglio nativo | Mostrata a 1440 / 1920 |
|---|---|---|---|
| Apertura, il furgone | `storia_camion2_foralberg.jpg` | 4205x3208 | 1440 / 1920 |
| Firma, "La nostra firma" | stesso file, il cassone | 1590x1988 | 526 / 637 |
| Firma, "Qui va la vostra" | Catalogo p. 103, `estratte/p103-000.jpg` | 1049x1311 | 526 / 637 |
| Storia 1960, 38a Fiera | `storia_fiera_1_foralberg.jpg` | 4059x3012 | 856 / 1036 |
| Storia 1962, via San Fermo | `storia_via_san__fermo.jpg` (cartolina) | 1000x705 | 856 / 1036 |
| Storia 1964, 42a Fiera | `storia_fiera_2_foralberg.jpg` | 4088x2943 | 856 / 1036 |
| Storia oggi, copertina | `00__FB_CP25__COMPLETO__LowRes-1.jpg` | 2480x3507 | 493 / 613 |
| Chi siamo, piatto ovale | Catalogo p. 4 | 1262x1578 | 416 / 504 |
| Indice, 14 anteprime 4:5 | Catalogo pp. 91, 103, 182, 232, 290, 352, 391, 400, 412, 448, 464, 470, 494, 498 | da 794 a 1990 px di lato | 526 / 637 |

Tolti da `sito-he/img/`: `fiera36-*`, `furgone-firma-*` (sostituito dal 4:5 `firma-cassone-*`), `piatto-marmo-*`, le foto del catalogo a colori. Nessuna foto di repertorio, nessuna immagine generata.

## Misure e prove

- Caratteri a 1440: 147, 104 (anni, indirizzi, planimetria), 96 (firma), 63, 36, 24, 19, 16, 14. A 390: 57, 46, 35, 29, 22, 19, 17, 16, 15, 14.
- Altezza: 14.402 px a 1440 (con l'apertura fissata), 15.079 a 390.
- **Peso al primo caricamento** (rete a riposo, Playwright): 1.093 KB a 1440 (soglia 2,5 MB), 558 KB a 390 (soglia 1,5 MB); 621 a 768, 1.062 a 1024, 1.136 a 1920. Foto d'apertura precaricata, Jost precaricato, tutte le immagini con larghezza e altezza; nessuno spostamento del layout (altezze delle sezioni uguali prima e dopo il caricamento delle foto pigre, provato a 1440 con e senza movimento, a 390 con il movimento e a 1024 senza).
- **Prove della sezione 6**: a 390, 768, 1024, 1440 e 1920, con e senza riduci movimento, scorrimento orizzontale 0 e nessun errore di script; con riduci movimento la pagina è completa (`_prova/he/prove/riduci-1440-intera.jpg` e `-390`). Nessun carattere U+2014 nella pagina, negli script e in questa nota.

## Problemi aperti

- **Foto del presente**: la distanza che resta dipende soprattutto da qui. Il presente è raccontato con le foto del catalogo (dei fornitori, ora almeno tutte uguali di trattamento) e con la copertina in grigio, che in "Oggi" sembra un cartoncino. In ordine di valore: un piatto bianco personalizzato con il marchio di un cliente vero, dall'alto (sostituisce la p. 103 in "Qui va la vostra" ed è la prova dell'idea); lo showroom di via Cile frontale come gli stand in fiera (per "Oggi" e per la sezione dove); una tavola apparecchiata nello showroom (per chi siamo); le persone, il magazzino, un furgone di oggi con la firma se c'è.
- **Date**: in pagina restano solo quelle della riga del tempo del sito non contraddette (1953, 1959, 1960, 1962, 1964, 1980, 2008). Da chiedere: anno della 36a Fiera, anno del furgone, ordine delle sedi (la 38a Fiera, 1960, mostra già "via S. Fermo 16"; il sito dà via San Fermo nel 1962; il cassone porta "via Trieste 11").
- **Catalogo da 56 MB**: per capitoli non sta nei limiti (vedi sopra). Serve dall'azienda un'esportazione leggera per capitolo da InDesign (Porcellana in due parti) o un catalogo sfogliabile.
- **Diritti dell'archivio** ("Foto Giordani") e originali a piena risoluzione; permesso d'uso delle foto del catalogo, molte dei fornitori.
- **Modulo**: compone un'email e mostra il testo da copiare; va collegato a un servizio che riceva i file (LEGGIMI).
- **Link legali**: puntano alle pagine di oggi su foralberg.it; le Note legali citano ancora "Selco".
- **Numeri**: "oltre 30.000 articoli" e "più di 6.000 in pronta consegna" sono del sito e del catalogo; tolto "11 agenti", in conflitto con LinkedIn e Atoka.
- **Righe senza marchio** nell'indice (Melamina, Pasticceria, Pizzeria, Stoccaggio, Piccoli macchinari): i marchi vanno chiesti, non inventati.
- **`DIREZIONE-HE.md`** descrive ancora il sipario e il catalogo a colore smorzato: non l'ho riscritta, vale questa nota.
