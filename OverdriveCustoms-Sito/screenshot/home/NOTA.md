# Overdrive Customs, home: nota

## Livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP a più larghezze con srcset), carattere in `sito/fonts/`. La home com'era prima di questo passaggio (Hagane scontornata sul bianco calce, titolo "Special, dal telaio in su", selettore delle moto) è copiata in `_prova/versione-1-originale/` (sito e screenshot). Per questa azienda non c'era una "versione 1 con l'uso": l'uso è stato preso direttamente dalla scheda `_prova/uso/SCHEDA.md` e risolto qui.

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari) adattata a un'officina di quartiere che lavora su appuntamento, sezione B (difetti delle nostre home), sezione C (15 regole). Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14, le pagine intere di Joseph Brot e Union (a pezzi), più il foglio del committente (`_invio/zona/home/livello-professionale.jpg`) e le note di Unicar e Panificio Fornasiero.

Rifare tutto: `bash _prova/script/build_finale.sh --immagini` (immagini con `pro_img.py`, pagina con `pro_pagina.py` dal modello `pro_pagina.tpl.html`, screenshot con `pro_shot.mjs` all'ora simulata martedì 3 novembre 2026 alle 10, JPEG con `pro_jpg.py`, controlli con `pro_controlli.mjs`, esito in `_prova/pro-controlli.json`). Senza `--immagini` rifà solo pagina, screenshot e controlli.

Screenshot (stessi nomi di prima): `home-1440.jpg` (8777 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (13359 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Orari e dove" al piede), `selettore-1440.jpg` (il selettore non c'è più: ora è la sezione "Le special" che l'ha sostituito), prime schermate a 320, 768, 1024 e 1920, più `menu-390.jpg` (menu aperto). Guardati a pezzi a 390 e 1440 accanto ai riferimenti; pagine intere a 320, 768 e 1024 guardate a pezzi durante il lavoro (non consegnate).

### Com'è fatta, in breve

- **Testata fissa** (80 px a 1440, 64 a 390): logo in corsivo vero, menu "Orari e dove", "Officina", "Trasformazioni", "Le special"; a destra "WhatsApp" con il bordo e "Chiama 340 251 0434" pieno. Sul telefono resta il bottone rosso col numero (sotto 360 px dice "Chiama") e "Menu".
- **Apertura**: occhiello "Vigonovo (VE), Riviera del Brenta · dal 2015", titolo che dice il mestiere "Officina Harley-Davidson e custom giapponesi" (maiuscolo stretto, 88 px a 1440, 40 a 390), la foto vera dell'officina con Matteo, la Sportster e la Envy (sul telefono in alto, a tutta larghezza, senza testo sopra), lo stato di oggi calcolato sull'ora di Roma, "Scrivi su WhatsApp" pieno e "Chiama 340 251 0434" col bordo, "Via San Francesco 8/a, Vigonovo · Indicazioni", "Moto ferma? La vengo a prendere col furgone. Chiedi il ritiro" e la riga di Hagane come prova.
- **In officina** (grigio chiaro): la loro frase "Officina specializzata in customizzazioni, riparazioni, motoristica e restauro...", le marche in tre colonne, tre schede cliccabili con foto vera (tagliandi e gomme, riparazioni e ripristino, restauro) che aprono WhatsApp con il messaggio già scritto; fascia nera "Moto ferma? La vengo a prendere" con il bottone del ritiro.
- **La tua moto, trasformata**: quattro schede per famiglia (Sportster, Softail e Dyna, Touring e bagger, custom giapponesi), ognuna con la foto, cosa è stato fatto, l'anno e un link WhatsApp col messaggio per quella famiglia.
- **Come si comincia** (blocco rosso pieno): i tre passi e "Manda la foto della tua moto".
- **Le special** (blocco nero): la frase di Matteo "I mostri non sono nella vostra testa.... Li creo io!" come manifesto, Hagane grande con le due copertine, Special K e Drakkar, l'albo dei primi posti dal 2018 al 2024.
- **Chi c'è dietro**: ritratto di Matteo, due frasi sue, quattro numeri grandi (2015, 8, 2, 3), "Lavoro con" Cisco Leather, Rolling Paint, Kustomstore.
- **Orari e dove** (grigio chiaro): scheda della sede con indirizzo, stato, tabella degli orari col giorno di oggi in neretto, WhatsApp, Chiama, Indicazioni; le tre fiere dell'anno; Instagram ed email per la stampa; il modulo "Preferisci l'email?" con il tipo di richiesta.
- **Piede** nero in quattro colonne: officina e indirizzo, contatti, orari, link della pagina e Instagram con "il diario dell'officina"; Privacy e Cookie.

### Esito regola per regola (controlli di `_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile**: PASSA. A 390, a metà pagina, il bottone "340 251 0434" sta in alto (48 px) e si tocca; 4 link `tel:` (testata, apertura, sede, piede); la prima voce del menu è "Orari e dove", come "Negozi e orari" della famiglia B.
2. **Prima schermata con mestiere, luogo, prova e azione**: PASSA. 1440x900: "Harley" a 157 px, "Vigonovo" e "dal 2015" a 125, WhatsApp 533-585, più la riga di Hagane (premio e copertine). 390x844: "Vigonovo" e "2015" a 345, "Harley" a 377, WhatsApp 633-685 largo 350 px (tutta la riga), Chiama 695-747, Indicazioni a 764.
3. **Immagine vera nell'apertura**: PASSA. La copertina del sito (2560x1440, Matteo in officina, fascia rossa, cartello TRASPORTO): 801x451 a 1440, 390x260 a 390 (taglio 3:2 su Matteo e la Sportster). Nessuno scontorno.
4. **Zero repertorio**: PASSA. "indicativ" 0; nessuna immagine da banche (i segnaposto Unsplash di `assets/esterne/` non sono usati); nessuna illustrazione.
5. **Foto in serie**: PASSA, con un limite. Le moto sono quasi tutte la stessa serie: di fianco davanti alla lamiera del loro capannone, con lo stesso trattamento (saturazione e contrasto di Instagram attenuati in `pro_img.py`); fanno eccezione la 883 e Special K, nel servizio in studio di @boemphoto, e Hagane nel campo. Tre formati: 16:9 (tutte le schede, Hagane e l'apertura dal tablet in su), 3:2 (apertura sul telefono), 1:1 (copertine e ritratto). Due didascalie (le copertine) su 14 foto.
6. **Palette dal marchio**: PASSA. Nero #151515, bianco #FFFFFF delle pareti, rosso #B3261E della fascia e degli scaffali, verde #22663A solo per "Aperto"; grigi lamiera (#26292C, #5B5F64, #A9ADB2, #D6D7D8, #EFF0F1). Niente fondo `--carta`, niente bianco calce.
7. **Scala corta e leggibile**: PASSA. 1440: 88, 56, 32, 22, 19, 16, 14 px; 390: 40, 36, 28, 20, 17, 16, 14 px (7 misure). Testo 19/17 px; 14 px solo per occhielli, etichette in maiuscolo spaziato e riga legale. H1 88 px maiuscolo, interlinea 0,95 (fascia B: 85-90).
8. **Due famiglie al massimo**: PASSA, con una sola. Archivo: titoli in maiuscolo stretto (larghezza 75 %, peso 800, come le scritte della loro pubblicità e delle fiere), testo, etichette e bottoni a larghezza normale in 400 e 800.
9. **Servizi in schede con la foto del lavoro**: PASSA. "In officina": 3 colonne, 3 schede tutte cliccabili, foto vera di quel lavoro (16:9), nome e link a WhatsApp con il servizio scritto. Sul telefono diventano righe compatte (foto di 120 px, nome, link) per portare prima le trasformazioni. Gomme e riparazioni motori non hanno una foto loro: stanno nelle schede con tagliandi e ripristino.
10. **Almeno tre tipi di prove**: PASSA. Quattro numeri (2015, 8 primi posti, 2 copertine, 3 fiere fisse); fascia "Lavoro con" con didascalia (Cisco Leather, Rolling Paint, Kustomstore rivenditore ufficiale); copertine delle riviste e albo dei premi al posto delle certificazioni, che non hanno. Recensioni: nessuna leggibile nelle fonti, non inventate (LEGGIMI).
11. **Lavori con un nome**: PASSA. Sette special nell'albo con anno, base, premio e fiera; Hagane larga 737 px a 1440 (più di metà pagina) con base, chi ha fatto i pezzi, premio e copertine; quattro trasformazioni con famiglia, anno e lavori fatti. I clienti non hanno il nome: nei post ci sono solo i profili Instagram dei proprietari, che non metto senza permesso.
12. **Ritmo a blocchi**: PASSA. Blocchi pieni oltre al piede: "Come si comincia" in rosso e "Le special" in nero; "In officina" e "Orari e dove" in grigio chiaro; spazio tra le sezioni 120 px a 1440 e 64 a 390; margini 64 e 20 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno (rosso, bianco sul rosso) e con il bordo; raggio 4 px; 52 px (48 in testata); testo 16 px, peso 800. Tutti i bottoni di chiamata hanno il numero, tranne quello della testata sotto 360 px ("Chiama").
14. **Modulo e "dove e quando"**: PASSA. Modulo in home con il tipo di richiesta in caselle (tagliando o riparazione, trasformazione, ritiro della moto ferma, stampa e fiere), nome, telefono, email, moto, messaggio; compone un'email (mailto con oggetto "tipo, nome" e tutti i campi), da collegare a un servizio (LEGGIMI). Scheda della sede con orari in tabella, "Indicazioni" (Google Maps, percorso) e "Chiama". Nessun iframe.
15. **Piede completo**: NON PASSA del tutto. Ci sono nome, indirizzo, telefono, WhatsApp ed email cliccabili, orari, link della pagina, Instagram col sottotitolo, Privacy e Cookie, in 4 colonne a 1440 con testo di almeno 14 px. Mancano ragione sociale e partita IVA, che non sono pubbliche: non le invento, vanno chieste (LEGGIMI). Certificazioni: non ne hanno.

### Uso (scheda `_prova/uso/SCHEDA.md`, paragrafo 8)

- Visitatore 1, telefono 390x844: "Harley-Davidson" e "Vigonovo" sopra 844 px; WhatsApp (`wa.me/393402510434` con "Ciao Matteo, vorrei fissare un appuntamento in officina. La mia moto è: ") alto 52 px a 633 px; `tel:+393402510434` a 695 px; stato di oggi a 545 px: martedì alle 10 "Aperto ora, fino alle 13", alle 14 "In pausa, riapre alle 15:30", venerdì alle 19:30 "Chiuso, riapre martedì alle 9:30", domenica "Oggi chiuso, riapre martedì alle 9:30", lunedì "Oggi chiuso, riapre domani alle 9:30"; nei festivi (fissi e Pasquetta) "Oggi è festa." con l'orario di solito, senza dire se l'officina è chiusa (non lo sappiamo); Indicazioni a 764 px; "furgone" a 922 px con "Chiedi il ritiro" su WhatsApp. Con JavaScript spento si legge "Martedì-venerdì 9:30-13 e 15:30-19. Si riceve solo su appuntamento: scrivimi."
- Visitatore 2: la parola "trasformazioni" nell'apertura porta alla sezione; le quattro famiglie iniziano a 2624 px a 390 (prima Sportster, poi Softail e Dyna, Touring, giapponesi a 3953), ognuna con foto e lavori fatti e un link WhatsApp per la sua famiglia; "Come si comincia" spiega foto su WhatsApp e poi officina; "Manda la foto della tua moto" apre WhatsApp con "Ciao Matteo, ti mando la foto della mia moto: vorrei trasformarla. L'idea è: ".
- Visitatore 3, computer: Hagane con premio, anno e le due copertine nella stessa sezione; le tre fiere col mese; Instagram ed email per la stampa in "Orari e dove" e nel piede.
- Identità: tre frasi di Matteo citate così come le ha scritte ("I mostri non sono nella vostra testa.... Li creo io!", "In molti, visti i tempi, non avrebbero scommesso un euro su questo progetto.", "Non siamo importanti come gli altri...quelli grossi...ma ci siamo anche noi."), più "now better than new" e "artigiani tra Padova e Venezia" dai loro post; si parla in prima persona come Matteo ("La vengo a prendere", "chiedimi"). Tolti lo slogan "Special, dal telaio in su", la newsletter e il bianco calce.

### Controlli generali

- Scorrimento orizzontale: nessuno a 320, 360, 390, 414, 600, 768, 899, 900, 1024, 1099, 1100, 1280, 1440, 1920, 2560 (`pro_controlli.mjs`). Corretti durante il lavoro: a 320 il titolo usciva di 23 px (ora 34 px sotto i 375).
- Sovrapposizioni: nessuna negli screenshot a 320, 390, 768, 1024, 1440, 1920. Corretti durante il lavoro: a 1024 la foto dell'apertura riempiva la prima schermata e i bottoni andavano a capo su tre righe (ora l'apertura si divide in due colonne da 900 px e i bottoni vanno uno sotto l'altro fino a 1099); la scheda "Restauro" rimasta sola su una riga a 768 (ora tre colonne da 760 px); il bottone "Menu" che restava grigio dopo il tocco (gli effetti al passaggio ora valgono solo con il mouse).
- Collegamenti: `tel:+393402510434`; `https://wa.me/393402510434` con dieci messaggi diversi già scritti; `mailto:overdrivecustoms@live.com` (anche con oggetto per la stampa); Google Maps in percorso su "Overdrive Customs, Via San Francesco 8/a, 30030 Vigonovo VE"; Instagram; nessuna ancora rotta. Privacy e Cookie puntano a `/privacy` e `/cookie`, da scrivere.
- Dato strutturato `MotorcycleRepair` (schema.org) con indirizzo, telefono, orari e Instagram.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script nuovi.

### Caratteri e licenze

Archivo (Omnibus-Type), da Google Fonts, file variabile con gli assi di peso e larghezza servito da `sito/fonts/` (woff2 latin e latin-ext), SIL Open Font License 1.1 (`sito/fonts/OFL-Archivo.txt`): uso commerciale libero, si può incorporare e ridistribuire con il sito. È lo stesso carattere della versione 1: cambia solo l'uso (titoli in maiuscolo stretto e pesante, niente più grottesco leggero).

### Non applicato, apposta

- Apertura a tutto schermo con una frase sopra la foto (famiglia B, punto 2): la scheda vuole la foto dell'officina senza testo sopra, e sul telefono i bottoni devono stare nella prima schermata. La foto è grande (801x451 a 1440) accanto al titolo.
- Novità di stagione: non c'è una fonte per la prossima fiera con le date; le fiere fisse sono in "Orari e dove" con il mese, le date "su Instagram".
- Newsletter: tolta, Instagram è il loro canale.
- Recensioni, clienti con il nome, certificazioni, partita IVA: non sono nelle fonti; da chiedere.
- "Il preventivo si fa dopo aver visto la moto": è nella scheda ma da confermare, quindi non è in pagina (LEGGIMI).
- Zona e costo del ritiro col furgone: non scritti da nessuna parte, in pagina c'è solo "scrivimi dove sei".
- Accessori custom e cappellini: una riga in "Lavoro con"; lo shop online citato nel 2023 non l'ho trovato.

---

## Versione 1 originale (24 ottobre 2026), prima del livello professionale

Quello che segue descrive la versione copiata in `_prova/versione-1-originale/`.

Proposta non richiesta di nuova homepage (solo la home). Pagina in `sito/index.html`, immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `_prova/script/build_finale.sh`.

### L'idea
Una moto sola, sul bianco calce, con le legende che dicono chi ha fatto ogni pezzo: è Hagane, la chopper che ha vinto la categoria Metric al Biker Fest 2024 ed è finita in copertina su Kustom World e su Bigtwin. Il titolo è **Special, dal telaio in su**: viene dal loro post del 20/06/2024 ("Frame, front fork, etc.. built by us") e dalla loro parola per queste moto ("costruire special", post del 07/10/2023). Le tre legende fanno il resto: telaio e forcella di Overdrive Customs, motore e ruote da una Suzuki DR650, sella di Cisco Leather. Con il nome di un'altra officina la pagina non regge: la moto, le legende, il titolo e la chiusura sono loro.

Direzione A del prototipo ("La moto sul bianco"), scelta dal giudice; dalla B restano solo la voce (la frase dei mostri, l'H2 "Dal tagliando alla moto da concorso") e la foto vera dell'officina, ora in chiusura.

### Le prime due schermate
- **1440x900**: testata con il logo vero (SVG), menu (Officina, Le moto, Riviste, Dove siamo) e il telefono. Titolo su una riga a 100 px. Sotto, a destra, Hagane scontornata (immagine 867 px compresa l'ombra) con le tre legende in una fila sola, sulla stessa linea di base, e i fili verticali che scendono sui pezzi. A sinistra tre righe su chi sono, il bottone rosso "Chiama 340 251 0434", "Su appuntamento, da martedì a venerdì"; la didascalia di Hagane chiude all'altezza delle gomme.
- **Seconda schermata**: "Dal tagliando alla moto da concorso", la data di apertura (2 maggio 2015), due elenchi brevi (In officina, Su progetto); poi "Le moto premiate".
- **1024 e 768**: la pagina passa alla disposizione del telefono già a 1180 px: titolo, moto larga quanto il contenuto (920 px a 1024), i numeri sui pezzi con l'elenco sotto, poi testo e bottone.
- **390x844**: titolo su due righe a 50 px, Hagane a tutta larghezza con i numeri sui pezzi, l'elenco delle legende subito sotto, poi testo e bottone. Testata con logo, telefono e bottone "Menu".
- Pagina: 5092 px a 1440 (piede compreso), 5595 px a 390.

### Come è fatto lo scontorno
Script `_prova/script/finale_taglio.py`, solo pixel della foto originale (Instagram, 1080 px), niente generato:
- gomme e cerchi come ellissi vettoriali misurate sulla foto (`fit_ruote.py`), con sfumatura di 1 px;
- ruota davanti: ogni raggio è trovato sulla foto tra la flangia del mozzo e il cerchio, assestato al decimo di pixel e reso come linea piena e continua, del rosso bruno misurato sui raggi veri (prima erano puntinati);
- ruota dietro: disco, corona e catena tenuti per colore; i fori dell'erba hanno ora bordi tondi e puliti;
- gomme: il riflesso grigio sul fianco destro della gomma dietro è abbassato al tono della gomma; nella parte bassa delle due gomme, dove passava l'erba, il colore resta scuro e neutro; i puntini scuri sui cerchi rossi sono chiusi col rosso vicino;
- telaio: il tubo verticale dietro il motore, bucato dalla catena, è chiuso con i bordi misurati sulla foto;
- bordo del corpo levigato a doppia misura, colori del bordo presi dall'interno; bordo alto del serbatoio come curva liscia; tono: rosso meno saturo, neri più profondi, HDR attenuato; ombre morbide di contatto.
È ancora una foto da 1080 px: a 867 px regge, da vicino si vede il limite del file. La strada vera è nel LEGGIMI (originale del fotografo o scatto in studio).

### Caratteri e colori
- **Archivo** (Omnibus-Type, Google Fonts), un solo file variabile con gli assi di peso e larghezza, servito da `sito/fonts/` (woff2 latin e latin-ext). Licenza **SIL Open Font License 1.1** (`sito/fonts/OFL-Archivo.txt`): uso commerciale libero, si può incorporare e ridistribuire con il sito. Titoli a larghezza 106 % in peso 500, spaziatura da -0,03 a -0,035em; testo 400 a 17-19 px, interlinea 1,55; etichette e bottoni 600; cifre tabellari per telefono, anni e orari. Niente monospazio, niente corsivo, nessun secondo carattere. Riferimento: il grottesco largo dei marchi del mondo custom (Revival Cycles, la scheda "THE RELOAD 650" di Roland Sands) e i caratteri piccoli e ordinati di Auto Fabrica; il corsivo resta solo nel logo.
- **Colori**: bianco calce `#F3F1EC` (fondo), inchiostro `#151515`, grigio delle note `#5F6267` (5,4:1 sul calce), un solo accento rosso officina `#B3261E` sul bottone, sul punto della moto scelta e sul fuoco da tastiera; piede `#151515` con testo `#ECE9E2` e note `#AEABA4` (8:1), segnaposto della newsletter `#9C998F` (6,4:1), filo del campo `#8A8780` (5,1:1); bianco sul rosso del bottone 6,5:1. Tutto sopra AA.

### Interazione
Un gesto solo, in "Le moto premiate": quattro schede (Envy 2019, Drakkar 2021, Special K 2022, 883 Old Style 2023) cambiano la foto e il testo del premio con un cambio netto, senza dissolvenza. Si apre su Special K (foto in studio, chiara come l'apertura; la Envy è già nella foto della chiusura). Tablist vero: clic, dito, frecce, Home e Fine; con Tab si entra solo nella scheda attiva; il testo del premio è annunciato agli screen reader; il fuoco si vede (bordo rosso). I nomi delle moto nel piede aprono la scheda giusta.
Sotto i 900 px la testata ha un bottone "Menu" vero (`aria-expanded`, `aria-controls`): apre i quattro link a 66 px d'altezza l'uno, si chiude con un tocco su un link, con "Chiudi" o con Esc (il fuoco torna sul bottone). Le transizioni (0,15 s) sono solo cambi di colore su ciò che si tocca: nessuna animazione allo scorrere, nessun effetto sul cursore, nessun elemento che sbiadisce.

### Foto: origine e licenza
Solo foto dell'azienda, dal sito e dal profilo Instagram @overdrive_customs (`assets/originali/`, voti in `_prova/inventario-immagini.json`). Nessun segnaposto di repertorio, nessuna foto nuova scaricata, nessuna immagine generata dall'IA. Lavorate con PIL e OpenCV ed esportate in WebP a più larghezze con `srcset`, mai oltre la misura del file (tranne l'apertura, a doppia misura levigata dallo scontorno).
- Apertura: Hagane nel campo, `feed/20240522_C7QjkJVIRt0.jpg` (post del 22/05/2024, autore non indicato), scontornata.
- Selettore, riquadro fisso 3:2 largo al massimo 720 px. Envy `feed/20181121_BqcLrvEgKvp.jpg` e Drakkar `feed/20210816_CSo4M02INbn.jpg`, tutte e due di fianco davanti alla stessa lamiera grigia, con l'HDR attenuato e un filo più chiare; la Drakkar era 1080x617, la lamiera sopra il manubrio è allungata di 103 px specchiando e allungando le sue prime 50 righe (la moto non è toccata). Special K `feed/20230828_Cwfiz3-oi3b.jpg` e 883 Old Style con Matteo `feed/20231202_C0Wverwo_GZ.jpg` (foto @boemphoto), servizio in studio su fondo bianco, a 720 e 704 px.
- Copertine: Kustom World agosto 2024 (`feed/20240819_C-20QVBoqJR.jpg`) e Bigtwin aprile 2025 (`feed/20250327_DHsQHfYN4bp.jpg`).
- Chiusura: la copertina del sito di oggi, `copertina-sito-original.jpg` (2560x1440, Matteo in officina con la Envy e una Sportster, autore da chiedere), a tutta larghezza in 16:10, a 1440 mostrata a 1440 px CSS.
- Ogni moto compare una volta sola, tranne Hagane (apertura e le due copertine, che sono la prova) e la Envy (selettore e foto dell'officina, lontane).
- Licenza: sono foto dell'azienda e di fotografi terzi; le copertine sono delle riviste. Prima di pubblicare servono i permessi (vedi LEGGIMI).

### Chiusura e piede
- Chiusura "b con foto", testo sopra e foto a tutta larghezza sotto: a sinistra la frase loro, "I mostri non sono nella vostra testa: li creo io" (post del 07/10/2023, "I mostri non sono nella vostra testa.... Li creo io!", punteggiatura adattata), e sotto "Sempre tanta voglia di fare e costruire special." (stesso post); a destra i recapiti: numero grande con `tel:`, WhatsApp, indirizzo con il link a Google Maps, orari e "Solo su appuntamento", email con `mailto:`. Sotto, la foto dell'officina con una didascalia.
- Piede: logo SVG ricostruito (fedele) con una riga su chi sono; colonne Officina, Le moto, Contatti, tutte della stessa misura; newsletter "Fiere e moto nuove" con email, bottone e consenso privacy, perché l'officina ha fiere fisse ogni anno, moto nuove presentate lì e clienti privati; sotto, "Seguici" con il solo Instagram (Facebook tolto finché non è confermato). Non invia nulla finché non si collega a un servizio (LEGGIMI). Ultima riga: nome, indirizzo, Privacy (`/privacy`), Cookie (`/cookie`); ragione sociale, P.IVA e REA non sono pubblici e vanno aggiunti appena Matteo li dà. A 768 le tre colonne in fila e la newsletter sotto; a 390 Officina e Le moto in due colonne, poi Contatti, poi la newsletter.

### Rifinitura dopo il giudizio cieco (ultimo passaggio)
Giudizio: K0 7, K6 6, non passava. Difetti, uno per uno:
1. **Titolo** (bloccante): "Il telaio lo facciamo noi" ricalcava la formula di Recinzioni Formentin. Ora "Special, dal telaio in su"; "facciamo noi" non c'è più in pagina.
2. **Scontorno** (bloccante): raggi davanti come linee piene, riflesso della gomma dietro abbassato, tubo del telaio chiuso (già avviati nel passaggio interrotto, verificati e tenuti); in più fori della ruota dietro puliti, parte bassa delle gomme ripulita, puntini sui cerchi chiusi. Resta il limite del file da 1080 px.
3. **Foto della chiusura** (importante): via la foto da 640 px; ora la copertina del sito da 2560 px a tutta larghezza.
4. **Envy doppia e fascia dell'officina** (importante): la fascia dopo "Dal tagliando alla moto da concorso" è tolta (la foto è andata in chiusura); il selettore si apre su Special K.
5. **Menu sotto i 900 px** (importante): bottone "Menu" con `aria-expanded` e `aria-controls`, provato con tocco, Invio, Tab ed Esc a 390 e 768.
6. **Foto del selettore disomogenee** (importante): la Drakkar nel negozio con le insegne è sostituita da una foto di fianco davanti alla lamiera; Envy e Drakkar con HDR attenuato. Ora due coppie coerenti (lamiera, studio); il servizio unico da rifare è nel LEGGIMI.
7. **Legende** (minore): tre legende con un fatto ciascuna (chi ha fatto il pezzo), nessuna ripete il titolo.
8. **La Morelia** (minore): tolta dai primi posti (resta da confermare nel LEGGIMI).
9. **Didascalia di Hagane** (minore): "Prima nella categoria Metric al Biker Fest di Lignano".
10. **1024** (minore): da 901 a 1180 px la disposizione impilata, moto a 920 px.
11. **Piede** (minore): Facebook tolto, Seguici sotto la newsletter, colonne della stessa altezza, Privacy e Cookie su `/privacy` e `/cookie`.
12. **"Le moto premiate"** (minore): titolo a sinistra e testo a destra sulla stessa riga, foto e schede che partono alla stessa altezza; niente più vuoto sopra la lista.
Per la soglia delle foto (paragrafo f) le copertine sono un po' più grandi (8 colonne) e la foto della chiusura è in 16:10: area coperta da foto 36 %.

### Controlli
- `_metodo/kit/segnali.sh` sulla pagina finale: 0 soglie bloccanti su 10, 0 da guardare su 8. Foto 36 % dell'area, Archivo 100 %, monospazio 0 %, 2 filetti, 0 frecce, 0 titoli col punto, 3 misure di H2, 2 fasce di fondo, date presenti.
- `_prova/script/finale_prove.mjs` (dentro `build_finale.sh`): larghezza del documento uguale alla finestra a 320, 360, 390, 414, 560, 600, 768, 900, 901, 1024, 1180, 1181, 1280, 1366, 1440, 1680, 1920 e 2560; selettore provato con frecce, Home, Fine e Tab, e con il tocco a 390; menu provato con tocco, Invio, Tab ed Esc; i nomi del piede aprono la scheda giusta; nessuna ancora rotta.
- Collegamenti: `tel:+393402510434`, `https://wa.me/393402510434`, `mailto:overdrivecustoms@live.com`, Google Maps su "Via San Francesco 8/a 30030 Vigonovo VE", Instagram.
- Risoluzione: a DPR 1 nessuna immagine è mostrata oltre la sua misura. A DPR 2 e 3 restano morbide le foto del selettore (file da 720 px) e un poco le copertine e la foto della chiusura a 1440x2 (2880 px chiesti, 2560 nel file): servono gli originali (LEGGIMI).
- Screenshot guardati a pezzi a 1440 e 390, più le prime schermate a 320, 768, 1024 e 1920 e il menu aperto a 390.
- Nessun U+2014 nella pagina, in questa nota e nel LEGGIMI; nessun segnaposto in pagina; nessun dato senza fonte in `01-analisi.md`.
- Divieti: niente gradienti viola, testo in gradiente, emoji, Inter, card con bordo colorato, vetro, badge, tre box con icona, Lucide, shadcn, dissolvenze, effetti sul cursore, bottoni che sbiadiscono, lineette lunghe, parole da brochure, corsivi d'accento.
