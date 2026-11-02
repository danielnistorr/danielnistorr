# La Termica, home finale: nota

Pagina: `sito/index.html` (statica, nessuna libreria). Rigenera tutto: `sh _prova/script/build_finale.sh` (immagini, caratteri, controlli, screenshot, segnali). Altezza: 5614 px a 1440 piede compreso, 7026 px a 390.

## L'idea

"Rame sui coppi": il cielo della foto diventa la carta della pagina. Da quella carta salgono le tre canne in rame di un loro lavoro in un centro storico, e i tubi orizzontali entrano dal bordo sinistro della finestra e corrono sotto il titolo. Il titolo si appoggia sul primo tubo. Il rame su coppi veneti, con i terminali in fila, è solo loro: con il nome di un concorrente la foto non regge.

## Le prime schermate

- **1440, prima schermata**: testata chiara (logo vero, cinque voci, telefono). La foto prende tutta la larghezza della finestra: i tre terminali arrivano quasi alla testata, i tre tubi in rame escono dal bordo sinistro, sopra di loro c'è solo carta. Nella carta, a sinistra, il titolo in Brygada 1918 a 96 px "Canne fumarie in rame e inox, su misura", la frase loro "Progettiamo con voi l'impianto più adatto", il bottone rame `tel:` e "Venite in showroom". Niente legende, niente numeri: una sola didascalia semplice sotto la foto, allineata al bordo destro.
- **1024 e 1180**: stessa impaginazione; la foto scende di 110 px, così il bottone resta sopra il primo tubo.
- **1920 e 2560**: la foto resta a tutta larghezza e il testo scende con la finestra (`padding-top: max(48px, 42vw - 560px)`), sempre appoggiato sopra il tubo.
- **768**: testo sopra, poi la foto intera a tutta larghezza.
- **390**: titolo a 43 px su tre righe, frase, bottone a tutta misura, poi il taglio verticale della stessa foto (le tre canne verticali e i gomiti). Il bottone "Menu" con `aria-expanded` apre le cinque voci; il telefono resta in testata.

## Sezioni (4 più chiusura e piede)

1. Chi siamo: frase serif e due paragrafi su due colonne (1978, Mario Camporese con i due figli, magazzino con showroom di oltre 500 m², camera di commercio).
2. Servizi: 7 righe a filetti #D9CFC4, tutte uguali (64-95 px a 1440), nome in Brygada 24 px e una riga in Host Grotesk.
3. Lavori ultimati con linguette (Palazzine, Ville, Camini autoportanti). Titolo, linguette e riga di testo stanno in alto, all'altezza dei terminali; la foto, alta 760 px, è a filo del bordo destro. Le tre foto hanno lo stesso trattamento (cielo portato alla carta) e nessuna viene dal cantiere dell'apertura.
4. Materiali e su misura: a sinistra il titolo, la tabella 316L / 304 / Rame / Ovali, "Su misura" e "Pronto Lamiera"; a destra, su 5 colonne (circa 520 px), l'armadio inox di tre quarti scontornato sulla carta, senza ombre disegnate.

## Chiusura e piede

