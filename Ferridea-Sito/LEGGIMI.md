# Ferridea, proposta di nuova home: LEGGIMI

È una proposta non richiesta, solo per la home, per Ferridea di Malimpensa Mario (viale Veneto 32, Saonara PD). L'azienda non è stata contattata e non è stato pubblicato niente.

## Dove sono le cose

| Cosa | Dove |
|---|---|
| Analisi con le fonti | `01-analisi.md` |
| Home finale | `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/` |
| Screenshot | `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` |
| Nota di progetto | `screenshot/home/NOTA.md` |
| Script per rifare tutto | `bash _prova/script/build_finale.sh`, che chiama `build_img.py` (immagini), `scala_poligoni.py` (scontorno della scala), `shot_finale.mjs` (screenshot), `verifica.mjs` (console, larghezze, tastiera, tocco, collegamenti; esito in `_prova/verifica-finale.txt`) e i segnali da IA |
| Prototipi scartati e scelti | `_prova/home/a/` (scelto) e `_prova/home/b/` |

## Dati da confermare con l'azienda (non sono a vista in pagina, salvo dove detto)

1. **P.IVA 02602070282.** È nel piede, ma viene da impresaitalia.info, non dal loro sito. Va confermata. Il sito deve mostrarla per legge, e oggi non lo fa.
2. **REA e PEC.** Non li ho trovati e non sono in pagina; se ci sono, vanno aggiunti alla riga legale. Capitale sociale: non si applica, perché è una ditta individuale.
3. **Codice ATECO**: l'elenco dice 28.1, mentre per un fabbro ci si aspetta 25.1.
4. **1959**: che cosa è cominciato quell'anno e chi l'ha cominciato, e da quando c'è la ditta individuale di oggi. In pagina c'è "dal 1959" e "nel settore dal 1959", come sul loro sito. "In officina dal 1959" è stato tolto.
5. **Quale numero mettere in evidenza.** Oggi in evidenza c'è il fisso 049 879 2451, nella testata, nel bottone e nella chiusura. Va chiesto se preferiscono il cellulare 335 520 3918 e se il fisso è ancora anche fax.
6. **Orari d'officina.** Non sono pubblicati e quindi non sono in pagina. Un aggregatore indica 8-19 nei feriali e 8-12 il sabato: non è affidabile.
7. **Metalli e lavorazioni.** Le righe del selettore abbinano il ferro battuto ai cancelli, la lamiera a cancelli e parapetti e l'inox a parapetti, corrimano e scale. Questi abbinamenti vengono dal loro elenco di lavorazioni e dalle foto: vanno confermati. Va chiesto anche se i serramenti sono di produzione propria o montati, e con quale sistema.
8. **Capottine** "con copertura in vetro o in policarbonato": viene dalle foto, va confermato.
9. **Le tre legende sulla scala d'apertura**: "Fissata solo al muro", "Niente montanti", "Su misura per quel vano". Dicono quello che si vede nella foto e che è proprio di una scala a sbalzo, ma vanno confermate con l'azienda. Se ci danno spessore dei gradini, materiale (lamiera piegata? acciaio pieno?) e tipo di fissaggio, conviene aggiungere una legenda con la misura vera, in cifre tabellari.
10. **Descrizioni delle foto**: "cancello a tre pannelli in lamiera" (tessera Cancelli), "parapetto a cavi tesi" in inox (scheda Inox), il cancello in lamiera forata a quadri della chiusura. Vengono dalle foto: vanno confermati materiale e finitura (la lamiera forata è zincata o inox? la superficie a vortici è una satinatura fatta da loro?).
11. **Macchine.** Gli "impianti produttivi tecnologicamente avanzati" della loro home sono citati come "impianti che lavorano di precisione". Va chiesto quali sono, se si possono nominare e se si possono fotografare.
12. **Seconda sede o vecchio indirizzo** a Noventa Padovana (via Polati): un risultato di ricerca lo cita, ma non ho trovato conferme.
13. **Zona servita, numero di persone, clienti.** Va chiesto se lavorano anche per imprese e condomini.
14. **Social e recensioni**: non ne ho trovati. Per questo nel piede non c'è la colonna Seguici.

## Permessi sulle foto

Tutte le foto in pagina sono foto di lavori Ferridea prese dal loro sito di oggi (`assets/originali/`, elenco in `assets/CREDITI.md`). Serve:
- il permesso dell'azienda, e dei clienti per le case riconoscibili (balcone con la porta rossa, scala con i gradini in rovere, scala in marmo della scheda Inox, i due cancelli);
- nel sito nuovo, rinominare i file che contengono nomi di clienti o di luoghi (Fanton Michele, San Giacomo, Treviso), cosa già fatta in `sito/img/`, e non citarli in didascalia.

