# Stefano Aiti: analisi per la nuova home

Siti visti il 24/10/2026:
- https://www.stefanoaiti.com: home, About, Contatti e 72 pagine del portfolio, crawl in `_prova/crawl/`.
- https://www.aitistudio.it: 8 pagine.
- https://www.weddgraphy.it: home.
- La scheda di Matrimonio.com.

Le fonti sono citate come URL più la frase. "sa.com" sta per stefanoaiti.com, "ais.it" per aitistudio.it.

## 1. In breve

- **Chi**: Stefano Aiti, fotografo, con lo studio in Via Galileo Galilei 40 int. 26 a Mestrino (PD).
  - È una ditta individuale: P.IVA e codice fiscale personale stanno nel piede di tutti e tre i suoi siti.
  - Il marchio è il logo "AIT STUDIO" (le lettere AIT disegnate come un tetto). Nei testi lo studio si chiama "Studio Aiti" o "Aiti Studio".
  - Si è laureato allo Iuav in "Architettura" e in "Comunicazioni Visive e Multimediali". Fotografa dal 1995 ed è professionista dal 2008 (sa.com/about).
- **Cosa fa davvero**: la nota di partenza è giusta solo a metà. Il portfolio di sa.com, fermo al 2017-2018, mostra architettura e contract, still life di prodotto e corporate. Oggi però lo studio si presenta in un altro modo.
  - Il sito ais.it (2025) dice: "Siamo uno studio specializzato nella comunicazione per imprese e realtà nel settore delle infrastrutture stradali e costruzioni".
  - I servizi elencati su ais.it sono reportage di cantiere, fotografia aziendale, grafica delle livree dei mezzi, video e siti web.
  - C'è un terzo marchio per i matrimoni, "Weddgraphy" (weddgraphy.it e Matrimonio.com).
- **Per chi**:
  - Clienti con una pagina nel portfolio: Lago, Luceplan, Artufficio (sei banche e casse rurali arredate), Calearo, Calegaro, Bellissima Vodka (Bagnoli), Trek, Goppion Caffè, Saip, Superoro, Pianegonda e altri.
  - Clienti su ais.it: Salima Srl, Girardini SpA, Martini Silvestro e un cantiere Anas a Carpane.
  - "Riello" ha una pagina, ma contiene solo una pagina di brochure impaginata, non una foto.
- **Quanti**: due persone con nome e telefono, Stefano Aiti e Giulia Morandin (ais.it/contatti). Fatturato e collaboratori non sono pubblici.
- **Il punto**: c'è un autore con un archivio da rivista e una home che non lo dice. La home nuova deve servire le sue foto con una riga su chi è, e decidere come tenere insieme l'autore (architettura e still life) e lo studio dei cantieri (sez. 9).

## 2. Il sito di oggi

**Pagine**:
- Home: griglia di 14 progetti.
- About.
- Architecture, Corporate e Still Life: menu a tendina con 58 voci di progetto.
- Contatti, Informativa cookies, Trattamento dati personali.
- `portfolio-4-columns`: pagina demo del tema rimasta online, con 11 gallerie di gare MTB e la frase "4 columnsbrandingindustrial designmobilefoodmusicvideophotostravel The best way to come".
- In tutto le pagine portfolio sono 72; 14 non sono nel menu (gare di moto e MTB, Berny, Sfizio, Studio Guerra, Pianegonda, Costagroup).

**Testi veri (verbatim, sa.com/about)**:
- "Nel 1995 inizia l'infinito percorso fotografico rinascendo nell'anno 2008 come fotografo professionista, dando alla luce lo Studio Aiti ove attualmente la produzione si caratterizza per l'elevatissima qualità e pulizia d'immagine, con concreta, e crescente, specializzazione in fotografia di architettura, contract, still-life e corporate."
- "Lavoro con aziende orgogliose di ciò che fanno: imprimete con bellezza il vostro marchio, le foto sono comunicazione silenziosa, ma è il passaparola della qualità a creare il gran rumore!"
- La prima riga "Nato nel 1977 come uomo, cresciuto per studiare..." e la versione inglese ("Multimedial Visual Comunication", "clean imagine, whit") vanno riscritte.
- Badge "professionista socio di: associazione nazionale fotografi professionisti" (immagine `tau.jpg`, TAU Visual).

