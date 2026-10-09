# Fonti tipografiche: accoppiate, caratteri Google Fonts poco abusati, regole d'uso

Ricerca del 6 ottobre 2026 per i siti WordPress + Elementor gratuito proposti alle PMI di Padova e Vicenza.
Domanda: che cosa dicono le fonti di mestiere sulle accoppiate di caratteri, quali famiglie di Google Fonts
sono di qualità alta e poco viste nei siti generati, quali sono abusate e quali regole d'uso separano un
lavoro professionale da uno generato.

Ogni affermazione ha la fonte accanto. I conteggi "FIU n" sono i lavori archiviati su Fonts In Use per quella
famiglia (pagina del carattere, controllata il 6/10/2026). I dati scaricati stanno in
`/tmp/claude-0/-home-user-danielnistorr/89486122-32ef-5f21-add5-5cbe6108c543/scratchpad/ricerca-caratteri/fonti-tipografiche/`.

---

## 0. In breve

1. Le fonti serie partono tutte dalla stessa domanda: serve davvero un secondo carattere? Prima si esauriscono
   pesi, stili, larghezze e grandezze ottiche del primo
   ([Google Fonts Knowledge](https://fonts.google.com/knowledge/choosing_type/pairing_typefaces),
   [Butterick](https://practicaltypography.com/mixing-fonts.html),
   [Pimp my Type](https://pimpmytype.com/pairing-fonts/)).
2. Se i caratteri sono due, ognuno ha un ruolo fisso e la differenza deve essere netta, oppure i due devono
   condividere lo scheletro (modello di forma). Il caso peggiore sono due caratteri simili in superficie e
   diversi nella costruzione, tipo Poppins con Open Sans
   ([font matrix](https://fonts.google.com/knowledge/choosing_type/pairing_typefaces_based_on_their_construction_using_the_font_matrix),
   [Pimp my Type](https://pimpmytype.com/bad-font-pair-hacks/)).
3. Il problema dei siti generati non è il carattere ma il default. Inter compare in 34 siti del giorno di
   Typewolf, e in 33 di questi è affiancato da almeno un carattere non Google, di solito un serif o un display
   con molta personalità (Reckless, Roslindale, GT Super, Editorial New...) ([Typewolf, Inter](https://www.typewolf.com/inter)).
   I modelli invece usano "la media del web": "Almost always Inter is their primary type choice"
   ([Pimp my Type, 2026](https://pimpmytype.com/about-ai-design/)).
4. Il default che ci riguarda direttamente: il kit di Elementor nasce con Roboto (primario, testo, accento) e
   Roboto Slab (secondario) ([codice Elementor](https://github.com/elementor/elementor/blob/main/core/kits/documents/tabs/global-typography.php)).
   Roboto è anche il Google Font più richiesto del web ([Web Almanac 2025](https://almanac.httparchive.org/en/2025/fonts)).
5. Esiste una "seconda ondata" di caratteri da IA: quelli che i prompt anti IA consigliano al posto di Inter
   (Space Grotesk, Playfair Display, Fraunces, Crimson Pro, Bricolage Grotesque, Newsreader, IBM Plex,
   JetBrains Mono, Satoshi, Clash Display) ([Anthropic cookbook](https://github.com/anthropics/claude-cookbooks/blob/main/coding/prompting_for_frontend_aesthetics.ipynb)).
   Usati nello stesso modo (serif ad alto contrasto su crema, etichette in maiuscolo spaziato, monospazio per i
   dati, una parola in corsivo) sono riconoscibili quanto Inter
   ([frontend-design skill](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)).
6. Nei lavori veri dei nostri settori lo schema ricorrente è: un carattere di titolo con un'idea precisa più un
   Google Font solido per il testo. Esempi: Beton Asfalti, conglomerati bituminosi a Trento (Nure + Archivo),
   Birrificio Ventitre in Irpinia (Annuario + Vollkorn), Champagne M. Marcoult (Tungsten + Spectral + Trade
   Gothic), Kakoulidis Vineyards (Publico + Commissioner), appartamenti nel bosco Waldquartier (Brice + Karla).
   Link nella sezione 5.
7. Verifica tecnica fatta qui: l'API CSS di Google Fonts toglie numeri minuscoli (`onum`), maiuscoletto
   (`smcp`), forme per maiuscolo (`case`) e set stilistici, che invece ci sono nei file completi del repository.
   Le cifre tabellari (`tnum`) restano quasi sempre. Per numeri minuscoli e maiuscoletto veri serve ospitare i
   file completi (sezione 4.6).

---

## 1. Cosa dicono le fonti di mestiere

### 1.1 Google Fonts Knowledge (articoli su abbinamento, lettura, spaziatura)

Testi ufficiali di Google Fonts, sorgenti pubblici su GitHub (`google/fonts/cc-by-sa/knowledge`).

- **Prima domanda: serve un secondo carattere?** "Do we really need a secondary typeface? Have we explored all
  of the possibilities on offer in our primary one, such as the various weights, styles, widths, and optical
  sizes?" Il secondo serve in quattro casi: cambio di contesto (dati accanto al testo), personalità del marchio
  da correggere, pesi o corsivi mancanti, lingue mancanti.
  [Pairing typefaces](https://fonts.google.com/knowledge/choosing_type/pairing_typefaces)
- **Parentele**: Jessica Hische propone di pensare i caratteri come fratelli, cugini, parenti lontani: un
  fratello condivide altezza della x, contrasto, larghezza e tono; un parente lontano un solo tratto, ma quello
  giusto. Jason Santa Maria: caratteri che non competono ma nemmeno si confondono; nel dubbio un serif e un
  sans. Stesso articolo.
- **Superfamiglie**: stessa struttura, stessa spaziatura, stesse proporzioni; esempi su Google Fonts:
  Merriweather e Merriweather Sans, Roboto Slab e Roboto Mono, Nunito e Nunito Sans, Quattrocento e
  Quattrocento Sans. "We should only introduce a secondary typeface if it can do something our primary
  typeface cannot." [Within a family / superfamily](https://fonts.google.com/knowledge/choosing_type/pairing_typefaces_within_a_family_superfamily)
- **Stesso designer o stessa fonderia**: la "mano" del disegnatore si riconosce e lega i caratteri (esempio
  Epilogue e Anybody di Etcetera Type).
  [Same designer or foundry](https://fonts.google.com/knowledge/choosing_type/pairing_typefaces_by_the_same_type_designer_or_type_foundry)
- **Font matrix** (Indra Kupferschmid): tre livelli, scheletro (dinamico, razionale, geometrico), carne
  (contrasto e grazie), pelle (dettagli). Tre regole: stesso scheletro va bene; combinazioni "in diagonale"
  (scheletro e carne diversi) contrastano senza disturbarsi; da evitare caratteri con stessa carne e scheletro
  diverso, perché "will create an irritating result".
  [Font matrix](https://fonts.google.com/knowledge/choosing_type/pairing_typefaces_based_on_their_construction_using_the_font_matrix)
- **Carattere affidabile**: copertura linguistica (Europa centrale e orientale inclusa), I l 1 ben distinti,
  regolare, corsivo, grassetto e grassetto corsivo, funzioni OpenType.
  [Choosing reliable typefaces](https://fonts.google.com/knowledge/choosing_type/choosing_reliable_typefaces)
- **Emozione e storia**: il lettore reagisce prima con l'emozione; molte associazioni vengono dalla storia dei
  caratteri (gotico medievale, display anni Settanta). Citazione di Matthew Carter: "Type is a beautiful group
  of letters, not a group of beautiful letters."
  [Emotive considerations](https://fonts.google.com/knowledge/choosing_type/emotive_considerations_for_choosing_typefaces)
- **Interlinea**: per il latino tra 115% e 150%; più piccolo il corpo, più aria; per i titoli grandi meno del
  corpo, 90-100% a 72 px; su mobile più stretta che su desktop (es. 150% largo, 130% mobile).
  [Choosing a suitable line height](https://fonts.google.com/knowledge/using_type/choosing_a_suitable_line_height)
- **Lunghezza della riga**: Bringhurst 45-75 caratteri; Material 40-60.
  [Understanding measure](https://fonts.google.com/knowledge/using_type/understanding_measure_line_length)
- **Spaziatura delle lettere**: più aperta per maiuscolo e maiuscoletto, mai troppo, leggermente negativa per i
  titoli grandi; attenzione a cifre e legature.
  [Track carefully or not at all](https://fonts.google.com/knowledge/using_type/track_carefully_or_not_at_all)
- **Numeri**: quattro tipi (lineari proporzionali, minuscoli proporzionali, lineari tabellari, minuscoli
  tabellari). Nel dubbio lineari proporzionali; tabellari per tabelle e orari; minuscoli nel testo corrente.
  [Understanding numerals](https://fonts.google.com/knowledge/introducing_type/understanding_numerals)
- **Corsivi finti**: conviene caricare anche il grassetto corsivo, altrimenti il browser lo sintetizza.
  [Foundations of web typography](https://fonts.google.com/knowledge/using_type/the_foundations_of_web_typography)

### 1.2 Butterick's Practical Typography

- **Mescolare caratteri**: "Mixing fonts is never a requirement, it's an option." La maggior parte dei
  documenti tollera un secondo carattere, pochi un terzo. Non è vero che si accoppiano solo serif e sans:
  "lower contrast between fonts can be more effective than higher contrast" (i giornali usano due serif).
  Ogni carattere deve avere un ruolo costante; mai due caratteri nello stesso paragrafo; metodo affidabile:
  caratteri dello stesso designer. [Mixing fonts](https://practicaltypography.com/mixing-fonts.html)
- **Regole chiave**: corpo 15-25 px sul web; interlinea 120-145%; riga 45-90 caratteri; maiuscolo solo per meno
  di una riga, con 5-12% di spaziatura; grassetto o corsivo, mai insieme; niente maiuscoletto finto.
  [Summary of key rules](https://practicaltypography.com/summary-of-key-rules.html),
  [All caps](https://practicaltypography.com/all-caps.html),
  [Bold or italic](https://practicaltypography.com/bold-or-italic.html)
- **Titoli**: pochi livelli (due meglio di tre); lo spazio sopra e sotto è l'enfasi migliore; grassetto, non
  corsivo; ingrandire "by the smallest increment necessary". Sulla scala modulare: "When your headings look
  right, they are right. The ratio is irrelevant." [Headings](https://practicaltypography.com/headings.html)
- **Caratteri liberi**: "in terms of design and craftsmanship, most free fonts are garbage", ma alcuni sono
  ottimi perché finanziati da chi aveva budget: Source Serif e Source Code (Adobe), IBM Plex, Cooper Hewitt,
  Charter. [Free fonts](https://practicaltypography.com/free-fonts.html)
- **Siti web**: i sistemi a template hanno accelerato "a new cargo cult of design habits... We swapped ugly for
  boring", e i caratteri di sistema sono stati sostituiti da "questionable free fonts, especially Google
  Fonts". [Websites](https://practicaltypography.com/websites.html)
- **Numeri alternativi**: proporzionali nel testo, tabellari per colonne di cifre; i minuscoli stanno male con
  il maiuscolo. [Alternate figures](https://practicaltypography.com/alternate-figures.html)

### 1.3 Typewolf (Jeremiah Shoaf)

- **Lista dei 40 migliori Google Fonts**: in testa DM Sans, Inter, Space Mono, Space Grotesk, Work Sans, Syne.
  Criterio per il testo: regolare, corsivo e grassetto, contrasto basso o medio, occhi ampi, aperture aperte,
  x alta. [Typewolf Google Fonts](https://www.typewolf.com/google-fonts). Nota: è la lista che tutti copiano, ed
  è anche per questo che quei nomi oggi sono ovunque.
- **Accoppiate Google "fresche"** (2016): volutamente caratteri nuovi e poco usati invece dei "Google Fonts
  staples like Open Sans and Merriweather"; titolo usato solo grande, testo con x alta, contrasto basso e
  corsivi. Coppie: Cormorant Garamond + Proza Libre, Libre Franklin + Libre Baskerville, Trirong + Rubik,
  Work Sans + Taviraj, Eczar + Gentium Basic (due serif: "a case where we can get away with breaking the
  rules"). [Five fresh pairings](https://www.typewolf.com/blog/google-fonts-combinations)
- **Schede dei caratteri** (con i siti che li usano):
  Alegreya "I rarely see Alegreya used on the web... one of the absolute best fonts available on Google Fonts"
  ([Alegreya](https://www.typewolf.com/alegreya)); Karla ha spaziatura un po' larga ma "tons of character"
  ([Karla](https://www.typewolf.com/karla)); Cormorant ha occhi "scandalously small", non da testo
  ([Cormorant](https://www.typewolf.com/cormorant)); su Work Sans nel 2015: "I'm predicting that we'll start to
  see Work Sans used all over the web" ([Work Sans](https://www.typewolf.com/work-sans)), cioè così nasce un
  abuso.
- **Dato utile** (conteggio fatto qui sulle schede Typewolf): Inter 34 siti, 33 con un carattere non Google
  accanto; DM Sans 6 su 6; Karla 25 su 28; Work Sans 16 su 21. I designer usano questi sans come voce di
  servizio sotto un titolo con personalità. [Inter](https://www.typewolf.com/inter),
  [DM Sans](https://www.typewolf.com/dm-sans)

### 1.4 Fonts In Use

Archivio indipendente di lavori reali, filtrabile per formato (Web) e settore (Food/Beverage, Travel,
Health...). Prevalgono stampa e identità, quindi i conteggi misurano la presenza nei lavori curati, non la
diffusione sul web.

- Nei 1438 lavori elencati sulle pagine delle 131 famiglie controllate (per le famiglie più usate la pagina ne
  mostra 59), 118 usano solo Google Fonts (selezione nella sezione 5, elenco completo in appendice).
- Critica utile su Aeon magazine: "All the webfonts in use are freebies from Google's repository... they feel
  like placeholders, waiting to be replaced with the real thing." Il rischio non è il catalogo ma la scelta
  fatta per comodità. [Aeon magazine](https://fontsinuse.com/uses/3730/aeon-magazine)
- Nei settori vicini ai nostri il titolo è quasi sempre un carattere con un'idea e il testo un Google Font
  solido (sezione 5.2).

### 1.5 Pimp my Type (Oliver Schöndorfer)

- **Accoppiare**: chiedersi se serve un secondo carattere ("For many projects one typeface with a Regular and a
  Bold weight, and maybe an Italic might be sufficient"); avere una ragione; scegliere prima la base; usare
  meno stili possibile. Tre livelli: superfamiglie; contrasto netto; costruzione (forma di a e g, aperture,
  asse, contrasto, altezza della x, larghezza, prova con la parola "Megatypos"). "Avoid to combine two fonts
  from the same category". [Pairing fonts](https://pimpmytype.com/pairing-fonts/)
- **Coppie sbagliate**: Poppins con Open Sans irrita perché uno è geometrico e l'altro dinamico; si rimedia solo
  in parte con peso, corpo, maiuscolo, distanza. [Bad font pair hacks](https://pimpmytype.com/bad-font-pair-hacks/)
- **IA**: "AI models were trained on the average of the web. So they repeat mediocrity by imitating generic
  cookie-cutter templates and often using the same Google Fonts. Almost always Inter is their primary type
  choice." [About AI design, maggio 2026](https://pimpmytype.com/about-ai-design/). ChatGPT propone prima
  "the familiar, overused typefaces like Roboto or Open Sans", poi Quicksand per un'interfaccia, scelta
  sbagliata. [Quicksand](https://pimpmytype.com/chatgpt-font-fail/)
- **Abusati**: "Montserrat is horribly overused" ([Montserrat](https://pimpmytype.com/montserrat-font-pairs/));
  Inter "dramatically overused... in headings it soon looks very generic or dull"
  ([Inter pairings](https://pimpmytype.com/inter-pairings/)).
- **Liberi ma buoni**: League of Moveable Type, Beautiful Webtype, Indestructible Type (Jost, Besley), Fontshare,
  UNCUT; con l'avvertenza "some fonts are pretty popular, thus overused".
  [Free & paid quality fonts](https://pimpmytype.com/free-quality-fonts/)
- **Ospitare in proprio**: "If you want consistency, self-host your fonts" (dopo l'aggiornamento di Inter su
  Google Fonts). [Google Fonts hosting](https://pimpmytype.com/google-fonts-hosting/)
- Le sue scelte libere della rubrica Font Friday includono Andada Pro, Asap, BioRhyme, Commissioner, Geologica,
  Host Grotesk, Newsreader, Piazzolla, Rasa, Signika, Young Serif.
  [Open source nel suo catalogo](https://pimpmytype.com/font-license/open-source/)

### 1.6 Fonderie libere e come servirle con Elementor gratuito

- **The League of Moveable Type** (2009): "the first open-source type foundry", nata "to raise the design
  standards of the web" ([manifesto](https://www.theleagueofmoveabletype.com/manifesto)). Del loro catalogo
  ([theleagueofmoveabletype.com](https://www.theleagueofmoveabletype.com/)) sono su Google Fonts, fra gli altri,
  League Gothic (revival di Alternate Gothic), League Spartan, Sorts Mill Goudy, Fanwood Text, Linden Hill,
  Goudy Bookletter 1911, Prociono e Raleway
  ([scheda League Gothic](https://github.com/google/fonts/blob/main/ofl/leaguegothic/DESCRIPTION.en_us.html)).
- **Velvetyne** (Francia): associazione dal 2010, caratteri con licenze libere; 397 lavori su Fonts In Use
  (Sporting Grotesque, Tiny, Le Murmure, Pilowlava, Avara, Compagnon). Quasi tutti espressivi, adatti a cultura
  ed eventi, non a una carpenteria. [Velvetyne su Fonts In Use](https://fontsinuse.com/foundry/1853/velvetyne)
  (il sito velvetyne.fr il 6/10/2026 dava errore 500).
- **Collletttivo** (Italia): fonderia open source, 16 caratteri (Apfel Grotezk, Sinistre, Messapia, Coconat,
  Ronzino, Absans); 86 lavori su Fonts In Use, Apfel Grotezk il più usato.
  [collletttivo.it](https://www.collletttivo.it/), [su Fonts In Use](https://fontsinuse.com/foundry/2875/collletttivo)
- **Fontshare** (Indian Type Foundry): gratis anche per uso commerciale, ma i caratteri "Closed Source" (licenza
  FFL) non si possono passare al cliente: "If your client wants to use a font that you have downloaded, they
  must download it themselves". [FAQ](https://www.fontshare.com/faq), [licenze](https://www.fontshare.com/licenses/itf-ffl).
  In più Satoshi, Clash Display e Cabinet Grotesk sono proprio quelli che il cookbook Anthropic suggerisce per
  lo stile "Startup" (sezione 3.4).
- **Come servirli**: Elementor ha l'opzione "Load Google Fonts Locally"; dalla 3.32.1 è facoltativa e spenta di
  default; Elementor scrive che senza richieste a Google "no user data is shared externally", utile per il GDPR
  ([Elementor help](https://elementor.com/help/load-google-fonts-locally)). Per file non Google (Velvetyne,
  Collletttivo) o per Google Fonts ospitati in locale c'è il plugin gratuito Custom Fonts di Brainstorm Force,
  compatibile con Elementor ([wordpress.org](https://wordpress.org/plugins/custom-fonts/)).

### 1.7 Altre fonti

- **The Elements of Typographic Style Applied to the Web** (Bringhurst portato in CSS): "Don't compose without a
  scale" ([3.1.1](http://webtypography.net/3.1.1)); 45-75 caratteri, 66 ideale ([2.1.2](http://webtypography.net/2.1.2));
  maiuscolo e maiuscoletto spaziati del 5-10% ([2.1.6](http://webtypography.net/2.1.6)); numeri minuscoli nel
  testo, lineari con il maiuscolo ([3.2.1](http://webtypography.net/3.2.1)).
- **I Love Typography**: oggi è soprattutto un negozio di fonderie indipendenti; non ho trovato un articolo
  recente sull'abbinamento. Pimp my Type segnala il suo strumento di ricerca CEDARS+
  ([Pimp my Type](https://pimpmytype.com/free-quality-fonts/)).

---

## 2. Famiglie Google Fonts di qualità alta e poco viste nei siti generati

Dati tecnici dal catalogo pubblico ([fonts.google.com/metadata/fonts](https://fonts.google.com/metadata/fonts))
e dalle schede del repository ([github.com/google/fonts](https://github.com/google/fonts)). "FIU n" = lavori su
Fonts In Use. "Rischio IA" segnala le famiglie che compaiono nei prompt anti IA o nelle liste SEO 2026
(sezione 3): non vanno escluse, vanno usate senza i tic del generato.

### Serif da testo e da titolo

**1. Source Serif 4** (Frank Grießhammer, Adobe). Transizionale ispirato a Fournier, pensato con Source Sans 3
([scheda](https://github.com/google/fonts/blob/main/ofl/sourceserif4/DESCRIPTION.en_us.html)). Pesi 200-900 con
corsivi; assi `opsz` 8-60 e `wght`. Testo lungo e titoli (grandezza ottica alta). Butterick lo cita fra i
liberi davvero buoni ([free fonts](https://practicaltypography.com/free-fonts.html)). Lavori: sito Aardman
Animations con Rubik ([FIU](https://fontsinuse.com/uses/58068/aardman-animations-website)), Juniper Design
([FIU](https://fontsinuse.com/uses/73234/juniper-design)); FIU 18. Limiti: tono neutro, da documentazione;
via API perde numeri minuscoli e maiuscoletto.

**2. Literata** (TypeTogether). Nata per Google Play Books, rifatta variabile
([scheda](https://github.com/google/fonts/blob/main/ofl/literata/DESCRIPTION.en_us.html)). Pesi 200-900 con
corsivi; `opsz` 7-72. Testo lungo, didascalie, titoli. Pimp my Type la propone come testo sotto titoli
geometrici ([Montserrat pairs](https://pimpmytype.com/montserrat-font-pairs/)). Lavori: giornale Rad und Tat
Berlin con CoFo Sans e Atkinson ([FIU](https://fontsinuse.com/uses/57645/rut-rad-und-tat-berlin-newspaper));
FIU 5. Limiti: voce da libro digitale, poco carattere nei titoli.

**3. Newsreader** (Production Type). Per lettura continua a schermo
([scheda](https://github.com/google/fonts/blob/main/ofl/newsreader/DESCRIPTION.en_us.html)). Pesi 200-800 con
corsivi; `opsz` 6-72. Titoli, sommari, citazioni, testo. Lavori: sito di L'Obs, titoli e citazioni in Text e
Display ([FIU](https://fontsinuse.com/uses/45802/l-obs-website)), Daylit Studio con Atkinson Hyperlegible
([FIU](https://fontsinuse.com/uses/79109/daylit-studio-website)), The HY Times con Libre Franklin
([FIU](https://fontsinuse.com/uses/79388/the-hy-times)); FIU 9. Limiti: rischio IA (lista "Distinctive" del
cookbook Anthropic); senza maiuscoletto.

**4. Spectral** (Production Type, commissionato da Google). Sette pesi con corsivi e maiuscoletto, pensato per
lo schermo ([articolo](https://github.com/google/fonts/blob/main/ofl/spectral/article/ARTICLE.en_us.html)).
Nessun asse variabile. Testo lungo e titoli classici. Lavori: etichette e sito di Champagne M. Marcoult
([FIU](https://fontsinuse.com/uses/50720/champagne-m-marcoult)), rivista letteraria Failles Flots Fils Flammes
([FIU](https://fontsinuse.com/uses/38063/failles-flots-fils-flammes-website)), Kick
([Typewolf](https://www.typewolf.com/site-of-the-day/go-kick)); FIU 25. Limiti: maiuscoletto e numeri minuscoli
solo ospitando i file completi; compare nella lista SEO di muz.li.

**5. Alegreya + Alegreya Sans** (Juan Pablo del Peral, Huerta Tipográfica). Scelta fra i 53 "Fonts of the
Decade" ATypI; ritmo dinamico, radice calligrafica, pensata per la letteratura
([scheda](https://github.com/google/fonts/blob/main/ofl/alegreya/DESCRIPTION.en_us.html)). Serif 400-900 e
Sans 100-900, entrambi con corsivi. Racconto, menu, pagine "chi siamo" di agriturismi e cantine. Typewolf: "one
of the absolute best" ([Alegreya](https://www.typewolf.com/alegreya)). Lavori: Jamie Wilson
([Typewolf](https://www.typewolf.com/site-of-the-day/jamie-wilson)), Maurizio Ilpiac Piacenza
([Typewolf](https://www.typewolf.com/site-of-the-day/maurizio-ilpiac-piacenza)), libri
([FIU](https://fontsinuse.com/uses/67506/cuanto-te-pesa-tu-peso-by-virginia-busnelli)); FIU 22 + 18. Limiti:
molto letterario, poco adatto a schede tecniche.

**6. Piazzolla** (del Peral, HT). Compatto, pensato per la stampa periodica, "distinctive voice" nei titoli
([scheda](https://github.com/google/fonts/blob/main/ofl/piazzolla/DESCRIPTION.en_us.html)). Pesi 100-900 con
corsivi; `opsz` 8-30. Lavori: Jornadas de Edición Universitaria con Alegreya Sans
([FIU](https://fontsinuse.com/uses/36172/jornadas-de-edicion-universitaria-10)), Hochschulen in der Pandemie
con IBM Plex Sans ([FIU](https://fontsinuse.com/uses/48644/hochschulen-in-der-pandemie)); FIU 8. Limiti: neri
pesanti ai pesi alti, pochi esempi web.

**7. Andada Pro** (Carolina Giovagnoli, HT). Slab organico a contrasto medio, da testo, premiato alla Biennale
Iberoamericana ([scheda](https://github.com/google/fonts/blob/main/ofl/andadapro/DESCRIPTION.en_us.html)).
Pesi 400-840 con corsivi. Testi caldi per ristoranti e agriturismi. Lavori: libro con Alegreya Sans
([FIU](https://fontsinuse.com/uses/42213/nhemombaraete-reko-ra-i-by-jose-vera)), Alba magazine
([FIU](https://fontsinuse.com/uses/54773/alba-magazine-14)); FIU 10. Scelta di Pimp my Type. Limiti: tono
rustico.

**8. Vollkorn** (Friedrich Althausen). "Quiet, modest and high quality text face for bread and butter use",
grazie scure e corpose ([scheda](https://github.com/google/fonts/blob/main/ofl/vollkorn/DESCRIPTION.en_us.html)).
Pesi 400-900 con corsivi; nel file completo maiuscoletto, numeri minuscoli, set stilistici. Lavori: Birrificio
Ventitre in Irpinia, sito e lattine, con Annuario di Resistenza
([FIU](https://fontsinuse.com/uses/46054/birrificio-ventitre-beers); il sito carica Vollkorn da Google Fonts),
Cedille con Lora ([Typewolf](https://www.typewolf.com/site-of-the-day/cedille)); FIU 9. Per agriturismi,
cantine, birrifici, trattorie. Limiti: fuori luogo per clinica o meccanica.

**9. Libre Caslon Text + Libre Caslon Display** (Impallari). Text ottimizzato per 16 px, Display per i titoli,
basato sui Caslon americani ([scheda](https://github.com/google/fonts/blob/main/ofl/librecaslontext/DESCRIPTION.en_us.html)).
Text 400 e 700 con corsivo; Display solo 400. Lavori: Federalist Reader
([FIU](https://fontsinuse.com/uses/79099/federalist-reader)), Mutt
([FIU](https://fontsinuse.com/uses/73605/mutt)); FIU 2 + 2. Limiti: pochi pesi, display senza corsivo.

**10. Besley** (Owen Earl, Indestructible Type). Clarendon antico con angoli appena arrotondati
([scheda](https://github.com/google/fonts/blob/main/ofl/besley/DESCRIPTION.en_us.html)). Pesi 400-900 con
corsivi. Titoli per artigiani, ferramenta, birrifici: il Clarendon ha tradizione di insegne e manifesti.
Lavori: Histoires sportives ([FIU](https://fontsinuse.com/uses/64055/histoires-sportives)); FIU 1. Limiti:
pochi lavori documentati.

**11. Zilla Slab** (Typotheque per Mozilla). Slab contemporaneo da Tesla, "unexpectedly sophisticated industrial
look" ([scheda](https://github.com/google/fonts/blob/main/ofl/zillaslab/DESCRIPTION.en_us.html)). Pesi 300-700
con corsivi veri. Titoli per industria e trasporti. Lavori: sito TriMet, titoli in Zilla Slab e testo in Source
Sans ([FIU](https://fontsinuse.com/uses/69330/trimet-phase-3)), Florestal
([FIU](https://fontsinuse.com/uses/67941/florestal)); FIU 6. Pimp my Type lo indica con Montserrat
([Montserrat pairs](https://pimpmytype.com/montserrat-font-pairs/)). Limiti: associato a Mozilla; nella lista
SEO di muz.li.

**12. Young Serif** (Bastien Sozeau). Old style pesante sul modello di Plantin Infant e ITC Italian Old Style
([scheda](https://github.com/google/fonts/blob/main/ofl/youngserif/DESCRIPTION.en_us.html)). Un solo peso,
niente corsivo. Solo titoli: gastronomia, macellerie, birrifici. Lavori: Tens con Karla
([Typewolf](https://www.typewolf.com/site-of-the-day/tens-sunglasses), il sito usa ancora Karla), Butter Meat
Co. ([FIU](https://fontsinuse.com/uses/46522/butter-meat-co-branding)), East Branch Brewing
([FIU](https://fontsinuse.com/uses/21836/east-branch-brewing-company)); FIU 5. Limiti: un peso; chiede un testo
sobrio accanto.

**13. Eczar** (Vaibhav Singh, Rosetta). Calligrafico e vivace, latino e devanagari; il carattere display cresce
con il corpo ([scheda](https://github.com/google/fonts/blob/main/ofl/eczar/DESCRIPTION.en_us.html)). Pesi
400-800, niente corsivi. Titoli con calore umano. Lavori: Orthopädie Kreuzberg, studio ortopedico a Berlino
("liveliness and human closeness" con Montserrat per la chiarezza)
([FIU](https://fontsinuse.com/uses/55445/orthopaedie-kreuzberg)), Thomas Schrijer
([Typewolf](https://www.typewolf.com/site-of-the-day/thomas-schrijer)); coppia Eczar + Gentium in
[Typewolf](https://www.typewolf.com/blog/google-fonts-combinations). Limiti: niente corsivo.

### Sans serif

**14. Libre Franklin** (Impallari). Interpretazione del Franklin Gothic di Benton (1912), nove pesi
([scheda](https://github.com/google/fonts/blob/main/ofl/librefranklin/DESCRIPTION.en_us.html)). Pesi 100-900 con
corsivi. Titoli e testo per industria, giornali, enti. Typewolf: con Libre Baskerville "evoking an established
and traditional feel" ([Typewolf](https://www.typewolf.com/blog/google-fonts-combinations)). Lavori: The HY
Times ([FIU](https://fontsinuse.com/uses/79388/the-hy-times)), Medeina Musteikyte, solo Libre Franklin
([Typewolf](https://www.typewolf.com/site-of-the-day/medeina-musteikyte)); FIU 15. Limiti: niente cifre
tabellari, nemmeno nel file completo (verifica sezione 4.6): no per listini e dati tecnici in colonna.

**15. Public Sans** (US Web Design System). Basato su Libre Franklin, "strong, neutral"
([scheda](https://github.com/google/fonts/blob/main/ofl/publicsans/DESCRIPTION.en_us.html)). Pesi 100-900 con
corsivi; cifre tabellari. Interfaccia, moduli, testo. Lavori: Gunpowder Mills con Avec
([FIU](https://fontsinuse.com/uses/79095/gunpowder-mills)), HETIME con Hawthorn
([Typewolf](https://www.typewolf.com/site-of-the-day/hetime)); FIU 6. Limiti: neutro, chiede un titolo con
carattere.

**16. Archivo** (Omnibus-Type, Héctor Gatti). Grottesco ispirato ai caratteri americani di fine Ottocento, nato
per i titoli; assi `wdth` 62-125 e `wght` 100-900 con corsivi
([scheda](https://github.com/google/fonts/blob/main/ofl/archivo/DESCRIPTION.en_us.html)). Industria, costruzioni,
macchine: stretto per i titoli, normale per il testo, una sola famiglia. Lavori: Beton Asfalti, conglomerati
bituminosi, Trento ([FIU](https://fontsinuse.com/uses/72654/beton-asfalti)), MycoTech
([FIU](https://fontsinuse.com/uses/79120/mycotech)), Kook Furniture
([FIU](https://fontsinuse.com/uses/49413/kook-furniture-website)); FIU 35. Limiti: già usato nei nostri siti
(GardensPav); nella lista SEO madegooddesigns (con Lora).

**17. Chivo** (Omnibus-Type). Primo grottesco della fonderia: Black per i titoli, Regular per leggere
([scheda](https://github.com/google/fonts/blob/main/ofl/chivo/DESCRIPTION.en_us.html)). Pesi 100-900 con
corsivi, più Chivo Mono. Lavori: Stan's Grill con Vertigo ([FIU](https://fontsinuse.com/uses/60220/stan-s-grill)),
SFL e The Ministry of Print, solo Chivo ([Typewolf](https://www.typewolf.com/chivo)); FIU 12. Limiti: su Aeon è
stato letto come "placeholder" ([FIU](https://fontsinuse.com/uses/3730/aeon-magazine)): serve una ragione.

**18. Asap** (Omnibus-Type). Angoli appena arrotondati, stessa larghezza in tutti gli stili, quindi cambiando
peso il testo non scorre; assi `wdth` 75-125 e `wght` 100-900
([scheda](https://github.com/google/fonts/blob/main/ofl/asap/DESCRIPTION.en_us.html)). Schede prodotto,
etichette, alimentare. Lavori: Carrs Pasties ([FIU](https://fontsinuse.com/uses/48812/carrs-pasties-brand-refresh));
FIU 2. Limiti: tono amichevole e commerciale.

**19. Saira** (Omnibus-Type). Sistema con `wdth` 50-125 e `wght` 100-900, dall'Extra Condensed all'espanso
([scheda](https://github.com/google/fonts/blob/main/ofl/saira/DESCRIPTION.en_us.html)). Titoli tecnici per
costruttori di macchine. Lavori: Afrikamera ([FIU](https://fontsinuse.com/uses/71538/afrikamera)); FIU 1.
Limiti: forme squadrate che scivolano nel cliché sportivo o automobilistico; pochi lavori.

**20. Overpass** (Delve Fonts). Interpretazione della Highway Gothic della segnaletica USA
([scheda](https://github.com/google/fonts/blob/main/ofl/overpass/DESCRIPTION.en_us.html)). Pesi 100-900 con
corsivi, più Overpass Mono. Impianti, energia, logistica. Lavori: BiteSize Learning con Fraunces
([FIU](https://fontsinuse.com/uses/56266/bitesize-learning-rebrand)), sito Polaron Solartech
([FIU](https://fontsinuse.com/uses/35141/polaron-solartech)); FIU 3. Limiti: associazione forte con la strada
americana.

**21. Fira Sans** (Erik Spiekermann, Carrois). Per Firefox OS, vicino a FF Meta, tre larghezze con corsivi e un
monospazio ([scheda](https://github.com/google/fonts/blob/main/ofl/firasans/DESCRIPTION.en_us.html),
[Typewolf](https://www.typewolf.com/fira-sans)). Testi tecnici, tabelle, schede. Lavori: sito della
commissione 6 gennaio con Merriweather ([FIU](https://fontsinuse.com/uses/43105/select-committee-to-investigate-the-january-6)),
EUT+ con Fira Mono ([FIU](https://fontsinuse.com/uses/54203/eut-european-university-of-technology)); FIU 14.
Limiti: aria da software.

**22. Schibsted Grotesk** (Bakken & Bæck per Schibsted). "Digital-first", per interfacce, con radici nella
stampa del gruppo ([scheda](https://github.com/google/fonts/blob/main/ofl/schibstedgrotesk/DESCRIPTION.en_us.html)).
Pesi 400-900 con corsivi. Lavori: SYM Group ([FIU](https://fontsinuse.com/uses/72134/sym-group-website)); FIU 1.
Limiti: pochi lavori documentati.

**23. Familjen Grotesk** (Familjen STHLM). Grandi "ink trap", x alta, aperture chiuse; testo e titoli
([scheda](https://github.com/google/fonts/blob/main/ofl/familjengrotesk/DESCRIPTION.en_us.html)). Pesi 400-700
con corsivi. Lavori: identità di Uniworld Logistics, Milano
([FIU](https://fontsinuse.com/uses/68240/uniworld-logistics-visual-identity-revamp)); FIU 4. Limiti: le ink trap
nei titoli grandi datano il lavoro; nella lista SEO madegooddesigns.

**24. Karla** (Jonny Pinhorn). Grottesco eccentrico; spaziatura larga ma molto carattere
([Typewolf](https://www.typewolf.com/karla)). Pesi 200-800 con corsivi. Testo per ospitalità e turismo. Lavori:
Harzverbunden Waldquartier, dieci appartamenti nel bosco nell'Harz, testo in Karla e titoli in Brice
([FIU](https://fontsinuse.com/uses/69576/harzverbunden-waldquartier)), Tens con Young Serif, District con
Inconsolata ([Typewolf](https://www.typewolf.com/site-of-the-day/district-magazine)); FIU 25. Limiti:
spaziatura da stringere leggermente nei titoli.

**25. Atkinson Hyperlegible Next** (Braille Institute). Per ipovedenti, forme non ambigue; la Next aggiunge
pesi, crenatura e lingue ([articolo](https://github.com/google/fonts/blob/main/ofl/atkinsonhyperlegiblenext/article/ARTICLE.en_us.html)).
Pesi 200-800 con corsivi. Studi medici, farmacie, orari, moduli. Lavori: Daylit Studio con Newsreader
([FIU](https://fontsinuse.com/uses/79109/daylit-studio-website)), Junges Schloss Landesmuseum Württemberg
([FIU](https://fontsinuse.com/uses/70373/junges-schloss-landesmuseum-wuerttemberg)), Dirty Profits
([FIU](https://fontsinuse.com/uses/65263/dirty-profits)); FIU 8. Limiti: le forme distintive danno un tono
istituzionale.

**26. Signika** (Anna Giedryś). Per segnaletica e orientamento, contrasto basso e x alta, sulla scia di Ronnia,
Meta e Tahoma; asse `GRAD` per testo chiaro su scuro
([scheda](https://github.com/google/fonts/blob/main/ofl/signika/DESCRIPTION.en_us.html)). Pesi 300-700, niente
corsivi. Indicazioni, piante, orari di hotel e cliniche. Lavori: logo Blue Apron
([FIU](https://fontsinuse.com/uses/21408/blue-apron-inc-identity)); Pimp my Type lo preferisce a Quicksand per
le interfacce ([articolo](https://pimpmytype.com/chatgpt-font-fail/)); FIU 2. Limiti: niente corsivo.

**27. Commissioner** (Kostas Bartsokas). Umanista a basso contrasto con tre "voci": asse `FLAR` che trasforma i
terminali in grazie glifiche, asse `VOLM`, inclinazione `slnt`
([scheda](https://github.com/google/fonts/blob/main/ofl/commissioner/DESCRIPTION.en_us.html)). Pesi 100-900.
Lavori: Kakoulidis Vineyards con Publico per i titoli ([FIU](https://fontsinuse.com/uses/40125/kakoulidis-vineyards));
FIU 3. Scelta di Pimp my Type. Limiti: su Google il corsivo è solo inclinato; senza cifre tabellari nel file
servito dall'API.

**28. Big Shoulders** (Patric King per il Chicago Design System). Superfamiglia di gotici americani condensati
legati a ferrovie e storia civica di Chicago ([scheda](https://github.com/google/fonts/blob/main/ofl/bigshoulders/DESCRIPTION.en_us.html)).
Assi `opsz` 10-72 e `wght` 100-900. Titoli industriali, cantieri, eventi. Lavori: Signaal RadioFestival
Bruges ([FIU](https://fontsinuse.com/uses/61550/signaal-radiofestival-bruges)), Digitalis
([FIU](https://fontsinuse.com/uses/64581/digitalis)); FIU 2. Limiti: solo titoli.

### Superfamiglie e monospazio

**29. IBM Plex** (Sans, Sans Condensed, Serif, Mono; Mike Abbink con Bold Monday). Grottesco "neutral, yet
friendly" con serif e mono coordinati ([scheda](https://github.com/google/fonts/blob/main/ofl/ibmplexsans/DESCRIPTION.en_us.html));
Butterick lo cita ([free fonts](https://practicaltypography.com/free-fonts.html)). Sans 100-700 con `wdth`
75-100. Lavori: NorthMed, sanità e tecnologia ([FIU](https://fontsinuse.com/uses/66227/northmed-visual-identity)),
Sustainable Futures Collaborative con Lusitana ([FIU](https://fontsinuse.com/uses/60029/sustainable-futures-collaborative)),
Grammys 2026 con IvyMode ([FIU](https://fontsinuse.com/uses/75184/the-grammys-2026)); FIU 37 (Sans), 47 (Mono).
Limiti: rischio IA ("Technical: IBM Plex family" nel cookbook); è già un nostro tic (Wirmec, GardensPav).

**30. Martian Mono** (Evil Martians). Monospazio con `wdth` 75-112,5 e `wght` 100-800
([scheda](https://github.com/google/fonts/blob/main/ofl/martianmono/DESCRIPTION.en_us.html)). Codici articolo e
dati tecnici veri. Lavori: sito Build Australia ([FIU](https://fontsinuse.com/uses/78547/build-australia-website));
FIU 9. Limiti: il monospazio per etichette piccole è un segno del generato (sezione 3.4).

**31. DM Mono** (Colophon per DeepMind). Tre pesi con corsivi
([scheda](https://github.com/google/fonts/blob/main/ofl/dmmono/DESCRIPTION.en_us.html)). Lavori: Flask & Field con
Fraunces ([Typewolf](https://www.typewolf.com/site-of-the-day/flask-and-field)), Dr Frankel's Clinic
([FIU](https://fontsinuse.com/uses/72746/dr-frankel-s-clinic)); FIU 21. Limiti: come Martian Mono, più l'eco
della famiglia DM.

### Da tenere in seconda fila

- **Crimson Pro** (Jacques Le Bailly, 200-900 con corsivi): buono da testo, ma nel cookbook come "Editorial";
  FIU 3 ([FIU](https://fontsinuse.com/typefaces/105578/crimson-pro)).
- **Brygada 1918** (Capitalics, revival polacco, 400-700 con corsivi): nessun lavoro su Fonts In Use; già usato
  da noi ([scheda](https://github.com/google/fonts/blob/main/ofl/brygada1918/DESCRIPTION.en_us.html)).
- **Castoro** (Tiro Typeworks, tipi olandesi XVI-XVIII secolo): solo regolare e corsivo, nessun lavoro
  archiviato ([articolo](https://github.com/google/fonts/blob/main/ofl/castoro/article/ARTICLE.en_us.html)).
- **Sorts Mill Goudy, Fanwood Text, Linden Hill** (Barry Schwartz, League): revival di Goudy e Ruzicka, un solo
  peso con corsivo; buoni per menu e carte dei vini, non per un sito intero
  ([Fanwood](https://github.com/google/fonts/blob/main/ofl/fanwoodtext/DESCRIPTION.en_us.html)).

---

## 3. Famiglie abusate dai siti generati e dai template, con le prove

### 3.1 Default di piattaforme e strumenti

| Strumento | Caratteri di partenza | Prova |
|---|---|---|
| Elementor (kit globale) | Roboto 600 primario, Roboto Slab 400 secondario, Roboto 400 testo, Roboto 500 accento | [global-typography.php](https://github.com/elementor/elementor/blob/main/core/kits/documents/tabs/global-typography.php) |
| WordPress Twenty Twenty-Four | Inter (testo), Cardo (titoli) | [theme.json](https://github.com/WordPress/twentytwentyfour/blob/trunk/theme.json) |
| WordPress Twenty Twenty-Five | Manrope, Fira Code | [theme.json](https://github.com/WordPress/twentytwentyfive/blob/trunk/theme.json) |
| Next.js `create-next-app` (Vercel; v0 lavora con Next.js, Tailwind e shadcn/ui) | Geist, Geist Mono | [layout.tsx](https://github.com/vercel/next.js/blob/canary/packages/create-next-app/templates/app-tw/ts/app/layout.tsx), [v0 docs](https://v0.app/docs) |
| bolt.diy (prompt di sistema) | nessun nome: "Modern, readable fonts", "premium typography"; il modello riempie con la sua media | [prompts.ts](https://github.com/stackblitz-labs/bolt.diy/blob/main/app/lib/common/prompts/prompts.ts) |
| Lovable, Framer | non ho trovato una fonte primaria che fissi il carattere; fonti secondarie parlano di Tailwind e Inter | [rapidevelopers](https://www.rapidevelopers.com/md/lovable-integration/tailwind), [aiskill.market](https://aiskill.market/blog/banning-inter-the-font-tell) |

### 3.2 Diffusione misurata

Web Almanac 2025, capitolo Fonts: Roboto è il Google Font più richiesto (circa 9,2% delle richieste desktop a
Google Fonts) ed è dichiarato su circa il 10-10,7% delle pagine; poi Poppins (5,8-6,0%), Open Sans (5,0-5,6%),
Montserrat (3,3-3,9%); Inter in crescita, circa 1,4-1,5%; Lato tra i più caricati.
[almanac.httparchive.org/en/2025/fonts](https://almanac.httparchive.org/en/2025/fonts)

### 3.3 Liste SEO che si copiano a vicenda

- muz.li, 2026: Inter, Roboto, Open Sans, Work Sans, Merriweather, Lora, Libre Baskerville, Spectral, Oswald,
  Anton, Montserrat, Bebas Neue, Roboto Slab, Zilla Slab, Bitter, più script e mono.
  [muz.li](https://muz.li/blog/best-free-google-fonts-for-2026/)
- madegooddesigns, marzo 2026: Inter, Hanken Grotesk, Fraunces, JetBrains Mono, Bricolage Grotesque, Playfair
  Display, DM Serif Display, Space Grotesk, Outfit, Sora, Plus Jakarta Sans, Geist, Manrope, Onest, Mona Sans,
  Instrument Serif... Coppie: Playfair + Inter, Fraunces + Inter, Cormorant Garamond + Montserrat,
  DM Serif Display + DM Sans, Archivo + Lora. [madegooddesigns](https://madegooddesigns.com/best-google-fonts/)
- La lista Typewolf dei 40 migliori apre con DM Sans, Inter, Space Mono, Space Grotesk
  ([Typewolf](https://www.typewolf.com/google-fonts)).

### 3.4 Prompt "anti IA" che hanno creato una seconda ondata

Il cookbook Anthropic per l'estetica del frontend dice "Never use: Inter, Roboto, Open Sans, Lato, default
system fonts" e propone al loro posto JetBrains Mono, Fira Code, Space Grotesk, Playfair Display, Crimson Pro,
Fraunces, Clash Display, Satoshi, Cabinet Grotesk, IBM Plex, Source Sans 3, Bricolage Grotesque, Newsreader,
con l'indicazione "Use extremes: 100/200 weight vs 800/900... Size jumps of 3x+". Lo stesso testo ammette: "You
still tend to converge on common choices (Space Grotesk, for example) across generations."
[prompting_for_frontend_aesthetics.ipynb](https://github.com/anthropics/claude-cookbooks/blob/main/coding/prompting_for_frontend_aesthetics.ipynb)

La skill frontend-design aggiornata elenca i tratti del design generato: sfondo crema (#F4F1EA) con serif
display ad alto contrasto e accento terracotta; nero con un solo accento acido; impaginato da quotidiano con
filetti sottili; kit di card arrotondate tutte uguali; etichetta in maiuscolo spaziato sopra ogni titolo,
puntini medi tra i metadati, monospazio per le piccole etichette dati, freccia in coda ai link. Tra i tic
tipografici: una sola parola del titolo in corsivo, grassetto o colore; maiuscolo per le etichette.
[SKILL.md](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)

Instrument Serif è il serif della "serif renaissance" dei marchi IA, con il corsivo usato per l'enfasi
([Keya Vadgama, 2025](https://keyavadgama.substack.com/p/the-serif-renaissance-in-ai-branding)).

### 3.5 Elenco delle famiglie da evitare come scelta di partenza

- **Default puri**: Roboto, Roboto Slab, Open Sans, Lato, Poppins, Montserrat, Inter, Geist, Manrope, Cardo
  (prove 3.1 e 3.2; giudizi di Pimp my Type su Montserrat e Inter in 1.5).
- **Seconda ondata da prompt e liste**: Space Grotesk, Space Mono, Playfair Display, Fraunces, Instrument Serif,
  Instrument Sans, Bricolage Grotesque, DM Sans, DM Serif Display, Plus Jakarta Sans, Outfit, Sora, Syne,
  Unbounded, Cormorant Garamond, JetBrains Mono, e da Fontshare Satoshi, Clash Display, Cabinet Grotesk
  (prove 3.3 e 3.4).
- **Tic di casa**: Barlow e Barlow Condensed con IBM Plex Mono ricorrono negli script di BenvegnuSrl,
  GardensPav e Wirmec (`*-Sito/**/*.py`, osservazione interna).

### 3.6 Perché il problema è il default e non il carattere

- Gli stessi caratteri, scelti con una ragione, stanno in lavori pubblicati: Inter in 141 lavori su Fonts In Use
  ([FIU](https://fontsinuse.com/typefaces/93554/inter)) e in 34 siti del giorno Typewolf, quasi sempre accanto a
  un carattere non Google ([Typewolf](https://www.typewolf.com/inter)); Montserrat accanto a Eczar per uno studio
  ortopedico ([FIU](https://fontsinuse.com/uses/55445/orthopaedie-kreuzberg)); Fraunces con Overpass per
  sostituire un'identità ferma ai default di Calibri ([FIU](https://fontsinuse.com/uses/56266/bitesize-learning-rebrand)).
- Il generato si riconosce dal pacchetto: stesso carattere, stessi tre pesi, stessa scala, stesso layout,
  stesso colore. "The model isn't choosing Inter because it's right for your product... it's the statistical
  center" ([aiskill.market](https://aiskill.market/blog/banning-inter-the-font-tell)); "they repeat mediocrity
  by imitating generic cookie-cutter templates" ([Pimp my Type](https://pimpmytype.com/about-ai-design/)).
- I template fanno lo stesso: "We swapped ugly for boring" ([Butterick](https://practicaltypography.com/websites.html)).
- Cambiare solo nome al carattere non basta: la seconda ondata (3.4) dimostra che l'elenco "alternativo" diventa
  in fretta un nuovo default.

---

## 4. Regole d'uso che separano il professionale dal generato

### 4.1 Uno o due caratteri

- Partire da uno solo e chiedersi che cosa non sa fare
  ([Google Fonts Knowledge](https://fonts.google.com/knowledge/choosing_type/pairing_typefaces),
  [Butterick](https://practicaltypography.com/mixing-fonts.html), [Pimp my Type](https://pimpmytype.com/pairing-fonts/)).
- Un solo carattere basta quando ha pesi, corsivi e magari larghezze o grandezze ottiche: Archivo, Saira, Asap,
  Fira (larghezze), Source Serif 4, Newsreader, Literata, Piazzolla (`opsz`). Siti di soli caratteri singoli
  nei siti del giorno: Libre Franklin ([Medeina Musteikyte](https://www.typewolf.com/site-of-the-day/medeina-musteikyte)),
  Chivo ([SFL](https://www.typewolf.com/site-of-the-day/sfl)), Eczar ([Thomas Schrijer](https://www.typewolf.com/site-of-the-day/thomas-schrijer)).
- Il secondo carattere serve per un ruolo diverso: titoli, dati, didascalie, un'altra lingua
  ([Google Fonts Knowledge](https://fonts.google.com/knowledge/choosing_type/pairing_typefaces)). Ruolo fisso,
  mai due caratteri nello stesso paragrafo ([Butterick](https://practicaltypography.com/mixing-fonts.html)).
- Accoppiare per scheletro, non per etichetta: stesso modello di forma, oppure contrasto netto su scheletro e
  carne; evitare superfici simili su scheletri diversi
  ([font matrix](https://fonts.google.com/knowledge/choosing_type/pairing_typefaces_based_on_their_construction_using_the_font_matrix)).
- Scorciatoie affidabili: stessa superfamiglia (Alegreya e Alegreya Sans; Source Serif 4 e Source Sans 3; Fira;
  IBM Plex); stesso designer o fonderia (Piazzolla e Alegreya Sans di del Peral; Archivo, Chivo, Saira, Asap di
  Omnibus; Libre Franklin, Libre Caslon, Public Sans della scuola Impallari; Spectral e Newsreader di
  Production Type) ([Google Fonts Knowledge](https://fonts.google.com/knowledge/choosing_type/pairing_typefaces_by_the_same_type_designer_or_type_foundry),
  [Butterick](https://practicaltypography.com/mixing-fonts.html)).
- Due serif o due sans si possono accoppiare se il contrasto è voluto (Butterick: i giornali; Typewolf: Eczar e
  Gentium), non per caso (Pimp my Type: Poppins con Open Sans).

### 4.2 Scala

- Usare una scala limitata di intervalli e non inventare un corpo per ogni blocco ("Don't compose without a
  scale", "limit yourself, at first, to a modest set of distinct and related intervals",
  [webtypography.net 3.1.1](http://webtypography.net/3.1.1); l'esempio della pagina usa 36, 24, 18, 14 e 12 px
  presi dalla scala tradizionale).
- Titoli: pochi livelli; ingrandire il minimo necessario; lo spazio fa più del corpo
  ([Butterick](https://practicaltypography.com/headings.html)).
- Diffidare dei salti estremi (pesi 100 contro 900, corpi tre volte più grandi): è proprio la ricetta del prompt
  anti IA ([cookbook](https://github.com/anthropics/claude-cookbooks/blob/main/coding/prompting_for_frontend_aesthetics.ipynb)).

### 4.3 Corpo, interlinea, riga

- Corpo del testo 15-25 px ([Butterick](https://practicaltypography.com/summary-of-key-rules.html)); a parità di
  corpo i caratteri con la x alta sembrano più grandi e chiedono meno interlinea
  ([Butterick, line spacing](https://practicaltypography.com/line-spacing.html)).
- Interlinea 1,2-1,45 ([Butterick](https://practicaltypography.com/line-spacing.html)) o 1,15-1,5
  ([Google Fonts Knowledge](https://fonts.google.com/knowledge/using_type/choosing_a_suitable_line_height));
  titoli grandi 0,9-1,0; su mobile più stretta; più aria per serif e righe lunghe.
- Riga 45-75 caratteri, 66 ideale ([webtypography.net 2.1.2](http://webtypography.net/2.1.2)), 45-90 per
  Butterick ([line length](https://practicaltypography.com/line-length.html)), che propone anche la prova
  pratica: tra due e tre alfabeti minuscoli per riga. In Elementor si traduce in una larghezza massima del blocco
  di testo, da tarare con quella prova su ogni carattere (indicazione nostra).

### 4.4 Maiuscolo e spaziatura

- Maiuscolo solo per meno di una riga, sempre spaziato del 5-12%
  ([Butterick](https://practicaltypography.com/all-caps.html)), 5-10% per Bringhurst
  ([webtypography.net 2.1.6](http://webtypography.net/2.1.6)); titoli grandi con spaziatura leggermente negativa
  ([Google Fonts Knowledge](https://fonts.google.com/knowledge/using_type/track_carefully_or_not_at_all)).
- L'etichetta in maiuscolo spaziato sopra ogni titolo è un segno del generato
  ([frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)) e coincide
  con il divieto "badge sopra il titolo".

### 4.5 Pesi pochi, corsivi veri

- Una famiglia di testo con due pesi (regolare e grassetto o semigrassetto) e il corsivo; un peso per i titoli.
  "Use as few different styles as possible" ([Pimp my Type](https://pimpmytype.com/pairing-fonts/)); grassetto o
  corsivo, non insieme; i pesi Black solo per titoli ([Butterick](https://practicaltypography.com/bold-or-italic.html)).
- Corsivo vero: caricare il corsivo e il grassetto corsivo, altrimenti il browser li inventa
  ([Google Fonts Knowledge](https://fonts.google.com/knowledge/using_type/the_foundations_of_web_typography)).
  Senza corsivo su Google Fonts: Space Grotesk, Manrope, Syne, Eczar, Young Serif, Signika, Inknut Antiqua,
  Big Shoulders (catalogo [metadata](https://fonts.google.com/metadata/fonts)). Con questi si mette
  `font-synthesis: none` nel CSS aggiuntivo per non avere corsivi finti
  ([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/font-synthesis)).
- Con un sans il corsivo dice poco: meglio il grassetto per l'enfasi
  ([Butterick](https://practicaltypography.com/bold-or-italic.html)).

### 4.6 Numeri tabellari e minuscoli (con verifica tecnica)

- Regola: cifre proporzionali nel testo, tabellari per prezzi, orari, dati tecnici in colonna; minuscole nel testo
  corrente con serif, lineari con il maiuscolo
  ([Google Fonts Knowledge](https://fonts.google.com/knowledge/introducing_type/understanding_numerals),
  [Butterick](https://practicaltypography.com/alternate-figures.html), [webtypography.net 3.2.1](http://webtypography.net/3.2.1)).
- Verifica fatta qui con fontTools: richiesta standard `https://fonts.googleapis.com/css2?family=NOME` (sottoinsieme
  latino) confrontata con i file completi di [github.com/google/fonts](https://github.com/google/fonts).
  - Dall'API spariscono `onum` (numeri minuscoli), `smcp`/`c2sc` (maiuscoletto), `case`, `zero`, `ss01`: per
    esempio Spectral, Source Serif 4, EB Garamond, Alegreya e Vollkorn li hanno nel file completo e non in quello
    servito; Inter perde `case`, `zero`, `ss01` e le varianti `cv`.
  - `tnum` resta in quasi tutte le famiglie controllate; manca in Libre Franklin e IBM Plex Sans anche nel file
    completo, e in Hanken Grotesk e Commissioner nel file servito dall'API.
  - Conseguenza: per maiuscoletto e numeri minuscoli veri bisogna ospitare i file completi (plugin Custom Fonts,
    [wordpress.org](https://wordpress.org/plugins/custom-fonts/)). Da verificare se il caricamento locale di
    Elementor scarica i file completi o quelli dell'API.

### 4.7 Quando un serif ha senso e quando è una posa

- Ha senso quando c'è da leggere (storie, menu, carte dei vini, pagine dell'albergo), quando il settore ha una
  tradizione a stampa (etichette, giornali, insegne) e quando il serif ha corsivi veri e una versione da testo:
  Spectral per Champagne Marcoult ([FIU](https://fontsinuse.com/uses/50720/champagne-m-marcoult)), Vollkorn per
  Birrificio Ventitre ([FIU](https://fontsinuse.com/uses/46054/birrificio-ventitre-beers)), Newsreader per L'Obs
  ([FIU](https://fontsinuse.com/uses/45802/l-obs-website)). Le associazioni storiche del carattere devono
  coincidere con il soggetto ([Google Fonts Knowledge](https://fonts.google.com/knowledge/choosing_type/emotive_considerations_for_choosing_typefaces)).
- È una posa quando serve solo a dire "eleganza": serif display ad alto contrasto su crema
  ([frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)), serif scelto
  per sembrare umani ([Vadgama](https://keyavadgama.substack.com/p/the-serif-renaissance-in-ai-branding)), una
  parola del titolo in corsivo serif (divieto già dato). Per un costruttore di macchine un grottesco con
  larghezze (Archivo, Saira) dice di più di qualsiasi Didone.

---

## 5. Accoppiate concrete viste in lavori reali

### 5.1 Solo Google Fonts

| # | Accoppiata (ruoli dove noti) | Lavoro | Settore, luogo |
|---|---|---|---|
| 1 | Eczar (titoli) + Montserrat (testo e dati) | [Orthopädie Kreuzberg](https://fontsinuse.com/uses/55445/orthopaedie-kreuzberg) | studio medico, Berlino; identità e sito |
| 2 | Newsreader + Atkinson Hyperlegible | [Daylit Studio website](https://fontsinuse.com/uses/79109/daylit-studio-website) | studio di design e servizi, Texas; sito |
| 3 | Spectral + Work Sans | [Failles Flots Fils Flammes](https://fontsinuse.com/uses/38063/failles-flots-fils-flammes-website) | rivista letteraria online, Parigi |
| 4 | Piazzolla + Alegreya Sans (stesso designer) | [Jornadas de Edición Universitaria](https://fontsinuse.com/uses/36172/jornadas-de-edicion-universitaria-10) | evento editoriale, Buenos Aires; web e identità |
| 5 | Fraunces (titoli) + Overpass (testo) | [BiteSize Learning](https://fontsinuse.com/uses/56266/bitesize-learning-rebrand) | formazione aziendale, Regno Unito; sito e materiali |
| 6 | Rubik Black + Source Serif | [Aardman Animations](https://fontsinuse.com/uses/58068/aardman-animations-website) | animazione, Bristol; sito |
| 7 | Merriweather (titoli) + Fira Sans (testo, navigazione) | [Commissione 6 gennaio](https://fontsinuse.com/uses/43105/select-committee-to-investigate-the-january-6) | istituzionale, Washington; sito |
| 8 | Merriweather + Merriweather Sans | [Pivo Bakalář](https://fontsinuse.com/uses/67847/pivo-bakalar) | birrificio, Repubblica Ceca; etichette, insegne |
| 9 | Zilla Slab (titoli) + Source Sans (testo) | [TriMet](https://fontsinuse.com/uses/69330/trimet-phase-3) | trasporto pubblico, Portland; sito |
| 10 | Archivo + DM Serif Display | [Kook Furniture](https://fontsinuse.com/uses/49413/kook-furniture-website) | arredamento, Sudafrica; sito |
| 11 | Krub (sistema) + Archivo (logotipo) | [MycoTech](https://fontsinuse.com/uses/79120/mycotech) | biomateriali, Argentina; sito e imballi |
| 12 | IBM Plex Sans + Lusitana | [Sustainable Futures Collaborative](https://fontsinuse.com/uses/60029/sustainable-futures-collaborative) | ricerca e politiche, India |
| 13 | Barlow + Vidaloka | [Wohnbar magazine](https://fontsinuse.com/uses/58423/wohnbar-magazine) | casa e cibo, Linz; rivista |
| 14 | League Gothic + Instrument Serif | [Panaille](https://fontsinuse.com/uses/61384/panaille-restaurant) | ristorante, Bordeaux; insegne e identità |
| 15 | Young Serif + Karla | [Tens](https://www.typewolf.com/site-of-the-day/tens-sunglasses) | occhiali, e-commerce; sito |
| 16 | Work Sans + Alegreya | [Maurizio Ilpiac Piacenza](https://www.typewolf.com/site-of-the-day/maurizio-ilpiac-piacenza) | portfolio di un designer di identità; sito |
| 17 | Fraunces + Poppins | [Maria Coassin](https://fontsinuse.com/uses/72040/maria-coassin-gelato-consultant) | consulenza gelateria, Roma e Seattle; sito |

Note: nella 1, 14 e 17 c'è un carattere della lista 3.5 (Montserrat, Instrument Serif, Poppins, Fraunces), scelto
con una ragione dichiarata; la 7 e la 8 usano Merriweather, che Typewolf considera uno "staple"
([Typewolf](https://www.typewolf.com/blog/google-fonts-combinations)). Elenco completo dei 118 lavori di soli
Google Fonts trovati: appendice in fondo.

### 5.2 Schema dei nostri settori: titolo con un'idea, testo Google

| Lavoro | Titolo | Testo | Settore |
|---|---|---|---|
| [Beton Asfalti](https://fontsinuse.com/uses/72654/beton-asfalti) | Nure (variabile, "for industrial applications") | Archivo | conglomerati bituminosi, Trento |
| [Birrificio Ventitre](https://fontsinuse.com/uses/46054/birrificio-ventitre-beers) | Annuario (Resistenza) | Vollkorn | birrificio, Irpinia |
| [Champagne M. Marcoult](https://fontsinuse.com/uses/50720/champagne-m-marcoult) | Tungsten | Spectral, Trade Gothic | vino, Champagne |
| [Kakoulidis Vineyards](https://fontsinuse.com/uses/40125/kakoulidis-vineyards) | Publico | Commissioner | vino, Pieria |
| [Harzverbunden Waldquartier](https://fontsinuse.com/uses/69576/harzverbunden-waldquartier) | Brice | Karla | appartamenti vacanza nel bosco, Harz |
| [Stan's Grill](https://fontsinuse.com/uses/60220/stan-s-grill) | Vertigo | Chivo | ristorante, Melbourne |

Con il solo catalogo Google il ruolo del titolo "con un'idea" lo possono fare Young Serif, Eczar, Libre Caslon
Display, Besley ai pesi alti, Big Shoulders, Archivo o Saira alle larghezze estreme; in alternativa un carattere
libero di Collletttivo o Velvetyne ospitato in proprio (1.6).

---

## Metodo e limiti

- Fonti lette direttamente: Typewolf (lista, articolo 2016, 66 schede di caratteri), Fonts In Use (131 pagine di
  carattere, 139 pagine di lavori), Google Fonts Knowledge (sorgenti su GitHub), Butterick (16 capitoli), Pimp
  my Type (10 articoli e il catalogo open source), webtypography.net, League of Moveable Type, Collletttivo, Fontshare, Elementor, codice di
  Elementor, WordPress, Next.js, bolt.diy, Anthropic, Web Almanac 2025.
- Fonts In Use privilegia stampa e identità; Typewolf privilegia studi americani e caratteri commerciali: i
  conteggi indicano la presenza nei lavori curati, non la diffusione sul web.
- Il campo `popularity` del catalogo Google Fonts non è documentato e non è stato usato.
- Default di Lovable e Framer non verificati su fonti primarie.
- Velvetyne.fr era irraggiungibile (errore 500); I Love Typography non ha dato articoli pertinenti.
- La verifica OpenType riguarda il sottoinsieme latino servito a Chrome il 6/10/2026.

---

## Appendice: lavori su Fonts In Use che usano solo Google Fonts

Ricavati dalle pagine delle 131 famiglie controllate (6/10/2026). Formato e settore come classificati da Fonts In Use.

| Caratteri | Lavoro | Formato | Settore | Luogo |
|---|---|---|---|---|
| Alegreya + Alegreya Sans | [Cuánto te pesa tu peso by Virginia Busnelli](https://fontsinuse.com/uses/67506/cuanto-te-pesa-tu-peso-by-virginia-busnelli) | Books | Food/Beverage, Health/Fitness | Argentina, Buenos Aires |
| Alegreya + Alegreya Sans | [El teatro del espíritu by Carlos Rivarola](https://fontsinuse.com/uses/40491/el-teatro-del-espiritu-by-carlos-rivarola) | Books | Performing Arts | Argentina |
| Alegreya + Alegreya Sans | [Será su nombre by Luis Loyola Cano](https://fontsinuse.com/uses/36786/sera-su-nombre-by-luis-loyola-cano) | Books | Literature, Performing Arts | Argentina |
| Alegreya + Alegreya Sans | [Borges y sus firmas](https://fontsinuse.com/uses/21913/borges-y-sus-firmas) | Booklets/Pamphlets, Ephemera | Literature, Art | Argentina, Buenos Aires |
| Aleo + DM Sans | [Reality House](https://fontsinuse.com/uses/62337/reality-house-1) | Web, Branding/Identity, Mobile/Tablet, Booklets/Pamphlets | Services, Health/Fitness | United States, New York City |
| Amaranth + Open Sans | [UC Propone 2019](https://fontsinuse.com/uses/43621/uc-propone-2019) | Books | Institutional, Science/Nature, Education/Academia | Chile, Santiago |
| Andada + Alegreya Sans | [Nhemombaraete reko rã’i by José Verá](https://fontsinuse.com/uses/42213/nhemombaraete-reko-ra-i-by-jose-vera) | Books | Literature, Science/Nature, Art, Religion/Spirituality | Brazil, Brasília |
| Andada + Montserrat | [Transpassar: Poetics of movement](https://fontsinuse.com/uses/19978/transpassar-poetics-of-movement) | Books | Literature | Brazil, São Paulo |
| Archivo + DM Serif Display | [Kook Furniture website](https://fontsinuse.com/uses/49413/kook-furniture-website) | Web, Social Media | Home/Interior, Retail/Shopping | South Africa |
| Archivo + Judson | [We Wear Eco Website](https://fontsinuse.com/uses/35050/we-wear-eco-website) | Web | Fashion/Apparel | United States |
| Atkinson Hyperlegible + Newsreader | [Daylit Studio website](https://fontsinuse.com/uses/79109/daylit-studio-website) | Web | Services, Graphic Design | United States, Allen |
| Barlow + Noto Serif | [Silent Hill 2 Remake videogame](https://fontsinuse.com/uses/66399/silent-hill-2-remake-videogame) | Software/Apps | Entertainment, Technology | Poland, Kraków |
| Barlow + Vidaloka | [Wohnbar magazine](https://fontsinuse.com/uses/58423/wohnbar-magazine) | Magazines/Periodicals | Home/Interior, Food/Beverage | Austria, Linz |
| Bebas Neue + Poppins + Merriweather | [Darko audio website](https://fontsinuse.com/uses/39420/darko-audio-website) | Web, Film/Video | Lifestyle | Australia, Sydney |
| Biryani + Lato + Open Sans | [Away-Days by Berlin Type School and UdK TypoLabor](https://fontsinuse.com/uses/14049/away-days-by-berlin-type-school-and-udk-typol) | Web | Event, Graphic Design, Education/Academia | Germany, Berlin |
| Bungee + Jura + Montserrat | [Cantrip Seltzer](https://fontsinuse.com/uses/48619/cantrip-seltzer) | Web, Packaging, Branding/Identity | Product, Food/Beverage | United States, Massachusetts |
| Cormorant + Amiko + Raleway | [Brilliante Ideen gesucht](https://fontsinuse.com/uses/18096/brilliante-ideen-gesucht) | Web, Booklets/Pamphlets | Technology, Kids, Education/Academia | Switzerland, Zürich |
| Cormorant + Great Vibes + Playfair Display | [LovePaper](https://fontsinuse.com/uses/79877/lovepaper) | Web, Software/Apps | Services | Brazil |
| Cormorant + Josefin Sans | [Endlich wieder Meer by Christiane Franke (Goya)](https://fontsinuse.com/uses/42666/endlich-wieder-meer-by-christiane-franke-goya) | Books | Literature | Germany, Hamburg |
| Cormorant + Open Sans | [Farbpigmente: 50 Farben und ihre Geschichte by David Coles](https://fontsinuse.com/uses/66368/farbpigmente-50-farben-und-ihre-geschichte-by) | Books | Science/Nature | Switzerland, Zürich |
| DM Sans + DM Serif Text | [Diseño Especulativo v. DCP infographic](https://fontsinuse.com/uses/69566/diseno-especulativo-v-dcp-infographic) | Infographics/Maps | Graphic Design, Education/Academia | Spain, Sevilla |
| Domine + Roboto | [Campaign Monitor’s 2018 Predictions](https://fontsinuse.com/uses/19508/campaign-monitor-s-2018-predictions) | Web | Technology | United States, San Francisco |
| EB Garamond + Inter + Open Sans | [WordPress.org website (2024)](https://fontsinuse.com/uses/60495/wordpress-org-website-2024) | Web, Mobile/Tablet | Technology | United States, California |
| EB Garamond + Sorts Mill Goudy + Spirax | [Dave on Design](https://fontsinuse.com/uses/55873/dave-on-design) | Web | Graphic Design, Technology | Estonia |
| Economica + Open Sans | [“How Search Works” by Google](https://fontsinuse.com/uses/15783/how-search-works-by-google) | Web | Technology | United States |
| Eczar + Montserrat | [Orthopädie Kreuzberg](https://fontsinuse.com/uses/55445/orthopaedie-kreuzberg) | Branding/Identity | Health/Fitness | Germany, Dortmund |
| Exo + Manrope | [Neon Team Agency website](https://fontsinuse.com/uses/59595/neon-team-agency-website) | Web, Mobile/Tablet |  | Thailand, Phuket |
| Fahkwang + Nunito Sans | [hômnay beauty](https://fontsinuse.com/uses/73055/homnay-beauty) | Packaging, Advertising, Branding/Identity | Product, Lifestyle | Vietnam, Thành phố Hồ Chí Minh |
| Fira Sans + Fira Mono | [EUT+ (European University of Technology)](https://fontsinuse.com/uses/54203/eut-european-university-of-technology) | Branding/Identity, Social Media | Institutional, Technology, Education/Academia, Governmental/Civic | France, Troyes |
| Fira Sans + Fira Mono | [Tabuh game](https://fontsinuse.com/uses/9112/tabuh-game) | Mobile/Tablet, Software/Apps | Entertainment | Germany |
| Fraunces + Overpass | [BiteSize Learning rebrand](https://fontsinuse.com/uses/56266/bitesize-learning-rebrand) | Web, Branding/Identity, Mobile/Tablet, Booklets/Pamphlets | Services, Education/Academia, Business/Finance | United Kingdom |
| Fraunces + Poppins | [Maria Coassin: gelato consultant](https://fontsinuse.com/uses/72040/maria-coassin-gelato-consultant) | Web | Services, Food/Beverage | Italy, United States |
| Fredoka + Lato | [Cocina sin gluten para niños by Dolly Walsh](https://fontsinuse.com/uses/30030/cocina-sin-gluten-para-ninos-by-dolly-walsh) | Books | Food/Beverage, Kids, Health/Fitness | Argentina, Buenos Aires |
| Funnel Display + Bitter + Atkinson Hyperlegible | [Dirty Profits](https://fontsinuse.com/uses/65263/dirty-profits) | Web, Mobile/Tablet | Activism, Business/Finance, Governmental/Civic | Germany, Berlin |
| Gilda Display + Space Mono + Xanh Mono | [raye the store 08, Beauty Edition](https://fontsinuse.com/uses/59932/raye-the-store-08-beauty-edition) | Signs, Branding/Identity | Event, Retail/Shopping, Health/Fitness | United Kingdom, London |
| HK Grotesk + DM Mono | [SkyFi website](https://fontsinuse.com/uses/50011/skyfi-website) | Web, Mobile/Tablet | Technology | United States, New York City |
| HK Grotesk + Spectral | [Encoded Symbols , IN Residence monographs](https://fontsinuse.com/uses/37983/encoded-symbols-in-residence-monographs) | Books | Education/Academia, Art | Italy, Favara |
| IBM Plex Sans + IBM Plex Mono | [NorthMed visual identity](https://fontsinuse.com/uses/66227/northmed-visual-identity) | Branding/Identity | Technology, Health/Fitness | Israel |
| IBM Plex Sans + IBM Plex Mono | [Giacomo Works](https://fontsinuse.com/uses/28323/giacomo-works) | Web | Graphic Design | Germany, Berlin |
| IBM Plex Sans + IBM Plex Mono + IBM Plex Serif | [“Accidentes”, typographic CV](https://fontsinuse.com/uses/30616/accidentes-typographic-cv) | Infographics/Maps | Graphic Design | Spain, Sevilla |
| IBM Plex Sans + IBM Plex Mono + IM Fell English | [Corsaires Studio](https://fontsinuse.com/uses/27301/corsaires-studio) | Web, Branding/Identity, Mobile/Tablet | Services, Graphic Design | France, Bordeaux |
| IBM Plex Sans + Lusitana | [Sustainable Futures Collaborative](https://fontsinuse.com/uses/60029/sustainable-futures-collaborative) | Branding/Identity, Magazines/Periodicals, Posters/Flyers | Institutional, Education/Academia, Activism | India |
| IM Fell English + IM Fell DW Pica + Libre Caslon Display | [Federalist Reader](https://fontsinuse.com/uses/79099/federalist-reader) | Web | Literature, Education/Academia, Politics | United States |
| Instrument Serif + Anton | [Freedl Dolce Club](https://fontsinuse.com/uses/79375/freedl-dolce-club) | Object/Product | Fashion/Apparel, Lifestyle | Germany, Italy |
| Instrument Serif + Geist Sans | [Sommerfest 25 Künstler:innenhäuser Worpswede poster](https://fontsinuse.com/uses/73366/sommerfest-25-kuenstler-innenhaeuser-worpswed) | Posters/Flyers | Event, Art | Germany, Worpswede |
| Inter + Plus Jakarta Sans | [Secret Project](https://fontsinuse.com/uses/61811/secret-project) | Branding/Identity, Social Media | Services, Technology, Education/Academia | Indonesia, Jakarta |
| Josefin Sans + Amatic SC | [Vandal wines](https://fontsinuse.com/uses/45415/vandal-wines) | Packaging | Food/Beverage | New Zealand |
| Krub + Archivo | [MycoTech](https://fontsinuse.com/uses/79120/mycotech) | Web, Packaging, Branding/Identity | Product, Science/Nature | Argentina, Rafaela |
| Lato + Fira Sans | [The Center of Gravity website](https://fontsinuse.com/uses/73659/the-center-of-gravity-website) | Web | Institutional, Science/Nature, Education/Academia | Denmark, Copenhagen |
| Lato + Oswald | [Addictions prevention action](https://fontsinuse.com/uses/10084/addictions-prevention-action) | Web | Activism, Health/Fitness | Poland |
| Lato + Playfair Display | [Chidusz magazine](https://fontsinuse.com/uses/20337/chidusz-magazine) | Magazines/Periodicals | Literature, Religion/Spirituality, Local | Poland, Wrocław |
| Lato + Playfair Display | [Ara.cat ’s 2013 Year in Review](https://fontsinuse.com/uses/6244/ara-cat-s-2013-year-in-review) | Web, Infographics/Maps | News | Spain, Barcelona |
| League Gothic + Instrument Serif | [Panaille restaurant](https://fontsinuse.com/uses/61384/panaille-restaurant) | Signs, Branding/Identity, Mobile/Tablet, Social Media, Ephemera | Food/Beverage | France, Bordeaux |
| League Gothic + Montserrat + Merriweather | [Electronic Frontier Foundation (EFF)](https://fontsinuse.com/uses/55258/electronic-frontier-foundation-eff) | Web, Branding/Identity | Institutional, Technology, Activism, Governmental/Civic | United States, California |
| Lexend + MuseoModerno | [mona rebrand (ArtCenter College of Design project)](https://fontsinuse.com/uses/75079/mona-rebrand-artcenter-college-of-design-proj) | Branding/Identity | Institutional, Art | United States, California |
| Libre Baskerville + Source Sans | [Typozon portfolio website (2017)](https://fontsinuse.com/uses/16655/typozon-portfolio-website-2017) | Web | Graphic Design | Colombia, Bogotá |
| Literata + Cousine + Sofia | [Tribute to Vietnam’s great prime ministers](https://fontsinuse.com/uses/62178/tribute-to-vietnam-s-great-prime-ministers) | Posters/Flyers | Politics, Other | Vietnam |
| Manrope + IBM Plex Mono | [Phosphor Icons website](https://fontsinuse.com/uses/67558/phosphor-icons-website) | Web | Graphic Design | United States, Colorado |
| Merriweather + Fira Sans | [Select Committee to Investigate the January 6th Attack on the U.S. Capitol website](https://fontsinuse.com/uses/43105/select-committee-to-investigate-the-january-6) | Web | Politics, Governmental/Civic | United States, Washington, D. C. |
| Merriweather + Merriweather Sans | [Pivo Bakalář](https://fontsinuse.com/uses/67847/pivo-bakalar) | Packaging, Advertising, Signs, Object/Product, Branding/Identity | Product, Food/Beverage, Retail/Shopping | Czech Republic |
| Merriweather + Merriweather Sans | [Main-Post website](https://fontsinuse.com/uses/24414/main-post-website) | Web | News, Local | Germany, Würzburg |
| Merriweather + Mulish | [Together For Yes](https://fontsinuse.com/uses/21695/together-for-yes) | Web, Advertising, Branding/Identity | Activism, Governmental/Civic | Ireland, Dublin |
| Merriweather + Open Sans | [Polskie Radio website](https://fontsinuse.com/uses/64074/polskie-radio-website) | Web | News | Poland |
| Merriweather + Open Sans | [Moxie robot website](https://fontsinuse.com/uses/40711/moxie-robot-website) | Web | Product, Kids, Education/Academia | United States |
| Merriweather + Open Sans + Montserrat | [Wemind website](https://fontsinuse.com/uses/51352/wemind-website) | Web | Business/Finance | France, Paris |
| Merriweather + Roboto | [South China Morning Post website](https://fontsinuse.com/uses/24407/south-china-morning-post-website) | Web | News | China, Hong Kong |
| Merriweather + Source Sans | [whitehouse.gov website (2018)](https://fontsinuse.com/uses/22378/whitehouse-gov-website-2018) | Web | Governmental/Civic | United States, Washington, D. C. |
| Merriweather + Work Sans | [Glass Onion, “The Million Dollar Napkin” website](https://fontsinuse.com/uses/73707/glass-onion-the-million-dollar-napkin-website) | Web, Film/Video | Film/TV | United States |
| Mona Sans + Anton + Instrument Serif | [Fermented Films](https://fontsinuse.com/uses/64040/fermented-films-1) | Web, Branding/Identity | Film/TV | Slovenia |
| Montserrat + Climate Crisis | [FIMU Belfort Festival 2026](https://fontsinuse.com/uses/77496/fimu-belfort-festival-2026) | Branding/Identity, Posters/Flyers, Mobile/Tablet, Booklets/Pamphlets | Event, Kids, Music | France, Marseille |
| Montserrat + Inter | [Decentriq](https://fontsinuse.com/uses/59878/decentriq) | Web, Branding/Identity, Social Media | Technology | Switzerland, Germany |
| Montserrat + Roboto | [“Cardume” graphics for Instituto Guaicuy](https://fontsinuse.com/uses/64771/cardume-graphics-for-instituto-guaicuy) | Branding/Identity, Posters/Flyers | Institutional, Event, Science/Nature, Activism, Local, Governmental/Civic | Brazil, Belo Horizonte |
| Montserrat + Roboto Condensed | [Mapa Paraopeba](https://fontsinuse.com/uses/64773/mapa-paraopeba) | Infographics/Maps | Science/Nature, Governmental/Civic | Brazil, Belo Horizonte |
| Montserrat + Source Sans | [Deca WordPress Theme](https://fontsinuse.com/uses/11393/deca-wordpress-theme) | Web | Product | India |
| Montserrat + Ubuntu | [Antena 1 identity (2022-)](https://fontsinuse.com/uses/58183/antena-1-identity-2022) | Branding/Identity, Film/Video | Film/TV | Romania |
| Mulish + Khand | [Ayok’a identity](https://fontsinuse.com/uses/45414/ayok-a-identity) | Branding/Identity, Social Media | Retail/Shopping, Art | Switzerland, Russia |
| Nanum Myeongjo + Bitter + Work Sans | [Types of Type](https://fontsinuse.com/uses/19151/types-of-type) | Web | Graphic Design | United States, Los Angeles |
| Newsreader + Karla + Oswald | [L’Obs website](https://fontsinuse.com/uses/45802/l-obs-website) | Web | News | France, Paris |
| Newsreader + Xanh Mono + Space Grotesk | [The Collective Spark: Igniting Thinking in Groups, Teams and the Wider World](https://fontsinuse.com/uses/60367/the-collective-spark-igniting-thinking-in-gro) | Books | Education/Academia | Australia, Belgium |
| Noto Serif + Poppins | [beckn](https://fontsinuse.com/uses/75323/beckn) | Web, Branding/Identity, Posters/Flyers, Film/Video | Services, Technology | India, Bangalore |
| Nunito Sans + Poppins | [eSharp portfolio website](https://fontsinuse.com/uses/39125/esharp-portfolio-website) | Web | Services | Australia, Sydney |
| Ojuju + Space Mono + Xanh Mono | [raye the store 10](https://fontsinuse.com/uses/62010/raye-the-store-10) | Signs, Branding/Identity, Posters/Flyers | Retail/Shopping, Lifestyle | United Kingdom, London |
| Onest + BIZ UDMincho | [NoCamera photo app](https://fontsinuse.com/uses/76916/nocamera-photo-app) | Branding/Identity, Software/Apps, Social Media | Technology, Art | Argentina, Buenos Aires |
| Piazzolla + Alegreya Sans | [Jornadas de Edición Universitaria 10](https://fontsinuse.com/uses/36172/jornadas-de-edicion-universitaria-10) | Web, Branding/Identity | Event, Education/Academia | Argentina, Buenos Aires |
| Playfair Display + Inter | [Sacha Tourtoulou portfolio](https://fontsinuse.com/uses/29406/sacha-tourtoulou-portfolio) | Web | Other | France, Paris |
| Playfair Display + Lato | [Yuko Shimizu website](https://fontsinuse.com/uses/6089/yuko-shimizu-website) | Art/Illustration | Graphic Design | United States, New York City |
| Playfair Display + Lato | [Designers checklists advices](https://fontsinuse.com/uses/5978/designers-checklists-advices) | Web | Graphic Design | France |
| Playfair Display + Roboto | [Shaping the Future of Bel Canto](https://fontsinuse.com/uses/77514/shaping-the-future-of-bel-canto) | Booklets/Pamphlets | Education/Academia, Music | Greece, Italy |
| Playfair Display + Roboto + Poppins | [Increaseo](https://fontsinuse.com/uses/29853/increaseo) | Web, Branding/Identity | Business/Finance | Australia, Erina |
| Poppins + Inter | [Inkbot Design](https://fontsinuse.com/uses/63859/inkbot-design) | Web, Branding/Identity | Services, Graphic Design | United Kingdom, Northern Ireland |
| Poppins + Work Sans | [don Gata studio website](https://fontsinuse.com/uses/50276/don-gata-studio-website) | Web | Services, Graphic Design | Portugal |
| Prompt + Work Sans | [Onomatopoeia.club](https://fontsinuse.com/uses/34154/onomatopoeia-club) | Web, Branding/Identity | Music, Film/TV | United Kingdom, London |
| Proza Libre + Open Sans | [redro.de](https://fontsinuse.com/uses/14793/redro-de) | Web | Graphic Design | Germany, Mainz |
| PT Serif + Chivo + Quattrocento | [Aeon magazine](https://fontsinuse.com/uses/3730/aeon-magazine) | Web, Magazines/Periodicals | Literature | United Kingdom, London |
| Public Sans + Karla | [HoodieHut website](https://fontsinuse.com/uses/38630/hoodiehut-website) | Web | Services, Fashion/Apparel, Retail/Shopping | United Kingdom, Sheffield |
| Quicksand + Roboto | [Seed Furniture](https://fontsinuse.com/uses/8870/seed-furniture) | Web | Home/Interior |  |
| Roboto + Merriweather | [The Moscow Times website](https://fontsinuse.com/uses/45172/the-moscow-times-website) | Web | News | Netherlands, Russia |
| Roboto + Roboto Mono | [5th International Symposium on Solar Sailing](https://fontsinuse.com/uses/33848/5th-international-symposium-on-solar-sailing) | Web, Branding/Identity | Event, Technology, Science/Nature | Germany, Aachen |
| Rubik + Source Serif | [Aardman Animations website](https://fontsinuse.com/uses/58068/aardman-animations-website) | Web, Mobile/Tablet | Entertainment, Film/TV | United Kingdom, Bristol |
| Rubik Mono One + Rubik | [Donos do mercado by João Peres & Victor Matioli](https://fontsinuse.com/uses/38494/donos-do-mercado-by-joao-peres-and-victor-mat) | Books | Food/Beverage, Retail/Shopping, Activism, Governmental/Civic | Brazil, São Paulo |
| Source Sans + Space Mono | [Access Democracy](https://fontsinuse.com/uses/58646/access-democracy) | Branding/Identity, Social Media | Technology, Activism | Germany, Berlin |
| Space Grotesk + Instrument Sans | [Modal Digital website](https://fontsinuse.com/uses/68541/modal-digital-website) | Web | Services, Graphic Design, Technology | United Kingdom, Manchester |
| Space Grotesk + Space Mono | [Othernity: Reconditioning Our Modern Heritage](https://fontsinuse.com/uses/42801/othernity-reconditioning-our-modern-heritage) | Books, Branding/Identity, Posters/Flyers, Exhibition/Installation | Event, Architecture | Hungary, Italy |
| Space Grotesk + Space Mono | [Artoid Studio branding and website](https://fontsinuse.com/uses/40665/artoid-studio-branding-and-website) | Web | Services, Art, Film/TV | Hungary, Budapest |
| Space Mono + Barlow | [Aura Bora packaging](https://fontsinuse.com/uses/45890/aura-bora-packaging) | Packaging | Product, Food/Beverage | United States, San Francisco |
| Space Mono + Roboto | [720 Protections website](https://fontsinuse.com/uses/36656/720-protections-website) | Web, Branding/Identity | Product, Sports | Austria, Germany |
| Space Mono + Space Grotesk | [CPS-IT brand identity](https://fontsinuse.com/uses/27501/cps-it-brand-identity) | Web, Branding/Identity, Posters/Flyers | Services, Technology | Germany, Berlin |
| Spectral + Work Sans | [Failles Flots Fils Flammes website](https://fontsinuse.com/uses/38063/failles-flots-fils-flammes-website) | Web | Literature | France, Paris |
| Syne + Syne Tactile | [XOXO Festival 2018](https://fontsinuse.com/uses/24383/xoxo-festival-2018) | Web | Event, Technology, Art | United States, Portland |
| Syne + Syne Tactile | [WeTransfer: Ideas Report 2018](https://fontsinuse.com/uses/24520/wetransfer-ideas-report-2018) | Web | Services, Technology | Netherlands, Amsterdam |
| Syne + Syne Tactile | [Soft art fair](https://fontsinuse.com/uses/23028/soft-art-fair) | Branding/Identity, Posters/Flyers | Event, Graphic Design, Music, Art | Philippines, Cagayan de Oro |
| Syne + Syne Tactile + Syne Mono | [Synesthésie ¬ MMAINTENANT flyers and software](https://fontsinuse.com/uses/32468/synesthesie-mmaintenant-flyers-and-software) | Posters/Flyers, Software/Apps | Art | France, Saint-Denis |
| Syne + Syne Tactile + Syne Mono | [Temple magazine Nº7 “No Limit”](https://fontsinuse.com/uses/28929/temple-magazine-no7-no-limit) | Magazines/Periodicals | Fashion/Apparel, Art | France, Paris |
| Syne + Syne Tactile + Syne Mono | [Synesthésie ¬ MMAINTENANT poster](https://fontsinuse.com/uses/27135/synesthesie-mmaintenant-poster) | Posters/Flyers | Art | France, Paris |
| Unna + Open Sans | [Sturm & Dreck album release party tickets by Feine Sahne Fischfilet](https://fontsinuse.com/uses/31664/sturm-and-dreck-album-release-party-tickets-b) | Ephemera | Event, Music | Germany, Loitz |
| Vollkorn + Tagesschrift | [Mundräuber-Handbuch](https://fontsinuse.com/uses/2223/mundraeuber-handbuch) | Books | Food/Beverage, Activism | Germany, Weimar |
| Work Sans + Space Grotesk + Source Serif | [seekicks: Transformative practices that shape the world](https://fontsinuse.com/uses/66842/seekicks-transformative-practices-that-shape-) | Web, Booklets/Pamphlets | Education/Academia, Art, Business/Finance | Germany, Berlin |
| Young Serif + Poppins + Outfit | [Presentable website](https://fontsinuse.com/uses/74661/presentable-website) | Web, Mobile/Tablet | Services, Graphic Design | India, Gurgaon |

Totale: 118 lavori.
