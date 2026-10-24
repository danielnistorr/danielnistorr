# Zeta S.r.l., home finale "Cristal": nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini, caratteri, screenshot, collaudo, segnali). Parte dal prototipo A scelto dal giudice, con le sue indicazioni applicate e gli innesti presi da B.

Screenshot in questa cartella: `home-1440.jpg` (5023 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (6793 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`.

## L'idea

Un pezzo vero di Zeta, il loro raccoglitore campionario in PVC blu goffrato, posato grande e quasi di piatto su carta chiara, sotto il loro motto scritto su una riga sola da margine a margine. Una sola legenda indica la cosa che fa il mestiere: il bordo saldato ad alta frequenza. Il resto della pagina resta sulla stessa carta: il colore pieno viene solo dagli oggetti, il verde Zeta solo da logo, bottone, linguetta attiva e date. Tutte le foto della pagina sono di Zeta: nessuna foto d'archivio.

## Le prime due schermate

- **1440, prima schermata**: testata leggera (logo vero, quattro voci, telefono). "Diamo forma alle vostre idee" su una riga da 64 a 1376 px (108 px, General Sans 500). Sotto, il raccoglitore parte dal centro della pagina ed esce dal bordo destro e dal fondo della schermata, tagliato dalla piega. Sul bordo alto della copertina una sola legenda con filo corto: "Bordo saldato ad alta frequenza", e sotto in grigio "Raccoglitore campionario in PVC goffrato". In basso a sinistra, nell'aria libera, la riga su cosa fanno, il bottone "Chiedete un preventivo" (mailto) e il telefono. Il fondo ha una luce morbida che si spegne prima del bordo: nessuno scalino a 900 px.
- **1440, seconda schermata**: "Su misura, dal raccoglitore alla busta", la frase sul campione che vi rendiamo, e le sei famiglie di articoli solo testo, con filetto sopra, in tre colonne, note in #4E5550 su al massimo due righe (formati e goffrature, robot che sigillano i cartoncini, molla 3 o 6 mm, libri dizionari e agende, cartoncino da 200 g/m², vinile da 100 a 300 micron). Poi per chi lavorano, con "compagnie di assicurazione" come nel loro testo.
- **390**: logo, telefono e un vero bottone "Menu" (si chiude anche con Esc). Titolo su due righe a 53 px, raccoglitore a tutta larghezza che esce a destra, la legenda come didascalia sotto, poi la riga, il bottone e il telefono: tutto entro 844 px (fine a 809 px).
- Poi: Materiali (il gesto), Storia (1969, 1986, 1994, 2015 e la foto vera di reparto), chiusura "b con foto", piede.

Rispetto al prototipo: via le tre legende numerate e lo schema di Agnoletto e Area Systems (titolo in alto a sinistra su due righe con l'oggetto in diagonale accanto); via le tre foto d'archivio del selettore e la pila di raccoglitori bianchi della chiusura; "cataloghi" sostituito da "libri, dizionari e agende"; riquadro del selettore in 4:3.

## Caratteri e colori

- **General Sans** 500 per titoli e linguette, **Switzer** 400 e 500 per testo, numeri, menu e piede. Tutte e due di Indian Type Foundry su Fontshare, **ITF Free Font License** (uso commerciale gratuito, anche sul web); i woff2 sono serviti dalla pagina da `sito/fonts/` (tre file, 59 kB in tutto).
- Perché due famiglie: General Sans non ha cifre tabellari, Switzer sì (`font-variant-numeric: tabular-nums`), così micron, millimetri, grammature, date e telefono stanno in colonna. General Sans fa solo i titoli (10,4 % del testo).
- Riferimenti: Kartell e Fedrigoni per il titolo grande grottesco, con poche parole accanto alla materia; Smythson e LAMY per l'oggetto di cancelleria solo, nitido su fondo pulito, col colore che viene dal prodotto; dalle home amate della campagna (Mario Agnoletto chiaro, Hambro) il pezzo vero, grande, con una legenda e tanta aria.
- Colori: carta #F7F6F2, piano delle foto del selettore #EDEBE5, piede #EFEDE7, inchiostro #14201A, verde Zeta #0A6B42 (dal logo), note e titoletti del piede #4E5550. Contrasti: note 7,1:1 sulla carta e 6,6:1 sul piede; bianco sul bottone verde 6,6:1; verde delle date sulla carta 6,1:1.

## Interazione

Un solo gesto: il selettore "Materiale" con tre linguette vere (ruolo tablist): Colorato, Cristal, Opaco. Cambia di netto la foto, la didascalia, il titoletto e la riga sotto; frecce, Home e Fine da tastiera, e col dito. Le altre due foto si precaricano dopo la prima. Niente animazioni allo scorrere, niente effetti sul cursore: al passaggio cambia solo il colore di link e linguette.

## Foto: origine e licenza

Tutte foto di Zeta S.r.l., scaricate dal loro sito (`assets/originali/`), usate come materiale loro per la proposta. Nessuna foto esterna, nessuna immagine generata dall'IA. Trattamento comune con PIL: scontorno su piano chiaro con ombra corta e lunga rifatta per i prodotti, curva morbida e tono appena caldo per le foto di reparto; WebP in più larghezze con srcset (script `_prova/script/finale_img.py`).

| In pagina | File sorgente | Lavorazione | Larghezze |
|---|---|---|---|
| Apertura | `2019_12_couvette-campionario-1.jpg` (5456 px) | scontornato, scritta della copertina tolta, interno schiarito, specchiato, ruotato di 7 gradi, ombre rifatte, trasparenza | 800, 1200, 1800, 2600 |
| Materiali, Colorato | stesso raccoglitore | primo piano del bordo saldato posato su #EDEBE5 (non sul grigio scuro di B) | 700, 1050, 1400 |
| Materiali, Cristal | `2019_12_porta-campioni-1.jpg` (5456 px) | scontornato dal nero, posato su #EDEBE5, taglio dentro l'oggetto | 700, 1050, 1400 |
| Materiali, Opaco | `2019_12_cartella-campionario.jpg` (1200 px) | scontornato dal nero, posato su #EDEBE5 | 700, 1050 |
| Storia | `2023_02_LAVORAZIONE-PLASTICA-RICICLATA.jpg` (1024 px) | curva leggera | 640, 1024 |
| Chiusura | `2023_02_BUSTE-PVC-SU-MISURA.jpg` (1200x500) | taglio 4:3 sull'uomo e sulle mani, curva leggera | 480, 667 |
| Logo | `logo-zeta-2268x1098.png` | ritagliato, WebP a 1x e 2x (300 e 600 px); non ricostruito in SVG | 300, 600 |

La foto della chiusura non compare altrove nella pagina e non è usata in altre home della campagna (è una foto loro). Nessuna didascalia "Foto indicativa": sono tutti oggetti e reparti veri.

## Il piede

Logo vero e una riga su chi sono; colonne Azienda (Chi siamo, Storia, Ecosostenibilità, PVC Bio), Prodotti (sette categorie vere con i loro indirizzi), Contatti (telefono con tel:, email con mailto:, indirizzo con il link alla mappa, orari), Seguici (solo LinkedIn, l'unico social che esiste) e Lingua (Italiano come lingua corrente con aria-current, poi i domini .co.uk, .fr, .de, .es). Titoletti in maiuscolo piccolo a 6,6:1. In fondo: ZETA S.r.l., indirizzo, P.IVA e C.F. 00220030282, Registro Imprese di Padova, capitale sociale 51.480 euro i.v., Privacy, Cookie. A 390 le colonne si impilano in ordine (Azienda e Prodotti affiancate, poi Contatti, Seguici e Lingua).

**Niente newsletter**: Zeta lavora su commessa per aziende, non ha notizie (la pagina news è vuota), né fiere, cataloghi scaricabili o collezioni; le novità vere arrivano una volta l'anno e LinkedIn basta.

## Controlli

- Screenshot guardati a pezzi a 1440 e 390, più 320, 768, 1024, 1366 e 1920: nessuno scorrimento orizzontale (collaudo `_prova/script/collaudo.mjs`), nessun testo sovrapposto né fuori finestra, a 1920 il titolo resta su una riga e il raccoglitore esce dal fondo.
- Linguette provate col clic e con freccia destra e Home; menu del telefono aperto, chiuso con Esc.
- Altezza a 1440: 5023 px piede compreso.
- Nessun carattere U+2014 nella pagina, negli script e nei .md.
- Segnali da IA (`segnali.sh`): 17 soglie su 18 OK (nessuna etichetta sopra i titoli, nessuna freccia, nessun numero grande con etichetta, tre misure di H2, due famiglie con ruoli fissi, 13 filetti, nessun titolo nero). Resta sotto soglia l'area foto: 26,6 % contro 35 %. È il caso previsto dal metodo per le aziende che non hanno foto grandi: le foto vere di Zeta più larghe con persone e reparti sono di 1024-1200 px, e il giudice ha chiesto di tenere le sei famiglie solo testo e il riquadro del selettore in 4:3. Si sale sopra il 35 % con gli originali del servizio 2023 e con lo still life chiesto nel LEGGIMI (foto di reparto a metà schermo e a filo).
- Nessuno dei divieti del committente: niente gradienti viola, niente card, niente icone, niente badge, niente dissolvenze, niente corsivi d'accento.
