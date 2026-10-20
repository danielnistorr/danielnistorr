# Home finale: "Lo strumento"

Pagina: `sito/index.html` (si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini, controllo dei testi, screenshot e prove a 320, 768, 1024, 1920). Base: prototipo A, con tutte le indicazioni del giudice e gli innesti da B. Altezza a 1440: 5977 px con il piede; a 390: 6516 px.

## L'idea

Il loro mestiere è misurare l'energia: in apertura c'è un solo strumento di misura vero, un amperometro da pannello, scontornato lungo la ghiera e posato sulla carta della pagina con un'ombra corta, grande e nitido, accanto al titolo loro. Le tre legende nominano parti che si vedono davvero nella foto, con il filo che arriva proprio lì: 1 L'ago (a riposo), 2 Lo zero (la vite di azzeramento sotto il quadrante), 3 Classe 1,5 (il segno di precisione stampato sul quadrante). I fili e i punti delle legende sono in bianco con fusione "differenza": scuri sulla carta e sul quadrante, chiari dove passano sul nero della ghiera. Il resto della pagina è carta chiara, un carattere solo e il verde del logo come accento.

## Prime due schermate

- **1440, prima schermata** (`home-1440-prima-schermata.jpg`). L'amperometro a sinistra (690 px, dentro il margine di 64 px), il titolo a destra su tre righe a 95 px (dall'intestazione di privacy.php), la riga su cosa vendono e da quando, il bottone "Chiamate lo 049 8791358" (tel:) e il link al catalogo. Le legende stanno su una riga sotto lo strumento; "Foto indicativa" sta nell'angolo libero in basso a destra della foto, sopra le legende, non più da sola sotto. La prima schermata finisce con le legende (y circa 860): sotto restano circa 40 px di carta.
- **390, prima schermata** (`home-390-prima-schermata.jpg`): titolo su tre righe a 47 px, lo strumento a tutta larghezza subito sotto (senza legende, che a 390 non si leggerebbero), "Foto indicativa" a destra sotto la foto, poi la riga, il bottone del telefono e il link. Testata con logo, telefono cliccabile e un vero bottone "Menu". A 768 e a 1024 le legende tornano, solo con il titoletto (distanza minima 29-42 px).
- **Seconda schermata**: "Misurare i consumi per centri di costo, e poi ridurli" a tutta misura con i due paragrafi sotto, uno accanto all'altro (non più titolo a sinistra e testo a destra), poi la frase dei numeri a 44 px: "Dal 1991 a Saonara: 11 aree, 148 prodotti a catalogo, oltre 90 impianti in referenza".

## Il resto della pagina

