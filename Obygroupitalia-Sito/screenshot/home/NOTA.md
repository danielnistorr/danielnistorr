# Oby Group Italia, nuova home: nota

Versione finale della direzione A, "Ogni traccia", rifinita dopo il giudizio cieco (50/80, non passava). Pagina statica in `sito/index.html` (si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Tutto si rifà con `sh _prova/script/build_finale.sh` (immagini con `finale_img.py`, pagina da `finale-pagina.html`, screenshot; `finale_chiusura.mjs` per la chiusura, `finale_prova_gesto.mjs` per provare il gesto con tastiera, mouse e dito, i link e la misura delle tacche). Le modifiche di questo giro sono scritte in `rifinitura_pagina.py`, che parte dalla copia `finale-pagina-prima-del-giudizio.html`.

Screenshot: `home-1440.jpg` (5663 px compreso il piede), `home-1440-prima-schermata.jpg`, `home-390.jpg` (6631 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`.

## Idea

Il bianco del lavoro finito. La pagina è chiara e ordinata come un ambiente dopo l'intervento, e la prima cosa che si vede è un lavoro loro: la copertura piana rivestita di bianco con la membrana STARFLEX, con il torrino e il parapetto rivestiti, presa dal loro sito. Sopra c'è il titolo "Eliminiamo ogni traccia del danno". Con il nome di un'impresa di bonifica qualsiasi la prima schermata non regge più: la copertura Starflex è il servizio su cui Oby punta dal 2026. Poi la pagina racconta il percorso: il danno (la cucina bruciata) e i nove passaggi del loro pronto intervento, le aree, Starflex, l'azienda, e in chiusura la stanza rifatta con la loro frase "Ti riconsegnamo il tuo bene nelle condizioni originarie".

## Cosa è cambiato dopo il giudizio cieco

- **Apertura rifatta.** Via il respiratore Pexels e i tre richiami a punto e filetto (gesto già visto in altre home della campagna, e non leggevano l'oggetto). Ora il titolo sta sul gesso, su due righe a 108 px; sotto ci sono la riga sui sinistri (incendio, allagamento, grandine, bonifica industriale) e il bottone rosso. Più sotto la copertura Starflex è a tutta larghezza, alta fino al bordo dello schermo, con la didascalia "Fig. 1". Non c'è più il muro grigio #CBCAC5 con lo stacco a y=900: la foto è un rettangolo netto e voluto, e la membrana è il punto più chiaro della pagina. Non ci sono più il logo sul cappuccio a 1024 né la testata sopra la foto.
- **Niente prima e dopo finto.** Il cursore con due ambienti diversi è stato tolto. Pronto intervento ha una sola foto, la cucina dopo un incendio in fascia 21:9 ("il punto da cui si parte"), e sotto il righello dei nove passaggi. La stanza rifatta è passata in chiusura.
- **Chiusura senza tuta né maschera.** Ora c'è la stanza rifatta, pareti bianche e porta finestra, a filo del bordo destro: è quello che la frase promette.
- **Starflex asciugata.** Restano il titolo, il paragrafo, la foto (ora il fibrocemento rivestito accanto al fotovoltaico, l'altra foto Starflex del loro sito, in 5:2) e una sola riga, "30 anni di durabilità certificata per STARFLEX® ULTRA", con il PDF. Le due liste sono passate alla pagina /copertura-sicura-starflex/. Il "30" grande non c'è più.
- **Azienda senza i quattro "fatti".** Restano il titolo e il paragrafo, sfalsato sotto il titolo dalla colonna 7.
- **Un solo registro, il tu**, come nei loro testi: "Chiama lo 0444 1329022", "Cosa succede quando ci chiami", "tocca un numero o scorri il righello".
- **Piede:** ogni voce della colonna Interventi punta alla sua riga (#danni-post-incendio e così via). Privacy e Cookie puntano a /privacy-policy/ e /cookie-policy/.
- **Tacche** alte 48 px a ogni larghezza (a 390 misurano 39x48).
- **Titoli** con `text-wrap: balance`: niente parole sole a fine riga.

## Le prime due schermate

1. **Apertura.** A 1440 si vedono la testata sul gesso (logo, menu, "Uffici 0444 1329022"), il titolo in Onest 300 a 108 px su due righe, il paragrafo a sinistra e il bottone rosso a destra, e da y=504 la copertura a tutta larghezza fino al bordo dello schermo (altezza `100vh - 280px`, minimo 420 px). A 1920 la foto è alta 720 px e il testo resta sulla griglia di 1440. A 390, nei primi 844 px, ci sono la testata con il telefono e un vero bottone Menu, il titolo su tre righe ("Eliminiamo / ogni traccia / del danno"), la copertura in un taglio quadrato centrato sul torrino, la didascalia e il bottone rosso. Tra 641 e 900 px il paragrafo e il bottone vanno uno sotto l'altro.
2. **"Cosa succede quando ci chiami".** Titolo e due righe su 6 colonne, poi la cucina bruciata larga quanto la griglia, poi il righello 01-09 a cifre tabellari. La tacca attiva è rossa e sotto c'è il nome del passaggio. La pagina si apre sul passaggio 01, "Sopralluogo e consulenza nell'immediato".

Poi vengono:
- **Interventi.** Le nove aree vere in una lista a filetti, ognuna con il suo id.
- **Copertura Sicura Starflex.** Titolo a sinistra e paragrafo a destra, la foto a tutta larghezza, una riga e il PDF.
- **Azienda.**
- **Chiusura "b con foto".** Testo a sinistra e stanza rifatta a destra fino al bordo.
- **Piede.**

Un solo fondo per tutta la pagina; il gesso scuro compare solo nel piede.

## Caratteri e colori

- **Onest** (Google Fonts, SIL Open Font License 1.1; licenza in `sito/fonts/OFL.txt`) è l'unica famiglia. È variabile 100-900 e viene servita dalla pagina (`sito/fonts/onest-latin.woff2`, `onest-latin-ext.woff2`). Titoli in 300-340 con spaziatura da -0,03 a -0,045em, testo in 400, etichette in 600, cifre tabellari su tutta la pagina (`tabular-nums`) per telefoni, tacche e "30 anni". Il riferimento sono i titoli enormi di poche parole di Petzl e il registro calmo, in prima persona, di Gasparoli. Onest è un grottesco neutro con curve morbide: serio senza allarme, e non sta nelle liste b della guida. Geist, proposto nell'analisi, è stato scartato perché è il carattere di serie di Next.js e v0.
- **Colori:**
  - gesso #F4F3F0 (fondo) e gesso scuro #EBE9E4 (solo piede);
  - inchiostro #1D1C1B, dal nero del logo #231F20;
  - cenere #64615B per i testi secondari e le tacche non ancora fatte (5,6:1 sul gesso);
  - rosso #C8161D per bottone, telefoni e tacca attiva: è il rosso del logo #E41D25 scurito quanto basta per l'AA con il bianco (5,8:1). Il rosso pieno resta solo nel logo.
  - Il legno di B è stato tolto: un colore d'accento in meno. Nella prima schermata gli unici colori forti sono il rosso del bottone e del logo.
- **Trattamento unico delle foto** (PIL, `finale_img.py`): saturazione da -10 a -20 %, nero sollevato a 16, un velo del 3 % verso il gesso. Le due coperture hanno in più una piccola correzione della dominante blu del cielo; quella dell'apertura ha anche una curva che apre solo i toni alti, così la membrana resta bianca senza bruciare. La cucina ha una schiarita leggera. Ogni foto è esportata in due o tre larghezze con srcset, e al telefono con tagli suoi.

## Interazione

Una sola: il righello dei nove passaggi del loro pronto intervento. Le nove tacche sono veri bottoni in un gruppo con tabindex mobile: un solo tasto Tab per entrare e uscire, le frecce spostano il passaggio e il fuoco, Home e Fine vanno al primo e all'ultimo. Si può toccare una tacca, oppure trascinare il dito o il mouse lungo il righello (pointer events, `touch-action: pan-y`, così la pagina continua a scorrere in verticale). Il nome del passaggio è in un'area `aria-live`, e ogni tacca ha un `aria-label` con il suo passaggio e `aria-current="step"` su quella attiva. Le transizioni riguardano solo il colore delle tacche (.12 s) e il fondo del bottone rosso. Nient'altro si muove: nessuna animazione allo scorrere, nessun effetto che segue il cursore, nessuna dissolvenza.

## Foto: origine e licenza

| In pagina | File sorgente | Origine | Licenza |
|---|---|---|---|
| Apertura (1440 e telefono) | `assets/originali/9e96e5_520d02be…webp` | sito di Oby (forse foto di MPM) | da confermare con l'azienda |
| Pronto intervento, cucina | `assets/esterne/pexels-10252682.jpg` | F. Hektor, Pexels | Licenza Pexels, uso commerciale libero |
| Starflex | `assets/originali/9e96e5_c7d17813…webp` | sito di Oby (forse foto di MPM) | da confermare con l'azienda |
| Chiusura, stanza rifatta | `assets/esterne/pexels-7031621.jpg` | Max Vakhtbovych, Pexels | Licenza Pexels |

Tutte sono già in `assets/CREDITI.md`, con la licenza Pexels verificata sulla pagina della foto. Non ne è stata scaricata nessuna nuova, e nessuna compare nei CREDITI delle altre home della campagna (controllato il 24/10/2026). Nessuna è generata dall'IA e nessuna ha marchi in primo piano. La copertura dell'apertura è tagliata sotto le torri, così l'insegna sul fondo non entra a nessuna larghezza. Nella pagina non c'è più nessuna persona di repertorio. Le foto da rifare dal vero sono nel LEGGIMI.

## Piede

- Logo vettoriale vero (`sito/img/logo-obygroup.svg`, estratto senza ridisegnarlo dalla brochure Starflex 2026) con una riga su chi sono.
- Colonna Azienda: Chi siamo, Pronto intervento, Copertura Starflex, Brochure PDF.
- Colonna Interventi: le nove aree vere, ognuna con il link alla sua riga della lista; su due colonne a 390.
- Colonna Contatti: "Uffici" sopra il telefono in rosso semibold, poi cellulari, email, sede operativa con link alla mappa, sede legale. Tutto è cliccabile.
- Colonna Seguici: solo Facebook, l'unico social trovato.
- Riga legale: ragione sociale, P.IVA e CF, REA, capitale sociale, Privacy (/privacy-policy/) e Cookie (/cookie-policy/).
- A 390 le colonne si impilano in ordine.
- **Niente newsletter:** è un servizio d'emergenza su chiamata e non ha novità periodiche da comunicare. Per le assicurazioni basta il PDF di Starflex.

## Controlli (dopo la rifinitura)

- `segnali.sh` (kit): 0 soglie bloccanti su 10. Foto al 35,8 %, Onest al 100 %, mono 0 %, 11 filetti, 0 frecce, 0 etichette maiuscole, 0 numeri grandi con etichetta, 2 fasce di fondo, una data (2018). Prima della correzione la soglia "titolo a sinistra e paragrafo a destra" segnava due sezioni: Azienda ora ha il paragrafo sotto il titolo, e resta solo Starflex. Due righe da guardare, con il loro motivo:
  - gli H2 hanno due misure (60 e 56 px), perché la pagina punta sul titolo d'apertura da 108 px e sulla foto;
  - c'è una numerazione 01-09, perché sono i nove passi in ordine del loro pronto intervento.
- **Larghezze guardate a pezzi:** 1440, 390, 320, 768, 1024 (prima schermata), 1920. scrollWidth è uguale a innerWidth a 320, 360, 390, 414, 640, 641, 768, 900, 901, 1024, 1100, 1280, 1440, 1680, 1920 e 2560. Nessuna sovrapposizione. A 768 il bottone non va più a capo (`white-space: nowrap`, sotto il paragrafo).
- **Gesto, provato con Playwright** (`finale_prova_gesto.mjs`):
  - a 1440: freccia destra due volte (02, 03), freccia sinistra (02), Fine (09), Home (01), Tab che esce dal righello verso il link del PDF, clic sulla tacca 03, trascinamento dal 5 al 62 % (06); il contorno rosso di 2 px è visibile al fuoco da tastiera;
  - a 390, al tocco: Menu che si apre e si chiude sul link, tacca 09, tacca 05; tacche di 39x48 px.
- **Link:** `tel:+3904441329022`, `tel:+393408349597`, `tel:+393939114656`, `mailto:info@obygroupitalia.com`, due link a Google Maps per via Ghizzole 41, Longare. Nessuna ancora senza destinazione; l'unico `href="#"` è il logo che riporta in cima.
- Nessun U+2014 in pagina, negli script, nella NOTA, nel LEGGIMI e nei CREDITI. Nessun segnaposto in pagina. Ogni fatto viene da `01-analisi.md`.
- **Contrasto AA sui testi:** la cenere sul gesso fa 5,6:1, il grigio del piede #55524D sul gesso scuro 6,4:1, il bianco sul rosso 5,8:1.
- **Peso:** `sito/` pesa 3,8 MB, con 20 immagini JPEG più il logo SVG, tutte usate dalla pagina. La foto d'apertura a 1440 pesa 330 KB: è la texture della membrana, che sotto quella qualità si impasta.
