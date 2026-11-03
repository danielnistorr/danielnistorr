# Peruzzo Grafiche: proposta di nuova homepage

Proposta non richiesta di una nuova home per Peruzzo Grafiche Srl (Mestrino, Padova). Solo la home. Non è pubblicata, non è stata mandata all'azienda.

Versione attuale: **livello professionale, 3/11/2026** (regole in `_metodo/professionale/REGOLE.md`, famiglia M; scheda d'uso in `_prova/uso/SCHEDA.md`). La versione precedente ("Stampare è un'arte" con The Private Eye in apertura) è copiata com'era in `_prova/versione-1-originale/` (sito, screenshot e nota).

## Dove sono le cose

- `sito/index.html`: la home, statica (si apre con file:///). `sito/img/`: solo le immagini usate, JPEG in più larghezze e il logo PNG. `sito/fonts/`: Funnel Sans e Piazzolla in woff2 con i testi della licenza SIL OFL 1.1.
- `screenshot/home/`: screenshot a 1440 e 390 (interi e prima schermata), `chiusura-1440.jpg` (dove siamo e piede) e `NOTA.md` con struttura, esito delle 15 regole, compiti della scheda d'uso, applicati e respinti, caratteri e foto.
- `_prova/script/build_finale.sh --immagini`: rifà immagini (`pro_img.py`), controlli (`pro_controlli.mjs`, esito in `_prova/pro_controlli.json`) e screenshot (`pro_shot.mjs`). `pro_misura.mjs`: scorrimento orizzontale a una larghezza.
- `01-analisi.md`: fatti con le fonti; `assets/CREDITI.md`: origine e licenza di ogni foto.

## Il modulo va collegato a un servizio

In home ci sono due moduli: **"Chiedete un preventivo"** (nome, casa editrice o azienda, email, telefono, tipo di lavoro, confezione, formato, pagine, copie, carta, stampa, quando serve, link ai file, note) e **"Ti chiamiamo noi"** (nome e telefono). Oggi non inviano niente da soli: controllano i campi obbligatori e **compongono un'email** (`mailto:` a info@graficheperuzzo.it, con oggetto "Richiesta di preventivo: tipo, copie" o "Ti chiamiamo noi" e i campi nel testo) che il visitatore invia dal suo programma di posta, allegando i PDF. Nel sito pubblicato vanno collegati a un servizio di invio (per esempio il Gravity Forms che usano oggi sul sito WordPress, o un servizio di moduli), con:
- il caricamento dei file (PDF, fino a quale peso: da chiedere) al posto del solo link;
- la risposta automatica e il consenso privacy;
- l'invio a info@graficheperuzzo.it o all'indirizzo che l'azienda indica per i preventivi.
Il modulo completo a tre passi di oggi (copertina, sovracoperta, capitelli, finiture) può restare nella pagina `preventivi.html`; i link "Preventivo per..." delle confezioni impostano già la confezione nel modulo della home.

## Pagine del sito nuovo a cui punta la home

`lavori.html` (con le ancore `#fumetti`, `#libri`, `#cataloghi`), `prestampa.html`, `stampa.html`, `legatoria.html`, `logistica.html`, `chi-siamo.html`, `fsc.html`, `privacy.html`, `cookie.html`. Ancore della home: `#lavori`, `#confezioni`, `#reparti`, `#preventivo`, `#richiamo`, `#chi`, `#dove`, `#contenuto`.

## Da chiedere all'azienda (e da confermare prima di pubblicare)

1. **Orari** d'ufficio e di carico e scarico (non pubblicati): vanno accanto all'indirizzo in "Dove siamo" e nel piede. Oggi al loro posto c'è "Prima di passare per un ritiro o una consegna, chiamateci."
2. **Come mandare i file**: specifiche degli esecutivi (PDF, abbondanze, profilo colore), peso massimo, se preferiscono un link di trasferimento o un loro FTP, e chi li riceve.
3. **Tempi e tirature**: tempi indicativi di produzione per confezione e tiratura minima e massima, da aggiungere nel blocco preventivo.
4. **Lavori in pagina e permessi.** Sono foto della loro pagina Prodotti: La sposa yemenita (BeccoGiallo), Paper Girls 2 (Bao Publishing), Ferrari cerca e trova (Franco Cosimo Panini), Helidon Xhixha, Refractive Vibes (Contini Art UK). Le copertine e le tavole sono di editori e autori: servono i permessi, o la conferma che li hanno già (le usano oggi sul loro sito). Per ogni lavoro servono anche **anno, confezione, pagine e copie** (la regola 11 chiede 2-3 dati e l'anno, oggi non ci sono).
5. **Clienti nominati**: BeccoGiallo, Coconino Press, Tunuè, Bao Publishing, Saldapress, Lucca Comics & Games, Franco Cosimo Panini, Il Castoro, Baldini e Castoldi, Contini Art UK, Galleria Contini, Vecchiato Arte, Atala, Selle Royal, Calpeda (tutti da foto, crediti e loghi del loro sito). Quali si possono citare? Senza permesso si tolgono i nomi e restano i tipi di lavoro.
6. **Recensioni**: non ce ne sono di pubbliche. Se un editore o una galleria dà due righe firmate (nome, casa editrice, città), si aggiungono come prova (regola 10).
7. **Parco macchine di oggi** (Stampamedia 2014: 3 Heidelberg 8 colori, 7 unità di piega, raccoglitrice a 18 stazioni, cucitrice a filo refe, linea per il cartonato) e se si possono nominare Heidelberg, Müller Martini, Polar, Ricoh: con i dati veri il blocco dei numeri può dire macchine, gruppi, metri quadrati.
8. **Dipendenti e fatturato**: 22 dipendenti (aziende.it) o 21 (Atoka); fatturato da aggregatori. Fuori dalla pagina finché non li confermano.
9. **PEC** peruzzografichesrl@legalmail.it (solo aziende.it), REA e capitale sociale per la riga legale del piede.
10. **FSC**: in pagina solo "carta certificata FSC®", senza codice. Il codice FSC® C114625 (nell'immagine del marchio sul loro sito) è ancora valido e intestato alla srl attuale? Con il codice si può mettere il certificato scaricabile (A1, punto 8).
11. **Dal 1989**: è l'anno dell'attività di Alberto Peruzzo; la srl di oggi è più giovane. Va bene "dal 1989"?
12. **Alberto Peruzzo**: vuole comparire con la foto al banco (`IMG_8479`, 2018)? È lo stesso Alberto Peruzzo della Fondazione Peruzzo e della donazione di Modern Art alla Marciana (Finestre sull'Arte, 2026)? Se sì, e se lo vuole, una riga in "Chi c'è dietro".
13. **Peruzzo Editoriale, Peruzzine e la parete degli autori**: lo shop si ferma al 2018 e peruzzine.com non risponde. Se sono attivi tornano in pagina (e nel piede la colonna Edizioni); il disegno con la dedica "Grazie per averci stampato a very good book" torna se si sa chi è l'autore.
14. **Social**: nel piede Facebook e Instagram (link del sito di oggi; Instagram ha ancora il nome del marchio vecchio). Prima di pubblicare togliere quello fermo da più di un anno.
15. **Ragione sociale e marchio**: in pagina "Peruzzo Grafiche Srl" (VIES) e il logo 2022. La privacy di oggi cita ancora "PERUZZO INDUSTRIE GRAFICHE S.R.L." con la P.IVA 03946690280, che oggi è di un'altra società: va aggiornata.
16. **Telefoni**: in pagina 049 9002884 (principale, anche in testata) e 049 9002885. Il fax 049 9002896 va ancora indicato?
17. **Le foto del servizio Canon 2018**: chi le ha scattate, se si possono usare, e gli originali a piena risoluzione (online quasi tutte a 800 px).

## Foto da fare dal vero

La home non usa foto di repertorio né disegni (decisione del committente). Le foto in pagina sono tutte loro; quelle da rifare, in ordine:

1. **Apertura, la legatoria**: la foto di oggi (2400 px, luce al neon, grandangolo) regge ma è documentaria. Rifarla nello stesso punto (linea Müller Martini con le segnature sui bancali), con una persona che lavora sulla linea, luce del capannone corretta con un pannello a sinistra, ottica da 35-50 mm all'altezza del banco, almeno 4000 px, RAW. Taglio 3:2.
2. **Reparti, quattro foto 3:2 della stessa serie**: prestampa (mani sul file o sulla prova colore), stampa (il tipografo con il contafili davanti alla Speedmaster), legatoria (il blocco cucito a filo refe tra le mani, come `IMG_7955`), logistica (bancali fasciati pronti sul furgone con il logo 2022). Oggi sono a 800 px: servono almeno 2400 px, stessa luce e stessa distanza.
3. **Lavori, quattro still life quadrati**: un fumetto in brossura, un cartonato, un libro illustrato aperto, un catalogo d'arte, sullo stesso fondo grigio chiaro, luce morbida da sinistra, stessa inquadratura dall'alto a 30 gradi, almeno 2400 px. Solo lavori con il permesso dell'editore.
4. **Chi c'è dietro**: un ritratto di Alberto Peruzzo al banco o in legatoria, luce naturale, senza la parete affollata dietro.
5. **La sede**: la notturna regge; una ripresa di giorno dell'ingresso per il carico aiuterebbe chi viene per un ritiro.

## Licenze

- Foto di repertorio in pagina: nessuna. Le foto Unsplash e Pexels di `assets/esterne/` non sono in pagina e restano solo come archivio (vedi `assets/CREDITI.md`).
- Foto in pagina: tutte di Peruzzo, prese dal loro sito solo per la proposta; le copertine sono di terzi (punto 4).
- Caratteri: Funnel Sans e Piazzolla, SIL Open Font License 1.1 (uso commerciale e ospitalità consentiti), file in `sito/fonts/` con i testi della licenza.

## Loghi

- In pagina il logo 2022 (`logo-peruzzo-grafiche-bianco-2022-686x165.png`) ricolorato in grafite #272727, PNG, a 166 e 200 px: regge fino a circa 340 px a 2x.
- **Serve il logo vettoriale** (SVG, PDF o AI) dall'azienda o dal loro grafico, e la conferma del marchio da usare (2022 "Peruzzo Grafiche" o storico "Peruzzo Industrie Grafiche").
- Nessun logo di cliente è in pagina: i 48 loghi della Libreria sono marchi di terzi; i clienti sono scritti come testo.