**Testi veri (verbatim, ais.it)**:
- "ideazione, realizzazione ed editing vengono svolti totalmente da noi e con la nostra attrezzatura".
- "catturare non solo l'essenza fisica di un cantiere, ma anche la sua storia, il suo processo e il suo impatto sul territorio circostante".
- "Realizziamo monografie aziendali come autentici racconti per immagini della vostra realtà".
- "Decoriamo i veicoli con i vostri colori aziendali e il vostro logo".

Su nessuno dei siti ci sono numeri, premi o pubblicazioni.

**Tecnologia di sa.com**:
- WordPress 6.9.10 installato in `/website/`, tema Coffeebean (child), Redux, griglia "jquery-masonry-image-gallery".
- Contact Form 7 con honeypot, Real Cookie Banner, plugin "wp-copyrightpro".
- Font da Google: ABeeZee, Monda, Inconsolata, Nunito.
- Fatto da melabyte, piede "© 2018". La sitemap va dal 23/02/2017 al 15/09/2023.
- Nessuna meta description. Il telefono non è cliccabile (nessun `tel:` né `mailto:`). Il logo in testata è un PNG di 100x80.
- ais.it è un WordPress 7.1.3 con Avada e Slider Revolution, dello stesso autore (melabyte).
- weddgraphy.it è un Adobe Muse del 2015.

**Problemi a 1440** (`_prova/attuale/home-1440.jpg`, pezzi in `p1440/`):
- Non c'è un titolo né una frase: nessuno capisce chi è né cosa fa.
- Il menu è in inglese.
- La griglia mescola foto quadrate e rettangolari senza didascalie. In fondo restano tre caselle vuote con l'icona di caricamento che gira.
- Il piede è in monospazio grigio con "ADDRESS_", "MOBILE_", il codice fiscale personale e "This site is protected by wp-copyrightpro.com".
- La pagina progetto (`luceplan-1440.jpg`) ha una foto di testata a tutta larghezza sotto un menu semitrasparente, poi miniature fitte senza testo.

**Problemi a 390** (`home-390.jpg`, pezzi in `p390/`):
- La pagina è alta 8301 px: 14 foto una dopo l'altra, nessuna parola fino al piede.
- Non c'è scorrimento orizzontale.

Le prime schermate di ais.it e weddgraphy.it sono in `_prova/attuale/ais-*.jpg` e `wed-1440-prima.jpg`. Su ais.it c'è un riquadro grigio semitrasparente sopra la foto della pala.

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Stefano Aiti (ditta individuale; insegna "Stefano Aiti - FOTOGRAFO", "Aiti Studio") | piede di sa.com: "Stefano Aiti - FOTOGRAFO \| © 2018 \| P.IVA 04257170284"; piede di ais.it: "© Aiti Studio 2025 - P.IVA 04257170284" |
| P.IVA | 04257170284 | stessi piedi. La cifra di controllo è valida. Il codice d'ufficio 028 è Padova: è una mia lettura |
| Codice fiscale | personale, pubblicato nei piedi | sa.com e ais.it. Non va ripetuto nella home nuova, basta la P.IVA |
| Indirizzo | Via Galileo Galilei 40 int. 26, 35035 Mestrino (PD) | piede di sa.com: "ADDRESS_Via Galileo Galilei 40 int. 26 35035 Mestrino (PD), ITALY"; ais.it/contatti: "Il nostro studio si trova a Mestrino (PD), Via G. Galilei 40 int.26." |
| Telefono | +39 348 748 58 71 | piede di sa.com: "MOBILE_+39 348 748 58 71"; ais.it/contatti: "STEFANO AITI Tel. 348 7485871" |
| Email | stefano@stefanoaiti.com; info@aitistudio.it; info@weddgraphy.it | piede di sa.com; ais.it/contatti: "STUDIO info@aitistudio.it"; weddgraphy.it |
| PEC | stefanoaiti@pec.it | piede di sa.com |
| Collaboratrice | Giulia Morandin, "Tel. 333 18873930" | ais.it/contatti. Il numero ha una cifra di troppo: da verificare, e non va messo in pagina senza consenso |
| Anno | professionista dal 2008, fotografa dal 1995 | sa.com/about (frase citata in sez. 2) |
| Associazione | socio TAU Visual (associazione nazionale fotografi professionisti) | badge in sa.com/about |
| Matrimoni | "Stefano Aiti Weddgraphy": 9 recensioni, media 4,9, su Matrimonio.com dal 2016, prezzo "a partire da" 1.000 euro | https://www.matrimonio.com/fotografo-matrimonio/stefano-aiti-weddgraphy--e159440 |
| REA, capitale, dipendenti | non pubblici; il capitale non c'è perché è una ditta individuale | |

