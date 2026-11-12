# 02. Concorrenti e riferimenti di design

Ricerca del 6 ottobre 2026. Ogni sito è stato aperto dal vivo con Playwright (Chromium attraverso il proxy) a 1440 e a 390 px e fotografato a pagina intera; i siti che mostrano i contenuti solo durante lo scorrimento sono stati fotografati anche a finestre successive e poi cuciti. Visitati 6 concorrenti (più 4 pagine interne) e 17 siti di riferimento (più 2 pagine interne): ne restano 6 premium e 1 funzionale. Cinque siti non si sono lasciati fotografare, del tutto o in parte: sono indicati come tali, senza giudizi.

File: screenshot in `_prova/ricerca/` (`c*` concorrenti, `r*` riferimenti, `p-*` pagine interne, `c0-dibi-*` il sito attuale per confronto), pezzi già tagliati in `_prova/ricerca/pezzi/`, ritagli dei gesti in `_prova/ricerca/ritagli/`, campione delle tre accoppiate in `_prova/ricerca/campioni/accoppiate-1440.png` e `accoppiate-390.png` (sorgente `accoppiate.html`, con foto e testi veri di Di Bi). Script in `_prova/script/`: `foto.cjs` (screenshot, caratteri e colori letti dal browser), `link.cjs`, `cuci.py`, `ritagli.py`, `contrasto.py` (rapporti WCAG).

**Chi è Di Bi, per scegliere i riferimenti** (solo dal sito attuale). Azienda di Cassola (Via Grande 89) nata "oltre trent'anni fa" dai fratelli Bizzotto (anno esatto [DA CONFERMARE]), nel "distretto orafo" vicentino-bassanese. Produce catene in oro e in argento: le catene base ("rolo, spiga e grumetta") e le "Fantasie", nelle carature 8, 9, 10, 14, 18, 21 e 22 kt e in "lega gialla, bianca e rosè", più la linea Tessuto, "il fiore all'occhiello della produzione". Sei fasi di lavorazione nominate nella pagina Azienda: fusione, laminazione e trafilatura; produzione a macchina; saldatura; diamantatura; finitura; galvanica ("placcatura eseguita in azienda"). Membro del Responsible Jewellery Council: nell'immagine della pagina Certificazioni si leggono "Certified Member COP 0000 6883" e "Chain of Custody C0000 6884", con tre PDF (rendicontazione, politica della filiera, politica per i diritti umani). Il catalogo si chiede per email o con un modulo: vende ad aziende, non al pubblico.

