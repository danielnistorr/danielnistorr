# La Termica, home finale: nota

Pagina: `sito/index.html` (statica, nessuna libreria). Rigenera tutto: `sh _prova/script/build_finale.sh` (immagini, caratteri, controlli, screenshot, segnali). Altezza: 5799 px a 1440 piede compreso, 6849 px a 390.

## L'idea

"Rame sui coppi": il cielo della foto diventa la carta della pagina e da quella carta salgono le tre canne in rame di un loro lavoro in un centro storico. È il prototipo B scelto dal giudice, con la prima schermata ripensata dentro la stessa direzione (K0 era 6): un solo oggetto, nitido, su fondo pulito. Il rame su coppi veneti, con i terminali in fila, è solo loro: con il nome di un concorrente la foto non regge.

## Le prime due schermate

- **1440, prima schermata**: testata chiara (logo vero, cinque voci, telefono). A sinistra il titolo in Brygada 1918 a 96 px "Canne fumarie in rame e inox, su misura", la frase loro "Progettiamo con voi l'impianto più adatto", il bottone rame `tel:` e "Venite in showroom". A destra, a filo del bordo e ancorata in basso, la foto larga 940 px. Cosa cambia rispetto al prototipo:
  - la foto parte dall'originale a 2592 px scaricato dal sito, non dalla copia a 2000;
  - le case, la chiesa e i comignoli dietro il gomito diventano carta piena, senza velature;
  - a destra della canna più alta il tetto lontano e il comignolo in mattoni diventano carta fino al colmo, così resta solo il rame;
  - i bordi delle canne e del primo tubo orizzontale sono rette stimate sull'immagine: niente alone e niente dentini;
  - resta una sola legenda, "Terminale in rame", rivolta verso la carta; "Comignolo in mattoni" è tolta;
  - la didascalia "01 Tre canne in rame sui coppi di un centro storico. Lavoro La Termica."
- **1440, seconda schermata**: la frase serif accorciata come chiesto ("Vendiamo, installiamo e manteniamo canne fumarie in inox e in rame, con video ispezioni e spazzacamino.") e due paragrafi brevi su due colonne: il 1978 nelle coibentazioni, Mario Camporese con i due figli, il magazzino con showroom di oltre 500 m², l'autorizzazione della camera di commercio. "Da oltre vent'anni" è tolto.
- **390**: titolo a 43 px su tre righe, frase, bottone a tutta misura, poi un taglio verticale della stessa foto (le tre canne verticali e i gomiti, 1166 px di larghezza per 390) con la legenda a destra del terminale più alto. Il bottone "Menu" con `aria-expanded` apre le cinque voci; il telefono resta in testata.

## Sezioni (4 più chiusura e piede)

1. Chi siamo (frase e due colonne).
2. Servizi: 7 righe a filetti #D9CFC4, nome in Brygada 24 px e una riga in Host Grotesk. Il fotogramma della video ispezione è un cerchio di 200 px sulla sua riga. Il cerchio scuro del prototipo con i servizi attorno è tolto.
3. Lavori ultimati con linguette (Case, Centri storici, Camini autoportanti). Titolo, linguette e riga di testo sono un blocco unico, centrato in verticale rispetto alla foto alta 840 px a filo del bordo destro. "Centri storici" ora è tagliata sotto la chiesa: niente bordo frastagliato.
4. Materiali e su misura. L'armadio inox raddrizzato su carta prende il posto del raccordo a T bruciato. Tabella 316L / 304 / Rame / Ovali con le righe riscritte dai loro testi, poi "Su misura" e "Pronto Lamiera".
- La fascia a tutta larghezza del traliccio è tolta: rifaceva la terza linguetta e allungava la pagina oltre i 5800 px.

## Chiusura e piede

- **Chiusura**: frase loro "Non lasciamo niente al caso" a 84 px, poi "Analizziamo ogni caso nel dettaglio, anche la canna che avete già." Sotto, il telefono grande (`tel:`), l'email (`mailto:`) e l'indirizzo con il link a Google Maps. Niente orari, che non esistono, e niente fax, da confermare. A destra, a filo del bordo, la loro foto delle tre canne inox con il vapore (IMG_0099): il cielo azzurro è virato verso la carta e l'acciaio prende un tono caldo. Bologna e San Petronio sono tolti.
- **Piede** su #EAE3D9:
  - logo PNG a 2x con una riga su chi sono;
  - quattro colonne di link: Servizi, Prodotti con le voci vere, Su misura, Azienda;
  - il "Promemoria pulizia", con campo a filetto, bottone e casella di consenso: una mail all'anno prima dell'inverno, perché i clienti sono anche privati e la pulizia torna ogni anno;
  - niente "Seguici", perché non esistono profili social;
  - la riga legale: ragione sociale, P.IVA, indirizzo, Privacy, Cookie.
  - A 390 le colonne si aprono a fisarmonica con veri bottoni (`aria-expanded`).

