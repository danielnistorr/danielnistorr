# Home di Molon Giovanni

## Livello professionale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso), struttura A1 adattata a un costruttore di macchine da fieno che vende tramite rivenditori. Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14, le pagine intere di barth e Cly-Del (a pezzi). Scheda d'uso: `_prova/uso/SCHEDA.md`.

Questa home sostituisce "Il pettine" (versione 1, copiata com'era in `_prova/versione-1-originale/` con sito e screenshot). Per Molon non c'era ancora una versione 1 con l'uso: i compiti della scheda (par. 8) sono stati risolti in questa passata.

Pagina: `sito/index.html` (statica, si apre con file:///), immagini WebP in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (logo `finale_logo.py`, immagini `pro_img.py`, pagina da `pagina-pro.html`, screenshot `pro_shot.mjs`, controlli `pro_controlli.mjs`). Altezza: 11.080 px a 1440, 16.093 a 390.

### Che cosa resta della versione 1 e che cosa cambia
- Restano il titolo "Ranghinatori a cinghie", Sofia Sans (una famiglia), il rosso Molon #C8231B, il logo SVG ricostruito, la foto del frontale in collina (`2017_10_11.08_10ritoc.jpg`, la migliore che hanno), l'archivio e la tabella dei frontali.
- Via la carta beige #F3F0E7, lo scontornato grande su fondo chiaro in apertura, la stessa foto del 230 riportata in scala per fingere gli altri modelli, il selettore animato, i 21 link "#", Tracmaster tra i rivenditori, le lingue nascoste nel Menu a 390.
- Struttura (M adattata): testata con lingue e telefono; apertura con mestiere, luogo, prova, foto vera e tre ingressi per mezzo; Ricambi (antracite); le tre famiglie con le loro tabelle; girelli e scopatrici; come lavora e i numeri (rosso pieno); rivenditori; chi siamo con archivio e squadra (antracite); contatti con il telefono grande e il modulo; piede in quattro colonne.

### Le prime schermate
- **1440 x 900**: testata fissa di 80 px (logo, cinque voci, IT DE EN FR, bottone rosso "049 900 0103"). A sinistra occhiello rosso "Arlesega di Mestrino (PD) · dal 1936", H1 "Ranghinatori a cinghie" a 64 px con la riga "per portattrezzi, trattori e motofalciatrici, dal 1967" a 24, frase loro ("Rivoltano l'erba, la mettono in andana e allargano l'andana..."), "Chiama 049 900 0103" pieno e "Ricambi" bordato. A destra la foto vera 3:2. Sotto, tre schede per mezzo con lo scontornato della famiglia, il numero dei modelli e le larghezze: tutto entro i 900 px.
- **390 x 844**: testata fissa di 72 px con logo, bottone del telefono con il numero e Menu; lingue IT DE EN FR a vista (44 px di tocco); la foto 16:9 a filo; occhiello, H1 a 40 px, riga del mestiere; "Chiama 049 900 0103" e "Ricambi" in una fila a tutta larghezza; i tre ingressi per mezzo come bottoni grandi. Tutto senza scorrere.
- **1024 x 768 e 960-1099**: apertura a due colonne come a 1440, menu nel bottone. **768**: testo, ingressi, poi la foto. **320**: i due bottoni dell'apertura vanno uno sotto l'altro a tutta larghezza; il telefono in testata perde l'icona.

### Le 15 regole, una per una
Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** Testata `sticky` di 81 px a 1440 e 73 a 390; bottone pieno alto 48 px con il numero. Al 50 % della pagina il bottone è a 12-16 px dall'alto e `elementFromPoint` lo trova (si tocca). 6 link `tel:`, tutti `tel:+390499000103`. Per M c'è anche la voce Contatti con il modulo.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa, con una riserva a 390.** H1 con il mestiere, "Arlesega di Mestrino (PD)", "dal 1936" e "dal 1967", bottone di chiamata in vista a 1440 e a 390. A 390 il bottone "Chiama" occupa 197 dei 350 px perché divide la fila con "Ricambi", come chiede la scheda: la fila è a tutta larghezza e il telefono è anche nella testata. A 320 è a tutta larghezza.
3. **Immagine vera nell'apertura: passa.** Il frontale Molon rosso al lavoro sul prato in collina davanti a un portattrezzi, con l'andana. Nessuno scontornato in apertura.
4. **Zero repertorio: passa.** `indicativ` 0, `unsplash|pexels` 0 nella pagina; in `sito/img/` solo foto dell'azienda e il logo. Le Pexels di `assets/esterne/` non sono usate (vedi `assets/CREDITI.md`).
5. **Foto in serie: passa, con riserva.** Tre formati a ogni larghezza (3:2, 4:3, 16:9); 1 didascalia su 12 immagini (la squadra). Le foto in campo hanno lo stesso trattamento (saturazione 0,92, contrasto 1,04), gli scontornati lo stesso fondo grigio e la stessa linea di terra; l'archivio è in bianco e nero neutro, senza viraggi. Riserva: sono scatti di anni e mani diversi (2017, 2025, archivio, squadra a luce piatta); la serie vera chiede la giornata di riprese del LEGGIMI.
6. **Palette dal marchio: passa.** `--rosso` #C8231B (la vernice delle macchine, da confermare il codice) con `--rosso-scuro` solo per il passaggio del mouse; `--antracite` #1F2122 dal logo; il resto sono grigi neutri freddi (`--grigio` #F0F1F1, `--linea`, `--testo-2`, `--nero` del piede). 0 colori scritti fuori da `:root`. Nessun beige.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 20, 24, 32, 48, 64, 96) e 8 a 390 (14, 16, 18, 20, 24, 28, 40, 48); testo corrente 17 px a 1440 e 16 a 390; nessun testo sotto i 14 px; H1 64/40, H2 48/28 (fascia M).
8. **Due famiglie al massimo: passa.** Una sola, Sofia Sans, pesi 400 e 700 (titoli 700, testo 400).
9. **Schede con la foto: passa a 1440.** Griglia di 3 colonne nell'apertura, ognuna con lo scontornato vero della sua famiglia (stesso taglio 3:2, stesso fondo), nome, misure, freccia; tutta la scheda è un link alla tabella. Sotto i 1100 px le foto delle schede si tolgono e restano bottoni grandi (lo chiede la scheda d'uso per il telefono). Girelli e scopatrici: due schede orizzontali con foto, link alle pagine di oggi.
10. **Almeno tre tipi di prova: non passa (2 su 4).** Ci sono i numeri aziendali (1936, 1967, 100-280 cm di lavoro, 3.000 m² coperti, 5,0 su Google con 8 recensioni) e la fascia dei partner con il paese e il sito. Mancano le recensioni con nome e comune (i testi su Google non sono leggibili), clienti con il nome e certificazioni: non sono nelle fonti e non sono stati inventati (LEGGIMI).
11. **Lavori con un nome: non passa.** Nessun lavoro con cliente, luogo e anno nelle fonti (LEGGIMI). Al loro posto le tabelle dei 25 modelli, che per un costruttore sono la prova più utile.
12. **Ritmo a blocchi: passa.** Blocchi pieni oltre al piede: Ricambi e Chi siamo in antracite, Come lavora in rosso Molon; Posteriori, Girelli e Contatti in grigio. Sezioni 120/120 px a 1440 e 72/72 a 390; contenitore di 1280 px con margini di 80 a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno rosso e bordato (sul rosso: pieno bianco), raggio 4 px, 52 px (48 in testata), testo 17 px (16 sul telefono); tutti i bottoni di chiamata contengono "049 900 0103".
14. **Modulo e "dove" per il mestiere: passa.** Modulo con tipo di richiesta (ranghinatore per il mio mezzo, ricambio, listino e ordini per rivenditori, altro), nome, azienda, email, telefono, paese e zona, presa di forza, marca e modello del mezzo, modello e anno dalla targhetta, messaggio; i bottoni "Va sul mio mezzo?" scelgono il tipo. L'allegato del disegno di A6 qui è la foto del pezzo e della targhetta: un mailto non porta allegati, quindi la pagina dice di allegarle all'email che si apre (il servizio vero è nel LEGGIMI). Sede con "Vai alla mappa" e "Indicazioni stradali" (Google Maps); nessun iframe.
15. **Piede completo: non passa del tutto.** Quattro colonne (marchio, macchine, contatti, rivenditori e lingue), testo di almeno 14 px, ragione sociale, indirizzo, P.IVA 00258060284, telefono ed email cliccabili, mappa, Privacy e Cookie. Mancano gli orari (non pubblicati) e le certificazioni (nessuna nota): da chiedere. La ragione sociale S.r.l. o S.n.c. è da confermare.

### Compiti della scheda d'uso (par. 8)
- **Contadino, 390 x 844.** Vede il frontale Molon al lavoro, "Ranghinatori a cinghie" e il bottone "Motofalciatrici e motocoltivatori": un tocco e trova MINI, MIKY e MAJOR con larghezze e pesi, poi la tabella dei 10 modelli. **Riesce.** "Va su un Reform a 540 giri?": i giri sono scritti in chiaro ("qualsiasi trattore agricolo con presa di forza a 540 o 1000 giri/minuto"), le marche no, perché vanno confermate da Molon; al loro posto "Va sul mio mezzo? Chiedete a noi" apre il modulo con il tipo già scelto. **Riesce a metà.** Rivenditore per l'Alto Adige: Gasser con il sito; per il Tirolo e la Svizzera "chiamateci: vi diciamo a chi rivolgervi" con il bottone. **Riesce a metà** (mancano i telefoni dei rivenditori). Tedesco: DE a vista nella prima schermata, un tocco (porta alla versione tedesca del sito di oggi). **Riesce.**
- **Proprietario con guasto, 390 x 844.** "Ricambi" e il telefono senza scorrere, un tocco chiama. **Riesce.** Un tocco porta al blocco Ricambi con le tre cose da dire (targhetta, foto, numero sull'esploso). **Riesce**, senza gli orari (non pubblicati). "Manda la foto per email" apre la posta con oggetto "Ricambio Molon" e la traccia; WhatsApp non c'è finché non lo confermano. **Riesce.**
- **Rivenditore, 1440 x 900.** Le tre famiglie e il telefono nella prima schermata; un clic porta alla tabella dei frontali con pettini, doppi denti, lavoro, larghezza massima e peso. **Riesce**; mancano attacchi per marca e verso della presa di forza (da chiedere). Depliant PDF: non esiste; al suo posto "Datenblatt auf Deutsch" e "Data sheet in English" sotto ogni tabella (le pagine di oggi). **Riesce a metà.** Email e telefono in testo copiabile, e "Siete un rivenditore? Listino, ordini e configurazioni" con l'email già intitolata. **Riesce.**
- **Per tutti**: 0 link "#", nessuna foto di repertorio, nessuna immagine riscalata a fingere un altro modello, nessuno scorrimento orizzontale, zone toccabili di almeno 44 px (resta sotto solo il link nascosto "Vai al contenuto").

### Foto, origine e trattamento
Tutte di Molon Giovanni, da molonmachinery.com (`assets/originali/`, voti in `_prova/inventario-immagini.json`):
- `apertura-*` e `apertura-tel-*`: `2017_10_11.08_10ritoc.jpg` (3264 x 2448), tagli 3:2 e 16:9, al massimo 1600 px.
- `frontale-lago-*`: `2017_10_11.08_4-copia.jpg` (2000 x 1500), 4:3.
- `major-prato-*`: `2025_03_dok-tc-07-molon-br.jpg` (4032 x 3024, orientamento EXIF corretto), 4:3.
- `archivio-*`: `2017_10_foto4.jpg`, 4:3, bianco e nero neutro.
- `squadra-*`: `2017_10_P1090586_mod-1.jpg`, 16:9.
- `s-*`: gli scontornati `2017_10_230_5-scont.jpg`, `2017_10_RANGHINATORE-POST09noEtichette.jpg`, `2018_01_MAJOR160_sf.jpg`, `2017_10_girello-380.jpg`, `2017_10_SCOPA-lamiera.jpg`, moltiplicati sul grigio #F0F1F1 a parità di massa, 3:2.
Nessuna foto mostra macchine di altri costruttori in primo piano; i portattrezzi e il trattore verde non hanno marchi leggibili.

### Caratteri e licenze
Sofia Sans (Lettersoup, Google Fonts), file variabile latino servito dalla pagina (`sito/fonts/sofia-sans-latin-var.woff2`), SIL Open Font License 1.1, testo in `sito/fonts/OFL-Sofia-Sans.txt`: uso commerciale libero.

### Fonti dei dati in pagina
`01-analisi.md` (storia, numeri, recapiti, partner, testi loro), `_prova/uso/SCHEDA.md` (portattrezzi, compiti), e le tabelle dei modelli lette il 3/11/2026 sulle pagine di molonmachinery.com (`_prova/crawl/`: frontali, posteriori, motofalciatrici, girelli, scopatrici), le stesse che 01-analisi riassume per intervalli. Le frasi tra virgolette sono loro. "100-280 cm" è l'intervallo delle tabelle (MINI 100, 300 PRO).

### Controlli fatti (3/11/2026)
- Screenshot guardati a pezzi: 1440 intera e prima schermata, 390 intera e prima schermata, chiusura a 1440; più 320 x 640, 768 x 1024, 1024 x 768 (prima schermata e intere). Confrontati con barth e Cly-Del: stessa idea di blocchi pieni, numeri in fascia, schede con l'oggetto vero, piede scuro in quattro colonne.
- Larghezza del documento uguale alla finestra a 320, 390, 768, 1024 e 1440; 0 sovrapposizioni tra elementi a tutte e cinque.
- Link: `tel:+390499000103` (6), `mailto:info@molonmachinery.com` (5, di cui ricambi e listino con oggetto e traccia; il modulo compone il suo), Google Maps su "Molon Giovanni Via Mestrina 10 35035 Arlesega PD" e indicazioni verso "Via Mestrina 10 35035 Arlesega Mestrino PD". Lingue e schede in tedesco e inglese puntano alle pagine vere del sito di oggi.
- Modulo provato: senza nome ed email avvisa e porta il fuoco sul primo campo vuoto; i bottoni "Va sul mio mezzo?" scelgono il tipo; menu del telefono con Esc. Nessun errore in console.
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
