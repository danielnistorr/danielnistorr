# Poli-Art: analisi per la nuova home

Sito: https://poli-art.it (crawl e screenshot del 24/10/2026: home, 11 pagine, sitemap Yoast, libreria media di WordPress via `/wp-json/wp/v2/media`, 195 voci). Le pagine del sito sono indicate con il percorso dopo il dominio. Testi estratti in `_prova/crawl/*.txt`, script in `_prova/script/`.

## 1. In breve

- **Chi**: Poli-Art di Zigliotto Manuel, **ditta individuale** (non una società), via Tesinella 7, 36040 Grisignano di Zocco (VI). Titolare Manuel Zigliotto.
- **Da quando**: il sito dice "L'Azienda nasce nel 1986" (`cosa-facciamo/`). La partita IVA attuale però ha un'anzianità di "11 - 20 anni" (informazione-aziende.it). Quindi il 1986 è l'anno del mestiere, forse di una ditta precedente: va chiarito (sez. 9). Il "da oltre 38 anni" del sito è fermo al 2024; Pagine Gialle scrive "40+".
- **Cosa fanno davvero**: tagliano e scolpiscono **polistirene espanso** "tramite l'utilizzo di macchine a controllo numerico ed ove necessario con l'insostituibile lavorazione artistico manuale" (`cosa-facciamo/`), poi lo resinano, lo verniciano e lo rifiniscono. Ne escono:
  - scenografie, vetrine e stand;
  - oggetti fuori scala per le fiere (barattoli, flaconi, scarpe, palloni giganti);
  - lettere e loghi in volume;
  - decori e cornici per l'edilizia e casseri per il calcestruzzo;
  - prototipi e mockup;
  - torte finte monumentali;
  - stampa 3D in plastica.
  Gli allestimenti con palloncini li fa il partner Palloncini WOW, non Poli-Art.
- **Per chi**: soprattutto aziende, cioè espositori in fiera, negozi, marchi, imprese edili e pasticcieri. In più feste private ("eventi privati e aziendali", `allestimento-eventi/`).
- **Quanti**: dipendenti e fatturato non sono pubblici. ATECO 32.99.9 "Fabbricazione di altri articoli n.c.a.".
- **Correzioni alla nota di partenza**:
  - "Loghistica" non è logistica. È un gioco di parole su **loghi**: "Realizzazione Loghi: Creazione di loghi aziendali e pubblicitari in polistirolo" (`realizzazioni/`). Il riassunto generato in home e nel piede ("logistica e fieristica") è sbagliato.
  - L'immagine della home non è l'unica fatta con l'IA: **tutte le 11 testate** delle pagine sono immagini Midjourney (file "bellic8145_...").
  - Le foto vere non sono 6-15 per pagina: sono **circa 140**, quasi tutte nella pagina `realizzazioni/`, che non è nel menu.
- **Il dettaglio solo loro**: il **grezzo bianco e la finitura che inganna l'occhio**. Hanno coppie di foto prima e dopo:
  - la testa sfaccettata ancora bianca in laboratorio (`Face-of-GOD2`) e poi cromata in un atrio (`Face-of-GOD`);
  - la scarpa gigante bianca accanto al disegno (`Scarpa-converse3`) e poi coperta di fiori;
  - il blocco grezzo (`Blocco-marmo3`) e poi in finto marmo.
  È la frase del sito "con gli opportuni trattamenti plastici, possiamo ottenere delle superfici resistenti agli urti a prova di 'curiosi'" (`scenografie/`), fatta immagine.

## 2. Il sito di oggi

**Pagine**:
- Menu: Home, Chi siamo (`cosa-facciamo/`), Servizi con sottomenu (Stampa 3D, Scenografie, Prototipi, Mockup, Loghistica, Edilizia, Cake design, Allestimento Eventi), Contatti con modulo Gravity Forms.
- Nella sitemap c'è anche `realizzazioni/`, la galleria con circa 140 foto, che non ha nessun link dal menu.
- Mancano le pagine privacy e cookie: `privacy-policy/` risponde 404.
- Le pagine sono state modificate l'ultima volta tra giugno e ottobre 2024. Non ci sono notizie (`/wp-json/wp/v2/posts` è vuoto).