## 4. Materiale visivo

Ho guardato tutte le 948 foto del portfolio su 20 fogli provino (`_prova/fogli/`), più le 40 immagini di ais.it.
- In `assets/originali/portfolio/` ho tenuto 90 file (21 MB): le copertine dei progetti non sportivi e le foto migliori.
- In `assets/originali/aitistudio/` ci sono 40 file.
- Misure, soggetto e voti (qualità / forza come apertura, da 1 a 10) sono in `_prova/inventario-immagini.json`.
- Su sa.com non ci sono video. Su ais.it ci sono 4 video YouTube del canale di Salima Srl, che non ho scaricato.
- Misure: le copertine sono a 1900 px, tutte le altre a 1200 px sul lato lungo. Sono versioni web e servono gli originali.

| Gruppo | Esempi (id) | Qualità | Apertura | Giudizio |
|---|---|---|---|---|
| Still life su bianco | antenna Calearo (202), ciotola d'argento al sole (220), vaso di cubetti Marijke (638), sigillo Bellissima (122), gioielli Superoro (828) | 8-9 | 8-9 | il meglio: un oggetto, luce pulita, fondo chiaro. È esattamente la ricetta del committente |
| Architettura chiara | scala a chiocciola in marmo dall'alto (819, 1900x1900), oblò bianco di Brendola (67), ciminiera della Fornace Morandi (195), parete curva in legno (13) | 8-9 | 7-9 | luce morbida, verticali dritte, nessun effetto |
| Still life su nero | Trek Slash (855), fari Borromini (164), olio Saip (774), lampadario Hope (597) | 8 | 6 | tecnicamente perfette ma scure: per una sezione, non per l'apertura |
| Interni contract | banche Artufficio, Belludi, Studio 4 Marmicolor | 6-7 | 3-5 | corrette, a volte grandangolo spinto; da usare poche |
| Cantieri e mezzi (ais.it, 2024-2025) | Scania all'alba rasoterra (a3), stesa notturna davanti al Santo di Padova (a37), Volvo Salima (a26) | 7-8 | 6-7 | lavoro recente e forte, ma con colore e HDR molto spinti: va scelto con cura |
| Persone, moda, sport | Eastfur, Sweden, gare MTB e moto (circa 330 foto) | 5-6 | 1-3 | fuori registro: da togliere dalla home |
| Da escludere | brochure Riello (769), mockup e schermate di siti (a8-a12, a29-a34), schema Bomag (a0) | 2-3 | 0 | non sono fotografie |
| Logo e ritratto | favicon 512 completo; ritratto 667x1000 del 2016; ritratto dello studio in bianco e nero (a4) | | | ritratto vecchio e piccolo: va rifatto |

**Verdetto**: il materiale regge una home di alta gamma, ed è il migliore della campagna. In media vale 7,5 su 10, con una decina di foto da 8-9 come apertura. Ci sono tre limiti:
- le misure web: a 1440 a tutta larghezza reggono solo le copertine da 1900 px, e per gli schermi 2x servono gli originali;
- l'età: quasi tutto è caricato tra febbraio e marzo 2017;
- i diritti dei soggetti dei clienti (sez. 9).

## 5. Due direzioni artistiche

