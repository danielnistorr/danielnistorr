# Plastificazione Bastianello: analisi per la nuova home

Sito: https://www.plastificazionebastianello.it (crawl e screenshot del 24/10/2026: home, 6 pagine di menu e piede, sitemap Yoast, libreria media di WordPress via `/wp-json/wp/v2/media`, 2 PDF). Le pagine del sito sono indicate con il percorso dopo il dominio. Testi estratti in `_prova/crawl/*.txt`, script in `_prova/script/`.

## 1. In breve

- **Chi**: Plastificazione Bastianello S.r.l., via dell'Industria 2, 36040 Grisignano di Zocco (VI). La srl è iscritta il **01/03/2004** (aziende.it), costituita il 15/01/2004 (companyreports.it); il sito dice "opera nel settore cartotecnico **da oltre 40 anni**" (`azienda/`): la storia prima del 2004 (ditta precedente, fondatore) non è pubblica.
- **Cosa fa davvero**: nobilitazione **conto terzi** di fogli stampati e astucci fustellati per chi produce packaging: finestratura (anche ad angolo), plastificazione e accoppiatura con film, verniciatura UV a fondo pieno o con riserve, verniciatura blister, serigrafia UV lucida, opaca e ad alto spessore. Il certificato BRCGS lo dice in una riga: "Finestratura (PVC, PP, rPET) anche ad angolo, verniciatura UV (a rilievo, lucida od opaca) anche serigrafica, trattamento a blister, laminazione (PP) di semilavorati in cartoncino teso anche in microonda per scatole di cartone (astucci)".
- **Per chi**: cartotecniche e stampatori che fanno astucci per alimentare (anche a contatto diretto), cosmesi e lusso. Nessun cliente nominato.
- **Quanti**: piccola: **9 dipendenti** nel 2022 e nel 2024, fatturato 2024 **€ 824.503** (aziende.it; companyreports dà la fascia "da 10 a 19"). Capitale € 110.000.
- **Correzioni alla nota di partenza**: (1) **non fanno scatole di lusso**: il settore si chiama "Packaging di lusso e shoppers" e significa film metallizzati, olografici, soft touch e antigraffio applicati agli stampati di altri. (2) La "verniciatura UV a rilievo" c'è (certificato, e "alto spessore" in `servizi/`), ma è serigrafica. (3) La **BRCGS** pubblicata è **scaduta**: i due certificati sul sito valgono fino al 05/03/2020 (grado C) e al 05/03/2021 (grado A). Va chiesto il certificato in corso prima di scriverla in pagina.
- **Il dettaglio solo loro**: il lucido su opaco. La loro foto migliore è un foglio nero con un damasco in serigrafia UV lucida che si accende solo a luce radente. È il mestiere in un'immagine: la stampa la fa un altro, loro la fanno brillare, proteggere, vedere attraverso una finestra.

## 2. Il sito di oggi

**Pagine** (menu, piede e sitemap, tutte 200): Home, Azienda, Servizi (ancore `#finestratura`, `#plastificazione`, `#verniciatura-uv`, `#verniciatura-blister`, `#verniciatura-serigrafica`), Settori (`#packaging-alimentare`, `#packaging-bio`, `#packaging-lusso`), Certificazioni, Contatti (modulo), Privacy policy, Cookie policy. Nessuna notizia, nessun articolo (`/wp-json/wp/v2/posts` vuoto), nessun catalogo. Pagine modificate l'ultima volta ad aprile 2022.