1. Il catalogo con il selettore delle 11 aree (l'unico gesto). I marchi solo nella riga d'intestazione; "Protezione di interfaccia CEI 0-21" scritta col nome giusto della norma. Il pannello prende l'altezza della scheda più lunga, ricalcolata al cambio di larghezza: cambiando area la pagina sotto non salta (811 px a 1440 per tutte le 11 schede).
2. L'analisi dei consumi sul campo #E6E4DE: "Gli sprechi possono pesare dal 10 al 30% sulla bolletta" a 66 px, le righe sugli Energy Manager e il bottone a sinistra; a destra il contatore su muro a calce, quadrato, allineato in alto al titolo e fino al bordo destro della finestra (anche a 1920). A 390 la foto va sotto il testo, a filo del bordo destro.
3. "Lavoriamo con installatori, manutentori, studi tecnici, consulenti, ESCO e con le aziende che consumano", con la coda in grigio, e tre righe: Assistenza tecnica (le tre note linkate), Cataloghi e preventivi, Lavora con noi.
4. Chiusura "b con foto": foto a sinistra a filo del bordo (7 colonne su 12, alta 940 px), testo a destra centrato in altezza. Frase loro dalla home di oggi: "Il modo migliore per risparmiare è decidere di farlo". Telefono a 48 px con tel:, email con mailto:, sede con "Apri la mappa" (coordinate di dove-siamo.php), agenti. La foto è un soggetto diverso dall'apertura: i moduli su guida DIN in un quadro, con i morsetti verdi.
5. Piede: logo vero (lo stesso ritaglio della testata, senza la riga della ragione sociale, 300 px, WebP 2x; nessun SVG ricostruito, perché il logotipo a lettere disegnate non si rifà fedele a mano), la riga "Gli specialisti del controllo e la gestione dei consumi energetici. Dal 1991 a Saonara."; sulla stessa riga, dalla terza colonna, la newsletter con il campo a sola linea, "Iscrivetevi" testuale a destra e la casella del consenso; quattro colonne (Azienda, Prodotti, Assistenza, Contatti con tel., fax senza link, email, PEC scritta per esteso con mailto, indirizzo con mappa); riga legale con ragione sociale, P.IVA e C.F., REA, Privacy, Cookie. Niente Seguici: non hanno social. A 390 le colonne si aprono a fisarmonica con bottoni veri (`aria-expanded`). Nessun testo sotto 12 px nel piede.

## Caratteri e colori

- Un carattere solo: **Pathway Extreme** (Eduardo Tunni, Google Fonts), variabile con larghezza 75-100 e asse ottico. Licenza **SIL Open Font License 1.1**, letta nel file servito (nome 14: "https://scripts.sil.org/OFL"; nome 0: "Copyright 2019 The Pathway Extreme Project Authors"). Servito dalla pagina da `sito/fonts/pathway-extreme-latin.woff2`. Titoli a larghezza 76-84 % e peso 400, testo a larghezza 100 %; cifre tabellari (`tnum`) per numeri, misure e telefoni. Motivo: il logotipo TONINATO GIORGIO è fatto di lettere strette e geometriche e il grottesco stretto ne è l'eco, con l'aria delle targhette degli strumenti; non fa il verso a Gira (UniversNext) né a Janitza (Source Sans). Non è nella lista b della guida né nelle altre home della campagna.
- Colori: carta #F3F2EE, campo #E6E4DE (analisi e chiusura), inchiostro #1F2321, grigio #565B58 per i testi secondari (AA su tutti e due i fondi), verde del logo #00A650 solo per sottolineature, verde scuro #00783A per i numeri accesi e i numeri delle legende (AA). Le foto hanno lo stesso trattamento (colore spento al 70-72 %, neri appena sollevati): bianco e nero dello strumento, calce del contatore, grigio e verde dei moduli.
- Riferimenti (sez. 7 di 01-analisi): Vimar per l'oggetto tecnico solo su fondo chiaro, Basalte e Gira per la frase grande con tanto vuoto, Janitza per il mestiere scritto come un fatto, Sense per il titolo grande che dice cosa fanno.

## Interazione

Il selettore delle 11 aree del catalogo: un tablist vero (frecce, Home, Fine, Tab), a 390 una riga che scorre di lato dentro la sezione e si tocca col dito. Al tocco cambia la scheda: nome dell'area, prodotti a catalogo, categorie vere, un prodotto d'esempio con le misure (per esempio "TA 30: spazio cavo 28 mm, spazio barra 30x10") e il link all'area. Nessuna animazione d'ingresso, nessun effetto che segue il cursore; transizioni di 120-150 ms solo su link e bottoni, spente con `prefers-reduced-motion`. Provato da tastiera e al tocco in `scatti_finali.mjs` (frecce fino a "T.A. a foro passante", Fine fino a "Monitoraggio sismico", tocco sull'area 08, fisarmonica Contatti, menu).

## Foto: origine e licenza

Tutte segnaposto, marcate "Foto indicativa" in pagina. Le foto dell'azienda non reggono (foto di catalogo dei produttori a 300 px, voto 3/0-1 in `_prova/inventario-immagini.json`). Licenza Unsplash (uso commerciale libero, modifiche ammesse), verificata sulla pagina di ogni foto il 20/10/2026. Nessuna è in un altro `*-Sito/assets/CREDITI.md` della campagna. Annotate in `assets/CREDITI.md`.

- Apertura: Markus Spiske, https://unsplash.com/photos/ar6XfQSeSwM, riscaricata a 4800 px; solo l'amperometro, scontornato con una maschera circolare sul cerchio della ghiera misurato sul file (centro 1016, 1573; raggio 900), ombra corta disegnata con PIL e controllata perché non tocchi il bordo della tela; `sito/img/ampere-700/1000/1380/2000.jpg`.
- Analisi: Moritz, https://unsplash.com/photos/WwQYfbYuDGU, marca del contatore sfocata; `sito/img/contatore-600/900/1260.jpg`.
- Chiusura: Aleksandr Lyaptsev, https://unsplash.com/photos/lTAh5dGmN-8, marchi delle etichette sfocati; `sito/img/moduli-600/900/1170.jpg`.

## Controlli (ultimo giro)

- Scorrimento orizzontale: scrollWidth uguale a innerWidth a 320, 360, 390, 560, 768, 900, 1024, 1180, 1280, 1440, 1920, 2560 (`verifica_finale.mjs` e `scatti_finali.mjs`). A 320 il telefono della testata si nasconde (resta nel bottone subito sotto il titolo).
- Guardati a pezzi: 1440 e 390 (le schermate in questa cartella), 320, 768, 1024, 1920 (prove PNG, poi cancellate). Nessuna sovrapposizione; legende distanti almeno 29 px a 1024 e 42 px a 768.
- Interazione: selettore provato con frecce, Fine e tocco (frecce fino a "T.A. a foro passante", Fine fino a "Monitoraggio sismico", tocco sull'area 08 a 390); altezza del catalogo identica su tutte le 11 schede a ogni larghezza; fisarmonica Contatti al tocco; menu mobile con `aria-expanded`; newsletter che risponde "non ancora collegata".
- Collegamenti: `tel:+390498791358`, `mailto:info@toninatogiorgio.it` (anche con oggetto "Analisi dei consumi"), `mailto:amministrazione@pec.toninatogiorgio.it`, mappa con le coordinate 45.38446, 11.986261.
- Console senza errori aprendo da file:/// (tolto il preload del carattere, che dava l'errore CORS).
- Nessun U+2014 in pagina, in questa NOTA, nel LEGGIMI e nei CREDITI (`controlla_testi.py` e grep), nessun segnaposto in pagina.
- Segnali da IA (`_metodo/kit/segnali.sh`): famiglia unica, niente mono, niente etichette sopra i titoli, niente titoli col punto, niente frecce, niente titoli neri; "titolo a sinistra e testo a destra" ora in una sola sezione (il catalogo). Da guardare e tenuti con ragione: 5 fasce di fondo (una è la carta della pagina), i numeri accesi nella frase dei numeri e il conteggio del selettore, la numerazione 01-11 che è l'indice del catalogo, i "gradienti" che sono le sottolineature dei link. **Area foto 20,6 %, sotto la soglia del 35 %**: è una scelta, perché il committente premia la pagina pulita con un solo oggetto e altre foto di repertorio la renderebbero un catalogo di stock; salirà con le foto vere (LEGGIMI, Foto da rifare dal vero).
- Dati: tutti da 01-analisi.md. Cosa resta da confermare è nel LEGGIMI.

## Cosa è cambiato nell'ultimo giro (dal giudizio cieco)

- Apertura: al posto della foto dei fili colorati, un oggetto vero della misura (l'amperometro), con le legende riscritte sulle parti visibili. Tolta la legenda "analizzatore e T.A." che indicava un ricciolo di filo.
- Chiusura: i moduli su guida DIN al posto del fascio di fili; nessuna foto ripete un'altra.
- Corpo: una foto nella fascia dell'analisi, nella metà destra che era vuota, fino al bordo della pagina; padding della fascia da 128-136 a 112 px.
- "Foto indicativa" dentro l'angolo libero della foto; fondo della prima schermata stretto (chi siamo parte 64 px sotto).
- Legende a 1024: solo il titoletto, distanza minima 29 px.
- Catalogo: altezza fissa del pannello, nessun salto cambiando area.
- Chi siamo in colonna unica con i paragrafi affiancati sotto il titolo; titoli con `text-wrap: balance`.
- "93 impianti" diventa "oltre 90 impianti" finché non si riconta.
- Piede: logo senza la riga della ragione sociale, PEC per esteso con mailto.
- Tolto il preload del carattere (errore CORS da file:///).