## Caratteri e colori

- **Brygada 1918** (Google Fonts, SIL Open Font License 1.1, uso commerciale libero) per i titoli, le voci dei servizi, i materiali e il telefono grande, in peso 400-500. È un serif da stampa dritto e solido, come chiede la direzione B. Cifre tabellari su 316L, 304, 7/10 mm e telefono.
- **Host Grotesk** (Google Fonts, SIL Open Font License 1.1) per il testo, il menu, le didascalie e il piede.
- I file woff2 (latin e latin-ext) sono serviti dalla pagina in `sito/fonts/`.
- Colori:
  - carta #F3EEE7 e piede #EAE3D9;
  - inchiostro #221E1B e testo tenue #5B524A: 6,6:1 sulla carta e 6,0:1 sul piede;
  - rame #9A4F2C per il bottone (bianco su rame 5,95:1), il segno della linguetta attiva e "Iscrivimi" (4,67:1 sul piede);
  - il rosso e il giallo del logo stanno solo nel logo.
- Riferimenti: Rheinzink (il metallo sul tetto come architettura, sotto un cielo vero) e Wittus (fondo chiaro, un solo oggetto, tanta aria), dalla sezione 7 dell'analisi. Il registro è quello delle home amate di Mario Agnoletto in chiaro (un pezzo vero con la legenda) e Hambro.

## Interazione

Un solo gesto, le linguette dei lavori: `role="tab"`, frecce sinistra e destra, Home e Fine. Il cambio di foto e di riga è netto, senza dissolvenza. Le altre due foto si caricano dopo la pagina, così il cambio è immediato. Le transizioni (0,12 s sul colore) ci sono solo su link e bottoni. Niente animazioni allo scorrere, niente effetti che seguono il cursore.

## Foto, origine e licenza

Tutte le foto e il logo sono di La Termica, presi dal loro sito (libreria media di WordPress). Nella home non c'è nessuna foto di repertorio e nessuna immagine generata.

| File in `sito/img/` | Origine | Trattamento |
|---|---|---|
| `rame-*`, `rame-v-*` | `CAM00223.jpg`, originale 2592x1944 | cielo, case, chiesa e tetto lontano portati alla carta; bordi delle canne su rette; ritaglio largo e verticale |
| `lav-palazzina-*` | `DSC00639.jpg` | cielo e azzurro tra le foglie portati alla carta |
| `lav-centro-*` | `CAM00226.jpg` | taglio sotto la chiesa |
| `lav-traliccio-*` | `DSC03630.jpg` | cielo portato alla carta |
| `ispezione-*` | `Immagine-077.jpg` | ritaglio quadrato, cerchio in CSS |
| `armadio-*` | `DSC01934.jpg` | raddrizzato, acciaio quasi neutro, posato sulla carta |
| `vapore-*` | `IMG_0099.jpg` | riduzione del rumore, cielo virato verso la carta, viraggio caldo |
| `logo-400.png`, `logo-600.png` | `logo-completo-3000x938.jpg` | fondo bianco reso trasparente |

Le foto sono di telefoni e compatte del 2014: vanno rifatte dal vero (elenco nel LEGGIMI).

## Controlli

- Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1440 e 1920. L'unico elemento fuori finestra è il link "Vai al contenuto", nascosto finché non riceve il fuoco.
- Le pagine intere a 1440 e 390 e quelle a 320, 768, 1024 e 1920 sono state guardate a pezzi, insieme alle tre linguette a 1440 e al menu e alla fisarmonica a 390.
- Nessun carattere U+2014 in pagina e nei .md.
- Segnali da IA (`_metodo/kit/segnali.sh`): 0 soglie da correggere su 10, 0 da guardare su 8. L'area delle foto è al 35,2 %.
- Nessun dato inventato: ogni fatto viene da `01-analisi.md`; i dubbi sono nel LEGGIMI.
