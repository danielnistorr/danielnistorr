# Plastificazione Bastianello, home finale: nota

Pagina: `sito/index.html` (immagini in `sito/img`, caratteri in `sito/fonts`). Si rifà tutto con `sh _prova/script/build_finale.sh` (foglio d'apertura, foto, pagina, screenshot). Base: prototipo A "La finestra", scelto dal giudice (`_prova/giudizio.json`), con gli innesti da B. Questa è la rifinitura dopo il giudizio cieco sulla home finale (47 su 80, apertura da rifare).

## L'idea
Il lucido su opaco, cioè il dettaglio solo loro (analisi, sezione 1): la stampa la fa un altro, loro la fanno brillare, la proteggono, le aprono una finestra. In prima schermata un oggetto solo e vero: un foglio di cartoncino nero opaco con un damasco in serigrafia UV lucida, dalla loro foto migliore, ritagliato sul solo motivo e appoggiato sul fondo carta con un'ombra morbida. Il nero sta solo dentro l'oggetto, come nel riferimento Burgopak; tutto il resto è color carta. Sotto, una riga sola lo spiega: "Serigrafia UV lucida su nero opaco. La stampa è del cliente, il lucido è nostro." Con il nome di un altro finestratore la frase non regge.

## Cosa è cambiato in questa rifinitura
- **Apertura**: tolto il fotomontaggio Pexels dell'astuccio bianco (senza stampa, prospettiva incoerente, "Foto indicativa" in prima schermata). Al suo posto il foglio col damasco (foto loro, 917 x 763 px di ritaglio, ruotato di 2,5 gradi, ombra a tre livelli disegnata in PIL, WebP con trasparenza a 640, 880 e 1105 px). Tolti i tre punti numerati con filetti e la legenda: era lo stesso gesto della home Mario Agnoletto. Tolta la riga "Fogli fino a 120 x 160 cm" (valeva solo per la plastificazione e l'unità non è confermata). Il bottone è allineato al piede del foglio.
- **Foto delle schede**: stesso trattamento misurato per tutte (saturazione media portata a 0,085, tono caldo leggero, neri sollevati), così la finestratrice e il film olografico stanno nella stessa famiglia; il film Unsplash è desaturato al 38 %. La foto è larga 8 colonne (867 px a 1440) senza sbordare, e ogni file ha almeno quella larghezza: niente più ingrandimenti a 1x. `sizes` corretti: `(max-width:900px) 100vw, (max-width:1200px) 54vw, 867px`.
  - Finestratura: la finestratrice ad altezza nastro con gli astucci finestrati (foto loro, 1664 px).
  - Verniciatura UV: i fogli con UV a riserva, con il marchio "nathia" tolto in tutte le ripetizioni (inpainting sui soli tratti delle lettere, riquadri lilla riempiti col loro colore); didascalia "marchio del cliente oscurato".
  - Verniciatura serigrafica: la verniciatrice serigrafica con le aste cromate sui fogli in corsa (foto loro, 1706 px), al posto del damasco che ora apre la pagina.
- **Fascia del reparto**: tolta la foto affollata della verniciatrice con gli astucci per biscotti. Al suo posto, sotto la frase grande, la finestratrice in mosso con gli astucci in uscita (foto loro, 2560 px), che chiude la frase "le apriamo una finestra".
- **Schede sotto i 900 px**: una riga sola che scorre in orizzontale (scroll-snap, barra nascosta), la scheda scelta portata in vista da tastiera e al tocco.
- **Chiusura**: H2 "Abbiamo investito per migliorare i tempi di risposta", dalla pagina `azienda/`, al posto dello slogan generico col tu. Telefono, email e mappa invariati.
- **Testi**: "Packaging biodegradabile" ora dice "Accoppiature con film riciclabili con la carta, oppure compostabili e biodegradabili." (il film compostabile non va nella carta). La nota del disegno in scala della plastificazione dice "Il foglio più grande che lavoriamo, 120 x 160 cm." senza parlare di un tratteggio che lì non c'è. La riga sotto la frase grande ora riprende `azienda/` ("specializzati nelle lavorazioni e nobilitazioni conto terzi dello stampato").
- **Piede**: logo (228 px) e riga su chi sono come prima colonna di una griglia a cinque, allineati in alto con i titoletti; sotto i 1400 px il logo va su una riga sua e le quattro colonne restano sotto; a 768 due colonne, a 390 una.
- **1024**: titolo e paragrafo di "Per chi fa astucci" allineati sulla linea di base; foto della scheda in 4:5 tra 900 e 1200 px, alta quanto la colonna del testo; testo della chiusura su sei colonne.
- **Menu a 390**: pannello color carta a tutta altezza (100dvh), pagina bloccata dietro, chiusura con il bottone, con Esc o scegliendo una voce.
- Altezza: 4744 px a 1440 con il piede (prima 5188), 5549 a 390.

