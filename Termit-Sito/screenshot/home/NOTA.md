# Termit, home finale: nota

Pagina: `sito/index.html` (statica, si apre con file:///). Immagini in `sito/img/` (JPEG e WebP in più larghezze), caratteri in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh` (immagini, pagina, screenshot). Altezza: 5491 px a 1440, 6231 px a 390.

## Idea

La coibentazione vista in sezione. Il titolo "Isolanti termoacustici" corre su una riga sola, a tutta larghezza; sotto, una frase e il telefono; poi un solo oggetto, grande quanto la griglia: mezza coppella in lana di roccia rivestita in alluminio, sul suo tubo d'acciaio, vista dal taglio. La fibra bruna gira attorno al foro come in una coppella a fibre concentriche. Sotto il piano di taglio le legende stanno nelle posizioni vere degli strati: la quota sullo spessore della lana ("Spessori 20-120 mm", dalle schede delle coppelle a catalogo), al centro il nome con λ da 0,037 a 0,044 W/mK e il link "Le coppelle a magazzino", a destra il rivestimento in alluminio retinato. Nessun codice di fornitore in apertura.

## Cosa è cambiato in questa rifinitura (giudizio cieco del 24/10/2026)

- Apertura: via la tubazione Grygier in bianco e nero e la sezione disegnata da 128 px con la legenda numerata 1-2-3. Al suo posto la coppella in sezione, calda e a colori, centrata sotto il titolo e larga 1312 px a 1440, senza colonna di testo accanto. La frase d'apertura è scesa da 42 a 19 parole; telefono e catalogo stanno sulla stessa riga, a destra.
- A 1024x768 frase, "Chiama 049 640060" e catalogo cadono entro 377 px; a 390 entro 398 px.
- Su misura spostata subito dopo le famiglie, così il tratto di sola tipografia si accorcia; foto del taglio ad acqua nella versione più stretta e calda del loro sito (1000x645), mostrata a 656 px accanto al testo, con la didascalia sotto: niente più vuoto a destra.
- Un solo trattamento per tutte le immagini: colore naturale, appena caldo. Apertura (coppella) e chiusura (impianto in lamierino) hanno soggetti diversi.
- "Una storia lunga più di cinquant'anni": le tre colonne uguali diventano una riga di fatti in prosa (ISO 9001 dal 2004 con il certificato RINA, consegne con mezzi propri su automezzi di circa 10 metri, EcoVadis bronzo, ANICTA, EIIF) e, accanto, Partner e marchio Termit Isolbag 039.
- Dati: nella ricerca le schede navali hanno la famiglia vera (Lana di roccia), "navale" resta tra le esigenze; la frase di Edilizia è quella del loro sito ("Lana di vetro, elastomero espanso, canne fumarie, accessori."); tolta dalla chiusura la riga del nuovo listino; nel piede "Pezzi su misura" passa in testa alla colonna Azienda.
- Ricerca: trova anche singolare e plurale ("coppelle" trova la coppella Isocamino).

## Prime schermate

- 1440: logo verde, menu, telefono; titolo in Zalando Sans Expanded 400 a 120 px; frase a sinistra, bottone e catalogo a destra; la coppella dal 403 px in giù, tagliata dal bordo della schermata poco sopra il piano di taglio.
- 390: titolo su due righe a 48 px, frase, bottone del telefono, la coppella a tutta larghezza, le legende e il nome sotto; tutto nella prima schermata da 844 px.
- 1024 e 768: titolo su una riga, frase e bottoni impilati, la coppella larga quanto la griglia. 1920: si vede la coppella intera dentro la griglia da 1440.

## Ordine della pagina

Apertura con la coppella; otto famiglie con la ricerca; pezzi su misura con il taglio ad acqua; tre settori in righe (Industria, Edilizia, Navale); "Una storia lunga più di cinquant'anni" in prosa con Partner e marchio; chiusura con foto; piede.

## Caratteri e colori

- Zalando Sans Expanded 400 per i titoli, Zalando Sans 400 e 500 per i testi: una superfamiglia. Licenza SIL Open Font License 1.1 (Google Fonts), file woff2 serviti dalla pagina in `sito/fonts/`, testo della licenza in `sito/fonts/OFL.txt`. Motivo: il logo TERMIT è un largo corsivo pesante con "ISOLANTI TERMICI" spaziato; un grottesco espanso gli sta accanto e ha la sicurezza dei titoli di Paroc senza il condensato maiuscolo.
- Colori: carta #F4F3EF (anche il fondo dell'immagine della coppella), grafite #1B1C1E (15,4:1), grigio #5A5D62 per il testo secondario (5,9:1 sulla carta, 5,4:1 sul piede), link verde scuro #2E6B21 (5,8:1), filetti alluminio #C9CCCF, piede #E9E8E3, verde del marchio #51B038 solo nel logo della testata. Il colore caldo viene dall'oggetto: la fibra bruna della lana di roccia.
- Riferimenti: Thermaflex (un solo tubo tagliato che mostra gli strati, su fondo chiaro), Paroc (il titolo grande e largo), Troldtekt (la carta calda e il colore calmo).

## Interazione

Un solo gesto: "Cerca per codice o per esigenza". A riposo la griglia delle otto famiglie; mentre si scrive (o toccando un'esigenza) la griglia lascia il posto alle schede trovate, al massimo 8 righe, poi "Mostra tutte le N". Il link "Le coppelle a magazzino" sotto la coppella apre la stessa ricerca con le coppelle. Cambio netto, nessuna dissolvenza; il conteggio è annunciato con aria-live. Campo, bottoni e link veri. Altro: menu a bottone sotto i 900 px; piede a fisarmonica a 390 (details e summary).

## Foto, origine e licenza

- Apertura: illustrazione costruita con PIL (`_prova/script/finale_coppella.py`). La fibra è la foto di Engin Akyurt, Pexels 9893816, licenza Pexels "Free" (letta il 24/10/2026); rivestimento e tubo sono disegnati dallo script, nessuna IA. Proporzioni di un tubo da 114,3 mm con 60 mm di isolante. È un segnaposto: lo scatto vero è la foto 1 del LEGGIMI.
- Su misura: la macchina da taglio ad acqua del sito Termit (versione 1000x800, ritagliata a 1000x645), l'unica foto loro.
- Chiusura: Peter Jochim, Pexels 36824351, licenza "Free", taglio 4:5. Nessuna di queste foto è usata in un'altra home della campagna.
- Logo: PNG bianco trasparente del sito (539x85), ricolorato; in pagina a 176 e 200 px, quindi a circa 3x.

## Piede

Logo grafite con una riga su chi sono; quattro colonne (Prodotti con le otto famiglie; Settori; Azienda con Pezzi su misura, Chi siamo, Certificazioni, Partner, News, Condizioni di fornitura; Contatti con telefono, email, indirizzo con mappa e LinkedIn, l'unico social che esiste); newsletter "Listino e novità" con consenso e messaggio d'esito (non invia nulla finché non è collegata a un servizio); riga legale con ragione sociale, indirizzo, P.IVA, REA, PEC, Privacy, Cookie, Condizioni di fornitura. Newsletter motivata: Termit pubblica ogni anno il nuovo listino e notizie di prodotto, e i clienti sono professionisti che riordinano.

## Controlli (24/10/2026, dopo la rifinitura)

- Screenshot di consegna rifatti e guardati a pezzi: 1440, 390 (pagina intera e prima schermata), chiusura 1440; guardati anche 320, 768, 1024 e 1920.
- `scrollWidth` uguale a `innerWidth` a 320, 360, 390, 414, 600, 768, 900, 1024, 1180, 1280, 1366, 1440, 1600, 1920, 2560 (`_prova/script/finale_controlli.mjs`). A 900 l'immagine della coppella sporgeva di 1 px: corretto con `overflow:hidden` sull'apertura.
- Interazione (`_prova/script/finale_prova_ricerca.mjs`): link "Le coppelle a magazzino" con Invio a 1440 e con il dito a 390, cinque schede; "ps680" una scheda, famiglia Lana di roccia; "Tubazioni" 25 schede con le prime 8 e "Mostra tutte le 25"; esigenza spenta con Invio, torna la griglia; "zzzz" il messaggio con il telefono.
- Collegamenti: `tel:+39049640060`, `mailto:info@termitisolanti.com`, mappa Google sull'indirizzo di via Emilia Romagna 19; tutte le ancore interne hanno una destinazione.
- `segnali.sh` a 1440: 17 soglie su 18 OK. Resta l'area foto al 26,6 % (soglia 35 %): la coppella è grande ma ha molta carta attorno, il taglio ad acqua non può andare oltre i 656 px senza perdere nitidezza, e non esistono foto di repertorio adatte per i materiali in sezione. Con gli scatti veri del LEGGIMI (macro dei materiali per le famiglie, magazzino) l'area supera il 35 %.
- Nessun U+2014 nella pagina, negli script, in NOTA, LEGGIMI e CREDITI; nessuna dissolvenza, nessun effetto sul cursore, nessuna opacità al passaggio, nessuna icona Lucide, nessun badge, nessuna card.
- Contrasto AA su tutti i testi (valori sopra).
- Ogni dato in pagina viene da `01-analisi.md` o dal crawl (schede delle coppelle: spessori 20-120 mm, λ 0,037-0,044).
