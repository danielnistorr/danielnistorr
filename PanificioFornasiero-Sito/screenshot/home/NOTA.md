# Home finale, Panificio Galileo Fornasiero (2 novembre 2026, ultimo passaggio)

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP a più larghezze con srcset), caratteri in `sito/fonts/`. Si rigenera tutto con `_prova/script/build_finale.sh`.

Screenshot: `home-1440.jpg` (6255 px compreso il piede), `home-1440-prima-schermata.jpg`, `home-390.jpg` (7913 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`.

## Idea

La frase di Galileo al Mattino di Padova, "Siamo Fornasiero, fornai anche nel nome", è l'impaginazione: la seconda e la terza riga del titolo partono esattamente sotto la F di "Fornasiero", così "Forna" e "forna" stanno una sopra l'altra, nel colore delle spighe. Nel gradino che resta libero sotto "Siamo" c'è la loro focaccia veneta, intera, vista dall'alto. Titolo e oggetto si incastrano: con il nome di un altro forno la pagina non sta in piedi.

## Cosa è cambiato in questo passaggio

Prima schermata (bloccante e importanti del giudice, più la richiesta del committente del 2 novembre):
- Via il panino di repertorio su lino grigio, la foto a tutta larghezza con la sfumatura e "Foto indicativa". L'oggetto ora è un prodotto loro: la focaccia veneta con la glassa di zucchero e le mandorle (foto Nikon del panificio, dicembre 2020), scontornata intera con GrabCut (`_prova/script/scontorna_focaccia.py`; dove la focaccia appoggia sull'etichetta del sacco il bordo è letto a mano sul file originale), con un'ombra morbida a destra e in basso come la luce di finestra della foto. A 1440 è larga 403 px e alta 412 (il 46 % dello schermo); nessun bordo tocca la testata o i lati: la cupola sta 256 px sotto la testata, sotto la prima riga del titolo, il bordo sinistro è sul margine di pagina (72 px) e tra il bordo destro e la colonna del testo restano 43 px.
- Nessuna sfumatura linear-gradient sulle foto, in nessun punto della pagina.
- Il fondo dell'apertura e del piede non è più la carta: è la mollica (#F4E6B5), il giallo di uova e burro dentro la focaccia e il panettone. La ragione si vede: la fetta del panettone nel dittico di Natale e le tagliatelle all'uovo hanno lo stesso giallo. Il resto della pagina resta la carta bianca del sacchetto della bottega (#FAF9F6), che si vede dietro le tartarughe. Niente beige di comodo.
- La scelta di impaginazione nuova per la campagna: l'oggetto sta dentro il gradino del titolo, non a destra e non sopra; il titolo è a 145 px su tre righe e occupa tutta la larghezza utile (1296 px a 1440). Nessuna delle copertine di `_invio/zona/home/` e delle home amate ha un titolo a gradino con l'oggetto nel gradino, né un fondo giallo preso dal prodotto. Niente legende numerate, pallini o filetti sull'oggetto: solo una didascalia sotto ("La focaccia delle Feste, con la glassa e le mandorle.").
- La riga di stato di riserva ora dice "Dal lunedì al venerdì dalle 8.30. Il sabato mattina via Alsazia 3 è aperta.", senza far credere che via Vigonovese il sabato sia chiusa. Il link agli orari va a capo pulito sotto.
- A 1280x720 tutta l'apertura sta nella piega (bottone e stato finiscono a 668 px); a 1920 l'apertura è centrata in altezza e non supera 860 px; a 390 la focaccia sta sopra, centrata, e il titolo su quattro righe con "Fornasiero" e "fornai" allineati; tutto il blocco, bottone e stato compresi, sta nei primi 844 px.

Parte centrale:
- Chi siamo: la frase è "Galileo Fornasiero è arrivato a Camin il primo aprile del 1963. Fidalma è al banco da sessant'anni." (Filippo, Romina e Michele Daniele tolti finché il panificio non dà il permesso). Le date stanno a destra della vetrina, allineate in alto alla foto.
- Il pane di oggi: le tartarughe sono ridotte a 6 colonne (636x707 a 1440), tagliate da x 320 (fuori il pangrattato a sinistra e la sessola di plastica a destra), con la scritta "Fornasiero srl Camin-Padova" in alto; la dominante gialla della lampada è corretta verso il bianco delle foto di Natale; la didascalia è sotto la foto. A sinistra, nella stessa altezza: titolo, i cinque pani con il nome di casa uno per riga in Sentient a 56 px, come sulla lavagna del banco, e in fondo gli altri quindici pani. Nessuna colonna vuota.
- Pasta, pizze e dolci: le forniture sono uscite dalla sezione (ora il titolo dice il vero) e stanno in una riga sotto le schede dei negozi, con il link a `fornitura.html`. Restano tre voci, in tre righe nome e descrizione, sotto una fascia a tutta larghezza di tagliatelle all'uovo (segnaposto con "Foto indicativa" in didascalia).
- Natale: il dittico è panettone e sacco del cinquantesimo (l'etichetta 1963-2013 con il bordo della focaccia), per non ripetere la focaccia intera dell'apertura. Le due didascalie hanno lo stesso rientro (var(--m) dal bordo della propria foto).
- Chiusura: la foto di repertorio fredda con i quadretti blu è sostituita da panini nei sacchetti di carta, luce calda; la foto è alta esattamente quanto la colonna del testo (posizione assoluta dentro la cella), e la colonna distribuisce frase, schede e riga delle forniture dall'alto in basso. A 1440 testo e foto finiscono alla stessa riga. I due pannelli delle schede occupano la stessa cella: cambiando negozio la pagina non salta.
- Piede: logo a 120 px (PNG a 2x e 3x), la scritta sotto il cesto si legge; tra la fascia alta e il filetto delle colonne 44 px; a 390 ogni link delle colonne è alto 40 px (padding 9 px sopra e sotto).

## Caratteri e colori

- Titoli, nomi dei pani, telefoni: Sentient 400/500. Testo: General Sans 400/500. Tutti e due di Indian Type Foundry, da Fontshare, licenza ITF Free Font License (uso commerciale gratuito), file serviti dalla pagina in `sito/fonts/`. Una serif dritta e piena, senza corsivi, che regge il titolo a 145 px come una scritta da bottega; il riferimento per la coppia serif grande e bastone piccolo è il piede di Poilâne. Cifre tabellari per orari e telefoni.
- Colori: mollica #F4E6B5 (apertura e piede), carta #FAF9F6, inchiostro bruno #33261F (13,9:1 sulla carta, 11,7:1 sulla mollica), testo secondario #645349 (6,9:1 e 5,8:1), spiga #9A5320 per "Forna/forna" e le date (5,5:1 e 4,6:1), blu #2E4D7B per bottone, campo del modulo e fuoco (8,1:1 e 6,8:1; bianco sul blu 8,5:1). Tutti AA.

## Interazione

Un solo gesto: le schede dei due negozi nella chiusura. Veri bottoni con ruolo tab, frecce, Home e Fine da tastiera, cambio netto senza dissolvenze; per ognuno lo stato di adesso calcolato sull'ora di Roma, il telefono grande con tel:, gli orari, mailto: e "Apri nella mappa". Se all'apertura è aperto solo via Alsazia, la scheda mostra quello. Transizioni solo di colore su link, schede e bottoni; niente comparse allo scorrere, niente effetti al cursore.

## Foto, origine e licenza

- Apertura: la focaccia veneta, foto del panificio (`b56ebf_fabc...`, Nikon D3300, dicembre 2020), scontornata.
- Chi siamo: la vetrina con Galileo e Fidalma, loro, 640x319 alla misura nativa.
- Il pane di oggi: tartarughe della galleria del sito del panificio, loro.
- Pasta fresca: Karen Sewell, https://unsplash.com/photos/T6vI65xwoNA, Licenza Unsplash. SEGNAPOSTO, con "Foto indicativa" in didascalia.
- Natale: panettone sul sacco di juta e l'etichetta del cinquantesimo, foto loro.
- Chiusura: Victoria Nazaruk, https://unsplash.com/photos/ytxRXkY8QE4, Licenza Unsplash. SEGNAPOSTO, senza didascalia che la faccia passare per loro. Non usata in altre home della campagna (controllati tutti i `*-Sito/assets/CREDITI.md` il 2/11/2026); idem Sewell.
- Logo nel piede: il PNG del sito a una tinta, nel bruno del sacchetto; non ricostruito in SVG perché il disegno ha ombre e sfumature.
- Nessuna immagine generata dall'IA. Trattamento comune con PIL in `_prova/script/finale_img.py`.

## Piede

Logo e una riga su chi sono; newsletter "Gli avvisi di Romina" (prenotazioni delle Feste e dolci nuovi: ha senso, hanno clienti privati e notizie che tornano ogni anno), con campo, bottone e consenso, che non invia nulla finché non si collega a un servizio; quattro colonne (Il panificio, Prodotti, I negozi, Seguici con il solo Instagram, l'unico social collegato dal loro sito); riga legale con ragione sociale, indirizzo e P.IVA, Privacy e Cookie. Il REA non c'è finché non arriva una visura. A 390 le colonne si impilano nell'ordine Il panificio, Prodotti, I negozi, Seguici.

## Controlli (2 novembre 2026)

- Screenshot guardati a pezzi: 1440 intera e prima schermata, 390 intera e prima schermata, 320, 768, 1024, 1280x720, 1920.
- scrollWidth uguale a innerWidth a 320, 360, 390, 430, 600, 601, 768, 900, 901, 1024, 1100, 1101, 1280, 1440, 1680, 1920 e 2560 (`_prova/script/controlli.mjs`).
- Altezza a 1440: 6255 px compreso il piede.
- Gesto (`_prova/script/prova_gesto.mjs`, orologio finto, ora di Roma): lunedì 10.00 e 14.30, mercoledì 10.00 e 17.00 (si apre su via Alsazia), venerdì 21.00, sabato 10.00 (via Alsazia aperta, via Vigonovese "meglio chiamare") e 15.00, domenica 10.00; frecce, Home e Fine da tastiera; tocco a 390; menu del telefono.
- Collegamenti: tel:+390498702658, tel:+390498705107, tel:+393386600664, mailto:info@panificiogalileofornasiero.it, due link alla mappa (via Vigonovese 116 e via Alsazia 3), nessuna ancora rotta.
- Segnali da IA (`_metodo/kit/segnali.sh`): 0 soglie bloccanti su 10, 0 da guardare su 8; foto al 38,4 % della pagina, 3 misure di H2, un solo titolo col punto (la citazione di Galileo), 4 filetti larghi, nessun mono, nessun badge, nessuna freccia, nessuna numerazione.
- Nessun carattere U+2014 in pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.
- Divieti del committente: nessun gradiente, nessun titolo in gradiente, niente Inter, niente icone, niente card, niente vetro, niente corsivo serif d'accento, niente legende numerate.
- PNG temporanei cancellati (anche quelli grandi in `_prova/cieco/`).