Il materiale è il punto forte: foto prodotto professionali e coerenti (catene su carta chiara, stessa luce, 1500-2000 px, fondo misurato #F4F0EF e #E8E4E1), cinque foto di lavorazione in bianco e nero (fusione, macchina per catene, fili, mola, mani con la pinza; 1500x1500 e 2364x2362), lo stabilimento in bianco e nero (3543x2230), il logo a 2075x815 (lettere grigie #70767A, disco oro #C59910). Quindi i riferimenti giusti sono produttori di catene e di gioielli in oro e la filiera dei metalli preziosi, non le maison di moda; delle maison si guarda solo come raccontano la lavorazione.

## 1. Concorrenti

| # | Concorrente | Dove | Cosa fa (dal loro sito) | Cosa fa meglio di Di Bi oggi | Cosa fa peggio | Screenshot |
|---|---|---|---|---|---|---|
| 1 | [Karizia](https://www.karizia.it/) | Via Perosi 18, Cassola: lo stesso comune | "catene in argento e oro realizzate a macchina per il settore della gioielleria", fondata nel 1987; "oltre 8.000 modelli" | numeri in home (fatturato, articoli in portafoglio, dipendenti, certificazioni); fiere con i loghi (HKTDC, JCK Las Vegas, Vicenzaoro); pagina "Richiedi accesso al catalogo" con campi azienda, città, nazione; fondo pagina con PEC e P.IVA; relazione di sostenibilità | i numeri sono contatori animati: a 1440 il nostro scatto ferma "+98" e "63", a 390 "+100" e "65"; nel nostro scatto, sotto il menu, l'apertura resta una fascia bianca vuota; testi grigi #777A7E giustificati; titoli prodotto con i superlativi dell'elenco vietato; foto di riunione e di una squadra di pallavolo come "valori" | `c1-karizia-1440/390.png`, `p-karizia-prodotti/catalogo-1440.png`, ritaglio `21` |
| 2 | [Alessi Domenico](https://www.alessidomenico.com/) | Bassano del Grappa ([scheda RJC](https://www.responsiblejewellery.com/member/alessi-domenico-spa/)) | "Italian Chains Since 1946"; gioielli e catene in oro e argento; area "Business (B2B)" | quattro fasce foto a tutta larghezza; una macro vera di catene piatte in oro e una foto di macchina con la catena in lavorazione; fondo pagina ordinato in sei colonne (Gioielli, Catene, Alessi World, Academy, Gruppo, Legal) con voci come Certificazioni, Chain Magazine, Investitori | la home apre con una modella e lo slogan "Emozioni Senza Tempo": parla al pubblico prima che al cliente d'azienda; in home non ci sono né catalogo né contatti; titoli in graziato The Seasons; a 390 l'icona dell'accessibilità copre la parola "Catene" | `c2-alessidomenico-*`, ritaglio `20` |
| 3 | [Filk](https://www.filk.it/) | Via dell'Industria 8, Mussolente (VI) | "Fabbrica Italiana Lavorazione Ketten", catene in oro | notizie con la data e le fiere già annunciate (Vicenzaoro 15-19 gennaio 2027, HKTDC 4-8 marzo 2027, pubblicate a settembre 2026); modulo con "Request catalog"; capitale sociale e P.IVA in vista | la home è solo uno slider a schermo intero con la facciata della fabbrica e un titolo in Old Standard TT maiuscolo; nessuna catena in home; a 390 lo stesso slider | `c3-filk-1440/390.png` |
| 4 | [Asolo Gold](https://www.asologold.com/) | San Zenone degli Ezzelini (TV) | "progetta, realizza e commercializza catene in oro e platino"; "oltre 50 anni"; UNI EN ISO 14001:2015; membro RJC | foto prodotto curate e riconoscibili (catene appese a un vetrocemento, a un flute, dentro un bicchiere d'acqua); certificazioni scritte in fondo pagina | titolo in graziato corsivo dorato ("L'oro, tra storia e futuro."), cioè il cliché bocciato; nel nostro scatto lunghi vuoti bianchi tra le sezioni e un'immagine rotta | solo `pezzi/c4-asologold-1440-*.jpg` e ritaglio `23`: lo scatto è riuscito una volta, poi il sito ha smesso di rispondere attraverso la nostra rete (connessione interrotta); testo verificato con un secondo accesso |
| 5 | [Bassano Collection](https://www.bassanocollection.it/) | Bassano del Grappa | gioielli e catene in argento 925; "over 1,200 Silver Chain designs", "over 30 years" | "Download our catalogues": il catalogo si scarica senza chiederlo; famiglie elencate per nome (Basic Chains, Hollow, Oxidized Bracelets...) | non verificabile a vista: a 390 il sito si è caricato senza fogli di stile (`c5-bassanocollection-390.png`, inutilizzabile), a 1440 non ha risposto; contenuti letti solo come testo | nessuno valido |
| 6 | [UnoAErre](https://www.unoaerre.it/) | Arezzo | "Made in Italy since 1926" (dal logo); oggi un negozio online di gioielli con prezzi | categorie con foto prodotto su grigio chiaro uniforme e nome sotto; fotografia di prodotto coerente | è un negozio al dettaglio (spedizioni, carrello, recensioni): un altro mestiere; Cormorant e Jost; nel nostro scatto il blocco video resta nero | `c6-unoaerre-1440/390.png` |

Per confronto, il sito di Di Bi oggi (`c0-dibi-1440/390.png`, ritaglio `22`): intestazione senza logo, slogan corsivo dorato in maiuscolo con un superlativo dell'elenco vietato, riquadri con bordo oro, carattere Palanquin.

**Cosa fanno i migliori:**
- dicono dove sono e cosa fanno in una riga, con i numeri (Karizia, Asolo Gold, Bassano Collection);
- mostrano le fiere con le date (Filk, Karizia): per un'azienda che vende ai grossisti è la notizia che conta;
- rendono il catalogo facile da chiedere o da scaricare (Karizia, Filk, Bassano Collection);
- hanno almeno una foto vera di lavorazione (Alessi Domenico, la macchina con la catena).

**Cosa non fa nessuno (lo spazio per Di Bi):**
1. **la lavorazione per fasi, con foto vere.** Nessun concorrente elenca le fasi. Di Bi le nomina già (sei) e ha cinque foto in bianco e nero di fusione, macchina, fili, mola e mani;
2. **carature e leghe scritte come un dato.** Nessuna home le dice; Di Bi pubblica 8, 9, 10, 14, 18, 21 e 22 kt in tre leghe;
3. **la certificazione con i numeri.** Karizia e Asolo Gold scrivono "certificazioni" o "membro RJC"; Di Bi può mostrare COP 0000 6883 e Chain of Custody C0000 6884 con i suoi tre documenti (validità da verificare sul registro RJC [DA CONFERMARE]);
4. **una fotografia di prodotto tutta dello stesso set.** I concorrenti mescolano campagne con modelle, foto d'archivio e prodotto; le foto di Di Bi hanno la stessa carta e la stessa luce, quindi possono reggere da sole il sito.

**Posizionamento proposto** (solo fatti del sito attuale): "Catene in oro e in argento, base e fantasia, dalla fusione alla galvanica. A Cassola, nel distretto orafo di Bassano." L'anno di fondazione va chiesto: il sito dice "oltre trent'anni fa" in un testo del 2017-2018, quindi non si scrive "da oltre 30 anni" (contatore che invecchia) ma "dal [anno DA CONFERMARE]". Contro Karizia (stesso comune, più grande) non si gareggia sui numeri ma su fasi, leghe e Tessuto; contro Alessi Domenico (stessa zona, campagne con modelle) si parla al compratore d'azienda.

**Copy da evitare** (visto nei concorrenti e nel sito attuale): i superlativi dell'elenco PAROLE_VIETATE di `build.py`, presenti nei titoli di Karizia e nello slogan di Di Bi; "Emozioni senza tempo", "Made in Italy" usato come aggettivo, i valori in parole astratte (Rispetto, Impegno, Focus); i contatori di anni.

**Caratteri dei concorrenti** (da non usare, per distinguersi): Karizia Poppins e caratteri di sistema; Alessi Domenico The Seasons e Brother 1816; Filk Old Standard TT; Asolo Gold un graziato corsivo (carattere non rilevato); UnoAErre Cormorant e Jost; Di Bi oggi Palanquin.

## 2. Riferimenti premium

Tratti comuni ai riferimenti tenuti: il metallo fotografato da vicino come oggetto, su un fondo piatto (grigio, bianco o nero) e quasi mai con testo sopra; titoli in un bastoni leggero, spesso maiuscolo e largo (FOPE, Buccellati) o in un grottesco pulito (Legor, CMSA); il colore oro lo porta il prodotto, l'interfaccia resta in nero, bianco e grigio; la lavorazione raccontata per nome, fase per fase. Il corsivo graziato compare solo in Buccellati (citazioni) e in Wellendorff (scartato): è il cliché da non riprendere.

### 2.1 FOPE: [fope.com](https://www.fope.com/en/)
Orafi di Vicenza dal 1929: catene e maglie in oro, la maglia "Novecento" e il sistema brevettato Flex'it ("microscopic 18-carat gold springs"). Stesso distretto e stesso oggetto di Di Bi, ed è il sito più alto della zona. Caratteri letti dal browser: NeuzeitGro 300 maiuscolo (81 px, spaziatura 3,24 px) per i titoli e le etichette, Suisse Neue (un graziato dritto e largo) per i titoli interni e il testo della pagina Brand. Fondi #CCCECC, #CBCCD0 e #F1F3F0.
- **Gesto da riprendere:** (1) il gioiello come oggetto su un grigio piatto, grande, con il nome piccolo in maiuscolo in un angolo e niente altro (`02`); (2) nella pagina Brand, etichetta minuscola in maiuscolo ("HISTORY", "TECHNOLOGY"), titolo breve e una sola colonna stretta di testo, poi un dittico di macro della maglia a tutta larghezza, senza scritte (`03`, `05`); (3) "Hands, machines": la tecnologia raccontata con una sola foto di macchina e mani (`04`); (4) nella pagina di categoria, griglia a 4 colonne di celle grigie unite da filetti sottili, con lo stesso modello in oro giallo, rosa e bianco uno accanto all'altro (`19`), e titolo a sinistra con una riga di testo a destra (`19b`).
- **Da evitare:** campagne con modelle (Di Bi non ne ha e non servono a chi compra catene a peso); il titolo maiuscolo bianco sopra un affresco, illeggibile nella pagina Brand; il riquadro "Confirm location" che copre la pagina; testo a 10-12 px.
- **Da telefono** (`r1-fope-390.png`): i nomi delle collezioni restano sopra la foto e finiscono sul gioiello; da noi il nome va sotto la foto.
- **Ritagli:** `01-fope-striscia-prodotto-e-indossato.jpg`, `02-fope-prodotto-come-oggetto-su-grigio.jpg`, `03-fope-etichetta-titolo-colonna.jpg`, `04-fope-mani-e-macchine.jpg`, `05-fope-dittico-macro-della-maglia.jpg`, `19-fope-griglia-tre-ori.jpg`, `19b-fope-titolo-a-sinistra-testo-a-destra.jpg`.

### 2.2 Buccellati, pagina Craftsmanship: [buccellati.com](https://www.buccellati.com/en_us/maison-craftmanship/)
Orafi milanesi; la pagina sulla lavorazione chiama ogni tecnica col suo nome (Segrinato, Telato, Ornato, Modellato; nell'indice Engraving, Enchaining, Tulle, Lace, Twisted thread). Novecento Wide (bastoni largo) per titoli e menu, Cormorant per il testo. Nero #0F0F0F.
- **Gesto da riprendere:** (1) "Main techniques": cinque quadrati di macro, piccoli, col nome della tecnica sotto in maiuscolo spaziato (`06`); (2) la fascia nera con i nomi delle tecniche in grande, uno per riga, separati da filetti sottili (`07`). Per Di Bi è la forma giusta per le sei fasi: nomi grandi su nero, filetto, numero piccolo, e accanto le foto in bianco e nero.
- **Da evitare:** le citazioni in Cormorant corsivo, i paragrafi lunghi in graziato, il pannello cookie a tutta altezza (a 390 copre metà pagina, `r14-buccellati-craft-390.png`).
- **Ritagli:** `06-buccellati-indice-delle-tecniche.jpg`, `07-buccellati-tecniche-in-elenco-su-nero.jpg`.

### 2.3 Legor Group: [legor.com](https://legor.com/)
Leghe di metalli preziosi, polveri e "soluzioni galvaniche" per la gioielleria, a Bressanvido (VI): la filiera di Di Bi, nella stessa provincia, e un'azienda che vende ad aziende come lei. Caratteri gopher e Montserrat; link in maiuscolo color oro bruno #A8833B preceduti da una lineetta corta; fascia nera #000000.
- **Gesto da riprendere:** (1) "Saremo presenti a": le fiere in righe su nero, data a sinistra, nome grande al centro, padiglione e stand a destra, freccia, filetti tra le righe (`08`); (2) la riga delle certificazioni con il marchio RJC e il numero del certificato scritto sotto (`09`); (3) le quotazioni dei metalli come riga di testo, che a 390 diventa un elenco verticale leggibile (`10`, `r5-legor-390.png`).
- **Da evitare:** cornici sfalsate attorno alle foto, foglie decorative, il riquadro "You can find our offices" che si apre da solo, la fascia crema #F5F1E9; il link oro #A8833B dà 3,5:1 su bianco, sotto il minimo. Le quotazioni in tempo reale servono a chi vende metallo: per Di Bi richiederebbero una fonte di dati e non sono richieste dal suo lavoro, quindi non si fanno. A 390 la parola "Fashion&Decorative" esce dalla pagina e un paragrafo diventa minuscolo.
- **Ritagli:** `08-legor-fiere-in-righe.jpg`, `09-legor-certificazioni-rjc-coc.jpg`, `10-legor-quotazioni-metalli.jpg`.

### 2.4 CMSA Cendres+Métaux: [cmsa.ch](https://www.cmsa.ch/)
Componenti e leghe in metalli preziosi per orologeria e lusso, medicale e industria, "Swiss Made", "140+ years": un produttore che vende ad aziende, in metallo prezioso, come Di Bi. Euclid Circular A, fondo #F2F2F2, rosso solo nei dettagli.
- **Gesto da riprendere:** (1) "Our services": il processo come sequenza orizzontale con numeri grandi 01, 02, 03, il nome della fase in neretto piccolo e due righe di spiegazione (`11`); (2) l'apertura divisa, testo breve a sinistra su grigio e a destra una macro del metallo tenuto con i guanti (`12`).
- **Da evitare:** le forme arrotondate e la "L" rossa, i pulsanti con bordo rosso, le tessere bianche con i numeri, le notizie con immagini d'archivio ("News Message"); a 390 nel nostro scatto il logo non si carica e l'icona dell'accessibilità copre "Contact Our Experts".
- **Ritagli:** `11-cmsa-processo-numerato.jpg`, `12-cmsa-apertura-testo-e-macro.jpg`.

### 2.5 Niessing: [niessing.com](https://niessing.com/en-DE)
Manifattura di gioielli a Vreden dal 1873, venduta nei suoi negozi e da gioiellieri partner. TheSans, fondo bianco, testo #555559.
- **Gesto da riprendere:** (1) "Made by hand / Tradition and innovation under one roof / Design is developed through dialogue": tre foto verticali di lavorazione (grani d'oro versati nel crogiolo, la superficie di un lingotto, un anello sotto la luce) con un titolo leggero e poche righe sotto ciascuna, e la frase "from melting the bars of gold or platinum, to finishing the jewelry... under one roof" (`14`). Di Bi scrive la stessa cosa ("placcatura eseguita in azienda", "produzione controllata in ogni fase") e ha le foto; (2) la macro dell'anello che esce dai bordi della pagina (`15`).
- **Da evitare:** il titolo in maiuscolo solo contorno ("ARE YOU READY FOR THE ORIGINAL?"), i caroselli di prodotti con prezzo, le categorie con il nome bianco sopra i volti, il pannello cookie a metà pagina.
- **Ritagli:** `14-niessing-tre-fasi-sotto-un-tetto.jpg`, `15-niessing-macro-oltre-il-bordo.jpg`.

### 2.6 Kriskadecor: [kriskadecor.com](https://kriskadecor.com/en/)
Catene di alluminio per l'architettura e l'arredo: "Linking Ideas Since 1926", "The Original Patent 1932". È un produttore di catene, in un altro mercato. Hoves, fondi giallo e grigio.
- **Gesto da riprendere:** una sola maglia isolata, ingrandita e messa al centro come un segno, con accanto la data del brevetto (`13`). Per Di Bi: una maglia (rolo, spiga, grumetta, Tessuto) fotografata in macro come apertura della pagina Catene o come separatore, solo con una foto nuova a risoluzione piena [foto da fare]; la frase sui "numerosi brevetti internazionali" del sito attuale resta [DA CONFERMARE] finché non ci sono numero e anno.
- **Da evitare:** il giallo pieno, i pulsanti a pillola, il video d'apertura (nel nostro scatto "Player error"), le schede colorate dei designer, la maglia che copre il titolo a 390.
- **Ritaglio:** `13-kriskadecor-maglia-come-segno.jpg`.

### 2.7 Riferimento funzionale (contenuto giusto, aspetto da non riprendere)

| Riferimento | Cosa fa | Cosa si prende | Cosa no |
|---|---|---|---|
| [Italpreziosi](https://www.italpreziosi.it/) (affinazione e metalli preziosi, Arezzo) | i semilavorati (barre, grani, lamine) scontornati su bianco con nome e due righe; "Una posizione centrale nella catena del valore" come elenco numerato 01-05 diviso da filetti; la purezza scritta sul prodotto | le famiglie di catene come oggetti scontornati con nome e riga tecnica; l'elenco numerato a filetti per Azienda e Lavorazione | Sora con titoli in Minion corsivo, schede arrotondate, pulsanti a pillola, barra delle quotazioni che scorre. Ritagli `16`, `17`, `18` |

### 2.8 Aperti e scartati

- [Wellendorff](https://www.wellendorff.com/de/): cordoni in oro (la "Wellendorff-Kordel"), quindi stesso oggetto; ma fondo marrone, crema, graziato con titoli corsivi e campagne con modelle: proprio il cliché bocciato, anche in un'azienda vera. I contenuti compaiono solo scorrendo (scatto a finestre in `r9-wellendorff-1440-cucito.png`).
- [Marco Bicego](https://marcobicego.com/): negozio al dettaglio, Didot e Avenir, tre icone in fila ("Spedizione express", "Confezione regalo", "Servizio concierge").
- [Officina Bernardi](https://www.officinabernardi.com/): vicini di Cassola (Borso del Grappa), ma negozio con prezzi e immagini da campagna su fondi turchesi.
- [Pomellato](https://www.pomellato.com/it_it): la catena Iconica fotografata bene, ma è una maison al dettaglio; nel nostro scatto il carattere dei titoli non si carica e la pagina sborda di 2 px.
- [Metalor](https://metalor.com/) e [C.Hafner](https://www.c-hafner.de/): filiera giusta (affinazione), siti datati: numeri in cerchi blu, riquadri verdi, ritratto d'archivio.
- [Gay Frères](https://www.gayfreres.ch/) (bracciali in metallo per orologeria): sito "under construction".
- Non fotografabili: [Rolex](https://www.rolex.com/) e [PAMP](https://www.pamp.com/) rispondono "Access Denied" al browser automatico; [Valcambi](https://www.valcambi.com/) non ha risposto attraverso la nostra rete. Non usati.

## 3. Cosa si riprende

| Gesto | Da | Dove nel sito di Di Bi | Con quale materiale vero | Condizione |
|---|---|---|---|---|
| Apertura divisa: testo su bianco a sinistra, foto prodotto a destra fino al bordo, il fondo della fascia uguale alla carta della foto | FOPE (oggetto su fondo piatto), CMSA (testo e macro) | Home | `AU-BASE.jpg` 2000x1500 o `Gruppo04` 1500x1124 | colonna foto al massimo 1000 px CSS con AU-BASE, 750 con le foto da 1500 se si vuole il 2x; ritaglio per breakpoint, mai ingrandire; niente testo sulla foto |
| Etichetta piccola, titolo breve, una colonna stretta di testo | FOPE Brand | Azienda (fratelli Bizzotto, il distretto, lo statuto del 1339, la corporazione di Bassano del 1776) | testi della pagina Azienda, corretti | i fatti storici restano quelli scritti dall'azienda |
| Dittico di due foto a tutta larghezza, senza scritte, didascalia sotto | FOPE Brand | Tessuto, Collezioni | `FOTO-EMOZIONALI` 1417x946 (Tessuto), `Gruppo06_B` 1500x1125 (argento), `Gruppo_01c` (catene in più colorazioni) | due colonne di 720 px a 1440: sotto la misura nativa |
| Le sei fasi in grande, una per riga tra filetti, su nero, con le foto in bianco e nero accanto | Buccellati (tecniche), CMSA (numeri 01-06), Niessing (tre foto) | Lavorazione, e un estratto in Home | i sei nomi della pagina Azienda; `1craft1` (fusione), `3craft1` (macchina per catene), `4craft1` (fili), `61` (mola), `4dibispa` (mani con la pinza) | abbinamento foto e fase [DA CONFERMARE]; saldatura e galvanica non hanno foto: brief nel LEGGIMI |
| Famiglie di catene come piccoli quadrati di macro con il nome sotto | Buccellati (indice tecniche), Italpreziosi (semilavorati con nome) | Catene: rolo, spiga, grumetta, Fantasie, Tessuto | ritagli dalle foto da 1500 px | ogni quadrato mostrato a metà della sua misura ritagliata o meno; dove manca la macro, foto da fare |
| Stesso modello nelle tre leghe, affiancato | FOPE (griglia tre ori) | Oro: "lega gialla, bianca e rosè" | oggi solo `Gruppo_01c` mostra più colorazioni insieme | servizio fotografico: stessa catena in tre leghe [foto da fare] |
| Carature scritte come dato tecnico: 8 · 9 · 10 · 14 · 18 · 21 · 22 kt | FOPE ("18-carat gold springs"), Italpreziosi (purezza dichiarata) | Home, Oro | testo della pagina Collezioni | solo le carature pubblicate; per l'argento la lega va chiesta [DA CONFERMARE] |
| Riga certificazioni con marchio e numero | Legor | Certificazioni e fondo pagina | COP 0000 6883, CoC C0000 6884, i tre PDF già pubblicati | validità e data dei certificati sul registro RJC [DA CONFERMARE] |
| Fiere in righe: data, fiera, stand, freccia | Legor, Filk (notizie datate) | al posto della pagina News vuota | nessuno: le fiere di Di Bi non sono pubblicate | la sezione esiste solo se il cliente dà date e stand [DA CONFERMARE] |
| Catalogo su richiesta con campi per l'azienda | Karizia, Filk ("Request catalog") | Catalogo (Contact Form 7) | email dibi@dibispa.com già usata dal modulo attuale | nessun download finché il cliente non fornisce un PDF |
| Una maglia isolata e ingrandita come segno | Kriskadecor | apertura di Catene o separatore | nessuna foto adatta oggi | solo con macro nuova; mai ingrandire le foto da 1500 px |

Non importato: modelle e campagne, caroselli e slider, video d'apertura, contatori animati (Karizia), corsivo graziato dorato (Asolo Gold, Wellendorff), forme arrotondate (CMSA), cornici sfalsate e foglie (Legor), quotazioni in tempo reale, finestre "scegli il paese" e widget che coprono il testo, tre icone in fila.

## 4. Accoppiate

Campione con foto e testi veri di Di Bi: `_prova/ricerca/campioni/accoppiate-1440.png` e `accoppiate-390.png` (nessuno sbordamento a 390). Contrasti calcolati con la formula WCAG (`_prova/script/contrasto.py`). Tutti i caratteri sono su Google Fonts e si caricano da Elementor come famiglie normali (nessun asse di larghezza da gestire a mano).

### A. "Trafila": Lexend Exa + Lexend (consigliata)

- **Caratteri:** Lexend Exa 300 maiuscolo per i titoli (48-52 px a 1440, 30 px a 390, spaziatura 0,01 em, al massimo cinque o sei parole); Lexend Exa 400 a 13-14 px maiuscolo per carature, nomi delle fasi e numeri. Lexend 300 a 18 px per i testi d'apertura, 400 a 16-17 px per il testo corrente, 400 a 12 px maiuscolo spaziato 0,1 em per menu ed etichette. Lexend Exa è la versione larga di Lexend: un solo disegno, due larghezze, come Barlow e Barlow Condensed per Benvegnù ma al contrario.
- **Palette:** bianco #FFFFFF; carta #F3EFEC (la carta delle foto di Di Bi, misurata #F4F0EF e #F0ECEB: è un grigio caldo quasi neutro, non un crema giallo) per le fasce con foto prodotto; inchiostro #18181A; grigio #5F6468 per il testo secondario (il grigio del logo #70767A va bene solo su bianco e da 18 px in su); oro Dibi #C59910 solo per filetti, disco del logo e linee di fase, mai per il testo su chiaro; oro scuro #7E6108 per i link.

| Testo | Fondo | Contrasto |
|---|---|---|
| inchiostro #18181A | bianco | 17,7:1 |
| inchiostro #18181A | carta #F3EFEC | 15,5:1 |
| grigio #5F6468 | bianco | 6,0:1 |
| grigio #5F6468 | carta #F3EFEC | 5,2:1 |
| grigio logo #70767A | bianco | 4,6:1 (solo testo grande) |
| oro scuro #7E6108 | bianco | 5,8:1 |
| oro scuro #7E6108 | carta #F3EFEC | 5,1:1 |
| bianco | oro scuro #7E6108 | 5,8:1 (pulsante) |
| oro Dibi #C59910 | bianco | 2,7:1: solo elementi grafici |

- **Da dove viene:** il logotipo DIBI, largo, sottile e grigio; il NeuzeitGro 300 maiuscolo di FOPE e il Novecento Wide di Buccellati, cioè i due siti più alti visti per l'oro; il fondo piatto dietro il prodotto di FOPE e CMSA; il link dorato di Legor, scurito perché il suo #A8833B non passa (3,5:1).
- **Perché per Di Bi:** il titolo largo e sottile riprende il marchio che il cliente ha già; la carta delle sue foto diventa il fondo, così le catene non hanno bordi; l'oro resta quello del logo e compare come linea, come la catena è una linea. Nessun concorrente usa questi caratteri.
- **Rischio:** Lexend Exa sotto i 13 px diventa troppo larga e in testo lungo stanca: solo titoli brevi ed etichette. Lexend 400 in grande ha un tono scolastico: per i testi d'apertura si usa il 300.

### B. "Punzone": Hedvig Letters Serif + Mona Sans

- **Caratteri:** Hedvig Letters Serif (graziato dritto a basso contrasto, con ottica automatica) per i titoli 32-40 px e per i testi lunghi della pagina Azienda; Mona Sans 500 a 11-12 px maiuscolo spaziato 0,12-0,16 em per etichette e menu, 400 per didascalie, 600 per i link.
- **Palette:** bianco, inchiostro #1C1C1C, grigio #5F6468, oro scuro #7E6108 per i link, carta #F3EFEC solo dietro le foto prodotto.

| Testo | Fondo | Contrasto |
|---|---|---|
| inchiostro #1C1C1C | bianco | 17,0:1 |
| grigio #5F6468 | bianco | 6,0:1 |
| oro scuro #7E6108 | bianco | 5,8:1 |
| inchiostro #18181A | carta #F3EFEC | 15,5:1 |

- **Da dove viene:** la pagina Brand di FOPE, l'unico riferimento alto che usa un graziato: Suisse Neue dritto, su bianco, con etichette in bastoni maiuscolo e una colonna stretta; il dittico di macro senza testo.
- **Perché:** dà il tono della pagina di storia (statuto del 1339, corporazione di Bassano del 1776) e del Tessuto.
- **Rischio:** tutti i concorrenti della zona usano un graziato (Alessi Domenico, Asolo Gold, Filk, UnoAErre): Di Bi sembrerebbe uno di loro. Con la carta e un corsivo diventerebbe la versione "Atelier" già bocciata. Si può usare solo dritto, su bianco, mai corsivo, e solo per titoli e testi lunghi.

### C. "Fusione": Chivo + Chivo Mono, fondo nero

- **Caratteri:** Chivo 300 maiuscolo a 34 px (22 px a 390) per i nomi delle fasi su nero; Chivo 400 per il testo; Chivo Mono 400-500 a 12-13 px per numeri di fase, date delle fiere, numeri dei certificati (COP 0000 6883), carature.
- **Palette:** nero #111111, filetto #2B2B2B (solo linee), bianco, grigio chiaro #A9ADB0, oro Dibi #C59910 per numeri ed etichette su nero; carta #F3EFEC per le fasce prodotto alternate.

| Testo | Fondo | Contrasto |
|---|---|---|
| bianco | nero #111111 | 18,9:1 |
| grigio chiaro #A9ADB0 | nero #111111 | 8,4:1 |
| oro Dibi #C59910 | nero #111111 | 7,1:1 |
| nero #111111 | oro Dibi #C59910 | 7,1:1 (pulsante) |
| grigio logo #70767A | nero #111111 | 4,1:1: il logo su nero va schiarito |

- **Da dove viene:** la fascia nera delle tecniche di Buccellati (#0F0F0F) e quella delle fiere di Legor; le foto di lavorazione in bianco e nero di Di Bi; il monospaziato viene dai numeri dei certificati RJC e dalle date delle fiere, che sono dati da leggere in colonna.
- **Perché:** la lavorazione è il fatto che i concorrenti non mostrano, e su nero le foto della fusione e della mola rendono di più.
- **Rischio:** un sito tutto nero è il cliché della gioielleria scura e mette in difficoltà le foto prodotto su carta chiara; serve una versione chiara del logo (le lettere #70767A su nero danno 4,1:1). Va usato per una sola fascia per pagina.

### Raccomandazione

**A come base.** È l'unica che nasce dal marchio che Di Bi ha già (lettere larghe e sottili, disco oro) e dalla carta delle sue foto, e la tipografia larga e leggera è quella dei due riferimenti più alti per l'oro (FOPE, Buccellati). Da C si innesta una sola fascia nera per Lavorazione e certificazioni, con i nomi delle fasi in Lexend Exa invece che in Chivo (una sola famiglia in tutto il sito); da B si prendono il dittico senza testo e la colonna stretta, scritti in Lexend 300. La scelta definitiva si fa in 2.3, con il punteggio sui criteri del metodo.

**Perché niente graziato e niente crema:** nel settore il graziato è la scelta dei concorrenti locali e di Wellendorff (marrone, crema, corsivo), cioè proprio quello che l'utente ha bocciato; i riferimenti che vendono metallo e lavorazione (FOPE nei titoli, Buccellati nei titoli, Legor, CMSA, Kriskadecor) usano un bastoni. Il fondo chiaro di Di Bi non è un crema scelto per gusto: è la carta su cui l'azienda ha già fotografato le sue catene.
