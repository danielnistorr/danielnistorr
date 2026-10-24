# Home finale Ciesseci (CSC Factory): "Il segno sul capo"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `build_img.py`, carattere, screenshot con `shots.mjs`); il collaudo è `_prova/script/prova_finale.mjs`. Pagina alta 5911 px a 1440 (piede compreso), 7730 px a 390.

Base: il prototipo A scelto dal giudice (Archivo, carta, inchiostro e verde, schede delle tecniche, chiusura, piede). L'ultima rifinitura risponde al giudizio cieco in `_prova/cieco.json`.

## Idea

Il mestiere di Ciesseci è mettere un segno su un capo. La prima schermata mostra il capo prima del segno: una maglietta bianca intera, grande, al centro, sotto il titolo loro "Stampa e ricamo: diffondiamo il tuo brand." Il titolo dice il segno, il capo è il supporto. Il resto della pagina mostra il segno vero: le cinque lavorazioni, il loro showroom, la loro felpa con il 1982 stampato come un numero di maglia, la loro sede.

## Cosa è cambiato in questa rifinitura

- **Apertura rifatta** (bloccanti 1 e 2). Tolto il ritaglio della felpa (421 px, già tagliato nel file, mostrato a 1:1 e morbido). Ora c'è un capo intero: una maglietta bianca stesa piana e ripresa dall'alto (Pexels, segnaposto dichiarato nel LEGGIMI), sorgente 3800 px, esportata a 1400 px e mostrata a 680 px a 1440 (2,06 pixel del file per pixel CSS), 560 px a 768 (2,5), 366 px a 390 (2,7, file da 1000 px). La maglietta prende circa il 44 % della larghezza a 1440 ed è intera nella prima schermata, orlo e ombra compresi. Impianto nuovo: titolo centrato in due righe sopra, capo al centro, a sinistra le due righe di presentazione e a destra preventivo e telefono, allineati a metà del capo. Non è più "titolo a sinistra, scontorno a destra" come in Innovatex e Hambro.
- **Nessun taglio dritto sul capo** (importante 3). La maglietta non è scontornata: lo script stima il fondo grigio della foto con una superficie polinomiale sui pixel lontani dal capo, lo divide via e lo porta esattamente al colore carta #F4F3EF. La maglietta tiene la sua ombra vera e l'immagine finisce sulla carta senza bordi.
- **Didascalia dell'apertura tolta** (minore 4): il capo si spiega da solo. La felpa 82 è scesa nella sezione 1982, in un dettaglio di 421 px accanto al numero grande (sorgente 900 px), con la didascalia "La felpa CSC Factory. Il 1982 stampato come un numero di maglia." allineata sotto la foto.
- **768 e 1024** (importante 5, minore 10): tra 561 e 1100 px il capo sta al centro (al massimo 620 px), testo e azioni sotto su due colonne; nessun vuoto grande. Nella sezione 1982 la frase e la felpa stanno accanto al numero fino a 861 px.
- **Scheda Incisione laser** (importante 6): la foto loro della macchina era larga 1024 px e a tutta larghezza si ingrandiva 1,4x. Sostituita con un segnaposto Pexels di 2400 px (testa laser su legno); quella vera va rifatta (LEGGIMI). Tutte e cinque le schede ora sono in 2:1 con sorgenti da 1440 a 2400 px: a 1440 nessuna è ingrandita. Il palco delle schede si ferma a 1680 px sugli schermi molto larghi.
- **Chiusura** (importante 7): ora c'è la facciata di Via Zanella con l'insegna (foto loro, 1020 px) in 3:2, mostrata a 793 x 528 a 1440: nessun ingrandimento, niente parete dei marchi.
- **Sezione abbigliamento** (importante 8): via i caschi e i gilet di repertorio (Paquet). Ora c'è lo showroom loro del 2019, ritagliato in 4:5 sulla giacca verde, i capi e le magliette stampate in vetrina (544 x 680), mostrato al massimo a 544 px, mai ingrandito.
- **Piede** (minore 9): Seguici è diventata la quarta colonna (Lavorazioni, Abbigliamento, Azienda, Seguici); la newsletter è una riga a sé sotto, testo a sinistra e campo a destra. La riga legale non spezza più le voci (ogni voce in `nowrap`, separate da spazio e non da puntini, così a capo non resta un puntino in testa alla riga).
- **Newsletter** (minore 11): all'invio controlla email e consenso e scrive in una zona `aria-live` "Modulo dimostrativo: non ancora collegato al servizio di invio."
- **Preload del carattere tolto** (minore 12): su file:// la console ora è senza errori.
- **Schede, testi** (minore 13): un'etichetta sola "Su cosa", a 14 px nel colore #4A4C47; tolta la coda "Cinque, da vicino:". Per la Sublimazione, al posto di "Colori", "Tessuto: la stampa entra nella tinta. Non ci sono limiti di colore." (dalle loro frasi).

