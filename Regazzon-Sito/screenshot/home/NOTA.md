# F.lli Regazzon, home finale: "Trasmettiamo potenza"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (logo, immagini, pagina, screenshot, misure a otto larghezze, prova dei gesti).

Altezza: 4506 px a 1440, 4800 px a 390, piede compreso.

## L'idea

La copertina della loro brochure, rifatta per lo schermo. Sulla brochure c'è il motto "Trasmettiamo potenza" sopra una corona a dentatura interna vista da vicino, con le marcature incise sul fianco. La home riprende la stessa coppia, frase e foto, che è dell'azienda e di nessun altro. La foto è in macro: l'arco della corona esce dalla pagina in alto, in basso e a destra. Il titolo sta dentro la curva dei denti. Poi la pagina torna al fondo acciaio per reparti, qualità e chiusura. I titoli delle sezioni seguono la serie delle copertine del catalogo: "Trasmettiamo potenza", "Trasmettiamo qualità", "Trasmettiamo esperienza".

## Cosa è cambiato in questo passaggio (2 novembre)

Richiesta del committente: "più roba di alta gamma, meno uguali tra loro". Il giudice cieco: K0 7, K1 6, K6 6 (apertura in formula di campagna), K5 6, totale 55 su 80.

1. **Apertura rifatta dentro la stessa idea.**
   - Via le tre legende numerate con pallino e filetto. Resta una didascalia sobria in basso: "Corona a dentatura interna, con le marcature incise sul fianco. È la foto della copertina della nostra brochure."
   - Al posto del pignone scontornato in basso a destra c'è la foto della copertina della brochure: una macro a tutta altezza, a filo su tre lati. È una foto di Regazzon finora non usata: estratta con pdfimages dalla brochure del sito, 1024x709, il doppio dell'altezza delle strisce del sito.
   - Il titolo va su due righe da 104 px e si incastra nella curva dei denti. Il bordo dei denti è controllato da `finale_controlla.mjs`: almeno 29 px di distanza, nella stima più prudente, a ogni larghezza.
   - La testata diventa una fascia a sé sul fondo acciaio. Sotto comincia la copertina, una lastra fotografica con il bordo netto: il pezzo è tagliato dal bordo della foto, non da una sezione.
2. **Impaginazione che nella campagna non c'è.** Nessuna home della campagna ha un pezzo più grande dello schermo, tagliato a filo su tre lati, con il titolo dentro la curva del pezzo (confronto con `_invio/zona/home/copertine-est-grisignano.jpg` e con le prime schermate di Bertolin, Area Systems, Mario Agnoletto e FM Sistemi). Al telefono la foto viene prima del titolo, come una copertina.
3. **Colore di fondo dal prodotto.** Il fondo è #E9EBEC, il grigio freddo del fondale delle loro still life, preso dalle foto stesse. Non è un beige. La ragione si vede: la chiusura è una still life con il fondale portato esattamente a quel colore (scarto di 1 livello RGB), quindi pezzo e pagina stanno sulla stessa superficie. La copertina tiene il fondale della brochure, schiarito: a sinistra #CDCFD0 circa, dietro al titolo.
4. **Chiusura** (difetto importante): il pezzo è intero, con aria, e i bordi non si vedono più.
   - Impaginazione: testo a sinistra, foto a destra fino al bordo.
   - La foto è pignone e corona dal catalogo (p. 9, 626x604): la stessa still life di prima, ma con il riflesso sul piano. Il fondale è portato al colore della pagina, con 70 px d'aria in più sopra. Il riflesso si spegne negli ultimi 120 px, come su un piano lucido.
   - La corona esce dal bordo destro della pagina.
   - Misurato: ai bordi della foto lo scarto con la pagina è di 1 o 2 livelli RGB.
5. **Fig. 2** (importante): servita alla misura vera, 982 px (ingrandimento 1,0 a 1440), saturazione all'85 %. Ha perso il numero "Fig. 2", perché non c'è più una Fig. 1.
6. **Schede che non saltano** (importante): l'altezza dei dati viene da uno script. Al caricamento e a ogni cambio di larghezza misura il reparto con il testo più lungo. Provato con Playwright cliccando le 8 schede: #reparti resta 918 px a 1440, 742 a 1024, 932 a 390.
7. **Qualità** (minore): `id="qualita"` sta sulla sezione giusta, che ha un titolo suo, "Trasmettiamo qualità".
   - Il testo viene dalla pagina Azienda: materiali, impianti, controlli nelle varie fasi. Sotto c'è il certificato RINA con il PDF.
   - La frase Zeiss non è più ripetuta: resta solo nella scheda Controllo.
   - La riga dei settori è salita in Chi siamo ("Per chi."). Così sparisce il titolo nostro "Lavoriamo per l'industria pesante".
