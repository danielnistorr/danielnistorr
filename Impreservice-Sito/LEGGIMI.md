# Impreservice: proposta di nuova home

Proposta non richiesta di nuova homepage per Impreservice S.r.l. (Grisignano di Zocco, VI). Solo la home.

- Pagina: `sito/index.html` (statica, si apre con doppio clic), immagini in `sito/img/`, caratteri in `sito/fonts/`.
- Screenshot e nota di progetto: `screenshot/home/` (`NOTA.md` spiega idea, caratteri, colori, interazione, foto e controlli).
- Rigenerare immagini e screenshot: `bash _prova/script/build_finale.sh` (usa `_prova/script/finale_img.py` per le foto, `_prova/script/sezione_img.py` per l'apertura e `_prova/script/scatta_finale.mjs`). Prova dei gesti, delle larghezze e dei collegamenti: `node _prova/script/prova_gesti.mjs file://$PWD/sito/index.html`.
- Analisi con le fonti: `01-analisi.md`. Crediti delle foto: `assets/CREDITI.md`. Prototipi e giudizio: `_prova/home/a/`, `_prova/home/b/`.

## Dati da confermare con l'azienda

Ogni fatto in pagina viene da `01-analisi.md`. Questi sono in pagina ma sono letture o fonti vecchie:

1. **"Due bussole, una per concio"** e "il perno unisce un concio al vicino quando l'anello si chiude": lettura del disegno e del nome "conci attrezzati". Confermare dove stanno le bussole e come si monta il perno.
2. **Rivestimento in materiale composito** contro corrosione e abrasione: dal comunicato tunnelbuilder.com del 2013. Vale ancora per le versioni di oggi?
3. **Smart HD (480 kN) e Hybrid (boccola L140 passo 5 mm)**: dalla notizia tunnelbuilder.it del 23/09/2022. Sono in produzione?
4. **Linea ponti e viadotti** (giunti Sapjoint, membrana Sapeflex, posa): fonte del 2013. È ancora attiva? Fanno anche la posa?
5. **La sezione dell'apertura è una ricostruzione**: Easy Click Smart (profili misurati sui disegni `asm-smart`, `perno-smart`, `bussola-smart`) dentro due conci tagliati. Da confermare con un loro disegno di posa: a che profondità sta la bussola nel concio e con quale verso (in pagina il collo, cioè la parte stretta, guarda il giunto e il fondo chiuso sta nel calcestruzzo, come nell'assieme CAD); la forma della sede del perno vicino al giunto (in pagina una sede conica che segue il rigonfiamento del perno); se il perno arriva già avvitato in un concio, come mostra lo stato "Aperto"; in quale giunto lavora (longitudinale o circonferenziale). La didascalia in pagina dice "ricostruito dai disegni tecnici".
6. **Colore del pezzo**: in pagina è nero satinato, come nei loro render (`34/35/36-Senza-nome`). Confermare materiale e finitura.
7. **42 cantieri** (24 Italia, 8 Europa, 10 Mondo, dall'elenco Referenze): anni, opere e fornitura vera; quali si possono nominare. Le 14 schede di oggi dicono tutte "Diga, 2020".
8. **Brevetto IT 1391815** (deposito 29/10/2008) in contitolarità con Innotek Srl: come vogliono citarlo; altri brevetti.
9. **"Siamo in ventidue"** (piede): dai registri (atoka), 22 dipendenti.
10. **Capitale sociale 10.000 €**: interamente versato? PEC da aggiungere alla riga legale (non trovata).
11. **Il titolo della chiusura** "Conci attrezzati con tecnologia Easy Click" è il titolo del loro video YouTube; "Consegne in tutto il mondo" e "tempi secondo quantità" vengono dalla pagina Prodotti ("Copriamo consegne in tutto il mondo", "Secondo quantità").
12. **carlo@impreservicesrl.it** in chiusura: va bene mostrarlo? Il cellulare +39 335 5618004 (notizia 2022) non è in pagina.
13. Non usati in pagina perché incerti: "dal 1998" (la srl è del 2000), "24 paesi" (l'elenco ne nomina 11), aeroporti e strade, fatturato.

## Foto da rifare dal vero

Le foto di cantiere in pagina sono segnaposto di repertorio (Pexels e Unsplash, licenza libera). Per il sito vero:

1. **L'apertura (la più importante)**: la strada più semplice è un render dal loro CAD. Due conci veri tagliati in sezione lungo l'asse del connettore (o un modello del concio nel CAD con il materiale calcestruzzo), Easy Click Smart nero annegato, vista ortogonale di fianco, luce morbida unica dall'alto a sinistra. Servono tre PNG trasparenti alti almeno 880 px, con il giunto chiuso a 3,0 volte l'altezza dal bordo sinistro del primo: concio sinistro con bussola e perno avvitato (largo 3,62 volte l'altezza), concio destro con la sua sede (largo 3 volte), bussola destra da sola sullo stesso riquadro del concio destro. Sostituiscono `sez-sx`, `sez-dx`, `sez-dx-b` senza toccare la pagina. In alternativa, la foto in studio: un concio vero segato a metà in stabilimento, con il connettore in vista, due scatti dallo stesso cavalletto (giunto aperto e chiuso).
2. **Un concio attrezzato in stabilimento**: la faccia del concio con le bussole annegate in vista, luce di giorno, di taglio per leggere il calcestruzzo.
3. **Un anello appena posato in un cantiere che si può nominare**, con il permesso del committente: dal centro della galleria, in prospettiva, giunti puliti; sostituisce la galleria di Mishin.
4. **Un giunto Sapjoint posato su un impalcato**, se la linea ponti è attiva; sostituisce il viadotto.
5. **Persone di Impreservice** al lavoro (montaggio, controllo, magazzino) per la chiusura, al posto dello scudo della fresa.

## Licenze

- **Geologica** (Monokrom), Google Fonts, SIL Open Font License 1.1: uso commerciale libero, file serviti dalla pagina in `sito/fonts/`.
- **Foto di repertorio**: Max Mishin (Pexels 11424325), Kewal Nagda (Pexels 27808651), Артем Дворецкий (Pexels 20818874, il calcestruzzo dei conci in apertura), licenza Pexels; Evangelos Mpikakis (Unsplash CPI7JAIVaDU), Unsplash License. Pagine e autori in `assets/CREDITI.md`. Attribuzione non obbligatoria; nessuna è generata dall'IA.
- **Disegni Easy Click e logo**: dell'azienda, presi dal sito di oggi. Il connettore in apertura è reso da uno script a partire dai loro disegni (nessuna immagine generata dall'IA).
- Le altre immagini del sito di oggi (foto stampa dei progetti, Beni Haroun con la firma del fotografo, render Alstom, catture di altri siti) non sono usate: i diritti vanno chiariti.

## Loghi

- In pagina c'è il simbolo blu (`logo-impreservice-icona-blu-1000.png` del sito di oggi), ritagliato ed esportato in PNG a 160 e 240 px; il nome "Impreservice" accanto è composto in Geologica, perché un logo con la scritta non l'ho trovato.
- Da chiedere: il **logo vettoriale originale** (SVG, AI o PDF) e, se esiste, la versione con la scritta. Il simbolo è geometrico e si può ricostruire in SVG, ma solo confrontandolo con l'originale.

## Pagine del sito nuovo (link di menu e piede)

Il menu porta alle sezioni della home (Easy Click, Ponti e viadotti, Referenze, Contatti); i link che rimandavano alla sezione in cui si trovavano ora puntano alle pagine che il sito nuovo avrà. Nella proposta queste pagine non esistono ancora:

| Pagina | File | Da dove ci si arriva |
|---|---|---|
| Easy Click (Smart, Medium, Magnum, Smart HD e Hybrid, con le ancore `#smart`, `#medium`, `#magnum`, `#smart-hd-hybrid`) | `easy-click.html` | piede, colonna Prodotti |
| Ponti e viadotti (Sapjoint, Sapeflex) | `ponti-e-viadotti.html` | sezione ponti ("La linea ponti"), piede |
| Referenze (i 42 cantieri) | `referenze.html` | sezione referenze ("Tutti i 42 cantieri"), piede |
| Azienda e brevetti | `azienda.html` | menu "Azienda", piede |
| Fiere e notizie | `notizie.html` | piede |
| Contatti | `contatti.html` | piede |
| Privacy, Cookie | `privacy.html`, `cookie.html` | riga legale del piede |
| Segnalazioni D.Lgs. 24/2023 | portale esterno già attivo, https://segnalazioni.impreservicesrl.it | riga legale del piede |

Social: solo YouTube (@Impreservicesrl).

## Newsletter

Non prevista: vendono a imprese di scavo e prefabbricatori, hanno due notizie in dieci anni e nessun catalogo; il blocco newsletter di oggi non sembra collegato a niente. Al suo posto la pagina "Fiere e notizie".