## Caratteri e colori

- Una famiglia: **Archivo** (Omnibus-Type, Google Fonts), variabile in peso e larghezza, servita dalla pagina in `sito/fonts/archivo-latin-var.woff2` (sottoinsieme latino, 90 KB). Licenza SIL Open Font License 1.1, uso commerciale libero; il testo è in `sito/fonts/OFL-Archivo.txt`.
- Titoli larghi (wdth 112-118, peso 460-560, spaziatura da -0,02 a -0,03em) come le lettere della coccarda CSC; etichette strette e maiuscole (wdth 68) solo nella testata e nei titoletti del piede, come "FACTORY" sotto il logo; testo a wdth 100; cifre tabellari per telefoni, orari, date, "50 mm", "1982". Niente corsivi.
- Riferimenti: Stanley/Stella per il tono (il capo basico trattato come un prodotto di valore, titolo grande e pulito); Hand & Lock per l'idea che un solo capo fotografato bene basta in apertura.
- Colori: carta #F4F3EF, piede #EAE8E2, inchiostro #151714, testo secondario #4A4C47 (8,1:1 su carta, 7,4:1 sul piede), didascalie #5C5E58 (6,1:1 su carta, 5,6:1 sul piede), verde del logo #0B6B35 per bottone, link e scheda attiva (6,1:1; testo carta sul verde 6,1:1). Il verde fluo solo nella foto della felpa, il verde chiaro solo nel logo.

## Interazione

Le cinque schede delle lavorazioni sono veri bottoni con ruolo tab: al clic o al tocco cambiano di netto foto, frase e supporti, senza dissolvenze; i pannelli hanno la stessa altezza, così la pagina sotto non salta. Da tastiera: Tab entra sulla scheda attiva, frecce destra e sinistra con ritorno all'inizio, Home e Fine; un altro Tab esce sul link del pannello; il fuoco è visibile. Il menu si apre con un bottone sotto i 1100 px. Nessuna animazione allo scorrere, nessun effetto che segue il cursore.

## Foto: origine e licenza

Trattamento unico: a colori, luci portate al colore carta, neri all'inchiostro, saturazione appena ridotta (0,88-0,9); la felpa tiene il fluo pieno. Esportate in più larghezze con srcset (`_prova/script/build_img.py`); il capo dell'apertura con `picture` (1400 px sopra i 560 px, 1000 px sotto).

| In pagina | File | Origine | Licenza |
|---|---|---|---|
| Apertura, maglietta bianca | `img/capo-1400.jpg`, `-1000.jpg` | Mr. Mockup, Pexels 12025472 (segnaposto): fondo stimato e portato al colore carta, ombra vera | Pexels License |
| Scheda Ricamo, coni di filo | `img/tec-ricamo-*.jpg` | PJ Wallace, Unsplash KAMaLRggG9g (segnaposto), scritte del marchio dei fili tolte | Unsplash License |
| Scheda Serigrafia, telaio alla finestra | `img/tec-serigrafia-*.jpg` | emarts, Unsplash ZCTh4f4mv18 (segnaposto) | Unsplash License |
| Scheda Sublimazione, maglietta sulla pressa | `img/tec-sublimazione-*.jpg` | Compagnons, Unsplash EY0BPl2rpME (segnaposto), etichetta tolta | Unsplash License |
| Scheda Stampa UV, plexiglass stampati | `img/tec-stampa-uv-*.jpg` | Ciesseci, `2019-10-sld-stampe-plexiglass.jpg` | materiale del cliente |
| Scheda Incisione laser | `img/tec-laser-*.jpg` | Sóc Năng Động, Pexels 38030790 (segnaposto) | Pexels License |
| Abbigliamento, showroom | `img/showroom-544.jpg`, `-400.jpg` | Ciesseci, `2019-02-ciesseci-nuova-sede-2.jpg`, ritaglio 4:5 | materiale del cliente |
| 1982, la felpa 82 da vicino | `img/felpa82-900.jpg`, `-640.jpg` | Ciesseci, `2018-02-csc-factory-14.jpg` | materiale del cliente |
| Chiusura, facciata di Via Zanella | `img/sede-1020.jpg`, `-700.jpg` | Ciesseci, `2022-04-sede-nuova-1.jpg` | materiale del cliente |
| Logo | `img/logo-csc-128.png`, `-240.png` (2x) | Ciesseci, `logo-badge-500x486.png` | marchio del cliente |