**Testi veri essenziali (verbatim)**:
- Home: h1 "Plastificazione Bastianello", sottotitolo "Impegno e volontà a tua completa disposizione."; citazione ripetuta in ogni pagina: "OPERANDO IN UN MERCATO IN CONTINUA EVOLUZIONE, LA STRATEGIA AZIENDALE È COSTANTEMENTE FOCALIZZATA ALLA MASSIMA SODDISFAZIONE DEL CLIENTE."
- `azienda/`: "Plastificazione Bastianello S.r.l è una azienda che opera nel settore cartotecnico da oltre 40 anni, specializzata nelle lavorazioni e nobilitazioni conto terzi dello stampato e del settore cartotecnico."; "Negli ultimi anni abbiamo messo in atto un piano di investimenti con l'obiettivo di aumentare la capacità produttiva e di migliorare ulteriormente i tempi di risposta".
- `servizi/`, finestratura: "La finestra viene realizzata su astucci o scatole e consente di vedere il prodotto inserito nella scatola."; "finestre in plastica trasparente, in pvc, pp, pet e materiali biodegradabili di diversi spessori e formati adatti al contatto alimentare"; "l'azienda si è, inoltre, specializzata nella finestratura ad angolo"; formati "da 15 x 20 cm fino ad arrivare a 100 X 140 cm, sia su teso che su microonda".
- Plastificazione e accoppiatura: "si applica una pellicola di un film plastico su cartone o fogli di carta"; "sia uno scopo estetico ... sia uno scopo di protezione"; "formati fino a 120 x 160"; plastificazione "in polipropilene e poliestere / in polietilene / con film metallizzati / con film olografici"; accoppiamento "con film idonei per contatto alimentare / con film speciali per rendere il prodotto finito interamente riciclabile con la carta / con film compostabili e biodegradabili".
- Verniciatura UV: "vernici lucide o opache"; "Possibilità di verniciatura a fondo pieno o con riserve."; fogli "da 43 x 60 cm fino a 115 x150 cm".
- Verniciatura blister: "Negli ultimi anni ci siamo specializzati nella verniciatura blister"; "stesura di collante all'acqua, che nell'applicazione della valva rinviene a caldo"; "blister pieno che con riserva nei formati che vanno da 50 x 70 cm sino a 88 x 126 cm".
- Verniciatura serigrafica: "La serigrafia UV ... si contraddistingue per la particolare brillantezza che conferisce ai colori"; "telai serigrafici e la successiva asciugatura degli stessi in speciali forni a raggi UV"; "effetti come: lucido, opaco ed alto spessore"; "f.to min 32 X 44 / f.to max 100 x 140".
- `settori/`: alimentare "rispettando le normative vigenti sui prodotti e materiali destinati al contatto con gli alimenti"; biodegradabile "in grado di poter essere smaltito direttamente nella raccolta differenziata della carta"; lusso e shoppers "Vari tipologie di film metallizzati, olografici, soft touch, antigraffio ... per rendere il prodotto visivamente elegante e allo stesso tempo delicato al tatto".
- `certificazioni/` e home: "Nel 2019 abbiamo ottenuto la Certificazione BRCGS Packaging Materials, considerato ormai un requisito necessario per operare nel settore alimentare."; due PDF, "2019" e "2020".
- Non ci sono: elenco macchine (marca, numero), numeri di produzione, clienti, orari, nomi delle persone.

**Tecnologia**: WordPress con tema su misura `pbastianello` della web agency piano-d.it ("Web agency" nel piede), PHP **7.4.33** (fuori supporto), nginx, Plesk, Varnish. Yoast SEO, Site Kit (GA4 G-X8NCETN8PX, Google Ads AW-10895612445), iubenda per i cookie, reCAPTCHA nel modulo, badge "Website Carbon". Font **Circular Pro** (commerciale, Lineto) Book, Bold, Black. Logo in SVG in linea nella testata. `theme-color` #cc3329.