**Testi veri essenziali (verbatim)**:
- Home: h1 "Poli-Art", "Lavorazione del polistirolo", "Esperti nella Lavorazione del Polistirene Espanso dal 1986".
- `cosa-facciamo/` (lo stesso testo di `Testi.docx`):
  - "Da oltre 38 anni è dedita alla lavorazione del polistirene espanso (polistirolo) impiegato in vari settori quali scenografie, edilizia, pasticceria, loghistica, fieristica etc."
  - "Essendo un mercato di nicchia l'esperienza ed il know-how maturato negli anni imperano per la riuscita di un buon prodotto."
- `scenografie/`:
  - "ideale per la creazione di scenografie teatrali, cinematografiche, usato molto nella vetrinistica e negli stand fieristici"
  - "facile da installare e rimuovere, rendendolo ideale per produzioni itineranti"
- `edilizia/`:
  - "Opportunamente resinato, il polistirolo viene impiegato per la realizzazione di tutti quegli elementi architettonici plastico decorativi"
  - "casseforme per il getto del calcestruzzo ... dai cornicioni sottotetto alle slitte per le scale a chiocciola alle colonne agli archi dei porticati ai getti industriali"
  - Il resto della pagina è un testo generico sull'isolamento.
- `mockup/`: "Molto richiesta è la realizzazione come macroscopia per valorizzare il prodotto ... riproposto in dimensioni più grandi suscita così la curiosità del passante".
- `prototipi-personalizzati-di-alta-qualita/`:
  - "Tutto inizia con un progetto 3D fornito dal Cliente o, se il cliente ne è sprovvisto, provvediamo noi all'elaborazione del solido virtuale."
  - "per poter vedere e tastare con mano quello che realmente sarà la produzione"
- `stampa-3d/`: "I materiali che utilizziamo sono principalmente plastiche ecosostenibili, ma stampiamo anche plastiche come ABS ed altre plastiche strutturali".
- `cake-design/`: "Il polistirolo è un alleato inestimabile per i pasticceri che desiderano creare torte monumentali"; "effetti ottici illusionistici".
- `loghistica/`: "Tutto parte col fissare dei paletti che strutturiamo assieme a Voi". Il resto della pagina è un testo generico sullo studio dei loghi.
- `allestimento-eventi/`:
  - "in collaborazione con un team di professionisti di Balloon Art con oltre 10 anni di esperienza nel settore eventi"
  - "100% biodegradabili"
  - "L'EFFETTO WOW GARANTITO"
- Non ci sono:
  - un elenco di macchine (marca, numero di pantografi, misure massime di lavoro);
  - certificazioni;
  - numeri;
  - clienti citati nel testo (i marchi si vedono solo nelle foto, sez. 9);
  - orari.

**Tecnologia**:
- WordPress 6.5.3 con il tema **Salient**, WPBakery, Salient Portfolio, Gravity Forms e Yoast.
- Server BitNinja WAF dietro Caddy.
- Google Analytics G-QCBYY6XLXL. Lo script Cookiebot è caricato, ma nelle prove non è comparso nessun banner.
- Font: Nunito, Muli e Roboto da Google, caricati senza consenso.
- Logo in PNG 1815x400 in due versioni, blu ardesia e bianca.

**Problemi a 1440** (`_prova/attuale/home-1440.jpg`, `home-1440-prima-schermata.jpg`, pezzi in `p1440/`):
- Prima schermata:
  - frammenti grigi generati con l'IA, tagliati da un'onda bianca;
  - il titolo "Poli-Art" è centrato, in blu su grigio, e si legge male;
  - non c'è nessun lavoro vero.