8. **Dentatura, guanto a chiazze** (minore): la zona del guanto, fuori fuoco, è ammorbidita e spenta solo lì, con una maschera sfumata. Nessun taglio della foto.
9. **Foto più calde** (minore): saturazione all'85 % per tutti i reparti (prima 50 %). L'oro del creatore e le scintille restano vivi. Tre schede hanno foto nuove e più nitide dal catalogo 2012 (986x670):
   - Tornitura: gole al tornio verticale;
   - Saldatura: un saldatore al lavoro, quindi una persona in più nella pagina;
   - Controllo: il tastatore Zeiss sui denti.
10. **Menu del telefono** (minore): da aperto il bottone dice "Chiudi". Il menu si chiude con Esc (il fuoco torna al bottone), con un tocco fuori o scegliendo una voce. Dentro il menu ci sono Italiano, English e Deutsch.
11. **1024** (minore): le legende non ci sono più, quindi niente esce dal margine.
12. **HTML del piede** (minore): ricontrollato con un parser. Tutti i tag sono chiusi, nessun errore. La colonna Contatti aveva già `</ul></div>`; ora il piede è scritto su più righe, così si legge.

## Le prime schermate

- **1440x900**:
  - testata alta 96 px sul fondo acciaio;
  - sotto, la copertina alta 804 px: la foto a 1,134 volte, il suo fondale prolungato a sinistra con un modello liscio, cioè lo stesso gradiente continuato e nessun pixel inventato;
  - titolo 500 a 104 px, spaziatura -0,04em, interlinea 0,92; sotto, la riga con moduli e diametri, il bottone "Inviateci il disegno" (mailto con oggetto) e il telefono;
  - didascalia in basso a sinistra.
- **1920 e 2560**: la composizione resta ancorata alla griglia di 1296 px. Il fondale si allunga a sinistra, il pezzo non cresce oltre 1,134.
- **1024x768**: stessa composizione, foto a 0,95 volte.
- **Tra 601 e 900 px**: la foto intera della copertina (1024 px) sopra, poi titolo e testo.
- **390x844 e 320**:
  - un taglio 780x662 sull'arco con le marcature, poi la didascalia, il titolo su due righe a 55 px, il testo e il bottone, tutto nella prima schermata;
  - a 320 il titolo è a 45 px e sta nella riga.

## Caratteri e colori

- **General Sans** (Indian Type Foundry, da Fontshare), pesi 400, 500 e 600, una sola famiglia, file woff2 serviti da `sito/fonts/`.
  - Licenza ITF Free Font License: uso commerciale consentito, anche sul sito. I file non si possono ridistribuire.
  - Riferimenti: il titolo corto e sicuro di RENK, il grottesco pulito delle home amate.
  - Misure: titolo 104 px, H2 44 px, frase di chiusura 96 px, testo 18 px con interlinea 1,55.
  - General Sans non ha cifre tabellari, quindi le misure stanno in frasi, mai in colonne. Cifre, Ø e × sono legati da spazi non separabili.
- **Colori** (contrasti calcolati con la formula WCAG):
  - fondo acciaio #E9EBEC;
  - copertina, a sinistra, circa #CDCFD0;
  - inchiostro #1B1C20, il nero del logo (14,2:1 sul fondo, 10,9:1 sulla copertina);
  - grigio testo #53565B (6,2:1);
  - sabbia #807062, gli ingranaggi del logo, per la riga della scheda attiva;
  - sabbia scura #685A4C per il contatore (5,6:1);
  - didascalia della copertina #3D4045 (6,7:1);
  - piede #DCDFE1, con testi #36393E (8,7:1), #404348 (7,4:1) e #4A4D52 (6,3:1).
  - Niente blu, niente oro del "50 YEARS".

## Il gesto

"Otto reparti, le loro misure": otto schede (Dentatura, Rettifica ingranaggi, Tornitura, Fresatura, Alesatura, Rettifica, Saldatura, Controllo).
- Al clic o al tocco cambiano di colpo la foto, la riga di capacità presa dalle pagine del sito e le marche delle macchine, con il contatore "01 di 08".
- ARIA tablist, tab e tabpanel; frecce, Inizio e Fine; fuoco visibile.
- Le voci Ingranaggi e Lavorazioni del menu aprono Dentatura e Tornitura.
- L'altezza è fissa, quindi la pagina non salta.
- A 390 la striscia delle schede scorre, e l'ultima voce visibile resta tagliata a metà.
- Nessuna dissolvenza, nessuna animazione allo scorrere. Transizioni di 0,12-0,15 s solo sul colore di schede, link e bottoni: il bottone si inverte, non sbiadisce.

## Chiusura e piede

- **Chiusura "Trasmettiamo esperienza"** (motto di catalogo): testo a sinistra, foto a destra fino al bordo.
  - Telefono a 46 px con tel:+39049760969.
  - "Il disegno, anche senza campione: info@regazzon.it", con mailto e oggetto.
  - "Via Lussemburgo 17, 35127 Padova (Camin)", con link a Google Maps.
  - Niente orari (non pubblicati), niente fax.
