# F.R.A.M.O., home: nota

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
