# Plastificazione Bastianello, home finale: nota

Pagina: `sito/index.html` (immagini in `sito/img`, caratteri in `sito/fonts`). Si rifà tutto con `sh _prova/script/build_finale.sh` (astuccio, foto, pagina, screenshot). Base: prototipo A "La finestra", scelto dal giudice (`_prova/giudizio.json`), con gli innesti da B. Il K0 di A era 6: la prima schermata è stata ripensata, non ritoccata.

## L'idea
Il mestiere in un oggetto solo: un astuccio bianco con la finestra, nitido sul fondo carta, disegnato come una tavola tecnica. Tre punti numerati scendono con un filetto sottile fino alla legenda sotto l'oggetto: dove interviene Bastianello (cartoncino, finestra, faccia). Le misure vere diventano disegno: per ogni lavorazione i fogli minimo e massimo in scala, dentro il tratteggio del foglio più grande che lavorano. Tutto color carta, il nero solo dentro le foto di reparto. Con il nome di un concorrente la pagina non regge: formati, film, frasi e foto di reparto sono i loro.

## Le prime due schermate
1. Testata con il logo vero (SVG del sito di oggi), quattro voci, telefono. A sinistra "Nobilitiamo lo stampato" in Archivo largo a 104 px, in basso la riga su cosa fanno e per chi e il bottone rosso "Chiedi un preventivo" con "Fogli fino a 120 x 160 cm", allineati al piede dell'astuccio. A destra l'astuccio (720 px con l'ombra, a filo del margine destro) con i punti 1, 2, 3 collegati da filetti da 1 px (inchiostro al 40 %) alle tre voci della legenda, allineate sotto l'oggetto; "Foto indicativa" in didascalia. A 390: titolo, astuccio alto circa 280 px, quattro righe di testo, bottone entro i primi 844 px, poi la legenda.
2. "Cinque lavorazioni, conto terzi": cinque schede (Finestratura, Plastificazione e accoppiatura, Verniciatura UV, Verniciatura blister, Verniciatura serigrafica). Foto 4:3 a filo del bordo sinistro, a destra nome, frase dai loro testi, varianti e fogli in scala con minimo e massimo.

Poi: la frase grande sul fondo carta "La stampa la fa un altro. Noi la proteggiamo con un film, la facciamo brillare con la vernice, le apriamo una finestra." (Archivo largo, 52 px), sotto la loro foto dei fogli stampati da altri che passano nella verniciatrice serigrafica, a tutta larghezza e senza titolo sopra, con la riga grigia su anni, conto terzi, sede e investimenti; "Per chi fa astucci" con i tre settori in righe con filetti (titolo a sinistra, testo a destra); chiusura con la loro frase "Impegno e volontà a tua completa disposizione", telefono grande con tel:, email con mailto:, indirizzo e link alla mappa, e la foto del loro film olografico a filo del bordo destro, alta quanto il blocco di testo; piede.

Altezza: 5188 px a 1440 con il piede, 5947 px a 390.

## Piede
Fondo #EEEBE5, stesso tono della pagina. Logo vero in SVG con una riga su chi sono; quattro colonne con titoletti brevi: Azienda (Chi siamo, Certificazioni, Chiedi un preventivo), Lavorazioni (i cinque nomi interi), Settori (i tre nomi interi), Contatti (telefono, email scritta per intero, indirizzo con mappa). Riga legale: © 2026 Plastificazione Bastianello S.r.l., P.IVA e C.F. 03124050240, Cap. soc. € 110.000 i.v., Privacy, Cookie. REA e PEC non ci sono: vengono da aggregatori, vanno verificati con la visura. A 390 le colonne si impilano nell'ordine. I link puntano alle pagine del sito nuovo (elenco nel LEGGIMI).
- Niente newsletter: lavorano conto terzi su commessa per cartotecniche e stampatori, non hanno notizie, fiere, cataloghi, collezioni né clienti privati. Al suo posto "Chiedi un preventivo".
- Niente "Seguici": non hanno social, né nel codice del sito né in rete.

## Caratteri e colori
- **Archivo** (Google Fonts, SIL Open Font License 1.1), asse di larghezza: titolo a larghezza 112, H2 e frase grande a 120, peso 400. La forma larga richiama la scritta spaziata PLASTIFICAZIONE / BASTIANELLO del loro logo; nei riferimenti, i titoli grandi e calmi di Derprosa e Progress Packaging.
- **Onest** (Google Fonts, SIL Open Font License 1.1), pesi 400 e 500, per testo, menu, legenda e piede; cifre tabellari per formati e telefono.
- File woff2 serviti dalla pagina in `sito/fonts` (sottoinsieme latino, variabili). La licenza OFL permette di incorporarli e servirli.
- Carta #F6F4F0, piede #EEEBE5, inchiostro #171717, grigio #5B5751, filetti #D8D3CB, rosso del logo #CC3429 solo su bottone, scheda attiva e sottolineatura del telefono. Contrasti: grigio su carta 6,5:1, grigio sul piede 6,0:1, bianco sul rosso 5,1:1, inchiostro su carta 16,3:1.

## Interazione
Un solo gesto: le schede delle lavorazioni. Veri bottoni con ruolo tab, frecce, Home e Fine da tastiera, tocco al dito; il cambio è netto, senza dissolvenze. Cambiano foto, testo e il disegno dei fogli in scala, così il cartotecnico vede subito se il suo formato entra. A 390 il menu si apre con un vero bottone ("Menu" / "Chiudi", aria-expanded, Esc). Nessuna animazione allo scorrere, nessun effetto sul cursore; al passaggio cambiano solo colore o sottolineatura.

## Foto, origine e licenza
Trattamento unico: colori calmati, tono caldo leggero, neri appena sollevati (PIL), WebP in più larghezze con srcset, 1,7 MB in tutto.
- Apertura: astuccio con finestra da Pexels 15807279, Connor Scott McManus (Pexels License). Fotomontaggio indicativo: scontornato e specchiato, tolti il dolce e l'etichetta della pasticceria, finestra ridisegnata vuota con lo spessore del cartoncino, cornice destra ricostruita, ombra nuova. Nessuna IA. Da rifare dal vero.
- Plastificazione: film olografico, Unsplash gOfXb8eW4g8, Emily Bernal (Unsplash License), "foto indicativa" in didascalia.
- Dal loro sito: astucci sotto la finestratrice (`fienstartura-1`), fogli con UV a riserva (`VERNICIATURA-UV`, 990 px, marchio "nathia" di un cliente), cartoncino a gradini (`blister.jpeg`, probabile repertorio, "foto indicativa"), damasco in serigrafia UV ritagliato sul solo motivo a fuoco, senza marchio né scritte (`VERNICIATURA-SERIGRAFICA`), fogli di astucci per biscotti nella verniciatrice serigrafica (`SERIGRAFIA-1`), film olografico sulla plastificatrice (`plastificazione-1`, chiusura).
- Nessuna foto di repertorio già usata in altre home della campagna; la foto della chiusura non compare altrove nella pagina. Le foto di fibbie di Ruan Richard Rodrigues non sono usate.

## Controlli
- Screenshot guardati a pezzi a 1440 e 390, più 320, 768, 1024 e 1920: nessuno scorrimento orizzontale, nessuna sovrapposizione (prova automatica `_prova/script/finale_prova.mjs`, che prova anche schede da tastiera e al tocco e il menu a 390).
- `_metodo/kit/segnali.sh` a 1440: 0 soglie bloccanti su 10. Foto 35 % della pagina, Onest 87,8 % e Archivo 12,2 %, 0 mono, 0 etichette maiuscole, 0 frecce, 7 filetti larghi, 2 fasce di colore (pagina e piede), 1 sezione con titolo a sinistra e testo a destra. Da guardare: due misure di H2 (56 e 72 px, voluto: la chiusura è più grande) e nessuna data in pagina, perché l'unico anno sicuro è quello della srl (2004) e "da oltre 40 anni" va chiarito (LEGGIMI).
- Divieti del committente: niente gradienti, testo in gradiente, emoji, Inter, card con bordo colorato, vetro, scuro a basso contrasto, tre box con icona, badge sopra il titolo, icone Lucide, dissolvenze allo scorrere, effetti sul cursore, bottoni che sbiadiscono, corsivi d'accento. Nessuna lineetta lunga U+2014 in pagina, negli script e nei .md.
- Dati: ogni fatto viene da `01-analisi.md`. Non sono in pagina la BRCGS (certificati pubblicati scaduti), REA e PEC, dipendenti e fatturato, la frase procedurale sul preventivo del prototipo A.
- Fonti dei riferimenti guardati: `riferimenti/` (Derprosa, Burgopak, Progress Packaging, Kurz, Pusterla) e le prime schermate delle home amate della campagna (Mario Agnoletto chiara con le legende, Hambro, FM Sistemi chiara, Tek.Lam). Rispetto ad Agnoletto e Hambro l'oggetto non ha legende sparse attorno: i filetti scendono dritti a una legenda sotto, come in una tavola tecnica.
