# Fratelli Zuin, home: "Scavi, cassoni scarrabili, strade e fognature a Padova, dal 1946"

La home di prima (fondo giallo, la parola "risucchio" a tutta pagina, nove lavori in una frase da toccare, sei foto Unsplash "indicative") è salvata con la sua nota in `_prova/versione-1-originale/` (sito e screenshot). Questa nota descrive la home di oggi.

Screenshot in questa cartella: `home-1440.jpg` e `home-390.jpg` (pagine intere), `home-1440-prima-schermata.jpg` e `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (preventivo, enti, dove siamo, piede).

## Livello professionale, ritocco finale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia S. Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14, le pagine intere di Eggentaler e di Wilson, a pezzi. Scheda d'uso: `_prova/uso/SCHEDA.md`. Questo giro applica il controllo del livello professionale (voto 6) e le prove dei due clienti tipo (privato a 390, tecnico a 1440).

### Che cosa è cambiato in questo giro e perché

- **Apertura a 1440 con la foto vera a destra**, come chiede la scheda (par. 4) e come fanno Eggentaler e Kline: griglia 7/5, a sinistra occhiello, H1 a 64 px, la riga loro, "Chiama 049 625336" e "Scrivi per un preventivo", l'indirizzo con la mappa; a destra una foto verticale 4:5 alta 633 px, l'escavatore della Ditta che carica il cassone rosso del DAF (`pagina-iniziale-1`, 2000 px, ritagliata a 704x880 e servita senza ingrandire). Via il pannello di sei riquadri bordati, che sembrava un'interfaccia.
- **Le sei voci in una striscia nera sotto l'apertura**, sei colonne divise da filetti verticali, testo bianco: tutte e sei dentro la prima schermata a 1440. A 390 restano dov'erano (sotto i bottoni, prima dell'indirizzo), ma senza bordo: righe a due colonne con filetto, alte 52 px, con la freccia rossa. "Strade e cortili" diventa "Cortili e passi carrai" (le strade sono già nel titolo): il privato legge "passi carrai" senza toccare.
- **Sotto i 900 px la foto dell'apertura è la stessa scena intera** (striscia larga, art direction con `<picture>`): a 390 resta alta 140 px in fondo alla prima schermata.
- **Un gesto di scala nella seconda schermata**: "1946" a 144 px (52 a 390) con "La Ditta nasce nel cortile di casa dei tre fratelli Zuin, con il primo autocarro, un DOGE."; accanto tre cifre a 48 px in righe con filetto: 3 generazioni, 2-25 m³ cassoni scarrabili, 30-250 q autocarri (dato del sito `.com`, in SCHEDA par. 1). "SOA" non è più una cifra.
- **Fascia delle qualifiche**, con filetti e senza loghi (non abbiamo il certificato): Attestazione SOA, qualificazione per i lavori pubblici; REA PD 82662, iscritta alla Camera di Commercio di Padova; ATECO 42.11, costruzione di strade e autostrade.
- **Serie fotografica** (`_prova/script/pro_img.py`): stessa curva per tutte. Blu del cielo spenti del 45%, saturazione -15%, alte luci compresse fino a 240 (il bianco bruciato diventa il grigio chiaro della pagina), bilanciamento appena freddo. Nelle 4:3 il taglio scende perché il cielo stia attorno al 20% (ritiro, demolizioni, fognature, scavi). La scheda "Scavi e movimento terra" usa ora `movimento-terra-1000x800-1` (stessa giornata dell'apertura, altro punto di vista), così nessuna foto si ripete.
- **Risucchio**: la frase corretta ("Scavi controllati e aspirazione di qualsiasi materiale: liquido, secco, solido e polveri, anche in luoghi confinati"); i quattro materiali come testo in grassetto separato da punti, non più riquadri che sembrano bottoni; l'autobotte combinata è un link alla scheda "Fognature e spurgo"; la riga "Portata, profondità di scavo e lunghezza del tubo: chiedetecele al telefono, per il vostro lavoro"; i bottoni sotto la foto (niente vuoto nero) e "oppure scrivete a info@fratellizuin.it" in chiaro, da copiare se il computer non ha un programma di posta. "Quantità indicativa" diventa "quantità approssimativa" (anche nella mail).
- **Sul telefono il risucchio viene subito dopo l'apertura** (comincia a 747 px, la foto si intravede già in fondo alla prima schermata), poi le cifre e le qualifiche: il tecnico vede foto e materiali entro la seconda schermata come prima; a 1440 l'ordine resta apertura, cifre, risucchio (il risucchio comincia a 1,54 schermate).
- **Schede dei servizi a 390**: foto a tutta larghezza in 3:2 e il testo sotto, invece della miniatura con il testo in una colonna di 182 px.
- **Lavori a Padova** in righe con filetto (nome a 24 px, a destra tipo e anno), non più schede grigie con "Città Padova" ripetuto.
- **Per enti e imprese** in una sezione a sé su grigio, dopo il preventivo: il privato arriva prima al modulo. "Dove siamo" passa a bianco.
- **Modulo**: nessuna scelta preimpostata su "Per quando" (se resta vuota la mail dice "Per quando: da concordare"); le righe dei campi facoltativi vuoti (email, descrizione) non compaiono nella mail.
- **Testata**: timbro a 128 px a 1440 (testata 88 px) e 84 px a 390 (testata 72). **Piede**: link alti 44 px per il dito, voce "Dati per enti e imprese".

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi a 1440, 390, 320, 768 e 1024.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa 88 px a 1440 e 72 a 390, bottone rosso "049 625336" alto 48 px con la cornetta; a metà pagina si vede e si tocca (`elementFromPoint`) a 1440 e a 390. 6 link `tel:`, tutti `tel:+39049625336`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** H1 con mestiere, "Padova" e "dal 1946"; a 1440 bottone di chiamata a 609 px, foto intera (633 px), le sei voci e l'indirizzo dentro i 900 px; a 390 bottone a tutta colonna (350 su 350) a 251 px, "Scrivi", le sei voci, l'indirizzo con la mappa e la foto (140 px) dentro gli 844 px.
3. **Immagine vera nell'apertura: passa, con riserva.** Escavatore e autocarro con il cassone rosso al lavoro, foto loro; nessun oggetto scontornato. Riserva: nessuna persona, e la provenienza della foto è "loro (probabile)" (LEGGIMI, foto).
4. **Zero repertorio: passa.** `grep -ci indicativ index.html` = 0; in `sito/img/` solo foto e logo dal loro sito (`assets/originali/`); nessuna Unsplash o Pexels.
5. **Foto in serie: passa.** Otto foto dallo stesso archivio con lo stesso trattamento (sopra); formati: a 1440 4:5, 2:1 e 4:3; a 390 striscia 2,79:1, 2:1 e 3:2; nessuna didascalia; nessuna ingrandita. Restano foto d'archivio di giornate diverse: il livello di Klindworth o Wilson arriva solo con la ripresa nuova (LEGGIMI).
6. **Palette dal marchio: passa.** `--rosso` #B42620 (cassoni), `--rosso-scuro` per il passaggio del mouse, `--nero` #141414 (timbro), `--bianco`; grigi neutri freddi. Fondo bianco, nessun beige.
7. **Scala tipografica corta: passa.** 7 misure a 1440 (14, 17, 20, 24, 48, 64, 144) e 7 a 390 (14, 16, 18, 20, 30, 34, 52); testo corrente 17 e 16 px; niente sotto i 14 px; H1 64/34, H2 48/30.
8. **Due famiglie al massimo: passa.** Una sola, Archivo, pesi 400 e 700.
9. **Servizi in schede con la foto: passa.** Griglia di 3 colonne a 1440 (2 a 1024 e 768, una a 390), sei schede con foto loro, stesso taglio (4:3, 3:2 sul telefono), nome e link, tutta la scheda cliccabile. Strade, cortili, urbanizzazioni e SOA in elenco a righe: le foto di questi lavori non ci sono.
10. **Almeno tre tipi di prova: non passa (2 su 4).** Ci sono 4 cifre (1946, 3 generazioni, 2-25 m³, 30-250 q) e la fascia delle qualifiche con didascalia (SOA, REA, ATECO). Mancano recensioni (nessuna in rete) e clienti con il nome: non si inventano (LEGGIMI punti 9 e 10).
11. **Lavori con un nome: non passa.** Tre lavori con luogo e tipo (Ex Foro Boario 1968-69, Azienda del Gas di Via Trieste, Prato della Valle), anno solo per il primo, nessuna foto e nessun numero. Servono lavori recenti con committente, anno, dati e foto (LEGGIMI punto 8).
12. **Ritmo a blocchi: passa.** Bianco (apertura), nero (striscia, cifre, qualifiche, risucchio), grigio (lavori), bianco (chi siamo), rosso (preventivo), grigio (enti), bianco (dove siamo), nero (piede): 3 blocchi pieni oltre al piede. Sezioni a 120 px a 1440 e 72 a 390; contenitore 1280 px, margini 80 e 20 px.
13. **Un solo sistema di bottoni: passa.** Pieno rosso e bordato (nero sul chiaro, bianco sul nero), raggio 4 px, 56 px (48 in testata e Menu), testo 17 e 16 px; i bottoni di chiamata contengono il numero. Tolti gli altri stili bordati (riquadri delle voci, materiali); restano solo le radio del modulo, che sono controlli.
14. **Modulo e "dove" per il mestiere: non passa (manca l'elenco dei comuni).** Modulo con nome, telefono, email, tipo di lavoro (10 voci), indirizzo del lavoro, descrizione, per quando (nessuna scelta preimpostata) e l'istruzione per le foto (un mailto non porta allegati); nessun iframe di mappa. Le zone servite non sono note (LEGGIMI punto 2).
15. **Piede completo: non passa (mancano orari e zone).** Quattro colonne, testo di almeno 14 px, logo, nome, telefono, fax, email, sedi con la mappa, lavori, P.IVA, REA, SOA, Privacy e Cookie. Orari, zone e PEC non sono nelle fonti (LEGGIMI punti 1, 2 e 6).

### Compiti dei clienti tipo e della scheda (par. 8)

- *Privato, 390*: bottone tel: alto 56 px a 251 px, la testata con il numero resta fissa; "Cassoni scarrabili 2-25 m³", "Fognature e spurgo" e "Cortili e passi carrai" visibili senza toccare; "Via Bassette 6/A, Padova Est" visibile e apre Maps; "Scrivi per un preventivo" apre con un tocco l'email con oggetto e traccia (indirizzo, foto); il modulo arriva prima dei dati per gli enti; nessun orario inventato.
- *Tecnico, 1440 e 390*: a 1440 il risucchio comincia a 1,54 schermate, foto e "liquido, secco, solido e polveri" nella seconda schermata (a 390 la sezione comincia a 0,88 schermate); chiamata, email ed email in chiaro dalla sezione; l'autobotte porta alla scheda dello spurgo.
- *Ente, 1440*: SOA, REA e ATECO nella seconda schermata; ragione sociale, P.IVA, sedi in "Per enti e imprese" e nel piede, senza fisarmoniche; storia dal 1946 e tre lavori di Padova per nome.
- Prove automatiche (`pro_controlli.mjs`): menu del telefono aperto e chiuso; "Dove siamo" sotto la testata; la scheda "Fognature e spurgo" sceglie "Fognatura o spurgo" nel modulo; invio vuoto fermato con "Mancano: nome e cognome, telefono, indirizzo del lavoro." e il fuoco sul nome; email composta senza la riga vuota "Email:" e con "Per quando: da concordare"; nessun errore di script.

### Caratteri e licenze

- **Archivo** (Omnibus-Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; servito dalla pagina (`sito/fonts/archivo-latin-var.woff2`), licenza in `sito/fonts/OFL.txt`. Pesi 400 e 700.
- Foto e logo: solo materiale del loro sito (`assets/originali/`), da usare con il loro permesso. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Controlli fatti (3/11/2026)

- `sh _prova/script/build_finale.sh`: immagini, pagina, controlli di testo, screenshot, `pro_controlli.mjs` (regole 1-9, 12 e 13 superate nelle misure; 10, 11, 14 e 15 no, per i motivi sopra).
- Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1280, 1440 e 1920; nessuna sovrapposizione nell'apertura e nessun testo che esce da bottoni, schede, cifre o qualifiche.
- Screenshot guardati a pezzi a 1440 e a 390, prime schermate e pezzi a 320, 768 e 1024. Nessun U+2014 in pagina, nelle note e negli script.
