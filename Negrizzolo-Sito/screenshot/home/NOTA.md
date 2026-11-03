# Home Negrizzolo: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (pagina, screenshot, controlli; con `--immagini` anche le foto). La home di prima e la sua nota ("Il cassone rosso", selettore delle portate) sono in `_prova/versione-1-originale/`.

## Livello professionale (3/11/2026)

Richieste del committente: "ancora troppo poco professionale e di design, e design funzionale all'attività"; "non rappresentano bene l'identità e l'utilizzo corretto"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso), sezioni A, B e C. Scheda d'uso: `_prova/uso/SCHEDA.md`. Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14, le pagine intere di barth e Cly-Del a pezzi; e le tre home di prova (Unicar, Oby, Panificio Fornasiero, colonna di destra di `_invio/zona/home/livello-professionale.jpg`).

Screenshot (stessi nomi): `home-1440.jpg` (7192 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (10709 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Orari e contatti" al piede), tutti all'ora simulata martedì 3 novembre alle 10. Guardati a pezzi a 1440 e 390 accanto a barth e Cly-Del, e a 320, 768 e 1024.

### Struttura (famiglia M, adattata a un'officina che risponde al telefono)

1. **Testata fissa** sobria: logo del biglietto, sei voci con le loro parole (Prodotti, Riparazioni, Taglio laser, Usato, Chi siamo, Orari e contatti) e il telefono come bottone col numero. Finché si vede il Chiama dell'apertura il bottone della testata è a filo, poi torna rosso pieno: un solo rosso pieno alla volta.
2. **Apertura** con la dichiarazione di mestiere, come Cly-Del ("Specialists in..."): il titolo è il loro, allungato ai tre mestieri come chiede la scheda: "Rimorchi, carribotte e vasche inox. Riparazioni di qualsiasi marca. Taglio laser."; occhiello "Officina meccanica dagli anni '50 · Grisignano di Zocco (VI)"; lo stato calcolato sull'ora ("Aperti ora, fino alle 12") con l'orario intero sotto; Chiama 0444 614515 e Come arrivare. A fianco (sopra, sul telefono) la loro foto intera del dumper rosso NE GRI ZZO LO davanti alla facciata blu con l'insegna, non scontornata.
3. **Competenze e processi** come indice, nella stessa prima schermata a 1440: tre colonne Costruiamo / Ripariamo / Taglio laser, ognuna con righe da toccare (portate e prezzo dell'usato allineati a destra, come una tavola tecnica): ribaltabili 35-200 q, fissi 30-200 q, carribotte 14-250 hl, vasche inox anche sul vostro rimorchio, usato 7.800 €; qualsiasi marca, ricambi, "Macchina ferma? 0444 614515", orari; "8 ore lavorative", materiali, "Mandate il disegno a laser@negrizzolo.it".
4. **Le nostre macchine**: sei schede con la loro foto in 4:3, quanti modelli a listino, nome, portata, una riga e il link alla scheda; la sesta è l'usato con il prezzo in rosso.
5. **Numeri** su blocco blu della facciata, titolo con la loro frase "La prima in Veneto a dedicarsi alla costruzione di cisterne e carribotte": 1800, 250 hl, 50 modelli, 2.000 mq coperti, 5.000 mq di piazzale, 8 ore. Cifre a 96 px: il gesto di scala della pagina.
6. **Riparazioni di qualsiasi marca** con le loro parole e, accanto, il riquadro "Macchina ferma? Chiamate l'officina" con lo stato, la tabella degli orari (il giorno di oggi in grassetto), Chiama e Come arrivare.
7. **Taglio laser e carpenteria** su blocco antracite: lavorazioni, "8 ore lavorative" in grande, gli otto materiali in tavola, "Mandate il disegno" (email già scritta con materiale, spessore, quantità, lavorazioni, consegna) e il telefono.
8. **Chi siamo**: cinque date in orizzontale (1800, anni '50, anni '60, anni '80, 2000), la foto d'archivio alla sua misura e la frase di AgroNotizie 2008.
9. **Orari e contatti** su zinco: la sede dall'alto, indirizzo, Indicazioni e Apri la mappa (nessuna mappa incorporata), telefono, le due email per settore, orari; accanto il modulo **Richiesta**.
10. **Piede** antracite in quattro colonne.

### Che cosa resta della versione 1 e che cosa è cambiato

- **Restano**: il titolo (sono le loro parole, ora con i tre mestieri), Archivo (una sola famiglia), il rosso dei cassoni, il logo SVG del biglietto, il tono serio col "voi", i dati veri delle tabelle (come gamme e numero dei modelli).
- **Via**: il fondo carta beige (#F4F2EE) in tutta la pagina; i rimorchi scontornati con l'ombra disegnata e il trattore cancellato (regola 3 e scheda par. 7); il selettore delle 11 portate, che prendeva la seconda schermata e tre schermate di tabelle sul telefono; la colonna "Video" del canale fermo; "Telefono e fax"; didascalie a 13 px.
- **Nuovo per l'uso**: riparazioni e laser nella prima schermata (prima a y 3.800 su 6.933 a 390); stato aperto/chiuso in apertura; "Come arrivare" con un tocco; l'usato con il prezzo; la mail del laser con un clic nella prima schermata a 1440; il modulo per tipo di richiesta.

### Esito regola per regola (misure di `_prova/script/pro_controlli.mjs`, esito in `_prova/pro_controlli.json`, più gli screenshot)

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa alta 80 px a 1440 e 73 a 390, bottone "0444 614515" alto 48 px. A metà pagina, a 1440 e a 390, il bottone si vede, è rosso pieno e si tocca (`elementFromPoint`). 7 link `tel:`, tutti `tel:+390444614515`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** H1 con i tre mestieri, "Grisignano di Zocco (VI)" e "dagli anni '50" nell'occhiello, Chiama a y 443-495 a 1440; a 390 Chiama largo quanto la colonna (349 px) a y 673-725, Come arrivare a 737-789.
3. **Immagine vera nell'apertura: passa, con riserva.** La loro foto intera: un loro dumper col nome sul cassone davanti alla sede con l'insegna. Mezzo col marchio e sede, ma senza persone, ed è di 1000 px (mostrata a 629 px a 1440, 349 a 390, mai ingrandita): va rifatta (LEGGIMI, foto 1). Nessuna illustrazione, per decisione del committente.
4. **Zero repertorio: passa.** `indicativ` 0 volte; in `sito/img/` solo foto del loro sito e il logo; nessun file Unsplash o Pexels.
5. **Foto in serie: passa, con riserva.** 9 foto, due formati (10:7 l'apertura, 4:3 tutto il resto), una sola didascalia (l'archivio, che aggiunge il fatto), stessa curva di colore per tutte, nessuna ingrandita. Riserva: sono scatti del sito di oggi con luci diverse (sole, tramonto, cielo velato); la serie vera viene dal servizio fotografico.
6. **Palette dal marchio: passa.** `--rosso` #C41A22 (cassoni, vicino al #EF3F35 del logo) con `--rosso-scuro` solo per il passaggio del mouse, `--blu` #1D4C6A (la facciata), `--verde` solo per il punto "Aperti ora"; neutri freddi (bianco, zinco #EEF0F1, grigio del logo #B3B5B8, antracite #16181A). Nessun colore scritto fuori da `:root`. Fondo bianco, nessun beige.
7. **Scala tipografica corta: passa.** 7 misure a 1440 (14, 18, 22, 28, 44, 60, 96) e 7 a 390 (14, 17, 20, 24, 30, 34, 56); testo corrente 18 px a 1440 e 17 a 390; niente sotto i 14 px; H1 60/34, H2 44/30 (fascia M).
8. **Due famiglie al massimo: passa.** Una sola, Archivo, pesi 400 e 700: larghezza 74 % per titoli e cifre (come le lettere sui cassoni), 100 % per testo e interfaccia.
9. **Servizi in schede con la foto: passa.** Griglia di 3 colonne a 1440 (2 a 768, righe con miniatura 4:3 a 390), 6 schede, tutte con foto vera nello stesso taglio 4:3, nome, gamma e link; tutta la scheda è un link.
10. **Almeno tre tipi di prova: non passa.** Ci sono i numeri aziendali (6) e la certificazione CE e omologazione scritta nelle schede e nel piede (una riga, non una fascia di loghi: non hanno altri certificati), più la citazione di AgroNotizie 2008. Mancano recensioni e clienti con il nome: non sono nelle fonti e non sono stati inventati (LEGGIMI, punti 5, 6 e 10).
11. **Lavori con un nome: non passa.** Nessun lavoro con cliente, luogo e anno nelle fonti (LEGGIMI, punto 6). Le schede mostrano lavori loro ma senza nome.
12. **Ritmo a blocchi: passa.** Due blocchi scuri pieni oltre al piede (numeri blu, laser antracite) e due in zinco (le tre porte, orari e contatti). Sezioni a 120/120 px a 1440 e 64/64 a 390; margini 75 px a 1440 (contenitore di 1290) e 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno rosso e a filo, raggio 4 px ovunque, alti 52 px (48 in testata), testo 18 px a 1440 e 17 a 390 (15 solo sotto i 360 px, in testata); tutti i bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: passa, con riserva.** Modulo in home con tipo di richiesta (macchina nuova, vasca sul proprio rimorchio, usato, riparazione, ricambio, taglio laser), nome, azienda, telefono, email, due campi che cambiano col tipo (per il laser "Materiale e spessore" e "Quantità") e messaggio; controllo di nome e recapito; le richieste del laser vanno a laser@, le altre a info@. Riserva: il disegno non si allega nel modulo (un mailto non porta file), si allega alla mail che si apre; da collegare a un servizio (LEGGIMI). Sede con indirizzo, Indicazioni e Apri la mappa; nessun iframe.
15. **Piede completo: passa.** Ragione sociale, P.IVA e C.F., REA, indirizzo con "Vai alla mappa", telefono ed email cliccabili, orari, prodotti, officina, certificazione CE, Privacy e Cookie; 4 colonne a 1440, testo di almeno 14 px. Zone servite: non pertinenti (famiglia M: una sola sede).

### Compiti della scheda d'uso (par. 8)

- **Compra, 390**: titolo e foto vera del loro rimorchio entro y 844 (foto 88-333, H1 409-548); "Carribotte 14-250 hl" a y 970-1014, un tocco porta a `carribotte.html`; "Usato: rimorchio 60 q.li, 7.800 €" a y 1060-1104 senza aprire il menu, e la scheda dell'usato con la foto più sotto; Chiama `tel:+390444614515` largo 349 x 52 px.
- **Macchina ferma, 390**: Chiama a y 673-725; stato "Aperti ora, fino alle 12" a 572; "di qualsiasi marca" nel titolo; Come arrivare a 737-789 (Google Maps, percorso verso via Ferramosca 14). Il numero resta nella testata fissa.
- **Orari** (prove della scheda e festivi): martedì 10 "Aperti ora, fino alle 12"; martedì 13 "Pausa pranzo, riapriamo alle 14"; martedì 19 "Chiusi ora, riapriamo domani alle 8"; venerdì 19 "Chiusi ora, riapriamo lunedì alle 8 (sabato mattina su appuntamento)"; sabato 10 "Sabato mattina: su appuntamento, chiamate"; domenica "Chiusi ora, riapriamo lunedì alle 8"; 8 dicembre e Pasquetta "Chiusi oggi, festivo. Riapriamo domani alle 8"; senza JavaScript resta l'orario intero.
- **Laser, 1440**: "Taglio laser, conto terzi" e "8 ore lavorative" a y 673-717; `mailto:laser@negrizzolo.it` con oggetto e traccia a y 763-807 (una sola mail del laser in tutta la pagina); gli otto materiali nella sezione laser, con un clic dall'indice. I formati accettati non sono scritti perché non sono nelle fonti (LEGGIMI, punto 1): questa parte della prova riesce a metà.
- **Per tutti**: nessuno scorrimento orizzontale a 320, 360, 390, 414, 768, 1024, 1280, 1440, 1920 e 2560; nessuna sovrapposizione nell'apertura a 1440 e 390; nessuna foto di repertorio; nessun U+2014; nessun errore di script; menu a 390 che si apre, porta al laser sotto la testata e si chiude; modulo vuoto fermato con l'avviso, modulo compilato che compone l'email senza inviarla.

### Caratteri e licenze

- **Archivo** (Omnibus-Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; licenza in `sito/fonts/OFL.txt`. Servito dalla pagina (`Archivo-var-latin.woff2`, `Archivo-var-latin-ext.woff2`, assi larghezza e peso), nessuna richiesta a Google Fonts.
- Foto: solo materiale del loro sito (`assets/originali/`, elenco in `assets/CREDITI.md`), da usare con il loro permesso. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.
