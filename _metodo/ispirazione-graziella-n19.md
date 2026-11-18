# Ispirazione: Pelletteria Graziella e Studio N19

Due siti indicati dal committente "come eventuale ispirazione di tipologia di design". Il committente ha precisato che
**non vanno replicati su tutti i siti**: servono a capire il registro per i soggetti di moda o di fascia alta, e anche lì
sono una valutazione da fare caso per caso, non una regola.

- https://www.pelletteriagraziella.com/ (pelletteria conto terzi per marchi di moda, Veneto; sito fatto da Studio N19)
- https://www.studion19.it/ (agenzia di comunicazione, Fiesso d'Artico)

Sono tutti e due siti Wix (Thunderbolt), stesso autore: si vede nelle scelte comuni (menu a tutta pagina, etichette minuscole,
caratteri Helvetica di Wix, effetti di comparsa di Wix).

## Come sono state fatte le prove (19/10/2026)

- Chromium senza interfaccia, banner cookie rifiutato, finestre 1440 x 900 e 390 x 844 (mobile, touch).
- Home e due pagine interne ciascuno: Graziella `history-pelletteriagraziella` e `product-pelletteriagraziella`,
  N19 `servizi` e `contatti`.
- In `_metodo/ispirazione/`, solo JPEG qualità 80:
  - `*-prima.jpg`: prima schermata dopo il caricamento;
  - `*-intera.jpg`: cattura a pagina intera di Chromium. **Su questi siti inganna**: i blocchi che compaiono allo scorrere
    restano invisibili, quindi in `n19-home-1440-intera.jpg` ci sono fasce bianche vuote che dal vivo non lo sono;
  - `*-scorsa.jpg`: la pagina scorsa una finestra alla volta, con 1,6 s di attesa a ogni passo, e poi ricucita. È la più
    fedele. Ha due difetti: qualche giunta doppia, dove una foto si stava ancora muovendo, e il riquadro fisso
    "Privacy Policy / Cookie Policy" di N19 che si ripete a ogni passo;
  - `graziella-menu-1440.jpg`, `n19-menu-1440.jpg`: il menu aperto;
  - `n19-hover-galleria-1440.jpg`: galleria con il mouse sopra una foto; `graziella-hover-marchi-1440.jpg`: l'elenco dei marchi.
- Misurati dal codice: caratteri calcolati (famiglia, peso, misura, interlinea, spaziatura), colori del testo e dei fondi,
  posizione e misura di ogni immagine, sezioni, parole. Movimenti: stato di opacità, filtro, trasformazione e ritaglio di ogni
  elemento visibile subito all'arrivo e dopo 1,6 s; posizioni prima e dopo lo spostamento del mouse in tre punti; prima
  schermata fotografata a 0,3 / 1 / 2 / 3,5 / 6 s dal caricamento.
- I caratteri caricati da Graziella come file utente (`wfont_...`) sono stati riconosciuti scaricando i file e leggendo la
  tabella dei nomi.
- Limite: il Chromium di prova non riproduce i video mp4 (H.264): i video di sfondo si vedono come immagine di attesa o vuoti.

Le misure in px sono a 1440. Wix qui scala tutto in proporzione alla larghezza (misura di progetto x 1440/1280): il titolo
della home di Graziella è 70 px nel progetto e 78,75 px a 1440.

---

## 1. Pelletteria Graziella

### Prima schermata (`graziella-home-1440-prima.jpg`)
Tutto su fondo nero pieno `#000000`. Testata alta 145 px, trasparente e non fissa: a sinistra il marchio (monogramma PG,
"Pelletteria Graziella", "DAL 1986 MADE IN ITALY"), al centro due righe minuscole "Based in / Venice, Italy" e
"Contact / mail / Tel" in Helvetica Light 10 px, a destra solo l'icona del menu. Sotto, a destra, un lettore audio "the sound of
our work" (play, barra, scarabocchio a mano). Il titolo occupa la metà sinistra a x 79: "We develop and produce high-quality
leather goods for luxury fashion brands." su cinque righe, serif leggero a 78,75 px con interlinea 0,9, parole alterne in
bianco e in grigio `#6E6E6E`, quattro parole in corsivo. Un filetto bianco orizzontale (x 534-794) entra nel titolo. Sotto,
"MADE IN ITALY" in Helvetica Bold 13,5 px. A destra una foto di prodotto (borsa Wandler su tavolo chiaro) 750 x 391,
che parte a y 511 ed è tagliata dal bordo della finestra. A sinistra in basso "SCROLL DOWN" verticale con una linea.
**Per i primi 3,5 s la pagina è nera**: si vedono solo marchio, menu e lettore; titolo e foto arrivano dopo (prova a 0,3 / 1 / 2 /
3,5 / 6 s).

