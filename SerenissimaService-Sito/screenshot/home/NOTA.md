# Serenissima Service, home finale: nota

Pagina: `sito/index.html` (statica, si apre con file:///). Immagini in `sito/img/` (solo quelle usate, WebP in 2-4 larghezze, loghi PNG a 1x e 2x), caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, pagina da `_prova/script/index.html`, screenshot). Base: prototipo A "La cabina", con le indicazioni del giudice e gli innesti da B.

Altezza: 4802 px a 1440 (piede compreso), 6029 px a 390.

## Idea

La cabina di verniciatura è il cuore di una carrozzeria, e Serenissima ne ha nove. La home si apre dentro una di loro, vuota e in asse: le pareti della cabina hanno lo stesso colore della pagina, quindi la foto esce dalla carta senza un bordo superiore, e l'unico colore oltre al verde del bottone è il giallo del sollevatore, al centro sotto il titolo. Poi la pagina tiene la promessa del loro logo, "Botta? Risposta!": cinque reparti nella stessa sede, la storia dal 1993, il sinistro senza anticipi, "Pensiamo a tutto noi" con la sede.

## Le prime due schermate

1. Testata chiara: scritta del logo, cinque voci, telefono. Titolo loro, da `chi-siamo`: "Ci prendiamo cura di tutto ciò che la tua auto richiede" (Archivo semi espanso 500, 94 px, due righe). Sotto, la riga sui reparti e i 3000 mq a sinistra, il bottone verde "Chiama lo 049 760655" e gli orari a destra. La cabina parte già sotto quella riga: i primi 112 px sfumano nella carta (maschera CSS), le pareti trattate con PIL hanno il colore #F4F2EC della pagina. Il sollevatore giallo è intero sopra la piega (finisce a 861 px su 900), in asse con il centro della pagina. Due legende sole, con filo e pallino, che dicono cosa succede lì dentro: "Una delle 9 cabine di Corso Stati Uniti" sull'apertura di fondo, dove si vede la cabina successiva, e "Verniciatura all'acqua, essiccazione in cabina" sul sollevatore. Oltre 1600 px la foto sfuma anche ai lati.
   A 390: titolo a 40 px su quattro righe, la riga, il bottone con gli orari accanto, poi un taglio verticale della stessa cabina con la sfumatura in alto e il sollevatore intero entro gli 844 px; le legende diventano una didascalia sotto la foto.
2. "Cinque reparti, una sede": cinque linguette, una foto 2,25:1 larga quanto la griglia (1312 x 583 a 1440), una frase vera del reparto, i dettagli, il link e il numero giusto.

Poi: "Dal 1993 in Corso Stati Uniti" (le mani che lucidano una portiera bianca a filo del bordo sinistro; storia, dotazione e prove in un blocco unico allineato in alto alla foto); "Il sinistro, senza anticipi" con la domanda loro "Hai avuto un incidente?" sopra, i cinque passi numerati perché sono una procedura e il modulo CID come link sotto il passo 1; la chiusura; il piede.

## Caratteri e colori

- **Archivo** (Google Fonts, SIL Open Font License 1.1, testo della licenza in `sito/fonts/OFL.txt`), una sola famiglia variabile servita da `sito/fonts/` (woff2 latin e latin-ext, nessuna chiamata a Google). Titoli con l'asse della larghezza a 112 % in peso 500, testo a 100 % in 400, cifre tabellari per telefoni, orari e numeri della dotazione. Riferimento: Thornley Kelham (restauro auto, titoli in Archivo); la versione larga e piena sta accanto al graziato pesante di "SERENISSIMA" nel logo. Due misure di titolo: H1 94 px, chiusura 84 px; tutti gli H2 di sezione a 52 px; spazio tra le sezioni 160 px a 1440.
- Colori: carta #F4F2EC (i pannelli della cabina), piede #EAE7DF, inchiostro #161714, grigio #5C5E58 (6,1:1 sulla carta), verde del logo #076633 (6,7:1) per il bottone e il passaggio sui link, giallo #F2C200 solo come barra sotto la linguetta scelta, mai per il testo. Il nero c'è solo nei titoli.
- Riferimenti: Lanzante (un solo oggetto su un fondo chiaro che sfuma), Touring Superleggera (titolo grande e molta aria prima della foto), Thornley Kelham (l'officina mostrata come un luogo bello). Delle home amate della campagna: la fibbia di Hambro e il tubo di FM Sistemi che si sciolgono nella pagina, le legende di Mario Agnoletto.

## Interazione

Un solo gesto: le linguette Carrozzeria, Officina, Cristalli, Grandine, Soccorso stradale cambiano di colpo foto, frase e azioni del reparto, senza dissolvenza; Soccorso porta al cellulare 335 5639355. È un vero `tablist`: frecce, Home e Fine, fuoco visibile, tocco (provato con `_prova/script/finale_linguette.mjs`). A 390 le linguette stanno su una riga che scorre in orizzontale, con la sfumatura a destra come indizio, e la linguetta scelta viene portata in vista. Le foto degli altri reparti si caricano dopo la pagina. Senza JavaScript i cinque pannelli si vedono in fila. Sotto 900 px il menu è un `details` nativo. Nessuna animazione allo scorrere, nessun effetto sul cursore.

## Foto: origine e licenza

Tutte dell'azienda, scaricate dalla libreria media pubblica di serenissimaservice.it (`assets/CREDITI.md`): si usano solo per la proposta e, nel sito vero, con il loro consenso. Nessuna foto di repertorio, nessuna immagine generata, nessuna didascalia che attribuisce all'azienda una foto non sua.
- Apertura: `2015-04-forniEst5.jpg`, cabina vuota in asse, 1920 px; taglio largo 1600 x 620 e taglio alto 900 x 980 per il telefono.
- Reparti: `2015-04-DSC_0014.jpg` (parete della colorimetria con la scritta "Serenissima Service", tagliata stretta), `2015-04-DSC_0101.jpg` (officina, taglio alto e rossi del pavimento spenti), `2015-04-IMG_1435-1.jpg` (ventosa sul parabrezza), `2019-08-christian.jpg` (levabolli con la lampada a righe), `2015-04-IMG_1387.jpg` (carro attrezzi "Il Socio", con la mail personale sulla portiera coperta dalla vernice della portiera stessa).
- Storia: `2015-04-lucidat.jpg` (due mani che lucidano una portiera bianca; la stampa del fornitore sul guanto attenuata). Ho preferito le mani alle cartelle colore indicate dal giudice: le cartelle anche ritagliate restano fitte e fredde, con il marchio Cromax su ogni cartellino, e la pagina aveva bisogno di una persona al lavoro (K7). Il tunnel forni dello smart repair non ha una foto che regge.
- Chiusura: `2015-04-ESTERNO.jpg`, tagliata sull'insegna e sull'ingresso giallo, cielo desaturato verso un azzurro pallido, targhe sfocate; impaginazione presa da B, foto a filo del bordo sinistro (metà pagina) e testo a destra. Non è la foto dell'apertura né una foto già usata in un'altra home.
- Loghi: `logo-2016-03-LOGO-02.png` nel piede (180 px, PNG a 1x e 2x), `logo-2022-05-Logo-Serenissima-Service-2022-Sticky.png` in testata (162 px, 1x e 2x).
- Trattamento unico ("carta", `_prova/script/finale_img.py`): bilanciamento verso un grigio neutro, livelli, poi moltiplicazione per il colore della carta, così nessun bianco è più chiaro della pagina; saturazione 0,9, nitidezza dopo il ridimensionamento; WebP in più larghezze con `srcset`.

## Piede

Logo intero e una riga su chi sono; quattro colonne con titoletti che non sono titoli (`p` collegati alle `nav` con `aria-labelledby`): Servizi, Per te, Azienda, Seguici (solo Facebook, l'unico social che esiste). Riga legale: Serenissima Service S.r.l., Corso Stati Uniti 19/19-A, 35127 Padova, P.IVA e C.F. 00019100288, Privacy, Cookie. A 390 le colonne si impilano una sotto l'altra in ordine, separate da un filetto, con le voci in riga. **Niente newsletter**: nessuna novità periodica (l'ultima news è del 22/02/2024) e i promemoria utili (tagliando, revisione, gomme) vanno legati al veicolo e passano dalla prenotazione, non da una lettera a tutti.

## Controlli

- Larghezze 320, 390, 768, 1024, 1440, 1920: nessuno scorrimento orizzontale (le linguette a 390 scorrono dentro la loro riga), nessuna sovrapposizione; screenshot guardati a pezzi.
- Segnali da IA (`segnali.sh`): 0 soglie bloccanti; da guardare solo le misure degli H2 (52 e 84 px), voluta: l'unico elemento davvero grande è il titolo d'apertura e la chiusura gli fa eco. Foto 35,6 % della pagina, 9 filetti, nessuna freccia, nessun numero grande con etichetta, una sola famiglia.
- Nessun carattere U+2014 nella pagina e nei file di testo; tel: e mailto: su tutti i recapiti; indirizzo con il link alla mappa.