## Le prime due schermate
1. Testata con il logo vero (SVG del sito di oggi), quattro voci, telefono. A sinistra "Nobilitiamo lo stampato" in Archivo largo a 104 px; in basso la riga su cosa fanno e per chi e il bottone rosso "Chiedi un preventivo", allineato al piede del foglio. A destra il foglio col damasco, circa 650 x 550 px, con la riga di didascalia sotto. A 390: titolo, foglio a tutta larghezza, didascalia, quattro righe di testo e bottone entro i primi 844 px (finisce a 732).
2. "Cinque lavorazioni, conto terzi": cinque schede. Foto 4:3 su otto colonne, a destra nome, frase dai loro testi, varianti e fogli in scala con minimo e massimo.

Poi: la frase grande "La stampa la fa un altro. Noi la proteggiamo con un film, la facciamo brillare con la vernice, le apriamo una finestra." e sotto la finestratrice a tutta larghezza, con la riga grigia sugli anni e la didascalia; "Per chi fa astucci" con i tre settori in righe con filetti; la chiusura con frase, telefono grande con tel:, email con mailto:, indirizzo e link alla mappa, e il loro film olografico a filo del bordo destro; il piede.

## Piede
Fondo #EEEBE5, stesso tono della pagina. Logo vero in SVG con una riga su chi sono; quattro colonne: Azienda (Chi siamo, Certificazioni, Chiedi un preventivo), Lavorazioni (i cinque nomi), Settori (i tre nomi), Contatti (telefono, email, indirizzo con mappa). Riga legale: © 2026 Plastificazione Bastianello S.r.l., P.IVA e C.F. 03124050240, Cap. soc. € 110.000 i.v., Privacy, Cookie. REA e PEC non ci sono: vengono da aggregatori. I link puntano alle pagine del sito nuovo (elenco nel LEGGIMI).
- Niente newsletter: lavorano conto terzi su commessa per cartotecniche e stampatori, senza notizie, fiere, cataloghi, collezioni né clienti privati. Al suo posto "Chiedi un preventivo".
- Niente "Seguici": non hanno social, né nel codice del sito né in rete.

## Caratteri e colori
- **Archivo** (Google Fonts, SIL Open Font License 1.1), asse di larghezza: titolo a 112, H2 e frase grande a 120, peso 400. La forma larga richiama la scritta spaziata del loro logo e i titoli calmi di Derprosa e Progress Packaging.
- **Onest** (Google Fonts, SIL Open Font License 1.1), pesi 400 e 500, per testo, menu, didascalie e piede; cifre tabellari per formati e telefono.
- File woff2 serviti dalla pagina in `sito/fonts`. La licenza OFL permette di incorporarli e servirli.
- Carta #F6F4F0, piede #EEEBE5, inchiostro #171717, grigio #5B5751, filetti #D8D3CB, rosso del logo #CC3429 solo su bottone, scheda attiva e sottolineatura del telefono. Contrasti: grigio su carta 6,5:1, grigio sul piede 6,0:1, bianco sul rosso 5,1:1, inchiostro su carta 16,3:1.

## Interazione
Un solo gesto: le schede delle lavorazioni. Veri bottoni con ruolo tab, frecce, Home e Fine da tastiera, tocco al dito; il cambio è netto, senza dissolvenze. Cambiano foto, testo e il disegno dei fogli in scala. Sotto i 900 px la riga scorre e porta in vista la scheda scelta. A 390 il menu si apre con un vero bottone ("Menu" / "Chiudi", aria-expanded, Esc). Nessuna animazione allo scorrere, nessun effetto sul cursore; al passaggio cambiano solo colore o sottolineatura (0,15 s).

