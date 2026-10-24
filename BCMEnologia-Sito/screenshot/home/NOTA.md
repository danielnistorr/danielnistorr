# Home finale di B.C.M. Enologia, "Il torchio": nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `_prova/script/build_finale.sh` (immagini con `finale_img.py`, controlli e screenshot con `finale_shots.mjs`); i controlli dell'ultimo passaggio sono in `_prova/script/controlli_finali.mjs`. Alta 5.070 px a 1440 piede compreso, 6.916 px a 390.

## Idea

Il torchio idraulico BCM, la loro foto migliore, in piedi sulla carta chiara come in una tavola di catalogo fatta bene: un solo oggetto vero, grande, con la sua ombra su una linea di terra sottile. Quattro legende a filo leggono il pezzo (vite, martinetto DAVID, gabbia in faggio, bacino). Il selettore del diametro cambia i numeri veri della scheda tecnica e porta il torchio in scala sulla linea di terra. La stessa linea di terra torna sotto le sei macchine. Con il nome di un concorrente la pagina non regge: il "60" impresso nel faggio, i cerchi rossi, il DAVID e le sue spinte sono solo di BCM.

## Ultimo passaggio: cosa è cambiato dopo il giudice cieco

Il giudice aveva dato K0 7,5 e K6 6. Le correzioni sono tutte dentro la stessa idea:

- **Il gesto agisce sull'oggetto.** Il torchio cresce e cala dalle ruote in proporzione all'altezza della gabbia del modello scelto: il 90 (gabbia alta 105 cm) ha l'altezza piena della prima schermata, il 60 il 71 %, il 45 il 57 %. Le legende restano agganciate ai pezzi perché la loro posizione usa la stessa scala. Il cambio è netto, senza animazione. Fuori dal modello 60 la didascalia dice "Foto del modello 60, in proporzione alla gabbia del 45". Al telefono la foto non si riscala, perché il selettore sta sotto la foto e la pagina salterebbe sotto il dito: cambiano capacità, peso, gabbia e modello DAVID.
- **Chiusura.** Adesso la frase e i recapiti stanno sopra e la fila di torchi è a tutta larghezza sotto. Il taglio nuovo, largo 1.920 px, non viene mai ingrandito a 1440 né a 1920. Le alte luci sono recuperate e il faggio ha il 22 % di saturazione in meno, con il colore generale al -20 %. I rossi tornano verso il #9E2B22 dei cerchi. La fascia alta con plastica e scatole è rifilata e abbassata. Per il telefono c'è un taglio a parte (1280x800).
- **Officina.** Il taglio è nuovo, in 16:9, sulla fila di meccanismi, senza sgabello, tavolo e cassoni. I medi sono più luminosi di circa 0,7 EV e i grigi sono scaldati verso la carta. La foto sta su 9 colonne (972 px CSS) con la didascalia nelle 3 accanto; la sorgente è larga 1.060 px, quindi non viene ingrandita.
- **Le sei macchine.** Hanno lo stesso trattamento del torchio: rossi e blu del motore spenti, alte luci da flash riportate giù, toni caldi e un filo di contrasto locale. Il faggio della gabbia è riportato verso quello del torchio. In ogni riga l'area visibile degli oggetti sta entro circa il 15 %: il martinetto è al 72 % del riquadro e la gabbia al 74 %, così un componente non è più grande quanto un torchio intero. Le box sono alte 360 px.
- **Link.** Ogni voce della griglia ha il suo id (`#torchi`, `#martinetti`, `#gabbie`, `#pompe`, `#pigiatrici`, `#frutta`) e porta alla pagina della sua linea. Nel menu, "Martinetti DAVID" porta a `#martinetti` e "Ricambi" a `#ricambi`, il paragrafo dei ricambi. I cataloghi portano alla pagina download; Privacy, Cookie e l'informativa portano alle pagine vere. Nessun `href="#"` e nessun link che punta alla sezione che lo contiene.
- **Preventivo nella prima schermata.** Sotto capacità e peso c'è una riga: "Per un preventivo: 049 640372 o info@bcmenologia.com", con `tel:` e `mailto:`. Non c'è nessun bottone pieno.
- **Testi.** "Il DAVID è progettato e brevettato da BCM negli anni 80…" (prima soggetto e verbo non andavano d'accordo). Nella storia tutto è in terza persona: "Di ogni macchina BCM tiene i ricambi…".
- **Piede, colonna Contatti.** Ci sono telefono, email, indirizzo breve con il link alla mappa e "Cataloghi PDF"; gli orari restano solo nella chiusura. Il logo nel piede è a 128x72.
- **Newsletter.** Quando l'invio è valido, sotto il campo compare "Grazie. (Modulo dimostrativo, da collegare al servizio di invio.)" in una riga `aria-live`. La validazione di email e consenso è quella del browser.
- **Menu al telefono.** Il tocco non accende più il celeste di sistema. A menu aperto il bottone dice "Chiudi", Esc lo chiude e il fuoco torna sul bottone.
- **Mappa.** La query è "Viale Veneto 10-12 35020 Saonara PD" in tutti e due i link.
- **Fra 881 e 960 px**, accanto al torchio il titolo restava in una colonna di 150 px. Il giudice non l'aveva visto, perché non aveva provato quelle larghezze. Ora fino a 960 vale l'impaginazione da tablet, e fra 961 e 1180 l'altezza del torchio ha un tetto anche sulla larghezza: alla colonna del titolo restano almeno 400 px. Sotto i 1180 px la didascalia scende sotto la linea di terra, così non tocca le legende quando vanno a capo.

## Prime due schermate

1. **Apertura (1440x900)**:
   - il menu sta accanto al logo e il telefono rosso in alto a destra, così il centro resta libero per la vite;
   - il torchio sta sulla linea di terra, che corre da margine a margine all'altezza delle ruote;
   - a sinistra il titolo "Torchi e martinetti, dal 1960" (Zodiak 114 px), la riga dei fatti, il selettore 45-90, capacità e peso e la riga del preventivo;
   - le legende stanno in una colonna allineata a destra.
   A 390: titolo, il torchio grande senza legende, la riga, il selettore, le quattro misure in due colonne e la riga del preventivo.
2. **Le macchine**:
   - titolo "Attrezzatura per l'enologia, dalla pigiatura al travaso";
   - sei oggetti scontornati con la stessa ombra, in una griglia 3x2 senza riquadri, appoggiati sulla linea di terra;
   - ogni voce ha una frase con misure vere;
   - a 390 è una colonna sola.

Poi l'officina, "Dal 1960, i torchi e i loro ricambi" con i tre fatti (SIMEI 2009-2019, spedizioni, cataloghi in quattro lingue), la chiusura e il piede.

## Caratteri e colori

- **Zodiak** 400 (Indian Type Foundry, Fontshare, ITF Free Font License: uso commerciale gratuito) per i titoli. È una serif ad alto contrasto che fa eco al "BCM" con le grazie del logo.
- **Sofia Sans** (Lettersoup, Google Fonts, SIL Open Font License 1.1) per il testo.
- **Sofia Sans Condensed** (stessa licenza) solo per misure, modelli e telefono, con cifre tabellari.
- I file woff2 sono in `sito/fonts/` e serviti dalla pagina, senza chiamate esterne. `font-synthesis: none`.
- Colori:
  - carta #F2F0EB;
  - inchiostro #1C1B1A;
  - testo secondario #57534E (6,7:1 sulla carta, 6,0:1 sul piede #E8E4DC);
  - un solo accento, #9E2B22, il rosso dei cerchi (6,5:1 sulla carta; bianco su rosso 7,4:1).
  Niente fondo nero: le foto sono al sole e chiedono luce.

## Interazione

Un solo gesto: il selettore del diametro della gabbia (45, 50, 55, 60, 65, 70, 80, 90).
- Sono radio veri: dito, clic, frecce della tastiera e Tab, con il fuoco visibile.
- Al cambio si aggiornano:
  - la scala del torchio e delle legende;
  - capacità e peso;
  - la vite (Ø mm);
  - il martinetto (modello DAVID e spinta);
  - la gabbia (diametro x altezza);
  - la didascalia.
- Dati dalla tabella del torchio idraulico e da quella dei martinetti (brochure BCM 2022).
- Niente dissolvenze allo scorrere, niente effetti sul cursore. Su bottoni e link toccati c'è solo un cambio di colore pieno di 0,12 s.

## Foto

Tutte di BCM, dal loro sito (`assets/originali/`), lavorate con PIL in `finale_img.py` ed esportate in WebP in più larghezze con srcset. Nessuna foto di repertorio. I diritti sono da confermare (LEGGIMI).
- Scontornati: bordo ammorbidito, ombra a terra uguale per tutti, trattamento comune.
- Officina (wa0032) e chiusura (wa0000), galleria "In azienda" del 2022: sono foto da telefono, ripulite. Vanno rifatte dal vero (LEGGIMI).
- Logo: il PNG bianco del sito (170x96) ricolorato in inchiostro, a 85x48 in testata (2x) e a 128x72 nel piede. Non è ricostruito in SVG.

## Chiusura e piede

- **Chiusura "b con foto"**:
  - la frase loro (dal "chi siamo") "Piccola e seria azienda artigianale" a sinistra, i recapiti a destra;
  - i recapiti: telefono grande rosso (`tel:+39049640372`), email (`mailto:`), indirizzo con "Apri la mappa", orari;
  - sotto, la fila di torchi a tutta larghezza;
  - niente riquadri.
- **Piede**:
  - logo e una riga su chi sono;
  - colonne Macchine, BCM e Contatti;
  - newsletter piccola "Una lettera prima della vendemmia";
  - riga legale con ragione sociale, P.IVA e C.F., REA, capitale sociale, Privacy e Cookie.
  Niente "Seguici", perché non c'è nessun social. A 390 l'ordine è: logo, Macchine e BCM su due colonne, Contatti, newsletter, riga legale.

## Controlli (ultimo passaggio)

- **Scorrimento orizzontale**: scrollWidth uguale a innerWidth a 320, 360, 390, 414, 600, 768, 880, 881, 1024, 1180, 1280, 1366, 1440, 1600, 1920 e 2560.
- **Screenshot guardati a pezzi**: 1440 e 390, intere e prima schermata; 320, 768, 1024, 1280, 1366 e 1920 in `_prova/tmp-finale/`; 920, 961, 1024, 1100 e 1180 con i modelli 45, 60 e 90. Nessuna sovrapposizione fra legende, didascalia e titolo.
- **Gesto con la tastiera**: da 60, tre volte freccia sinistra porta al 45. Il torchio passa da 604 a 483 px e le legende scendono con lui; la freccia successiva torna al 90.
- **Gesto con il clic**: sul 90 si legge 660 kg, 630 kg, E-90, 50.850 kg, Ø 90 mm, 90 × 105 cm, e il torchio è alto 846 px.
- **Tocco a 390**: sull'80 si legge 475 kg, 460 kg, 80 × 95 cm, D-80.
- **Menu**: si apre con "Chiudi", Esc lo chiude, il tocco su una voce lo chiude e porta all'ancora.
- **Newsletter**: senza consenso non parte; con il consenso compare la riga di riscontro.
- **Link**: un solo numero `tel:+39049640372`, un solo `mailto:info@bcmenologia.com`, la mappa su "Viale Veneto 10-12 35020 Saonara PD". Nessun `href="#"`, e tutte le ancore esistono.
- **Foto**: naturalWidth è maggiore o uguale alla larghezza CSS a 1440 e a 1920 (officina 1060 su 972, chiusura 1920 su 1920). A 2560 la chiusura è ingrandita di 1,33 volte: serve lo scatto nuovo.
- **U+2014**: nessuno in pagina, in questa nota e nel LEGGIMI.
- **Segnali da IA** (`_metodo/kit/segnali.sh`): 17 soglie su 18 a posto. Da guardare: due misure di H2 (60 e 66 px), volute, perché la gerarchia la fa l'apertura da 114 px. Resta sotto soglia l'area foto, al 29,5 % contro il 35 %. È il caso che la guida descrive per le aziende senza foto grandi: le loro foto vere più larghe sono scatti da telefono di 1.920 px, il resto è scontornato. In più, il torchio riportato in scala al modello 60 occupa meno spazio. La guida dice che non va nascosto: è la prima cosa da chiedere a BCM, cioè la giornata di foto nel LEGGIMI. Non ho allargato le foto oltre la loro misura nativa. Il taglio più alto della chiusura riportava plastica e scatole e l'ho scartato.
- **Divieti del committente**: niente gradienti viola, testo in gradiente, emoji, Inter, card col bordo colorato, vetro, badge, tre box con icona, Lucide, shadcn, dissolvenze, effetti sul cursore, hover che sbiadiscono, corsivo d'accento, tabelle a filetti.
- **Dati**: ogni numero viene da `01-analisi.md` e dalle brochure in `assets/originali/cataloghi/`.
