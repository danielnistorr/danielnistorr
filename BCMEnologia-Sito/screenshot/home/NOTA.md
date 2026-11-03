# Home di B.C.M. Enologia: nota

## Livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///). La versione di prima ("Il torchio" sulla carta, con il selettore del diametro) è copiata in `_prova/versione-1-originale/` (sito, screenshot, LEGGIMI). Per BCM non c'era una "versione 1 con l'uso" separata: le prove d'uso della SCHEDA (`_prova/uso/SCHEDA.md`, paragrafo 8) sono state risolte in questo stesso passaggio e sono tra i controlli.

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia M (manifattura), sezione B (difetti delle nostre home), sezione C (15 regole). Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14 (foglio `riferimenti.jpg`, più Cly-Del, barth, Odermatt, Kline e Wilson a 390), le pagine intere di Cly-Del e barth a pezzi.

Rifare tutto: `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, screenshot con `pro_shots.mjs` all'ora simulata lunedì 2 novembre 2026 alle 10, controlli con `pro_controlli.mjs`: 60 su 61 passano, quello che non passa è la regola 11).

Screenshot (stessi nomi): `home-1440.jpg` (8470 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (13067 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Contatti" al piede). Guardati a pezzi a 390 e 1440 accanto a Cly-Del e barth, e a 320, 768, 1024, 1280 e 1920.

### Che cosa è cambiato, in breve

- **Struttura della famiglia M adattata a un'officina che tiene i ricambi**: testata fissa con sei voci (Ricambi, Macchine, Misure, Cataloghi, Chi siamo, Contatti), "Catalogues EN · DE · FR" e il bottone "Chiama 049 640372"; apertura con il mestiere nel titolo, il comune nell'occhiello, lo stato "Aperto ora" e la loro foto dei torchi in magazzino; un indice delle otto linee con la misura in una riga (come una pagina di catalogo); Ricambi e assistenza su blocco scuro (che cosa fotografare, Chiama, email con l'oggetto, il martinetto con la targhetta); otto schede delle linee con foto, misura, scheda e PDF; le tabelle delle misure (torchio idraulico e "Quale DAVID per il tuo torchio"); sei numeri su blocco rosso; cataloghi con lingua e peso, brochure ZIP, come si compra e i rivenditori; chi siamo con le date; contatti con la tabella degli orari e il modulo; piede in quattro colonne.
- **Il titolo**: "Torchi, martinetti DAVID e pompe, dal 1960". È il titolo di prima ("Torchi e martinetti, dal 1960") con le pompe, che sono metà del loro lavoro di oggi (SCHEDA, par. 1 e 4).
- **Il tono**: "noi" e "tu" come scrivono loro ("teniamo i ricambi", "siamo sempre a tua disposizione", "Produciamo...", "Una piccola e seria azienda artigianale" come titolo di chi siamo, non come slogan di chiusura). Tolti la terza persona, la newsletter e il selettore in apertura.
- **Foto, decisione "niente"**: nessuna foto di repertorio, nessuna illustrazione. Restano solo foto di BCM: in apertura la fila di torchi pronti in magazzino (wa0000, la loro foto più forte: faggio, cerchi rossi, martinetti), in quadrato nativo 1060 px (in pagina 563 px) e in 16:9 sul telefono; in chi siamo la fila di meccanismi in officina (wa0032, stessa giornata, stesso trattamento); il martinetto con la targhetta su fondo scuro nei ricambi, dove serve a far vedere che cosa fotografare; gli otto scontornati del sito tutti nello stesso quadrato grigio. Tolto il torchio scontornato sulla carta dell'apertura (regola 3 e difetto B2).
- **Colori dal marchio**: niente più carta beige. Fondo bianco, grigio neutro #F0F0EE per i blocchi chiari, ghisa #1F1E1C per testo e blocchi scuri, rosso #9E2B22 dei cerchi e del logo dei cataloghi per bottoni, cifre e un blocco pieno, verde #2A6234 solo per "Aperto ora".
- **Tipografia**: da tre famiglie (Zodiak, Sofia Sans, Sofia Sans Condensed) a due. Sofia Sans Condensed 700 per titoli e cifre, come i titoli dei loro cataloghi; Sofia Sans 400 e 700 per testo, etichette, bottoni e tabelle. Zodiak tolto: la serif da galleria a 114 px era una delle cose che "a loro sembrerebbe da grafico" (SCHEDA, par. 5).

### Uso: le prove della SCHEDA

- **A, ricambio, telefono 390x844**: senza scorrere ci sono "ricambi" nella riga sotto il titolo, "Aperto ora, fino alle 18" (calcolato sull'ora di Roma, lunedì-venerdì 8-18, festivi e Pasquetta chiusi, "riapriamo lunedì alle 8" il sabato), "Chiama 049 640372" a tutta larghezza (350x52) e "Ricambi e assistenza". Un tocco su "Ricambi e assistenza" porta ai tre passi (targhetta, diametro di gabbia o vite, pezzo) e al bottone "Manda le foto per email" con l'oggetto "Ricambio per la mia macchina BCM" e il testo da riempire: secondo tocco. A metà pagina il bottone Chiama resta nella testata (48 px).
- **B, rivenditore, 1440x900**: senza scorrere l'indice delle linee mostra pompe Volumex, pompe con inverter, inverter universale e pigiatrici; in un clic dalla scheda "Pompe con inverter" si scarica il catalogo PDF, con "2,3 MB, IT DE EN FR" scritto prima; "Catalogues EN · DE · FR" in testata porta ai cataloghi con una riga in inglese; nei contatti telefono, email e indirizzo stanno in 420 px.
- **C, scelta**: a 390 "Pompe Volumex, fino a 950 hl/ora" è nell'indice a 782 px (prima schermata e poco più) e porta alla scheda; "Quale DAVID per il tuo torchio" dice la vite da 45 a 100 mm per ogni modello; "Come si compra" è nella stessa sezione dei cataloghi; "Apri la mappa" è nei contatti e nel piede.

### Esito regola per regola (controlli di `_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile**: PASSA. Testata fissa a tutte le larghezze (80 px a 1440, 72 a 390); a 390 al 50% della pagina il bottone "049 640372" è a 12 px dall'alto, alto 48; 6 link `tel:`, tutti `+39049640372`. Per la famiglia M c'è anche la voce "Contatti" e il modulo.
2. **Prima schermata con mestiere, luogo, prova, azione**: PASSA a 1440x900 e 390x844. "Torchi, martinetti DAVID e pompe" in H1, "Saonara, Padova" nell'occhiello, "dal 1960" nel titolo, "Chiama 049 640372" pieno (a 390 a tutta larghezza).
3. **Immagine vera dell'azienda in apertura**: PASSA. La fila di torchi BCM nel loro magazzino (nativa 1060x1060, in pagina 563x563 a 1440; 16:9 a tutta larghezza sul telefono). Non è uno scontornato su fondo chiaro.
4. **Zero repertorio**: PASSA. "indicativ" 0; nessuna immagine da banche e nessun file da `assets/esterne/`.
5. **Foto in serie**: PASSA con un limite. Due serie: le due foto della galleria "In azienda" (stesso giorno, stesso trattamento di `pro_img.py`) e gli scontornati del sito, tutti con lo stesso trattamento, la stessa ombra e lo stesso quadrato. Formati a 1440: tre (1:1, 16:9 e il martinetto scontornato, 1,15). Didascalie: 2 su 11 foto, tutte e due con un fatto (cosa fotografare; luogo e anno). Il limite: sono scatti da telefono e da catalogo, non di un solo fotografo (LEGGIMI, foto da rifare).
6. **Palette dal marchio**: PASSA. Rosso #9E2B22 (cerchi, bacini, logo dei cataloghi) e ghisa #1F1E1C, verde solo per "Aperto ora", più bianco e quattro grigi; niente `--carta`.
7. **Scala corta e leggibile**: PASSA. 1440: 68, 44, 26, 20, 18, 16, 14 (7 misure); 390: 48, 38, 30, 22, 18, 17, 16, 14 (8). Testo corrente 18 e 17 px. I 14 px sono solo etichette in maiuscolo spaziato (come M, A4) e la riga legale. Titolo 68 px a 1440 (fascia 60-70), 38 a 390 (34-40).
8. **Due famiglie**: PASSA. Sofia Sans Condensed (titoli, cifre, telefono grande) e Sofia Sans (testo e interfaccia).
9. **Servizi in schede con foto**: PASSA. Otto schede in 4 colonne (2 sotto 860 px), passo 28 px, tutte col quadrato 1:1 grigio, nome di 26 px, una riga di misure, "Scheda della linea" (tutta la parte alta è un link) e sotto il PDF o lo ZIP con peso e lingue.
10. **Almeno tre tipi di prove**: PASSA con quello che hanno. Sei numeri veri (1960, 30+, 400, 950, 8, 4); rivenditori con il nome (Vivi in Campagna, Enologys, Kidonakis, KOL-Technik); marchio registrato DAVID e quattro SIMEI con il link alle foto degli stand al posto delle certificazioni, che non hanno. Recensioni: nessuna nelle fonti, non inventate (LEGGIMI).
11. **Lavori con un nome**: NON PASSA (non ci sono nelle fonti). Nessuna cantina cliente è nominata in 01-analisi o nella SCHEDA. Al loro posto ci sono le tabelle delle misure, che per chi sceglie un torchio servono di più. Da chiedere: tre cantine con nome, comune, anno, modello e una foto (LEGGIMI).
12. **Ritmo a blocchi**: PASSA. Blocchi pieni oltre al piede: Ricambi su ghisa e numeri su rosso; blocchi grigi per indice, misure e chi siamo. Spazio tra le sezioni 120 px a 1440 e 72 a 390; margini 80 e 20 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno rosso e con il solo bordo, raggio 4 px, 52 px (48 in testata), testo 18 e 16 px; ogni bottone di chiamata ha il numero.
14. **Modulo e "dove e quando" per il mestiere**: PASSA. Modulo M adattato: tipo di richiesta (Ricambio o assistenza, Preventivo, Sono un rivenditore), macchina e modello dalla targhetta, nome, azienda, email, telefono, messaggio, "Foto della targhetta e del pezzo: allegale all'email che si apre"; compone un mailto con oggetto e campi (da collegare a un servizio, LEGGIMI). Sede con indirizzo, "Apri la mappa", telefono, email e la tabella degli orari; nessun iframe.
15. **Piede completo**: PASSA, senza certificazioni (non ne hanno). Logo, ragione sociale, sede con la mappa, Macchine (8 linee), BCM, Contatti con orari e il link EN DE FR, P.IVA, REA, capitale sociale, Privacy e Cookie; 4 colonne a 1440, testo da 14 px.

