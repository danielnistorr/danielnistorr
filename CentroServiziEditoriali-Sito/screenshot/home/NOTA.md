# Home finale, "Giornali in rotativa"

## Idea
La home è impaginata come una prima pagina. In alto c'è il nome del mestiere, "Giornali in rotativa", come una testata. Sotto c'è il filetto doppio dei giornali, con la riga dei dati veri al posto della data: Grisignano di Zocco e Imola, 2 rotative Goss Universal, 4 torri colore e 64 pagine a colori, broadsheet, tabloid e rivista. Poi viene la foto grande a tutta larghezza delle loro copie appena piegate, con la mano guantata che ne prende una (foto 69 del reportage di Grisignano).

L'oggetto in apertura è il prodotto che esce dalle loro macchine, non la materia prima. La bobina, che avvicinava la pagina a quella di una cartiera, scende a metà pagina come fascia.

La carta poi si segue all'indietro: formati, bobina, lavorazioni, e in chiusura il nastro che corre tra i rulli.

## Cosa è cambiato in questo giro (dal giudizio cieco)
- **Apertura rifatta**:
  - via la bobina scontornata con il "foglio" piatto dietro, e via le legende a puntino uguali a quelle di Agnoletto;
  - ora ci sono la testata, il filetto doppio con la riga dei dati e la foto delle copie a tutta larghezza;
  - il testo e il bottone stanno a destra del titolo, allineati al suo piede: a 1440 non resta il quadrante vuoto in basso a sinistra;
  - fra 961 e 1180 px il testo va sotto il titolo, con il bottone a destra;
  - a 390 la foto è un taglio 5:4 sulla pila centrale e sul guanto, e tutta la prima schermata sta negli 844 px.
- **Legende**: niente più dati sulla foto. La Goss compare solo nella riga dei dati e nei formati; la grammatura resta solo nel paragrafo delle carte, dove la dice il loro sito.
- **Bobina**: diventa la fascia 2:1 a metà pagina, con la foto 13 intera e la luce vera. Niente scontorno, niente levigatura, niente grana sintetica. Esportata fino a 2560 px dall'originale.
- **Chiusura**: la foto è il nastro tra i rulli (foto 24), a filo del bordo sinistro. "Tre sedi, oltre 10.000 m²", con Grisignano, Imola (Galeati dal 1816, rilevata nel 2014) e Mestre, sta sopra i recapiti. La sezione "Sedi" separata non c'è più, e l'ancora `#sedi` ora porta alla chiusura.
- **Lavorazioni**:
  - "per chi" (editori, free press, GDO, concessionarie) va accanto al titolo;
  - le tre voci hanno la stessa gerarchia (h3 a 30 px, riga di dati, testo) e un filetto in testa;
  - "Dalla borsa alla TV, dal meteo all'oroscopo" diventa la riga di dati di Grafica e redazione.
- **Formati**:
  - la quota del tabloid ha due linee: 37 sulla quota interna e 44 su una quota esterna che va da 0 a 44, con ogni numero al centro del suo segmento;
  - i nomi delle sagome non attive sono in #6B675F (4,6:1 sulla carta) invece di #9D988E (2,4:1).
- **Piede**:
  - fondo #DED8CC con un filetto pieno in inchiostro in testa e margine di 96 px;
  - a 390 le colonne vanno una sotto l'altra, in ordine;
  - "Contatti" non è più ripetuto: è tolto da Azienda e il titoletto della colonna porta a `contatti.html`;
  - link esterni finali in https (galeati.it, litostampaveneta.it, 3d-venice.com), senza rel=noopener inutile.
- **Testata sotto 960 px**: il bottone diventa "Chiudi" a menu aperto e in fondo al menu c'è il telefono con tel:.

## Prime due schermate
- **1440** (`home-1440-prima-schermata.jpg`):
  - testata con il logo vero, cinque voci e il telefono;
  - titolo su una riga a 111 px, a destra il testo e il bottone rosso "Chiama lo 0444 414303";
  - filetto doppio e riga dei dati;
  - dalla quota 424 la foto delle copie, che riempie il resto della schermata.
- **390** (`home-390-prima-schermata.jpg`):
  - titolo su due righe, testo, bottone a tutta larghezza;
  - filetto doppio e riga dei dati su tre righe;
  - la foto 5:4 fino a 828 px.
- **Pagina intera**:
  - ordine: apertura, formati, fascia della bobina, lavorazioni, chiusura, piede;
  - altezze: 5098 px a 1440, 5946 a 390, 6144 a 320, 6111 a 768, 4754 a 1024, 5744 a 1920.

