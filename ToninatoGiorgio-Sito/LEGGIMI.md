# Toninato Giorgio: proposta di nuova home

Proposta non richiesta di una nuova homepage per TONINATO GIORGIO di Rigato Claudia & C. s.n.c. (Villatora di Saonara, PD). Solo la home. Nulla è stato inviato all'azienda né pubblicato.

## Cosa c'è

- `sito/index.html`: la home finale (si apre con file:///). `sito/img/`: solo le immagini usate, JPEG e WebP in più larghezze. `sito/fonts/`: il carattere servito dalla pagina.
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, e `NOTA.md` (idea, schermate, caratteri, colori, interazione, foto, controlli).
- `_prova/script/build_finale.sh`: rifà immagini, controlli e screenshot (`build_img.py`, `controlla_testi.py`, `scatti_finali.mjs`). La pagina è scritta a mano. `_prova/script/verifica_finale.mjs`: area foto, altezza del catalogo su tutte le schede, distanza fra le legende, console, scorrimento da 320 a 2560, collegamenti.
- `01-analisi.md`: i fatti con le fonti. `_prova/home/a` e `b`: i due prototipi da cui è nata la finale (scelto A).

## Dati da confermare prima della messa in linea

1. **"Dal 1991"**: l'attività parte nel 1991 (chi-siamo.php), l'attuale snc è costituita il 22/12/2009 (companyreports.it). Chiedere se la snc continua la ditta del 1991 e se va scritto così.
2. **Impianti in referenza**: 01-analisi dice 93, `_prova/crawl/referenze.json` ha 94 righe senza doppioni. Finché non si riconta sulla pagina vera, in home c'è "oltre 90 impianti in referenza", in un posto solo (la frase della seconda schermata). Con il numero confermato si scrive quello. In home solo numeri: nessun nome di cliente o di persona senza il loro permesso.
3. **148 prodotti e 11 aree**: contati sul sito di oggi (2013, novità fino al 2020). Confermare che il catalogo è ancora questo e quali marchi trattano ancora (in pagina solo Electrex, Astrel Group, 4-noks, Nethix, Yuasa nell'intestazione del catalogo; Kemet-Arcotronics, Panasonic, Pectech, Boldrin non scritti).
4. **Energy Manager e analisi dei consumi** con relazione tecnica: chi la fa, se è ancora attiva e se è ancora gratuita (in pagina non c'è scritto "gratuita").
5. **"Gli sprechi possono pesare dal 10 al 30% sulla bolletta"**: è la loro frase di news.php ("possono incidere dal 10% al 30%"); confermare che la vogliono in evidenza.
6. **Frase di chiusura** "Il modo migliore per risparmiare è decidere di farlo": è nel cartiglio della home di oggi; confermare che è ancora la loro.
7. **Orari** di ufficio e magazzino: non pubblicati, quindi in chiusura non ci sono. Aggiungerli se li danno. Dire se c'è un banco aperto agli installatori.
8. **Numero verde 800 34 13 18** (immagine in dove-siamo.php): non usato finché non confermano che è loro.
9. **"Il preventivo si chiede dal sito, per telefono o per email"** e **"Cerchiamo... un agente per la zona libera"**: da Preventivi e da agenti.php ("Cercasi Collaboratore per la zona libera"); confermare che valgono ancora.
10. **Capitale sociale**: non pubblico, quindi non è nella riga legale. Se lo vogliono, va aggiunto lì.
11. **Norma**: in pagina "CEI 0-21" (il nome corretto); sul sito di oggi è scritto "CEI-021".
12. **Testo del consenso della newsletter**: da far rileggere a chi cura la privacy (privacy@toninatogiorgio.it).

## Newsletter

Ha senso: pubblicano novità di prodotto, promozioni, cataloghi e inviti a seminari e webinar, e la loro informativa prevede già comunicazioni via email con consenso revocabile. Nel piede c'è il campo email, il bottone "Iscrivetevi" e la casella del consenso. **Il modulo non funziona finché non si collega a un servizio di invio** (Brevo o Mailchimp, con doppio consenso): oggi controlla solo i campi e risponde che l'iscrizione sarà attiva quando verrà collegato.

## Pagine del sito nuovo a cui puntano i link

Nella home i link a pagine che non esistono ancora sono `#`. Da creare:

- Azienda: Chi siamo, Agenti e zone, Referenze, Lavora con noi, Dove siamo.
- Prodotti: una pagina per area (Monitoraggio consumi, Gruppi di misura UTF, T.A. apribili, T.A. a foro passante, IoT e M2M, Telecontrollo, Fotovoltaico Elios4you, Protezione di interfaccia CEI 0-21, Accumulatori, Smart home Rialto, Monitoraggio sismico) e l'elenco di tutte le 11 aree.
- Assistenza: Assistenza tecnica (con il modulo di richiesta), Note tecniche (le 14 da scaricare, tra cui "Protocollo Modbus", "Nota tecnica applicativa per l'installazione di reti RS485", "Selezione del T.A. e determinazione della sezione del cavo di collegamento"), Domande frequenti, Cataloghi (9 PDF), Richiesta di preventivo, Analisi dei consumi.
- Legali: Privacy (oggi è un PDF), Cookie (oggi non esiste: `cookie.php` dà 404).
- Social: nessuno trovato, quindi niente colonna Seguici.

## Foto da rifare dal vero

Le tre foto in pagina sono segnaposto di Unsplash, marcate "Foto indicativa": l'amperometro analogico di Markus Spiske in apertura, il contatore su muro a calce di Moritz nell'analisi, i moduli su guida DIN di Aleksandr Lyaptsev in chiusura. Nessuna mostra Toninato o un prodotto che vendono; i marchi stampati sono sfocati. Le foto dell'azienda oggi sono solo schede dei produttori a 300 px. Servizio fotografico consigliato:

1. **Apertura, la più importante**: un loro strumento da pannello o un trasformatore amperometrico a foro passante (per esempio il TA 30) attraversato da un cavo di rame, ripreso di fronte o dall'alto su cartoncino chiaro senza grana, luce morbida dall'alto con ombra corta, almeno 6000 px di lato, nessun marchio in vista, molto fondo libero intorno (in pagina va scontornato come l'amperometro di oggi). Le tre legende vanno riscritte sulle parti del pezzo vero: per un T.A. "spazio cavo 28 mm", "spazio barra 30x10", "secondario 5 A"; per un analizzatore 96x96 il display, i morsetti, il formato.
2. Per il selettore del catalogo, la stessa serie, un oggetto per area sullo stesso cartoncino e con la stessa luce: un analizzatore su guida DIN, un contatore UTF, una batteria Yuasa, un termostato Rialto, un T.A. apribile. Così al tocco cambia anche l'oggetto.
3. **Analisi**: le mani di un Energy Manager con lo strumento portatile su un quadro vero, a fuoco sullo strumento, verticale (va nel posto del contatore, a destra fino al bordo).
4. **Chiusura**: il magazzino o il banco di Saonara in luce naturale, verticale, con gli scaffali o le scatole in fila; niente persone in posa.

Oggi le foto coprono circa il 20 % della pagina a 1440: con le foto vere l'impaginazione resta la stessa.

## Licenze

- Carattere: **Pathway Extreme** (Eduardo Tunni, Google Fonts), SIL Open Font License 1.1, uso commerciale libero; servito da `sito/fonts/pathway-extreme-latin.woff2`.
- Foto segnaposto: licenza Unsplash (uso commerciale libero, attribuzione non richiesta, modifiche ammesse), verificata sulla pagina di ogni foto il 20/10/2026; dettagli in `assets/CREDITI.md`. Nessuna immagine generata dall'IA.
- Foto dei produttori nel crawl (Electrex, Yuasa, Nethix, 4-noks e altri): non usate in home; per usarle nelle pagine prodotto serve il permesso dei produttori.

## Loghi

- Il logo usato è il PNG trasparente del sito di oggi (`images/logo_azienda_full.png`, 3180x650), ritagliato senza toccare la forma: in testata e nel piede lo stesso ritaglio, marchio e logotipo senza la riga della ragione sociale (che nel piede è per esteso nella riga legale), in WebP a 2x.
- Nessun SVG ricostruito: il logotipo ha lettere disegnate che a mano non si rifanno fedeli. Chiedere all'azienda se esiste un logo vettoriale (AI, EPS, PDF o SVG) dal grafico che l'ha disegnato.
- Nessun logo di terzi in pagina.
