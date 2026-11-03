# Overdrive Customs, home: nota

## Livello professionale, con il ritocco finale (3 novembre 2026)

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP a più larghezze con srcset), carattere in `sito/fonts/`. La home di prima del livello professionale (Hagane scontornata sul bianco calce, titolo "Special, dal telaio in su", selettore delle moto) è in `_prova/versione-1-originale/`; quella del primo passaggio professionale, prima di questo ritocco, è in `_prova/pro-controllo/` (screenshot del controllore: home-1440-prima.jpg, home-390-prima.jpg e le pagine intere a pezzi).

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari) adattata a un'officina di quartiere che lavora su appuntamento, sezione B (difetti delle nostre home), sezione C (15 regole). Riferimenti guardati di nuovo per il ritocco: le prime schermate a 1440 e 390 di tutti e 14 (`riferimenti.jpg`, `rif-tutti-390.jpg`, `rif-altri-1440.jpg`) e le pagine intere di Union e Joseph Brot, a pezzi.

Rifare tutto: `bash _prova/script/build_finale.sh --immagini` (immagini con `pro_img.py`, pagina con `pro_pagina.py` dal modello `pro_pagina.tpl.html`, screenshot con `pro_shot.mjs` all'ora simulata martedì 3 novembre 2026 alle 10, JPEG con `pro_jpg.py`, controlli con `pro_controlli.mjs`, esito in `_prova/pro-controlli.json`). Senza `--immagini` rifà solo pagina, screenshot e controlli. Misure rapide delle posizioni: `node _prova/script/ritocco_misure.mjs`.

Screenshot (stessi nomi di prima): `home-1440.jpg` (10567 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (14085 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Orari e dove" al piede), `selettore-1440.jpg` (la sezione "Le special", che ha preso il posto del selettore), prime schermate a 320, 768, 1024 e 1920, `menu-390.jpg` (menu aperto). Guardati a pezzi a 1440 e 390; prime schermate a 320, 768 e 1024 guardate una per una.

### Che cosa è cambiato nel ritocco

- **Apertura** (era lo schema delle home della campagna, titolo a sinistra e foto 801x451 a destra): ora è un blocco nero. Sul computer l'occhiello "Vigonovo (VE), Riviera del Brenta · dal 2015" e il titolo bianco "Officina Harley-Davidson e custom giapponesi" (88 px) stanno in alto su tutta la larghezza; sotto, su una riga, lo stato di oggi e i due bottoni; poi la foto vera dell'officina a tutta larghezza (1440x706, taglio 2,04:1 che tiene il cappello di Matteo e le ruote), larga al massimo 1600 px. Sotto la foto una fascia nera in quattro colonne con filo rosso: ritiro col furgone, indirizzo e Indicazioni, i lavori dell'officina, la prova "1° al Biker Fest 2024" con le copertine. A 1440x900 la foto occupa 1440x461 della prima schermata (prima 801x451). Sul telefono resta l'ordine voluto dalla scheda (foto in alto senza testo sopra, poi titolo, stato, WhatsApp, Chiama), ora su nero; "Moto ferma?" sale subito sotto i bottoni.
- **Testata nera** con logo bianco, menu, "WhatsApp" col bordo e "Chiama 340 251 0434" pieno; nel menu del telefono ci sono anche "Moto ferma? Ritiro" e "Come si comincia".
- **Scala**: testo corrente a 17 px a 1440 (prima 16); titoli delle sezioni principali a 56 px a 1440 e 28 a 390 (prima tutti a 32); il manifesto "I mostri non sono nella vostra testa.... Li creo io!" a 88 px su tutta la larghezza; "La tua moto, trasformata" ha l'intestazione al centro, titolo e testo uno sotto l'altro. Tolto il grigio dai testi lunghi (resta solo nelle note di una riga).
- **Trasformazioni**: la scheda Sportster ora è la Sportster 48 "Jericho" davanti alla lamiera (post del 08/01/2021), come le altre tre; la 883 con Matteo, in studio, è passata tra le special. Sul telefono le schede sono righe compatte (miniatura e titolo, testo e link sotto) e le quattro schede stanno a 2474, 2740, 3005 e 3294 px, con le etichette delle famiglie a 2487, 2753, 3018 e 3307 (prima 2839, 3250, 3685, 4167). La foto non è più un link: il link è "Ho una Sportster: scrivimi", alto 44 px. La scheda Softail dice i lavori dei post (cambio a mano "suicide shift", ruota da 21 pollici, scarichi Vance & Hines su una Dyna).
- **Le special**: tre racconti grandi alternati, foto 737 px a 1440: Hagane (foto a sinistra), Drakkar (a destra, con il kit di @killer.custom e la vernice "Carraragray"), 883 Old Style (a sinistra). Special K, dello stesso servizio in studio della 883, sta accanto all'albo dei primi posti.
- **Prove**: "3 copertine: Bikers Life 2021, Kustom World 2024, Bigtwin 2025" (prima "2", in contrasto con la scheda di Drakkar); nuova fascia "Riviste che hanno pubblicato le nostre moto" (Ferro 2015, Bikers Life dal 2018, Kustom World 2018-2024, Special Cafe 2023, Bigtwin 2025).
- **Come si comincia**: il passo 3 ora è un passo ("Si costruisce qui, con artigiani tra Padova e Venezia: selle di Cisco Leather, vernici di Rolling Paint"); sotto il bottone "Si apre WhatsApp con il messaggio pronto: allega la foto con la graffetta e invia."
- **Piccoli**: link della fascia d'apertura e del piede con un'area da toccare di 44 px; "Lavoro con" con i testi attaccati al nome; bottoni "Chiama 340 251 0434" senza il doppio stacco; nei festivi "Oggi chiuso per festa, riapre ... alle 9:30"; "Solo su appuntamento: scrivimi prima di passare" nel corpo normale, non più grigio; il messaggio WhatsApp principale è neutro ("Ciao Matteo, ti scrivo per la mia moto. È una: ").

### Esito regola per regola (controlli di `_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile**: PASSA. A 390, a metà pagina, il bottone "340 251 0434" sta in alto (top 8, alto 48 px) e si tocca; 4 link `tel:` (testata, apertura, sede, piede); la prima voce del menu è "Orari e dove".
2. **Prima schermata con mestiere, luogo, prova e azione**: PASSA. 1440x900: "Vigonovo" e "dal 2015" a 121 px, "Harley" a 153, WhatsApp e Chiama a 349-401. 390x844: "Vigonovo" e "2015" a 345, "Harley" a 377, WhatsApp 633-685 largo 350 px, Chiama 695-747.
3. **Immagine vera nell'apertura**: PASSA. La copertina del sito (2560x1440, Matteo in officina, fascia rossa, cartello TRASPORTO), a tutta larghezza: 1440x706 a 1440, 390x260 a 390. Nessuno scontorno.
4. **Zero repertorio**: PASSA. "indicativ" 0; nessuna immagine da banche (i segnaposto Unsplash di `assets/esterne/` non sono usati); nessuna illustrazione al posto delle foto.
5. **Foto in serie**: NON PASSA del tutto. Formati: 3 a 1440 (2,04:1 l'apertura, 16:9 le schede e i racconti, 1:1 copertine e ritratto) e 3 a 390 (3:2, 16:9, 1:1); 2 didascalie su 15 foto. La luce invece non è una sola e con le foto che hanno non può esserlo: ho raggruppato le foto per serie (officina e trasformazioni tutte di fianco davanti alla lamiera grigia, con lo stesso trattamento di `pro_img.py`; la 883 e Special K, servizio in studio di @boemphoto, vicine tra le special), ma restano Hagane nel campo al sole e il ritratto in bianco e nero. Serve la mezza giornata di foto descritta nel LEGGIMI.
6. **Palette dal marchio**: PASSA. Nero #151515, bianco #FFFFFF delle pareti, rosso #B3261E della fascia e degli scaffali, verde #22663A solo per "Aperto" (sul nero dell'apertura lo stesso verde schiarito, #7BD88F, per leggerlo); grigi lamiera (#26292C, #5B5F64, #A9ADB2, #D6D7D8, #EFF0F1). Niente `--carta`.
7. **Scala corta e leggibile**: PASSA. 1440: 88, 56, 32, 22, 19, 17, 14 px; 390: 40, 36 (numeri dei passi), 28, 20, 17, 16, 14 px. Testo corrente 17-19 px a 1440 e 16-17 a 390; 14 px solo per occhielli ed etichette in maiuscolo spaziato e la riga legale. H1 88 px maiuscolo, interlinea 0,95.
8. **Due famiglie al massimo**: PASSA, con una sola. Archivo: titoli in maiuscolo stretto (larghezza 75 %, peso 800), testo, etichette e bottoni a larghezza normale in 400 e 800.
9. **Servizi in schede con la foto del lavoro**: PASSA. "In officina": 3 colonne, 3 schede tutte cliccabili con foto 16:9 di quel lavoro, nome e link a WhatsApp. Le trasformazioni sono lavori e non servizi: lì la foto non è un link (richiesta della prova d'uso) e il link è in fondo alla scheda.
10. **Almeno tre tipi di prove**: NON PASSA. Dei quattro tipi della regola ce ne sono due: 4 numeri aziendali (2015, 8 primi posti, 3 copertine, 3 fiere fisse) e la fascia dei fornitori con didascalia ("Lavoro con": Cisco Leather, Rolling Paint, Kustomstore). In più ci sono prove forti fuori dai quattro tipi: la fascia delle 5 riviste, le copertine, l'albo dei primi posti. Recensioni con nome e comune e clienti con il nome non sono nelle fonti (Paginegialle e Cylex 403, Facebook senza login): non le invento, sono nel LEGGIMI tra le cose da chiedere. Con tre recensioni vere della scheda Google la regola passa.
11. **Lavori con un nome**: PASSA. Tre racconti con nome, anno, luogo (la fiera) e 2-3 dati, ognuno con la foto a 737 px su 1440 (più di metà pagina): Hagane 2024, Drakkar 2021, 883 Old Style 2023 (il file della 883 è di 704 px, mostrato a 737). In più Special K, l'albo di 7 righe e 4 trasformazioni con l'anno. Il cliente non ha il nome: nei post ci sono solo i profili Instagram dei proprietari, che non metto senza permesso.
12. **Ritmo a blocchi**: PASSA. Blocchi pieni oltre al piede: apertura nera, "Come si comincia" rossa, "Le special" nera; "In officina" e "Orari e dove" grigio chiaro, trasformazioni e "Chi c'è dietro" bianche. Spazio tra le sezioni 120 px a 1440 e 64 a 390; margini 64 e 20 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno (rosso; bianco sul rosso) e con il bordo; raggio 4 px; 52 px (48 in testata); testo 17 px a 1440 e 16 a 390, peso 800. I bottoni di chiamata hanno il numero (sotto 360 px quello della testata dice solo "Chiama").
14. **Modulo e "dove e quando"**: PASSA. Modulo in home con il tipo di richiesta in 4 caselle, nome, telefono, email, moto, messaggio; compone un'email (mailto con oggetto "tipo, nome" e tutti i campi), da collegare a un servizio (LEGGIMI). Scheda della sede con orari in tabella e il giorno di oggi in neretto, "Indicazioni" (Google Maps, percorso), "Chiama" e WhatsApp. Nessun iframe.
15. **Piede completo**: NON PASSA del tutto. Ci sono nome, indirizzo con Indicazioni, telefono, WhatsApp ed email cliccabili, orari, link della pagina, Instagram col sottotitolo, Privacy e Cookie, in 4 colonne a 1440 con testo di almeno 14 px e link alti 44 px. Mancano ragione sociale e partita IVA, che non sono pubbliche: non le invento (LEGGIMI). Certificazioni: non ne hanno. Privacy e Cookie puntano a `/privacy` e `/cookie`, pagine da scrivere (oggi 404 anche sul sito attuale).

In sintesi: 12 regole passano, 3 no (5 per la luce delle foto, 10 per le recensioni, 15 per la P.IVA). Tutte e tre dipendono da materiale che l'azienda deve dare.

### Uso (scheda `_prova/uso/SCHEDA.md`, paragrafo 8), dopo il ritocco

- **Visitatore 1, telefono 390x844**: "Harley-Davidson" e "Vigonovo" sopra 844 px; WhatsApp (`wa.me/393402510434`, "Ciao Matteo, ti scrivo per la mia moto. È una: ") alto 52 px a 633; `tel:+393402510434` a 695; stato di oggi a 545: martedì alle 10 "Aperto ora, fino alle 13. Solo su appuntamento: scrivimi prima di passare. Oggi 9:30-13 e 15:30-19."; alle 14 "In pausa, riapre alle 15:30"; venerdì alle 19:30 "Chiuso, riapre martedì alle 9:30"; domenica "Oggi chiuso, riapre martedì alle 9:30"; lunedì "riapre domani"; 8 dicembre e Pasquetta "Oggi chiuso per festa, riapre domani alle 9:30". "Moto ferma? La vengo a prendere col furgone. Chiedi il ritiro" a 767-823 (prima 925, fuori dalla prima schermata); "Indicazioni" a 826 (prima 764: ora sta sul bordo della prima schermata, sempre con un tocco). Link della fascia con area da toccare di 44 px (prima 17). Riesce come prima, il ritiro meglio.
- **Visitatore 2**: le quattro famiglie a 2474, 2740, 3005 e 3294 px: entro tre scorrimenti (3376 px) c'è un caso per famiglia con la foto e il titolo, anche senza passare dal menu (prima riusciva solo col menu). "Come si comincia" ha la sua voce nel menu; "Manda la foto della tua moto" apre WhatsApp con "Ciao Matteo, ti mando la foto della mia moto: vorrei trasformarla. L'idea è: " e la nota dice di allegare la foto. Toccare la foto di una scheda non apre più WhatsApp. Riesce meglio.
- **Visitatore 3, computer**: Hagane con premio, anno e le due copertine nello stesso racconto; Drakkar e la 883 con fiera e anno; le tre fiere col mese; Instagram ed email per la stampa in "Orari e dove" e nel piede. Riesce come prima.
- **Identità**: le frasi di Matteo citate così come le ha scritte ("I mostri non sono nella vostra testa.... Li creo io!", "In molti, visti i tempi, non avrebbero scommesso un euro su questo progetto.", "Non siamo importanti come gli altri...quelli grossi...ma ci siamo anche noi.", "now better than new", "artigiani tra Padova e Venezia"); prima persona di Matteo. L'apertura nera con la foto grande dell'officina dice "officina custom" e non più "servizio".

### Controlli generali

- Scorrimento orizzontale: nessuno a 320, 360, 390, 414, 600, 768, 899, 900, 1024, 1099, 1100, 1280, 1440, 1920, 2560 (`pro_controlli.mjs`).
- Sovrapposizioni: nessuna negli screenshot a 320, 390, 768, 1024, 1440, 1920. Corretto durante il lavoro: a 1440 il titolo andava su tre righe accanto ai bottoni (ora titolo su tutta la larghezza e bottoni sulla riga sotto); i link nel testo della fascia d'apertura con l'area di 44 px spezzavano l'interlinea (ora l'area è fatta con il padding).
- Collegamenti: `tel:+393402510434`; `https://wa.me/393402510434` con dieci messaggi diversi già scritti; `mailto:overdrivecustoms@live.com`; Google Maps in percorso su "Overdrive Customs, Via San Francesco 8/a, 30030 Vigonovo VE"; Instagram; nessuna ancora rotta (nuove: `#ritiro`, `#comincia`).
- Dato strutturato `MotorcycleRepair` (schema.org) con indirizzo, telefono, orari e Instagram.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.

### Caratteri e licenze

Archivo (Omnibus-Type), da Google Fonts, file variabile con gli assi di peso e larghezza servito da `sito/fonts/` (woff2 latin e latin-ext), SIL Open Font License 1.1 (`sito/fonts/OFL-Archivo.txt`): uso commerciale libero, si può incorporare e ridistribuire con il sito.

### Non applicato, apposta

- Foto dell'apertura a tutta larghezza senza niente sopra fino al bordo della prima schermata (come Union e Joseph): a 1440x900 i bottoni devono stare nella prima schermata, quindi titolo e bottoni stanno sopra la foto, sul nero. Testo sopra la foto: no, la scheda vuole la foto senza testo e le pareti bianche non reggono un titolo bianco.
- Spostare "Orari e dove" prima di "Chi c'è dietro" (prova d'uso, minore): lo stato di oggi, gli orari brevi, l'indirizzo e Indicazioni sono già nella prima schermata; la tabella completa resta vicino al modulo e al piede, e il menu ci porta con un tocco.
- Novità di stagione: non c'è una fonte per la prossima fiera con le date.
- Recensioni, clienti con il nome, certificazioni, partita IVA, "il preventivo si fa dopo aver visto la moto", zona e costo del ritiro: non sono nelle fonti o sono da confermare; nel LEGGIMI.
- Newsletter: no, Instagram è il loro canale.

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