## Foto da rifare dal vero (mezza giornata, luce di mattina laterale, cavalletto, fotocamera vera e non compatta)

1. **Apertura: la scala a sbalzo**, o un altro pezzo loro su un muro chiaro.
   - Ripresa frontale e diritta, obiettivo a 50-85 mm equivalenti, ottica in bolla, senza cucina e senza finestra in campo.
   - Luce laterale morbida, che faccia un'ombra netta sotto ogni gradino.
   - Almeno 6000 px di lato lungo.
   - Oggi è uno scontorno da una compatta del 2008: regge, ma i bordi sono morbidi.
2. **Dettaglio del ferro battuto.** Una voluta battuta da vicino (macro o 100 mm), con lo sfondo chiaro e uniforme dietro il cancello, per esempio con un telo grigio chiaro. Oggi si vede il selciato bagnato attraverso le volute, e la foto è appena sufficiente a 1312 px (ora tagliata a 2,6:1 e servita senza ingrandimento).
3. **Lamiera.** Il pannello a raggiera, frontale e diritto, senza scuri rossi dietro, a mezzogiorno con il cielo coperto.
4. **Inox.** Il parapetto a cavi della scala in marmo, frontale, senza quadri e lumi in campo, con un tele da 85-100 mm sui montanti e sul corrimano.
5. **Capottine.** La pergola bianca di nuovo, dal giardino, con il cielo e senza le case dei vicini; oggi il taglio lascia molto muro vuoto.
6. **Serramenti in alluminio** finiti e puliti, montati. Le foto di oggi sono di cantiere, con calcinacci: per questo non ci sono in pagina.
7. **Officina di viale Veneto**, di giorno, con le mani al lavoro, una saldatura molata e un chiavistello. È la foto giusta per la chiusura al posto della scala interna, e per la pagina `/azienda/`.
8. **Cancelli.** Il cancello a tre pannelli (tessera Cancelli) senza la casa gialla e l'albero sopra, a luce coperta; e il cancello in lamiera forata della chiusura da vicino, frontale, con il sole basso di lato che faccia leggere la superficie a vortici. Il portone ad arco del 2006 (1200x1600 px) è uscito dalla pagina: si può rifare per la pagina `/cancelli/` se il cliente lo permette.

## Licenze

- **Caratteri.** Archivo di Omnibus-Type, da Google Fonts, con licenza SIL Open Font License 1.1: uso commerciale libero, si può servire dal proprio dominio. I file sono in `sito/fonts/`.
- **Foto.** Sono dell'azienda (vedi sopra). Le foto Unsplash in `assets/esterne/` non sono usate nella versione finale e restano solo nei prototipi; le licenze sono in `assets/CREDITI.md`.

## Logo

- Il logo non esiste. La testata di oggi è testo in Arial blu.
- La scritta "FERRIDEA" in testata e nel piede è una **proposta**: Archivo larghezza 125, peso 600, maiuscolo spaziato 0,08 em. È testo HTML, non un'immagine.
- Va chiesto se esiste un marchio su insegna, furgone o carta intestata. Se esiste, va ridisegnato in SVG fedele e messo al posto della scritta.

## Pagine e link del sito nuovo

- **Pagine che restano agli indirizzi di oggi**, così non servono redirect: `/cancelli/`, `/capottine/`, `/parapetti/`, `/scale/`, `/serramenti/` e `/contatti/`.
- **Pagine nuove:**
  - `/azienda/`, la storia dal 1959 (la linka "Dal 1959" nel piede);
  - `/privacy/` e `/cookie/`, che oggi mancano.
- **Ancore della home:** `#lavori`, `#materiali`, `#officina` ("L'officina" nel piede) e `#contatti`.
- **"Saldature e riparazioni"** nel piede è testo senza link: nella home non c'è una sezione che ne parli. Se il sito nuovo avrà una pagina `/riparazioni/`, la voce diventa un link.
- **"Contatti"** compare nel piede solo come titolo della terza colonna (con telefono, cellulare, email e mappa); la pagina `/contatti/` resta e la linka il menu del sito completo.
- **Il marchio** in testata e nel piede punta a `/`.
- **Da togliere** dal sito di oggi: l'articolo di prova `/2016/11/01/hello-world/`.

## Consegna statica

- La pagina si apre anche con file:/// senza errori in console. Per questo non c'è il `<link rel="preload">` del carattere, che su file:// dà un errore CORS.
- Sul sito vero, servito in https, si può rimettere in `<head>`: `<link rel="preload" href="fonts/archivo-latin-var.woff2" as="font" type="font/woff2" crossorigin>`.

## Newsletter

Non c'è, e non va collegata a nessun servizio. Il motivo è nella NOTA: non hanno novità, fiere, cataloghi né collezioni da comunicare.
