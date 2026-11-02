# F.lli Regazzon, home finale: "Trasmettiamo potenza"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (logo, immagini, pagina, screenshot, misure). Base: prototipo A (`_prova/home/a/`), con le indicazioni del giudice applicate una per una.

Altezza: 4817 px a 1440, 4804 px a 390, piede compreso.

## L'idea

Il loro motto di catalogo, "Trasmettiamo potenza", sopra il loro pezzo vero: il pignone che ingrana con la corona, dal servizio still life di Regazzon. Il punto dove i denti si toccano è il motto detto dalla fotografia, e porta l'unica legenda col pallino pieno. Con il nome di un concorrente la pagina non regge: motto, pezzo, legende, misure e macchine sono loro.

## Le prime due schermate

- **1440x900, ripensata** (il K0 del prototipo era 7). Prima il titolo stava a sinistra e un secondo blocco di testo a destra: due fuochi. Ora c'è una sola colonna di lettura. Il titolo corre su una riga sola a 124 px, da margine a margine, come la riga di copertina del catalogo. Sotto, a sinistra, una riga con moduli e diametri, il bottone "Inviateci il disegno" (mailto con oggetto) e il telefono. In basso a destra c'è il pezzo, con le tre legende allineate su un'unica riga di richiamo, da sinistra a destra: 1 Mozzo scanalato, 2 Ingranamento (pallino pieno), 3 Corona dentata. La Fig. 1 è tolta, perché le legende dicono già cosa si vede.
- **Nitidezza**: la foto è ingrandita al massimo di 1,3 volte (1199x445 px da 922x342). Per dare aria al testo ho tolto 60 px di corona a destra. Il resto della prima schermata è il fondale della foto, prolungato con PIL: un modello liscio del suo stesso gradiente, nessun pixel inventato. A 1920 il pezzo resta a 1,3 volte e cresce solo il fondale. Sui fianchi dei denti c'è una maschera di contrasto leggera, con soglia alta perché non faccia aloni.
- **Raccordo in basso**: gli ultimi 72 px della tela sfumano nel colore carta della sezione dopo, così il pezzo non è più tagliato di netto.
- **Seconda schermata a 1440**: il paragrafo su chi sono, accorciato a tre righe a 36 px ("Lavoriamo sul disegno del cliente, con o senza campionatura: ingranaggi dal piccolo al medio pesante, cremagliere speciali, riduttori in piccole serie."). Sotto c'è la Fig. 2, larga quanto il contenuto (1296 px), con saturazione al 60 % e la didascalia "Corona dentata in reparto, più alta di chi la regge.".
- **390x844**: testata con logo, telefono e Menu, titolo su due righe a 55 px, la riga dei moduli, il bottone e il telefono. Sotto c'è il taglio sull'ingranamento con le legende 1 e 2, in quest'ordine. Il pezzo intero sta nella prima schermata.
- **Tra 601 e 900 px** si tiene la composizione grande: pezzo in basso a destra a 0,75 volte (quindi nitido) e legende 1 e 2. Sotto i 600 px si passa al taglio per il telefono.

## Caratteri e colori

- **General Sans**, Indian Type Foundry, scaricato da Fontshare. Licenza ITF Free Font License, che consente l'uso commerciale. Pesi 400, 500 e 600, una sola famiglia, file woff2 serviti da `sito/fonts/`. La licenza permette di usarlo sul sito ma non di ridistribuire i file: vanno tenuti fuori da archivi pubblici.
  - Riferimenti: il titolo corto e sicuro di RENK (Termina 600) e il grottesco pulito delle home amate (Hambro, Mario Agnoletto).
  - Misure: titolo 500 a 124 px con spaziatura -0,037em, H2 500 a 44 px, testo 400 a 18 px con interlinea 1,55, frase di chiusura a 96 px.
  - General Sans non ha cifre tabellari, quindi le misure stanno in frasi e in righe, mai in colonne. Cifre, Ø e × sono legati da spazi non separabili.
- **Colori**:
  - fondo carta #F2F2F0, e #FAFAF9 dove converge il fondale in alto;
  - inchiostro #1B1C20, il nero del logo;
  - grigio testo #55585D (6,4:1 su carta);
  - sabbia #807062, gli ingranaggi del logo, per la riga della scheda attiva;
  - sabbia scura #6B5D4F per i numeri delle legende e del contatore (5,6:1, AA);
  - piede #E7E7E4, con testi #3A3D42 (8,7:1) e #4E5156 (6,4:1).
  - Niente blu, niente oro del "50 YEARS".
- Riferimenti per l'impianto:
  - David Brown Santasalo: un pezzo solo regge la prima schermata.
  - RENK: la frase corta.
  - Mario Agnoletto: legende sottili sul pezzo vero.
  - FM Sistemi in chiaro: titolo sopra e oggetto sotto.

## Il gesto