**Problemi a 1440** (`_prova/attuale/home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-1440-fondo.jpg`, pezzi in `p1440/`; `servizi-1440.jpg`):
- Prima schermata: foto sfocata di una macchina (probabile repertorio), titolo centrato bianco col solo nome e lo slogan generico "Impegno e volontà"; il bottone porta a "Chi siamo", non a una lavorazione.
- Sotto: marchio BRCGS e testo su un certificato scaduto; poi cinque riquadri con **icone da catalogo** colorate (scatola, griglia, goccia, rulli) e tre per i settori (sacchetto, mondo con foglie, vestito con diamante e tacco).
- La "fascia sgranata": la foto in mosso `PARALLAX-bastianello.jpg` (2000x812, compressa) ripetuta in verticale per circa 1000 px sotto la citazione. Pagina alta **6622 px** quasi senza contenuto.
- Piede rosso pieno: indirizzo ma **niente telefono né email**, "Share Capital" in inglese, il badge di Website Carbon.
- Pagine Privacy e Cookie **vuote** (solo titolo). Nel modulo il campo "Message" è in inglese.
- `servizi/`: testo e foto alternati a zig zag con foto piccole; nel codice ogni sezione è ripetuta due volte.
- Refusi: "obbiettivo", "igenico-sanitaria", "Negl'ultimi", "Vari tipologie".

**Problemi a 390** (`home-390.jpg`, `home-390-prima-schermata.jpg`, pezzi in `p390/`; `servizi-390.jpg`):
- Prima schermata scura e sgranata, titolo spezzato in due righe di misure diverse.
- "CERTIFICAZIONE BRCGS" tocca i bordi dello schermo; ogni icona occupa una schermata: pagina alta **5014 px** per otto parole.
- Il banner iubenda copre il fondo; nel piede manca il telefono cliccabile. Non c'è scorrimento orizzontale.

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Plastificazione Bastianello S.r.l. | piede di ogni pagina: "© 2026 Plastificazione Bastianello S.r.l."; certificato BRCGS |
| P.IVA e C.F. | 03124050240 | piede: "P.I. e C.F. 03124050240"; aziende.it |
| Capitale sociale | € 110.000 i.v. | piede: "Share Capital: 110.000,00 € I.V."; aziende.it: "110.000 euro" |
| REA | VI-300667 | https://www.aziende.it/plastificazione-bastianello-s-r-l: "REA: VI-300667"; companyreports.it: "VI 300667". Non è sul sito |
| PEC | plastificazionebastianello@cgn.legalmail.it | aziende.it (non è sul sito) |
| Indirizzo | via dell'Industria 2, 36040 Grisignano di Zocco (VI) | `contatti/`: "V. Dell'industria, 2 / 36040 – Grisignano Di Zocco"; link "Visualizza Mappa" a Google Maps (45.48317, 11.71154) |
| Telefono | +39 0444 414040 | `contatti/`: "Telefono +39 0444 414040", `tel:+390444414040` |
| Email | info@plastificazionebastianello.it | `contatti/`, `mailto:` |
| Fax, orari | non pubblicati | |
| Iscrizione / costituzione | 01/03/2004 (CCIAA Vicenza) / 15/01/2004 | aziende.it: "Data iscrizione: 01/03/2004"; https://www.companyreports.it/plastificazione_bastianello_srl-03124050240: "Data di costituzione 15/01/2004" |
| Anni di mestiere | "da oltre 40 anni" | `azienda/` |
| ATECO | 17.23 Fabbricazione di prodotti cartotecnici | aziende.it |
| Dipendenti | 9 (2022 e 2024) | aziende.it; companyreports: fascia "da 10 a 19" |
| Fatturato e utile | 2024 € 824.503 (utile € 26.114); 2023 € 944.161 (€ 33.069); 2022 € 857.832 (€ 13.938) | aziende.it |
| Contributi pubblici | "9 misure per 928.672 euro (2021-2023)", fonte RNA | aziende.it (coerente con il "piano di investimenti" di `azienda/`) |
| BRCGS | CSQA, "BRC Global Standard for Packaging and Packaging Materials Issue 5", site code 6464286, certificato BRC 2019-56344 (grado C, scad. 05/03/2020) e BRC 2020-56344 (grado A, audit 16-17/01/2020, scad. 05/03/2021), "High hygiene" | `wp-content/uploads/2022/03/Bastianello-Certificato-1.pdf` e `BASTIANELLO-BRC-1.pdf`. La directory BRCGS pubblica non risponde senza accesso: stato attuale non verificato |
| Social | nessuno | nessun link nel codice; ricerche web del 24/10/2026 senza risultati |