### Respinti o non applicati, con il motivo

- **Lavori con il nome, recensioni, certificazioni, squadra con i nomi**: non sono nelle fonti; non inventati, chiesti nel LEGGIMI.
- **Testata di 56 px a 390** (SCHEDA, par. 4): la regola A2 chiede 72-88 px e la prima schermata ci sta lo stesso (la foto finisce a 704 px su 844).
- **Torchio idraulico a destra in apertura a 1440** (SCHEDA, par. 4): la regola 3 vieta l'oggetto scontornato su fondo chiaro in apertura; il torchio è nella prima scheda delle linee. Al suo posto la loro foto dei torchi in magazzino, che mostra le stesse macchine.
- **Martinetto con la targhetta nella prima schermata a 390** (SCHEDA, par. 4): è nella sezione Ricambi, a un tocco, accanto ai passi "che cosa fotografare", dove spiega che cosa mandare; in apertura c'è la foto del magazzino per la regola 3.
- **Il selettore del diametro con il torchio in scala** (versione di prima): tolto. Le stesse misure sono nella tabella del torchio idraulico, leggibili tutte insieme.
- **Mappa incorporata**: no (regola 14 e A6): link "Apri la mappa".

### Controlli generali

- Nessuno scorrimento orizzontale a 320, 360, 390, 768, 1024, 1280, 1440, 1920 (corretto durante il lavoro: la tabella del torchio a 320, con le gabbie "45 × 60" su una riga e i margini delle celle stretti sotto 360 px).
- Nessuna sovrapposizione negli screenshot a 320, 390, 768, 1024, 1280, 1440, 1920 (corretti durante il lavoro: le righe dei PDF non allineate nelle schede, perché anche il link del PDF si allungava; le schede a due colonne enormi a 1024, ora 4 colonne fino a 860 px; il campo "Azienda" più basso degli altri).
- Collegamenti: `tel:+39049640372` (6), `mailto:info@bcmenologia.com` (6, tre con oggetto), due mappe su "Viale Veneto 10-12 35020 Saonara PD", 14 ancore tutte esistenti, nessun `href="#"`; PDF e ZIP con i percorsi e i pesi letti dal sito il 3/11/2026.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script nuovi.

