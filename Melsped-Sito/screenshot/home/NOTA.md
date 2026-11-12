# Melsped, home finale "Il piazzale"

Pagina: `sito/index.html`. Si rifà con `bash _prova/script/build_finale.sh`. Altezza a 1440: 4.960 px, piede compreso (a 390: 4.942 px). L'altezza resta uguale con tutte e quattro le schede del selettore.

## L'idea

Un solo semirimorchio bianco, fermo su un piazzale di cemento chiaro sotto un cielo sereno, e sopra il loro titolo, "Abbatti i confini", su una riga sola da un margine all'altro.
- Il titolo è largo come il mezzo è lungo: Archivo al 118 % di larghezza, la scritta piatta di una fiancata. La coda del rimorchio finisce sul margine destro, come la "i" finale.
- Il cemento della foto diventa il fondo della pagina (#EDEAE4): tutte le sezioni stanno sul piazzale.
- Il giallo del logo è l'unico accento: il bottone del telefono, la voce scelta del selettore, i tre paesi dell'Est.

Con il nome di un concorrente la pagina non regge, già dalla prima schermata: sotto "Abbatti i confini" la riga dà un nome ai confini, "Da Saonara verso Ungheria, Bulgaria e Romania, e in tutta Europa, dal 1975", con i tre paesi dell'Est (le loro linee "estremamente enfatizzate") nel campo giallo del logo, come più sotto nell'elenco delle linee dirette. Poi le definizioni di groupage e Intrastat, viale Veneto e i recapiti.

## Le prime due schermate

1. **Apertura** (ripensata rispetto al prototipo A, nella stessa direzione).
   - "Abbatti i confini" in Archivo 500 a 170 px nel cielo, allineato a 64 px.
   - Sotto, a 23 px, la riga "Da Saonara verso Ungheria, Bulgaria e Romania, e in tutta Europa, dal 1975", con i tre paesi in giallo.
   - La foto è raddrizzata (il fotografo l'aveva inclinata di 5,5 gradi), così il mezzo e il titolo sono due fasce orizzontali parallele.
   - Sul cemento: la riga su chi sono, il bottone giallo "Chiamate lo 049 879 1919" e l'email.
   - La foto parte dall'originale a 4240 px: ritoccata lì, poi ridotta, quindi nitida a 1440 e a 2880 per gli schermi retina.
   - A 390 il titolo va su due righe a 80 px sopra il camion, che esce dal bordo destro; il cielo è allungato con PIL perché titolo e firma ci stiano. A 1920 c'è un taglio più largo, a 1024 uno con più cielo.
2. **Chi siamo**: una frase grande sul mestiere ("Organizziamo la spedizione e facciamo le pratiche...") che chiude con la prova, "Dal 1975, con un magazzino di oltre 1.400 m² a Saonara", poi la riga sui partner. Niente fila di fatti in colonne.
3. Poi il selettore Strada, Aereo, Mare, Dogana; le linee dirette; la chiusura e il piede.

## Caratteri e colori

- **Archivo** (Omnibus-Type, Google Fonts, SIL Open Font License 1.1), una famiglia sola, file variabili woff2 serviti da `sito/fonts/` (licenza in `sito/fonts/OFL.txt`).
  - L'asse della larghezza fa i ruoli: 118 % peso 500 per apertura, voci del selettore, paesi e frase di chiusura; 108-112 % per la frase di "Chi siamo", il telefono e il bottone; 100 % peso 400 per il testo.
  - Spaziatura da -0,02 a -0,035em sui titoli grandi. Cifre tabellari per telefono, fax, m², anni e dati societari.
  - Riferimenti (sez. 7 dell'analisi):
    - Gander & White, per l'anno di fondazione dato come firma sotto un titolo enorme;
    - Momart, per un solo oggetto vero in luce di giorno;
    - Forto, per il titolo corto su fondo chiaro che regge identico a 390;
    - Kuehne+Nagel, per i modi di spedire come parole su una riga.
  - Niente monospazio, niente corsivo.
- **Colori**:
  - cemento #EDEAE4 (fondo) e #E3DED5 (piede);
  - asfalto #1D1E20 per il testo (13,9:1);
  - #15191C per i titoletti del piede (13,2:1);
  - grigio #5E5B55 per le legende (5,6:1 sul fondo, 5,1:1 sul piede);
  - #77736C solo per le voci grandi non scelte del selettore (3,9:1, testo grande);
  - giallo del logo #F7CF0A sempre dietro testo scuro (11:1).

## Interazione

Un gesto solo: il selettore dei modi di spedire. Le parole grandi Strada, Aereo, Mare, Dogana sono un vero `tablist`.
- La voce scelta prende il campo giallo. Cambiano di netto, senza dissolvenze, la foto a tutta larghezza (12:5; 3:2 da 600 a 820 px; 4:5 sotto i 600), il titolo, due righe dai loro testi e da due a quattro voci brevi.
- I quattro pannelli stanno nella stessa cella della griglia: cambiando scheda la pagina non salta.
- Nella voce Groupage c'è la citazione delle loro note: «riunire e raggruppare piccole partite provenienti da mittenti diversi». Nella voce Intrastat c'è «l'elenco riepilogativo degli acquisti e delle cessioni intracomunitarie».
- Si usa con il clic, con il dito e con la tastiera (frecce, Home, Fine), provato con `_prova/script/prova_tastiera.mjs`.
- Le transizioni (0,12 s) ci sono solo sul colore delle voci e del bottone, che al passaggio passa da giallo su scuro a scuro su giallo, senza sbiadire.
- Il menu a 390 è un bottone con `aria-expanded`. Nel piede, sotto i 640 px, le tre colonne sono una fisarmonica con veri bottoni (`aria-expanded`, "+" disegnato in CSS); senza script le liste restano aperte.

## Chiusura e piede

- **Chiusura**, con il testo a sinistra e la foto a destra fino al bordo:
  - la frase è "Le esigenze del cliente al primo posto", la seconda metà del titolo del loro profilo, che chiude il cerchio con "Abbatti i confini";
  - i recapiti stanno a 48 px sotto la frase: il telefono grande con `tel:`, l'email con `mailto:`, l'indirizzo con "apri la mappa", e il fax in piccolo;
  - la foto è una fila di bancali filmati nella luce delle finestre, la merce pronta a partire, in 4:3, con il blocco di testo centrato in verticale. È un soggetto diverso da tutti i modi del selettore.
- **Piede**:
  - il logo SVG a 150 px, tagliato sopra la riga "SPEDIZIONI INTERNAZIONALI", che a quella misura sarebbe illeggibile, e una riga su chi sono;
  - tre colonne sulla griglia: Servizi (Strada e groupage, Est Europa, Aereo, Mare, Dogana e Intrastat, Logistica e magazzino), Azienda (Chi siamo, Paesi serviti, English), Contatti (telefono, email, PEC, mappa e per ultimo LinkedIn, l'unico social verificato);
  - in fondo la riga legale (ragione sociale, P.IVA e C.F., REA, capitale sociale), Privacy e Cookie, e una riga sola "Foto indicative, da sostituire con le foto di Melsped" al posto delle sei legende di prima.
- **Niente newsletter**: Melsped è uno spedizioniere B2B senza fiere, cataloghi, collezioni né clienti privati, e le sole notizie del sito sono cronache di pallavolo del 2012.

## Foto: origine e licenza

Tutte segnaposto Unsplash, licenza Unsplash (uso commerciale libero), verificata sulla pagina di ogni foto. Nessuna è generata dall'IA e nessuna è usata in altre home della campagna (controllato sui `CREDITI.md` di tutte le cartelle). Ritocchi in `assets/CREDITI.md`.

| Dove | Foto | Ritocchi |
|---|---|---|
| Apertura | Dextar Studio `2wpx8Bl0mwM`, originale 4240 px | ritoccata sull'originale e raddrizzata: lamelle della calandra ricostruite al posto della stella, tolte le scritte di visiera, cabina, porta e la sigla "FRC" del rimorchio (lamiera ricostruita riga per riga), parasole ciano portato a vetro scuro, catarifrangente fucsia sostituito dal telaio; cielo schiarito, il cemento sfuma nella pagina |
| Strada | Matthew Jackson `SJGC3NNOqU4` | coperti due marchi sui sigillanti |
| Aereo | Peaky_82 `PEf3deR3l_U` | coperti i marchi sui motori e sulla scaletta |
| Mare | Venti Views `1cqIcrWFQBI` | nessun ritocco di contenuto |
| Dogana | Craftsman Concrete Floors `hnMqVv0EkRc` | spenti i cavi fucsia del soffitto |
| Chiusura | Zemos `qHo65Xyzcvo` | taglio senza la parte scura del tetto |

Trattamento comune ai modi e alla chiusura, fatto con PIL: ombre sollevate, saturazione dal 50 al 72 %, bianco appena caldo e croma dei blu e dei ciano abbassato, così cielo, mare e capannoni stanno nella stessa luce (foglio di controllo `quattro-modi.png`, rigenerato da `finale_img.py` e cancellato da `build_finale.sh` dopo averlo guardato). WebP in più larghezze con `srcset`. Il brief per rifarle dal vero è nel `LEGGIMI.md`.

## Cosa è cambiato nella rifinitura (dopo il giudizio cieco)

- **Prima schermata**: la firma sotto il titolo ora dà un nome ai confini con i loro dati e il giallo del logo (bloccante del giudice).
- **Foto d'apertura**: rifatta dall'originale a 4240 px, ritocchi rifatti e controllati al 200 % su tutti i tagli; nitidezza leggera dopo la riduzione.
- **Selettore**: Aereo e Mare portati nella luce di Strada; Dogana cambiata (via il magazzino affollato sotto il neon, ora un capannone chiaro e vuoto); pannelli impilati nella stessa cella, così l'altezza non cambia; a 768 la foto è in 3:2 (alta 512 px), il 4:5 resta sotto i 600 px.
- **Chiusura**: via le baie B9 e B10, che ripetevano Strada; ora i bancali filmati.
- **Testi**: tolta la voce "Dove" da Aereo e Mare, "mondo industrializzato" resta solo sotto i paesi; "Imbarchi, sbarchi e operazioni doganali"; tolta la fila dei tre fatti di "Chi siamo" (1975 e 1.400 m² ora chiudono il paragrafo grande); "Est Europa" non si ripete più nei fatti né in Strada (ora "Fuori UE").
- **Piede**: tre colonne invece di quattro, LinkedIn come ultima voce di Contatti, "Contatti" tolto da Azienda; a 390 un solo filetto sotto la fisarmonica.
- **Legende**: le sei "Foto indicativa" tolte, una riga sola nel piede.
- **Tocco**: tutti i bersagli a 390 alti almeno 44 px (Privacy, Cookie, email, mappa, telefono in testata, voci del selettore e del piede).

## Controlli

- **Segnali da IA** (`segnali.sh` del kit, a 1440): 0 soglie bloccanti su 10 e 0 da guardare su 8.
  - Foto al 37,4 % della pagina, Archivo al 100 %, monospazio allo 0 %.
  - 1 filetto (sopra la riga legale), nessuna freccia, nessuna etichetta maiuscola, nessuna fila di numeri con etichetta oltre a una.
  - 2 fasce di fondo (la pagina e il piede), date: 1975.
- **Ai divieti**, guardando gli screenshot a pezzi: niente gradienti viola, badge, card, tre box con icona, Lucide, vetro, dissolvenze o effetti sul cursore. Nessun U+2014 nella pagina, nel LEGGIMI, nei CREDITI né in questa nota (controllo in `build_finale.sh`, solo sui file di testo).
- **Larghezze** guardate a pezzi: 320, 390, 768, 1024, 1440 e 1920. `scrollWidth` uguale a `innerWidth` a 320, 360, 375, 390, 414, 480, 600, 700, 768, 820, 900, 1024, 1180, 1280, 1366, 1440, 1600, 1920 e 2560 (`controlli_finali.mjs`).
- **Interazione**: selettore con clic, tocco (Dogana a 390) e tastiera (frecce, Home, Fine, con il fuoco che segue la scheda); fisarmonica del piede con tocco, Invio e spazio (`prova_tastiera.mjs`). Altezza della pagina uguale con le quattro schede a tutte le larghezze.
- **Collegamenti**: `tel:+390498791919`, `mailto:info@melsped.it`, `mailto:melsped@pec.it`, la mappa Google sulle coordinate del loro sito (45.381175, 11.957872).
- **Contrasti AA**: testo #1D1E20 sul cemento 13,9:1; grigio #5E5B55 5,6:1; testo scuro sul giallo 11:1; la riga sotto il titolo è in #1D1E20 sul cielo chiaro.
- **Immagini**: `controlla_img.py` verifica che ogni immagine citata esista e toglie quelle non usate. 44 file in `sito/img/`, 3,9 MB in tutto. La pagina a 1440 carica 480 kB di immagini, comprese le quattro foto del selettore (a 390: 320 kB); sugli schermi retina l'apertura sale al taglio da 2880 px.
