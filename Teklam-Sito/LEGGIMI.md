# Tek.Lam S.r.l., proposta di nuova home

Proposta non richiesta: solo la home, da mostrare all'azienda. Non è pubblicata e l'azienda non è stata contattata.

- `01-analisi.md`: azienda, sito di oggi, fatti con le fonti, materiale visivo, direzioni artistiche, riferimenti.
- `sito/`: la home finale (`index.html`, `img/`, `fonts/`). Si apre con file:///. Sostituisce la versione precedente (quella col raggio rosso e Mona Sans).
- `screenshot/home/`: home intera e prima schermata a 1440 e a 390, più `NOTA.md` (idea, prime due schermate, caratteri, colori, interazione, foto, controlli).
- `assets/originali/`: le immagini del sito teklam.it. `assets/esterne/`: foto Unsplash e Pexels scaricate come segnaposto (nella home finale resta solo la spazzolatura della lastra), licenze in `assets/CREDITI.md`.
- `_prova/`: lavoro di servizio (crawl, riferimenti, prototipi A e B in `_prova/home/`, script). `bash _prova/script/build_finale.sh` rifà immagini, caratteri, pagina, controlli e screenshot.

## L'idea in una riga

La home è una lastra di inox 3000 x 1500 appena tagliata: TEK.LAM è tagliato via e nei vuoti si vede il loro laser che taglia; le sei lavorazioni sono sei pezzi ancora annidati, ricalcati da pezzi veri delle loro Realizzazioni; toccandone uno si solleva e sul resto del foglio, inciso nel metallo, compaiono la foto di quel pezzo e la macchina.

## Da confermare con Tek.Lam prima di pubblicare

- **Spessori massimi del laser**: in pagina (riga 01 della distinta, interruttore Ferro, Inox, Alluminio) ci sono quelli della home di oggi, 20/15/10 mm. La pagina Attrezzature dice 25/15-20/12 mm. Quando arriva il dato giusto si cambia `SPESSORI` in `_prova/script/finale_build.py`.
- **Pezzi e lavorazioni**: le sei sagome del foglio sono ricalcate dalle foto di Realizzazioni (case per elettromedicale, griglie per movimento terra, cassetto per arredo odontoiatrico, telaio inox, telaio in tubolare per banco frigo) e dal render `2020-08-pc.jpg`. Ogni pezzo è messo sotto una lavorazione (case sotto taglio laser, griglia sotto punzonatura, cassetto sotto piegatura, telaio inox sotto saldatura, telaio frigo sotto tubi e profili): l'abbinamento è dedotto dalle foto, va confermato pezzo per pezzo. In pagina il cartellino dice solo "da una nostra realizzazione", non con quale macchina è stato fatto quel pezzo.
- Portata delle piegatrici: home "3100x100 T e 3100x125 T", Attrezzature "3100×120 t" e "3100×100 t". In pagina solo la lunghezza utile, 3100 mm.
- La Trumpf TrumaBend V170 della foto caricata nel 2024: è in officina? Se sì l'elenco delle macchine è vecchio e la riga Piegatura va aggiornata (non è in pagina).
- Cesoia Gasparini ("fino a mm 3000 di lungh. x sp. 6 8"): in pagina solo la lunghezza. Troncatrice OMES "fino a 120 mm": diametro o lato? In pagina come nella fonte.
- Autocarro con gru ("35 qli complessivi") e "7,5 di pianale" del centinato: in pagina solo "autocarro con gru" e "50 quintali di portata utile".
- Zincatura e sabbiatura: la pagina Attrezzature le dà su impianti esterni collegati ("anche con sabbiatura e zincatura a freddo e/o caldo"); in pagina sono scritte così. Confermare che sia ancora vero.
- Indirizzo: "Via del Lavoro, 68" (contatti) o "Viale del Lavoro, 68" (privacy). In pagina c'è Via.
- PEC e data di costituzione della S.r.l., da aggiungere nel piede.
- La forma della storia: in pagina "Tek.Lam nasce come carpenteria di piccoli manufatti in ferro battuto", "nel 2020 la «storica» FDS Volpato S.n.c. passa il testimone a Tek.Lam S.r.l." e "l'esperienza dei fondatori, dal 1978" (tutte frasi del loro sito). Va bene così?
- Il render `2020-08-pc.jpg` del pezzo 06 è un modello del loro ufficio tecnico? Oggi la didascalia resta generica ("Modello 3D di un pezzo in lamiera, prima di tagliare il foglio").
- Settori e note: vengono dalle schede di Realizzazioni del 2020. Sono ancora attuali? Lavorano anche per la moda o la pelletteria del distretto? Non scritto.
- Certificazioni, numero di macchine, superficie dell'officina, clienti citabili, un lavoro con nome e anno: oggi non ci sono. Un lavoro con nome e anno sarebbe il contenuto più forte da aggiungere.
- Dati Atoka (8 dipendenti, 1,0 milioni di ricavi): non usati senza consenso.
- Uso delle foto del loro sito (tutte quelle della pagina, tranne la spazzolatura della lastra) e consenso delle persone ritratte (il saldatore, la mano sulla piegatrice).
- Link: "Macchine e misure" nel cartellino porta alla riga della distinta; Privacy e Cookie puntano alle pagine di oggi su teklam.it, da rifare con il nuovo sito.

