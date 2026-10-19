# Antonio Bertolin Srl: nota sulla home finale

Versione finale della home, costruita sulla bozza B ("Il telaio"), che ha scelto il committente. La bozza A ("Senza pigmento") era la preferita del giudice. Qui ne entrano solo due dettagli, descritti più sotto. La versione finale che c'era prima in `sito/` era costruita sulla A ed è stata sostituita del tutto. I suoi script sono in `_prova/script/finale-su-a-scartata/`.

File:
- la pagina: `sito/index.html`, con `sito/img/` e `sito/fonts/`;
- la sorgente: `_prova/script/pagina-finale.html`;
- lo script che rifà tutto: `bash _prova/script/build_finale.sh`, che rifà immagini, caratteri, pagina, controlli sul testo, screenshot e segnali.

## L'idea

La fabbrica vera come prova. La pagina si apre sul telaio di ossidazione caricato di boccole, a tutta larghezza, con due legende numerate come su una tavola di reparto. Sopra, su bianco, c'è il nome del mestiere in una riga sola che occupa tutta la giustezza: "Ossidazione anodica".

Poi vengono:
- chi sono;
- i sei trattamenti, che si filtrano per metallo;
- il colore, che sul titanio è uno spessore e sull'alluminio un pigmento, mostrato sui loro pezzi;
- l'impianto del 2018 e lo stabilimento di Tombelle accanto ai contatti.

Su questa pagina il nome di un concorrente non reggerebbe: le foto, i colori dichiarati, il 2018 e l'indirizzo sono tutti di Bertolin.

## Le prime due schermate

**A 1440** (`home-1440-prima-schermata.jpg`):
- la testata ha il logo, quattro voci, "Scriveteci" (mailto) e il telefono;
- il titolo è a 134 px, largo quanto la gabbia;
- sotto, a partire dalla settima colonna, ci sono tre righe su cosa fanno e dove;
- poi viene il telaio da bordo a bordo, alto 700 px, con le legende "1 Barra del telaio" e "2 Boccola tornita".

Nella seconda schermata ci sono:
- la didascalia "Boccole sul telaio, prima del bagno di ossidazione.";
- il paragrafo grande su chi sono: officina metalmeccanica, materiale rotabile, particolari su specifica, poi i trattamenti di superficie;
- la riga "Per chi lavoriamo".

**A 390** (`home-390-prima-schermata.jpg`):
- il titolo va su due righe a 47 px, seguito dalle tre righe di testo;
- il telaio è in un taglio verticale 4:5 a filo, con le stesse due legende, e la prima schermata finisce sulla foto;
- la testata ha il logo, "Scriveteci" e il telefono;
- sotto i 350 px "Scriveteci" lascia il posto al solo telefono.

**Altezza della pagina**:

| Larghezza | Altezza |
|---|---|
| 1440 | 5736 px |
| 390 | 5785 px |
| 320 | 5944 px |
| 768 | 5929 px |
| 1024 | 5163 px |
| 1920 | 5797 px |

Le sezioni sono cinque (apertura, chi, trattamenti, colore, stabilimento e contatti), più il piede.

## Cosa è cambiato rispetto alla bozza B

Dalla bozza B restano l'idea, la prima schermata, il trattamento delle immagini, il carattere e i colori. Ecco cosa è cambiato.

**Telaio, più nitido e più luminoso**
- La fascia larga ora è tagliata solo sulla parte a fuoco della foto (da x 0 a 1720 su 2560). A 1440 la foto si riduce invece di ingrandirsi, e la metà destra sfocata, quella "impastata", resta fuori.
- Il fondo è schiarito verso il bianco.
- La maschera di contrasto è leggera.

**Legende del telaio**
- La legenda "3 Pinza" non indicava niente di leggibile ed è tolta.
- "Boccola in alluminio tornito" diventa "Boccola tornita", perché il metallo non è confermato.
- La didascalia non dice più "in alluminio".

**Trattamenti**
- Il selettore a pillola bianca, che sembrava un componente di serie, è sostituito da una frase: "Il pezzo è in alluminio, titanio o acciaio?". Le tre parole sono bottoni veri, sottolineati a puntini; quella scelta prende la sottolineatura piena.
- La colonna delle misure tiene solo i valori veri: 0-400 nm, 5-20 micron, grigio scuro, citrico o nitrico.
- Tolti i riempitivi "Brillante / senza bave" e "Satinato / finitura sabbiata".

