# Griste, home finale: "Il cassetto del campionario"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, pagina da `finale/index.html`, controllo U+2014, screenshot con `finale_scatta.mjs`). Parte dal prototipo A scelto dal giudice; in quest'ultimo passaggio la prima schermata è stata rifatta (vedi in fondo).

## L'idea

Griste fa gioielli per scarpe, non minuteria, e il suo tesoro è il campionario negli astucci di velluto: la home si apre come un cassetto del campionario. In alto il loro claim "La maison del gioiello per calzature" su due righe; sotto, su un solo ripiano segnato da un filetto, i quattro pezzi veri delle quattro collezioni. Quello scelto sta alla sua misura vera, gli altri tre piccoli accanto; sotto il pezzo scelto c'è la sua riga d'archivio (nome, collezione, posto nella collezione, lavorazione), presa dalle schede di griste.com. Si sceglie un pezzo e quello cresce nel suo scomparto: è l'unico gesto.

## Le prime due schermate

- 1440: testata con logo SVG, menu, telefono. Il titolo su due righe a 76 px nelle colonne 1-8; nelle colonne 9-12, allineati al piede del titolo, il paragrafo su che cosa fanno e per chi e il bottone blu (mailto). Sotto, il cassetto: il fiore in smalto (Natura) a 450 px nel primo scomparto; la fibbia (Moda), l'applicazione con le catene (Macchina creativa) e il bottone di strass (Natura umana) a 190 px negli altri tre, tutti appoggiati sullo stesso filetto. Sotto ogni pezzo il nome della collezione e il numero dei pezzi; sotto quello scelto "Fiore, Natura, 1 di 31, Lavorazione su metallo con smalto" e i link "Chiedete questo pezzo" (mailto con l'oggetto del pezzo) e "I 31 pezzi della collezione". Finisce a 886 px.
- 390: titolo su tre righe, il pezzo scelto a tutta colonna (342 px), la riga d'archivio e i due link, poi gli altri tre pezzi in fila con i nomi: il gesto sta tutto nei primi 844 px, con il pezzo che cambia sopra il dito. Sotto vengono il paragrafo, il bottone e il telefono (tel:). Tutto allineato a sinistra.
- Seconda schermata: "Azienda", la storia in una frase grande (1975, microlavorazioni e galvanica, gli anni Ottanta e la calzatura), Alberto e Letizia Burattin, il Gruppo Altofare, le due strade (archivi o pezzo su misura); poi quattro date su una fila: 1975, anni ’80, 2008 (fotovoltaico 49 kW), 2022 (ISO 14001:2015 Certiquality).
- Poi: "Dal disegno al prototipo" (titolo, le due foto vere del cesello e dei bagni galvanici affiancate dentro la griglia, poi due colonne: la loro frase sul processo a sinistra, l'elenco verbatim delle lavorazioni e le materie prime a destra); "Il campionario, ovvero il tesoro di Griste" (titolo su una riga, sei pezzi veri sulla stessa linea con i conteggi per tipo, ognuno è un link al campionario filtrato; poi gli astucci di velluto a sinistra, il bestiario e i conteggi per lavorazione a destra); la chiusura; il piede. Pagina alta 4781 px a 1440, 6467 a 390.

## Caratteri e colori

- Noto Serif Display 300 per titolo, titoli di sezione, frase d'azienda, anni e telefono della chiusura (mai sotto 32 px, come chiede la guida dei caratteri; mai corsivo, `font-synthesis:none`); Red Hat Text 400 e 500 per testo, nomi delle collezioni, riga d'archivio, didascalie e piede, con cifre tabellari per telefoni, posti nella collezione e conteggi. Quote misurate: Red Hat Text 86,6 %, Noto Serif Display 13,4 %.
- Perché: la serif leggera ad alto contrasto è il registro di Aquazzura (Miller leggero su fondo chiaro), il mondo dei clienti di Griste, e di Danielle Frankel per la guida dei caratteri (settore c5, gioielli e moda); il grottesco pulito e geometrico richiama FuturaStd di Pomellato e NeuzeitGro di FOPE. Niente Bodoni Moda (la scelta lusso più prevedibile) e niente Instrument Sans (lista b).
- Licenza: Google Fonts, SIL Open Font License 1.1, uso commerciale ammesso; file WOFF2 latini variabili serviti dalla pagina in `sito/fonts/`.
- Colori: avorio neutro #F4F2EE (fondo, appena caldo come l'oro dei pezzi), #EAE6DF (piede), inchiostro #15181D (15,9:1 sul fondo, 14,3:1 sul piede), grigio #5B616C per nomi non scelti, didascalie e testi del piede (5,6:1 sul fondo, 5,0:1 sul piede, AA), blu Griste #014778 del logo per bottone, link e pezzo scelto (8,6:1 e 7,8:1). Il colore pieno lo portano solo i pezzi.

## Interazione

I quattro pezzi del cassetto sono schede vere (`role=tablist`, `role=tab` con `aria-selected` e nome "Natura, 31 pezzi", pannello `role=tabpanel` con la riga d'archivio e la descrizione del pezzo per i lettori di schermo). Al clic o al tocco lo scomparto del pezzo scelto si allarga e il pezzo passa da 190 a 450 px in 0,2 s (solo dopo il primo tocco; niente animazione con "riduci movimento"); cambiano la riga d'archivio, l'oggetto della mail di "Chiedete questo pezzo" e il link alla collezione. Frecce, Home e Fine passano da un pezzo all'altro con il fuoco; Tab esce verso "Chiedete questo pezzo". Sotto i 961 px il pezzo scelto sale in alto a tutta colonna e gli altri tre stanno in fila sotto la sua riga. Provato con `_prova/script/finale_prova_schede.mjs` a 1440 con il clic e a 390 con il tocco (DPR 2): i quattro stati, le frecce, Home, Fine e Tab. Niente comparse allo scorrere, niente effetti sul cursore. Menu a bottone sotto i 960 px.

## Chiusura e piede

- Chiusura "b con foto": foto a sinistra a filo del bordo (anche a 1920), a destra la loro frase "Griste realizza sogni, quelli che i clienti conoscono e quelli che ancora non sanno di avere", sotto il telefono grande (tel:), info@ (mailto), l'indirizzo e "Apri la mappa" (Google Maps sulle coordinate di via Irpinia 55).
- Piede staccato da un filetto a tutta larghezza e da un fondo più deciso: logo SVG con la riga "Gioielli e accessori per calzature. Parte del Gruppo Altofare" (link ad altofare.com); colonne Azienda, Collezioni, Contatti (amministrazione@, PEC, Come raggiungerci: telefono e info@ sono già nella chiusura); newsletter "Collezioni e fiere" con email, bottone e casella del consenso (ha senso: collezioni stagionali, fiere, newsletter già mandate nel 2020, la privacy la cita); riga legale con ragione sociale, indirizzo, P.IVA e C.F., REA, capitale sociale (senza "i.v."), Privacy, Cookie, Codice etico e Modello 231, English. Nessuna colonna "Seguici": nessun social verificato. A 1024 la newsletter va sotto le colonne, a 768 e 390 tutto si impila nell'ordine. La newsletter non invia nulla finché non si collega a un servizio (vedi LEGGIMI).

## Foto, origine e licenza

- Pezzi del cassetto e del campionario: scontornati veri del sito di Griste (`assets/originali/file__prodotti__*`, 450x450). È la misura più grande che c'è sul server: nelle cartelle `file/prodotti/<id>/` ci sono solo `small_`, `tagliata_` e `zoom_`, tutti uguali. Mai ingranditi: il pezzo scelto è a 450 px a 1440 (420 tra 1181 e 1439, 380 tra 961 e 1180, 400 sul tablet, 342 sul telefono). Nitidezza leggera, ombra corta disegnata con PIL, WebP con trasparenza a 342 e 450 px.
- **Limite bloccante della proposta**: sugli schermi 2x e 3x il pezzo resta morbido finché Griste non manda gli originali dello studio fotografico (almeno 1800 px). Con quelli il pezzo scelto va portato a 560-600 px a 1440 ed esportato a 900 e 1350 px.
- Laboratorio: due foto vere di Griste (`photogallery-gioielli-f03`, `f04`, 640x427) con lo stesso bilanciamento (media dei canali portata allo stesso neutro caldo), affiancate dentro la griglia a 636 px, quindi mai ingrandite a 1x. Tolta la foto del CAD: monitor con un marchio e un programma generico.
- Chiusura: segnaposto Unsplash di GN Group, mani al banco orafo con un bulino, anelli e catene sul banco (`assets/esterne/unsplash-9rdoc89WxP0-gngroup-banco-orafo.jpg`, 1800x2400), Unsplash License verificata sulla pagina della foto, non usata in altre home della campagna (vedi `assets/CREDITI.md`). Tagliata sulle mani senza il viso, 4:3 a 900, 1350 e 1600 px e 1:1 a 600 e 1200 per il telefono, luce calda tenuta, neri appena aperti. In pagina "Foto indicativa": va sostituita con le mani di Griste al banco di smaltatura.

## Controlli

- Screenshot guardati a pezzi: 1440 (intera e prima schermata), 390 (intera e prima schermata), 320, 768, 1024, 1920 (in `_prova/controlli/`), i quattro stati del cassetto a 1440 e a 390 (`_prova/prova-schede/`).
- `_prova/script/finale_larghezze.mjs`: scrollWidth uguale a innerWidth a 26 larghezze da 320 a 2560 (a 360 il telefono andava fuori di 7 px: ora va a capo sotto il bottone), nessun pezzo fuori dalla finestra, titolo e testo mai sovrapposti. Link: `tel:+390498790716`, `mailto:info@griste.com` (anche con l'oggetto del pezzo), `mailto:amministrazione@griste.com`, `mailto:gristesrl@legalmail.it`, mappa `https://www.google.com/maps/search/?api=1&query=45.38008%2C11.96602`.
- U+2014: zero in pagina, NOTA, LEGGIMI, CREDITI e script.
- `segnali.sh` a 1440 (`_prova/segnali-finale/home-1440-soglie.json`): 17 soglie su 18 a posto, nessuna "da guardare" (titolo a sinistra e paragrafo a destra solo nella sezione Azienda). Resta sotto soglia l'area foto, 25,4 % contro 35 %: Griste non ha foto grandi (scontornati a 450 px, laboratorio a 640 px) e non ho riempito la pagina di repertorio. È la prima cosa da chiedere (vedi LEGGIMI, foto da rifare).
- Confronto della prima schermata con Mario Agnoletto (titolo a sinistra, pezzo a destra con legende a filetto), Marin Assemblaggi (pezzi con punti numerati e interruttore), Tre Emme (ruota con punti numerati e pallini dei colori) e Tacchificio Riviera (titolo centrato in alto, pezzo al centro, tre schede di testo sotto): qui non ci sono legende né punti; il gesto è il cassetto con tutti e quattro i pezzi veri sullo stesso ripiano, il titolo è a sinistra su due righe con il testo a destra.
- A vista: nessun gradiente, nessun corsivo d'accento, nessuna card, nessun badge, nessuna icona, nessun hover che sbiadisce.

## Cosa è cambiato in quest'ultimo passaggio

- Apertura rifatta: tolte le legende a filetto e i punti numerati (erano nomi letti dalla foto); al loro posto la riga d'archivio con i dati delle schede di Griste. Il pezzo centrato con il titolo sotto e le schede di testo è diventato il cassetto con i quattro pezzi veri; il titolo è salito in alto a sinistra con il testo e il bottone accanto.
- Testo d'apertura senza "dal 1975" (contraddiceva "negli anni Ottanta passa alla calzatura"); "dal 1975" resta nella storia e nella fila delle date. Dalla riga del piede tolti "dal 1975" e l'indirizzo, che compariva tre volte.
- "i figli di Guido" tolto: "Oggi la guidano Alberto e Letizia Burattin".
- I conti per lavorazione spiegati: "Molti uniscono più lavorazioni: 58 hanno strass, 30 smalto, 18 pietre, 3 perle".
- "Anni Ottanta" nella fila delle date diventa "Anni ’80" e non va più a capo a 1024.
- Lavorazioni e campionario: niente più paragrafi serif grandi con la metà destra vuota; titolo, immagini, poi due colonne di testo in Red Hat Text a 19 px.
- Laboratorio: due foto invece di tre, dentro la griglia, stesso bilanciamento, didascalie allineate al bordo della propria foto.
- Chiusura: la foto dei sandali (fredda, da sposa) sostituita dalle mani al banco orafo di GN Group.
- Fondo scaldato a #F4F2EE, piede #EAE6DF con filetto in testa; contrasti ricontrollati.
- Telefono: tutto allineato a sinistra; i pezzi da scegliere stanno nella prima schermata.