### Le prime tre schermate (`graziella-home-1440-scorsa.jpg`)
1. Titolo e foto come sopra.
2. "we are" + filetto corto a sinistra; nella metà destra (da x 773) un paragrafo serif a 33,75 px in bianco, grigio e
   corsivo, poi un paragrafo serif 22,5 px con interlinea 1,0 (fitto). Poi una banda fotografica 1395 x 702 (margini 23 px)
   con una foto molto sfocata dello stabilimento in grigio e la frase "Made in Veneto. Made with passion." sopra.
3. "our works" a sinistra e una frase tra virgolette a destra in 10 px; al centro i nomi dei marchi clienti composti come testo
   (Wandler, Coperni, RSVP, Ateliers Auguste, Advene, Joseph, Frenzlauer, Nanushka, Mouliebre) in serif 52 px, centrati,
   uno per riga, con uno scarabocchio "click here". Nel codice ci sono le foto dei marchi, sparse, che a schermo non si
   vedono: probabilmente compaiono al passaggio, non verificato.

Poi: "We offer a complete, tailor-made service" (serif 39 px) con tre video/foto di lavorazione sfalsati; banda 1395 x 720 di
lavorazione (guanti bianchi, borse appese) con testo sopra; "our services" con quattro righe separate da filetti
(titolo serif 56 px, una riga di descrizione in Helvetica Light 16 px); macro della cucitura 1025 x 526 accanto a una
miniatura 266 x 307 allineata in alto; foto editoriale (modella con borsa) 720 x 877 attaccata al bordo sinistro, testo
allineato a destra nell'altra metà; "Reach Out" a 112 px; piede con i dati societari completi (ragione sociale, sede, P.IVA,
REA, capitale, PEC, whistleblowing) a 11 px.

### Pagine interne
- `graziella-history-1440-scorsa.jpg`: una frase d'apertura serif 33 px a sinistra, "1980" a destra; banda in bianco e nero
  di cartamodelli appesi a tutta larghezza; cronologia a righe (anno in serif 22 px, 3-5 righe di Helvetica 11 px, foto
  orizzontale 375 x 155 a destra) per 1980, 2000, 2010, 2021, 2025; i due titolari in bianco e nero affiancati con i nomi
  ai lati; "factory" con testo su energia e stabilimento.
- `graziella-products-1440-scorsa.jpg`: stesso titolo della home su una riga lunga con filetto; poi una galleria a mosaico
  larga 896 px spostata a destra (x 466-1362), con la colonna sinistra vuota tranne una frase verticale; 2-3 foto per riga,
  4 px tra le foto, 26 foto, pagina lunga 12.254 px. Alcune foto hanno una didascalia in un carattere diverso (quello della
  galleria Wix).
- Mobile (`graziella-home-390-scorsa.jpg`): titolo serif 50 px, poi tutto in colonna; a 390 molti pezzi si sovrappongono
  (testo sopra le foto della lavorazione, frasi tagliate), un bottone tondo "torna su" fisso copre il contenuto.

### Caratteri (dal codice)
| ruolo | famiglia | peso | misura / interlinea a 1440 | note |
|---|---|---|---|---|
| titoli, testo d'apertura | Awesome Serif Light (file utente `c2c2f7_ffbada...`, Nicky Laatz, 2022, a pagamento) | 300 | 112,5/101 · 78,75/70,9 · 39,4/35,4 · 33,75/30,4 · 22,5/22,5 | interlinea 0,9-1,0, spaziatura normale |
| parole d'accento | Awesome Serif Italic Light (`c2c2f7_93ddd...`) | 300 | come sopra | corsivo dentro il titolo |
| voci dei servizi | Awesome Serif Regular (`279e2d_dd32da...`) | 400 | 56,25/84,4 | |
| testo, etichette | Helvetica W01 Light (Wix) | 400 | 16/25,6 · 13,5 · 11,25/11,25 · 10,1/10,1 | spaziatura -0,04 em |
| piccole maiuscole | Helvetica W01 Bold (Wix) | 400 | 13,5/13,5 · 10,1 | "MADE IN ITALY" |