## Foto da rifare dal vero

Oggi in pagina c'è una sola foto di repertorio, la spazzolatura della lastra (apryan widodo, Unsplash, luce rifatta). Tutte le altre sono di Tek.Lam, ma sono fotogrammi da telefono di 470-1330 px e ritagli di 240-380 px dai collage di Realizzazioni: reggono come documento, non come stampa. Mezza giornata di fotografo in officina, file da almeno 3000 px di lato lungo:

1. **La lastra della prima schermata** (rende vera l'idea): un foglio di inox spazzolato o decapato 3000 x 1500 fotografato dall'alto, in pianta, sul banco o su un cavalletto, con una sola luce radente calda da sinistra in alto (portone o lampada morbida a 20-30 gradi), dopo il taglio con lo scheletro e i pezzi ancora dentro. Obiettivo lungo da lontano per non deformare, a f/8.
2. **Il letto a punte del loro Byspeed**, sotto la lastra: di sera, con la macchina che taglia ferro spesso, ripreso basso, le punte del banco e le scie delle scintille, fermo e nitido; sostituisce il fotogramma mosso di `slide2-2` nei vuoti delle lettere.
3. **I sei pezzi veri** del foglio (o sei pezzi recenti che preferiscono mostrare), ognuno fotografato da solo su fondo scuro, a 45 gradi, con la stessa luce: vanno nelle finestre del cartellino al posto dei ritagli dai collage, e da quelle foto si ridisegnano le sagome.
4. **Le macchine per le strisce**: SG6 con il pezzo separato e impilato all'uscita (al posto di `slide3`), piegatrice con la mano sulla lamiera, più luminosa di `slide4`, Byspeed con un foglio tagliato sul piano, Pedrazzoli con un tubolare curvato.
5. **La storia**: la saldatura TIG sul cassone col film blu rifatta a piena risoluzione, stessa scena di `slide1`; Sandro e Dimitri Volpato in officina, sul lavoro e non in posa.
6. **Sede e mezzi** a 3000 px, la palazzina con l'acero rosso e i due autocarri, in una giornata coperta.

## Caratteri e licenze

- Big Shoulders Display e Sofia Sans (Google Fonts), SIL Open Font License 1.1: uso commerciale libero, file serviti dalla pagina in `sito/fonts/`, licenze in `sito/fonts/OFL-bigshouldersdisplay.txt` e `OFL-SofiaSans.txt`. Niente monospazio.
- Foto di repertorio: una sola in pagina, la spazzolatura della lastra (Unsplash License; URL, autore e note in `assets/CREDITI.md`). Nessuna immagine generata dall'IA.

## Loghi

Il segno in testata e nel piede è ritagliato dal PNG verticale del loro sito (`2020-07-logo-TEKLAM.png`, 1772 px); la scritta TEK.LAM è composta in Big Shoulders Display, TEK pesante e LAM chiaro come nel marchio, e le lettere tagliate nella lastra sono disegnate a mano sulla stessa logica. Serve il logo vettoriale (SVG o PDF) da Tek.Lam per confermare proporzioni e colore del rosso.

## Righe "da guardare" dei controlli (segnali.sh, 0 bloccanti)

- 6 fasce di fondo: grafite della riga e della frase, carta delle lavorazioni e della storia (spezzata da due foto a tutta larghezza), carta dei settori, grafite dei contatti e del piede. Non sono fasce alterne uguali: la carta è interrotta dalle foto della SG6, della saldatura e della piegatrice.
- 12 voci numerate: i numeri 01-06 sono i pezzi del foglio, ripresi nella distinta per legarla alla prima schermata; 1-6 sono le note dei settori.
- "1 altro gradiente": le tacche della scala in millimetri e il tratteggio della sezione, righe nette e non sfumature.

## Prototipi

`_prova/home/a/` ("Il foglio annidato", scelto) e `_prova/home/b/` ("Scintilla e spessore"), ognuno con la sua `nota.md`. Dalla B la home finale prende la luce calda, la tavolozza, l'interruttore degli spessori, le strisce foto, "Dal ferro battuto alla lamiera", la frase dei settori e il telefono grande dei contatti.