- Sotto ci sono otto icone da catalogo (mattoni, castello, palloncini, torta) in due file, con molto vuoto. È la sezione più grande della pagina.
- L'unica foto vera è la testa cromata, ritagliata in un cerchio.
- Pagina alta 2518 px, ma con quasi niente dentro.
- Il piede grigio azzurro ripete il riassunto sbagliato ("logistica"), il telefono non è cliccabile, e non ci sono P.IVA, privacy e social (che sono nel menu a scomparsa).
- `scenografie-1440.jpg`: testata IA, testo a sinistra e foto in un cerchio a destra, poi un carosello di foto piccole.
- `realizzazioni-1440.jpg`: 139 foto in una griglia a tre colonne alta 15273 px, senza didascalie né ordine.

**Problemi a 390** (`home-390.jpg`, pezzi in `p390/`):
- Ogni icona occupa mezza schermata, e la pagina arriva a 3889 px.
- Il titolo della prima schermata è piccolo sopra l'immagine IA.
- Nessuno scorrimento orizzontale. Il menu ad hamburger funziona.

**Obblighi**: sul sito mancano la **P.IVA** (obbligatoria per l'art. 35 del DPR 633/72) e l'informativa privacy, anche se c'è un modulo che raccoglie nome, email e telefono.

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Poli-Art di Zigliotto Manuel | piede di ogni pagina: "© 2026 Poli-Art di Manuel Zigliotto."; europages.it/POLIART-DI-ZIGLIOTTO-MANUEL/SEAC006167863-001.html: "POLI-ART DI ZIGLIOTTO MANUEL" |
| Forma | impresa individuale | informazione-aziende.it/Azienda_POLIART-DI-ZIGLIOTTO-MANUEL: "IMPRESA INDIVIDUALE" |
| P.IVA | 03796810244 | informazione-aziende.it (stessa pagina), dati iCribis. La cifra di controllo è valida e il codice d'ufficio 024 è Vicenza. **Non è sul sito** |
| ATECO | 32.99.9 | informazione-aziende.it: "Fabbricazione di altri articoli n.c.a." |
| Anzianità della P.IVA | 11-20 anni | informazione-aziende.it: "11 - 20 anni" |
| Anno del mestiere | 1986 | `cosa-facciamo/`: "L'Azienda nasce nel 1986." |
| Indirizzo | via Tesinella 7, 36040 Grisignano di Zocco (VI) | piede: "Via Tesinella, 7 – 36040 Grisignano di Zocco (VI)". Gli elenchi danno "7/A" (bluaziende.com) e "7/A/9" (europages, iCribis) |
| Telefono | 0444 614719 | piede: "T: 0444 614719"; `contatti/` |
| Email | info@poli-art.it | piede: "E: info@poli-art.it" |
| PEC, REA, capitale | non trovati | per una ditta individuale il capitale non si applica; il REA non è sugli elenchi letti (informazione-aziende risponde 429 a curl, paginegialle e paginebianche 403) |
| Orari | lun-ven 8-12 e 14.30-18 | solo dall'aggregatore showmelocal (riassunto di una ricerca): da confermare |
| Partner | Palloncini WOW (balloon art) | `allestimento-eventi/`: "in collaborazione con" e il logo `logo_palloncini_wow.svg` |
| Social | Facebook e Instagram | link in ogni pagina: facebook.com/p/Poli-Art-di-Zigliotto-Manuel-Lavorazione-del-Polistirolo-100068181162086/ e instagram.com/poliartgrisignano/ ("POLI-ART Grisignano (@poliartgrisignano)" nei risultati di ricerca). Follower e data dell'ultimo post non leggibili: le due pagine chiedono il login |
| Dipendenti, fatturato | non trovati | |

## 4. Materiale visivo

Ho scaricato 191 file (79 MB) in `assets/originali/`. Le 13 immagini IA sono salvate solo come copie ridotte `ia-*`. L'inventario, con misure, pagina, soggetto e voti (qualità / forza come apertura, da 1 a 10), è in `_prova/inventario-immagini.json`; i fogli provino sono in `_prova/fogli/foglio-0..8.jpg`, e le migliori in `scelte-1.jpg` e `scelte-2.jpg`. **Nessun video.** Media delle 158 foto vere: qualità **4,6**, apertura **2,9**.

| Gruppo | Quanti | Misure | Qualità | Apertura | Giudizio |
|---|---|---|---|---|---|
| Sala curva bianca con taglio di luce, volume cilindrico (`Pawson1-3`) | 3 | 2560x1920 | 6-7 | 5-6 | le più luminose e ordinate. Il soggetto però è lo spazio, non un oggetto |
| Testa sfaccettata: cromata in un atrio bianco (`Face-of-GOD`, `-GOD3`) e ancora bianca in laboratorio (`-GOD2`) | 3 | fino a 1920x2560 | 5-6 | 5-6 | l'oggetto più forte, e c'è anche il suo "grezzo". Controluce, verticale, sfondo disordinato |
| Stand mosaico+: oggetti di casa grigi su stampate da modellino giganti (`Oggetti1-4`) | 4 | 2560x1920 | 5-6 | 4-6 | l'idea più bella dell'archivio; foto da fiera con luce mista |
| Cassettoni dorati con tele dipinte, cornici accatastate (`CorniciORO*`) | 5 | 1024-2048 | 5-6 | 4-6 | nobile, luce piatta |
| Chaise longue bianca scolpita (`Chesslong`) | 2 | 2000x1500 | 5 | 5 | oggetto da copertina, ma fotografato in mezzo al magazzino |
| Lettere rosse MERAVIGLIAMO, lettere sparse (`3Da`, `3Db`) | 2 | 2560x1928 | 6 | 4-5 | pulite su bianco |
| Oggetti fuori scala: barattolo "nulla", pallone abitabile, bottiglia e schizzo di vino, razzo, confezioni, scarpa di fiori, flacone | circa 40 | 1024-2560 | 4-6 | 2-5 | il loro tratto più riconoscibile; quasi sempre marchi di clienti in vista |
| Edilizia: cornicioni in cantiere, cornici di finestra, casseri blu, slitte per scale | circa 20 | 780-2560 | 3-5 | 1-4 | veri ma da telefono, con ponteggi e cielo bianco |
| Laboratorio in attività (scocca di auto solare con persone, `Fotovoltaico-working`) | 1 | 2048x1536 | 4 | 4 | l'unica foto del lavoro in corso |
| Stampa 3D (giunti neri, vaso, lamelle) | 7 | 964x1280 | 4 | 1-2 | da telefono, dentro la macchina |
| Eventi: carte giganti e coniglio di fiori, piscina | 4 | fino a 2560 | 5 | 3 | |
| Palloncini WOW (lavori del partner) | 10 | 600-1240 | 6 | 2 | non di Poli-Art |
| Personaggi Disney (Topolino) | 4 | 640-1040 | 3 | 1 | da escludere (diritti) |
| Immagini Midjourney e rendering di repertorio (testate di oggi) | 13 | 2912x1632 | n.d. | 0 | da escludere |
| Icone da catalogo della home | 12 | 1080x1080 | 2 | 0 | da non usare |

**Verdetto**: il soggetto è tra i più visivi della campagna, ma la qualità fotografica **non regge una home di alta gamma** (media 4,6). Le foto sono da telefono, con sfondi di magazzino, luce al neon e marchi di clienti dappertutto. Per la proposta servono:
- come foto loro: la testa sfaccettata (grezza e cromata), la sala curva, lo stand mosaico+ e le cornici dorate;
- come segnaposto (sez. 6): l'oggetto bianco della prima schermata.

Per il sito vero serve **una giornata di still life su fondo bianco**, con pochi pezzi a luce morbida:
- un oggetto bianco appena fresato e lo stesso oggetto finito;
- un dettaglio di cornice;
- una lettera in volume;
- un pezzo stampato in 3D.

Più **mezza giornata in laboratorio**: pantografo, filo caldo, mani che rifiniscono, trucioli bianchi.

## 5. Due direzioni artistiche

Registro: una bottega di scultura e scenotecnica che lavora per aziende e marchi. Deve dare una sensazione di precisione e di meraviglia insieme, senza il tono da fiera. Il bianco del polistirolo è già un colore di alta gamma: va lasciato respirare.

**Ispirazioni Graziella e N19**: le uso poco. Poli-Art non è moda né lusso, anche se lavora per vetrine di moda (Paul & Shark, Converse). Ne prendo solo la molta aria, le poche parole e le etichette piccole, che sono già nella ricetta del committente.

**Direzione A, "Grezzo e finito" (chiara, un solo oggetto)**
- Idea visiva: prima schermata color polistirolo (#F5F4F1). C'è un solo oggetto bianco appena scolpito, grande e nitido a destra. A sinistra un titolo grande dai loro testi, per esempio "Lavoriamo il polistirolo dal 1986", con una riga sotto: scenografie, decori per l'edilizia, prototipi, fuori scala, stampa 3D. Seguono quattro sezioni: il prima e dopo, le lavorazioni, il laboratorio, la chiusura.
- Immagini: still life su bianco caldo a luce di finestra, con le coppie grezzo e finito.
  - Dal sito: `Face-of-GOD2` e `Face-of-GOD`, `Scarpa-converse3` e `-converse1`.
  - Segnaposto: Bolovtsova forme bianche (apertura), Karchmit testa in polistirolo.
- Tipografia: Familjen Grotesk (Google Fonts, OFL) per titoli e testo, con cifre tabellari per gli anni e le misure. Niente corsivi d'accento.
- Colore:
  - fondo carta #F5F4F1 e inchiostro #1B1D22 (contrasto 15,3:1);
  - il blu ardesia del logo, scurito a #4E5F7D (5,9:1 su carta, AA), solo per link, bottone e logo;
  - il colore pieno arriva solo dalle finiture vere (oro, cromo, rosso).
- Gesto: un interruttore "Grezzo / Finito" sotto la foto principale cambia la stessa inquadratura dal bianco del polistirolo alla finitura, con un cambio netto e senza dissolvenza. È un vero bottone, usabile da tastiera. Dice in un clic cosa fanno.

**Direzione B, "Fuori scala" (chiara e grafica, il loro tratto più riconoscibile)**
- Idea visiva: la "macroscopia" del sito (`mockup/`) come racconto. Fondo grigio fiera chiaro (#ECEBE7), un oggetto gigante scontornato al centro con accanto la sagoma di una persona per dare la scala, e il titolo enorme. Sotto, una fila ordinata di quattro o cinque oggetti fuori scala, tutti alla stessa altezza di riga, ciascuno con una didascalia di una parola. Poi edilizia e decori, la chiusura.
- Immagini: dal sito il pallone abitabile, la bottiglia con lo schizzo di vino, lo stand mosaico+, il razzo, le lettere MERAVIGLIAMO, tutti da rifotografare scontornati su fondo neutro. **Solo con il permesso dei clienti**, oppure oggetti senza marchio. Segnaposto: Mosayebzadeh testa sfaccettata, Granados laboratorio.
- Tipografia: Bricolage Grotesque (Google Fonts, OFL, asse ottico) per i pochi titoli molto grandi, Geist (Google Fonts, OFL) per il testo. Le misure in cifre tabellari.
- Colore: grigio fiera #ECEBE7, inchiostro #1B1D22, un solo accento rosso scenografia #B3311C (5,2:1 sul grigio, AA), preso dalle loro lettere rosse.
- Gesto: un righello di scala. Toccando un oggetto, accanto compaiono la sagoma umana in proporzione e l'altezza reale. Servono le misure vere dei pezzi, che oggi non sono pubblicate (sez. 9). Senza misure il gesto non si fa.

Per il committente la A è la più vicina alla ricetta: luminosa, un oggetto, tanta aria, e un gesto che spiega il mestiere. La B è più originale, ma dipende dai permessi sui marchi e dalle misure.

## 6. Immagini sostitutive

Ci sono 10 foto in `assets/esterne/` (6 Unsplash e 4 Pexels, al massimo 2400 px sul lato lungo). La licenza è verificata sulla pagina di ogni foto il 24/10/2026. Nessuna è Unsplash+, nessuna è già usata nella campagna, nessuna è generata dall'IA. URL, autori e licenze sono in `assets/CREDITI.md`; il foglio provino è `_prova/fogli/foglio-esterne.jpg`.
- Per A:
  - Bolovtsova forme bianche con disco (apertura) e con onda;
  - Karchmit testa in polistirolo (apertura alternativa).
- Per B: Mosayebzadeh testa sfaccettata, che è gesso e non polistirolo.
- Comuni:
  - Granados sagome in laboratorio e modellatura a mano (è schiuma per tavole da surf: atmosfera, non prodotto);
  - Kozu cornice a soffitto (edilizia);
  - Lute torta bianca a piani (cake design);
  - Li stampa 3D;
  - Stacchini palcoscenico con fondale dipinto (scenografie).
- Mancano, e nessun archivio libero li ha in modo decente:
  - il **pantografo o il filo caldo che taglia il blocco**;
  - un **cornicione in EPS resinato** pulito;
  - un **oggetto fuori scala senza marchio**.
  Sono le prime foto da fare dal vero.

## 7. Riferimenti di alta gamma nel mestiere

Aperti dal vivo il 24/10/2026. Le prime schermate sono in `riferimenti/<nome>-1440-prima-schermata.jpg` e `-390-prima-schermata.jpg` (JPEG qualità 78); i font sono letti dal codice.

1. **Bonaveri** (bonaveri.com, manichini scolpiti per la moda, Italia).
   - Di alta gamma: un solo corpo scultoreo lucido a tutta pagina, menu di quattro parole in maiuscoletto minuscolo, testi in Libre Baskerville. È il mestiere vicino: forme scolpite per vetrine di lusso.
   - Da non riprendere: il nero pieno, la firma in corsivo "Obsession" sopra la foto, il bottone verde fisso nell'angolo.
2. **Millennium FX** (millenniumfx.co.uk, protesi ed effetti speciali, Regno Unito).
   - Di alta gamma: un solo lavoro in primo piano, così realistico da sembrare una foto. È il "finito che inganna l'occhio" della direzione A. Logo in serif e menu spaziato in Montserrat 300.
   - Da non riprendere: la colonna di menu grigio ardesia fissa a sinistra, il carosello con i puntini, il volto di persona come apertura (Poli-Art non ha questo materiale).
3. **Stage One** (stageone.co.uk, scenotecnica e strutture per eventi, Regno Unito).
   - Di alta gamma: a 390 la prima schermata è un'unica opera (un lampadario monumentale per una cerimonia), con titolo e cliente in piccolo in basso. Titoli in Resial Bold Condensed.
   - Da non riprendere: a 1440 resta nero con il solo logo anche dopo 16 secondi (la cattura lo mostra), la linguetta gialla "CONTACT", il menu nascosto.
4. **HiLT Projects** (hiltprojects.com, set, vetrine e oggetti per marchi, Brooklyn).
   - Di alta gamma: fondo bianco, logo a destra, menu di cinque parole minuscole in Helvetica Neue 15 px. I lavori parlano da soli.
   - Da non riprendere: la griglia fitta di foto tutte uguali e piccole senza gerarchia, che a 390 diventa una lunga colonna.
5. **Window France** (windowfrance.com, manichini e oggetti per le vetrine dell'alta moda).
   - Di alta gamma: sotto la testata, prodotti bianchi e neri su grigio chiarissimo, molta aria, titoli in Helvetica leggera grande.
   - Da non riprendere: il video di apertura, che non parte e lascia un riquadro nero, il menu ad hamburger su desktop, le schede con bordo.

Aperti ma scartati, con gli screenshot cancellati:
- Scott Fleary: testo bianco sopra un carosello, bottone arancione.
- Wētā Workshop: il video dà errore.
- Creative Fabrications: grafica da cartone animato.
- Factum Arte: impaginazione datata a riquadri.
- Orac Decor: pagina di verifica antibot.
- NMC, MDM Props, Atomic Props, Asylum FX: non raggiungibili o domini in vendita.

## 8. Per il piede

- **Logo**, in `assets/originali/`:
  - `logo-blu-1815x400.png`: scritta POLI-ART in un lineare sottile art déco con un punto al posto del trattino, blu ardesia #5F708E (4,55:1 sul fondo carta, al limite dell'AA). PNG a palette, abbastanza nitido per 2x fino a circa 900 px di larghezza.
  - `logo-bianco-1815x400.png`: la stessa scritta in bianco.
  - `logo-favicon-512.png`: solo "PO".
  - Nessun SVG, né nel codice né tra i caricamenti, e nessun PDF. Ricostruirlo in SVG si può (sono archi e aste), ma solo se viene fedele. Altrimenti il PNG a 2x.
- **Menu e pagine di oggi**: Home, Chi siamo, Servizi (Stampa 3D, Scenografie, Prototipi, Mockup, Loghistica, Edilizia, Cake design, Allestimento Eventi), Contatti, più la galleria nascosta Realizzazioni. Nel piede di oggi: logo con il riassunto, "Servizi" (sette voci), "Contatti".
- **Colonne proposte**:
  - Lavorazioni: Scenografie e vetrine, Edilizia e decori, Prototipi e mockup, Loghi in volume, Stampa 3D, Cake design.
  - Azienda: Chi siamo, Realizzazioni, Eventi con Palloncini WOW.
  - Contatti: 0444 614719, info@poli-art.it, via Tesinella 7, Grisignano di Zocco (mappa).
  - Seguici: Instagram, Facebook.
- **Newsletter: non ha senso.** Non ci sono notizie, cataloghi, collezioni o fiere proprie, e il lavoro è su commessa. I clienti privati ci sono (feste, torte), ma per quello basta Instagram. Al posto della newsletter, il link "Seguici su Instagram".
- **Riga legale**: Poli-Art di Zigliotto Manuel, P.IVA 03796810244 (da confermare, viene da un aggregatore), Privacy, Cookie. Niente capitale sociale (ditta individuale). REA e PEC non trovati.

## 9. Da confermare

- **Partita IVA** 03796810244, REA e PEC: dalla visura. Oggi la P.IVA manca sul sito, ed è obbligatoria.
- **Il 1986**: chi ha fondato l'attività e con quale ditta. La P.IVA di Manuel ha 11-20 anni. Si può scrivere "dal 1986" e "40 anni" nel 2026?
- **Indirizzo esatto**: 7, 7/A o 7/A/9.
- **Orari**: ufficio e ritiro.
- **Le macchine**:
  - quanti pantografi CNC e quali misure massime di blocco;
  - filo caldo o fresa;
  - quali stampanti 3D;
  - se fanno resinatura e verniciatura interne.
- **Le misure** dei pezzi fuori scala, che servono per la direzione B.
- **I permessi dei clienti** di cui si vedono i marchi nelle foto: il barattolo "nulla" che richiama Nutella, Paul & Shark, Converse, Blauer, ASUS, Busatta, Sterilgarda, Bertolo, Taplast, Carlo Gavazzi, Pradaxa, Longo, mosaico+, Named Sport, Pietrarredo, Leodari 75. Quali si possono mostrare o nominare?
- **Le persone** nelle foto (`Nutella1`, `Albero`, `Fotovoltaico-working`, `Corner-Convers*`): se una è Manuel e se vuole comparire.
- **La testa sfaccettata** (`Face-of-GOD`): di chi è l'opera, dove è esposta, e se Poli-Art l'ha costruita o solo rifinita. La sala curva `Pawson`: per chi è stata fatta, se si può dire.
- **Palloncini WOW**: la collaborazione è ancora attiva? Gli eventi restano nel sito?
- **"Loghistica"**: tenere il gioco di parole o chiamarla "Loghi in volume"?
- **Personaggi Disney** (Topolino, `ITALO`): da togliere, salvo licenza.
- **Social**: sono attivi? Con quale frequenza pubblicano?
- **Privacy e cookie**: servono i testi. Il modulo raccoglie dati senza informativa e Google Analytics parte senza consenso.
- **Il file `CALABRIA.tif`** (non scaricato) e `Testi.docx`, pubblici tra i caricamenti.
