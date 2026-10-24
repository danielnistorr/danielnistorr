# L'Artificio Battagin: analisi per la nuova home

Sito: https://artificiobattagin.it/ (crawl, API WordPress e screenshot del 24/10/2026). Fonti citate come URL + frase; le pagine del sito sono indicate con il percorso dopo `artificiobattagin.it/`. Testi grezzi in `_prova/crawl/` (pagine, `posts-*.json`, `events.json`, `media-tutti.json`).

## 1. In breve

- **Chi**: A.B. s.r.l., insegna "L'Artificio Battagin", via della Croce Rossa 5/a, Padova. Bottega di famiglia: l'ha aperta Antonio Battagin con la moglie Gabriella Zoccarato; oggi "i figli Alessia e Matteo" sono "al timone dell'azienda" (`il-negozio/`).
- **Cosa fanno davvero (correzione alla nota)**: prima di tutto è un **negozio di belle arti**, non un laboratorio di cornici con un po' di colori. ATECO 47.62.20, "Commercio al dettaglio di articoli di cancelleria" (companyreports). Dentro ci sono tre cose: i reparti di belle arti (colori, carte, pennelli, tele, cavalletti, doratura, cartoleria), il **laboratorio interno di cornici** di Matteo, e l'area workshop **Artinpratica**. In più c'è uno shop online WooCommerce con 186 prodotti nella sitemap e spedizioni in tutta Italia.
- **Per chi**: artisti, illustratori, insegnanti, studenti e appassionati, adulti e bambini. Il claim è "Per i professionisti e gli amanti dell'arte" (home).
- **Da quando**: "Correvano gli anni '70" (`il-negozio/`). Un post del 30/03/2023 dice "50 anni fa, il nostro Artificio è nato come laboratorio di cornici artigianali", mentre la pagina Il negozio parla di una "bottega di pitture murali": le due versioni non coincidono (sez. 9). La srl è iscritta dal 31/08/2007 (aziende.it), lo stesso anno del trasloco in via Croce Rossa ("Dal 2007 lo store è situato in Via Croce Rossa").
- **Quanti**: da 2 a 5 addetti (companyreports), "2" dipendenti nel 2024 (aziende.it); fatturato 2024 di 472.047 euro (aziende.it). Su Instagram hanno "6,362 Followers, 882 Posts". Nel 2026 hanno messo in calendario 22 corsi e workshop (`wp-json/tribe/events`).
- **Il punto**: la parete degli angolari campione e Matteo con la cornice in mano sono le immagini più loro. Il racconto di famiglia ha cinque indirizzi in cinquant'anni. Oggi niente di tutto questo arriva in home.

## 2. Il sito di oggi