## Piede
- Il logo PNG/WebP a 2x, con una riga su chi sono.
- Quattro colonne: Azienda, Lavorazioni, Gruppo (con ↗ sui tre link esterni, dal CSS) e Contatti.
- La riga legale con ragione sociale, P.IVA, C.F. e Registro Imprese, REA e capitale, poi Privacy e Cookie.
- **Niente newsletter**: il lavoro è B2B su commessa per editori, concessionarie e GDO. Il blog è vuoto e non ci sono fiere, cataloghi o clienti privati da avvisare.
- **Niente "Seguici"**: le icone Facebook e LinkedIn del sito di oggi puntano a `#` e non abbiamo trovato pagine social.

## Caratteri e colori
- **Carattere**: Piazzolla, una famiglia sola (Huerta Tipográfica, Google Fonts, SIL Open Font License 1.1, testo in `sito/fonts/OFL-Piazzolla.txt`). È servito dalla pagina: `sito/fonts/piazzolla-latin.woff2`.
  - Scelta: è nata per lo spazio stretto della stampa quotidiana, cioè per il loro prodotto, e regge da sola la testata.
  - Uso: titoli 390-440 con spaziatura negativa, testo 400, enfasi 500-560, cifre tabellari su misure, grammature, telefoni e dati legali.
- **Colori**:
  - carta #ECE9E2, inchiostro #171615;
  - grigio piombo #56544F: 6,2:1 sulla carta e 5,3:1 sul piede;
  - piede #DED8CC;
  - rosso del logo scurito a #B4001B, solo sul bottone (bianco su rosso 7,1:1). Il verde resta nel logo.
- **Riferimenti**:
  - Graphius e Pureprint: far vedere il prodotto stampato, non la fabbrica;
  - Favini: un solo materiale, luce chiara;
  - dalla campagna: chiaro, un solo oggetto grande, poche sezioni.

## Interazione
- Un solo gesto: tre bottoni Broadsheet, Tabloid e Rivista, con `aria-pressed`. Il bottone scelto riempie la sua sagoma nel disegno in scala, mostra le quote e aggiorna la misura scritta (`aria-live`). Il cambio è netto.
- A meno di 960 px c'è un bottone "Menu" o "Chiudi" vero, con `aria-expanded`.
- Il primo tasto Tab porta a "Vai al contenuto".
- Non ci sono animazioni allo scorrere né effetti al cursore. L'hover cambia colore pieno, mai l'opacità. Il riflesso blu del tocco è tolto.

## Foto: origine e licenza
- **Tutte dell'azienda**, dal reportage del centro stampa di Grisignano (libreria media del loro sito). Nessun segnaposto esterno, nessuna immagine generata.
  - **69, le copie**: taglio 1960 × 1040 per lo schermo largo, taglio 5:4 da 1100 px per il telefono. L'arancio sfocato a destra è fuori, il polsino blu è spento verso il grigio.
  - **13, la bobina**: fascia 2:1 da 2560 px, foto intera.
  - **24, il nastro**: taglio quasi quadrato, con il corpo blu a destra tagliato fuori.
- **Trattamento comune**: neri appena sollevati, medi più chiari, colore smorzato verso la carta. WebP in più larghezze con srcset. Script: `_prova/script/finale_img.py`.
- **Limite**: la foto delle copie, tagliata, è larga 1960 px: a 1920 è a 1x. Va rifatta in alta risoluzione (vedi LEGGIMI). I diritti del reportage sono da confermare.

## Controlli
- **`finale_check.mjs`** a 320, 390, 768, 1024, 1440 e 1920: nessuno scorrimento orizzontale, nessun testo fuori finestra o sovrapposto, nessun U+2014; 9 link tel: e 2 mailto:.
- **`finale_prove.mjs`**:
  - scrollWidth uguale a innerWidth da 320 a 2560, a passi di 40 px;
  - con la tastiera: il primo Tab va a "Vai al contenuto", Invio su Broadsheet e Spazio su Rivista aggiornano disegno, misura e `aria-pressed`;
  - con il tocco a 390: Rivista cambia il disegno, il menu si apre con "Chiudi" e il telefono e si chiude scegliendo una voce;
  - collegamenti: tel:+390444414303, +390542646711 e +390412517416, mailto:info@centroservizieditoriali.it, Google Maps su via del Lavoro 18, i tre siti del Gruppo; nessuna ancora senza destinazione.
- **Screenshot guardati a pezzi** a 320, 390, 768, 1024, 1440 e 1920. Corretti in corsa:
  - a 1024 il bottone andava a capo nella colonna stretta: ora il testo va sotto il titolo;
  - a 768 la riga dei dati andava a capo in modo irregolare: ora è su due colonne;
  - il testo d'apertura a 1440 era troppo vicino alla testata.
- **`segnali.sh`**: 0 soglie bloccanti e 0 da guardare.
  - Area foto 38,1 %.
  - H2 di tre misure (58, 49 e 15 px).
  - Piazzolla al 100 %, 11 filetti, 0 frecce nel testo, una sola sezione con titolo a sinistra e paragrafo a destra (Lavorazioni).
- Nessun U+2014 nella pagina, in questa NOTA e nel LEGGIMI.