## Foto, origine e licenza
Trattamento unico misurato (PIL), WebP in più larghezze con srcset, 1,5 MB in tutto.
- Apertura: damasco in serigrafia UV lucida su nero opaco (`VERNICIATURA-SERIGRAFICA`, foto loro), solo il motivo, senza marchio, scritte né sito del cliente.
- Schede: finestratrice ad altezza nastro (`finestartura-2`); film olografico Unsplash gOfXb8eW4g8, Emily Bernal (Unsplash License), "foto indicativa"; fogli con UV a riserva (`VERNICIATURA-UV`, 853 px, marchio tolto); cartoncino a gradini (`blister.jpeg`, probabile repertorio, "foto indicativa"); verniciatrice serigrafica (`SERIGRAFIA-1`).
- Fascia: finestratrice in mosso (`fienstartura-1`). Chiusura: film olografico sulla plastificatrice (`plastificazione-1`).
- Nessuna immagine generata dall'IA, nessuna foto di repertorio già usata in altre home della campagna, nessuna foto ripetuta nella pagina; le foto di fibbie di Ruan Richard Rodrigues non sono usate.

## Controlli (24/10/2026, dopo la rifinitura)
- Screenshot guardati a pezzi: 1440 intera e prima schermata, 390 intera, prima schermata e menu aperto, 320, 768, 1024 e 1920 intere, le quattro schede nascoste a 1440, la riga delle schede a 390.
- `_prova/script/finale_prova.mjs` a 320, 360, 390, 430, 600, 768, 900, 1024, 1200, 1280, 1440, 1920 e 2560: scrollWidth uguale a innerWidth ovunque (a 1280 c'era uno sbordo di 45 px del piede, corretto con il passaggio a quattro colonne sotto i 1400 px). Schede: quattro frecce a destra portano a Serigrafica, Home alla prima, Fine all'ultima; tocco e clic aprono il pannello giusto; la riga resta su una riga sola e la scheda scelta è in vista (a 390, dopo Serigrafica, la riga è scorsa di 495 px). Menu da 320 a 600: pannello da 0 all'altezza dello schermo, pagina bloccata, Esc lo chiude e sblocca.
- Collegamenti: `tel:+390444414040`, `mailto:info@plastificazionebastianello.it`, `https://www.google.com/maps/search/?api=1&query=45.48317,11.71154` (8 collegamenti tra testata, menu, chiusura e piede).
- `_metodo/kit/segnali.sh` a 1440: 0 soglie bloccanti su 10. Foto 35,2 % della pagina, Onest 86,6 % e Archivo 13,4 %, 0 mono, 0 etichette maiuscole, 0 titoli col punto, 2 fasce di colore (pagina e piede), 7 filetti larghi, 1 sezione con titolo a sinistra e testo a destra, 0 frecce, 0 numerazioni. Da guardare: una sola misura di H2 (56 px, voluta: la chiusura non grida più del resto) e nessuna data in pagina, perché l'unico anno sicuro è quello della srl (2004) e "da oltre 40 anni" va chiarito (LEGGIMI).
- Divieti del committente: niente gradienti, testo in gradiente, emoji, Inter, card con bordo colorato, vetro, scuro a basso contrasto, tre box con icona, badge sopra il titolo, icone Lucide, dissolvenze allo scorrere, effetti sul cursore, bottoni che sbiadiscono, corsivi d'accento. Nessuna lineetta lunga U+2014 in pagina, negli script, in questa nota e nel LEGGIMI.
- Dati: ogni fatto viene da `01-analisi.md`. Non sono in pagina la BRCGS (certificati pubblicati scaduti), REA e PEC, dipendenti e fatturato.
- Riferimenti guardati: `riferimenti/` (Derprosa, Burgopak, Progress Packaging, Kurz, Pusterla) e le prime schermate delle home amate della campagna. Rispetto ad Agnoletto non ci sono più punti numerati né legende attorno all'oggetto: un foglio vero e una riga.