### Caratteri e licenze

Sofia Sans e Sofia Sans Condensed (Lettersoup, Google Fonts, SIL Open Font License 1.1), file woff2 variabili serviti dalla pagina da `sito/fonts/`; pesi usati 400 e 700. Zodiak (ITF Free Font License) non è più usato e il file è tolto da `sito/fonts/`.

---

## Versione 1 originale ("Il torchio"), prima del livello professionale

Quello che segue descrive la versione copiata in `_prova/versione-1-originale/`.

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `_prova/script/build_finale.sh` (immagini con `finale_img.py`, controlli e screenshot con `finale_shots.mjs`); i controlli dell'ultimo passaggio sono in `_prova/script/controlli_finali.mjs`. Alta 5.070 px a 1440 piede compreso, 6.916 px a 390.

### Idea

Il torchio idraulico BCM, la loro foto migliore, in piedi sulla carta chiara come in una tavola di catalogo fatta bene: un solo oggetto vero, grande, con la sua ombra su una linea di terra sottile. Quattro legende a filo leggono il pezzo (vite, martinetto DAVID, gabbia in faggio, bacino). Il selettore del diametro cambia i numeri veri della scheda tecnica e porta il torchio in scala sulla linea di terra. La stessa linea di terra torna sotto le sei macchine. Con il nome di un concorrente la pagina non regge: il "60" impresso nel faggio, i cerchi rossi, il DAVID e le sue spinte sono solo di BCM.

### Ultimo passaggio: cosa è cambiato dopo il giudice cieco

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

### Prime due schermate

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

### Caratteri e colori

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

### Interazione

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

### Foto

Tutte di BCM, dal loro sito (`assets/originali/`), lavorate con PIL in `finale_img.py` ed esportate in WebP in più larghezze con srcset. Nessuna foto di repertorio. I diritti sono da confermare (LEGGIMI).
- Scontornati: bordo ammorbidito, ombra a terra uguale per tutti, trattamento comune.
- Officina (wa0032) e chiusura (wa0000), galleria "In azienda" del 2022: sono foto da telefono, ripulite. Vanno rifatte dal vero (LEGGIMI).
- Logo: il PNG bianco del sito (170x96) ricolorato in inchiostro, a 85x48 in testata (2x) e a 128x72 nel piede. Non è ricostruito in SVG.

### Chiusura e piede

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

### Controlli (ultimo passaggio)

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