"Otto reparti, le loro misure": otto schede (Dentatura, Rettifica ingranaggi, Tornitura, Fresatura, Alesatura, Rettifica, Saldatura, Controllo).
- Al clic o al tocco cambiano di colpo la foto, la riga di capacità presa dalle pagine del sito e le marche delle macchine, con il contatore "01 di 08".
- Tastiera e lettori di schermo: ruoli ARIA tablist, tab e tabpanel; frecce, Inizio e Fine; fuoco visibile.
- Le voci "Ingranaggi" e "Lavorazioni" del menu aprono la scheda Dentatura e la scheda Tornitura.
- A 1440 la foto è alta 420 px, così schede, foto e riga di capacità stanno in una schermata.
- A 390 la striscia scorre e lo spazio tra le voci si regola perché l'ultima voce visibile resti tagliata a metà, senza sfumature. La foto passa a un taglio 4:3.
- Nessuna dissolvenza, nessuna animazione allo scorrere. Transizioni di 0,12-0,15 s solo sul colore di schede, link e bottoni: il bottone si inverte, non sbiadisce.

## Chiusura e piede

- **Chiusura "Trasmettiamo esperienza"** (motto di catalogo): testo sopra e foto a tutta larghezza sotto.
  - Telefono a 46 px con tel:+39049760969.
  - "Il disegno, anche senza campione: info@regazzon.it", con mailto e oggetto.
  - "Via Lussemburgo 17, 35127 Padova (Camin)", con link alla mappa.
  - Niente orari (non pubblicati), niente fax.
  - La foto è il giunto dentato della copertina del catalogo, l'unico pezzo intero del servizio: a 1,3 volte, sul suo fondale prolungato a destra e a sinistra. Non è la foto che compare sopra.
- **Piede**:
  - logo vero, una riga su chi sono, le lingue;
  - quattro colonne: Azienda, Ingranaggi, Lavorazioni, Contatti con la PEC;
  - riga legale: ragione sociale, P.IVA e C.F., REA PD 123452, capitale sociale 118.800,00 euro i.v., PEC, Privacy, Cookie, Dati legali.
  - Sotto i 600 px diventa una fisarmonica con bottoni veri e aria-expanded; Contatti resta sempre aperta. Senza JavaScript le colonne restano impilate e aperte. Tra 601 e 900 px le quattro colonne restano in fila.
  - **Niente newsletter**: è un'officina conto terzi senza novità periodiche da comunicare, con clienti solo aziendali.
  - **Niente "Seguici"**: non hanno social.

## Foto: origine e licenza

Tutte di F.lli Regazzon Officine Meccaniche S.r.l., scaricate dal loro sito (servizio still life e foto di reparto del catalogo 2012, "Photo: Nicola Verardo, Vanni Dalla Via"). Nessun segnaposto di repertorio, nessuna foto già usata nella campagna, nessuna immagine generata. I segnaposto di `assets/esterne/` non sono usati.

| In pagina | Origine (`assets/originali/`) | Lavorazione |
|---|---|---|
| apertura | `dentatura-est-4-980x340.jpg` | tagliata a 922 px, 1,3 volte, fondale prolungato, raccordo in basso; tela 2560 e 1820 px, taglio 780 per il telefono |
| Fig. 2 | `dentatura-est-2-980x340-.jpg` | saturazione 60 %, 1296 e 982 px, taglio 3:2 per il telefono |
| reparti | `dentatura-est-5`, `rettifica-980x340-4`, `tornitura-980x340-7`, `fresatura-regazzon-2`, `alesatura-980x340-1`, `rettifica-980x340-3-copia`, `saldatura-980x340-2`, `controllo-dimensionale-regazzon-2` | saturazione 50 % uguale per tutte; nella dentatura verde e arancio spenti di più, l'oro del creatore attenuato; 1296x420, 982x318, 4:3 a 780 |
| chiusura | `dentatura-est-1-980x340.jpg` | saturazione 60 %, 1,3 volte, fondale prolungato ai lati; tela 2560 e 1820, taglio 780x520 |
| logo | `logo-regazzon-da-brochure.svg` | tracciati originali resi in WebP trasparente a 720 px (3x) |

## Controlli

- Screenshot guardati a pezzi a 1440 e 390, e prime schermate a 320, 768, 1024 e 1920. Nessuno scorrimento orizzontale a nessuna larghezza (`finale_controlla.mjs`), nessun elemento fuori dalla finestra, nessuna sovrapposizione tra testo e legende.
- `finale_prova.mjs`: schede provate con clic, frecce, Fine e tocco; il menu apre la scheda giusta; la fisarmonica del piede funziona con tocco e Invio e torna in colonne sopra i 600 px.
- `segnali.sh` a 1440: 0 soglie bloccanti, 0 da guardare (foto al 45,5 %, una famiglia, 3 fasce, 5 filetti, nessuna freccia, nessun numero grande con etichetta).
- Nessuna lineetta lunga (U+2014) in pagina, negli script e nei .md. Nessun dato fuori da `01-analisi.md`. I valori in contraddizione restano fuori dalla pagina (vedi `LEGGIMI.md`).
