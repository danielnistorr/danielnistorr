# Eurotecnica Salmaso: proposta di nuova home

Proposta non richiesta di una nuova homepage per Eurotecnica Salmaso S.R.L. (Padova). Solo la home; le altre pagine sono quelle che il sito nuovo avrà (elenco sotto).

- Pagina: `sito/index.html` (statica, si apre con un doppio clic), immagini in `sito/img/`, caratteri in `sito/fonts/`.
- Screenshot e nota di progetto: `screenshot/home/` (`NOTA.md`: struttura, le 15 regole del livello professionale una per una, caratteri, controlli).
- Rifare tutto: `bash _prova/script/build_finale.sh` (immagini, pagina, screenshot, controlli). `IMMAGINI=0` salta le immagini, `CONTROLLI=0` le catture a 320, 768, 1024 e i controlli. Il sorgente è `_prova/script/index.src.html`: le email già composte (oggetto e traccia) le scrive lo script.
- Controlli: `node _prova/script/pro_controlli.mjs file://$PWD/sito/index.html` (esito in `_prova/pro_controlli.json`); orari: `node _prova/script/pro_orari.mjs file://$PWD/sito/index.html`.
- Versione del 3 novembre 2026, "livello professionale": sostituisce quella del 2 novembre ("Il giorno dell’evento", con il microfono di repertorio), che è copiata com’era in `_prova/versione-1-originale/`.
- Analisi con le fonti: `01-analisi.md`; scheda d’uso e identità: `_prova/uso/SCHEDA.md`. Crediti delle immagini: `assets/CREDITI.md`.

## Pagine linkate dalla home (da costruire)

| Indirizzo | Contenuto |
|---|---|
| `privacy/`, `cookie/` | informative (oggi c’è solo la privacy, pagina e PDF) |

La home oggi tiene tutto in sezioni con le ancore `#service`, `#noleggi`, `#impianti`, `#azienda`, `#dove`, `#richiesta`. Quando ci saranno le pagine interne (impianti per tipo di sala, service, noleggi, azienda, contatti) le schede e le porte possono puntare lì.

## Il modulo di richiesta va collegato

Il modulo in fondo alla home oggi **non invia niente**: compone un’email (mailto) con oggetto e campi e la apre nel programma di posta di chi scrive, a service@ per eventi e noleggi e a info@ per impianti, assistenza ed emporio. Prima di pubblicare va collegato a un servizio di invio (per esempio Contact Form 7 sul loro WordPress, che già usano nella pagina Contatti, o un servizio di moduli) con:
- gli stessi campi e la stessa logica (i campi da evento compaiono solo per service e noleggio; nome e telefono obbligatori);
- il caricamento della planimetria e delle foto della sala (oggi l’istruzione dice di allegarle all’email);
- l’informativa privacy accanto al bottone e la casella del consenso, se il servizio salva i dati;
- l’indirizzo a cui arriva ogni tipo di richiesta, da confermare con loro.

## Da chiedere all’azienda (non è in pagina, o è in pagina con riserva)

1. **Orari**: in pagina ci sono quelli di 2GIS, lun-ven 8.30-12.30 e 14.30-18.30, sabato e domenica chiuso. Il vecchio sito dell’emporio diceva 14.00-18.00. Quale è giusto? L’emporio dell’audio ha gli stessi orari dell’ufficio? Chiudono per il patrono (13 giugno, Sant’Antonio) o in agosto? La pagina oggi conta solo i festivi nazionali e Pasquetta (stato "Aperto ora / Chiuso ora" calcolato sull’ora di Roma).
2. **Recensioni**: non ne abbiamo lette (Google e Pagine Gialle bloccano la lettura). Se hanno recensioni Google, ne servono 3-6 con nome e comune, con il loro permesso, per una fascia di recensioni (regola 10).
3. **Clienti e lavori con il nome**: si possono citare la Camera di Commercio di Padova (2022, sala Consiglio e Giunta) e l’Università di Udine (2017)? E le sale delle foto del 2024: dove sono (la sala storica col soffitto dorato, il palco sul Canal Grande, la facciata con la proiezione, il teatro), in che anno, con quali committenti, e si possono nominare? Con 3 lavori con luogo, anno e due-tre dati (sale, lingue, persone) la home avrebbe la sezione dei lavori (regola 11).
4. **Zone servite**: in quali province o comuni lavorano di solito (Padova, Venezia, Vicenza dalle foto)? Serve un elenco vero per la regola 14; oggi non c’è.
5. **Squadra**: chi risponde al telefono, chi fa i sopralluoghi, chi segue il service: nomi, ruoli e anni di mestiere, se vogliono comparire (famiglia S, punto 6).
6. **Anno della srl** (1986 da LinkedIn, coerente con i 40 anni di atoka) e legame con il 1967 dei fratelli Salmaso: la home dice "1986, nasce Eurotecnica Salmaso S.R.L." e "Dal 1967".
7. **Marchi**: in pagina come testo, dall’immagine dei loghi della loro pagina Impianti (Sennheiser, Yamaha, dB Technologies, Crestron, Extron, AMX, Epson, Philips, Bose, Kramer, LG). Le didascalie vengono dalle foto e dai testi (radiomicrofoni Sennheiser, mixer Yamaha, casse dB Technologies, controllo Crestron Extron AMX, videoproiettore Epson, monitor Philips). Vanno confermati marchi e accordi.
8. **Videoconferenza**: quali programmi oggi (il sito dice Skype, WebEx, Lync)? In pagina c’è solo "Videoconferenza".
9. **Sale consiliari "anche con votazione elettronica"**: lo fanno ancora (con i loro sistemi o con un marchio)?
10. **MePA**: le cinque abilitazioni dal 20/04/2022 vengono da amministrazionicomunali.it: confermare che sono ancora attive.
11. **Logo vettoriale** originale (SVG, PDF o AI) e nome del carattere: in pagina c’è la bozza tracciata da noi.
12. **REA, PEC, capitale sociale**: non pubblicati sul sito, quindi non in pagina; se vanno nella riga legale, dal Registro Imprese.