- **Piede**:
  - logo vero, una riga su chi sono, le lingue;
  - quattro colonne: Azienda, Ingranaggi, Lavorazioni, Contatti con la PEC;
  - riga legale: ragione sociale, P.IVA e C.F., REA PD 123452, capitale sociale 118.800,00 euro i.v., PEC, Privacy, Cookie, Dati legali.
  - Sotto i 600 px diventa una fisarmonica con bottoni veri e aria-expanded; Contatti resta sempre aperta.
  - **Niente newsletter**: è un'officina conto terzi senza novità periodiche da comunicare, con clienti solo aziendali.
  - **Niente "Seguici"**: non hanno social.

## Foto: origine e trattamento

Tutte di F.lli Regazzon Officine Meccaniche S.r.l.: brochure e catalogo 2012 del sito, servizio di Nicola Verardo e Vanni Dalla Via. Nessun segnaposto di repertorio, nessuna foto già usata nella campagna, nessuna immagine generata. Nessuna foto oltre 1,3 volte la sua misura vera.

| In pagina | Origine (`assets/originali/`) | Lavorazione |
|---|---|---|
| apertura | `brochure-copertina-corona-1024x709.jpg` | filtro mediano 3 contro i blocchi JPEG; fondale stimato con un polinomio e schiarito della metà (155 diventa 205), con un peso a tenda che lascia l'acciaio com'è; tela di 900 px a sinistra e 500 a destra; tele alte 804, 709 e 520; foto intera a 1024 per il tablet, taglio 780x662 per il telefono |
| chi siamo | `dentatura-est-2-980x340-.jpg` | saturazione 85 %, 982 px nativi, taglio 3:2 a 780 per il telefono |
| reparti | `dentatura-est-5`, `rettifica-980x340-4`, `catalogo-p10-tornitura-verticale`, `fresatura-regazzon-2`, `alesatura-980x340-1`, `rettifica-980x340-3-copia`, `catalogo-p20-saldatura`, `catalogo-p24-controllo-zeiss` | saturazione 85 % uguale per tutte; guanto della dentatura ammorbidito; 1296x420, 982x318, 4:3 a 780 |
| chiusura | `catalogo-p9-pignone-corona-626x604.jpg` | fondale portato al colore della pagina; 70 px d'aria sopra; riflesso spento in basso; 626 e 814 px |
| logo | `logo-regazzon-da-brochure.svg` | tracciati originali resi in WebP trasparente a 720 px (3x) |

## Controlli (2 novembre)

- Screenshot guardati a pezzi a 1440 e 390; prime schermate a 320, 768, 1024 e 1920 guardate. `scrollWidth` uguale a `innerWidth` a 320, 390, 768, 1024, 1280, 1440, 1920 e 2560. Nessun elemento fuori dalla finestra (`finale_controlla.mjs`).
- `finale_prova.mjs`:
  - schede con clic, frecce, Inizio, Fine e tocco;
  - altezza costante a 1440, 1024 e 390;
  - il menu apre la scheda giusta;
  - menu del telefono: Chiudi, Esc, tocco fuori, lingue presenti;
  - fisarmonica del piede con tocco e Invio, che torna in colonne sopra i 600 px.
- Collegamenti: tutti i `tel:` sono +39049760969, i `mailto:` vanno a info@regazzon.it (con oggetto) e alla PEC, la mappa è un link di ricerca Google Maps su "F.lli Regazzon Via Lussemburgo 17 35127 Padova".
- `segnali.sh` a 1440: 0 soglie bloccanti, 0 da guardare (foto al 39,1 %, una famiglia, 3 fasce, 5 filetti, una sola sezione con titolo a sinistra e testo a destra, nessun numero grande con etichetta).
- HTML ricontrollato con un parser: nessun tag aperto o chiuso male.
- Nessuna lineetta lunga (U+2014) in pagina, negli script, in questa NOTA e nel LEGGIMI. Nessun dato fuori da `01-analisi.md`. I valori in contraddizione restano fuori dalla pagina (vedi `LEGGIMI.md`).

## Respinti

- **"Accanto il pezzo più piccolo e il più grande, in scala relativa vera"** (proposta del giudice): non abbiamo né le misure dei pezzi fotografati né foto dei pezzi estremi (Ø 20 e Ø 2000). Una scala "vera" sarebbe inventata. L'escursione da modulo 0,75 a modulo 25 resta detta in parole sotto il titolo e nella scheda Dentatura.
- **Una persona nella prima schermata**: il committente vuole un solo oggetto vero e grande in apertura. La persona entra con la foto di Chi siamo (alla misura vera) e con la nuova scheda Saldatura.