**Colore**
- Nuovo titolo sull'alluminio, in parallelo a quello sul titanio: "Sull'alluminio il colore è un pigmento". Il sito dice: "oltre all'ossidazione naturale abbiamo anche altri pigmenti".
- Il testo che ripeteva "moda e arredamento" è tolto.
- I tubi sono ripuliti dalla polvere con un filtro mediano verticale, applicato solo sui granelli.
- La minuteria ha un taglio un po' più alto.

**Contatti** (innesto da A)
- Nuova riga per il preventivo: "Per un preventivo mandate disegno, materiale e quantità a info@bertolinantonio.it", con un link sottolineato e nessun bottone colorato.
- Lo stesso indirizzo è nella testata, come "Scriveteci".
- L'indirizzo diventa il titolo ("Viale Serenissima 15, Tombelle di Vigonovo").

**Dati e testi**
- "Tra Padova e Venezia" diventa "in provincia di Venezia", come scrive il sito: "VE".
- Dalla A viene "metropolitane, tram, filobus e Ferrovie dello Stato": il sito dice "ferroviario, tranviario, filoviario".
- Il paragrafo su chi sono non ripete più il 2018, che resta nel blocco dello stabilimento.

**Accessibilità e dettagli**
- Link "Vai al contenuto".
- Grigio delle note scurito a #565A60 (6:1 sul campo alluminio).
- L'oro del passaggio sui link è scurito a #8F6B1D, che regge su bianco.
- Il link alla privacy porta alla pagina vera del sito di oggi.

**Indicazioni del giudice non applicate**, perché valgono solo per la A o cambierebbero la bozza scelta:
- Switzer al posto di Mona Sans;
- il piede chiaro;
- l'interruttore Titanio/Alluminio;
- l'apertura sui tondini.

## Caratteri e colori

**Carattere**: Mona Sans (GitHub, distribuito da Google Fonts), una sola famiglia variabile.
- Usi:
  - i titoli sono a larghezza 112 % e peso 430, con interlinea 0,92 e spaziatura -0,035em sul titolo grande;
  - il testo è a larghezza 100 % e peso 400, a 18 px;
  - le misure dei trattamenti sono a 30 px, larghezza 112 %.
- Riferimenti: il titolo leggero e spaziato di Medartis (impianti in titanio) e la pulizia di Ressence, nella sezione 7 dell'analisi.
- File: serviti dalla pagina in `sito/fonts/` (`monasans-latin.woff2`, `monasans-latin-ext.woff2`).
- Licenza: SIL Open Font License 1.1, il cui testo è in `sito/fonts/OFL-Mona-Sans.txt` (scaricato da github.com/google/fonts). Uso commerciale libero; "Mona" è un nome riservato, quindi i file non vanno modificati e poi ripubblicati con quel nome.
- Attenzione: Mona Sans è anche il carattere di testo della home di Paraga Pelli, nella stessa zona. Qui la differenza è nei titoli semi-espansi.
- Le cifre sono allineate e proporzionali. Le tabellari di Mona Sans hanno lo zero barrato da monospazio e darebbero l'aria da codice che la guida sconsiglia. Le misure stanno una per riga e allineate a destra, quindi non serve incolonnarle.

**Colori**:

| Colore | Uso |
|---|---|
| bianco #FFFFFF | la pagina |
| alluminio naturale #E6E7E8 | il solo campo pieno, i trattamenti |
| grafite #1C1E21 | testo e piede |
| grigio #565A60 | le note |
| spento #8A8E94 | i trattamenti che non valgono per il metallo scelto |
| oro #8F6B1D | solo al passaggio sui link |

Il colore pieno lo danno le foto dei pezzi anodizzati. Non ci sono gradienti, ombre o vetri.

## L'interazione

