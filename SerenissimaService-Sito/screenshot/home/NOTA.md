# Serenissima Service, home finale: nota

Pagina: `sito/index.html` (statica, si apre con file:///). Immagini in `sito/img/` (solo quelle usate, WebP in 2-5 larghezze, loghi PNG a 1x e 2x), caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, pagina da `_prova/script/index.html`, screenshot). Base: prototipo A "La cabina", con le indicazioni del giudice cieco e la richiesta del committente del 2 novembre ("più alta gamma, meno uguali tra loro").

Altezza: 5168 px a 1440 (piede compreso), 6130 px a 390.

## Idea

La promessa del loro logo, "Botta? Risposta!", detta da una carrozzeria che ha nove cabine di verniciatura. La prima schermata è un trittico in asse: al centro una sola foto alta e stretta, la cabina vista come una porta con dentro la Ferrari 488 che hanno riparato nel 2018; a sinistra la domanda "Botta?" in alto, a destra la risposta "Risposta!" più in basso, all'altezza del tetto dell'auto, e sotto la risposta cosa fanno e il telefono. La domanda e la risposta stringono la cabina: il mestiere è quello che sta in mezzo.

## Cosa è cambiato in questo passaggio (2 novembre)

- **Apertura rifatta dentro la stessa idea**: niente più titolo a sinistra e foto sfumata a destra con le legende. Foto verticale 1478 x 2180 in asse su cinque colonne (4-8), a filo della testata e lunga fino alla piega; "Botta?" sulle colonne 1-3 allineato alla foto, "Risposta!" sulle colonne 9-12, sfalsato di 1,6 righe. È un'impaginazione che nella campagna non c'è: tutte le altre home hanno il titolo a sinistra e l'oggetto a destra, oppure il titolo sopra una foto larga.
- **Niente legende con pallino e filetto**: tolte le due legende numerate; resta una didascalia sobria in basso a sinistra, allineata a destra contro la foto ("Una delle 9 cabine di verniciatura di Corso Stati Uniti, con la Ferrari 488 riparata nel settembre 2018"), visibile a tutte le larghezze e collegata alla figura con `aria-describedby`.
- **Colore di fondo dal mestiere**: il beige #F4F2EC è diventato il "bianco cabina" #EEF1ED, il bianco freddo e appena verde che hanno i pannelli e il film protettivo di una cabina di verniciatura sotto le lampade, campionato dalla foto stessa. La ragione si vede: le pareti della cabina nella foto e la pagina sono lo stesso bianco, e tutte le foto sono trattate moltiplicandole per quel colore. Il piede è lo stesso bianco in ombra (#E1E7E1).
- **Scala tipografica nuova**: titoli in Archivo stretto (larghezza 75 %, peso 600) a 124 px nell'apertura e nella chiusura, 68 px negli H2; il testo resta Archivo normale e i titoletti dei reparti semi larghi. Nella campagna nessuna home usa un titolo stretto e alto: qui fa da eco alla foto verticale e alle scritte dei mezzi da corsa e da soccorso.
- **Foto più grandi**: le foto dei reparti vanno a tutta larghezza fino a 1440 px (1,9:1, esportate fino a 1900 px); la lucidatura passa a sei colonne a filo del bordo sinistro; la sede nella chiusura a sei colonne a filo del bordo destro, con un taglio più largo (995 x 865, sempre senza le auto con le targhe).
- Intro dell'apertura con cinque reparti come il titolo della sezione (carrozzeria, officina e meccatronica, cristalli, grandine, soccorso stradale).
- Menu del telefono: la voce diventa "Chiudi" quando è aperto, senza il riquadro azzurro del tocco.
- `sizes` corretti per le foto tagliate con `object-fit: cover`, così il browser non sceglie mai un file più piccolo della misura mostrata a 1x.

Erano già stati sistemati nel passaggio precedente (verificati): auto vera nella prima schermata al posto della cabina vuota; titolo "Botta? Risposta!" al posto dello slogan generico; pannello Carrozzeria con la mascheratura della Ferrari (1742 px, mai ingrandita) al posto della parete colorimetria; storia e chiusura con impaginazioni diverse; albo della Polizia di Stato al passato ("Nel triennio 2023-2025"); "Certificazione ISO 9001" senza durata; "Centralino. Per i sinistri scegli l'interno Carrozzeria"; logo del piede a 240 px con il motto leggibile; menu del telefono a tutta larghezza; "Hai avuto un incidente?" dentro il paragrafo e non come etichetta sopra il titolo.

## Le prime schermate

1. 1440: testata (scritta del logo, cinque voci, telefono), il trittico. L'auto è larga 400 px su 533 della foto, intera sopra la piega (finisce a 805 px su 900). A 1024 il trittico resta, con il titolo calcolato sulle colonne (86 px). Oltre 1440 la composizione resta centrata nella griglia di 1440.
2. Sotto 900 px: "Botta?" a sinistra e "Risposta!" a destra su due righe, poi la cabina a tutta larghezza (16:10 a 768, quasi quadrata a 390 con l'auto all'82 % della larghezza), poi testo, bottone verde con gli orari e didascalia. A 390 il bottone è dentro la prima schermata (finisce a 814 px su 844).
3. "Cinque reparti, una sede": cinque linguette, la foto del reparto a tutta larghezza, una frase vera, i dettagli, il link e il numero giusto.

Poi: "Dal 1993 in Corso Stati Uniti" (le mani che lucidano una portiera bianca, a filo del bordo sinistro), "Il sinistro, senza anticipi" con i cinque passi numerati perché sono una procedura, la chiusura "Pensiamo a tutto noi" con la sede a filo del bordo destro, il piede.

## Caratteri e colori

- **Archivo** (Google Fonts, SIL Open Font License 1.1, testo in `sito/fonts/OFL.txt`), una sola famiglia variabile servita da `sito/fonts/` (woff2 latin e latin-ext, nessuna chiamata a Google). Titoli a larghezza 75 % e peso 600; testo a 100 % e 400; titoletti dei reparti a 112 % e 500; cifre tabellari per telefoni, orari e dotazione. Riferimento: Thornley Kelham (restauro auto, titoli in Archivo).
- Colori: bianco cabina #EEF1ED, piede #E1E7E1, inchiostro #161714, grigio #5C5E58 (5,8:1 sul fondo, 5,2:1 nel piede), verde del logo #076633 (6,2:1; testo bianco sul bottone 7,1:1) per il bottone e il passaggio sui link, giallo #F2C200 delle loro cabine e dell'ingresso solo come barra sotto la linguetta scelta, mai per il testo.
- Riferimenti: Lanzante (un'auto sola, nitida, molta aria), Touring Superleggera (titolo grande e niente altro), Thornley Kelham (l'officina come luogo bello).

## Interazione

Un solo gesto: le linguette Carrozzeria, Officina, Cristalli, Grandine, Soccorso stradale cambiano di colpo foto, frase e azioni del reparto, senza dissolvenza; Soccorso porta al cellulare 335 5639355. È un vero `tablist`: frecce con giro, Home e Fine, fuoco visibile, tocco. A 390 le linguette stanno su una riga che scorre, con la sfumatura a destra come indizio, e la linguetta scelta viene portata in vista. Le foto degli altri reparti si caricano dopo la pagina. Senza JavaScript i cinque pannelli si vedono in fila. Sotto 900 px il menu è un `details` nativo. Nessuna animazione allo scorrere, nessun effetto sul cursore.

## Foto: origine e licenza

Tutte dell'azienda, dalla libreria media pubblica di serenissimaservice.it (`assets/CREDITI.md`): solo per la proposta e, nel sito vero, con il loro consenso. Nessuna foto di repertorio, nessuna immagine generata.
- Apertura: `2018-09-F480inCabina.jpg` (iPhone 6s, 2196 x 2400), tre tagli: verticale per il computer, 4:3 per il tablet, quasi quadrato per il telefono. La Ferrari è l'auto di un cliente con il marchio visibile: va chiesto il permesso (LEGGIMI).
- Reparti: `2018-09-Mascheratura.jpg`, `2015-04-DSC_0101.jpg` (rossi del pavimento spenti), `2015-04-IMG_1435-1.jpg`, `2019-08-christian.jpg`, `2015-04-IMG_1387.jpg` (mail personale sulla portiera coperta).
- Storia: `2015-04-lucidat.jpg`. Chiusura: `2015-04-ESTERNO.jpg`, cielo desaturato, tagliata a sinistra delle auto in fila.
- Loghi: `logo-2016-03-LOGO-02.png` nel piede (240 px, 1x e 2x), scritta 2022 in testata (162 px, 1x e 2x).
- Trattamento unico (`_prova/script/finale_img.py`): bilanciamento verso il grigio neutro, livelli, moltiplicazione per il bianco cabina, saturazione 0,7-0,9, nitidezza dopo il ridimensionamento.

## Piede

Logo intero e una riga su chi sono; quattro colonne con titoletti (`p` collegati alle `nav` con `aria-labelledby`): Servizi, Per te, Azienda, Seguici (solo Facebook, l'unico social che esiste). Riga legale: Serenissima Service S.r.l., Corso Stati Uniti 19/19-A, 35127 Padova, P.IVA e C.F. 00019100288, Privacy, Cookie. A 390 le colonne si impilano in ordine, separate da un filetto. **Niente newsletter**: nessuna novità periodica (l'ultima news è del 22/02/2024) e i promemoria utili (tagliando, revisione, gomme) vanno legati al veicolo e passano dalla prenotazione, non da una lettera a tutti.

## Controlli (2 novembre)

- Larghezze 320, 360, 390, 414, 600, 768, 900, 1024, 1180, 1280, 1440, 1680, 1920, 2560: scrollWidth uguale a innerWidth ovunque (`_prova/script/finale_controlla.mjs`). Screenshot guardati a pezzi a 1440 e 390, pagine intere a 320, 768, 1024 e 1920, prima schermata a 1280 (`_prova/script/finale_apertura.mjs`).
- Immagini: a DPR 1 nessuna mostrata più grande del file a 320-1920 (misurati i pixel veri del file scelto da `srcset`). A DPR 2 l'apertura è nitida; le foto del 2015 (1920 px all'origine) e la sede restano sotto il 2x a 1440: è il limite delle sorgenti, scritto nel LEGGIMI.
- Linguette: tastiera (frecce con giro, Home, Fine) e tocco a 390, con la riga che porta in vista la linguetta scelta. Menu del telefono aperto a tutta larghezza.
- Collegamenti: `tel:+39049760655` (testata, apertura, carrozzeria, chiusura, menu), `tel:+393355639355` (soccorso, chiusura), `mailto:info@serenissimaservice.it`, indirizzo con il link a Google Maps.
- Segnali da IA (`segnali.sh`): foto 36,2 % della pagina, 9 filetti, nessuna freccia, nessun numero grande con etichetta, una famiglia. Unica soglia segnalata: "titolo in due frasi" per "Botta? Risposta!". È il motto stampato nel loro logo dal 2016, parola per parola, non una formula: lo tengo, con la conferma chiesta nel LEGGIMI. Da guardare: due misure di H2 (68 e 124 px), voluta, perché la chiusura fa eco all'apertura.
- Nessun carattere U+2014 nella pagina, in questa nota e nel LEGGIMI.
