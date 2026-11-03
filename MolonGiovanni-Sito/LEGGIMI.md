# Molon Giovanni: proposta di nuova homepage

Proposta non richiesta, solo la home. Nessun contatto con l'azienda, niente pubblicato.

- Pagina: `sito/index.html`, con `sito/img/` (WebP alla misura giusta, logo SVG scuro e bianco) e `sito/fonts/` (Sofia Sans, OFL).
- Versione attuale: "livello professionale" del 3/11/2026, con il ritocco finale dello stesso giorno (apertura su blocco antracite, sezione "Le macchine" con sei schede fotografiche, tabelle dei posteriori e delle motofalciatrici che si aprono, numeri aziendali senza date ripetute). Nota di progetto ed esito delle 15 regole: `screenshot/home/NOTA.md`. Misure: `_prova/pro_controlli.json`. Sorgente della pagina: `_prova/script/pagina-pro.html`.
- Per rifare tutto: `bash _prova/script/build_finale.sh`.
- Versione precedente ("Il pettine", 24/10/2026): copiata com'era in `_prova/versione-1-originale/`.
- Analisi con le fonti: `01-analisi.md`; scheda d'uso: `_prova/uso/SCHEDA.md`; tabelle dei modelli lette sul sito il 3/11/2026 in `_prova/crawl/`.

## Il modulo di contatto va collegato
Oggi il modulo "Richiesta" in fondo alla home compone un'email (mailto a info@molonmachinery.com, con oggetto secondo il tipo di richiesta e tutti i campi nel testo) e la apre nel programma di posta di chi scrive. Un mailto non porta allegati: la pagina chiede di allegare le foto all'email che si apre. Per il sito vero va collegato a un servizio di invio (il modulo del CMS o un servizio di moduli) che accetti anche le foto della targhetta e del pezzo (JPEG o PNG, qualche MB) e mandi una conferma a chi scrive. Lo stesso vale per i bottoni "Manda la foto per email" (Ricambi), "Scrivete" accanto a "Va sul vostro mezzo?" (frontali, posteriori, motofalciatrici: oggetto "Va sul mio mezzo?", traccia con marca e modello, presa di forza, zona) e "Scrivete a info@molonmachinery.com" (Rivenditori), che oggi sono mailto con oggetto e traccia.

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
9. **Anno di gEnio** (in pagina "Oggi"; il 2025 è solo dedotto) e quale anno vogliono in evidenza tra 1936 (fabbro) e 1967 (ranghinatori a cinghie): in apertura oggi c'è solo "dal 1936"; il 1967 è nel titolo del browser e nella cronologia di Chi siamo.
10. **Video**: se i canali YouTube "alessandra molon" sono ufficiali; in pagina ci sono solo i video già incorporati nelle loro pagine prodotto e quello di presentazione.
11. Il codice del **rosso Molon** (in pagina #C8231B, campionato vicino alla vernice) e il **logo vettoriale** originale (oggi SVG ricostruito dal logo piatto grigio).

## Pagine del sito nuovo a cui puntano i link
Oggi i link della home vanno alle sezioni della pagina o alle pagine vere del sito di oggi (nessun link "#"):
- lingue IT, DE, EN, FR e "Datenblatt auf Deutsch" / "Data sheet in English": alle versioni WPML di oggi; nel sito nuovo andranno le versioni tradotte della home e delle schede;
- Girelli spandivoltafieno e Scopatrici: alle pagine di oggi;
- Privacy e Cookie: alle informative di oggi (D.Lgs. 196/2003, da aggiornare al GDPR);
- da creare: una pagina per ogni famiglia con tabella, optional e depliant; Ricambi con l'esploso; Rivenditori con la mappa disegnata dei paesi; Chi siamo.
Nessuna newsletter: non serve collegare servizi oltre al modulo.

## Foto da fare dal vero
In pagina ci sono solo foto dell'azienda. Reggono la proposta, ma sono di anni, luci e mani diverse (regola 5). Per il sito vero, una serie con un solo fotografo e la stessa luce:
- **Apertura**: una mattina di fienagione in collina, luce bassa di lato, il frontale che lascia l'andana davanti a un portattrezzi senza marchi in vista, camera bassa all'altezza dei denti; taglio largo 3:2 e taglio 16:9 per il telefono, almeno 4000 px. Chiedere anche l'originale non ritoccato di `2017_10_11.08_10ritoc.jpg` e chi l'ha scattata.
- **Posteriori**: manca del tutto una foto in campo di un posteriore a 3 punti dietro un trattore (oggi la sezione ha solo la tabella).
- **Motofalciatrici**: un MINI o un MIKY con la motofalciatrice su un prato ripido, con la persona che guida.
- **Girelli e scopatrici** al lavoro (fieno sparso in pendenza; nocciole o foglie).
- **Ricambi**: la targhetta di una macchina (per mostrare dove si legge modello e anno), la cinghia con il cuscinetto in plastica, un pettine con i denti doppi: tre dettagli su fondo neutro, stessa luce.
- **Officina e persone**: saldatura, montaggio delle cinghie, verniciatura, Enio e Bruno Molon; la squadra di nuovo con luce morbida all'aperto (la foto di oggi è piatta).
- **Archivio**: chiedere le stampe originali e scansionarle a 1200 dpi.
- **Schede delle macchine**: i sei scontornati della sezione "Le macchine" (frontale, posteriore, MAJOR, gEnio, girello, scopatrice) rifatti con la stessa camera, la stessa luce e lo stesso angolo, su fondo grigio neutro; per il gEnio oggi c'è solo la GIF del depliant (`2025_02_gEnio-230-4-depliant.gif`, 256 colori): chiedere l'originale. Una foto del gEnio in campo su un pendio, per la riga gEnio dei frontali.

## Licenze
- Foto: di Molon Giovanni, scaricate da molonmachinery.com (`assets/CREDITI.md`). Vanno chiesti gli originali e confermati i diritti delle foto in campo fatte da rivenditori o clienti.
- Le foto Pexels in `assets/esterne/` non sono usate nella home.
- Carattere: Sofia Sans, SIL Open Font License 1.1 (`sito/fonts/OFL-Sofia-Sans.txt`), servito dalla pagina.

## Loghi
- `sito/img/logo-molon.svg` è ricostruito dal logo piatto grigio del sito (599 x 139 px); `logo-molon-bianco.svg` è lo stesso tracciato in bianco per il piede. Se esiste il vettoriale originale, va usato quello.
- I loghi dei partner e il banner EIMA non sono usati: sono marchi di terzi. I partner sono scritti in testo con il loro sito.
