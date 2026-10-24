# Griste S.r.l., proposta di nuova homepage

Proposta non richiesta di una nuova home per griste.com (solo la home). Nulla è stato pubblicato, inviato o comunicato all'azienda.

## Dove sono le cose

- `sito/index.html`: la home finale, statica (si apre con file:///). `sito/img/` solo le immagini usate, in più larghezze; `sito/fonts/` i due caratteri serviti dalla pagina.
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, e `NOTA.md` (idea, schermate, caratteri, colori, interazione, foto, controlli).
- `_prova/script/build_finale.sh`: rifà immagini (`finale_img.py`), pagina (da `finale/index.html`), controllo U+2014 e screenshot (`finale_scatta.mjs`, anche 320, 768, 1024, 1920 in `_prova/controlli/`). `finale_prova_schede.mjs` prova il cassetto delle collezioni con clic, tocco e tastiera; `finale_larghezze.mjs` controlla lo scorrimento orizzontale da 320 a 2560 px ed elenca i link tel, mailto e mappa.
- `01-analisi.md`: fatti con le fonti; `assets/CREDITI.md`: origine e licenza di ogni immagine; `_prova/home/a` e `b`: i due prototipi giudicati (la finale parte da A).

## Dati da confermare con Griste prima di pubblicare

- La riga d'archivio dei quattro pezzi in apertura viene dalle schede pubblicate su griste.com: nome ("fiore", "fibbia", "applicazione", "bottone"), collezione, lavorazione. Il "posto nella collezione" (Natura 1 di 31, Moda 3 di 21, Macchina creativa 25 di 26, Natura umana 6 di 21) è l'ordine in cui il sito di oggi mostra le schede, non un codice di catalogo: chiedere se Griste ha un codice articolo da mostrare al suo posto, e la misura vera di ogni pezzo in mm da aggiungere alla riga.
- Le descrizioni dei pezzi per i lettori di schermo (testo alternativo) sono scritte da me guardando la foto ("smalto bianco e verde", "telaio e ardiglione in metallo dorato"): da far rileggere a Griste.
- Se i quattro pezzi scelti sono ancora in produzione e rappresentano le collezioni di oggi; le 99 schede pubblicate sono del 2020 e il lookbook visibile è "SPRING SUMMER 2017": esiste una collezione corrente? I conteggi in pagina (31, 21, 26, 21; 33 applicazioni, 20 bottoni, 12 placche, 11 fibbie, 3 puntali, 2 talloni; 58 strass, 30 smalto, 18 pietre, 3 perle) sono contati sulle schede pubblicate.
- La frase sul Gruppo Altofare ("riunisce aziende italiane di accessori per il lusso") è una parafrasi di altofare.com; la data di ingresso nel gruppo; se in piede serve la dicitura "soggetta a direzione e coordinamento" (art. 2497-bis c.c.) e con quale ragione sociale.
- Civico (55, 55/55 o 55/57) e CAP (35020 sul sito, 35029 sul certificato ISO). In pagina: via Irpinia 55, 35020.
- Capitale sociale € 20.800,00 (Atoka scrive "21.0 K €") e se è interamente versato: in pagina è senza "i.v." finché non si conferma.
- Che Alberto e Letizia Burattin guidino ancora l'azienda dentro il gruppo (Alberto è "Managing Director Accessori Calzature" di Altofare). `chi-siamo.php` li chiama "i figli di Guido" senza cognome: se Griste vuole nominare il fondatore, verificare il nome completo (Guido Burattin?) prima di scriverlo.
- Orari (non pubblicati, non in pagina); fax 049 8791367 (non in pagina, se è ancora attivo).
- I clienti: nessun marchio è in pagina. Si possono citare marchi o almeno "per le maison della calzatura"?
- Fiere: Lineapelle febbraio 2026 è stata tolta dalla home perché passata; se ci sono fiere in calendario possono andare nella riga della newsletter.
- Ricavi e dipendenti (Atoka) non sono in pagina e non vanno messi senza consenso.
- Lingue: oggi IT ed EN; servono altre lingue per le fiere di Parigi?

## Newsletter

Il modulo "Collezioni e fiere" nel piede (email, bottone, casella del consenso con link alla privacy) **non funziona finché non si collega a un servizio**: oggi non invia nulla e dopo l'invio mostra un messaggio. Va collegato a Brevo o Mailchimp (o al servizio che Griste usava per la newsletter di dicembre 2020) con doppio consenso, lista "Collezioni e fiere", e va aggiornata l'informativa privacy con il servizio scelto. Ha senso per Griste: collezioni stagionali, fiere (Première Vision, Lineapelle), newsletter già mandate, la privacy di oggi cita "l'invio di newsletter".

## Foto da rifare dal vero

Il materiale di oggi regge la direzione ma non la misura: l'area foto della home è il 25 % contro il 35 % dei siti di riferimento, perché le foto vere più grandi sono di 640 px. È la prima cosa da chiedere.

1. **Gli originali degli scontornati** (lo studio fotografico che li ha fatti avrà i file grandi; sul server ci sono solo copie a 450 px): almeno 1800 px di lato, meglio 3000, per i quattro pezzi del cassetto e i sei del campionario. **È il limite bloccante della proposta**: oggi il pezzo scelto è a 450 px a 1440 e sugli schermi 2x si vede morbido. Con gli originali va portato a 560-600 px (`--fw` in `finale/index.html`) ed esportato a 900 e 1350 px in `finale_img.py`.
2. **La chiusura** (oggi segnaposto Unsplash di GN Group, mani al banco orafo, con "Foto indicativa"): le mani di Griste al banco di smaltatura o al cesello a Villatora, con un pezzo vero sul banco, oppure un pezzo Griste montato su una scarpa. Luce di finestra laterale e calda, pezzo e mani a fuoco, profondità di campo corta, niente visi; formato orizzontale 4:3, almeno 2400 px di lato, con margine per un taglio quadrato per il telefono. Niente marchi di scarpe leggibili.
3. **Il laboratorio** (cesello del fiore, bagni galvanici, e se c'è la smaltatura): le stesse scene a piena risoluzione, orizzontali 3:2, almeno 2000 px, luce uguale per tutte. La foto del CAD di oggi non è in pagina (monitor con un marchio): se si rifà, senza marchi e con un modello Griste sullo schermo.
4. **Il campionario aperto negli astucci di velluto**, dall'alto, luce diffusa, per la sezione "Il campionario, ovvero il tesoro di Griste" o per la pagina del campionario.

## Pagine che il sito nuovo avrà (link di testata, campionario e piede)

`chi-siamo.html`, `campionario.html` (anche filtrata: `campionario.html?tipo=applicazioni`, `bottoni`, `placche`, `fibbie`, `puntali`, `talloni`), `lavorazioni.html`, `sostenibilita.html`, `collezioni/natura.html`, `collezioni/moda.html`, `collezioni/macchina-creativa.html`, `collezioni/natura-umana.html`, `contatti.html`, `privacy.html`, `cookie.html`, `documenti.html` (Codice etico, Modello 231 e Whistleblowing, con i link ad altofare.com), `en/`. Oggi esistono solo in questa lista: vanno fatte.

## Loghi

- In testata e nel piede c'è `sito/img/logo-griste-blu.svg`, la mia ricostruzione in SVG del logo contenuto nel PDF del codice etico (1374x392 px): coincide con l'originale nel 99,3 % dei pixel. Il blu è #014778, quello del PDF; il JPEG del sito di oggi è #2F68C1.
- Da chiedere: il logo vettoriale originale e il blu ufficiale. Nessun social: la pagina LinkedIn "griste srl" (9 follower) non è verificata come ufficiale, quindi nel piede non c'è una colonna "Seguici".

## Licenze

- Caratteri: Noto Serif Display e Red Hat Text, Google Fonts, SIL Open Font License 1.1 (uso commerciale ammesso), serviti dalla pagina.
- Foto di Griste: scontornati e foto del laboratorio dal sito griste.com, di proprietà dell'azienda.
- Foto esterna: una sola in pagina, GN Group su Unsplash (mani al banco orafo, Unsplash License verificata sulla pagina della foto), segnaposto da sostituire; dettagli in `assets/CREDITI.md`. Nessuna immagine generata dall'IA.

## Controlli dei segnali da IA

`_metodo/kit/segnali.sh` a 1440 dà 17 soglie su 18 a posto e nessuna da guardare (esito in `_prova/segnali-finale/home-1440-soglie.json`). L'unica bloccante che resta è l'area foto (25,4 %): manca il materiale, vedi "Foto da rifare". Il titolo a sinistra con il paragrafo a destra c'è solo nella sezione Azienda.

## Cosa è cambiato nell'ultimo passaggio

Prima schermata rifatta come cassetto del campionario (tolte le legende lette dalla foto), testi corretti (la data 1975 non contraddice più gli anni Ottanta, "i figli di Guido", i conti per lavorazione), lavorazioni e campionario su due colonne, laboratorio a due foto, chiusura con le mani al banco orafo, fondo più caldo, piede staccato. I dettagli sono nella NOTA, in fondo.
