# F.R.A.M.O., home finale: nota

Pagina: `sito/index.html` (statica, si apre anche da file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini da `_prova/script/build_img.py`, pagina da `_prova/script/pagina.html`, screenshot). Prova del calibro e del menu: `node _prova/script/prova_finale.mjs`. Controlli di larghezza e screenshot alle altre misure: `node _prova/script/controlli.mjs <cartella>`.

Altezza: 5405 px a 1440 compreso il piede (cinque sezioni più il piede), 7171 px a 390.

## L'idea

Una tavola tecnica del loro lavoro: lo stesso tubo F.R.A.M.O. fotografato due volte, prima con il raccordo staccato e poi raccordato, uno sopra l'altro su carta chiara, con le tre parole con cui loro rifanno un tubo: lunghezza, tipologia, raccordatura ("identico nella lunghezza, tipologia e raccordatura", pagina Agricoltura). La lunghezza è una quota vera, con i richiami alle due estremità. Il quarto dato, il diametro, diventa l'unico gesto della pagina: il calibro da 3/16" a 3". Tutto il resto parla da banco: il campione da rifare, come si misura, il magazzino intorno al tubo, la sede.

## Le prime due schermate

1. Apertura (1440x900). Logo vero, quattro voci di menu, telefono. Il titolo "Tubi oleodinamici su misura" su una riga sola, largo quanto la gabbia (78 px a 1440). Sotto, la tavola su dieci colonne: in alto il tubo con il raccordo accanto (legende "Tipologia, il codice sulla guaina" e "Tubo e raccordo"), sotto lo stesso tubo raccordato (legenda "Raccordatura" e quota "Lunghezza" tra le due estremità). Didascalia a margine: "Foto provvisoria F.R.A.M.O.: lo stesso tubo prima e dopo il montaggio di un raccordo Push Lock." In fondo, dopo un filetto, la riga dei dati come il cartiglio di un disegno: a sinistra "Officina e magazzino a Saonara, Padova, dal 1986. / Su ordinazione o da campione, da 3/16" a 3"", a destra il bottone "Chiama 049 644909" e il link "Manda la foto del tubo su WhatsApp".
   Da 701 a 1279 px la stessa tavola (nove colonne sotto 900 px), con la didascalia sotto la quota: a 1024x768 e a 768x1024 la tavola intera, il testo e il bottone stanno sopra la piega.
   A 390: titolo su tre righe, poi la tavola girata in verticale (i due tubi affiancati, i raccordi in alto, la quota a destra), poi didascalia, testo, bottone e link.