**Pagine**: Il negozio, Belle Arti, Cornici, Workshop (calendario The Events Calendar con biglietti), Shop Online, News (114 articoli, l'ultimo del 23/09/2026), Contatti, Carrello. Nel piede ci sono Condizioni di vendita, Resi e rimborsi, Spedizioni e pagamenti, Privacy e Cookie (iubenda).

**Testi veri essenziali (verbatim)**:
- Home: "L'artificio" / "Per i professionisti e gli amanti dell'arte". Non c'è altro testo.
- Il negozio (`il-negozio/`):
  - "Correvano gli anni '70 quando Antonio Battagin, forte di una lunga esperienza presso uno storico negozio di Padova, pensò di avviare in pieno centro la sua prima bottega di pitture murali."
  - "Ad accompagnare Antonio nell'impresa fu la moglie, Gabriella Zoccarato"
  - "i figli Alessia e Matteo, oggi al timone dell'azienda"
  - "Una famiglia amante dell'arte che a Padova ha contribuito a far crescere la cultura del Bello"
  - Le sedi: "Piazza De Gasperi", "Via Marin a Città Giardino", "Via Cavalletto", "negli anni '90 Via Sarpi, un bellissimo spazio che divenne anche luogo di laboratori creativi [...] nonchè corniceria e galleria per esposizioni d'arte", "Dal 2007 lo store è situato in Via Croce Rossa, un luminoso open space che, oltre ai reparti vendita, comprende anche il laboratorio interno di cornici e un angolo interamente dedicato agli atelier artistici per adulti e bambini."
  - "i preziosi consigli di uno staff di esperti"
  - "nello spazio dedicato denominato Artinpratica [...] Laboratori creativi, Workshop, Corsi di aggiornamento"
- Cornici (`cornici/`):
  - "Il reparto corniceria è uno dei vanti di L'Artificio. Ad occuparsene è Matteo Battagin, esperto corniciaio da oltre vent'anni. Nel laboratorio interno Matteo taglia e assembla cornici in vari stili, dal più classico al più contemporaneo [...] Una particolarità è il taglio del passpartout a 45° per un migliore effetto estetico."
  - cornici a struttura grossa: "Semplici, barocche, in qualunque dimensione, sono adatte anche per valorizzare specchiere arredamentali";
  - cornici sottili: "ideali per stampe, grafiche d'autore e fotografie [...] compresa la Street Art".
- Post "Laboratorio di cornici artigianali" (30/03/2023): "un piccolo laboratorio di cornici dove ARTE e ARTIGIANALITÀ si incontrano grazie a MATTEO che [...] porta avanti una tradizione insegnata dal padre Antonio" e "ogni quadro abbia bisogno del suo miglior "vestito" per essere valorizzato al massimo".
- Belle Arti (`belle-arti/`), dieci reparti con i marchi:
  - colori: Winsor & Newton, Lefranc Bourgeois, Liquitex, Maimeri, Talens, Kreul, Marabu;
  - carte: Canson, Clairefontaine, Fabriano, Magnani 1404, Arches, Saunders, Morgantina, Strathmore;
  - pennelli: Borciani & Bonazzi, Tintoretto, Da Vinci, SEM;
  - cavalletti: "rigorosamente realizzati in Italia. Costruiti in pregiato legno di faggio" (Mabef);
  - tele: "disponibilità di tele di diverse misure, soprattutto di grandi dimensioni e anche nel formato in rotoli";
  - incisione: "Fiore all'occhiello i prodotti a marchio Charbonnel";
  - cartoleria: Tassotti, Caran d'Ache, Stifflex.
- Oggetti a marchio proprio: la "tavolozza in ceramica marchiata L'Artificio Battagin, realizzata a mano [...] dall'artista Mialmart" (28/05/2025), le "Gift Card L'Artificio, da 25€ 50€ 100€" (01/12/2023) e la cassetta-cavalletto in faggio con il marchio inciso (foto `IMG_0393`).
- Popup all'apertura: "Iscriviti ALLA NOSTRA NEWSLETTER PER TE UNO SCONTO DEL 15% SUL PRIMO ACQUISTO NEL NOSTRO SHOP ONLINE".
- Sul sito non ci sono certificazioni, macchine o numeri.

**Tecnologia**:
- WordPress 7.1.3 con il tema **Wyatt** di Qode Interactive (tema da negozio di belle arti comprato e lasciato quasi com'era: nella libreria media restano "This. Is. Wyatt." e i loghi "W" del tema).
- Elementor 4.3.5, WooCommerce 11.2.1, Slider Revolution, The Events Calendar con Tickets, Contact Form 7 con reCAPTCHA, Yoast, LiteSpeed, iubenda, widget WhatsApp.
- Caratteri: Spectral 700 per i titoli, Josefin Sans 600 per il menu, Roboto.
- Il logo è un PNG di 250x117.

**Problemi a 1440** (`_prova/attuale/home-1440-prima.jpg`, `home-1440.jpg`, pezzi in `pezzi/`):
- All'apertura due finestre coprono la pagina: il popup newsletter (busta disegnata su verde) e il banner cookie. È la schermata scura della nota: la home sotto non è scura.
- La prima schermata è una macchia di vernice color salmone con "L'artificio" in serif: non si vedono né cornici, né negozio, né persone.
- Sotto c'è un vuoto bianco di circa 1.100 px. Le sette tessere del menu (Il negozio, Belle Arti, Cornici, Shop online, Workshop, News, Contatti) hanno titoli a opacità 0 e compaiono solo con le animazioni o al passaggio del mouse.
- Le pagine Cornici e Il negozio, nella cattura automatica a 1440, restano bianche sotto la testata: il contenuto entra con animazioni a comparsa. Da un browser normale probabilmente appare, ma in ritardo.
- Nel piede ci sono ragione sociale, REA e P.IVA, ma nessun telefono e nessuna email; c'è il badge reCAPTCHA.

**Problemi a 390** (`home-390.jpg`, `cornici-390.jpg`):
- La testata color salmone occupa 600 px solo per il nome.
- Seguono sette tessere quadrate a tutta larghezza con icone disegnate (porta, pennellata, cornice, borsa di tela, bicchiere di matite, megafono, segnaposto) **senza scritte**: non si capisce cosa siano.
- Il bottone verde WhatsApp "Come posso aiutarti?" copre il testo. Non c'è scorrimento orizzontale.
- Nella pagina Cornici la foto di Matteo c'è, ma il testo è in un riquadro grigio coperto dal bottone WhatsApp.

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | A.B. s.r.l. | piede di ogni pagina: "A.B.s.r.l."; `condizioni-di-vendita/`: "venduti dalla società A.B. s.r.l. con sede a Padova in via della Croce Rossa 5/a, C.F e P.I 04191710286"; VIES: "A.B. S.R.L." |
| P.IVA / CF | 04191710286 | piede: "Partita IVA 04191710286"; VIES (24/10/2026): "isValid": true |
| REA | PD 369492 | piede: "Numero di Registrazione REA PD369492"; companyreports.it/a.b._srl-04191710286 |
| Sede | via della Croce Rossa 5/a, 35129 Padova | `contatti/`: "Via Croce Rossa 5/a - 35129 Padova (PD)"; VIES: "VIA DELLA CROCE ROSSA 5/A 35129 PADOVA PD" |
| Telefoni | 049 7811043; 380 2308602 | `contatti/`: "+39 049 7811 043", "+39 380 2308602" |
| Email | negozio@artificiobattagin.it | `contatti/` |
| Altra email | info@artificiobattagin.it | locandina dell'evento Tintoretto del 23/03/2024 (`2024-02_ArtificioBattagin_INSTA_EVENTO.jpg`): "Informazioni: info@artificiobattagin.it" |
| PEC | info@pec.artificiobattagin.it | aziende.it/a-b-s-r-l-PD (letta tramite WebFetch; la pagina risponde 403 a curl) |
| Iscrizione | 31/08/2007 | aziende.it: data di iscrizione |
| Capitale sociale | 10.000 euro | aziende.it |
| ATECO | 47.62.20 "Commercio al dettaglio di articoli di cancelleria" | companyreports |
| Fatturato | 2025: 424.167 euro (companyreports); 2024: 472.047 euro, 2023: 492.779, 2022: 459.824 (aziende.it) | |
| Addetti | "da 2 a 5" (companyreports); 2 nel 2024 (aziende.it) | |
| Orari | non pubblicati sul sito. Cylex (aggiornato il 21/11/2025) indica lunedì solo pomeriggio, domenica chiuso, martedì 09:00-12:30 e 15:30-19:00 | cylex-italia.it/padova/artificio-a-b--s-r-l--11213925.html: da confermare |
| Social | Instagram e Facebook | link nel piede: https://www.instagram.com/lartificiobattagin/ ("6,362 Followers, 237 Following, 882 Posts"); https://www.facebook.com/artificiobattagin/ (pagina chiusa senza login) |

## 4. Materiale visivo

Ho scaricato 119 file (circa 20 MB) in `assets/originali/`, con nomi `AAAA-MM_<file>`. Sono le immagini delle pagine, i loghi e le foto di negozio, laboratorio e workshop. Ho escluso le circa 1.100 foto di prodotto dello shop, che sono immagini dei fornitori. L'inventario con misure, soggetto e voti (qualità / apertura) è in `_prova/inventario-immagini.json`; i fogli provino sono in `_prova/fogli/`. Nella libreria ci sono due mp4 (la demo del tema e un video da telefono del 2024): non li ho scaricati.

| Gruppo | Misure | Qualità | Apertura | Giudizio |
|---|---|---|---|---|
| **Parete degli angolari** campione: spigoli a V in colonne, ori, argenti, colori (`2023-05_cornici-per-grafica.jpg`) | 1000x562 | 7 | 7 | la più loro e la più grafica; servizio professionale del 2023 |
| **Matteo** regge una cornice rossa e oro davanti alla parete (`2023-05_matteo.jpg`, anche quadrata 1080) | 1000x562 | 7 | 7 | la persona vera del laboratorio, sorriso, luce buona |
| Cornici barocche argento e oro su cavalletto (`2023-04_cornici-1.jpg`) | 1000x562 | 7 | 6 | profondità bella, un po' affollata |
| Cavalletti in faggio nel reparto (`2023-07_IMG_7395-2-scaled.jpg`) | 2560x1707 | 7 | 6 | **l'unica foto d'ambiente grande** |
| Cassetta-cavalletto in faggio con il marchio inciso, su grigio (`2024-07_IMG_0393-scaled.jpg`) | 2560x2560 | 7 | 6 | un oggetto loro, still life da studio; il fondo grigio sfumato è datato |
| Reparto cornici con cornici tonde dorate (`negozio-cornici`), matite numerate (`matite-1`), pennelli, tele, stecche | 1000x562 | 6-7 | 3-5 | dello stesso servizio, buone come seconde immagini |
| Foglia oro su azzurro (`post-doratura-1`) | 1080x1080 | 6 | 4 | colore e materia |
| Viste grandangolari del negozio, area Artinpratica | 1000x562 e 1080 | 4-5 | 2-3 | documentarie, pavimento blu e neon; per Chi siamo |
| Still life di prodotti di marca (Cotman, Bruynzeel, Winsor & Newton, Caran d'Ache) | 2560 | 5-6 | 1 | sono foto di marchi altrui: no in apertura |
| Gift card su giallo (`IMG_9542`) | 2560x1707 | 6 | 3 | oggetto loro |
| Post social con testo, locandine dei corsi, foto da telefono (WhatsApp), bambini con i volti coperti | 1080-1600 | 2-4 | 0-1 | da non usare |
| Illustrazioni del tema, fasce a pennellate, mockup e rendering (`atelier-papiri`, `post1-famiglia`) | varie | 0-3 | 0-1 | da togliere |
| Logo (`logo-artificio-battagin-250x117.png`) | 250x117 | 4 | 0 | serve il vettoriale (sez. 8) |

**Verdetto: 6 su 10.** Il soggetto regge una home di alta gamma, la risoluzione online no. Le tre foto migliori (angolari, Matteo, cornici barocche) vengono da un servizio professionale del 2023 ma sul sito sono a 1000 px: a 1440 reggono a metà larghezza, non a tutta pagina. Bisogna chiedere gli originali al fotografo. Grandi e buone ci sono solo i cavalletti e la cassetta col marchio. Manca il gesto del mestiere: il taglio a 45°, il passepartout, l'assemblaggio al banco. Per la proposta useremo le foto loro dove reggono e i segnaposto della sez. 6.

## 5. Due direzioni artistiche

Diverse dalla Bottega dell'Arte di Mestrino (calce e noce, portone restaurato, Zodiak con General Sans, oro brunito): qui il soggetto è la cornice come vestito del quadro, e il colore viene dalla parete degli angolari e dal logo.

**Direzione A, "Il miglior vestito" (chiara, un solo oggetto)**
- **Idea visiva**: una sola cornice vera, grande e nitida, appesa a un muro chiaro con la luce di finestra; accanto il titolo grande con le loro parole, "Ogni quadro ha bisogno del suo miglior vestito" (dal post del 30/03/2023). Poi poche sezioni: Matteo al banco ("esperto corniciaio da oltre vent'anni"), la parete degli angolari come unica foto larga, i cinque indirizzi della famiglia in una riga, e la chiusura.
- **Immagini**: still life chiari, frontali, un oggetto per inquadratura. Segnaposto d'apertura: cornice in rovere su muro bianco (In The Making Studio). Poi `matteo.jpg`, `cornici-per-grafica.jpg` e `cornici-1.jpg`, da riavere a piena risoluzione; per le barocche, l'intaglio dorato di Giatras.
- **Tipografia**: Gambetta (Fontshare, ITF Free Font License) in tondo per i titoli, mai il corsivo, più Switzer (Fontshare, stessa licenza) per testi, recapiti e cifre tabellari.
- **Colore**: carta #F6F3EE, inchiostro #1F1B17, verde Battagin #17633A (il verde della scritta del logo, scurito: circa 6,6:1 sulla carta) per link e bottone del telefono, e un fondo turchese pallido #CFE7E4 (il colore della parete degli angolari) per una sola sezione.
- **Gesto**: "Prova il profilo". Cinque angolari presi dalla loro parete (dorata classica, barocca argento, sottile nera, colore, legno naturale): al clic o al tocco la cornice dell'apertura cambia profilo di netto, senza dissolvenza, con il nome sotto. Su telefono sono cinque bottoni in fila.

**Direzione B, "Per i professionisti e gli amanti dell'arte" (chiara, editoriale)**
- **Idea visiva**: in apertura la cassetta-cavalletto in faggio col marchio L'Artificio Battagin, rifotografata su carta bianca e scontornata con la sua ombra. Il titolo grande è il loro claim. Sotto, tre reparti in tre righe pulite (Belle arti, Cornici, Artinpratica) e il prossimo appuntamento del calendario.
- **Immagini**: still life su bianco con ombra morbida e colore pieno solo negli oggetti. Ci sono `IMG_0393` (da rifare su bianco) e `IMG_7395-2`, i godet di Sgro, le scatole d'acquerello di Almendrada, i pennelli di Razumnaya; per la verticale, la tela bianca in una stanza chiara di Declan Sun.
- **Tipografia**: Familjen Grotesk (Google Fonts, OFL) per tutto, titoli in 500 grandi e stretti, cifre tabellari per date, orari e prezzi dei corsi. Il logo a lettere disegnate resta l'unico segno colorato.
- **Colore**: bianco carta #FAFAF7, inchiostro #161616, grigio #5C5852 per i testi secondari, un solo accento terracotta #B4492F (il #DE7A60 del sito di oggi scurito, circa 5,3:1 sul bianco).
- **Gesto**: "Cinque indirizzi". Una riga di anni e vie (Piazza De Gasperi, Via Marin, Via Cavalletto, Via Sarpi, Via Croce Rossa dal 2007): al tocco cambia di netto la frase verbatim della pagina Il negozio. Gli anni esatti delle prime quattro sedi vanno chiesti; finché mancano, solo i nomi delle vie.

**Ispirazioni Graziella e N19**: le uso pochissimo. Un negozio di belle arti con laboratorio di cornici non è moda né lusso, e il loro registro di menu a tutta pagina, etichette minuscole ed effetti di comparsa qui suonerebbe falso. Al massimo tengo l'idea di molta aria attorno a un solo oggetto, che è già nella ricetta del committente.

## 6. Immagini sostitutive

Ci sono 9 foto Unsplash in `assets/esterne/`, ridotte a 2400 px sul lato lungo. Ho verificato la licenza sulla pagina di ogni foto il 24/10/2026: "Free to use under the Unsplash License", nessuna Unsplash+. Nessuna compare nei CREDITI.md delle altre home della campagna. URL, autori e date sono in `assets/CREDITI.md`.
- **Aperture chiare**: cornice in rovere su muro bianco (In The Making Studio, `gx6NxtpgHqY`) per A; tela bianca in stanza chiara (Declan Sun, `piFLApvqtxY`) per B.
- **Cornici**: intaglio dorato (Margaret Giatras), cornice scura su intonaco (Gaspar Uhas), cornici in una cassa di negozio (Liana S).
- **Belle arti e workshop**: godet di acquerello (Maureen Sgro), scatole di acquerelli usate (Nicole Almendrada), pennelli su tavolozza (Jennie Razumnaya), mazzo di pennelli usati (Tasha Kostyuk).
- Manca un segnaposto del taglio a 45° e del passepartout: va fotografato dal vero da Matteo.

## 7. Riferimenti di alta gamma nel mestiere

Prima schermata a 1440 e 390 in `riferimenti/<nome>-1440.jpg` e `-390.jpg` (JPEG qualità 78), aperti dal vivo il 24/10/2026. I caratteri sono letti dal codice.

1. **Bourlet**, corniciai a Londra dal 1850 (bourlet.co.uk)
   - Cosa lo rende di alta gamma: in apertura **un solo angolo di cornice intagliata**, a V, su carta grigia, grande e nitido. Logo in maiuscolo con "EST. 1850", sei voci di menu, poi una frase serif verde. A 390 regge identico. È il riferimento più vicino alla direzione A, e l'angolare è lo stesso oggetto della loro parete.
   - Da non riprendere: il fondo grigio spento, la sezione successiva con l'opera d'arte di terzi in cornice nera.
2. **Arnold Wiggins & Sons**, corniciai fornitori della Corona (arnoldwiggins.com)
   - Cosa lo rende di alta gamma: una foto di cornici dorate in laboratorio con poca profondità di campo, maiuscolo spaziato, e subito sotto email e telefono in chiaro su fondo carta. Usa Alegreya Sans e Rubik.
   - Da non riprendere: la foto scura sotto la scritta bianca, le cinque tessere con il titolo sopra la foto.
3. **Lowy**, corniciai e restauratori a New York dal 1907 (lowy1907.com)
   - Cosa lo rende di alta gamma: la mano vera che ritocca una cornice dorata, a tutta pagina. Il marchio è un angolo di cornice in oro, come la L del logo Battagin. Usa Libre Baskerville con Gothic A1.
   - Da non riprendere: il bottone rosso "REQUEST QUOTE", il nome bianco centrato sulla foto, il video.
4. **L. Cornelissen & Son**, negozio di belle arti a Londra dal 1855 (cornelissen.com)
   - Cosa lo rende di alta gamma: la vetrina vera del negozio con l'insegna dorata come apertura e il menu dei reparti come quello di un'antica bottega. È la prova che un negozio di colori può raccontarsi come istituzione.
   - Da non riprendere: l'impianto da e-commerce di dieci anni fa, la colonna laterale, il menu su due righe.
5. **Sennelier**, colori per artisti a Parigi (sennelier-colors.com)
   - Cosa lo rende di alta gamma: un solo oggetto (un pastello in matita) in macro sul disegno vero, molto bianco attorno al logo, menu con poche voci.
   - Da non riprendere: il titolo bianco con ombra sulla foto, il bottone nero, Montserrat ovunque.

Scartati: John Jones (Londra), "upstream request failed"; Kremer Pigmente, verifica Cloudflare; Caran d'Ache, accesso bloccato; Pigment Tokyo, carosello affollato; Zecchi (Firenze), impianto datato.

## 8. Per il piede

- **Logo**: il migliore trovato è `assets/originali/logo-artificio-battagin-250x117.png`, un PNG con trasparenza. Le lettere sono disegnate: la L è un angolo di cornice dorata, la R ha un pennello, la I è una matita, poi un tubetto e un cerchio cromatico; sotto c'è "BATTAGIN" in verde. Esistono anche le icone quadrate a 512 (`logo-icona-512.png`, `logo-icona-lart-512.jpg`), che però mostrano solo "L'ART". Nel codice non c'è nessun SVG e non ho trovato PDF. Non lo ricostruirei in SVG: le lettere illustrate non verrebbero fedeli. Nel piede va usato il PNG a 125 px di larghezza (così è a 2x), e nel LEGGIMI va chiesto il vettoriale.
- **Voci di menu e pagine di oggi**: Il negozio (`/il-negozio/`), Belle Arti (`/belle-arti/`), Cornici (`/cornici/`), Workshop (`/workshop/`), Shop Online (`/shoponline/`), News (`/news/`), Contatti (`/contatti/`), Carrello, Condizioni di vendita (`/condizioni-di-vendita/`), Resi e rimborsi (`/resi-e-rimborsi/`), Spedizioni e pagamenti (`/spedizioni-e-pagamenti/`). Privacy e Cookie sono su iubenda. Le gift card stanno in `/product-category/idee-regalo/gift-card/`. Conviene tenere questi indirizzi.
- **Colonne proposte**: Negozio (Il negozio, Belle arti, Cornici su misura, Shop online, Gift card); Artinpratica (Workshop e corsi, News); Contatti (049 7811043 `tel:+390497811043`, 380 2308602 `tel:+393802308602`, negozio@artificiobattagin.it `mailto:`, via della Croce Rossa 5/a con link alla mappa; orari solo dopo conferma); Seguici (Instagram, Facebook).
- **Social veri**: https://www.instagram.com/lartificiobattagin/ e https://www.facebook.com/artificiobattagin/. Altri non ne ho trovati. Il widget WhatsApp c'è, ma il numero non è nel codice.
- **Newsletter: sì.** Ce l'hanno già: popup con "SCONTO DEL 15%" e campo nel piede con la casella "Acconsento a ricevere comunicazioni via email a fini promozionali e commerciali", su Contact Form 7, quindi senza un servizio di invio vero. Hanno clienti privati, promozioni a rotazione, 22 corsi nel 2026 e un articolo nuovo quasi ogni mese. Nel piede ci vanno campo email, bottone e consenso; il popup all'apertura va tolto. Nel LEGGIMI va scritto che va collegata a un servizio.
- **Riga legale**: A.B. s.r.l., P.IVA 04191710286, REA PD 369492. Il capitale sociale di 10.000 euro viene solo da aziende.it e va confermato prima di scriverlo. PEC info@pec.artificiobattagin.it (aziende.it).

## 9. Da confermare

- **L'origine**: bottega di pitture murali (`il-negozio/`) o laboratorio di cornici ("50 anni fa", post del 2023)? E l'anno esatto: "anni '70" non basta per scrivere "dal 197x".
- Gli anni delle cinque sedi (Piazza De Gasperi, Via Marin, Via Cavalletto, Via Sarpi, Via Croce Rossa dal 2007), per il gesto della direzione B.
- Orari di apertura: sul sito non ci sono; Cylex ne riporta di indicativi.
- Capitale sociale, PEC e anno di iscrizione vengono da aggregatori (aziende.it, companyreports), non da una visura.
- L'email da mostrare: negozio@ (sito) o info@ (locandine)?
- Il numero WhatsApp del widget: è il 380 2308602?
- Gli originali a piena risoluzione del servizio fotografico del 2023 (angolari, Matteo, cornici barocche, reparti), e chi li ha scattati.
- Se il marchio sulla cassetta-cavalletto (`IMG_0393`) è inciso davvero o aggiunto in grafica, e se la cassetta è un prodotto venduto con il loro marchio.
- Il ruolo di Alessia: il sito nomina Matteo per le cornici ma non dice di cosa si occupa lei.
- "Taglio del passpartout a 45°": serve una foto vera del gesto al banco.
- Il logo vettoriale.
- Quanto conta lo shop online rispetto al negozio: la home deve spingerlo o solo indicarlo?
