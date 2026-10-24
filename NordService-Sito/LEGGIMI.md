# Nord Service: proposta di nuova home

Proposta non richiesta di nuova homepage per Nord Service SRL (carrozzeria per macchine da lavoro, Mestrino PD). Solo la home.

- Pagina: `sito/index.html` (statica, si apre con file:///), `sito/img/`, `sito/fonts/`.
- Screenshot e nota di progetto: `screenshot/home/` (`NOTA.md`).
- Rifare tutto: `bash _prova/script/build_finale.sh` (script in `_prova/script/`: `finale_pala.py`, `finale_img.py`, `finale_controlli.mjs`).
- Analisi con le fonti: `01-analisi.md`. Prototipi: `_prova/home/a` (scelto) e `_prova/home/b`.

## Dati da confermare con l'azienda

In pagina c'è solo quello che sta in 01-analisi.md con la sua fonte; queste cose vanno chieste prima di pubblicare.
1. **La sequenza dell'apripista**: che le tre foto del 3, 10 e 16 ottobre 2024 (date dai nomi dei file) siano la stessa macchina. La linea dei giorni in apertura e le linguette ne dipendono. Se confermano anche la consegna quel giorno, "Finito" può diventare "Consegnato".
2. **La WA320**: che l'abbiano riverniciata loro (foto di maggio 2025). In pagina non lo diciamo, ma la macchina è in apertura.
3. **Le virole**: che siano un lavoro loro. La didascalia dice solo "Due virole blu sul camion. Maggio 2025."
4. **La macchina mascherata** della fascia (DSC07356): che tipo di macchina è, e se il nome si può scrivere.
5. **Testo nuovo da approvare**: "Il colore arriva solo dove la carta lascia scoperto" (didascalia della fascia) non è un loro testo; anche le didascalie delle foto e "Anche solo sul punto del danno" (dal loro "permette interventi localizzati in caso di danni") sono riscritte.
6. **Permessi sulle foto**: chi ha scattato le tre foto Sony e se si possono usare; macchine dei clienti con il marchio in vista (Komatsu WA320, CAT D8R): serve il permesso del cliente?
7. **Piede**: sede legale a Rubano (Via Pitagora 11/A, da VIES) e officina a Mestrino, scritte così? REA, capitale sociale, PEC e anno di costituzione non sono pubblici: non sono in pagina.
8. **Social**: l'Instagram è attivo? La pagina Facebook esiste (oggi il link è vuoto)?
9. **Tabarelli**: sei foto su 33 sono loro macchine; cliente fisso? Si può dire? Oggi non è in pagina.
10. **Ambiente**: "un occhio di riguardo per l'ambiente" non è in pagina finché non dicono cosa fanno (vernici a base acqua? recupero del garnet?). In pagina restano solo "poca polvere" e "il garnet si riusa", dal loro testo sulla sabbiatura.
11. Cabine (quante, quanto grandi, sabbiatura separata), dimensione massima dei mezzi: utili per una riga di prova in più.

## Pagine che il sito nuovo dovrà avere (link del piede)

`lavorazioni/sabbiatura-garnet/`, `lavorazioni/fondi-e-verniciatura/`, `lavorazioni/vetroresina-e-plastica/`, `lavorazioni/carpenteria/`, `lavorazioni/vetri/`, `lavorazioni/consulenza/`, `chi-siamo/`, `lavori/`, `contatti/`, `privacy/`, `cookie/`. Il menu in alto e "Prima e dopo" puntano alle sezioni della home. Da togliere dal sito di oggi: l'articolo di prova "Ciao mondo!" e la scheda Consulenza doppia (`-2`).

Niente newsletter: servizio su richiesta, senza notizie, fiere, cataloghi o clienti privati da informare.

## Foto da rifare dal vero

Mezza giornata con la stessa fotocamera Sony (APS-C, 35 mm o 50 mm), luce del mattino o cielo coperto chiaro.
- **Apertura**: una macchina finita sul piazzale, di tre quarti dal lato anteriore, fotocamera all'altezza dei mozzi, sfondo libero (muro chiaro o cielo pulito, niente altre macchine dietro). Si scontorna pulita, oppure regge da sola senza scontorno. Oggi la WA320 ha uno scontorno ricostruito e i vetri ritoccati.
- **Sequenza**: la stessa macchina sabbiata, verniciata e finita, **dallo stesso punto, con la stessa ottica e la stessa altezza** (segnare il punto a terra con il nastro). Così il cambio delle linguette diventa un prima e dopo esatto. Oggi sono tre foto da telefono con punti di vista diversi e il pavimento verde.
- **Mascheratura**: un dettaglio stretto di carta e nastro su un pezzo, con il colore che arriva al bordo della carta, per la didascalia "il colore arriva solo dove la carta lascia scoperto".
- **Materia**: metallo appena sabbiato in macro (luce radente) e vernice lucida appena data.
- **Chiusura**: un pezzo finito (anche le virole) su sfondo pulito, cielo non bruciato; o Stefano e Leonardo in officina, se vogliono comparire.

## Licenze

- **Carattere**: Archivo (Omnibus-Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero, servito da `sito/fonts/`.
- **Foto**: tutte di Nord Service SRL, scaricate da nordservice.net il 24/10/2026 (`assets/CREDITI.md`). Nessuna foto di repertorio in pagina: i segnaposto Unsplash in `assets/esterne/` non sono usati. Le sei foto di repertorio del sito di oggi (provenienza ignota) sono escluse.
- **Scontorno**: maschera fatta con ISNet (modello onnx di rembg, Apache 2.0), solo per separare la macchina dallo sfondo; nessun pixel generato.

## Logo

In pagina il PNG trasparente con "S.R.L." (`assets/originali/logo-nordservice-srl-1080x855.png`), ritagliato e a 2x (`sito/img/logo-112.png` in testata, `logo-192.png` nel piede). Non c'è un vettoriale: va chiesto all'azienda (o a chi l'ha disegnato) in SVG o PDF. Un SVG ricostruito a mano non è stato fatto perché il braccio a traliccio della "I" non verrebbe fedele.