Caricati ma non usati: Cormorant Garamond, Madefor, DIN Next (resti del modello Wix).

### Colori
Fondo `#000000` su tutta la pagina, testo `#FFFFFF`, secondo tono `#6E6E6E` (parole spente nei titoli, crediti). Nessun
colore d'accento: il colore lo portano le foto (cuoio, cammello, marrone). Nei bottoni solo bordo bianco 1 px, angoli tondi.

### Griglia e margini
Nessuna griglia a colonne regolari: due metà asimmetriche. Testo a x 79 (5,5 %); colonna di testo destra da x 773 a 1375;
bande foto a 23 px dai bordi (1395 di larghezza); foto editoriale a filo del bordo sinistro (0-720); elenco servizi da x 810
a 1350. Grandi vuoti verticali (150-250 px) tra un blocco e l'altro. Sezioni della home: 12, alte in media 670 px.

### Foto
Tre famiglie: prodotto su fondo chiaro (scatti dei marchi clienti), macro della pelle e della cucitura, lavorazione e
persone (mani, macchine, guanti bianchi). Tagli orizzontali larghi per le bande, verticali per le foto di contorno, accoppiate
grande + piccola. Nessun filtro sul colore; il bianco e nero solo per archivio e ritratti (storia). Le foto sono servite alla
misura di visualizzazione (Wix). Video in loop muti per la lavorazione.

### Movimenti e interazioni
| cosa | come (misurato) | divieti del committente |
|---|---|---|
| comparsa dei testi allo scorrere | `motion-fadeIn` + `motion-blurIn`: opacità da 0 a 1 e sfocatura da 6 px a 1 px in circa 1,6 s, su quasi ogni blocco di testo della home e della storia | **vietato** (sezioni in dissolvenza allo scroll) |
| comparsa delle foto | `motion-floatIn`: spostamento di 60 px dal basso + opacità da 0 | **vietato** |
| comparsa dei titoli "we are", "Reach Out" | `motion-revealIn`: ritaglio (`clip-path`) che si apre da sinistra | non è una dissolvenza, ma è una comparsa allo scorrere: da non usare |
| ingresso della prima schermata | 3,5 s di nero, poi titolo e foto | da non riprendere (attesa) |
| menu | pannello nero a tutta pagina, voci in corsivo serif 60 px, voce corrente barrata, contatti a destra | il corsivo è vietato; l'impianto no |
| galleria prodotti | filtro di opacità all'arrivo delle immagini (1,1-1,3 s), didascalie al passaggio | dissolvenza delle immagini: da non usare |
| un link | transizione `color 0.4s, opacity 0.4s` | se all'hover cala l'opacità è vietato (non verificato quale link) |
| lettore audio "the sound of our work" | play manuale | da non riprendere |
| mouse | nessun elemento si sposta seguendo il cursore (tre posizioni provate) | nessun effetto vietato |

### Testo e lunghezza
Home: circa 410 parole, solo in inglese; frasi brevi e grandi, poco testo corrente. Home 8.086 px a 1440 (9 schermate),
6.952 a 390; storia 6.107; prodotti 12.254-13.431 (la cattura a pagina intera e quella a passi danno altezze diverse).

---

## 2. Studio N19

### Prima schermata (`n19-home-1440-prima.jpg`, `n19-home-1440-scorsa.jpg`)
Fondo quasi bianco `#FEFEFC`. Testata bianca 68 px con filetto inferiore `#EFEFED`, non fissa: "Studio N19" in Helvetica
Bold con una scritta minuscola sotto, icona del menu a destra. Al centro, composto a scaletta, "This is a / creative / lab
studio" in Helvetica Bold 112,5 px, interlinea 0,8, spaziatura -0,05 em, grigio `#C2C2C2`; la parola "creative" resta sfocata.
A sinistra "creative agency" e a destra "© 23-26" a 33,75 px, con due trattini verde lime `#D2FF00` sopra. Cerchio sottile con
freccia che oscilla in basso a destra. Sotto la testata un video di sfondo (non riprodotto nella prova). **Prima del contenuto
c'è un'introduzione di 4-6 s**: solo la parola "creative" con due barre lime, poi il titolo arriva sfocato.

### Le prime tre schermate
1. Titolo come sopra.
2. "about studion19" in grigio `#C2C2C2` 47 px, poi un paragrafo-manifesto in Helvetica Bold 47 px con interlinea 1,0, nero,
   su tutta la larghezza (circa 60 parole); a destra, da x 845, un paragrafo in Helvetica Light 20 px. Etichetta "(projects.)"
   tra parentesi, grigia, 13,5 px.
