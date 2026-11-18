# Scaleabotola (Scalarredo S.r.l.): proposta di nuova home

Proposta non richiesta, solo la home. Non pubblicata, azienda non contattata.

- Pagina: `sito/index.html` con `sito/img/` e `sito/fonts/` (statica, si apre con file:///). Versione "livello professionale" del 3 novembre 2026, scritta a mano, con il ritocco finale dello stesso giorno (apertura con la foto a tutta altezza e le tessere del foro gialle, misure a pastiglie, racconto della Montreal, PLUS senza foto, modulo corretto).
- Screenshot: `screenshot/home/` (home-1440, home-1440-prima-schermata, home-390, home-390-prima-schermata, chiusura-1440). Nota di progetto ed esito delle 15 regole: `screenshot/home/NOTA.md`, sezione "Livello professionale".
- Rigenerare: `sh _prova/script/build_finale.sh --immagini controlli` (immagini con `pro_img.py`, screenshot, controlli con `pro_controlli.mjs`).
- Versione di prima (24 ottobre): `_prova/versione-1-originale/` (sito, screenshot, LEGGIMI e CREDITI di allora).
- Analisi e fonti: `01-analisi.md`; scheda d'identità e d'uso: `_prova/uso/SCHEDA.md`.

## Modulo da collegare

Il modulo "Mandateci le misure o il disegno" oggi non invia niente: compone un'email (mailto) a scalarredo@scalarredo.it con l'oggetto ("Misure del foro, Nome" per le retrattili, altrimenti il tipo di richiesta) e i campi (tipo, nome, telefono, email, comune, foro, altezza, solaio, messaggio), e chi scrive allega lì foto e disegni. Con "Scala da interno" le etichette diventano "Foro nel solaio" e "Da piano a piano" e le misure arrivano comunque nell'email; con "Visita in showroom" e "Altro" i campi delle misure si nascondono davvero (prima restavano visibili e i valori si perdevano). Il bottone "Mandateci il disegno" della sezione scale da interno sceglie da solo "Scala da interno". Accanto all'invio c'è l'indirizzo cliccabile per chi usa la webmail e il mailto non apre niente. Prima di pubblicare va collegato a un servizio di invio (per esempio il modulo del loro WordPress, Contact Form 7 o WPForms, già sul sito di oggi), con:
- il caricamento di foto del foro e disegni (JPG, PDF, DWG), che con l'email si fa a mano (da webmail il mailto può non aprire nulla: è il motivo principale per collegarlo);
- l'avviso di ricezione e la riga sulla privacy (oggi iubenda);
- la promessa dei tempi di risposta, se la vogliono dare (non c'è nelle fonti, quindi non è in pagina).

## Da chiedere o confermare con l'azienda

In pagina ci sono solo dati presi dai loro siti e dalla scheda; vanno comunque verificati prima di pubblicare:
- **Prezzi** letti nel negozio il 03/11/2026 (soffitto Easy da 238 euro, PLUS da 320, parete 70x100 425, 80x130 489, chiocciola in kit da 1.290, tutti IVA esclusa) e **306 prodotti** nel negozio: cambiano, vanno riletti alla pubblicazione o collegati al negozio.
- **Prezzi di terrazzo e soppalco**: non sono nelle fonti; in pagina c'è "prezzo al telefono" (tessere dell'apertura) e "Il prezzo ve lo dà l'ufficio tecnico".
- **Prezzi con la misura**: in pagina ora "Easy 50×90 238 € + IVA", "PLUS 50×80 320 € + IVA", "70×100 425 € + IVA", "80×130 489 € + IVA" (letti nel negozio). Se vogliono il prezzo accanto a ogni misura del foro, serve il listino per misura o il collegamento al negozio.
- **Collegamenti per misura**: le pastiglie 80×120, 100×100 (soffitto) e 70×100, 80×130 (parete) portano alla scheda del negozio, perché sono le sole schede per misura che abbiamo letto; le altre misure non hanno un indirizzo nelle fonti. Il negozio non ha una categoria "a soffitto": il blocco Soffitto porta alle linee Easy e PLUS. Con il sito nuovo conviene un filtro per misura del foro.
- **Altezza 300 cm**: le tavole dicono 300 cm; in pagina c'è "Misure per un'altezza da pavimento a soffitto di 300 cm; per altezze diverse chiamate l'ufficio tecnico". Confermare se 300 è l'altezza standard o la massima, e se per 260-280 cm va la stessa scala (è il dubbio di chi ha il metro in mano).
- **Misure dei fori**: prese dalle tavole "MISURE STANDARD DISPONIBILI" di scaleabotola.com (probabile fornitore): soffitto da 45x70 a 80x100, parete da 50x80 a 80x100, terrazzo da 60x80 a 80x100, soppalco 70x100; altezza 300 cm; 140 cm a terra e 170 per aprirla; gradini del soppalco 10x35 cm. Confermare che valgono per le scale che vendono oggi (il negozio ha anche 80x120, 100x100 e la parete 80x130, che la tavola non ha).
- **Tempi**: "solitamente in 5 gg. lavorativi" dal magazzino e "dalle 2 settimane alle 6 settimane" fuori misura (condizioni di vendita); se la posa in zona Padova, Vicenza e Venezia la fanno sempre loro.
- **Portata**: 150 kg con prova a 260 kg sono scritti; la norma (UNI EN 14975 con anni diversi nei due siti, "EN 131" nella pagina PLUS) resta fuori finché non dicono quale. Se c'è un certificato in PDF, va nel piede come prova (regola 10).
- **Orario del sabato**: oggi "solo al mattino". Serve l'ora di apertura e di chiusura: la riga "Aperto ora" il sabato dice "Il sabato solo la mattina: chiamate prima di passare" e dalle 12.30 dice chiuso (ora presa dal feriale, da confermare). Se chiudono nelle feste nazionali (la pagina lo dà per chiuso) e ad agosto.
- **Email da mettere in pagina**: oggi scalarredo@scalarredo.it (dalle condizioni di vendita); in alternativa info@scaleabotola.com. Il secondo numero 049 900 48 34 è un fax? Non è in pagina.
- **CAP 35035** di Mestrino: viene da un elenco pubblico (infoisinfo), non dal loro sito; REA "CCIAA 295631": provincia (presumibilmente Padova).
- **"Da due generazioni"**: anno d'inizio della famiglia (srl dal 1997, "più di 40 anni" e "trentennale" nei testi) e nomi; se vogliono, una riga con la loro storia e una data in apertura (oggi la prova è il magazzino in 5 giorni).
- **Chi produce che cosa**: per le scale da interno la pagina dice "Un team esperto segue la produzione, la progettazione e la posa in opera" (loro frase); per le retrattili non dice "prodotte da noi" (loro: "fornitura vendita e installazione").
- **Modelli nelle schede**: confermare che `montreal-012` è una Montreal (doppia fascia da 8 mm), `scala-giorno-New-York-1` una New York a zeta, `Scala-giorno-Boston-A` una Boston a cremagliera, `scala-elicoidale-B` una loro elicoidale, e che le foto si possono pubblicare (case di clienti).

## Per arrivare al livello dei riferimenti mancano (da chiedere, non inventati)

- **Recensioni** con nome e comune: oggi non ce ne sono di pubbliche (infoisinfo "0 commenti", Google non leggibile). Chiedere il profilo Google Business, o 3-5 clienti disposti a una frase con nome e comune.
- **Lavori con un nome**: tre scale da interno posate con comune, anno e due-tre dati (tipo, legno, foro), con una foto larga.
- **Certificazioni o fornitori**: il certificato della portata, il produttore delle retrattili se si può nominare.
- **Le persone**: chi risponde all'"ufficio tecnico" (nome e ruolo), da mettere accanto al telefono.
- **Foto dell'apertura con persone o negozio** (regola 3): oggi l'apertura ha la PLUS nella botola, a tutta altezza; il livello dei riferimenti chiede la facciata, lo showroom o le persone (vedi "Foto da fare dal vero", punti 1-3).

## Foto da fare dal vero

Oggi in pagina ci sono solo foto loro (o del fornitore), mai foto di repertorio; mancano quelle che una bottega mette in apertura (persone, negozio, magazzino). Una giornata nello showroom di Mestrino, un solo fotografo e una sola luce:
1. **Facciata e insegna sulla statale 11**, di giorno, con il giallo dell'insegna se c'è: va nella scheda "Negozio e orari" e nel piede.
2. **Showroom e magazzino**: le scale esposte, le retrattili in pronta consegna sugli scaffali (prova del "fornito magazzino"), luce del pomeriggio.
3. **La persona dell'ufficio tecnico** al telefono o al banco con una tavola misure, che guarda il lavoro e non l'obiettivo (con liberatoria).
4. **La PLUS montata nello showroom**, aperta, ripresa dall'alto dentro il foro come la foto di oggi (cavalletto sopra la botola, ottica 35 mm), e la stessa chiusa: sostituisce `PLUS-pantografo.jpg` se i diritti non sono loro. Almeno 4000 px sul lato lungo.
5. **Macro del gradino in frassino** con luce radente e del pannello da 18 mm: `banner-bg2.jpg` (vecchia e morbida) è stata tolta, il racconto della PLUS oggi è solo testo e gamma; con questa foto torna un racconto foto e testo.
6. **Scale da interno posate**, inquadrate sulla scala, casa sgombra, luce naturale, almeno 3000 px, in verticale 4:5 come le schede: una per tipo (a giorno, a zeta, a cremagliera, elicoidale, chiocciola, pedata alternata, ringhiera in vetro). Le prime da chiedere: una chiocciola Londra o Parigi e un parapetto in vetro (oggi senza foto, ed è dove l'aspetto decide).
7. **Originali più grandi** di `Scala-giorno-Boston-A.jpg` (800x600) e `scala-elicoidale-B.jpg` (480x620): in pagina sono mostrate a circa 300-380 px e sugli schermi 2x si sgranano. Chiedere i file d'origine ad almeno 1200 px. La New York (`scala-giorno-New-York-1.jpg`) è stretta sulla scala e smorzata, ma la carta da parati scura resta dietro la scala: una foto nuova a parete chiara la sostituirebbe.
Formato: RAW o JPEG alla massima qualità, bianco neutro sul muro.

## Foto in pagina e diritti

- `plus-*`: `scalarredo/PLUS-pantografo.jpg` (sul loro sito, ma ha l'aria di una foto di catalogo del produttore): chiedere se si può usare.
- `montreal-*` (racconto in 3:2, la foto intera), `newyork-*`, `elicoidale-*`: foto loro di scale posate presso clienti.
- `boston-*`: `scalarredo/Scala-giorno-Boston-A.jpg`, 800x600, professionale, forse di catalogo: confermare.
- Tolta la Montreal bianca ritoccata a mano della versione 1 (oggetti di casa cancellati), che non era più una foto fedele.
- Nessuna foto di repertorio in pagina (quelle scaricate in `assets/esterne/` restano non usate, vedi `assets/CREDITI.md`).

## Licenze

- Carattere: Archivo (Google Fonts), SIL Open Font License 1.1, uso commerciale libero; servito dalla pagina in `sito/fonts/archivo-latin.woff2`.

## Logo

- In testata e nel piede: blocco giallo #FFD700 con il marchio a triangolo in SVG (tracciato dai contorni del PNG vero) e la scritta "Scalarredo scale" estratta dal PNG nel blu del logo #0075FF (`sito/img/scritta.png`). Sotto i 385 px resta il quadrato giallo con il marchio.
- Da chiedere: un vettoriale del logo e il nome del carattere della scritta (simile a un Times); se il favicon "SC" giallo su blu è voluto.

## Collegamenti

Le voci della pagina portano alle pagine vere di oggi su scalarredo.it (categorie del negozio, pagine dei tipi di scala, catalogo PDF `Cat-Retrattili-1.pdf`, condizioni di vendita, cookie policy iubenda) e al canale YouTube. Con il sito nuovo vanno rifatte puntando alle pagine nuove. Il canale ha un indirizzo col nome personale (@giorgiotiziana4735): meglio uno col nome dell'azienda.

## Dominio

scaleabotola.com (e scale-botola.it) vanno reindirizzati alle pagine delle retrattili del sito nuovo (scalarredo.it), da decidere con loro.