## 4. Materiale visivo

Scaricati 38 file in `assets/originali/` (14 foto, 7 file di logo, 3 icone PNG e 10 SVG da catalogo, il marchio BRCGS, 2 PDF, il manifest). Inventario con misure, pagina, soggetto e voti (qualità / forza come apertura) in `_prova/inventario-immagini.json`; fogli provino `_prova/fogli/foglio-foto.jpg` e `foglio-grafica.jpg`. **Nessun video** sul sito.

| Foto | Misure | Qualità | Apertura | Giudizio |
|---|---|---|---|---|
| Damasco in serigrafia UV lucida su nero opaco, foglio del cliente "TANCELEBRATE / PaolaP" (`VERNICIATURA-SERIGRAFICA-scaled.jpg`) | 2560x1707 | 8 | 7 | la migliore: luce da studio, il lucido su opaco si vede davvero. Ma è scura e il marchio del cliente è leggibile: serve il permesso o un taglio sul solo damasco |
| Film olografico che si svolge sulla plastificatrice (`plastificazione-1-scaled.jpg`, Nikon D5100) | 1696x2560 | 6 | 6 | soggetto solo loro e luminoso; in alto scaffali e scatole da tagliare |
| Finestratrice in movimento, astucci e ruote (`fienstartura-1-scaled.jpg`) | 2560x1696 | 6 | 5 | mosso voluto, quasi bianco e nero: buona per una sezione |
| Finestratrice ad altezza nastro (`finestartura-2-scaled.jpg`) | 2560x1696 | 5 | 4 | documentaria, neon |
| Verniciatrice serigrafica con fogli di astucci per biscotti (`SERIGRAFIA-1-scaled.jpg`) | 2560x1696 | 5 | 3 | vera ma affollata |
| Fogli "nathia" con UV a riserva (`VERNICIATURA-UV.jpg`) | 990x640 | 6 | 2 | piccola, marchio del cliente |
| Offset CMYK, oro sotto il rullo, carta fustellata, foglio in volo, macchina sfocata dell'apertura | 990-1920 px | 5-6 | 1-3 | **probabile repertorio** (stile da banca immagini; una si chiama `sostituisce-foto-famiglia.jpg`) |
| Fascia in mosso (`PARALLAX-bastianello.jpg`) | 2000x812 | 3 | 1 | da non usare |
| Tre persone in posa su nero, forse la famiglia (`azinda_chi-siamo.jpeg`, non in pagina) | 1000x668 | 5 | 1 | flash datato; solo con consenso |
| Icone di servizi e settori | 500x500 | 2 | 0 | da non usare |
| Logo vettoriale PB (`logo-orizzontale-vettoriale.svg`) | viewBox 2144.7x500 | 9 | 0 | pronto per testata e piede |

**Verdetto**: media **4 su 10**. Il materiale **non regge da solo una home di alta gamma**, ma è meglio della media della campagna: ci sono tre foto vere di reparto in 2560 px e una foto di prodotto di livello (il damasco). Per la proposta: il damasco e il film olografico come foto loro, i segnaposto della sez. 6 per l'oggetto chiaro d'apertura e per la finestra. Per il sito vero serve **mezza giornata di still life** (un astuccio finestrato su fondo carta, lo stesso foglio prima e dopo la verniciatura, il damasco senza marchio, un campione per ogni film: metallizzato, olografico, soft touch) **e mezza giornata in reparto** (bobina di film, finestratrice, forno UV, mani sul foglio), con luce controllata.

## 5. Due direzioni artistiche