3. Riga "some projects of our agency" a sinistra e "× check all" a destra (20 px), poi uno scorrimento orizzontale di progetti:
   foto in bianco e nero alte 756 px affiancate con 10 px di spazio, freccia a destra.

Poi: banda video 1440 x 492 (un altoparlante in macro) con "We give voice to ideas" in 11 px al centro; elenco dei servizi in una
riga continua con le voci alternate nero / grigio; paragrafo "our strategy"; galleria a muratura in bianco e nero (32 foto,
10 px di spazio, margini 18 px); "alcuni dei nostri clienti" come elenco continuo separato da punto e virgola, nero e grigio;
fascia lime a tutta larghezza con "creative agency" a 270 px tono su tono (`#CDF901` su `#D2FF00`) e il riferimento
"Safety Yellow sRGB 204 255 0 HEX ##CCFF00"; piede nero con "THANK YOU FOR VIEWING STUDION19." a 78,75 px maiuscolo,
mail a 44 px, P.IVA e indirizzo, "© 2035 by Studio N19".

### Pagine interne
- `n19-servizi-1440-scorsa.jpg`: stessa apertura ("services" grande e sfocato), manifesto 47 px, poi l'elenco numerato
  **01-07 a tre colonne** (numero 11 px a x 90, titolo Helvetica Bold 27 px a x 263, descrizione Light grigia da x 803),
  righe alte circa 210 px separate da filetti grigi; banda video grigia "minimal is our format always"; galleria progetti.
- `n19-contatti-1440-scorsa.jpg`: apertura "contatti", mail grande a destra, sede legale e operativa in due colonne,
  icone social, due ritratti verticali (uno in bianco e nero, uno a colori), 3.215 px.
- Mobile (`n19-home-390-scorsa.jpg`): il titolo a scaletta si spezza ("This is a creative" in alto, "lab studio" 230 px
  più in basso a destra), il manifesto scende a 32 px, la galleria diventa una colonna; il riquadro fisso Privacy/Cookie
  copre il testo a ogni schermata.

### Caratteri (dal codice)
| ruolo | famiglia | peso | misura / interlinea a 1440 | spaziatura |
|---|---|---|---|---|
| titolo, manifesto, etichette | Helvetica W01 Bold (Wix) | 700 | 270/162 · 112,5/90 · 78,75/63 · 47,25/47,25 · 20,25/20,25 · 13,5 | -0,05 em in tutte le misure |
| testo | Helvetica W01 Light (Wix) | 300 | 20,25/26,3 · 13,5/13,5 | -0,04 / -0,05 em |

Una famiglia sola, due pesi. Mobile: titolo 40 px, manifesto 32 px, testo 20 px.

### Colori
Fondo `#FEFEFC` / `#FFFFFF`, testo `#000000`, testo spento `#C2C2C2`, testo secondario `#6E6E6E`, filetti `#EFEFED`,
accento lime `#D2FF00` (dichiarato `#CCFF00`), piede `#000000`. Foto tutte in bianco e nero.

### Griglia e margini
Margine esterno 18 px per foto e righe, 28 px per la testata; testo principale da x 29 a tutta larghezza; testo secondario
nella colonna destra da x 845 (59 %). Spazio tra le foto 10 px. Sezioni separate da filetti a tutta larghezza. Ogni capitolo
ha la stessa apertura: etichetta tra parentesi, riga "titolo a sinistra / × link a destra", contenuto. Home in 18 sezioni;
alcune sono alte 559 px con dentro solo una riga di testo e una barra lime.

### Foto
Ritratto di studio e still life su fondo grigio uniforme, tutto in bianco e nero (filtro `grayscale(1)`); al passaggio del
mouse la foto torna a colori in 0,6 s e compaiono cliente e progetto (`n19-hover-galleria-1440.jpg`). Muratura con tagli
misti verticali e orizzontali; bande video a tutta larghezza. Le foto sono servite alla misura di visualizzazione.

