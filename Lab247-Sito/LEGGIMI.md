# 247LAB, proposta di nuova homepage: LEGGIMI

È una proposta non richiesta: una sola pagina, la home.

## Cosa c'è e dove

- `sito/index.html` è la home finale, statica, senza dipendenze esterne.
- `sito/img/` contiene solo le immagini usate, in WebP qualità 85 a più larghezze.
- `sito/cataloghi/` contiene i tre cataloghi 2026 in PDF (RB, Twentyfour7, G-label), copiati da quelli pubblicati sul loro sito: si scaricano dalla sezione Tre collezioni.
- `sito/fonts/` contiene Jost e Hanken Grotesk in woff2 (SIL OFL 1.1).
- `screenshot/home/` contiene gli screenshot (1440 e 390, intera e prima schermata, chiusura e piede) e `NOTA.md`, che spiega idea, caratteri, colori e controlli.
- `_prova/script/build_finale.sh` rifà immagini, pagina e screenshot. Usa:
  - `finale_img.py` per le immagini;
  - `finale.html` come sorgente della pagina, con il logo inserito in fase di build;
  - `finale_chiusura.mjs`, `finale_misure.mjs` e `finale_test.mjs` per lo screenshot della chiusura, le misure e la prova dei gesti;
  - `finale_controlli.mjs` per i controlli finali: scorrimento da 320 a 2560, screenshot a 320, 768, 1024 e 1920, menu aperto, MINA con tastiera e tocco, collegamenti.
- `01-analisi.md` raccoglie i fatti con le fonti. `assets/CREDITI.md` dice l'origine di ogni immagine.
- I prototipi da cui nasce la pagina sono in `_prova/home/a` e `_prova/home/b`.

## Dati da confermare con l'azienda

- **Il motto in inglese come titolo**: "We don't fear the dark" con il sottotitolo italiano "La bellezza della luce nella sua forma più pura" (la frase della collezione tecnica). Va bene così o serve un titolo in italiano?
- **Ragione sociale** nella riga legale: "247LAB di Marco Bertelli, ditta individuale", con P.IVA 05375130282. Non sono in pagina:
  - il REA, perché non è stato trovato;
  - la PEC certificata@pec.247lab.it, letta solo in un estratto di ricerca.

  Il capitale sociale non si applica a una ditta individuale.
- **Indirizzo**: Via Emilia Romagna 31, oppure 31/33 come in un estratto camerale?
- **Orari**: non sono pubblicati, quindi non sono in pagina. Se ci sono, vanno nella chiusura sotto l'indirizzo.
- **"Fatte a mano in Italia" e "fatto a mano"** (RB): dove si producono le lampade? A Saonara o da terzisti? La pagina non dice "laboratorio".
- **"Dal 2021"** e "quasi due decenni" per Roberto. I progetti partono dal 2006, ai tempi di TWENTYFOUR7: quale anno di inizio vogliono dichiarare?
- **Nomi e dati dei prodotti**:
  - CIUCCIO in F066 è confermato a vista: è la stessa applique della scheda `ciuccio` e della pagina 104 del catalogo RB 2026. In pagina ci sono i dati del catalogo 2026 (1xE27 LED 6 W, 3000K, IP44, ottone naturale e vetro, alta 700 mm). La scheda del sito dice invece IP54: quale dei due è giusto?
  - La foto delle collezioni (F346, Casa P) mostra due fari in ottone su un'asta: non sappiamo il nome del modello, quindi la didascalia dice solo progetto, città, anno e fotografo. Se è un modello RB, va aggiunto il nome.
  - BOATY S (F024) viene dalla pagina dove compare la foto.
  - KYLE terra in Casa G è dedotta dalla forma.
- **G-label**: è già in vendita? Avrà una pagina sul sito nuovo?
- **MINA e lo shop**: prezzi (135 e 155 €), codici 247M.001-.003 e "Spedizione gratuita in tutta Italia" sono quelli dello shop di oggi. Lo shop resta? I link vanno alle schede attuali.
- **Committenti citati in home**: Ferragamo, 10 Corso Como, Hotel Mediterraneo, Fendi, Casadei, Tiziana Fausti, Palazzo Vendramin, H-Farm, Hotel Coast, Dolce&Gabbana, Enoteca S. Lucia, Casa G, Harry's Piccolo. Sono presi dalle loro schede di progetto: va chiesto se si possono citare in home.
- **Studi citati**: Marco Costanzi Architects, Parisotto + Formenton Architetti, Zanon Architetti Associati, MIDE architetti.
- **Newsletter**:
  - il servizio a cui collegarla;
  - chi la scrive e ogni quanto;
  - il testo dell'informativa privacy.

## Pagine del sito nuovo a cui puntano i link

Le sezioni della home restano ancore (`#collezioni`, `#mina`, `#progetti`, `#su-misura`, `#contatti`). Tutti gli altri link puntano oggi alle pagine vere del sito Wix, o ai PDF, e vanno sostituiti con le pagine del sito nuovo quando esisteranno:

