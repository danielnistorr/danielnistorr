# Melsped, home finale "Il piazzale"

Pagina: `sito/index.html`. Si rifà con `bash _prova/script/build_finale.sh`. Altezza a 1440: 5.065 px, piede compreso (a 390: 5.328 px).

## L'idea

Un solo semirimorchio bianco, fermo su un piazzale di cemento chiaro sotto un cielo sereno, e sopra il loro titolo, "Abbatti i confini", su una riga sola da un margine all'altro.
- Il titolo è largo come il mezzo è lungo: Archivo al 118 % di larghezza, la scritta piatta di una fiancata. La coda del rimorchio finisce sul margine destro, come la "i" finale.
- Il cemento della foto diventa il fondo della pagina (#EDEAE4): tutte le sezioni stanno sul piazzale.
- Il giallo del logo è l'unico accento: il bottone del telefono, la voce scelta del selettore, i tre paesi dell'Est.

Con il nome di un concorrente la pagina non regge: il titolo, l'elenco delle linee dirette con l'Est in giallo, le definizioni di groupage e Intrastat e i recapiti sono di Melsped.

## Le prime due schermate

1. **Apertura** (ripensata rispetto al prototipo A, nella stessa direzione).
   - "Abbatti i confini" in Archivo 500 a 170 px nel cielo, allineato a 64 px.
   - Sotto, la firma "Spedizioni internazionali da Saonara, dal 1975" in grigio scuro.
   - La foto è raddrizzata (il fotografo l'aveva inclinata di 5,5 gradi), così il mezzo e il titolo sono due fasce orizzontali parallele.
   - Sul cemento: la riga su chi sono, il bottone giallo "Chiamate lo 049 879 1919" e l'email. "Foto indicativa" in basso a destra, a 12 px.
   - A 390 il titolo va su due righe a 80 px sopra il camion, che esce dal bordo destro; il cielo è allungato con PIL perché titolo e firma ci stiano. A 1920 c'è un taglio più largo, a 1024 uno con più cielo.
2. **Chi siamo**: una frase grande sul mestiere ("Organizziamo la spedizione e facciamo le pratiche..."), poi la riga sui partner e tre fatti: 1975, 1.400 m², Est Europa.
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
  - #3E4143 per la firma sul cielo (da 5,1:1 in su);
  - #77736C solo per le voci grandi non scelte del selettore (3,9:1, testo grande);
  - giallo del logo #F7CF0A sempre dietro testo scuro (11:1).

## Interazione

Un gesto solo: il selettore dei modi di spedire. Le parole grandi Strada, Aereo, Mare, Dogana sono un vero `tablist`.
- La voce scelta prende il campo giallo. Cambiano di netto, senza dissolvenze, la foto a tutta larghezza (12:5, a 390 in 4:5), il titolo, due righe dai loro testi e quattro voci brevi.
- Nella voce Groupage c'è la citazione delle loro note: «riunire e raggruppare piccole partite provenienti da mittenti diversi». Nella voce Intrastat c'è «l'elenco riepilogativo degli acquisti e delle cessioni intracomunitarie».
- Si usa con il clic, con il dito e con la tastiera (frecce, Home, Fine), provato con `_prova/script/prova_tastiera.mjs`.
- Le transizioni (0,12 s) ci sono solo sul colore delle voci e del bottone, che al passaggio passa da giallo su scuro a scuro su giallo, senza sbiadire.
- Il menu a 390 è un bottone con `aria-expanded`. Nel piede, sotto i 640 px, le quattro colonne sono una fisarmonica con veri bottoni (`aria-expanded`, "+" disegnato in CSS); senza script le liste restano aperte.

## Chiusura e piede

- **Chiusura**, con il testo a sinistra e la foto a destra fino al bordo:
  - la frase è "Le esigenze del cliente al primo posto", la seconda metà del titolo del loro profilo, che chiude il cerchio con "Abbatti i confini";
  - i recapiti stanno a 48 px sotto la frase: il telefono grande con `tel:`, l'email con `mailto:`, l'indirizzo con "apri la mappa", e il fax in piccolo;
  - la foto delle baie B9 e B10 è in 4:3, con il blocco di testo centrato in verticale. Non c'è un vuoto tra la frase e il telefono.
- **Piede**:
  - il logo SVG a 150 px, tagliato sopra la riga "SPEDIZIONI INTERNAZIONALI", che a quella misura sarebbe illeggibile, e una riga su chi sono;
  - quattro colonne: Servizi (Strada e groupage, Est Europa, Aereo, Mare, Dogana e Intrastat, Logistica e magazzino), Azienda, Contatti (con la PEC), Seguici (solo LinkedIn, l'unico social verificato);
  - in fondo la riga legale (ragione sociale, P.IVA e C.F., REA, capitale sociale), Privacy e Cookie.
- **Niente newsletter**: Melsped è uno spedizioniere B2B senza fiere, cataloghi, collezioni né clienti privati, e le sole notizie del sito sono cronache di pallavolo del 2012.

## Foto: origine e licenza

Tutte segnaposto Unsplash, licenza Unsplash (uso commerciale libero), verificata sulla pagina di ogni foto. Nessuna è generata dall'IA e nessuna è usata in altre home della campagna (controllato sui `CREDITI.md` di tutte le cartelle). Ritocchi in `assets/CREDITI.md`.

| Dove | Foto | Ritocchi |
|---|---|---|
| Apertura | Dextar Studio `2wpx8Bl0mwM` | raddrizzata; tolti la stella, le scritte della cabina e la sigla "FRC" del rimorchio; spenta la parte fucsia sotto il rimorchio; cielo schiarito; il cemento sfuma nella pagina |
| Strada | Matthew Jackson `SJGC3NNOqU4` | coperti due marchi sui sigillanti |
| Aereo | Peaky_82 `PEf3deR3l_U` | coperti i marchi sui motori e sulla scaletta |
| Mare | Venti Views `1cqIcrWFQBI` | nessun ritocco |
| Dogana | AFINIS Group `OnbSOhz0oig` | nessun ritocco |
| Chiusura | Yuri Krupenin `4n2Tvf8ZKVM` | nessun ritocco |

Trattamento comune a tutte, fatto con PIL: ombre sollevate, saturazione ridotta, bianco appena caldo. Le foto sono esportate in WebP in più larghezze con `srcset`. La foto della chiusura non è quella che compare subito sopra. Il brief per rifarle dal vero è nel `LEGGIMI.md`.

## Controlli

- **Segnali da IA** (`segnali.sh` del kit, a 1440): 0 soglie bloccanti su 10 e 0 da guardare su 8.
  - Foto al 36,7 % della pagina, Archivo al 100 %, monospazio allo 0 %.
  - 1 filetto (sopra la riga legale), nessuna freccia, nessuna etichetta maiuscola.
  - 2 fasce di fondo (la pagina e il piede), una data (1975).
- **Ai divieti**, guardando gli screenshot a pezzi: niente gradienti viola, badge, card, tre box con icona, Lucide, vetro, dissolvenze o effetti sul cursore. Nessun U+2014 nella pagina, nel LEGGIMI né in questa nota.
- **Larghezze** guardate a pezzi: 320, 390, 768, 1024, 1440 e 1920. Nessuno scorrimento orizzontale e nessuna sovrapposizione.
  - A 320 il selettore scende a 19 px perché le quattro voci stiano su una riga.
  - Il paragrafo dell'apertura è largo 23,5em, così non tocca il muso del camion.
- **Contrasti AA** misurati sui pixel della foto per la firma e la legenda, e sui colori pieni per il resto.
- **Immagini**: `controlla_img.py` verifica che ogni immagine citata esista e toglie quelle non usate. 32 file in `sito/img/`, 2,6 MB in tutto; la pagina a 1440 ne carica meno di 400 kB.
