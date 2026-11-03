# Nardi S.r.l. Unipersonale: proposta di nuova homepage

Proposta non richiesta di una nuova home per narditalia.com. Solo la home; nessun contatto con l'azienda, niente pubblicato.

- **Pagina**: `sito/index.html` (si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/` (con `OFL.txt`).
- **Screenshot e nota**: `screenshot/home/`; la `NOTA.md` ha la sezione "Livello professionale" con l'esito delle 15 regole.
- **Rigenerare tutto**: `bash _prova/script/build_finale.sh` (dati dei prodotti, immagini, dati in pagina, screenshot, prove d'uso, controlli). Con `scarica_pagine=1` riscarica le 96 pagine prodotto da narditalia.com.
- **Versione precedente**: copia intatta di `sito/` e `screenshot/home/` in `_prova/versione-1-originale/`.
- **Fonti**: `01-analisi.md`, `_prova/uso/SCHEDA.md`; dati dei 96 prodotti in `_prova/dati-prodotti.json` (Store API di WooCommerce, pagine prodotto e libreria media di narditalia.com, letti il 3/11/2026).

## Che cosa fa la home

- **Chi ha la scatola in mano** (telefono): campo "Cosa devi fare?" e sei lavori con la scatola vera (crepe, fissare, fughe, muri, caminetti, gesso). Ogni risultato dice a cosa serve, acqua, tempi, spessore, uso interno o esterno, codici e confezioni, con i link alla scheda tecnica e alla scheda di sicurezza in PDF (176 PDF, tutti controllati: rispondono 200).
- **Il negoziante** (computer): telefono ordini grande con lo stato aperto o chiuso, "Codici e confezioni" (elenco dei 96 prodotti e 193 codici, filtrabile per linea e da stampare o salvare in PDF), "Diventa rivenditore" e "Chiedi il listino" (modulo).
- **Il professionista**: blocco Artelinea con le schede, la dichiarazione di prestazione dell'E180 in PDF, il telefono per quantità e consegna, la sede nel navigatore.

## Il modulo va collegato

Il modulo "Richiesta o ordine" oggi **compone un'email** (mailto a info@narditalia.com con oggetto e tutti i campi) e non invia nulla da solo. Nel sito vero va collegato a un servizio di invio (per esempio Contact Form 7 sul WordPress nuovo, o un servizio di moduli con antispam), con:
- la ricevuta automatica a chi scrive e l'indirizzo che riceve (info@ o un indirizzo ordini);
- il campo **allegato** per l'ordine o l'elenco in file (con un mailto non si può: oggi la pagina chiede di allegarlo all'email);
- l'informativa privacy aggiornata (il modulo di oggi cita ancora il D.Lgs 196/2003).

## Da chiedere all'azienda (prima di qualsiasi uso)

1. **Il numero in grande**: in pagina c'è 049 879 0626, quello del sito di oggi (fax 049 830 4579). Schede tecniche (2016), scheda di sicurezza (2019) e Reteimprese danno tel 049 879 9070 e il 049 879 0626 come fax. Quale va negli ordini?
2. **Vendita ai negozi**: la pagina dice "li vendiamo ai negozi in tutta Italia" e "se il tuo negozio non ce l'ha, può ordinarla a noi". Confermare: si vende direttamente ai negozi o anche tramite grossisti e catene? Ci sono un ordine minimo, condizioni o zone di consegna? Si vende ai privati in sede o si ritira in sede?
3. **Elenco dei rivenditori**: i cinque negozi in pagina (Polato Ferramenta, Emporium La Cometa, Santilli Vivai, Ferramenta Stella, Brico 5 Stelle) sono presi dai loro siti, dove vendono Briko Line; non sappiamo se comprano da Nardi o da un grossista. Serve l'elenco vero (per provincia) e il permesso di nominarli.
4. **Catalogo e listino**: esiste un catalogo in PDF? In pagina l'elenco dei codici si stampa dal sito; il listino è indicato come "su richiesta".
5. **Prove che mancano** (regole 10 e 11): recensioni di clienti (nessuna trovata: Google Maps non raggiungibile, Reteimprese senza recensioni), clienti o catene con il nome, lavori fatti con i prodotti Nardi (restauri, cornici, cantieri) con luogo e anno, fiere.
6. **Produzione**: la pagina dice "li produciamo". Quali dei 96 articoli produce Nardi e quali rivende (latta GESCOL e solfato di calcio sono di terzi; schiuma poliuretanica, rete, secchielli)?
7. **Orari**: lo stato aperto o chiuso usa lun-ven 8-12 e 14-18, i festivi nazionali e Pasquetta. Mancano il patrono di Saonara e le chiusure estive o di Natale.
8. **Schede**: le schede tecniche sono del 2016-2019 e la dichiarazione di prestazione dell'E180 del 2017: sono ancora valide? Quali prodotti sono fuori produzione? Errori da correggere nelle schede del sito: la colla per piastrelle grigia riporta "Acqua d'impasto: Bianca 28%", la polvere ceramica terracotta usa la foto della bianca, la malta grigia dice "Colore Bianco"; tre prodotti non hanno codici (Malta risanante idrorepellente, Artecoll AV 104, Secchielli anonimi bianchi).
9. **Fotovoltaico**: in pagina c'è solo "Dal 2011 un impianto fotovoltaico dà energia alla produzione"; "riducendo a zero le emissioni" resta fuori finché non lo confermano.
10. **La sede in foto** (`TESTATA6`): è la sede di Via S. Antonio 24/a (si vede il civico 24)? Si può pubblicare il magazzino (`IMG_4232`)?
11. Titolare attuale (Leonardo Nardi secondo Reteimprese?), PEC, social veri (oggi nessuno), logo vettoriale.
12. **Sito compromesso**: 2809 articoli di spam e 717 categorie spam sono ancora pubblici su narditalia.com. Vanno tolti prima della migrazione, con i redirect 301 delle schede prodotto.

## Link della proposta

In questa proposta i PDF e le pagine prodotto puntano a narditalia.com di oggi (sono le uniche che esistono). Nel sito vero vanno ripuntati alle nuove schede prodotto; i PDF possono restare dove sono. Privacy e Cookie puntano alle pagine di oggi.

## Foto da fare dal vero

Nella home ci sono solo foto e rendering di Nardi. Per arrivare al livello dei riferimenti serve mezza giornata con un fotografo, una sola luce e lo stesso trattamento per tutte:
- **La produzione e le persone** (oggi non c'è nessuna foto): le macchine che riempiono le scatole, le mani che chiudono un cartone da 12, chi prepara un bancale; luce naturale o luce di reparto morbida, orizzontali 16:9, almeno 3000 px di lato lungo. È la foto che manca di più: la regola 3 chiede persone o laboratorio.
- **Lo scaffale** (oggi `IMG_2282`, foto da telefono 1600x900 con i cartellini dei prezzi sfocati): rifarlo in un negozio cliente con il loro permesso, frontale, senza prezzi e senza prodotti di altri marchi, 16:9.
- **Il magazzino** (oggi `IMG_4232`): frontale sui bancali Briko Line, senza cellophane lucido, con una persona al lavoro.
- **La sede**: la facciata con le fasce lilla e il pilastro NARDI, dal basso, con un cielo pulito e senza il piazzale in primo piano, 16:9 di almeno 2400 px (oggi la sorgente è alta 700 px).
- **Le scatole**: una per lavoro (stucco, cemento rapido, stucco per fughe, malta pronta, malta refrattaria, alabastrino), stessa luce e stesso angolo, fondo neutro, quadrate di almeno 1200 px, per le miniature dei lavori e delle linee; meglio ancora i file di stampa delle confezioni.

## Licenze

- **Caratteri**: Encode Sans (The Encode Project Authors), Google Fonts, SIL Open Font License 1.1: uso commerciale libero; file serviti dal sito in `sito/fonts/`, licenza in `sito/fonts/OFL.txt`.
- **Foto e rendering**: tutti di Nardi, dalla libreria media di narditalia.com (`assets/originali/`); da usare con il loro permesso. Nessuna foto di repertorio, nessuna immagine generata dall'IA, nessun disegno. Dettagli in `assets/CREDITI.md`.

## Loghi

Il logo esiste solo raster: in pagina c'è `logo-nardi-bianco-500x139.png` del sito tagliato sul disegno (436x100) e con la maschera ricolorata in verde #276E59 (testata) e in bianco (piede). Da chiedere il logo vettoriale (AI, EPS, PDF o SVG).
