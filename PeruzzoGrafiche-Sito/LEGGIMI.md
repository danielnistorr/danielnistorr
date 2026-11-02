# Peruzzo Grafiche: proposta di nuova homepage

Proposta non richiesta di una nuova home per Peruzzo Grafiche Srl (Mestrino, Padova). Solo la home. Non è pubblicata, non è stata mandata all'azienda.

## Dove sono le cose

- `sito/index.html`: la home finale, statica (si apre con file:///). `sito/img/`: solo le immagini usate, JPEG in più larghezze. `sito/fonts/`: Piazzolla e Funnel Sans in woff2 con i testi della licenza SIL OFL 1.1.
- `screenshot/home/`: screenshot a 1440 e 390 (interi e prima schermata), chiusura e piede a 1440, e `NOTA.md` con idea, caratteri, colori, interazione, foto e controlli.
- `_prova/script/build_finale.sh`: rifà immagini, controlli e screenshot (`finale_img.py`, `finale_shot.mjs`). `_prova/script/rapido.mjs`: altezza e scorrimento orizzontale da 320 a 2560 px.
- `01-analisi.md`: fatti con le fonti; `assets/CREDITI.md`: origine e licenza di ogni foto; `_prova/home/a` e `b`: i due prototipi.

## Pagine del sito nuovo a cui punta la home

`preventivi.html` (con il parametro `confezione=punto-metallico`, `brossura` o `cartonato`: il modulo deve aprirsi già impostato), `prestampa.html`, `stampa.html`, `legatoria.html`, `logistica.html`, `chi-siamo.html`, `stabilimento.html`, `lavori.html` (l'attuale Libreria), `fsc.html`, `edizioni.html`, `peruzzine.html`, `negozio.html`, `privacy.html`, `cookie.html`. Ancore della home: `#confezioni`, `#editori`, `#reparti`, `#contatti`, `#contenuto`.

## Da confermare con l'azienda prima di pubblicare

1. **Copertine in pagina.** L'apertura mostra The Private Eye (Bao Publishing; in copertina Brian K. Vaughan, Marcos Martin, Muntsa Vicente) e la sezione editori Paper Girls 2 (Bao Publishing), Il club delle baby-sitter (Il Castoro) e una doppia pagina della Sposa yemenita (BeccoGiallo). Sono foto della pagina Prodotti del loro sito, ma le copertine e le tavole sono opere di editori e autori: prima di pubblicare servono i permessi, o almeno la conferma che Peruzzo li abbia già (le usa oggi sul proprio sito). Va confermato anche che li hanno stampati loro, come dice la pagina Prodotti. Senza permessi l'apertura torna allo still life di un loro lavoro senza copertina riconoscibile (sotto, "Foto da rifare").
2. **Editori e clienti nominati.** In pagina ci sono Bao Publishing, Coconino Press, Tunuè, Saldapress, BeccoGiallo, Il Castoro, Baldini e Castoldi, Franco Cosimo Panini, le gallerie Contini e Vecchiato Arte, Atala, Selle Royal, Calpeda e Lucca Comics & Games (tutti dall'analisi: foto dei lavori, crediti e loghi della pagina Libreria). Servono i permessi. Senza permessi l'elenco in serif si toglie e resta solo il titolo "Fumetti, libri e cataloghi d'arte per case editrici di tutta Italia" con una riga su gallerie e aziende senza nomi.
3. **Il disegno con la dedica** ("Grazie per averci stampato a very good book", `2018-05-IMG_8470`): tolto dalla pagina nella revisione (stava piccolo, in fondo a una colonna vuota). Se l'azienda dice chi è l'autore e dà il permesso, può tornare nella sezione editori, accanto ai tre lavori.
4. **Ragione sociale e marchio.** In pagina "Peruzzo Grafiche Srl" (VIES) e il logo 2022; l'insegna, il camion e il foglio stampato in oro della chiusura dicono ancora "Industrie Grafiche" (sul camion "S.P.A."). In pagina la didascalia della chiusura lo dichiara ("con il marchio storico Peruzzo Industrie Grafiche"). Va bene mostrare il foglio con il logo vecchio?
5. **Privacy.** La privacy di oggi cita "PERUZZO INDUSTRIE GRAFICHE S.R.L." con la P.IVA 03946690280, che per il VIES oggi è di Novanta Srl (Roma): va tolta e sostituita con 05078210282. REA, PEC e capitale sociale non sono in pagina (non trovati, o solo da Atoka): se sono pubblici si aggiungono alla riga legale del piede.
6. **Dal 1989.** È l'anno dell'attività di Alberto Peruzzo (home di oggi); la srl attuale è più giovane (Atoka: circa 9 anni). "Dal 1989" va bene così?
7. **FSC.** In pagina c'è solo "carta certificata FSC®", senza codice. Il codice FSC® C114625 si legge solo nell'immagine del marchio: è ancora valido e intestato alla srl attuale?
8. **Peruzzo Editoriale e Peruzzine.** Lo shop si ferma al 2018 e peruzzine.com non risponde. Se l'editoriale è fermo si tolgono la riga "Abbiamo anche un marchio nostro..." e la colonna Edizioni del piede. Se è attivo si può aggiungere la newsletter (oggi non c'è, vedi NOTA).
9. **Social.** Nel piede Facebook e Instagram (link del sito di oggi). L'attività non si può verificare da qui: il 24/10/2026 Instagram ha risposto 401 con "require_login" e Facebook rimanda al login. L'account Instagram ha ancora il nome del marchio vecchio (`peruzzo_industrie_grafiche`). Prima di pubblicare: guardare la data dell'ultimo post e togliere dal piede quello fermo da più di un anno. Lasciati fuori X (29 follower, fermo) e LinkedIn (profilo personale, non pagina aziendale).
10. **Fuori dalla pagina finché non arriva conferma:** orari di apertura (non pubblicati), fax 049 9002896, codice FSC, nomi e modelli delle macchine (Heidelberg Speedmaster, Müller Martini, Polar, Ricoh: si vedono nelle foto ma non sono scritti; nella foto della legatoria la targa Müller Martini si legge), numeri di Atoka (21 dipendenti, 13,7 milioni, capitale 1,0 milioni).
11. **Telefono.** In pagina 049 9002884 (principale, anche in testata) e 049 9002885, scritti come sul sito di oggi.

## Foto da rifare dal vero

Priorità uno, **still life per l'apertura e per le tre schede**. Oggi l'apertura usa la foto di The Private Eye dalla loro pagina Prodotti: è un loro lavoro ed è a colori, ma è una foto da telefono a 1200 px, mostrata a circa 1037 px CSS a 1440 (un po' morbida sugli schermi retina), e la copertina è di terzi. Tre lavori loro, uno per confezione: un punto metallico sottile (si deve vedere la piega del dorso con i punti), una brossura (un fumetto o un catalogo, dallo spigolo, con il taglio del blocco), un cartonato cucito (dallo spigolo, con l'unghiatura del cartone e la capitata). Fondo di carta naturale chiara, sempre lo stesso; luce morbida da finestra o da un grande bank laterale, da sinistra, ombra corta; stessa inquadratura per tutti e tre, macchina bassa a 15-20 gradi, lo spigolo a destra del centro, il libro che esce dal bordo sinistro; obiettivo da 90-100 mm, diaframma 8-11 perché sia nitido tutto lo spigolo; almeno 3000 px di lato lungo, RAW. Con queste tre foto le schede delle confezioni possono cambiare anche l'immagine, oltre al disegno del dorso. Per l'apertura conviene un lavoro con una copertina loro o di un editore che dà il permesso, sullo stesso fondo, a colori.

Poi:
- **Gli originali Canon del servizio 2018** (chi li ha scattati, se si possono usare, se esistono a piena risoluzione): la legatoria `IMG_8866` regge, ma online è a 2400 px con la luce del neon.
- **Il foglio stampato in oro** della chiusura (`IMG_8364`) è solo 1200x800: rifarlo in luce radente, almeno 3000 px, con la frase manoscritta leggibile.
- **Le copertine degli editori** (foto di prodotto del 2017, quasi tutte da iPhone 6, 1200 px): in pagina ce ne sono tre, portate sulla carta della pagina. Da rifare se arrivano i permessi, sullo stesso fondo e con la stessa luce dello still life, almeno 3000 px.

## Licenze

- Foto di repertorio in pagina: nessuna (la foto Pexels di Allec Gomes della prima versione non c'è più; resta in `assets/esterne/` come archivio, vedi `assets/CREDITI.md`). Tutte le foto in pagina sono di Peruzzo, prese dal loro sito solo per la proposta; le copertine sono di terzi (punto 1).
- Caratteri: Piazzolla e Funnel Sans, SIL Open Font License 1.1 (uso commerciale e ospitalità consentiti), file in `sito/fonts/` con i testi della licenza.

## Loghi

- In pagina il logo 2022 (`logo-peruzzo-grafiche-bianco-2022-686x165.png`) ricolorato in nero caldo, PNG: regge fino a circa 340 px a 2x (in pagina è a 133 e 200 px).
- Non esiste un vettoriale nel sito. La scritta si potrebbe ridisegnare, il monogramma no (lettere serif sovrapposte, troppo sgranate): **serve il logo vettoriale** (SVG, PDF o AI) dall'azienda o dal loro grafico, e la conferma di quale marchio usare (2022 "Peruzzo Grafiche" o storico "Peruzzo Industrie Grafiche").
- Nessun logo di cliente è in pagina: i 48 loghi della Libreria sono marchi di terzi.