### Movimenti e interazioni
| cosa | come (misurato) | divieti del committente |
|---|---|---|
| sfocatura e trasparenza legate allo scorrere | titoli e manifesti con `blur` da 2 a 5 px e opacità da 0,1 a 0,7 secondo la posizione nella finestra (fermi nel tempo, cambiano scorrendo) | **vietato** (comparsa in dissolvenza allo scroll) |
| comparse | `motion-fadeIn` su "We give voice to ideas", "creative agency", "Safety Yellow" | **vietato** |
| introduzione | 4-6 s con "creative" e due barre lime prima del titolo | da non riprendere |
| barre lime verticali | ferme nel tempo, scorrono a circa 0,65 della velocità della pagina (parallasse) | non è nell'elenco dei divieti, ma è decorazione senza funzione: da non riprendere |
| galleria | bianco e nero, poi colori al passaggio (`filter 0.6s`), didascalia sovrapposta | ammesso (non è opacità); su telefono non esiste il passaggio del mouse |
| scorrimento progetti | striscia orizzontale con freccia (`transform 0.8s`) | ammesso |
| freccia nel cerchio | oscilla in loop | da non riprendere |
| menu | pannello nero a tutta pagina, voci Helvetica Bold 100 px grigie, corrente barrata, mail 44 px e social a destra (`n19-menu-1440.jpg`) | ammesso |
| mouse | nessun elemento segue il cursore (si muove solo la freccia, per conto suo) | nessun effetto vietato |

### Testo e lunghezza
Home circa 550 parole (servizi 730), italiano e inglese mescolati ("about studion19", "check all", "hey. we are crazy").
Home 10.800 px a 1440 (12 schermate), 7.226 a 390; servizi 10.403; contatti 3.215.

---

## 3. Tratti da riprendere come "tipologia"

Per i soggetti di moda e di fascia alta; per gli altri si dice caso per caso. Ognuno con il file da cui viene.

1. **Titolo-manifesto lungo, a due toni senza corsivo.** Una frase di 12-16 parole su 4-5 righe, interlinea 0,9-1,0, con
   alcune parole nel tono spento (`#6E6E6E` su nero, `#C2C2C2` su bianco) invece che in corsivo o a colori. Da
   `graziella-home-1440-prima.jpg` (togliendo il corsivo) e `n19-home-1440-scorsa.jpg` (manifesto 47 px).
   Moda e lusso sì; aziende tecniche sì, in un grottesco, se la frase è vera e concreta.
2. **Campo unico nero e foto alla loro misura.** Tutta la pagina su `#000`, senza fasce di colore che si alternano: il colore
   lo portano solo le foto (cuoio, pelle). Da `graziella-home-1440-scorsa.jpg`. Pelletteria, moda, gioielli sì; aziende
   tecniche e industriali no (diventa cupo e "da lusso" fuori posto).
3. **Coppia grande + piccola allineata in alto.** Un macro di dettaglio grande (circa 70 % della larghezza) accanto a una
   miniatura verticale (circa 18 %), stessa linea superiore. Da `graziella-home-1440-scorsa.jpg` (cucitura 1025 x 526 + 266 x 307).
   Moda sì; manifatture e artigiani sì (dettaglio della lavorazione + pezzo finito); industria pesante solo se ci sono macro buoni.
4. **Etichetta piccola a sinistra, testo nella metà destra.** "we are" a sinistra seguito da un filetto corto, il paragrafo da metà
   pagina in poi, molto vuoto intorno. Da `graziella-home-1440-scorsa.jpg` e `graziella-history-1440-scorsa.jpg` ("factory" con il filetto).
   Vale per tutti i soggetti: è un impianto, non uno stile.
5. **Foto editoriale a metà pagina a filo del bordo.** Una foto verticale che tocca il bordo della finestra (0-720 a 1440) e il
   testo allineato a destra nell'altra metà. Da `graziella-home-1440-scorsa.jpg` (modella con borsa). Moda sì; altri
   soggetti solo con un ritratto o un ambiente vero, non con foto di repertorio.
6. **Elenco a righe con filetto e numero.** Righe separate da filetti sottili, numero piccolo, titolo grande, una riga di
   descrizione in colonna a parte. Da `n19-servizi-1440-scorsa.jpg` (01-07, tre colonne) e `graziella-home-1440-scorsa.jpg`
   ("our services", serif 56 px). Vale per tutti, ed è il tratto più adatto alle aziende tecniche (lavorazioni, fasi, reparti).
7. **Nomi di marchi o clienti composti come testo.** Niente parete di loghi: i nomi a 52 px centrati uno per riga
   (Graziella) o un elenco continuo con voci alternate nero / grigio (N19). Da `graziella-hover-marchi-1440.jpg`,
   `graziella-home-1440-scorsa.jpg`, `n19-home-1440-scorsa.jpg`. Moda e conto terzi sì, **solo con nomi pubblici e
   verificati** (niente clienti inventati); aziende tecniche: la versione a elenco continuo, solo se l'elenco è pubblico.