2. Il calibro "Da 3/16" a 3"". La frase vera sulla specialità, i cerchi concentrici in scala tra loro con il diametro scelto in giallo marchio, la lettura grande (1"), "Nominale DN 25", il tipo di tubo e il bottone "Chiedi un tubo da 1"" che apre WhatsApp con la misura già scritta. Sotto, le dodici misure: la scelta è la cella intera in giallo, a 768 sei per riga, a 390 tre per riga. Nota sotto il testo: "DN indicativi, secondo le norme EN e SAE".

Poi: "Porti il tubo vecchio, esce un tubo nuovo" (la macro vera IMG-9592 a filo del bordo sinistro, 432 px di larghezza così il file da 864 px regge lo schermo 2x; a destra la loro frase sul campione e i tre metodi di misura dalla loro guida, con il link "Come misurare un tubo"); "600 mq di magazzino, accanto all'officina" (boccole a tutta larghezza, alte 600 px, il paragrafo dei marchi a 22-23 px con cinque marchi in grassetto, a margine "1986" e "Pronta consegna", la riga dei settori con i tre link); la chiusura "Gli specialisti di Padova" (dallo slider della loro home) con il telefono, WhatsApp, email, indirizzo con la mappa e orari, e la foto fino al bordo destro su sette dodicesimi della larghezza; il piede.

## Caratteri e colori

- Anybody (Etcetera Type Co.), Google Fonts, SIL Open Font License 1.1 (`sito/fonts/OFL-Anybody.txt`), una sola famiglia variabile servita dalla pagina (`anybody-latin.woff2`, `anybody-latin-ext.woff2`). Titoli in larghezza 118-128 % e peso 360-420; testo al 104 %; legende, bottoni e titoletti del piede al 110-112 %. Motivo: la scritta FRAMO del logo è un lineare largo e sottile, il sito di oggi usa Zekton (largo tecnico), Öhlins (riferimento 1 in 01-analisi) lavora con lo stesso grottesco largo. Anybody ha le frazioni vere (3/16", 1 1/4" come in una scheda tecnica) e le cifre tabellari per DN, telefono e orari. Niente monospazio, niente Inter.
- Colori: carta #EFEDE8 (fondo unico di tutta la pagina e del piede), inchiostro #161616, acciaio #55595D per didascalie e legende (circa 6:1 sulla carta), filetti al 16 % d'inchiostro, giallo marchio #FFCD05 solo come campitura (cerchio del calibro, misura scelta, bottoni al passaggio), mai come colore di testo.

## Interazione

Uno solo: il calibro. Dodici bottoni in un gruppo radio (frecce, Home, Fine, tocco). Cambia il cerchio giallo, la lettura (pollici e DN), la riga sul tipo di tubo (fino a 1" anche termoplastico 1TD, 2TD, R7, dalla pagina Tubazioni) e il link WhatsApp con il messaggio "Buongiorno, mi serve un tubo oleodinamico da 1" (DN 25)." Nessuna animazione allo scorrimento, nessun effetto al cursore; transizioni di 0,12 s solo su bottoni e misure. Menu del telefono con un vero bottone (aria-expanded).

## Foto (origine e licenza)

- Apertura: `assets/originali/2023-07-IMG-9594.jpg` e `2023-07-IMG-9596.jpg`, foto F.R.A.M.O. dall'articolo "Il sistema Push Lock" (luglio 2023), 1024 px. Scontorno GrabCut sui pixel fotografati (nessuna parte ridisegnata o dipinta: il dado è quello della foto, con le sue luci), luce del tavolo corretta per tutto il pezzo, ombra vera trasformata in velatura semitrasparente sulla carta della pagina: nessun riquadro di fondo, nessuno scalino di tono. Ruotate di 8,8 gradi per avere la corda orizzontale e ritagliate con lo stesso riquadro. Mostrate a circa 1:1 a 1440 (file da 1056 px su 1090 px): sugli schermi 2x restano morbide, vanno rifatte (vedi LEGGIMI).
- Da campione: `2023-07-IMG-9592.jpg`, foto F.R.A.M.O. (DN10, 3/8", SAE 100R6), a colori, ritagliata per tenere la sezione con la treccia.
- Magazzino: Hans Westbeek, Unsplash s0xU_2ytj4I, Unsplash License; ruotata sull'asse della scatola, ritagliata 2,4:1 senza il cartone, ombre aperte e toni portati verso la carta (media al 50 %, nero minimo a 34).
- Chiusura: Tatiana Zhukova, Unsplash E3mqhLHvfP8, Unsplash License; non usata in altre home della campagna (controllati i `CREDITI.md` di tutte le cartelle `*-Sito`).
- Nessuna foto nuova scaricata in questo passaggio; licenze e autori in `assets/CREDITI.md`.

## Piede

Logo vero (PNG 500x90 mostrato a 196 px, basta per il 2x), una riga su chi sono, quattro colonne: Azienda, Lavorazioni con Settori, Prodotti, Contatti. Riga legale: F.R.A.M.O. S.r.l., via Liguria 32, 35020 Saonara (PD), P.IVA e C.F. 02075000287, Privacy, Cookie, Termini d'uso. REA fuori finché non arriva la visura. Niente social: non esistono (c'è solo WhatsApp, già nei contatti). Niente newsletter: i clienti sono officine e aziende che ordinano al banco o su WhatsApp, e F.R.A.M.O. non annuncia fiere, cataloghi propri o collezioni; le News sono guide tecniche. A 390 Azienda e Lavorazioni stanno affiancate, Prodotti e Contatti sotto.

## Cosa è cambiato in questo passaggio (giudizio cieco in `_prova/cieco.json`)

- Apertura rifatta come tavola tecnica: titolo su una riga sopra, la coppia di tubi a tutta gabbia, la riga dei dati in fondo. Non è più la posizione titolo-testo-bottone a sinistra con il pezzo a destra (Mario Agnoletto) né titolo a sinistra con testo a destra e pezzo sotto (FM Sistemi), e non c'è la barra di voci in fondo.
- Scontorno rifatto senza ritocchi: via il riquadro di fondo intorno al raccordo e le macchie di tono, nessun dado ridisegnato.
- "Lunghezza" è una quota tra le due estremità del tubo, con la scritta sulla linea (prima la linea la attraversava).
- La foto della chiusura e la frase: "Gli specialisti di Padova" su due righe, il telefono 56 px sotto il titolo (niente margin-top:auto).
- Calibro: la misura scelta è la cella intera in giallo, niente segno sopra la cella; riga "Misura" tolta; nota "DN indicativi, secondo le norme EN e SAE".
- Boccole schiarite (ombre aperte, toni verso la carta) e fascia più alta (600 px); macro a 432 px.
- Marchi a 22-23 px in peso normale, cinque in grassetto, "Brochure prodotti" a capo.
- Da 701 a 1279 px l'apertura non si impila più: a 1024x768 la tavola è intera sopra la piega.
- Didascalia della macro senza "in magazzino"; "Edilizia e movimento terra" anche nel piede.
- `prova_finale.mjs` aggiornata (la riga "Misura" non c'è più); nuovo `controlli.mjs`.

## Controlli

- Screenshot guardati a pezzi a 1440 e 390 (pagina intera), prime schermate a 320, 768, 1024 e 1920 (in `screenshot/home/`): nessuna sovrapposizione; a 320 il telefono in testata si nasconde e resta nel bottone.
- scrollWidth uguale a innerWidth a 320, 360, 375, 390, 414, 600, 700, 701, 768, 820, 900, 901, 1024, 1099, 1100, 1180, 1279, 1280, 1366, 1440, 1600, 1920 e 2560.
- Calibro provato con tastiera (freccia destra, Fine, Inizio) e clic a 1440, con il tocco a 390: lettura, DN, tipo e link WhatsApp cambiano insieme; il menu del telefono si apre con aria-expanded="true".
- Collegamenti: tel:+39049644909 (quattro), mailto:commerciale@framosrl.com (due), Google Maps "F.R.A.M.O. via Liguria 32 Saonara PD" (due), WhatsApp api.whatsapp.com/send?phone=39049644909.
- Segnali da IA (`segnali.sh` del kit): 17 soglie su 18 a posto; resta l'area foto al 30,1 % (soglia 35 %). È il caso previsto dalla guida per le aziende senza foto grandi: le foto vere di F.R.A.M.O. sono tre scatti da telefono a 1024 px, e allargarle ancora le renderebbe morbide anche a 1x; la prima cosa da chiedere all'azienda sono le foto (LEGGIMI). "Da guardare": le dodici sigle DN del calibro, che sono codici e non un elenco decorativo.
- Nessun carattere U+2014 in pagina, nella nota, nel LEGGIMI, nei crediti e negli script.
- Tutti i fatti vengono da 01-analisi.md e dalle pagine del sito citate lì; quello che manca o è dubbio è nel LEGGIMI.
- Da file:/// la console segnala il preload del carattere bloccato dal CORS: il carattere si carica comunque; servito da un sito vero il preload funziona.