| Voce | Oggi punta a | Pagina del sito nuovo |
|---|---|---|
| Collezione RB, RB decorativa | https://www.247lab.it/collezione-decorativa-1 | Collezione RB, con le famiglie Tavolo, Terra, Soffitto e parete, Parete, Soffitto, Sospensioni, Esterno, Complementi |
| Collezione Twentyfour7 | https://www.247lab.it/copia-di-nuova-pagina | Collezione Twentyfour7 |
| G-label, Catalogo G-label 2026 | `cataloghi/G-label_Catalogo_2026_ITA.pdf` (sul sito di oggi non c'è una pagina) | Collezione G-label |
| Catalogo 2026 di RB e Twentyfour7 | `cataloghi/*.pdf` | restano i PDF, nella pagina Cataloghi |
| Cataloghi, Cataloghi 2026 (testata, apertura, piede) | https://www.247lab.it/cataloghi | Cataloghi 2026, con i tre PDF |
| Tutti i progetti, Progetti (piede) | https://www.247lab.it/portfolio | Progetti, con le 41 schede |
| Chi siamo | https://www.247lab.it/about-3 | Chi siamo |
| Shop (piede) | https://www.247lab.it/category/all-products | Shop |
| Acquista nello shop (MINA) | le tre schede `product-page/mina`, `mina-marrone-brunito`, `mina-antracite` | Shop / MINA, con le tre schede |
| Privacy, informativa privacy | `/privacy` | Privacy (oggi il sito non ne ha una) |
| Cookie | `/cookie` | Cookie (oggi c'è solo il banner di Wix) |
| EN, English | `/en` | versione inglese |

I link a WhatsApp, alla mappa e ai social puntano già agli indirizzi veri.

## Newsletter: non funziona finché non si collega

Il modulo nel piede ha campo email, bottone e consenso, e controlla i dati in pagina, ma non invia niente a nessuno. Per non fingere un'iscrizione, oggi risponde "L'iscrizione apre a breve: intanto scrivici a info@247lab.it", con il link mailto. Per farlo funzionare:
1. collegarlo a un servizio (Brevo o Mailchimp) con il loro modulo incorporato o con le API;
2. attivare il doppio consenso;
3. scrivere l'informativa privacy e collegarla da "informativa privacy".

Ha senso perché ogni anno esce un catalogo nuovo, la G-label è appena uscita, lo shop vende ai privati e gli architetti aspettano i cataloghi.

## Foto da rifare dal vero, con le indicazioni di scatto

- **Roberto e Marco insieme al banco**, di sera, con una sola lampada accesa. Il muro scuro va lasciato libero a sinistra per il titolo e il banco deve essere senza libri né oggetti di altri marchi. Formato orizzontale 2:1, più una verticale 4:5. Nella F018 di oggi i libri e il televisore sono stati tolti con il taglio.
- **BOATY S accesa per l'apertura**, a una risoluzione più alta (oggi è l'originale Wix 4000x6000, ma il paralume occupa solo 1788 px di larghezza). Fondo nero, il fusto deve uscire dal bordo alto, il paralume va ripreso leggermente dal basso perché si veda l'interno acceso, con molto spazio nero sotto.
- **G-label e Twentyfour7 in luce del giorno**, come F346: un solo apparecchio su parete chiara. Oggi la sezione Tre collezioni ha una sola foto (F346) perché le foto di 1111 e dello SPOT G-6 (un render del catalogo) non reggevano accanto.
- **MINA nelle tre finiture con la stessa inquadratura vera**: le tre foto dello shop sono scattate da punti diversi. Oggi sono riportate con PIL alla stessa scala e allo stesso riquadro, e le ombre sono aperte perché il brunito si legga sul muro nero; va rifatta una serie a camera ferma, su fondo grigio medio.
- **Un macro della lavorazione dell'ottone** (taglio, brunitura) e il banco di lavoro di Saonara, se esistono.

## Licenze e permessi

- **Foto**: sono tutte dell'azienda.
  - Casa G (F288) e Casa P (F346) sono di Alessandro Cusano, come risulta dalle schede del sito: servono il permesso e il credito.
  - Delle foto di prodotto (BOATY S, MINA, CIUCCIO) e del ritratto F018 non è indicato l'autore: va chiesto chi le ha fatte e con quali diritti.
  - Nel prototipo B c'erano anche le foto di Harry's Piccolo di Roberto Pastrovicchio. Nella home finale non ci sono più, ma restano da chiarire se tornano nelle pagine Progetti.
- **Caratteri**: Jost e Hanken Grotesk, SIL Open Font License 1.1 (Google Fonts), serviti in locale. L'uso commerciale è libero.
- **Foto di repertorio**: nessuna nella home finale. Quelle in `assets/esterne/` restano solo come riserva, con le licenze in `assets/CREDITI.md`.

## Loghi

- **Logo 247LAB**: SVG ricostruito dal PNG originale 2246x455 con il tracciamento dei contorni (IoU 0,988), in `currentColor`. In pagina è in colore luce sul nero e in inchiostro sulla carta. Da chiedere all'azienda il vettoriale originale.
- **Favicon**: il pittogramma del faretto su binario, ricostruito in SVG.
- **Logo RB**: ricostruito (`assets/originali/logo-rb.svg`), non usato in home.
