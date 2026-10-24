# Impreservice: proposta di nuova home

Proposta non richiesta di nuova homepage per Impreservice S.r.l. (Grisignano di Zocco, VI). Solo la home.

- Pagina: `sito/index.html` (statica, si apre con doppio clic), immagini in `sito/img/`, caratteri in `sito/fonts/`.
- Screenshot e nota di progetto: `screenshot/home/` (`NOTA.md` spiega idea, caratteri, colori, interazione, foto e controlli).
- Rigenerare immagini e screenshot: `bash _prova/script/build_finale.sh` (usa `_prova/script/finale_img.py` e `_prova/script/scatta_finale.mjs`).
- Analisi con le fonti: `01-analisi.md`. Crediti delle foto: `assets/CREDITI.md`. Prototipi e giudizio: `_prova/home/a/`, `_prova/home/b/`.

## Dati da confermare con l'azienda

Ogni fatto in pagina viene da `01-analisi.md`. Questi sono in pagina ma sono letture o fonti vecchie:

1. **"Due bussole, una per concio"** e "il perno unisce un concio al vicino quando l'anello si chiude": lettura del disegno e del nome "conci attrezzati". Confermare dove stanno le bussole e come si monta il perno.
2. **Rivestimento in materiale composito** contro corrosione e abrasione: dal comunicato tunnelbuilder.com del 2013. Vale ancora per le versioni di oggi?
3. **Smart HD (480 kN) e Hybrid (boccola L140 passo 5 mm)**: dalla notizia tunnelbuilder.it del 23/09/2022. Sono in produzione?
4. **Linea ponti e viadotti** (giunti Sapjoint, membrana Sapeflex, posa): fonte del 2013. È ancora attiva? Fanno anche la posa?
5. **Il disegno in apertura è Easy Click Smart** (il file si chiama `asm-smart`) e la bocca della bussola destra è presa dal disegno della bussola singola, portata in prospettiva: confermare che sia lo stesso pezzo.
6. **Colore del pezzo**: nei loro render (`34/35/36-Senza-nome`) Easy Click è nero; in pagina è nel grigio caldo del disegno CAD, trattato come un pezzo in luce. Con la foto vera si userà il colore vero.
7. **42 cantieri** (24 Italia, 8 Europa, 10 Mondo, dall'elenco Referenze): anni, opere e fornitura vera; quali si possono nominare. Le 14 schede di oggi dicono tutte "Diga, 2020".
8. **Brevetto IT 1391815** (deposito 29/10/2008) in contitolarità con Innotek Srl: come vogliono citarlo; altri brevetti.
9. **"Siamo in ventidue"** (piede): dai registri (atoka), 22 dipendenti.
10. **Capitale sociale 10.000 €**: interamente versato? PEC da aggiungere alla riga legale (non trovata).
11. **carlo@impreservicesrl.it** in chiusura: va bene mostrarlo? Il cellulare +39 335 5618004 (notizia 2022) non è in pagina.
12. Non usati in pagina perché incerti: "dal 1998" (la srl è del 2000), "24 paesi" (l'elenco ne nomina 11), aeroporti e strade, fatturato.

## Foto da rifare dal vero

Le foto di cantiere in pagina sono segnaposto di repertorio (Pexels e Unsplash, licenza libera). Per il sito vero:

1. **Easy Click in studio (la più importante)**: fondo grigio chiaro senza giunture, luce morbida da sinistra con un pannello di rimando a destra, ottica lunga (90-100 mm), il pezzo di tre quarti come nel disegno CAD (asse a circa 25 gradi), due scatti dallo stesso cavalletto senza spostare nulla: aperto (bussole a qualche centimetro dal perno) e agganciato. File a 4000 px, in alternativa un render ad alta risoluzione esportato dal loro CAD con lo sfondo trasparente. Bastano quattro PNG trasparenti (bussola, perno, bussola, assieme) per sostituire i livelli `ec-*` senza toccare la pagina.
2. **Un concio attrezzato in stabilimento**: la faccia del concio con le bussole annegate in vista, luce di giorno, di taglio per leggere il calcestruzzo.
3. **Un anello appena posato in un cantiere che si può nominare**, con il permesso del committente: dal centro della galleria, in prospettiva, giunti puliti; sostituisce la galleria di Mishin.
4. **Un giunto Sapjoint posato su un impalcato**, se la linea ponti è attiva; sostituisce il viadotto.
5. **Persone di Impreservice** al lavoro (montaggio, controllo, magazzino) per la chiusura, al posto dello scudo della fresa.

## Licenze

- **Geologica** (Monokrom), Google Fonts, SIL Open Font License 1.1: uso commerciale libero, file serviti dalla pagina in `sito/fonts/`.
- **Foto di repertorio**: Max Mishin (Pexels 11424325), Sururi Ballıdağ (Pexels 16227437), Kewal Nagda (Pexels 27808651), licenza Pexels; Evangelos Mpikakis (Unsplash CPI7JAIVaDU), Unsplash License. Pagine e autori in `assets/CREDITI.md`. Attribuzione non obbligatoria; nessuna è generata dall'IA.
- **Disegni Easy Click e logo**: dell'azienda, presi dal sito di oggi.
- Le altre immagini del sito di oggi (foto stampa dei progetti, Beni Haroun con la firma del fotografo, render Alstom, catture di altri siti) non sono usate: i diritti vanno chiariti.

## Loghi

- In pagina c'è il simbolo blu (`logo-impreservice-icona-blu-1000.png` del sito di oggi), ritagliato ed esportato in PNG a 160 e 240 px; il nome "Impreservice" accanto è composto in Geologica, perché un logo con la scritta non l'ho trovato.
- Da chiedere: il **logo vettoriale originale** (SVG, AI o PDF) e, se esiste, la versione con la scritta. Il simbolo è geometrico e si può ricostruire in SVG, ma solo confrontandolo con l'originale.

## Pagine del sito nuovo (link di menu e piede)

Nella proposta puntano alle sezioni della home. Nel sito vero: **Easy Click** (Smart, Medium, Magnum, Smart HD, Hybrid), **Ponti e viadotti** (Sapjoint, Sapeflex), **Referenze** (i 42 cantieri), **Azienda e brevetti**, **Fiere e notizie**, **Contatti**, **Segnalazioni** (portale esterno già attivo, https://segnalazioni.impreservicesrl.it), **Privacy**, **Cookie**. Social: solo YouTube (@Impreservicesrl).

## Newsletter

Non prevista: vendono a imprese di scavo e prefabbricatori, hanno due notizie in dieci anni e nessun catalogo; il blocco newsletter di oggi non sembra collegato a niente. Al suo posto la pagina "Fiere e notizie".