È una sola: "Il pezzo è in alluminio, titanio o acciaio?", sopra l'elenco dei sei trattamenti.
- Un tocco spegne in grigio i trattamenti che non valgono per quel metallo. Quelli che restano accesi sono 2 per l'alluminio, 5 per il titanio e 2 per l'acciaio, secondo le schede del sito.
- Una riga sotto dice l'esito, per esempio "Per l'alluminio: 2 trattamenti su 6".
- Un secondo tocco sullo stesso metallo riaccende tutto.
- Sono bottoni veri con `aria-pressed`, alti 44 px, e l'esito è letto dai lettori di schermo (`aria-live`).
- Provata da `finale_shoot.mjs` col dito a 390, 320 e 768 e con Invio e Spazio a 1440, 1024 e 1920.
- Cambia solo il colore, in 0,12 s. Non ci sono dissolvenze, animazioni allo scorrere o effetti che seguono il cursore.

## Foto: origine e licenza

Tutte le foto in pagina sono di Antonio Bertolin Srl, scaricate dal loro sito il 19/10/2026 (`assets/originali/`, inventario in `_prova/inventario-immagini.json`). Non ci sono foto di repertorio né immagini generate. Lavorate da `_prova/script/finale_img.py`, esportate in JPEG, in più larghezze per `srcset`.

| In pagina | Originale (voto qualità/apertura) | Lavorazione |
|---|---|---|
| `telaio-largo` 960/1440/1720 | `DSC_0029-scaled.jpg` (6/6) | taglio sulla parte a fuoco, fondo schiarito, saturazione 0,82 |
| `telaio-alto` 390/780/1060 | lo stesso | verticale 4:5 sulle prime due file |
| `minuteria` 720/1080/1440 | `minuteria-medicale-scaled.jpg` (6/7) | bianchi puliti, taglio sul gruppo dei pezzi |
| `tubi` 720/1440/2180 | `acciaio-scaled.jpg` (6/5) | solo i tubi, senza la base con la scritta rossa, polvere tolta |
| `reparto` 640/960/1280 | `foto_aerea_bertolin-scaled.jpg` (6/3) | 4:3, saturazione 0,8, a mezza colonna vicino ai contatti |
| `logo-grafite`, `logo-bianco` | `logo-footer-bertolin.png` | forma presa dal file e ricolorata. Serve il vettoriale |

Le foto Unsplash e Pexels di `assets/esterne/` non sono usate. Quali foto vanno rifatte dal vero, e come, è scritto nel `LEGGIMI.md`.

## Le ispirazioni del committente (Pelletteria Graziella, Studio N19)

Le ho usate per un solo tratto, ed è una scelta. Antonio Bertolin è un'officina di trattamenti di superficie per il medicale e l'industria, non un marchio di moda o del lusso.
- Di Studio N19 resta il fondo chiaro con un titolo molto grande e tanta aria intorno. È quello che fa l'apertura.
- Di Pelletteria Graziella non c'è niente: il nero pieno, la serif col corsivo e il tono da maison sono fuori registro per un'officina che lavora per il medicale.

Il registro viene dal mestiere: la foto di reparto, le legende, le misure vere, i colori che il sito dichiara.

## Controlli

- **Larghezze**: a 1440, 390, 320, 768, 1024 e 1920 non c'è scorrimento orizzontale, nessun elemento esce dalla finestra, nessun testo si sovrappone a un altro e nessuna legenda esce dalla sua foto. Gli screenshot sono in `_prova/controlli/` e li ho guardati a pezzi con `slice.py`.
- **Testo**:
  - nessun U+2014 in pagina, script, LEGGIMI, NOTA e CREDITI;
  - nessun segnaposto;
  - nessuna nota di lavorazione a vista.
- **Segnali da IA** (`_prova/controlli/segnali/`, strumento del kit a 1440): 0 soglie bloccanti e 0 da guardare.

| Soglia | Valore |
|---|---|
| Area foto | 35,5 % |
| Famiglie di caratteri | Mona Sans al 100 % |
| Monospazio | 0 % |
| Etichette maiuscole | 0 |
| Misure di H2 | 3 (64, 40, 34 px) |
| Fasce di fondo | 3 |
| Filetti | 11 |
| Frecce | 0 |
| Numeri grandi | 1 (2018) |
| Contenuto datato | 2018 |
| Divieti | nessuno |

- **A occhio**: niente badge, tre box con icona, corsivo d'accento, card col bordo sinistro, glassmorphism o gradienti.
- **Peso della cartella `sito/`**: 1,9 MB.
