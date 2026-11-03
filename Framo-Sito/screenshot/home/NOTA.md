# F.R.A.M.O., home: nota

## Metodo ibrido (novembre 2026)

3/11/2026. Richiesta: "non è ancora super professionale" (giudice da agenzia a 6). Metodo scelto dal committente: prima schermata secondo la sezione D di `_metodo/professionale/ALTO-LIVELLO.md`, sotto i contenuti e le funzioni della versione professionale, rimessi su una griglia sola. La versione professionale com'era (pagina, immagini, caratteri e screenshot) è in `_prova/versione-pro/`. Direzione scritta prima dell'HTML: `_prova/alto/DIREZIONE.md`. Riga aggiunta in `_metodo/professionale/alto/REGISTRO-CARATTERI.md`.

### Che cosa è cambiato

- **Apertura, modello T (tipografia che mostra il mestiere).** Riferimenti: Pirtek UK (la carta millimetrata, un carattere, la didascalia di fatto; il sito oggi blocca le visite automatiche, quindi ci si è basati sulla scheda `alto/S.md`) e HANSA-FLEX (schermata del 3/11 in `_prova/alto/concorrenti/`). Il titolo è la scala dei diametri: "Tubi oleodinamici / da 3/16″ / fino a 3″", parole del loro articolo ("dal diametro di 3/16" fino a 3""). Il 3″ è alla misura vera: Red Hat Mono a 411 px, cifra alta 288 px, cioè tre quadrati da un pollice (96 px) della carta tecnica in CSS; la linea di base cade su una linea forte della carta (misurata: 828 px su 828). Il 3/16″ è alla stessa scala (cifra di 18 px). Sotto le due misure due filetti gialli lunghi quanto i diametri, 18 e 288 px. Niente cerchi né sezioni disegnate: solo cifre, filetti e carta. Sopra: la frase-firma "Porta il tubo vecchio: te lo rifacciamo identico", un solo bottone ("Manda la foto su WhatsApp" a 1440, "Chiama" a tutta colonna sotto i 1100 px) e "Saonara (PD), dal 1986". Nessuna foto (sono tutte di 1024 px: strada D2 tra 800 e 1600, alla misura vera e sotto).
- **Testata nera fissa**: logo vero (non più cliccabile), quattro voci che nominano quello che si cerca ("Tubi da campione", "Tubi su disegno e centraline", "Ricambi e marchi", "Come arrivare"), lo stato calcolato ("Aperto fino alle 12.30", solo da 1280 px in su) e il numero 049 644909 come link giallo alto 48 px, sempre in vista. Niente barra in basso sul telefono: il numero è già fisso in testata e sarebbe stato il terzo.
- **Culmine "Porta il tubo vecchio"**: la frase-firma come titolo (stesso trattamento dell'apertura, 40 px 500), la frase loro "identico nella lunghezza, tipologia e raccordatura" con la riga per i privati, il dopo (IMG-9596) a 954x634 su 9 colonne e il prima (IMG-9594) su 3, didascalie a due voci; i tre passi della foto in sola tipografia; "Come misurare un tubo". Le foto vengono dall'articolo "Il sistema Push Lock" del loro sito (25/7/2023): le didascalie lo dicono ("raccordo Push Lock montato, senza pressa", "fino a 16 bar") invece di farle passare per un tubo ad alta pressione.
- **Tubi su disegno e centraline**: titolo loro "Un distributore non si sceglie da un codice a catalogo", tipologie con le sigle in Red Hat Mono, "Che cosa mandarci", "Manda il disegno per email" (oggetto "Richiesta preventivo" e traccia), catalogo, centraline e condizioni di fornitura.
- **Ricambi e marchi**: i 16 marchi come righe d'indice (AMI, Manuli, Walvoil, Danfoss a 26 px, gli altri 12 a 19 px), tutti in una schermata dal menu; 600 mq dentro una frase; WhatsApp per la foto del pezzo come link.
- **Come arrivare**: "Officina e banco sono qui", indirizzo, descrizione della palazzina, "Apri la navigazione" (una volta sola in pagina), stato e tabella dei sette giorni con oggi in giallo.
- **Chiusura**, l'unico blocco giallo: "Fai una prova e in caso di dubbio, chiamaci.", "F.R.A.M.O. risponde sempre", lo stato e il modulo che compone l'email (campi ridotti: tolti email e quantità, che stanno nella traccia del preventivo).
- **Tolto**: la fascia gialla delle quattro cifre, le sei schede dei servizi, la sezione Settori e zone con i 16 comuni (le sei pagine per zona e i tre settori sono nel piede), gli occhielli maiuscoli, il numero a 120 px, i testi d'interfaccia in vista (restano a 14 px accanto al comando), la scheda Google Maps come secondo link, le fasce nere e grigie alternate. Da 9 a 6 sezioni, da 10.107 a 6.271 px a 1440.
- **Caratteri**: Red Hat Mono (gesto e dati) e Reddit Sans (titoli e testo), SIL OFL 1.1, in `sito/fonts/` con `OFL-RedHatMono.txt` e `OFL-RedditSans.txt`. Red Hat Text della riga del capitolo 5 è già in Griste e Tecnoplastic: Reddit Sans ha la stessa voce (grottesco aperto, tecnico, senza vezzi) e non è in nessuna home. Escono Anybody e Barlow.
- **Foto**: `assets/originali/` riscaricato dal loro sito (API dei media); provini in `_prova/alto/provini.jpg`; un solo trattamento (`_prova/alto/script/img.py`: bianco del tavolo verso il neutro, stessa curva, saturazione 0,88), WebP a 480, 768 e 1024 px con srcset. 2 foto, un formato (3:2), nessuna ingrandita a nessuna larghezza.
- **Colori**: carta #F3F1EA, inchiostro #1A1A19 e giallo #FFCD05 del logo. Due fondi di sezione (carta, giallo) più il piede nero. Contrasti: testo su carta 15,4:1, secondario su carta 6,7:1 e su giallo 5:1, giallo su nero 11,6:1.

### Misure (`node _prova/alto/misura-d.mjs`, esito in `_prova/alto/esito-d.txt`, dati in `misure-d.json`)

98 controlli su 98 passano.

- **Prima schermata 1440x900**: foto 0% (apertura di tipografia), 6 cliccabili (4 voci, numero, WhatsApp), 1 bottone, 159 caratteri fuori dal menu, nessuna fila d'ingressi, una sola cifra oltre i 30 px (il 3″ del gesto), nessun occhiello, `h1` di 7 parole senza virgole.
- **Prima schermata 390x844**: 4 cliccabili (numero, Menu, Chiama, WhatsApp), 1 bottone (Chiama, 350x56, a tutta colonna), carta tecnica con il gesto sul 90% dello schermo; stato con gli orari e "sabato chiuso", WhatsApp con il messaggio e la riga su che cosa fotografare, tutto sopra gli 844 px.
- **Pagina**: 747 parole, 6 sezioni, 6.271 px a 1440 (8.190 a 390), 0,24 MB a 1440 e 0,15 a 390; una griglia a 12 colonne con gli stessi bordi in tutte le sezioni e nel piede (80-1360 a 1440, 320-1600 a 1920, 20-370 a 390), bordi destri allineati; 2 famiglie; testo corrente di almeno 17 px; un solo elemento sopra i 100 px; frase-firma 2 volte con lo stesso trattamento; spazi tra le sezioni 54, 112, 136 e 176 px.
- **Ripetizioni**: numero scritto 2 volte (testata e piede), link `tel:` 2 a 1440 e 3 a 390 (più il Chiama dell'apertura), WhatsApp 2, `mailto:` 2, email scritta 2, navigazione 1, "Come misurare", catalogo e condizioni 2 ciascuno, 4 bottoni a 1440 e 5 a 390.
- Nessuno scorrimento orizzontale, nessuna sovrapposizione, nessun errore di script a 320, 390, 768, 1024, 1440 e 1920. Nessun U+2014, nessun "indicativ", nessun repertorio, nessun gradiente, dissolvenza, transizione, vetro, corsivo o iframe nel sorgente; nessuna ISO 9001 in vista.

### Compiti della scheda: dove stanno ora

- **V1.1 aperto adesso**: a 390 sotto WhatsApp nella prima schermata ("Aperto ora, chiude alle 12.30" con gli orari e "sabato chiuso"); a 1280 px e oltre nella testata. Provato alle 10.00 e alle 13.00 di martedì, sabato, l'8 dicembre e venerdì alle 18.30.
- **V1.2 chiamare**: numero nella testata fissa (48 px, si tocca anche a metà pagina) e "Chiama" 350x56 nella prima schermata.
- **V1.3 WhatsApp**: nella prima schermata con il messaggio pronto e la riga su che cosa fotografare; i tre passi finiscono a 1.562 px a 390 (entro due schermate).
- **V1.4 da campione e come arrivare**: la frase "identico nella lunghezza, tipologia e raccordatura" finisce a 1.173 px; prima e dopo cominciano a 1.598 px (il dopo finisce a 1.729, 41 px oltre le due schermate); "Come arrivare" è nel menu e dopo il salto "Apri la navigazione" e il numero in testata sono nello schermo.
- **V2.1 mestiere e scala**: `h1` "Tubi oleodinamici da 3/16″ fino a 3″", "Saonara (PD), dal 1986", voce di menu "Tubi su disegno e centraline". L'email non è più nella prima schermata (tetto di 160 caratteri): sta nella sezione dal menu, scritta accanto al bottone.
- **V2.2 marchi**: dal menu "Ricambi e marchi" i 16 marchi sono tutti nello schermo a 1440x900 (l'ultimo finisce a 740 px).
- **V2.3 e V2.4**: dal menu, tipologie, "Manda il disegno per email" con la traccia, catalogo e condizioni entro la schermata (le condizioni finiscono a circa 880 px); P.IVA nel piede.
- **V3**: la riga per i privati è nel testo del culmine (finisce a circa 1.170 px a 390); "Come misurare un tubo" nel culmine e nel piede; orari e strada senza altre pagine; modulo con "(se sei un privato, lascia vuoto)", campo mancante detto per nome con il fuoco sul nome, mail composta con "Azienda e P.IVA: privato".

### Guardato a pezzi

Pagine intere a 1440 e a 390 in colonne, prime schermate a 320, 768, 1024 e 1920, chiusura a 1440, accanto alla versione professionale e a HANSA-FLEX (`_prova/alto/confronto-1440.jpg`). Screenshot rifatti con gli stessi nomi (`node _prova/alto/script/screenshot.mjs`, ora del test martedì 10.00).

### Problemi aperti

- **La foto vera manca ancora.** Il gesto regge senza foto, ma la riga del capitolo 5 chiede accanto la macro della guaina di un loro tubo a due trecce con la scritta stampata: va fatta (LEGGIMI, foto da fare). La macro IMG-9592 resta fuori (TEXMASTER, SAE 100R6 a bassa pressione).
- **Il prima e dopo è un Push Lock** (fino a 16 bar), non un tubo da campione pressato: le didascalie lo dicono, ma la coppia "campione usurato / tubo nuovo" va fotografata. Il luogo dello scatto (sede di Saonara) è presunto: va confermato con l'autore delle foto.
- **La scala vera vale solo sul monitor a 96 px per pollice** (1440 e 1920). Sul telefono il 3″ è a 250 px; restano veri i filetti di 18 e 288 px.
- A 390 il dopo finisce 41 px oltre le due schermate (comincia dentro); a 1440 finisce a 1.829 px, comincia a 1.193.
- Il servizio fotografico e i nomi delle persone (squadra, chi risponde) restano le cose che servono per andare oltre l'8, come per tutto il gruppo S.
- Restano aperti i punti del LEGGIMI: privati, ISO 9001, recensioni, lavori con il nome, tempi del servizio da campione, ferie.
- Gli script di prima in `_prova/script/` (build_finale.sh, pro_controlli.mjs) non sono più sul disco dopo il riavvio: per questa versione valgono `_prova/alto/script/img.py`, `screenshot.mjs` e `_prova/alto/misura-d.mjs`.

---

Pagina: `sito/index.html` (statica, si apre anche da file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini da `_prova/script/pro_img.py`, pagina da `_prova/script/pagina.html`, caratteri da `_prova/home/a/fonts/` e `assets/fonts-barlow/`, screenshot con gli stessi nomi di prima). Controlli: `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), `node _prova/script/pro_largo.mjs 320 390 768 1024 1440 1920` (scorrimento orizzontale) e `node _prova/script/altezze.mjs 390 mobile` (altezza di ogni sezione).

La versione di prima (la "tavola tecnica" con il calibro) è copiata com'era in `_prova/versione-1-originale/`.

Altezza: 10107 px a 1440, 12899 px a 390 (prima del ritocco 9325 e 13872).

## Livello professionale (3/11/2026)

Richieste: "non rappresentano bene l'identità e l'utilizzo corretto di quello che dovrebbe essere il sito", "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia S. Scheda d'uso: `_prova/uso/SCHEDA.md`. Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14; le pagine intere di Kline e Wilson (primo giro), di Eggentaler e Dulwich Diggers (ritocco) a pezzi.

### Ritocco finale: che cosa è cambiato

Dal controllore del livello (voto 6) e dalle due prove con i clienti tipo.

1. **Apertura senza la macro.** La macro IMG-9592 aveva come scritta più grande "TEXMASTER" (non tra i loro marchi) ed era un SAE 100R6 a treccia tessile accanto a "altissime pressioni". Al suo posto, nella colonna 8/13, un blocco tipografico pieno in giallo del marchio, alto quanto il testo: "La specialità F.R.A.M.O.", "da 3/16"" a 72 px e "fino a 3"" a 200 px, poi "Tubazioni raccordate per alte e altissime pressioni, su ordinazione o da campione" (A7: home fatta di tipografia, come barth e Holzrausch). A 390 il blocco sta sotto i bottoni. La macro non è più in pagina.
2. **Sede tolta.** La foto azienda-01 porta la filigrana "© 2018 Google" in alto e a sinistra: è una cattura di Street View, non una foto loro. La sezione "Dove siamo" ora si regge sul testo (palazzina bianca con la fascia gialla e blu, cancello con il 32), con "Apri la navigazione" e "Chiama" subito sotto il titolo e la tabella dei sette giorni con il giorno di oggi in giallo. Il link "La scheda F.R.A.M.O. su Google Maps" usa l'identificativo della scheda preso dalla mappa del loro sito (`cid=4249055688706121423`) ed è alto 48 px.
3. **Griglia dei servizi** "Che cosa facciamo" (titolo loro: "Un grande magazzino, una moderna officina"), 6 schede su 3 colonne, passo 24 px, tutta la scheda è il link; copertina 3:2 su nero con il numero e la sigla in giallo: 3/16"-3" (tubi su misura), Identico (da campione), 600 mq (ricambi), Su progetto (centraline), 10 bar (pneumatica), 8 e 9 trefoli (sollevamento). Tolti i quattro accessi in fondo all'apertura (doppi con il menu e con la griglia); al loro posto il link "Costruttori: tubi su disegno e centraline" per l'ufficio tecnico.
4. **Numeri**: 1986, 600 mq, 16 (marchi, da Manuli a Walvoil), AMI (distributore ufficiale a Padova). Tolti "21 schede tubo" (contava le pagine del sito) e il 3/16"-3" (ora nell'apertura).
5. **Marchi con gerarchia**: AMI, Manuli, Walvoil e Danfoss in quattro caselle grandi a 48 px, gli altri 12 in sei colonne; Manuli, Balflex e ZEC con il numero di schede del loro catalogo (7, 9, 5). Tutti e 16 in una schermata a 1440x900. Sul telefono solo i nomi, su due colonne.
6. **Prima e dopo**: un solo formato (3:2), etichette "Prima" e "Dopo" nell'angolo al posto della didascalia; sotto i 700 px a tutta colonna (350x233 invece di 169x113). Stesso trattamento per le due foto (bianco neutro dal tavolo, saturazione 0,85, stessa curva).
7. **Tipologie**: aggiunte le sigle dei tubi in gomma che hanno nel catalogo (1SN, 2SN, 1SC, 2SC, 4SP, 4SH, dalle schede Manuli Rockmaster e Balflex).
8. **Caratteri**: Anybody 700 solo per titoli e cifre; testo, etichette, menu, bottoni e modulo in **Barlow** 400 e 700 (sans robusta da cartello stradale, non usata in nessun'altra home della campagna).
9. **Modulo**: campo "Quantità (pezzi o serie)", "Azienda e P.IVA", "Quando ti serve" su una riga (prima scelta accorciata in "Subito, macchina ferma", valore uguale), dopo l'invio il riquadro "Non si è aperto niente?" con "Copia il testo" e "Copia l'indirizzo" per chi usa la posta nel browser.
10. **Stato aperto o chiuso**: elenco `CHIUSURE` per ferie e ponti (vuoto finché l'azienda non dà le date; provato con date finte: "Chiuso per ferie, riapre lunedì 24 agosto alle 8.30").
11. **Telefono**: sotto i 700 px la chiusura mostra solo il numero grande, lo stato e WhatsApp (gli altri recapiti sono nel piede); servizi senza descrizione, settori senza riga di testo, passi più compatti: 12899 px contro 13872, con una sezione in più.
12. **Piede**: tolti "Certificazioni" e la politica per la qualità del 2022 finché non arriva il rinnovo ISO 9001; aggiunto "Come misurare un tubo".
13. Sotto la WhatsApp dell'apertura la riga "Fotografa il tubo intero, i due raccordi e la scritta sulla guaina."; "Come arrivare" ed email con area di tocco di 48 px; numero grande della chiusura che non va a capo da 701 a 1099 px; bottone "Menu" accanto al numero nelle testate da tablet.

### Le 15 regole, una per una

Misure di `pro_controlli.mjs` (`_prova/pro_controlli.json`), più gli screenshot guardati a pezzi a 1440 e 390 (pagina intera) e a 320, 768 e 1024 (pagina intera, solo per controllo, non salvate).

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa, 85 px a 1440 e 73 a 390; bottone giallo "049 644909" alto 48 px. A 390, a metà pagina, il bottone si vede e si tocca (`elementFromPoint`). 7 link `tel:+39049644909`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** 1440x900: H1 a 72 px, "Saonara (PD) · dal 1986", stato, Chiama, WhatsApp, email, il blocco 3/16"-3"; la fascia gialla comincia a 900 px, niente cifre tagliate. 390x844: Chiama largo 350 px su 350, alto 56; WhatsApp con il testo pronto; "Come arrivare"; il blocco comincia a 811 px, sotto i bottoni. La prova resta "dal 1986": recensioni e certificato da chiedere (LEGGIMI).
3. **Immagine vera nell'apertura: non passa, per scelta.** Le foto vere che reggono non mostrano persone, mezzi o sede, e il committente ha escluso illustrazioni e repertorio. L'apertura è tipografica (A7, "home fatta di tipografia"): nessuna immagine, nessun oggetto scontornato. La foto da fare è la 1 del LEGGIMI.
4. **Zero repertorio: passa.** "indicativ" 0, "provvisori" 0, nessun file da `assets/esterne`, Unsplash o Pexels. In `sito/img/` solo il prima e dopo (IMG-9594, IMG-9596), il logo e il simbolo. Tolta anche la cattura di Street View.
5. **Foto in serie: passa.** Due foto della stessa ripresa (stesso tavolo, stessa luce), un solo formato (3:2, anche le copertine delle schede), stesso trattamento, nessuna didascalia (solo le etichette Prima e Dopo), nessuna ingrandita oltre il file.
6. **Palette dal marchio: passa.** `--giallo` #FFCD05 (simbolo e insegna) e `--nero` #1A1A19 (scritta del logo), con `--giallo-scuro` e `--nero-2` per il passaggio del mouse; `--bianco` e i grigi freddi. Niente beige, niente testo giallo su chiaro.
7. **Scala corta: passa.** 8 misure a 1440 (15, 17, 19, 23, 48, 72, 120, 200) e 8 a 390 (15, 16, 17, 20, 22, 30, 40, 56). Testo corrente 19 px a 1440 e 17 a 390; il più piccolo 15 px. H1 72/40, H2 48/30.
8. **Due famiglie: passa.** Anybody (titoli e cifre, 700) e Barlow (testo e interfaccia, 400 e 700): ruoli fissi in tutta la pagina.
9. **Servizi in schede con la foto del lavoro: passa in parte.** La griglia c'è (6 schede, 3 colonne a 1440, 2 da 701 a 1099 e sotto i 700, passo 24 px, copertine tutte 411x274 a 1440, tutta la scheda cliccabile), ma la copertina è tipografica: loro non hanno una foto per ogni lavorazione. Quando arrivano le foto del LEGGIMI (punto 4) vanno nella stessa area 3:2.
10. **Almeno tre tipi di prova: non passa (2 su 4).** Numeri (4) e fascia dei fornitori con la didascalia (AMI distributore ufficiale, schede nel catalogo). Recensioni (4,8 su 11 su Google) e clienti con il nome non sono in pagina finché l'azienda non dà il permesso e i nomi (LEGGIMI, punti 3 e 5).
11. **Lavori con un nome: non passa.** Nessun lavoro con cliente, luogo e anno nelle fonti (LEGGIMI, punto 4).
12. **Ritmo a blocchi: passa.** Nero (apertura, ricambi, dove), giallo (numeri, chiusura), grigio (da campione), bianco (servizi, ufficio, zone). Sezioni 120/120 px a 1440 e 72/72 a 390 (fascia dei numeri 56 e 48). Margini 80 px a 1440, 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno giallo (nero sui fondi gialli) e bordato, raggio 4 px, 56 px (48 in testata e nel modulo), testo 17 px (16 in testata a 390). I bottoni di chiamata contengono il numero.
14. **Modulo e zone per il mestiere: passa.** Tipo di richiesta, quantità, macchina, codice, urgenza (subito con la macchina ferma, in settimana, senza fretta), descrizione, istruzione per foto e disegni (un mailto non porta allegati); niente indirizzo dell'intervento perché lavorano al banco. 16 comuni con la loro pagina. Nessun iframe. Compilato, compone `mailto:commerciale@framosrl.com` con oggetto "Un ricambio o un componente - macchina ferma - Mario Prova" e tutti i campi.
15. **Piede completo: passa con riserva.** Ragione sociale, P.IVA e C.F. 02075000287, indirizzo, telefono, WhatsApp ed email cliccabili, orari con il sabato, zone e settori, lavorazioni, condizioni di fornitura, Privacy e Termini; 4 colonne a 1440, testo di almeno 15 px. Manca la certificazione, tolta finché il rinnovo ISO 9001 non è confermato (il certificato scadeva il 22.06.2026).

### Compiti della scheda (par. 8)

- *Macchina ferma, telefono*: senza scorrere stato (martedì 11.00 "Aperto ora, chiude alle 12.30", martedì 13.00 "Chiuso ora, riapre alle 14.00", sabato 10.00 "Chiuso ora, riapre lunedì alle 8.30", 8 dicembre "Chiuso oggi, festivo, riapre domani alle 8.30"), Chiama a tutta larghezza alto 56 px, WhatsApp con il messaggio e, sotto, che cosa fotografare. "Come arrivare" porta alla sezione Dove: titolo, descrizione della palazzina, "Apri la navigazione" e "Chiama" restano nello schermo dopo il salto. Meno di prima: la foto della sede non c'è più (era di Google); resta la descrizione, e la scheda Google si apre con un tocco.
- *Ufficio tecnico, computer*: telefono, WhatsApp, email e "Costruttori: tubi su disegno e centraline" nella prima schermata; i 16 marchi in una schermata dal menu "Ricambi e marchi", AMI, Manuli, Walvoil e Danfoss in grande; sigle 1SN-4SH nelle tipologie; mail con oggetto "Richiesta preventivo" e la traccia (con quantità e P.IVA); catalogo e condizioni nella sezione Centraline; nessuna certificazione scaduta in vista.
- *Privato*: la riga "Anche se sei un privato..." sotto i tre passi, la guida "Come misurare un tubo" (anche nel piede), orari e indirizzo senza aprire altre pagine.
- *Identità*: frasi loro ("Porta il tubo vecchio", "Un grande magazzino, una moderna officina", "Pompa malfunzionante...", "ci chiamano prima di ordinare", "Fai una prova e in caso di dubbio, chiamaci", "F.R.A.M.O. risponde sempre"), logo vero, giallo come campitura e mai come testo su chiaro.

### Caratteri e licenze

- **Anybody** (Etcetera Type Co.), Google Fonts, SIL Open Font License 1.1: `sito/fonts/anybody-latin*.woff2`, licenza `OFL-Anybody.txt`. Solo 700, per titoli e cifre.
- **Barlow** (Jeremy Tribby, The Barlow Project), Google Fonts, SIL Open Font License 1.1, uso commerciale libero: `sito/fonts/barlow-400-latin*.woff2` e `barlow-700-latin*.woff2`, licenza `OFL-Barlow.txt` (scaricati da fonts.gstatic.com il 3/11/2026, copia in `assets/fonts-barlow/`).
- Foto: solo IMG-9594 e IMG-9596 dal loro sito, più il logo. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Controlli fatti (3/11/2026, dopo il ritocco)

- `pro_controlli.mjs`: regole 1, 2, 4, 5, 6, 7, 8, 12, 13, 14 superate; 9 e 15 in parte; 3, 10, 11 no, per i motivi detti. Nessuna ancora senza destinazione; menu a 390 aperto e richiuso; modulo vuoto fermato con "Mancano il nome e il telefono" e il fuoco sul nome.
- Nessuno scorrimento orizzontale a 320, 340, 360, 380, 390, 414, 600, 700, 701, 768, 900, 1024, 1099, 1100, 1200, 1279, 1280, 1440, 1920, 2560 (misurato dopo il caricamento dei caratteri; `pro_largo.mjs` ora lo aspetta).
- Screenshot guardati a pezzi: 1440 e 390 pagina intera, 320, 768 e 1024 pagina intera, prime schermate a 1920. Nessuna sovrapposizione. Nessun U+2014 in pagina, nei .md e negli script.
