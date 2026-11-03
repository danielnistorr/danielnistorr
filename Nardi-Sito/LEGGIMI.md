# Nardi S.r.l. Unipersonale: proposta di nuova homepage

Proposta non richiesta di una nuova home per narditalia.com. Solo la home; nessun contatto con l'azienda, niente pubblicato.

- **Pagina**: `sito/index.html` (si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/` (con `OFL.txt`), catalogo codici `sito/catalogo-codici-nardi.pdf`.
- **Screenshot e nota**: `screenshot/home/`; la `NOTA.md` ha la sezione "Livello professionale" con l'esito delle 15 regole.
- **Rigenerare tutto**: `bash _prova/script/build_finale.sh` (dati dei prodotti, immagini, dati in pagina, catalogo PDF, screenshot, prove d'uso, controlli). Con `scarica_pagine=1` riscarica le 96 pagine prodotto da narditalia.com.
- **Versione precedente**: copia intatta di `sito/` e `screenshot/home/` in `_prova/versione-1-originale/`.
- **Fonti**: `01-analisi.md`, `_prova/uso/SCHEDA.md`; dati dei 96 prodotti in `_prova/dati-prodotti.json` (Store API di WooCommerce, pagine prodotto e libreria media di narditalia.com, letti il 3/11/2026).

## Che cosa fa la home

- **Chi ha la scatola in mano** (telefono): campo "Cosa devi fare?" e sei lavori con la scatola vera (crepe, fissare, fughe, muri, caminetti, gesso). Ogni risultato dice a cosa serve, acqua, tempi, spessore, uso interno o esterno, codici e confezioni, con i link alla scheda tecnica e alla scheda di sicurezza in PDF (176 PDF, tutti controllati: rispondono 200).
- **Il negoziante** (computer): telefono ordini grande con lo stato aperto o chiuso, "Codici, confezioni e catalogo in PDF" (elenco dei 96 prodotti e 193 codici, filtrabile per linea, e il catalogo `sito/catalogo-codici-nardi.pdf` di 5 pagine A4 fatto dalla stessa tabella con `_prova/script/pro_catalogo.mjs`), "Diventa rivenditore" e "Chiedi il listino" (modulo).
- **Chi riconosce la scatola**: dodici scatole Briko Line da 1 kg in "Prodotti", ognuna apre la sua scheda.
- **Il professionista**: blocco Artelinea con le schede, la dichiarazione di prestazione dell'E180 in PDF, il telefono per quantità e consegna, la sede nel navigatore.

## Il modulo va collegato

Il modulo "Richiesta o ordine" oggi **compone un'email** (mailto a info@narditalia.com con oggetto e tutti i campi) e non invia nulla da solo; dopo il clic mostra sempre il testo pronto con "Copia il testo", per chi usa la webmail o non ha un programma di posta. Nel sito vero va collegato a un servizio di invio (per esempio Contact Form 7 sul WordPress nuovo, o un servizio di moduli con antispam), con:
- la ricevuta automatica a chi scrive e l'indirizzo che riceve (info@ o un indirizzo ordini);
- il campo **allegato** per l'ordine o l'elenco in file (con un mailto non si può: oggi la pagina chiede di allegarlo all'email);
- l'informativa privacy aggiornata (il modulo di oggi cita ancora il D.Lgs 196/2003);
- una conferma in pagina ("Richiesta ricevuta, ti richiamiamo entro ...") con i tempi di risposta che Nardi vuole promettere.

## Da chiedere all'azienda (prima di qualsiasi uso)

1. **Il numero in grande**: in pagina c'è 049 879 0626, quello del sito di oggi (fax 049 830 4579). Schede tecniche (2016), scheda di sicurezza (2019) e Reteimprese danno tel 049 879 9070 e il 049 879 0626 come fax. Quale va negli ordini?
2. **Vendita ai negozi**: la pagina dice "li vendiamo ai negozi in tutta Italia" e "se il tuo negozio non ce l'ha, può ordinarla a noi". Confermare: si vende direttamente ai negozi o anche tramite grossisti e catene? Servono, per tre righe nella sezione Per i negozi: l'ordine minimo, i tempi e il modo di consegna (corriere, franco, zone), se il bancale può essere misto e a chi si rivolge chi è fuori Veneto. Si vende ai privati in sede o si ritira in sede?
3. **Elenco dei rivenditori**: i cinque negozi in pagina (Polato Ferramenta, Emporium La Cometa, Santilli Vivai, Ferramenta Stella, Brico 5 Stelle) sono presi dai loro siti, dove vendono Briko Line; non sappiamo se comprano da Nardi o da un grossista. Serve l'elenco vero (per provincia) e il permesso di nominarli.
4. **Catalogo e listino**: in pagina c'è un catalogo codici in PDF fatto da noi con i codici e le confezioni del sito (aggiornato al 3/11/2026). Se Nardi ha un catalogo suo, va messo al suo posto; altrimenti va riletto e approvato. Il listino è indicato come "su richiesta". Mancano le confezioni dei due mordenti e di due codici della polvere ceramica (4312050, 4313050): in pagina "confezione: chiedere al 049 879 0626"; gli ossidi hanno "500 g x 6 pz" come nel vecchio sito.
5. **Prove che mancano** (regole 10 e 11): recensioni di clienti (nessuna trovata: Google Maps non raggiungibile, Reteimprese senza recensioni), clienti o catene con il nome, lavori fatti con i prodotti Nardi (restauri, cornici, cantieri) con luogo e anno, fiere. Quando arrivano, vanno dopo "Prodotti" come tre schede di lavoro con una foto larga almeno 640 px, luogo, anno, prodotto usato e quantità; fino ad allora in pagina non c'è nessun segnaposto.
6. **Produzione**: la pagina dice "li produciamo". Quali dei 96 articoli produce Nardi e quali rivende (latta GESCOL e solfato di calcio sono di terzi; schiuma poliuretanica, rete, secchielli)?
7. **Orari**: lo stato aperto o chiuso usa lun-ven 8-12 e 14-18, i festivi nazionali e Pasquetta. Mancano il patrono di Saonara e le chiusure aziendali (ferie di agosto, 24 e 31 dicembre, ponti): lo script ha già l'elenco `CHIUSURE` (vuoto), da riempire una volta l'anno con le date che dà Nardi; in quei giorni la pagina dirà "Chiuso per ferie: riapre ...".
8. **Schede**: nei risultati ogni prodotto ha le stesse quattro righe (acqua, tempi, spessore, uso); dove la scheda del sito non dà il dato c'è "vedi scheda tecnica". Servono da Nardi, in parole semplici, almeno per le scatole Briko Line: acqua per 1 kg, spessore massimo, quando è asciutto o pedonabile (stucco per fughe), larghezza delle fughe, temperatura e tempo prima di accendere il fuoco (malta refrattaria). Le schede tecniche sono del 2016-2019 e la dichiarazione di prestazione dell'E180 del 2017: sono ancora valide? Quali prodotti sono fuori produzione? Errori da correggere nelle schede del sito: la colla per piastrelle grigia riporta "Acqua d'impasto: Bianca 28%", la polvere ceramica terracotta usa la foto della bianca, la malta grigia dice "Colore Bianco"; tre prodotti non hanno codici (Malta risanante idrorepellente, Artecoll AV 104, Secchielli anonimi bianchi).
9. **Fotovoltaico**: in pagina c'è solo "Dal 2011 un impianto fotovoltaico dà energia alla produzione"; "riducendo a zero le emissioni" resta fuori finché non lo confermano.
10. **La sede in foto** (`TESTATA6`): è la sede di Via S. Antonio 24/a (si vede il civico 24)? Si può pubblicare il magazzino (`IMG_4232`), che ora è la foto dell'apertura? È il loro magazzino o quello di un cliente?
11. Titolare attuale (Leonardo Nardi secondo Reteimprese?), PEC, social veri (oggi nessuno), logo vettoriale.
12. **Sito compromesso**: 2809 articoli di spam e 717 categorie spam sono ancora pubblici su narditalia.com. Vanno tolti prima della migrazione, con i redirect 301 delle schede prodotto.
13. **Made in Italy**: in pagina "Scritto sulle confezioni Briko Line"; l'abbiamo letto su un'etichetta (ossido di ferro rosso). Confermare che compare su tutte.

## Link della proposta

In questa proposta i PDF e le pagine prodotto puntano a narditalia.com di oggi (sono le uniche che esistono). Nel sito vero vanno ripuntati alle nuove schede prodotto; i PDF possono restare dove sono. Privacy e Cookie puntano alle pagine di oggi.

## Foto da fare dal vero

Nella home ci sono solo foto e rendering di Nardi: le tre foto hanno lo stesso trattamento (bianco neutro, arancio delle scaffalature attenuato, stessa curva) e sono tutte in 4:3; i rendering delle confezioni sono su bianco pieno, senza riflesso, tutti alla stessa altezza (`_prova/script/pro_rendering.py`). La luce dei tre scatti resta diversa. Per arrivare al livello dei riferimenti serve mezza giornata con un fotografo, una sola luce e lo stesso trattamento per tutte:
- **La produzione e le persone** (oggi non c'è nessuna foto): le macchine che riempiono le scatole, le mani che chiudono un cartone da 12, chi prepara un bancale; luce naturale o luce di reparto morbida, orizzontali 16:9, almeno 3000 px di lato lungo. È la foto che manca di più: la regola 3 chiede persone o laboratorio.
- **Lo scaffale** (oggi `IMG_2282`, foto da telefono 1600x900 con i cartellini dei prezzi sfocati, in "Dove si comprano"): rifarlo in un negozio cliente con il loro permesso, frontale, senza prezzi e senza prodotti di altri marchi, 4:3.
- **Il magazzino** (oggi `IMG_4232`, in apertura a metà pagina): frontale sui bancali Briko Line, senza cellophane lucido, con una persona al lavoro, 4:3 di almeno 3000 px di lato lungo, con luce più calda e meno grigia di oggi.
- **La sede**: la facciata con le fasce lilla e il pilastro NARDI, dal basso, con un cielo pulito e senza il piazzale in primo piano, 4:3 di almeno 2400 px (oggi la sorgente è alta 700 px e il taglio è largo 747: in pagina è mostrata al massimo a 533 px).
- **Le scatole** (oggi i rendering del sito ripuliti; il cemento grigio Artelinea non ha un rendering, solo una foto da studio su grigio, ed è senza miniatura): una per lavoro (stucco, cemento rapido, stucco per fughe, malta pronta, malta refrattaria, alabastrino), stessa luce e stesso angolo, fondo neutro, quadrate di almeno 1200 px, per le miniature dei lavori e delle linee; meglio ancora i file di stampa delle confezioni.

## Licenze

- **Caratteri**: Encode Sans (The Encode Project Authors), Google Fonts, SIL Open Font License 1.1: uso commerciale libero; file serviti dal sito in `sito/fonts/`, licenza in `sito/fonts/OFL.txt`.
- **Foto e rendering**: tutti di Nardi, dalla libreria media di narditalia.com (`assets/originali/`); da usare con il loro permesso. Nessuna foto di repertorio, nessuna immagine generata dall'IA, nessun disegno. Dettagli in `assets/CREDITI.md`.

## Loghi

Il logo esiste solo raster: in pagina c'è `logo-nardi-bianco-500x139.png` del sito tagliato sul disegno (436x100) e con la maschera ricolorata in verde #276E59 (testata) e in bianco (piede). Da chiedere il logo vettoriale (AI, EPS, PDF o SVG).