## Foto: quali sono in pagina e quali vanno rifatte dal vero

In pagina solo foto loro, dalla libreria del loro sito (`assets/originali/`), tagliate tutte 3:2 e trattate allo stesso modo da `_prova/script/pro_img.py`, mai ingrandite: regia in sala storica (2024-05-1, apertura), palco (2024-05-3), radiomicrofoni (2024-05-6, tagliata sopra la bottiglia d’acqua), proiezione su facciata (2024-05-4), convegno con la ripresa sullo schermo (2024-05-2, tagliata senza i cartelli del committente), teatro (2024-05-5), banchi con unità di voto (2016-02-sala_vicenza), facciata con l’insegna (2016-02-Untitled-1-2), showroom (2024-05-Negozio-6).

**Diritti**: l’EXIF delle sei foto del 2024 riporta il copyright di un fotografo di repertorio (probabilmente ereditato da un modello di Photoshop). Va chiarito prima di pubblicare.

Sono scatti da telefono (al massimo 1600 x 616) e luci diverse fra loro. Una giornata di foto con un solo fotografo e una sola luce darebbe la serie che la regola 5 chiede. Da fare, in quest’ordine:
1. **Apertura**: la regia durante un convegno in una sala importante, con un loro tecnico al mixer (polo o giacca con il logo), il pubblico e la sala dietro; orizzontale 3:2, almeno 3000 px, reflex o mirrorless, luce della sala senza flash, senza schermi con testo leggibile.
2. **La squadra**: le 4 persone davanti alla sede con l’insegna "emporio dell’audio", e un ritratto per ciascuno per la sezione squadra.
3. **La sede da fuori** in una giornata coperta, con l’ingresso, l’insegna e l’angolo con Viale della Regione Veneto (serve a riconoscerla da chi arriva in macchina); e l’emporio dentro, ordinato, con luce uniforme.
4. **Traduzione simultanea**: le cabine in legno montate in una sala, ricevitori e cuffie sul tavolo dei delegati (oggi manca una loro foto: la scheda è solo testo).
5. **Streaming e riprese**: una telecamera della regia in sala e il banco con il computer della diretta.
6. **Una sala per tipo** con un loro impianto installato: sala consiliare, aula, teatro, chiesa; vuote, luce naturale, macchina sull’asse della sala.
7. **Il noleggio**: il materiale pronto al ritiro sul banco in sede (casse, radiomicrofoni, valigie dei ricevitori), con il tecnico che lo spiega.
8. **Un loro sistema per conferenze storico** (unità con microfono o con votazione), se ne hanno ancora uno, sul banco di un’aula.

## Prima di pubblicare (tecnico)

- Collegare il modulo (sopra).
- Con il sito servito in http rimettere in `<head>` il preload dei due caratteri (`fonts/general-sans-600.woff2` e `fonts/host-grotesk-variabile.woff2`, `as="font" type="font/woff2" crossorigin`): tolti dal file statico perché aperti come file:// danno errori CORS.
- Sostituire la bozza del logo con il vettoriale originale (`sito/img/logo.svg` e `logo-chiaro.svg`, che è lo stesso tracciato in bianco).
- Il link "Indicazioni" usa la loro scheda Google (`https://www.google.com/maps?cid=13052135561717271527`); se la scheda cambia, va aggiornato in cinque punti del sorgente.

## Licenze

- Caratteri: General Sans 600 (Fontshare, ITF Free Font License, uso commerciale ammesso) e Host Grotesk (Google Fonts, SIL Open Font License 1.1), serviti dalla pagina; testi in `sito/fonts/`.
- Foto: solo dell’azienda (vedi sopra). Le foto di repertorio di `assets/esterne/` non sono più usate in pagina (restano in cartella con i loro crediti). Nessuna immagine generata dall’IA, nessun disegno.

## Newsletter e social

Nessuna newsletter: il sito non pubblica notizie e il lavoro è a progetto. Social: la pagina aziendale LinkedIn (it.linkedin.com/company/eurotecnica-salmaso-srl) è nel piede.