Prima un appunto sulle ispirazioni Graziella e N19: le uso al 10%. È un fotografo per aziende, non un marchio di moda. Ne prendo solo il bianco, le etichette piccole e i nomi dei clienti composti come testo. Lascio fuori il menu a tutta pagina, le comparse di Wix e la foto di moda.

**Direzione A, "Comunicazione silenziosa" (chiara, un oggetto)**
- Idea visiva: carta bianca. Al centro l'antenna Calearo (202) grande e nitida, oppure la ciotola d'argento al sole (220). Sopra, il titolo con le sue parole: "Le foto sono comunicazione silenziosa." Poi tre campi (Architettura, Still life, Industria e cantieri), una foto grande ciascuno, i clienti come elenco di nomi e una chiusura con "il passaparola della qualità".
- Immagini: solo still life su bianco e architettura chiara (202, 220, 638, 819, 67, 195). Al massimo un cantiere all'alba (a3).
- Tipografia: Switzer di Fontshare per i titoli, grande, peso 500, spaziatura stretta. Didascalie in IBM Plex Mono piccolo (cliente, luogo, anno): riprende il monospazio di oggi, ma ordinato.
- Colore: carta #F6F5F2, inchiostro #141414, grigio del logo #A9ADAC solo per filetti e marchio. Il colore viene dalle foto (ciotole, piastrelle Lago).
- Gesto: l'elenco dei clienti fa da indice. Al clic o al tocco su un nome cambia la foto grande accanto, con un cambio netto e senza dissolvenza.

**Direzione B, "Linee e luce" (architettura e cantiere, chiara su calce)**
- Idea visiva: la scala a chiocciola in marmo (819) a tutta larghezza, quadrata, con il titolo sotto in bianco. Poi la ciminiera della Fornace Morandi e l'oblò di Brendola. Una sola fascia scura, dove l'immagine lo chiede: il cantiere notturno davanti alla Basilica del Santo (a37), che lega l'autore allo studio dei cantieri.
- Immagini: architettura chiara (819, 195, 67, 232), industria (Saip 770, Scania a3) e una still life (220) come pausa.
- Tipografia: Archivo di Google, con le larghezze condensate per titoli e etichette in maiuscolo spaziato, come le lettere "STUDIO" del logo. Archivo normale per il testo.
- Colore: calce #EEEDE9, cemento #6E7270 (AA sul chiaro), nero #111111. Un solo accento: il mattone della Fornace #A4583A, solo nei numeri.
- Gesto: un provino. Una striscia di sei miniature numerate per progetto; al clic la foto grande cambia e la didascalia dice cliente e luogo. È lo strumento del mestiere, usato come navigazione.

## 6. Immagini sostitutive

Le foto sostitutive servono poco, perché il portfolio copre quasi tutto. Ho scaricato 8 foto Pexels in `assets/esterne/`, a 2400 px sul lato lungo. Su ogni pagina ho verificato la licenza (vale "Free"); URL, autori e licenza sono in `assets/CREDITI.md`. Nessuna è già usata in un'altra home della campagna.
- Studio e attrezzatura: due fari in studio bianco vuoto (Hendy, per la chiusura di A), studio con fondale (Dummer), studio in bianco e nero (Hc Digital), softbox su bianco (Eshnazarov).
- Il mestiere: banco ottico Toyo (Yarovoy), Crown Graphic (Morgan).
- Cantiere e infrastrutture: treppiede su un ponte stradale (Takhgiriev), fotografo su cestello elevatore (Khlystunov).

Vanno rifatte dal vero lo studio di Mestrino (sala di posa, banco), Stefano al lavoro in cantiere e un ritratto nuovo.

## 7. Riferimenti di alta gamma nel mestiere

Le prime schermate a 1440 e 390 sono in `riferimenti/` (JPEG, qualità 78).

1. **Hélène Binet** (helenebinet.com).
   - Alta gamma: pagina bianca, quattro foto in bianco e nero con didascalie piccole in Neue Haas Grotesk ("Peter Zumthor, photographs from 1997 – 2011"), menu di tre parole.
   - Da non riprendere: la fila di quattro immagini piccole tagliate al bordo destro.