Registro: un terzista di precisione che lavora per chi fa packaging di valore. Serve la calma di un fornitore di materiali di fascia alta (Derprosa, Burgopak, sez. 7), non il tono di un'agenzia di packaging. **Le ispirazioni Graziella e N19 qui non le uso**: il soggetto non è moda né lusso, è lavorazione industriale conto terzi; ne resta solo l'idea di molta aria e poche parole, che è già nella ricetta del committente.

**Direzione A, "La finestra" (chiara, un solo oggetto)**
- Idea visiva: prima schermata color carta, un solo astuccio bianco con la finestra trasparente, grande e nitido a destra, ombra morbida; a sinistra il titolo preso dal loro testo, per esempio "Nobilitiamo lo stampato", e una riga sotto: finestratura, plastificazione, verniciatura UV, conto terzi. Poi quattro sezioni: le cinque lavorazioni, i film, il packaging alimentare con la BRCGS (se confermata), la chiusura con la foto della finestratrice.
- Immagini: still life su carta chiara a luce di finestra, un oggetto per inquadratura (astuccio finestrato, foglio verniciato a riserva, campione olografico). Segnaposto: McManus astucci con finestra, Pelicular scatola bianca, Singh astuccio e vasetto; dal sito il film olografico e la finestratrice.
- Tipografia: una grotesk neutra per titoli e testo, Instrument Sans (Google Fonts, OFL) o Switzer (Fontshare, ITF Free Font License), cifre tabellari per i formati ("15 x 20", "100 x 140 cm"). Niente corsivi d'accento.
- Colore: carta #F6F4F0, inchiostro #171717, il rosso del logo #CC3429 solo per link, bottone e la P del marchio (contrasto 4,7:1 su carta, AA per il testo).
- Gesto: una riga di cinque voci (Finestratura, Plastificazione, Verniciatura UV, Blister, Serigrafica) cambia la foto e mostra la frase verbatim e il formato minimo e massimo della lavorazione, con un cambio netto e senza dissolvenze. Veri bottoni, usabili da tastiera.

**Direzione B, "Lucido su opaco" (scura ma pulita solo in apertura)**
- Idea visiva: il loro damasco a tutta larghezza, tagliato sul solo motivo senza marchio, con la luce radente che accende il lucido sul nero; sopra, in chiaro, un titolo grande e sicuro. Subito sotto si torna al chiaro, come nella home Tek.Lam che è piaciuta: scuro solo dove la foto lo chiede. Poi i film (metallizzato, olografico, soft touch) come tre campioni veri, la finestratura, la chiusura.
- Immagini: macro a luce radente di superfici nobilitate (UV lucido su opaco, alto spessore, olografico, soft touch); il film olografico della loro plastificatrice. Segnaposto: Bernal film olografico, Talmacs carta in rilievo, Pelicular scatola nera su grigio chiaro.
- Tipografia: Archivo (Google Fonts, OFL) con l'asse di larghezza, Expanded per i pochi titoli e normale per il testo; misure e formati con cifre tabellari.
- Colore: nero caldo #141312 solo nella prima schermata, carta #F4F2EE per il resto, rosso #CC3429 del logo come unico accento, argento #C9CBCE per filetti e numeri sul nero.
- Gesto: "formati a confronto", cinque rettangoli in scala reale tra loro (da 15 x 20 a 120 x 160 cm) che si accendono al tocco della lavorazione e dicono minimo e massimo: un dato che oggi è sepolto nel testo diventa l'informazione più utile per un cartotecnico.

Per il committente la A è la più vicina alla ricetta che gli piace: luminosa, un oggetto, tanta aria. La B ha una foto loro più forte, ma dipende dal permesso del cliente o da uno scatto nuovo del damasco senza marchio.

## 6. Immagini sostitutive

