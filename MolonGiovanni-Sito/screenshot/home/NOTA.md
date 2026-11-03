# Home di Molon Giovanni

## Livello professionale (3/11/2026), con il ritocco finale

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso), struttura A1 adattata a un costruttore di macchine da fieno che vende tramite rivenditori. Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14 (fogli in `_prova/pro-controllo/rif/`), le pagine intere di barth e Cly-Del (a pezzi), più Budri e Odermatt nel controllo. Scheda d'uso: `_prova/uso/SCHEDA.md`.

Questa home sostituisce "Il pettine" (versione 1, copiata com'era in `_prova/versione-1-originale/` con sito e screenshot).

Pagina: `sito/index.html` (statica, si apre con file:///), immagini WebP in `sito/img/`, carattere in `sito/fonts/`. Sorgente: `_prova/script/pagina-pro.html`. Si rifà tutto con `bash _prova/script/build_finale.sh` (logo `finale_logo.py`, immagini `pro_img.py`, pagina, screenshot `pro_shot.mjs` a 1440, 390, 320, 768 e 1024, controlli `pro_controlli.mjs` in `_prova/pro_controlli.json`). Altezza: 11.530 px a 1440, 17.930 a 390.

### Ritocco finale: che cosa è cambiato rispetto alla prima passata "livello professionale"
Dal controllo del livello (voto 6) e dalle prove dei due clienti tipo (6,5 e 6,5):
- **Apertura con un gesto**: blocco antracite pieno con l'H1 bianco a 72 px (era 64 su bianco), occhiello bianco con il filetto rosso, la foto vera a filo destro e senza raggio, i tre ingressi in fila sotto, divisi da filetti scuri, solo testo, con la misura su una riga. Taglio della foto spostato sulla macchina e sull'andana (via il 16 % a destra, dove c'è il portattrezzi). Tolto "dal 1967" dalla riga del mestiere: in apertura resta "dal 1936" una volta sola.
- **390, bottone principale a tutta larghezza** (350 px). "Ricambi" diventa la prima riga degli ingressi ("Macchina ferma: come ordinare il pezzo"); i quattro ingressi stanno in righe di 56 px divise da filetti e l'ultimo finisce a y 815 su 844.
- **Nuova sezione "Le macchine"** subito sotto l'apertura, al posto di girelli e scopatrici: sei schede in 3 colonne (2 sotto i 1100 px, 1 sotto i 720), foto 3:2 a tutta larghezza della scheda (409 x 272 a 1440, 348 x 232 a 390), fondo della foto e della scheda dello stesso grigio, nome a 24 px, misure, freccia, tutta la scheda è un link. La sesta è il gEnio, con la sua foto vera (`2025_02_gEnio-230-4-depliant.gif`). Sotto i 1100 px le foto restano.
- **Tabelle**: quella dei frontali resta aperta (il rivenditore ci arriva con un clic); quelle dei posteriori e delle motofalciatrici sono righe "6 modelli posteriori" / "10 modelli per motofalciatrici" con i nomi dei modelli e il bottone "Vedi i 6 modelli" / "Vedi i 10 modelli" (aria-expanded; senza JavaScript restano aperte). Sul telefono la colonna "Massima cm" ora si vede (era nascosta) e si nasconde "Pettini"; sotto i 375 px si nasconde anche "Massima" perché la tabella stia nei 280 px. Nota sotto i frontali: "Il 300 PRO lavora 280 cm; 320 cm è la larghezza massima."
- **"Va sul mio mezzo?"**: al posto del link al modulo in fondo, la domanda "Va sul vostro mezzo? Diteci marca, modello e presa di forza." con due bottoni, "Chiama 049 900 0103" e "Scrivete" (mailto con oggetto "Va sul mio mezzo?" e traccia: marca e modello, presa di forza con giri e verso, zona, nome e telefono).
- **Numeri**: solo dati dell'azienda, a 96 px: 25 modelli di ranghinatori (9 + 6 + 10, dalle tabelle), 5 famiglie di macchine, 3.000 m² coperti, 5,0 su Google con 8 recensioni. Via 1936, 1967 (restano nella cronologia) e "100-280" (misura di prodotto).
- **Ricambi**: colonna di destra allineata in alto con il numero grande in bianco sopra i due bottoni; via il fax; "Se non rispondiamo, mandate la foto con il vostro telefono a info@molonmachinery.com" con il link alto 44 px.
- **Prezzo**: "Per il prezzo rivolgetevi al rivenditore o chiamateci" (prima la pagina dava per certo che il prezzo lo fa il rivenditore).
- **Contatti**: a partire da 1100 px i recapiti restano fermi accanto al modulo mentre si scorre (sticky).
- **Foto in serie**: stesso trattamento per tutte le foto in campo e per la squadra in `pro_img.py` (bianco neutro corretto a metà, spalla morbida sulle alte luci che recupera il cielo dell'apertura, ombre appena aperte, saturazione 0,92, contrasto 1,04); velatura tolta dalla foto del lago.
- **Codice e tocco**: nessuno stile in riga (fax, indirizzo e titolo "Lingue" del piede in classi; colore del link email in classe); il filetto dei numeri è il token `--filetto-chiaro`; link del piede, Privacy, Cookie, informativa del modulo e lingue (44 x 44, distanza 4 px) di almeno 44 px. Il menu del telefono si chiude prima di scorrere alla sezione, così il titolo non finisce più sotto la testata (prima, a 390, Ricambi dal menu arrivava 139 px troppo in alto).
- Occhiello dei frontali "Ranghinatori frontali per portattrezzi e trattori"; testo alternativo del MAJOR allineato alla tabella.

### Le prime schermate
- **1440 x 900**: testata bianca fissa di 81 px (logo, cinque voci, IT DE EN FR, bottone rosso "049 900 0103"). Blocco antracite: a sinistra occhiello "Arlesega di Mestrino (PD) · dal 1936", H1 "Ranghinatori a cinghie" a 72 px, riga "per portattrezzi, trattori e motofalciatrici", frase loro, "Chiama 049 900 0103" pieno e "Ricambi" bordato; a destra la foto vera 4:3 a filo del bordo. Sotto, i tre ingressi per mezzo (712-864 px).
- **390 x 844**: testata fissa di 73 px con logo, telefono e Menu; IT DE EN FR a vista; foto 16:9 a filo; blocco antracite con occhiello, H1 a 40 px, riga del mestiere, "Chiama 049 900 0103" a tutta larghezza, poi Ricambi e i tre ingressi (fino a y 815).
- **1024 x 768**: come a 1440 con il menu nel bottone; gli ingressi entrano interi. **768 x 1024**: foto 16:9 sopra, testo e ingressi in tre colonne sotto. **320 x 640**: come a 390; il telefono in testata perde l'icona.

### Le 15 regole, una per una
Misure di `node _prova/script/pro_controlli.mjs` (`_prova/pro_controlli.json`), più gli screenshot guardati a pezzi a 1440, 390, 320, 768 e 1024.

1. **Telefono come bottone nella testata fissa: passa.** Testata sticky di 81 px a 1440 e 73 a 390; bottone pieno alto 48 px con il numero. Al 50 % della pagina il bottone sta a 16 px dall'alto a 1440 e a 12 a 390 e `elementFromPoint` lo trova. 10 link `tel:`, tutti `tel:+390499000103`. Per M c'è anche la voce Contatti con il modulo.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** H1 con il mestiere, "Arlesega di Mestrino (PD)", "dal 1936", bottone di chiamata in vista; a 390 il bottone è largo 350 px su 350 (a tutta larghezza) e Ricambi resta in vista come prima riga degli ingressi.
3. **Immagine vera nell'apertura: passa.** Il frontale Molon rosso al lavoro sul prato in collina, con l'andana, tagliato sulla macchina. Riserva: il portattrezzi (senza marchi leggibili) occupa ancora la parte destra; la foto da rifare è nel LEGGIMI.
4. **Zero repertorio: passa.** `indicativ` 0, `unsplash|pexels` 0; 13 immagini visibili, tutte foto di Molon in `sito/img/`; nessuna illustrazione (gli SVG sono il logo, il telefono e le frecce).
5. **Foto in serie: passa con riserva.** Tre formati a ogni larghezza (4:3, 3:2, 16:9: a 1440 apertura, lago, MAJOR e archivio 4:3, schede 3:2, squadra 16:9; a 390 apertura e squadra 16:9); 1 didascalia su 13 immagini; stesso trattamento colore per tutte le foto in campo, schede tutte sullo stesso grigio con la stessa linea di terra. Riserva: restano scatti di anni e luci diverse (archivio in bianco e nero, squadra a luce piatta); la serie vera è la giornata di riprese del LEGGIMI.
6. **Palette dal marchio: passa.** `--rosso` #C8231B (la vernice delle macchine) e `--rosso-scuro` solo al passaggio del mouse; `--antracite` #1F2122 dal logo; il resto sono neutri freddi. 0 colori scritti fuori da `:root` (anche il filetto chiaro è un token). Nessun beige.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 20, 24, 32, 48, 72, 96) e 8 a 390 (14, 16, 18, 20, 24, 28, 40, 48); testo corrente 17/16 px; nessun testo sotto i 14 px; H1 72/40, H2 48/28 (fascia M).
8. **Due famiglie al massimo: passa.** Una sola, Sofia Sans, pesi 400 e 700.
9. **Schede con la foto: passa.** Sezione "Le macchine": 6 schede in 3 colonne a 1440 (passo 24 px), ognuna con la foto 3:2 dello stesso taglio (409 x 272), il nome e la freccia; tutte link. Le foto restano a tutte le larghezze (2 colonne sotto i 1100, 1 sotto i 720).
10. **Almeno tre tipi di prova: non passa (2 su 4).** Ci sono 4 numeri aziendali (25 modelli, 5 famiglie, 3.000 m², 5,0 su Google con 8 recensioni) e la fascia dei partner con paese e sito. Mancano recensioni con nome e comune, clienti con il nome e certificazioni: non sono nelle fonti (01-analisi: "Nessuna certificazione, nessun premio, nessun cliente citato") e non sono stati inventati; vanno chiesti (LEGGIMI, punto 7).
11. **Lavori con un nome: non passa.** Nessun lavoro con cliente, luogo e anno nelle fonti (LEGGIMI, punto 7).
12. **Ritmo a blocchi: passa.** Apertura, Ricambi e Chi siamo in antracite, Come lavora in rosso Molon (4 blocchi pieni oltre al piede); Posteriori e Contatti in grigio. Sezioni 120/120 px a 1440 e 72/72 a 390; margini 80 a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: passa.** 17 bottoni visibili a 1440, pieno rosso e bordato, raggio 4 px, 52 px (48 in testata), testo 17/16 px; tutti i bottoni di chiamata contengono "049 900 0103".
14. **Modulo e "dove" per il mestiere: passa.** Modulo con tipo di richiesta, nome, azienda, email, telefono, paese e zona, presa di forza, mezzo, macchina Molon dalla targhetta, messaggio; al posto dell'allegato del disegno la pagina chiede di allegare le foto all'email che si apre (un mailto non porta allegati; il servizio vero è nel LEGGIMI). Sede con "Vai alla mappa" e "Indicazioni stradali"; 0 iframe.
15. **Piede completo: non passa del tutto.** Quattro colonne (4fr 3fr 3fr 3fr), testo di 17 px e di 14 nella riga legale, ragione sociale, indirizzo, P.IVA 00258060284, telefono ed email cliccabili, mappa, rivenditori, lingue, Privacy e Cookie, link alti 44 px. Mancano gli orari (non pubblicati) e le certificazioni (nessuna nota): LEGGIMI punti 1 e 7. La ragione sociale S.r.l. o S.n.c. è da confermare (punto 8).

### Compiti della scheda d'uso (par. 8), dopo il ritocco
- **Contadino, 390 x 844.** In prima schermata la foto vera, il mestiere, il telefono a tutta larghezza, le lingue e i tre ingressi per mezzo: un tocco su "Motofalciatrici e motocoltivatori" porta a MINI, MIKY e MAJOR con larghezze e pesi. **Riesce**, come prima. "Va su un Reform a 540 giri?": i giri sono scritti, le marche no (vanno confermate da Molon, LEGGIMI punto 3); adesso accanto alla domanda ci sono "Chiama" con un tocco e "Scrivete" con la traccia già pronta, invece del modulo a 11.000 px. **Riesce a metà, meglio di prima.** Scelta della larghezza: frontali in tabella aperta; per posteriori e motofalciatrici le misure sono nel titolo, nella riga di presentazione e nelle tre schede MINI, MIKY e MAJOR, e la tabella intera è a un tocco ("Vedi i 6 modelli"); la colonna della larghezza massima ora si vede sul telefono. **Riesce.** Rivenditore: invariato (Gasser con il sito, "chiamateci" per le altre zone). **Riesce a metà.**
- **Proprietario con guasto, 390 x 844.** Telefono a tutta larghezza e "Ricambi" in prima schermata; un tocco chiama, un tocco porta al blocco Ricambi con il numero grande, le tre cose da dire e "Manda la foto per email". **Riesce.** Orari: non pubblicati, quindi il compito 1 resta senza "orari di oggi" (LEGGIMI punto 1). Ricambi dal rivenditore e tempi: non nelle fonti (punto 2).
- **Rivenditore, 1440 x 900.** Le tre famiglie e il telefono in prima schermata; un clic porta alla tabella aperta dei frontali. **Riesce.** Depliant PDF: non esiste (punto 6). Email e telefono in testo copiabile. **Riesce.**
- **Per tutti**: 0 link "#", nessuna foto di repertorio, nessuna immagine riscalata a fingere un altro modello, larghezza del documento uguale alla finestra a 320, 390, 768, 1024 e 1440, 0 sovrapposizioni, nessuna zona toccabile sotto i 44 px a nessuna delle cinque larghezze (escluso il link nascosto "Vai al contenuto").

### Foto, origine e trattamento
Tutte di Molon Giovanni, da molonmachinery.com (`assets/originali/`, voti in `_prova/inventario-immagini.json`, elenco in `assets/CREDITI.md`):
- `apertura-*` (4:3) e `apertura-tel-*` (16:9): `2017_10_11.08_10ritoc.jpg` (3264 x 2448), tolto il 16 % a destra, al massimo 1600 px.
- `frontale-lago-*`: `2017_10_11.08_4-copia.jpg` (2000 x 1500), 4:3, velatura tolta.
- `major-prato-*`: `2025_03_dok-tc-07-molon-br.jpg` (4032 x 3024, orientamento EXIF corretto), 4:3.
- `archivio-*`: `2017_10_foto4.jpg`, 4:3, bianco e nero neutro.
- `squadra-*`: `2017_10_P1090586_mod-1.jpg`, 16:9.
- `s-*`: gli scontornati `2017_10_230_5-scont.jpg`, `2017_10_RANGHINATORE-POST09noEtichette.jpg`, `2018_01_MAJOR160_sf.jpg`, `2025_02_gEnio-230-4-depliant.gif`, `2017_10_girello-380.jpg`, `2017_10_SCOPA-lamiera.jpg`, moltiplicati sul grigio #F0F1F1 a parità di massa, 3:2.
Nessuna foto mostra macchine di altri costruttori con marchi leggibili in primo piano.

### Caratteri e licenze
Sofia Sans (Lettersoup, Google Fonts), file variabile latino servito dalla pagina (`sito/fonts/sofia-sans-latin-var.woff2`), SIL Open Font License 1.1, testo in `sito/fonts/OFL-Sofia-Sans.txt`: uso commerciale libero.

### Fonti dei dati in pagina
`01-analisi.md` (storia, numeri, recapiti, partner, testi loro), `_prova/uso/SCHEDA.md` (portattrezzi, compiti), le tabelle dei modelli lette il 3/11/2026 sulle pagine di molonmachinery.com (`_prova/crawl/`). "25 modelli" è la somma delle tre tabelle (9 + 6 + 10); "5 famiglie" sono frontali, posteriori, per motofalciatrici, girelli e scopatrici (le voci Prodotti del sito di oggi).

### Controlli fatti (3/11/2026, ritocco finale)
- Screenshot rifatti in `screenshot/home/` (1440 e 390 intere e prima schermata, chiusura a 1440, prime schermate a 320, 768 e 1024) e guardati a pezzi, insieme alle pagine intere a 320, 768 e 1024.
- Interazione provata con Playwright: bottoni delle tabelle (si aprono e si chiudono, aria-expanded e testo corretti), menu del telefono (Ricambi, Rivenditori e Contatti arrivano a 80 px dall'alto, sotto la testata), ingresso "Ricambi", link "Chiedete il vostro" che sceglie il tipo nel modulo, avviso del modulo senza nome ed email. Unico messaggio in console: aprendo da file:// il preload del carattere è bloccato dal browser (CORS dei file locali); il carattere si carica comunque, e su un server il messaggio non c'è.
- Nessun carattere U+2014 nella pagina, negli script, in questa nota, nel LEGGIMI e nei CREDITI.


## Versione 1, "Il pettine" (24/10/2026), sostituita

Archiviata con sito e screenshot in `_prova/versione-1-originale/`. La nota di allora segue com'era.


Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, logo con `finale_logo.py`, pagina da `pagina.html`, screenshot con `finale_shot.mjs`). Prove della prima schermata con `prove_apertura.mjs`, controlli finali con `controlli_finali.mjs`. Altezza a 1440: 5517 px, piede compreso; a 390: 6690 px.

### L'idea
Il ranghinatore frontale a cinghie, scontornato e nitido sulla carta color fieno, è l'unico protagonista, e si misura: scegliendo il modello la macchina cambia larghezza in scala sopra una sola linea di terra quotata da 0 a 320 cm, con la barra rossa del lavoro e quella grigia della larghezza massima. È la loro tabella dei frontali (190, 210, 230, 250, 260, 300 PRO) resa visibile sul loro oggetto: con il nome di un altro costruttore la scala e i numeri non tornano più.

### Le prime due schermate
1. A 1440: testata con il logo MOLON in SVG, cinque voci, telefono e lingue. Titolo "Ranghinatori a cinghie" a 112 px su una riga. Sotto, a sinistra, la frase sulle tre operazioni e il bottone rosso "Chiama 049 900 0103"; in basso a sinistra la scelta del modello (sei numeri in cifre tabellari, Versione PRO, gEnio) con la riga "280 cm di lavoro, 320 massima, 16 pettini"; a destra la macchina sulla linea di terra. All'apertura è scelto il 300 PRO, il più largo. Nessuna legenda a filetti, nessuna riga "luogo, dal anno".
2. "Nove frontali per trattore, da 190 a 280 cm di lavoro": i sei dati del modello scelto (si aggiornano con la scelta in alto) e le quattro parti in una riga di testo con filetto sopra (denti doppi, pettini su cinghie trapezoidali, bandella fermafieno, ruote ballon), poi la nota su PRO e gEnio e su come è riportata la foto. Poi la gamma 2x2, la storia con l'archivio a filo, la riga dei rivenditori, la chiusura con la foto in campo, il piede.
A 390: testata con logo, telefono e bottone "Menu"; titolo su due righe, frase, bottone rosso, scelta del modello, la macchina sulla linea di terra: tutto dentro gli 844 px. Da 960 a 1439 la prima schermata scala anche con l'altezza della finestra (a 1366x768 e 1280x720 bottone e linea di terra restano sopra la piega); sotto i 960 si impila.

### Caratteri e colori, con i riferimenti
- Sofia Sans (Lettersoup, Google Fonts), una famiglia sola, file variabile latino servito dalla pagina (`sito/fonts/sofia-sans-latin-var.woff2`). Licenza SIL Open Font License 1.1, testo in `sito/fonts/OFL-Sofia-Sans.txt`: uso commerciale libero. Titoli 380 con spaziatura da -0,025 a -0,035em, testo 400, etichette e titoletti 500; cifre tabellari per modelli, misure e telefono. Motivo: è la scelta della guida per macchine e industria (c1, riferimenti Festool e Metzner), un impianto DIN con più calore, vicino alle scritte delle targhette delle macchine.
- Carta #F3F0E7 (lo stesso fondo su cui sono moltiplicati gli scontornati), piede #E2DDCF con un filetto in cima, inchiostro #1E1D1A, grigio #5D5950 (6,1:1 sulla carta, 5,1:1 sul piede), rosso Molon #C8231B solo per il bottone, il tratto del modello attivo e la barra del lavoro (bianco sul rosso 5,6:1). Riferimenti: Sneeboer (un solo rosso del marchio), Reform (il rosso coerente con le macchine), Pöttinger (la macchina riconoscibile prima di tutto); la pulizia chiara dalle home amate di Mario Agnoletto e Hambro.

### Interazione
Un gesto solo, "Scegli il modello": radio veri (frecce della tastiera, focus visibile, dito), più due caselle. Al cambio la macchina e le due barre cambiano larghezza in 0,18 s (niente con prefers-reduced-motion), si aggiornano la riga sotto i numeri (annunciata con aria-live) e i sei dati della sezione seguente. Versione PRO si spegne dove non esiste (190, 210), è fissa sul 300 PRO e altrove torna com'era stata scelta dal visitatore (variabile separata, provata). gEnio aggiunge 60 kg. Valori della tabella del sito (11-16 pettini, doppi denti 4, 4, 4-5, 5-6 sul PRO, pesi da 210 a 350 kg). Il menu a 390 e il piede a fisarmonica a 390 usano veri bottoni con aria-expanded; sopra i 640 i titoli del piede sono testo semplice, fuori dall'ordine di tabulazione. Nessuna comparsa allo scorrimento, nessun effetto sul cursore, hover a colore pieno.

### Foto, origine e licenza
Tutte dell'azienda, da molonmachinery.com (`assets/originali/`, vedi `assets/CREDITI.md`); nessuna foto di repertorio, nessuna immagine generata, nessuna foto già usata in un'altra home della campagna.
- `macchina-*`: `2017_10_230_5-scont.jpg` (2048x1536, fondo bianco), moltiplicato sulla carta con ombre di contatto; a 1440 è larga al massimo 880 px, quindi la variante da 1780 px basta anche a 2x. Per gli altri modelli la stessa foto è riportata in proporzione alla larghezza massima, e la pagina lo dice nella nota.
- `gamma-*`: `2017_10_RANGHINATORE-POST09noEtichette.jpg`, `2018_01_MAJOR160_sf.jpg` (fondo grigio riportato a bianco), `2017_10_380-2.jpg`, `2017_10_SCOPA-lamiera.jpg`: ritagliate sul loro ingombro (ignorando i puntini isolati), allineate a sinistra come i titoli, stessa linea di terra e stessa ombra; la scala sta a metà tra stessa area e stessa altezza, così il girello piatto e la scopatrice piena pesano uguale.
- `archivio-*`: `2017_10_foto4.jpg`, virata sul tono della carta, tagliata meno di prima.
- `chiusura-*`: `2017_10_11.08_10ritoc.jpg` (3264x2448, la foto migliore dell'inventario, voti 7/7), taglio 4:5 a sinistra: la macchina, l'andana e i due alberi sul crinale. Del portattrezzi restano lo specchio e un pezzo di cabina sul bordo destro, senza marchi leggibili.
- `logo-molon.svg`: ricostruito dal logo piatto grigio, confrontato al 400 % con l'originale.

### Piede
Logo e una riga su chi sono; colonne Prodotti (cinque famiglie e Ricambi), Azienda (Chi siamo, Storia, Rivenditori), Contatti (telefono, fax, email, indirizzo, mappa), Lingua; ultima riga con ragione sociale, indirizzo, P.IVA, Privacy, Cookie, ©. Fondo #E2DDCF con filetto, nessuna ombra, nessuna icona. Nessuna colonna Seguici finché i canali YouTube non sono confermati come ufficiali.
Newsletter: non c'è, perché vendono tramite rivenditori in Italia e all'estero, la pagina News è vuota dal 2017, le fiere non vengono comunicate e il cliente finale compra dal rivenditore; al suo posto la riga dei rivenditori con il telefono.

### Cosa è cambiato nella rifinitura finale (giudizio cieco in `_prova/cieco.json`)
- Prima schermata rifatta dentro la stessa idea: tolte le quattro legende numerate a filetti e la riga "Arlesega di Mestrino (PD), dal 1936" accanto al bottone; il selettore è salito nella prima schermata e la macchina cambia larghezza in scala sopra la linea di terra quotata. Le parti sono scese in una riga di testo sotto la piega.
- Prima schermata scalata anche sull'altezza (`--u` con `100svh`): niente sovrapposizioni tra 1100 e 1366 (provate 960, 1024, 1100, 1200, 1280, 1366, 1440, 1920), bottone sopra la piega a 1366x768 e 1280x720.
- Bug PRO corretto: dal 300 al 260 il PRO si spegne se il visitatore non l'ha scelto; la sua scelta resta passando per 190, 210 e 300.
- "Scegli il modello" al posto di "Scegli la larghezza di lavoro"; la riga sotto i numeri dice i cm veri (300 PRO = 280 cm di lavoro).
- Gamma: scontornati ritagliati e allineati a sinistra, masse pareggiate, righe più vicine; sezione di circa 1100 px a 1440.
- Storia: "2025" diventa "Oggi"; i rivenditori escono dalla colonna e diventano una riga a tutta larghezza con cinque nomi; colonna di testo allineata al fondo della foto.
- Chiusura con la foto 7/7 dell'inventario al posto di quella da telefono.
- Piede: fondo più scuro con filetto; titoli di colonna non più bottoni sul desktop.
- A 390 zone toccabili di almeno 44 px (modelli, caselle, link del piede e dei recapiti, logo), niente riquadro azzurro al tocco.
- Testi: h2 della gamma "Le altre macchine Molon" (non ripete più la frase d'apertura), sottotitolo riscritto; tolti gli indici 01-04 dalle parti.

### Controlli
- Screenshot guardati a pezzi: 1440 intera e prima schermata, 390 intera e prima schermata, chiusura e piede a 1440, più 320x640, 768x1024, 1024x768, 1920x1080 e le prove a 960, 1100, 1200, 1280, 1366 con il 190 e il 300. Larghezza del documento uguale alla finestra a 320, 360, 390, 640, 768, 900, 1024, 1099, 1100, 1280, 1366, 1440, 1920 e 2560.
- Interazione provata con Playwright: frecce e spazio sui radio, spazio sulla casella PRO, sequenze 300-260, 260 PRO-300-260, 190-230; tocco sui modelli a 390; menu con Esc; fisarmonica del piede. Nessun errore in console.
- Link: `tel:+390499000103`, `mailto:info@molonmachinery.com`, Google Maps su "Via Mestrina 10 35035 Arlesega Mestrino PD".
- `segnali.sh` a 1440: 0 soglie da correggere su 10, 0 da guardare su 8; foto al 35,1 %, una famiglia, 14 filetti larghi, 2 fasce di fondo (pagina e piede), H2 in 4 misure. L'unico gradiente sono le tacche della linea di terra.
- Nessun carattere U+2014 nella pagina, negli script, in questa nota e nel LEGGIMI.