Nessuna immagine generata dall'IA. Le due foto Pexels nuove sono controllate contro `_prova/usate-campagna.txt` e i `CREDITI.md` delle altre home della campagna: nessuna ripetuta.

## Chiusura e piede

- Chiusura "b con foto": "Ti aspettiamo a Mestrino" (frase loro dalla home), testo a sinistra, facciata fino al bordo destro; telefono grande `tel:+39049634423`, cellulare `tel:+393278831747` e WhatsApp, email `mailto:info@ciessecisrl.it`, indirizzo con "Apri la mappa" (Google Maps, ricerca di Via Zanella 1, 35035 Mestrino PD), orari. Nessun riquadro, nessuna tabella.
- Piede su #EAE8E2: logo PNG a 2x con una riga su chi sono e i recapiti; colonne Lavorazioni, Abbigliamento, Azienda, Seguici (i quattro profili veri, come parole); sotto, la newsletter "Novità e promozioni" (email, bottone, consenso; dimostrativa finché non si collega un servizio, vedi LEGGIMI); riga legale CIESSECI SRL, sede legale Via Cavour 8 Rubano, P.IVA e C.F. 03866700283, REA PD-343821, capitale sociale 10.200,00 €, Privacy, Cookie. A 1024 le quattro colonne stanno in una riga; a 768 due per riga; a 390 si impilano in ordine.

## Controlli (24/10/2026, dopo la rifinitura)

- Screenshot guardati a pezzi: 1440 (prima schermata e pagina intera), 390, 320, 768, 1024, 1920.
- `scrollWidth` uguale a `innerWidth` da 320 a 2560 px (passo 20 px fino a 1500, poi 80): nessuno scorrimento orizzontale.
- Schede provate con clic (le cinque), tocco a 390 (tre), tastiera (Tab, frecce con ritorno, Home, Fine, uscita con Tab): `aria-selected`, pannello visibile e altezza della pagina corretti. Menu al tocco a 390: si apre, `aria-expanded` giusto.
- Newsletter: vuota, senza consenso, completa; tre risposte giuste, la pagina non cambia.
- Link: `tel:+39049634423` in tre punti, `tel:+393278831747`, WhatsApp, `mailto:info@ciessecisrl.it`, mappa.
- Console senza errori su file://.
- Foto (pixel del file per pixel di schermo, schermo 1x): a 1440 nessuna sotto 1 (capo 2,06, schede 1,00, showroom 1,02, felpa 1,52, facciata 1,29); a 1024, 768 e 390 nessuna sotto 1. Sugli schermi 2x restano sotto 1 le foto loro da 1024 px (showroom, facciata) e le schede a tutta larghezza (sorgenti da 1680 a 2400 px per 2880 px di schermo): vanno rifatte dal vero (LEGGIMI). A 1920 la facciata è a 0,99.
- Nessun U+2014 nella pagina, negli script, nella NOTA e nel LEGGIMI.
- Strumento dei segnali (`kit/segnali.sh`, home a 1440): 17 soglie su 18 OK. Da correggere: area foto 28,8 % (soglia 35 %). Non la forzo: le foto loro sono di 1024 px e il giudice ha chiesto di non ingrandirne nessuna e di ridurre i segnaposto fuori dalle schede; l'apertura è un capo su carta, che è la ricetta del committente (un oggetto, tanta aria). Con gli scatti veri (LEGGIMI) showroom e facciata potranno crescere. Da guardare: due misure di H2 (58 e 66 px), lasciate così. Nessun gradiente, nessun badge sopra il titolo, nessuna icona, nessuna card, nessuna dissolvenza allo scorrere.
- Altezza a 1440: 5911 px, dentro 4500-7000.