Ci sono 9 foto in `assets/esterne/` (8 Unsplash, 1 Pexels, al massimo 2400 px sul lato lungo). Licenza verificata sulla pagina di ogni foto il 24/10/2026, nessuna Unsplash+, nessuna già usata nella campagna (controllati tutti i `*-Sito/assets/CREDITI.md` per identificativo e per file CDN), nessuna generata dall'IA. URL, autori e licenze in `assets/CREDITI.md`; foglio provino `_prova/fogli/foglio-esterne.jpg`.
- Per A: Pelicular scatola bianca su bianco (apertura), McManus astucci con finestra e biscotto (finestratura), Singh astuccio e vasetto (settori), Mildlee scatola kraft (biodegradabile).
- Per B: Bernal film olografico, Talmacs carta a rilievo, Pelicular scatola nera su grigio chiaro (lusso).
- Comuni: Pons ventaglio di cartoncini colorati, Sakti macchina con fogli (solo se manca la foto vera: è una stampante, non una plastificatrice).
- Mancano, e nessun archivio libero li ha in modo decente: **la verniciatura blister** (valva su cartoncino), **un foglio con UV a riserva** su fondo chiaro e **la finestratura ad angolo**. Sono le prime tre foto da fare dal vero.

## 7. Riferimenti di alta gamma nel mestiere

Aperti dal vivo il 24/10/2026; prime schermate in `riferimenti/<nome>-1440-prima-schermata.jpg` e `-390-prima-schermata.jpg` (JPEG qualità 78); font letti dal codice.

1. **Derprosa** (derprosa.com, film per plastificazione: il fornitore diretto del loro mestiere).
   - Di alta gamma: una sola bobina di film soft touch su fondo grigio, nitida, con il nome del prodotto accanto; titolo "The laminating films brand" in Untitled Sans 600, menu di cinque parole, fondo #F7F7F7. È la direzione A già fatta: un materiale da terzisti presentato come un oggetto.
   - Da non riprendere: il carosello con frecce e contatore "2/8", il banner dei cookie scuro che a 390 copre metà schermo.
2. **Burgopak** (burgopak.com, packaging di design, Londra).
   - Di alta gamma: un solo astuccio nero con la scritta "GLAMOUR" in argento su fondo grigio chiaro, molta aria, menu di quattro parole in maiuscoletto piccolo. Mostra che il nero si può usare dentro una foto chiara.
   - Da non riprendere: la scritta bianca spaziata sopra la foto che si confonde con l'oggetto, il paragrafo minuscolo centrato, l'impianto Wix.
3. **Progress Packaging** (progresspackaging.co.uk, packaging di lusso).
   - Di alta gamma: macro di una scatola nera con scritte in rilievo e lucido a luce radente, titolo "PACKAGING PARTNERS" in Helvetica Neue Bold Condensed 70 px. È il riferimento della direzione B.
   - Da non riprendere: il testo centrato bianco sopra la foto, il bottone con bordo sottile, il marchio B Corp appoggiato nell'angolo.
4. **Leonhard Kurz** (kurz.de, lamine e finiture di superficie).
   - Di alta gamma: una superficie decorata con lamina in primo piano a tutta larghezza, titolo grande Roboto 300 e 700 a 68 px, motto "making every product unique" in alto.
   - Da non riprendere: il riquadro blu pieno sopra la foto, la barra di menu blu con sei voci a tendina, i puntini del carosello.
5. **Pusterla 1880** (pusterla1880.com, packaging di lusso, Italia e Francia).
   - Di alta gamma: fondo bianco, titolo su tre righe con parole in nero e in grigio ("CREATORI D'IMBALLAGGI RESPONSABILI E RAFFINATI") in Arquitecta, logo colorato come unico colore.
   - Da non riprendere: la foto di due persone con la mascherina, il timbro rotante "depuis 1880", i quattro numeri di telefono in testata.

Aperti ma scartati (screenshot cancellati): GPA Global (nessun prodotto, banner cookie), Pozzoli (video YouTube non disponibile), Hunter Luxury (video che resta grigio), Scodix e Holmen Iggesund (pagina vuota o spostata), BOBST (scelta della regione), Steinemann e Heiber + Schröder (impianto datato), GF Smith (registro troppo rumoroso), Cartotecnica Postumia, Lucaprint, Colorplan e MW Luxury Packaging (non raggiungibili), Delta Global e Arjowiggins (domini venduti).

