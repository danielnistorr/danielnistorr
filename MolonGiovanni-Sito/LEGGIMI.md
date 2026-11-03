# Molon Giovanni: proposta di nuova homepage

Proposta non richiesta, solo la home. Nessun contatto con l'azienda, niente pubblicato.

- Pagina: `sito/index.html` (HTML e CSS a mano, si apre da file://), con `sito/img/` (WebP con srcset, logo SVG scuro e bianco) e `sito/fonts/` (Anek Latin, OFL).
- Versione attuale: **metodo ibrido** del 3/11/2026 (prima schermata secondo la sezione D, sotto i contenuti della versione professionale su una griglia sola). Direzione: `_prova/alto/DIREZIONE.md`; nota, misure e problemi aperti: `screenshot/home/NOTA.md` (sezione "Metodo ibrido"); misure: `node _prova/alto/misura-d.mjs` (risultati in `_prova/alto/misure/misure.json`); immagini: `python3 _prova/alto/script/img_alto.py`; screenshot: `node _prova/alto/script/shot.mjs`.
- Versione "livello professionale" (3/11/2026, con il ritocco finale): copiata com'era, sito e screenshot, in `_prova/versione-pro/`. I suoi script (`_prova/script/`) sono andati persi con il riavvio.
- Versione precedente ("Il pettine", 24/10/2026): copiata com'era in `_prova/versione-1-originale/`.
- Analisi con le fonti: `01-analisi.md`; scheda d'uso: `_prova/uso/SCHEDA.md`; tabelle dei modelli lette sul sito il 3/11/2026 in `_prova/crawl/`.

## Le email con la traccia vanno collegate
Nella home ibrida il modulo "Richiesta" non c'è più. Restano tre email con oggetto e traccia già scritti, una per bisogno, tutte a info@molonmachinery.com: "Scrivete" accanto a "Va sul vostro mezzo?" (oggetto "Va sul mio mezzo?": marca e modello del mezzo, presa di forza, ranghinatore, zona, nome e telefono), "Manda la foto per email" in Ricambi (oggetto "Ricambio Molon": modello e anno dalla targhetta, pezzo, numero sull'esploso, con le foto da allegare) e "Scrivete per il listino" per rivenditori e officine (oggetto "Rivenditori: listino e ordini"). Un mailto non porta allegati: per il sito vero conviene un modulo collegato a un servizio di invio che accetti le foto della targhetta e del pezzo (JPEG o PNG, qualche MB) e mandi una conferma a chi scrive, almeno per i ricambi.