8. **Cronologia a righe: anno, tre righe, foto orizzontale.** Una riga per data, foto 375 x 155 a destra, archivio in bianco e
   nero accanto alle foto di oggi. Da `graziella-history-1440-scorsa.jpg`. Vale per tutte le aziende di famiglia con date
   vere; per moda e lusso con le foto d'archivio, per l'industria con lo stabilimento.
9. **Bianco e nero uniforme per foto disomogenee.** Una galleria in cui tutte le foto passano in bianco e nero diventa un
   insieme coerente anche se gli scatti sono diversi. Da `n19-home-1440-scorsa.jpg` e `n19-hover-galleria-1440.jpg`.
   Utile ad aziende tecniche con foto di reparto miste; **nella moda no per il prodotto** (il colore del cuoio è
   informazione), sì per archivio, persone e lavorazione.
10. **Menu a tutta pagina con voce corrente barrata.** Pannello nero, voci enormi in colonna, pagina attuale barrata, contatti
    e mail a destra. Da `graziella-menu-1440.jpg` e `n19-menu-1440.jpg`. Moda sì (anche su desktop); per aziende
    tecniche solo come menu del telefono, con le voci visibili in testata su desktop.

Abbinamento dei caratteri: il registro di Graziella (serif da display leggero e stretto, molto grande, accanto a un grottesco
piccolo per etichette) corrisponde a quello già scelto per la moda in `CARATTERI-E-SEGNALI-IA.md` (Noto Serif Display 300 +
Kumbh Sans, "foto alla loro misura in campo nero"). Awesome Serif è a pagamento e non è in Google Fonts: non si porta in
Elementor gratuito.

## 4. Cosa NON riprendere

- **Comparse allo scorrere** di Graziella: dissolvenza + sfocatura su quasi ogni testo, foto che salgono di 60 px, titoli
  che si scoprono con il ritaglio. Divieto del committente.
- **Sfocatura e trasparenza legate allo scorrere** di N19 (titoli e manifesti sfocati a 2-5 px finché non sono a metà
  finestra). Divieto.
- **Corsivo serif per le parole d'accento** ("leather goods", "luxury", "brands", "Out", il menu tutto in corsivo). Divieto
  esplicito: il due toni grigio/bianco basta da solo.
- **Attese all'apertura**: 3,5 s di nero (Graziella), 4-6 s di introduzione (N19).
- **Verde lime su nero e bianco**: la coppia "nero con verde acido" è nella lista delle palette da generatore
  (`CARATTERI-E-SEGNALI-IA.md`); in più per la fascia alta è fuori registro. Lo stesso vale per le barre lime in
  parallasse, la freccia che oscilla e la scritta 270 px tono su tono.
- **Testo sopra le foto senza contrasto** e sovrapposizioni ("Technical expertise to refine every detail" scritto sopra
  "our details" e sopra la foto; su mobile frasi che finiscono sotto le foto).
- **Paragrafi serif con interlinea 1,0** (22,5/22,5) e dati societari a 11 px con interlinea 1,0: illeggibili. I dati
  completi in piede (P.IVA, REA, PEC) invece sì, ma a misura leggibile.
- **Solo icona del menu anche su desktop** per un'azienda che deve farsi trovare: va bene per un marchio di moda, non per
  un fornitore tecnico.
- **Resti del modello Wix**: "© 2035 by Studio N19", la X del menu nel blu di sistema, didascalie della galleria in un altro
  carattere, "contact" tagliato nel menu di Graziella, caratteri caricati e non usati, sezioni vuote alte 559 px, riquadro
  fisso Privacy/Cookie che copre il testo, bottone "torna su" sopra i contenuti su mobile.
- **Testi**: "Made with passion" (parola vietata), trattini lunghi nel testo (tra "service" e "from design to production"), refusi ("follo us
  on.", "More Project"), "click here", "hey. we are crazy", lettore audio "the sound of our work", sito di un'azienda
  italiana solo in inglese (Graziella), inglese e italiano mescolati (N19).
- **Pagine lunghissime**: N19 12 schermate per la home, Graziella 13.000 px per una galleria. Per i siti da proporre bastano
  6-8 schermate.