## 8. Per il piede

- **Logo** (in `assets/originali/`):
  - `logo-orizzontale-vettoriale.svg`: copiato dal codice della testata, vettoriale vero (viewBox 2144.7x500), monogramma PB con la P rossa #cc3429 e la B nera, scritta PLASTIFICAZIONE / BASTIANELLO spaziata. Il secondo tracciato non ha colore: va impostato a mano (nero o bianco).
  - `logo-marchio-PB-1500.png`, `logo-marchio-PB-738x841.png`, `logo-favicon-PB-512.png`, `logo-favicon-PB-512-b.png`: solo il monogramma.
  - `logo-orizzontale-1538x382.jpg`: raster su bianco.
  - `logo-vecchio-bianco-843x596.png`: il marchio precedente (foglio arricciato con pennino), non più in pagina.
- **Menu e pagine di oggi**: Azienda, Servizi, Settori, Certificazioni, Contatti; nel piede Informazioni, I nostri servizi (cinque), I nostri settori (tre), Link utili (Privacy policy, Cookie policy, Web agency).
- **Colonne proposte**:
  - Azienda: Chi siamo, Certificazione BRCGS, Richiedi preventivo.
  - Lavorazioni: Finestratura, Plastificazione e accoppiatura, Verniciatura UV, Verniciatura blister, Verniciatura serigrafica.
  - Settori: Packaging alimentare, Packaging biodegradabile, Packaging di lusso e shoppers.
  - Contatti: +39 0444 414040, info@plastificazionebastianello.it, via dell'Industria 2, Grisignano di Zocco (mappa).
  - Niente colonna "Seguici": non ci sono social.
- **Social**: nessuno, né nel codice né in rete.
- **Newsletter: non ha senso.** Conto terzi B2B su commessa, nessuna notizia, fiera, catalogo o collezione, nessun cliente privato. Al posto della newsletter, il link "Richiedi preventivo".
- **Riga legale**: Plastificazione Bastianello S.r.l., P.IVA e C.F. 03124050240, Cap. soc. € 110.000 i.v., Privacy, Cookie. REA VI-300667 e PEC solo dopo conferma (vengono da aggregatori, non dal sito).

## 9. Da confermare

- **BRCGS**: è ancora valida? I certificati pubblicati sono scaduti nel 2020 e nel 2021. Senza il certificato in corso, in pagina non si scrive.
- I **"oltre 40 anni"**: la srl è del 2004. Quando è nata l'attività, con quale ditta e chi l'ha fondata? Chi sono le tre persone di `azinda_chi-siamo.jpeg` e se vogliono comparire.
- Il **parco macchine**: quante finestratrici, plastificatrici, verniciatrici UV e serigrafiche, di che marca; se il "piano di investimenti" ha portato macchine nuove da mostrare.
- Il **soft touch e l'antigraffio**: sono film che applicano loro o solo una voce di elenco?
- I **permessi**: il damasco di "PaolaP" e i fogli "nathia" sono lavori di clienti con il marchio in vista. Si possono mostrare? Quali clienti vanno oscurati?
- Le **foto di probabile repertorio** (offset CMYK, oro sotto il rullo, carta fustellata, foglio in volo, apertura di oggi): da dove vengono e con quale licenza.
- **REA, PEC, dipendenti, fatturato**: dati di aziende.it e companyreports.it (che non concordano sui dipendenti), da verificare con la visura prima di scriverli.
- Gli **orari** dell'ufficio e del ritiro merce, un eventuale fax, il nome di un referente.
- La **finestratura ad angolo** e il "microonda": quali formati e spessori, se c'è un campione da fotografare.
- Le pagine **Privacy e Cookie** sono vuote sul sito di oggi: servono i testi (iubenda è già attivo per i cookie).