## Da chiedere all'azienda prima di pubblicare
Nessuno di questi compare in pagina come segnaposto.
1. **Orari** dell'ufficio e del magazzino ricambi, chiusure estive, se ricevono in sede e se vendono anche ai privati. Servono nel blocco Ricambi (sotto il numero grande, con "oggi aperto" o "oggi chiuso"), nei contatti e nel piede (regola 15). Finché mancano, il blocco Ricambi dice solo "Se non rispondiamo, mandate la foto con il vostro telefono".
2. **Ricambi**: se si possono mandare le foto anche su WhatsApp (e a quale numero); tempi di consegna dei pezzi comuni (cinghie, pettini, denti, cuscinetti); se i rivenditori tengono o ordinano i ricambi (da scrivere per ogni rivenditore); se esiste un esploso per modello da mettere in PDF, o se lo mandano loro a chi non l'ha; dove si trova la targhetta sulle macchine vecchie e cosa fare se è illeggibile.
3. **Compatibilità per mezzo**: con quali portattrezzi e motofalciatrici funzionano i frontali e i MAJOR (negli annunci dei rivenditori compaiono Aebi, Reform, Rasant, Carraro, Brielmaier, Rapid, BCS, Agria: in pagina non ci sono finché Molon non le conferma), il verso della presa di forza e gli adattamenti. Con questi dati il contadino trova "va sul mio Reform a 540 giri" senza telefonare: vanno scritti in una riga "Va su:" sotto il titolo di ogni famiglia e in una riga "Presa di forza" in ogni tabella (giri, verso, attacco: 3 punti cat. I, flangia o attacco rapido per motofalciatrice). È il primo motivo per cui il compito 1 del contadino riesce solo a metà.
4. **Notazione dei rivenditori**: se 230/4, 250/5, 300/6 Pro (larghezza e file di denti, come negli annunci; anche il file del loro depliant si chiama `gEnio-230-4`) corrispondono ai loro modelli, per scriverla accanto ai nomi delle tabelle. Se il MAJOR della foto in campo ("MAJOR 180.3" sulla fiancata) è il MAJOR 180 della tabella con 3 doppi denti. Se MINI 120 (motofalciatrici) e MINOR MINI 120 (posteriori) sono la stessa macchina con due attacchi.
5. **Rivenditori e prezzo**: se il prezzo al pubblico lo fissa il rivenditore e se Molon vende anche ai privati (in pagina oggi: "Per il prezzo rivolgetevi al rivenditore o chiamateci"); chi risponde al telefono in tedesco e in inglese (per scrivere accanto al numero, per esempio "Wir sprechen Deutsch", solo se è vero). L'elenco aggiornato con città e telefono (in pagina diventa un bottone "Chiama" per ogni rivenditore), compresi Austria e Svizzera (sul mercato si vedono Gailer, Stöckl, Rietzler, Wohllaib, JK Landmaschinen, Lagerhaus, BayWa, Sepp Knüsel, ma non sappiamo quali sono partner); Earth Tools (Stati Uniti?), Snopex (sito non raggiungibile) e Tracmaster (Regno Unito, non tra i partner del sito) sono fuori dalla pagina. In pagina oggi: Gasser (Chiusa, BZ), Agrometal (Slovenia), Kalinke (Berg-Höhenrain, Germania), Agrisorg (Romania), con il sito.
6. **Depliant** in PDF in italiano, tedesco, inglese e francese, per famiglia: oggi sotto le tabelle ci sono i link alle pagine tedesca e inglese del sito di oggi.
7. **Prove (regole 10 e 11)**: il permesso di citare 2-3 recensioni Google con nome e comune (oggi 5,0 su 8, testi non leggibili); clienti o lavori che si possono nominare (un'azienda agricola, un consorzio, un comune che usa le scopatrici) con luogo, anno e due dati; certificazioni o dichiarazioni CE da mettere nel piede; le fiere (EIMA 2024 c'era?).
8. **Ragione sociale**: in pagina "Molon Giovanni S.r.l." come nell'intestazione, in Chi siamo e nella privacy di oggi; il piede del sito e gli elenchi dicono "Molon Giovanni s.n.c. di Molon Enio e Bruno". Da confermare la forma attuale, il REA (PD-147285, solo estratto), PEC e capitale sociale.
9. **Anno di gEnio** (in pagina "Oggi"; il 2025 è solo dedotto) e quale anno vogliono in evidenza tra 1936 (fabbro) e 1967 (ranghinatori a cinghie): nella home ibrida l'apertura non ha anni; il 1936 è nel piede e nella cronologia di Chi siamo, il 1967 solo nella cronologia.
10. **Video**: se i canali YouTube "alessandra molon" sono ufficiali; in pagina ci sono solo i video già incorporati nelle loro pagine prodotto e quello di presentazione.
11. Il codice del **rosso Molon** (in pagina #C8231B, campionato vicino alla vernice) e il **logo vettoriale** originale (oggi SVG ricostruito dal logo piatto grigio).
12. **Foto in pagina**: luogo, anno e autore della foto d'apertura (`2017_10_11.08_10ritoc.jpg`, frontale davanti a un portattrezzi in collina) e di quella del MAJOR 180.3 su prato di montagna (`2025_03_dok-tc-07-molon-br`), per scrivere la didascalia "che cosa, dove, anno" (oggi l'apertura non ha didascalia e quella del MAJOR non ha l'anno); se va bene che il portattrezzi dell'apertura (adesivo "G6") resti riconoscibile.

## Pagine del sito nuovo a cui puntano i link
Oggi i link della home vanno alle sezioni della pagina o alle pagine vere del sito di oggi (nessun link "#"):
- lingue IT, DE, EN, FR e "Datenblatt auf Deutsch" / "Data sheet in English": alle versioni WPML di oggi; nel sito nuovo andranno le versioni tradotte della home e delle schede;
- Girelli spandivoltafieno e Scopatrici: alle pagine di oggi;
- Privacy e Cookie: alle informative di oggi (D.Lgs. 196/2003, da aggiornare al GDPR);
- da creare: una pagina per ogni famiglia con tabella, optional e depliant; Ricambi con l'esploso; Rivenditori con la mappa disegnata dei paesi; Chi siamo.
Nessuna newsletter: non serve collegare servizi oltre alle email con la traccia.

## Foto da fare dal vero
In pagina ci sono solo foto dell'azienda. Reggono la proposta, ma sono di anni, luci e mani diverse (regola 5). Per il sito vero, una serie con un solo fotografo e la stessa luce:
- **Apertura**: una mattina di fienagione in collina, luce bassa di lato, il frontale che lascia l'andana davanti a un portattrezzi senza marchi in vista, camera bassa all'altezza dei denti; taglio largo 3:2 e taglio 16:9 per il telefono, almeno 4000 px. Chiedere anche l'originale non ritoccato di `2017_10_11.08_10ritoc.jpg` e chi l'ha scattata. Stessa inquadratura di oggi (il cielo libero in alto a destra serve al titolo), ma con il ranghinatore Molon in primo piano su almeno il 55 % della larghezza: oggi a 300 px il soggetto più grande è la cabina del portattrezzi (adesivo "G6") e la home sembra di un concessionario di trattori. Prova: nella miniatura a 300 px il riquadro del ranghinatore è più largo di quello della cabina.
- **Posteriori**: manca del tutto una foto in campo di un posteriore a 3 punti dietro un trattore (oggi la sezione ha solo la tabella).
- **Motofalciatrici**: un MINI o un MIKY con la motofalciatrice su un prato ripido, con la persona che guida.
- **Girelli e scopatrici** al lavoro (fieno sparso in pendenza; nocciole o foglie).
- **Ricambi**: la targhetta di una macchina (per mostrare dove si legge modello e anno), la cinghia con il cuscinetto in plastica, un pettine con i denti doppi: tre dettagli su fondo neutro, stessa luce.
- **Officina e persone**: saldatura, montaggio delle cinghie, verniciatura, Enio e Bruno Molon; la squadra di nuovo con luce morbida all'aperto (la foto di oggi è piatta). Per la foto di oggi: chi sono Enio e Bruno Molon (da sinistra), per scriverlo nella didascalia; fino alla conferma resta "La squadra, quattordici persone".
- **Archivio**: chiedere le stampe originali e scansionarle a 1200 dpi.
- **Schede delle macchine**: i sei scontornati della sezione "Le macchine" (frontale, posteriore, MAJOR, gEnio, girello, scopatrice) rifatti con la stessa camera, la stessa luce e lo stesso angolo, su fondo grigio neutro; per il gEnio oggi c'è solo la GIF del depliant (`2025_02_gEnio-230-4-depliant.gif`, 256 colori): chiedere l'originale. Una foto del gEnio in campo su un pendio, per la riga gEnio dei frontali.

## Licenze
- Foto: di Molon Giovanni, scaricate da molonmachinery.com (`assets/CREDITI.md`). Vanno chiesti gli originali e confermati i diritti delle foto in campo fatte da rivenditori o clienti.
- Le foto Pexels in `assets/esterne/` non sono usate nella home.
- Carattere: Anek Latin (Ek Type), SIL Open Font License 1.1 (`sito/fonts/OFL-Anek-Latin.txt`), file variabile latino `sito/fonts/anek-latin-var.woff2` da `@fontsource-variable/anek-latin` 5.1.0, servito dalla pagina. Sofia Sans della versione professionale non è più usata.

## Loghi
- `sito/img/logo-molon.svg` è ricostruito dal logo piatto grigio del sito (599 x 139 px); `logo-molon-bianco.svg` è lo stesso tracciato in bianco per il piede. Se esiste il vettoriale originale, va usato quello.
- I loghi dei partner e il banner EIMA non sono usati: sono marchi di terzi. I partner sono scritti in testo con il loro sito.
