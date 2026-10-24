# Poli-Art: proposta di nuova homepage

Proposta non richiesta, solo la home. Nessun contatto con l'azienda, niente pubblicato.

- **Pagina**: `sito/index.html` (statica; immagini in `sito/img/`, carattere in `sito/fonts/`).
- **Screenshot e nota**: `screenshot/home/` (`NOTA.md` spiega idea, caratteri, colori, interazione, foto e controlli).
- **Rifare tutto**: `sh _prova/script/build_finale.sh` (immagini con `finale_img.py`, pagina da `finale_index.html`, screenshot con `finale_shot.mjs` e `finale_jpeg.py`). Contorni delle teste in `_prova/script/contorni/finale-testa-*.json`.
- **Analisi e fonti**: `01-analisi.md`. Prototipi e giudizio: `_prova/home/a` (scelto) e `_prova/home/b`.

## Dati da confermare prima di pubblicare

In pagina c'è solo ciò che è verificato o pubblicato da loro; quello che segue è dubbio e va chiesto.

1. **Partita IVA 03796810244**: viene da un aggregatore (informazione-aziende.it, dati iCribis), cifra di controllo valida, ufficio di Vicenza. Va confermata con la visura, insieme a REA e PEC (non trovati). Oggi sul sito la P.IVA manca, ed è obbligatoria.
2. **"Impresa individuale"** nella riga legale: da informazione-aziende.it.
3. **Il 1986** ("dal 1986" in apertura e nel piede): il sito dice "L'Azienda nasce nel 1986", ma la P.IVA di Manuel ha 11-20 anni. Chi ha fondato l'attività? Si può scrivere "dal 1986"?
4. **Indirizzo**: via Tesinella 7, 7/A o 7/A/9 (il link alla mappa oggi usa "Via Tesinella 7").
5. **Orari**: solo da un aggregatore (lun-ven 8-12 e 14.30-18), quindi non in pagina. Se confermati, vanno nella chiusura sotto l'indirizzo.
6. **La testa a facce piane** (apertura e interruttore): è davvero lo stesso pezzo, grezzo e finito, come dicono i nomi dei file? Poli-Art l'ha costruita, rifinita o ha fatto il modello per un'opera in metallo? Di chi è l'opera e dove è esposta? Gli occhi e la bocca sono in foglia d'oro? Le didascalie oggi sono neutre ("La testa cromata, con occhi e bocca dorati"; "La testa in polistirene, prima della finitura") e vanno precisate con la risposta. Se il finito non è opera loro, l'interruttore va rifatto con un'altra coppia (vedi foto da rifare).
7. **Il pallone abitabile**: è un lavoro loro per una fiera? La persona accanto (forse Manuel) acconsente a comparire? La didascalia "Il prodotto rifatto in grande per la fiera" va confermata.
8. **La sala curva e il volume in montaggio** (`Pawson2`, `Pawson3`): per chi, dove, se si possono mostrare; le due persone sul ponteggio acconsentono? Se il cliente si può nominare, una didascalia piccola sotto la foto della chiusura.
9. **Le macchine**: quanti pantografi CNC, misure massime del blocco, filo caldo o fresa, quali stampanti 3D. Con questi numeri si aggiunge una riga di prova in "Dal file al pezzo finito".
10. **Resinatura e verniciatura**: interne o affidate fuori? Il passo 3 oggi dice solo "La superficie viene trattata per reggere gli urti e prendere l'aspetto voluto".
11. **Marchi dei clienti** nelle foto: nello stand mosaico+ il marchio non si legge nel ritaglio ma il lavoro è riconoscibile; le lettere rosse compongono "MERAVIGLIAMO". Permesso di mostrarli.
12. **Palloncini WOW**: la collaborazione è attiva? Nel piede la voce "Eventi con Palloncini WOW" è stata tolta; se confermata si rimette nella colonna Azienda con la pagina `eventi/`.
13. **"Loghistica"**: in pagina "Loghi e lettere in volume". Tenere il gioco di parole?
14. **Social**: Instagram e Facebook sono attivi? Se uno è fermo da anni, meglio toglierlo da "Seguici".
15. **Privacy e cookie**: servono i testi (oggi `privacy-policy/` dà 404, Google Analytics parte senza consenso).

## Pagine che il sito nuovo deve avere (link del piede e del menu)

`scenografie/`, `edilizia/`, `prototipi-e-mockup/`, `loghi-in-volume/`, `cake-design/`, `stampa-3d/`, `chi-siamo/`, `realizzazioni/` (la galleria di oggi, riordinata con didascalie), `privacy/`, `cookie/`; più `eventi/` se Palloncini WOW resta. Le voci Lavorazioni, Laboratorio e Contatti puntano alle sezioni della home.

**Niente newsletter**: lavorano su commessa e non hanno notizie, cataloghi, collezioni o fiere proprie da comunicare; per i clienti privati basta Instagram.

## Foto da rifare dal vero

La qualità di oggi è da telefono (media 4,6 su 10). In ordine di priorità:

1. **La testa grezza e la testa finita**, priorità uno per l'apertura. Fondo bianco caldo continuo (carta o cartoncino a sguscio, colore vicino a #F5F4F1), luce di finestra laterale da sinistra più un pannello bianco a destra per aprire le ombre; macchina sul treppiede, stessa inquadratura, stessa altezza (circa a metà del pezzo), stessa luce per i due stati; obiettivo medio (50-85 mm equivalenti) per non deformare le facce; bilanciamento del bianco fissato a mano; RAW. Per il cromo, una tenda bianca grande attorno al pezzo, così il metallo riflette bianco e non la stanza. Se la testa non è più disponibile, la stessa sequenza con un altro pezzo a facce piane: appena fresato e poi finito.
2. **Un pezzo fuori scala senza marchio, con una persona accanto**, su fondo neutro, inquadratura frontale dalla stessa altezza degli occhi, per la casella "Prototipi e fuori scala".
3. **Il laboratorio**: il pantografo o il filo caldo che taglia il blocco, le mani che rifiniscono, i trucioli bianchi; luce del capannone più una lampada continua, niente pavimento arancio in primo piano. Serve per "Dal file al pezzo finito".
4. **Still life**: un dettaglio di cornice resinata, una lettera in volume, un pezzo stampato in 3D, su fondo bianco caldo.
5. **Uno stand o una vetrina finiti**, con luce pulita e il permesso del cliente.

## Licenze

- **Carattere**: Mona Sans (GitHub Next), da Google Fonts, SIL Open Font License 1.1: uso commerciale libero, file woff2 serviti dalla pagina (`sito/fonts/`, copia in `assets/fonts/`).
- **Foto in pagina**: tutte di Poli-Art, dalla libreria media del loro sito (`assets/originali/`); da usare solo con il loro consenso. Nessuna foto di repertorio in questa home, nessuna immagine generata dall'IA. I segnaposto scaricati in `assets/esterne/` (licenze in `assets/CREDITI.md`) non sono usati nella versione finale.
- **Logo**: PNG del sito (`logo-blu-1815x400.png`) ritagliato e ridotto a 300, 360, 600 e 720 px; non ricostruito in SVG. Per il sito vero conviene chiedere il file vettoriale originale.