2. **Iwan Baan** (iwan.com).
   - Alta gamma: una sola foto enorme (Museum of Fine Arts Houston) con la didascalia sotto, progetto e architetto. A 390 la foto diventa verticale e resta piena.
   - Da non riprendere: la barra grigia con il menu in Georgia piccolo, la ricerca e le icone social in testata.
3. **Marco Cappelletti** (marcocappelletti.com).
   - Alta gamma: una sola foto astratta di architettura bianca, centrata, con tanta aria. Menu "Index Info" in Styrene A.
   - Da non riprendere: il banner dei cookie che copre la foto e la foto piccola rispetto allo schermo.
4. **Andrea Martiradonna** (andreamartiradonna.com).
   - Alta gamma: una sola verticale in bianco e nero al centro, il nome in grotesk nero in alto a sinistra, due sole categorie, la P.IVA in piccolo nel piede.
   - Da non riprendere: il piede grigio chiaro a basso contrasto e le frecce del carosello a 390.
5. **Paolo Riolzi** (paoloriolzi.com).
   - Alta gamma: clienti di peso (la torre della Fondazione Prada) e foto luminose e pulite.
   - Da non riprendere: le foto sfalsate di misure diverse (le "strisce di altezze diverse" bocciate dal committente), il menu di otto voci in Times e il menu minuscolo a 390.

Scartato, in `riferimenti/scartati/`: Edward Burtynsky, perché un popup copre tutta la prima schermata.

## 8. Per il piede

- **Logo**:
  - `assets/originali/logo-ait-studio-tracciato.svg`: tracciato dal favicon 512 (`fav.png`), con nero #040000 e grigio #AAAEAD. A 900 px e a 120 px è fedele all'originale.
  - Originali: `logo-favicon-512.png` (484x375 utili), `logo-ait-studio-100x80.png` (testata di sa.com), `logo-aiti-studio-*` (lo stesso logo da ais.it).
  - Non ho trovato un vettoriale ufficiale.
- **Menu di oggi**:
  - sa.com: About, Architecture, Corporate, Still Life, Contatti, più le pagine Informativa cookies e Trattamento dati personali.
  - ais.it: Lo Studio, Fotografia (Reportage cantieri, Fotografia aziendale), Grafica & Web (Parco mezzi, Siti web), Video & Storytelling, Case History, Contatti.
- **Social**: nessuno. Non sono linkati su nessuno dei tre siti e non ne ho trovati con la ricerca. La colonna "Seguici" non va messa.
- **Newsletter**: non ha senso. Lavora su commessa per aziende, non ha notizie, fiere, cataloghi o collezioni, e i privati (i matrimoni) passano da un altro marchio. Basta una riga nella NOTA.
- **Riga legale**: "Stefano Aiti Fotografo, P.IVA 04257170284", PEC stefanoaiti@pec.it, Privacy, Cookie. Niente REA né capitale (ditta individuale). Il codice fiscale personale non serve.

## 9. Da confermare

- **Identità della home**: autore (sa.com: architettura e still life) o studio per costruzioni e strade (ais.it)? Oppure una home sola con i due campi e i matrimoni fuori? E quale dominio resta?
- I diritti d'uso delle foto dei clienti, soprattutto i cataloghi Lago e i marchi in primo piano (Bellissima, Trek, Roncato, Salima, Volvo), e l'elenco dei clienti che si possono nominare.
- Gli originali ad alta risoluzione delle foto scelte (oggi 1200 e 1900 px) e lavori architettonici più recenti del 2017.
- Riello: quale lavoro è stato fatto? La pagina mostra solo una brochure.
- Il ruolo e il telefono di Giulia Morandin ("333 18873930" ha 11 cifre).
- Se è ancora socio TAU Visual.
- Se il marchio da usare è "AIT Studio", "Aiti Studio" o "Stefano Aiti Fotografo", e se esiste il logo vettoriale.
- Il testo About da riscrivere ("Nato nel 1977 come uomo..." e la versione inglese con errori).
- Se vuole togliere dal sito le gare di moto e MTB e la moda (Eastfur, Sfizio).
- Un ritratto nuovo e le foto dello studio di Mestrino.