- **Chiusura**: frase loro "Non lasciamo niente al caso" a 84 px, poi "Analizziamo ogni caso nel dettaglio, anche la canna che avete già." Sotto, il telefono grande (`tel:`), l'email (`mailto:`), l'indirizzo con il link a Google Maps e la riga "Magazzino e showroom di oltre 500 m², al dettaglio e all'ingrosso". Niente orari, che non sono pubblici. A destra, a filo del bordo, la loro foto delle tre canne inox con il vapore, alta 640 px, in bianco e nero neutro; il testo è allineato al piede della foto.
- **Piede** su #EAE3D9:
  - logo PNG a 3x con una riga su chi sono;
  - quattro colonne di link: Servizi, Prodotti (le sette voci dell'analisi: Inox doppia parete, Rame, Inox monoparete, Ovali, Pellet e legna, Flessibili, Comignoli e accessori), Su misura, Azienda;
  - il "Promemoria pulizia": campo a filetto, bottone e casella di consenso. Una mail all'anno prima dell'inverno, perché i clienti sono anche privati e la pulizia torna ogni anno. Al clic mostra "Grazie, vi scriveremo prima dell'inverno." (`role="status"`) e non invia niente finché non si collega un servizio;
  - niente "Seguici", perché non esistono profili social;
  - la riga legale: ragione sociale, P.IVA, indirizzo, Privacy, Cookie.
  - A 390 le colonne si aprono a fisarmonica con veri bottoni (`aria-expanded`); un solo titolo `h2` per colonna è visibile a ogni larghezza.

## Caratteri e colori

- **Brygada 1918** (Google Fonts, SIL Open Font License 1.1, uso commerciale libero) per i titoli, le voci dei servizi, i materiali e il telefono grande, in peso 400-500. Cifre tabellari su 316L, 304, 7/10 mm e telefono.
- **Host Grotesk** (Google Fonts, SIL Open Font License 1.1) per il testo, il menu, le didascalie e il piede.
- I file woff2 (latin e latin-ext) sono serviti dalla pagina in `sito/fonts/`.
- Colori: carta #F3EEE7 e piede #EAE3D9; inchiostro #221E1B e testo tenue #5B524A (6,6:1 sulla carta, 6,0:1 sul piede); rame #9A4F2C per il bottone (bianco su rame 5,95:1), il segno della linguetta attiva e "Iscrivimi" (4,67:1 sul piede); il rosso e il giallo del logo stanno solo nel logo.
- Riferimenti: Rheinzink (il metallo sul tetto come architettura) e Wittus (fondo chiaro, un solo oggetto, tanta aria), dalla sezione 7 dell'analisi.

## Interazione

Un solo gesto, le linguette dei lavori: `role="tab"`, frecce sinistra e destra, Home e Fine, tocco sul telefono. Il cambio di foto e di riga è netto, senza dissolvenza; le altre due foto si caricano dopo la pagina. Le transizioni (0,12 s sul colore) ci sono solo su link e bottoni. Niente animazioni allo scorrere, niente effetti che seguono il cursore.

## Foto, origine e trattamento

Tutte le foto e il logo sono di La Termica, presi dal loro sito. Nessuna foto di repertorio, nessuna immagine generata.

| File in `sito/img/` | Origine | Trattamento |
|---|---|---|
| `rame-*`, `rame-v-*` | `CAM00223.jpg`, originale 2592x1944 | cielo, case, chiesa e tetto lontano portati alla carta piena; nessuna sfumatura sul bordo, i tubi escono dal bordo della finestra; curva sulle alte luci del rame, contrasto locale |
| `lav-palazzina-*` | `DSC00639.jpg` | cielo portato alla carta piena; taglio da x 210, il condizionatore resta fuori |
| `lav-ville-*` | `DSC00479.jpg` | cielo azzurro portato alla carta; antenna e cavo sul colmo tolti |
| `lav-traliccio-*` | `DSC03630.jpg` | cielo portato alla carta |
| `armadio-*` | `DSC01936.jpg` | scontornato lungo i sei spigoli del volume, acciaio neutro, nessuna ombra |
| `vapore-*` | `IMG_0099.jpg` | bianco e nero con filtro blu, gradiente del cielo spianato, acciaio neutro (R-B sotto 2), alte luci al tono carta |
| `logo-480.png`, `logo-640.png` | `logo-completo-3000x938.jpg` | fondo reso trasparente con soglia più dura, maschera leggermente rinforzata |

## Cosa è cambiato nella rifinitura (giudizio cieco del 24/10)

- Apertura: tolti la legenda a pallino "Terminale in rame" e il numero "01" con la didascalia in basso a sinistra. La foto è a tutta larghezza, i terminali salgono fino alla testata e il titolo si appoggia sul primo tubo. Tolta la velatura sul bordo sinistro; recuperate in parte le alte luci del rame; cielo riempito di carta piena e WebP a qualità 86.
- Lavori: "Centri storici" (stesso cantiere dell'apertura) sostituita con "Ville" (DSC00479); "Case" diventa "Palazzine", con il condizionatore fuori taglio. Blocco di testo in alto, non più centrato su 840 px. Linguette su una riga a 1024 e 1100.
- Servizi: tolto il cerchio della video ispezione; sette righe uguali.
- Su misura: l'armadio di fronte con l'ombra finta su 8 colonne diventa l'armadio di tre quarti su 5 colonne, senza ombra, a destra della tabella (area circa il 18 % di quella dell'apertura).
- Chiusura: foto rifatta in bianco e nero neutro; altezza 640 px e testo allineato al piede della foto; piede a 80 px.
- Testi: riga "Ovali" riscritta (ovali inox, a catalogo anche alluminati e flessibili); nel piede aggiunti Ovali e Flessibili; nella chiusura la riga sullo showroom, così "Venite in showroom" trova riscontro.
- Piede: un solo `h2` visibile per colonna; il promemoria mostra un messaggio al clic.
- Tolto il `preload` del carattere, che in `file://` dava un errore in console.
- Logo rigenerato a 3x (480 e 640 px).

## Controlli

- Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1100, 1180, 1280, 1440, 1920 e 2560 (`scrollWidth` uguale a `innerWidth`). L'unico elemento fuori finestra è il link "Vai al contenuto", nascosto finché non riceve il fuoco.
- Guardate a pezzi le pagine intere a 1440 e 390, quelle a 320, 768, 1024, 1180 e 1920, la prima schermata a 1024, 1280 e 1440, le linguette a 1440, il menu e la fisarmonica a 390.
- Interazione provata con Playwright (`_prova/script/interazione.mjs`): frecce e Fine sulle linguette a 1440, 1100 e 1024, tocco a 390, linguette sulla stessa riga a tutte le larghezze provate, messaggio del promemoria, fisarmonica, nessun titolo vuoto nel piede, nessun errore in console.
- Collegamenti: `tel:+390499002522` (tre volte), `mailto:info@latermicacamini.com`, mappa Google su "La Termica Via Bologna 6 35035 Mestrino PD".
- Cielo delle foto: tra i pixel quasi carta nessuno scarto visibile con il contrasto amplificato.
- Nessun carattere U+2014 in pagina e nei .md.
- Segnali da IA (`_metodo/kit/segnali.sh`): 0 soglie da correggere su 10, 0 da guardare su 8. Area delle foto al 40,5 %.
- Nessun dato inventato: ogni fatto viene da `01-analisi.md`; i dubbi sono nel LEGGIMI.
