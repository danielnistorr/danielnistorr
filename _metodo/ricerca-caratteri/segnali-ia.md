# Segnali che fanno riconoscere un sito fatto con l'IA

Ricerca del 6 ottobre 2026. Due parti: il catalogo dei segnali (con fonte, regola per riconoscerli, causa e mossa che li sostituisce) e la verifica sulle home di Gardens Pav, Wirmec e Benvegnù, messe a confronto con i siti reali dei tre settori aperti per questa ricerca (17 aperti, 15 misurati in tabella).

Materiali (cartella di lavoro, non nel repository): `/tmp/claude-0/-home-user-danielnistorr/89486122-32ef-5f21-add5-5cbe6108c543/scratchpad/ricerca-caratteri/segnali-ia/`
- `shots/` screenshot a 1440 dei siti di riferimento e delle nostre anteprime HTML, con `*-info.json` (caratteri, etichette, titoli, filetti letti dal browser);
- `mont/` i confronti affiancati (`macchine.jpg`, `calcestruzzo.jpg`, `hotel.jpg`, `hotel2.jpg`, `nostri.jpg`) e i ritagli citati sotto;
- `nostri/` i pezzi da 1600 px delle home (`gp/`, `wm/`, `bv/`), ottenuti con `kit/slice.py`.

Lo script di misura è copiato qui accanto: `misura-segnali.cjs` (uso nel paragrafo 7).

---

## 1. In breve

1. Le liste di segnali pubblicate nel 2026 sono due "ondate". La prima (viola, Inter, tre box con icona, badge sopra il titolo, vetro, gradienti) è quella che il committente ha già vietato. Quando la prima ondata viene vietata, i modelli ripiegano su una seconda ondata che Capital & Compute descrive così: "Warm editorial" (crema, serif a forte contrasto, terracotta), "Broadsheet cosplay" (filetti sottili, angoli vivi, colonne fitte da quotidiano) e "Template chrome" (eyebrow in maiuscolo spaziato, etichette in monospazio, frecce sui link) ([Capital & Compute, 25 set 2026](https://capitalandcompute.net/blog/fix-ai-slop-design/)). **Gardens Pav e Wirmec stanno dentro la seconda ondata**: "broadsheet cosplay" più "template chrome".
2. I caratteri che usiamo sono proprio quelli che i modelli scelgono quando gli si dice "non usare Inter". Il prompt ufficiale di Anthropic suggerisce a Claude JetBrains Mono, Fira Code, Space Grotesk, Playfair Display, Crimson Pro, la famiglia IBM Plex, Source Sans 3, Bricolage Grotesque, Newsreader ([Anthropic, 12 nov 2025](https://www.claude.com/blog/improving-frontend-design-through-skills)); Adrian Krebs, misurando 1.590 pagine, indica come "font da template" Space Grotesk, Instrument Serif, Geist, Syne, Fraunces ([README dello strumento](https://github.com/AdrianKrebs/ai-design-checker)); Adam Kucharski cita IBM Plex Mono come carattere "generico e abusato" nei lavori fatti con l'IA ([Kucharski, 2 set 2026](https://kucharski.substack.com/p/ten-reasons-your-vibe-coded-dashboard)). Gardens Pav è Archivo + IBM Plex Mono; Wirmec è IBM Plex Sans + Plex Sans Condensed + Plex Mono.
3. Il monospazio è il segnale più forte che abbiamo. Su 15 siti reali misurati, solo Escofet usa un monospazio, ed è il mono della sua stessa superfamiglia (Suisse Int'l Mono) per menu e didascalie di luogo. Gardens Pav ha il 22,5 % del testo in IBM Plex Mono e 57 etichette in maiuscolo, tutte in mono.
4. **La misura che separa meglio i nostri siti da quelli veri è la quota di pagina coperta da foto**: Gardens Pav 9,6 %, Wirmec 15,7 %, Benvegnù 40,2 %; i nove siti reali misurati stanno fra 37 e 63 % (unica eccezione Komax, 14 %, che è una pagina di notizie). Quando mancano le foto, la pagina si riempie di tipografia, filetti, etichette e numeri: è esattamente l'aspetto "IA".
5. Il ritmo è uniforme: Gardens Pav ha tutti gli H2 a 42 px, Wirmec tutti a 48 (tranne "W 1500"); Benvegnù ne ha cinque misure diverse (32, 40, 48, 56, 144). Gardens Pav e Wirmec hanno 8 fasce di fondo (bianco, grigio, scuro) quasi della stessa altezza; Escofet, Komax e Muottas Muragl 2.
6. Filetti: Gardens Pav 97 bordi sottili larghi più di 200 px, Wirmec 51, Benvegnù 43; i siti reali da 0 a 30 (mediana 9 sui 15 in tabella).
7. Frecce "→" scritte nel testo: Wirmec 20, Benvegnù 13, Gardens Pav 7; i siti reali da 0 a 2 (alcuni usano un'icona, contata a parte a occhio: Zünd e Rieder la usano su pochi link).
8. Il contenuto dei nostri siti è buono e specifico (misure, norme, cantieri, nomi degli agenti): non è il copy generico della prima ondata. Il problema è la forma: ogni dato è vestito da "scheda tecnica" (etichetta mono, filetto, freccia), e il vestito è lo stesso in ogni sezione e in ogni sito.
9. Benvegnù sembra fatto da una persona perché ha un'idea sola e visiva (le foto in bianco e nero del magazzino vero, grandi), una superfamiglia sola (Barlow e Barlow Condensed), nessun mono e titoli di misure diverse. Ha comunque cinque segnali residui (paragrafo 5.4).
10. Nessun segnale da solo dimostra l'IA: molti esistevano prima (Tailwind UI, shadcn, temi WordPress), come obiettano su Hacker News ([commenti di nomdep e raincole](https://news.ycombinator.com/item?id=47864393)). Conta l'accumulo: "vederne uno è un problema; vederne due nella stessa vista è una conferma" ([Hallmark, anti-patterns](https://github.com/Nutlope/hallmark)).

---

## 2. Fonti

| # | Fonte | Data | Cosa serve qui |
|---|---|---|---|
| F1 | Anthropic, "Improving frontend design through skills" [link](https://www.claude.com/blog/improving-frontend-design-through-skills) | 12 nov 2025 | Spiega la "convergenza distributiva" e dà la lista di caratteri da evitare (Inter, Roboto, Open Sans, Lato, Arial) e da usare (JetBrains Mono, Space Grotesk, Playfair, Crimson Pro, IBM Plex, Bricolage, Newsreader) |
| F2 | prg.sh, "Why Your AI Keeps Building the Same Purple Gradient Website" [link](https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website) | 2025 | Origine del viola: `bg-indigo-500` di Tailwind UI; scuse di Adam Wathan su X, agosto 2025 |
| F3 | Adrian Krebs, "Scoring Show HN submissions for AI design patterns" [blog](https://www.adriankrebs.ch/blog/design-slop/), [HN, 333 punti, 235 commenti](https://news.ycombinator.com/item?id=47864393), [strumento e regole](https://github.com/AdrianKrebs/ai-design-checker), [prova online](https://slopcop.adriankrebs.ch) | 20 apr 2026 | 14 schemi rilevati dal DOM su 1.590 pagine: 22 % con 4 o più schemi, 32 % con 2 o 3 |
| F4 | "Signs of AI Design" (febbhav) [link](https://github.com/febbhav/signs-of-ai-design), [HN](https://news.ycombinator.com/item?id=49063374) | lug 2026 | Lista completa per area, con la sezione "segni che non funzionano più" (il viola che migra verso crema, smeraldo, serif corsivo) |
| F5 | Impeccable, "The visible tells of AI design" [link](https://impeccable.style/slop) | 2026 | 67 regole con nome: "Label above a heading", "Tiny numbered section labels", "Hero metric layout", "Cream / beige palette", "Monotonous spacing", "Forced contrast" |
| F6 | Hallmark (Nutlope), skill anti-slop [repo](https://github.com/Nutlope/hallmark), [HN](https://news.ycombinator.com/item?id=49058547) | lug 2026 | Anti-pattern con causa e rimedio: eyebrow "spenti per default", divieto del capo di sezione a due colonne (etichetta a sinistra, titolo a destra), "Specimen fall-through", "AI nav", "AI footer", numeri inventati |
| F7 | Capital & Compute, "How to Fix AI Slop in Web Design, Tell by Tell" [link](https://capitalandcompute.net/blog/fix-ai-slop-design/) | 25 set 2026 | Prima e seconda ondata; i cinque gruppi della seconda |
| F8 | Kosta Canatselis, "Spot the slop" [link](https://world.hey.com/kostac/spot-the-slop-a-ui-designer-s-guide-to-fixing-ai-defaults-4c448c9c) | 23 lug 2026 | "Uniform everything": stessi padding, raggi, altezze; "tutto grida allo stesso volume" |
| F9 | tailthemes, "Five things make agent-built UI look generic" [link](https://tailthemes.com/blog/ai-design-slop-quality-gate) | 13 ago 2026 | Controlli verificabili: tinta unica camuffata da palette, densità uniforme (prova del 25 %) |
| F10 | Robots on Payroll, "How to avoid that vibe coded look" [link](https://robotsonpayroll.substack.com/p/how-to-avoid-that-vibe-coded-look) | 21 lug 2026 | Bordo sinistro colorato come segnale affidabile; rimedio: un file di regole tratto da un sito ammirato |
| F11 | Adam Kucharski, "Ten reasons your vibe-coded dashboard looks terrible" [link](https://kucharski.substack.com/p/ten-reasons-your-vibe-coded-dashboard) | 2 set 2026 | IBM Plex Mono come font abusato; tabelle "data dump"; colori tecnici senza tema |
| F12 | 925Studios, "AI Slop Fonts and Gradients" [link](https://www.925studios.co/blog/ai-slop-design-tells) | ott 2026 | Inter "la risposta più sicura possibile"; titoli senza peso ("Build faster. Ship smarter.") |
| F13 | Superdesign (Jason Zhou), "Why AI design looks generic" [link](https://www.superdesign.dev/blog/why-ai-design-looks-generic) | 15 giu 2026 | Convergenza distributiva spiegata per i non tecnici |
| F14 | Code My Spec (John Davenport), "Why vibe coded websites look the same" [link](https://codemyspec.com/blog/vibe-coded-websites-look-the-same) | 26 lug 2026 | Sequenza fissa di sezioni; etichette di sezione in maiuscolo |
| F15 | Hacker News, "How our vibe coded website looks like a designer made it" [link](https://news.ycombinator.com/item?id=49901973) | 29 set 2026 | 137 punti: anche con un processo da designer, i lettori riconoscono "LLMisms"; "claude brown" come nuovo colore tipico |
| F16 | Hacker News, "Are we in the era of AI slop landing pages?" [link](https://news.ycombinator.com/item?id=49024805) | 23 lug 2026 | Metriche finte ("Trusted by 10,000+ professionals") come segnale di sfiducia |
| F17 | Wikipedia, "Signs of AI writing" [link](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) | aggiornata 2026 | Segnali del testo: regola del tre, parallelismi negativi ("non solo X, ma Y"), trattini lunghi, linguaggio promozionale, "serves as" al posto di "è" |
| F18 | react.doctor, regola `no-uppercase-mono-label` [link](https://www.react.doctor/docs/rules/react-doctor/no-uppercase-mono-label) | 2026 | Un linter che segnala le etichette `font-mono uppercase tracking-widest`: il mono va riservato ai valori davvero "da codice" |
| F19 | Webdesigner Depot (Alex Harper), "The Vibe Coding Crisis" [link](https://webdesignerdepot.com/the-vibe-coding-crisis-is-web-design-becoming-a-commodity/) | 10 giu 2026 | "Feedback loop of averageness"; il verde smeraldo con vetro come nuovo template |

Limiti della ricerca: Reddit ha risposto 403 sia al sito sia alle API (r/web_design, r/UI_Design), quindi le discussioni di designer vengono da Hacker News, blog, Substack e repository; X non è leggibile senza accesso e le scuse di Adam Wathan sono citate attraverso F2 e F13. Quasi tutte le fonti parlano di pagine SaaS: i segnali valgono per noi solo dove li ritroviamo anche nelle misure (paragrafo 5).

---

## 3. Perché succede

- **Convergenza distributiva.** Un modello sceglie il seguito più probabile; senza vincoli, la pagina più probabile è la media di quello che ha letto. Anthropic lo scrive al modello stesso: "tendi a convergere verso output generici, 'on distribution'. Nel frontend questo crea quella che gli utenti chiamano estetica 'AI slop'" (F1). Lo ripetono F2, F12, F13, F19.
- **I default di chi ha scritto i dati.** Il viola nasce da `bg-indigo-500`, il colore di prova di Tailwind UI; i tre box, le card arrotondate e il badge vengono dai componenti Tailwind e shadcn più copiati (F2, F3, e il commento di port11 su [HN](https://news.ycombinator.com/item?id=47864393)).
- **La seconda ondata è fatta dalle stesse istruzioni anti-slop.** Quando si vietano Inter e viola, il modello pesca dalla lista "giusta" che gli è stata data. La lista di F1 (JetBrains Mono, Space Grotesk, IBM Plex, Bricolage, Newsreader, Playfair, Crimson Pro) e le pagine dimostrative di Hallmark (Fraunces + Geist + Geist Mono; Instrument Serif; Space Grotesk in coppia col mono) sono diventate a loro volta i caratteri riconoscibili: Krebs li conta come "Templated display fonts" (F3), F4 li chiama "tentativi di fuga" ("Geist, Space Grotesk, Instrument Serif as escape attempts"). Su HN un lettore nota che "non è più il viola di Tailwind, adesso è lo stesso schema beige" (ChrisArchitect, F3) e un altro parla di "claude brown" (jjcm, F15).
- **Il modello non ha foto.** Un generatore di codice può scrivere testo, filetti, numeri ed etichette, ma non scattare la foto del cantiere: riempie lo spazio con tipografia e decorazioni grafiche. È il motivo per cui la misura dell'area foto separa così bene i nostri siti dai riferimenti (paragrafo 5.1).
- **Le regole interne trapelano nella pagina.** Le istruzioni che diamo al modello ("ogni dato con la sua fonte", "nessun numero inventato", "etichetta e valore") sono buone per il lavoro ma finiscono stampate sul sito: didascalie con "foto della brochure", etichette sopra ogni dato, tabelle dove basterebbe una frase.

---

## 4. Catalogo dei segnali

Per ogni segnale: **regola** (come si verifica, con soglia dove possibile), **perché** (default da cui nasce), **mossa** (cosa fa un designer vero, con un esempio fotografato per questa ricerca), **fonti**, **da noi** (dove compare; i punti precisi sono nel paragrafo 5). Il peso (alto, medio, basso) dice quanto il segnale pesa nel giudizio "IA LIKE", da quante fonti lo citano e da quanto ci separa dai siti reali nelle misure.

### 4.1 Tipografia

**T1. Carattere della lista "preferiti dei modelli"** · peso alto
- Regola: il carattere principale (più del 50 % dei caratteri della pagina) o quello dei titoli è in una di queste liste. Prima ondata: Inter, Roboto, Open Sans, Lato, Arial, Poppins, Montserrat (F1, F6). Seconda ondata: Space Grotesk, Instrument Serif, Geist, Syne, Fraunces (F3); IBM Plex Mono (F11); JetBrains Mono, Fira Code, IBM Plex, Bricolage Grotesque, Newsreader, Playfair Display, Crimson Pro (lista consigliata da F1, quindi la più probabile in un sito fatto con Claude).
- Perché: sono i caratteri dei tutorial e dei prompt anti-slop; il modello li considera "distintivi" perché gli è stato detto così.
- Mossa: partire dal soggetto, non dalla lista. I siti reali misurati usano una famiglia aziendale (Frutiger a [Trumpf](https://www.trumpf.com/it_IT/) e [Metzner](https://www.metzner.com/), Helvetica Now a [Komax](https://www.komaxgroup.com/), Meta a [Godelmann](https://www.godelmann.de/)) o una superfamiglia con le sue varianti (Suisse Int'l e Suisse Int'l Mono a [Escofet](https://www.escofet.com/), Fedra Sans e Fedra Serif a [Paxmontana](https://www.paxmontana.ch/), Roboto e Roboto Condensed a [Hermle](https://www.hermle.de/en/)). Nota: Zünd usa IBM Plex Sans da solo ([zund.com](https://www.zund.com/it)) e non sembra IA: il carattere da solo non basta, conta come lo si veste (T2, T3).
- Da noi: Gardens Pav (IBM Plex Mono), Wirmec (IBM Plex intera). Benvegnù no (Barlow non compare in nessuna lista).

**T2. Monospazio come "sapore tecnico"** · peso alto
- Regola: un monospazio copre più del 5 % del testo di una pagina che non vende software, oppure serve per etichette, didascalie e valori insieme. Il controllo di F18 cerca proprio `font-mono uppercase tracking-widest` su etichette corte.
- Perché: per il modello "tecnico" e "industriale" vuol dire codice; Space Grotesk + JetBrains Mono e IBM Plex Sans + Plex Mono sono le coppie "tecniche" delle liste (F1, F6 tabella "Technical"). F4 lo chiama "monospace fonts used decoratively on marketing copy"; F7 lo mette nel "template chrome".
- Mossa: i numeri tecnici si allineano con le cifre tabellari del carattere di testo (`font-variant-numeric: tabular-nums`, F6), non cambiando carattere. Se il mono serve davvero, è quello della stessa famiglia e solo in un ruolo: Escofet lo usa per il menu e per i luoghi sotto le foto ("ELLINIKON EXPERIENCE PARK, ATENAS, GR"), mai per i dati. Su 15 riferimenti misurati, 14 non hanno mono.
- Da noi: Gardens Pav 22,5 % del testo in mono (etichette, didascalie, tabelle, conteggi); Wirmec 9,4 % (valori delle tabelle e dei modelli).

**T3. Etichetta maiuscola spaziata sopra ogni titolo (eyebrow, kicker)** · peso alto
- Regola: più di una etichetta per pagina in maiuscolo, corpo 10-14 px, spaziatura ampia, subito sopra un titolo, che ripete o anticipa l'argomento del titolo ("DEPURAZIONE" sopra "Dal dissabbiatore al depuratore biologico"). Non conta l'etichetta che porta un dato che cambia (data, luogo, codice): Zünd mette "4. OTTOBRE 2026 - 6. OTTOBRE 2026" sopra il nome della fiera, ed è informazione (`mont/zund-fiere.jpg`).
- Perché: è il primo elemento della formula dell'hero (badge, titolo, sottotitolo, due pulsanti); vietato il badge, il modello lo rende "editoriale" in mono maiuscolo.
- Mossa: il titolo dice già dove siamo; l'etichetta resta solo dove fa da indice o porta un dato. Hallmark le spegne per default e le ammette solo per contenuti davvero numerati, al massimo 1 o 2 per pagina (F6).
- Fonti: F3 ("All-caps headings and section labels"), F4 ("Eyebrow chip above the headline", "Repeated section kickers"), F5 ("Label above a heading"), F6, F7, F14, F18.
- Da noi: Gardens Pav ogni sezione; Benvegnù tre volte, con un filetto corto davanti ("DAL CATALOGO"); Wirmec una sola, in tondo minuscolo ("Dal 2010 a Ponte San Nicolò, Padova"), che va bene.

**T4. Titolo in due frasi col punto ("X. Y.")** · peso medio
- Regola: H1 o H2 che finiscono col punto e contengono due frasi brevi, la seconda a effetto ("36 cantieri, da Aosta ad Avetrana. Cinque oltre confine."). Soglia: più di un titolo col punto per pagina.
- Perché: è il ritmo dello slogan che i modelli imparano dalle landing ("Build faster. Ship smarter.", F12); F5 lo chiama "Forced contrast: repeated lines make every point sound like a slogan".
- Mossa: titolo descrittivo senza punto, come nei siti reali misurati (0 titoli col punto su 22 a Komax e Trumpf, 0 su 19 a Zünd, 2 su 25 a Escofet).
- Da noi: Gardens Pav 5 titoli su 13 col punto, compreso l'H1 in due frasi.

**T5. Parola d'accento in un altro carattere, in corsivo o in un altro colore** · peso alto (già vietato)
- Regola: nel titolo una parola sola cambia carattere, stile o colore. È lo schema n. 2 di F3 ("Hero font mix"); F6 lo chiama "uno dei segnali IA più affidabili".
- Da noi: assente. Da tenere nella lista dei divieti.

**T6. Gerarchia fatta di pesi vicini e misure uguali** · peso medio
- Regola: tutti gli H2 della home alla stessa misura; titoli a 600 e testo a 400 senza un terzo livello. Soglia: almeno 3 misure diverse di H2 in home.
- Perché: il modello applica una scala tipografica come un modulo; F6: "peso 400 accanto a 600 sembra un'impostazione di default; 200 accanto a 800 sembra una scelta"; F8 "Uniform everything".
- Mossa: un elemento davvero grande per pagina e gli altri che arretrano (F9 "Designate one genuinely oversized element per page"). Benvegnù lo fa: H2 a 32, 40, 48, 56 e 144 px ("VIENI AL BANCO" sopra la foto della sede).
- Da noi: Gardens Pav una sola misura di H2 (42 px, Archivo 600); Wirmec due (48 px e 176 px per "W 1500").

### 4.2 Colore

**C1. Viola, indaco, gradienti, testo in gradiente, alone colorato** · peso alto (già vietato)
- Regola: F3 schemi 3, 4, 7. Da noi: assenti.

**C2. Palette della seconda ondata** · peso alto
- Regola: fondo crema o beige con serif e accento terracotta vicino a #D97757 ("Warm editorial"); quasi nero con un verde acido o un vermiglione ("Dark signal"); verde smeraldo come sostituto del viola (F4, F7, F19); F5 ha la regola "Cream / beige palette".
- Perché: è la palette del marchio Claude e degli esempi "di buon gusto" (F15 "claude brown"; commento di ChrisArchitect in F3).
- Mossa: il colore viene dal soggetto (il materiale, le foto, il logo esistente). Rieder mostra i campioni di colore dei suoi pannelli invece di inventare una palette ([rieder.cc](https://www.rieder.cc/us/)); Escofet scrive i titoli in un verde scuro e lascia il colore alle foto delle piazze.
- Da noi: Gardens Pav (arancio del logo su grigi e quasi nero) e Wirmec (rosso del logo su ardesia) partono dal marchio, e va bene. Attenzione per Albergo Vescovi: il documento 02 già scarta "beige, ocra e Bembo" come "cliché crema e serif".

**C3. Un accento solo che fa tutti i lavori** · peso medio
- Regola: lo stesso colore saturo per pulsanti, sottolineature dei link, numeri grandi, trattini sotto i titoli e frecce. F9: "una palette ha bisogno di un secondo lavoro, non di un secondo campione".
- Mossa: il colore del marchio su una o due cose (pulsante e logo); il resto della pagina prende tono dalle foto. Benvegnù tiene il rosso solo nella barra del carosello.
- Da noi: Gardens Pav arancio su pulsanti, link, numeri 0,88 e 0,40, quote del disegno; Wirmec rosso su pulsanti, link, 6 trattini sotto i titoli.

**C4. Fasce alterne a ritmo regolare** · peso alto
- Regola: 6 o più fasce di fondo a tutta larghezza (bianco, grigio, scuro) di altezza simile. Misura del paragrafo 5.1: i nostri 6-8, i riferimenti 2-6 (eccezione Rieder, 10, per i caroselli).
- Perché: "ogni sezione un blocco" è il modo in cui i generatori e i page builder compongono una pagina; F4 "Monotonous spacing with uniform padding and section gaps", F5 "Monotonous spacing", F9 "Uniform density: squint or shrink to 25 %; if every band matches, layout is a list".
- Mossa: un fondo solo per quasi tutta la pagina e un unico cambio deciso (Escofet, Komax, Muottas Muragl: 2 fasce); oppure fasce date dalle foto a tutta larghezza (Krone, Hirschen).

### 4.3 Impaginazione

**L1. Titolo a sinistra, paragrafo a destra, in ogni sezione** · peso alto
- Regola: in 3 o più sezioni l'H2 occupa la colonna sinistra e un paragrafo introduttivo la colonna destra, alla stessa altezza.
- Perché: è la testata di sezione dei kit Tailwind e dei temi Elementor; Hallmark vieta la variante più marcata ("tag-left / heading-right", "il segnale più affidabile di un editoriale da template") e descrive il pacchetto "Specimen": etichette numerate a margine, titolo grande, colonne asimmetriche, filetti sottili (F6). Nessuna fonte esterna nomina proprio "titolo a sinistra, paragrafo a destra": è una osservazione nostra, confermata dal confronto (nei riferimenti fotografati non l'abbiamo trovata ripetuta in più sezioni).
- Mossa: titolo e testo nella stessa colonna, con la foto che guida (Escofet: foto a sinistra, testo grande a destra, una volta sola; Hirschen: foto e due righe).
- Da noi: Gardens Pav ("Dal dissabbiatore al depuratore biologico."), Wirmec ("Una stazione, una lavorazione sul cavo", "WirTest, il controllo dell'aggraffatura"), Benvegnù ("IL CATALOGO").

**L2. Capo di sezione "a cartella": etichetta a sinistra, etichetta a destra, filetto con le stanghette** · peso alto
- Regola: sopra ogni sezione una riga con due etichette in mono maiuscolo agli estremi e un filetto con i bordi rialzati. È il "Broadsheet cosplay" di F7.
- Mossa: nessuna testata ripetuta; se serve un indice, un menu ancorato o un titolo.
- Da noi: Gardens Pav in tutte e sei le sezioni.

**L3. Filetti ovunque** · peso alto
- Regola: più di 30 bordi sottili (1-2 px) larghi più di 200 px nella home. Gardens Pav 97, Wirmec 51, Benvegnù 43; riferimenti da 0 (Rieder, Hirschen, Fex) a 30 (Escofet), mediana 9.
- Perché: "etichetta, valore, filetto" è il modo più semplice di rendere "tecnico" un dato; F5 "Hairline border with wide shadow", F6 "Specimen... hairline rules", F7.
- Mossa: lo spazio separa, il filetto solo dove c'è una tabella vera.

**L4. Numero grande con etichetta piccola, righe di statistiche** · peso medio
- Regola: un numero a corpo da titolo con una didascalia sotto, da solo o in fila (F3 "Stat banner", F5 "Hero metric layout"); peggio se il numero non ha fonte (F6 "Invented metrics", F16).
- Perché: la casella "prova sociale" del template; il modello la riempie anche con dati veri, ma la forma resta quella.
- Mossa: il numero dentro una frase o in una tabella dove serve. Attenzione: anche Trumpf ha una riga "518,5 · 12 % · 3.006": è un segnale solo se si somma ad altri.
- Da noi: Gardens Pav "0,88" e "0,40" (dati veri, forma da template) e la fascia a quattro colonne sotto l'hero; Wirmec la riga "Stazioni · Sezione cavo · Alimentazione · Unità" sotto la macchina e "W 1500" a 176 px; Benvegnù "329 articoli Vibram al banco".

**L5. Numerazioni 01, 02, 03** · peso medio
- Regola: numeri a due cifre davanti a voci che non sono una sequenza (F3 "Numbered steps", F4 "Numbered section markers", F5 "Tiny numbered section labels"). Un commento su HN: l'IA "aggiunge bordi colorati, tag e numeri superflui dappertutto" (joegibbs, F3).
- Mossa: numerare solo una procedura vera.
- Da noi: Wirmec 01-12 davanti alle dodici lavorazioni, che non sono in ordine.

**L6. Indice a righe con conteggio e freccia** · peso medio
- Regola: lista di categorie, ognuna con il conteggio in mono e "→" ("Vasche monoblocco · 17 MISURE →", "WirTool · 10 modelli →").
- Mossa: le categorie come foto cliccabili (Benvegnù, catalogo con le foto del magazzino; Hermle, quattro foto con nome).
- Da noi: Gardens Pav nell'hero; Wirmec nella fascia a sei colonne sotto l'hero.

**L7. Hero diviso a metà con due pulsanti (pieno e vuoto)** · peso basso
- Regola: testo a sinistra, immagine a destra, pulsante pieno e pulsante a contorno (F7 "Stock page order", F14).
- Mossa: un'azione sola o nessuna sopra la piega (Hermle, Komax: un pulsante; Escofet, Hirschen: nessuno).
- Da noi: tutti e tre.

**L8. Menu e piede "da IA"** · peso basso
- Regola: logo a sinistra, 5-6 voci, pulsante a destra, filetto sotto; piede a quattro colonne con riga di copyright (F6 "The AI nav", "The AI footer"). Molti siti reali fanno lo stesso (Komax, Hermle): conta poco.
- Da noi: tutti e tre.

### 4.4 Componenti

**K1. Badge e pill sopra il titolo; card con icona in fila; FAQ a fisarmonica; testimonianze e loghi inventati** · peso alto (in gran parte già vietati)
- Regola: F3 schemi 13 e 14; F4 "Testimonial walls", "Logo soup"; F6 "Icon-tile feature card".
- Da noi: assenti in home. I loghi di Benvegnù sono i marchi venduti al banco: informazione vera.

**K2. Tabelle tecniche complete in home** · peso medio
- Regola: in home una o più tabelle di 6 o più righe di dati di prodotto (F11 "Data dump in main table").
- Perché: il modello ha i dati e li mostra tutti; nessuno gli dice che la home è un riassunto.
- Mossa: la home mostra una macchina o un prodotto per famiglia, con 2-3 dati in una frase; le tabelle stanno nelle schede (Komax, Hermle, Trumpf: nessuna tabella in home).
- Da noi: Gardens Pav (vasca 550, otto modelli di piattaforma, quattro classi del calcestruzzo, elenco di 36 cantieri); Wirmec (sette modelli WirAM, tabella W 1500, tabella WirTool).

**K3. Disegni ridisegnati e "schede" finte** · peso basso
- Regola: disegno tecnico rifatto in grafica con quote e didascalia in mono, che imita un catalogo (F6 lo chiama, per le interfacce, "Re-drawn UI chrome").
- Mossa: usare il disegno dell'azienda o una foto del prodotto posato.
- Da noi: Gardens Pav, pianta della piattaforma con quote arancio e didascalia mono. I disegni dei cavi di Wirmec vengono dalle brochure: sono un contenuto vero, si tengono.

### 4.5 Testi

**W1. Titoli-slogan a due tempi e contrasti forzati** · peso medio
- Regola: "X. Y." (T4); "Non solo X, ma Y"; "non è X, è Y" (F17 "Negative parallelisms"; F4 "negation pivots"; F5 "Forced contrast").
- Da noi: Gardens Pav "36 cantieri, da Aosta ad Avetrana. Cinque oltre confine.", "Vasche e impianti per il trattamento delle acque. Piattaforme prefabbricate per autolavaggi.".

**W2. Triadi ornamentali** · peso basso
- Regola: tre aggettivi o tre verbi in fila senza che servano tutti (F17 "Rule of three"). Le triadi di fatti veri non contano ("tagliare, spelare e aggraffare" sono le tre lavorazioni di Wirmec).
- Da noi: nessuna triade vuota trovata in home.

**W3. Promesse vaghe e parole da brochure** · peso alto (già vietato)
- Regola: "soluzioni", "eccellenza", "innovazione", "a 360 gradi", "supercharge", "elevate" (F4, F5, F12, F17 "promotional language"); in italiano anche "è importante sottolineare", "vale la pena ricordare", "in molti casi", "si può affermare che" ([Studio Cataldi, 10 apr 2026](https://www.studiocataldi.it/articoli/48141-come-riconoscere-un-testo-scritto-con-chatgpt.asp)).
- Da noi: assenti. Il copy dei tre siti è specifico (misure, norme, nomi). È il punto forte da tenere.

**W4. Fonte stampata nella didascalia** · peso medio
- Regola: didascalie che dichiarano da dove viene la foto del cliente stesso ("foto della brochure Wirmec", "Foto della scheda W200", "Servizio fotografico della scheda Booking.com").
- Perché: è la regola di lavoro "ogni dato con la fonte" che finisce sul sito; un sito aziendale non cita la propria brochure.
- Mossa: didascalia che dice dove e cosa ("Altivole (TV), autolavaggio, 2019"), come Escofet ("LA EXPLANADA, ALICANTE, ES"). La fonte resta nel LEGGIMI.
- Da noi: Wirmec (tre didascalie); prova delle accoppiate di Albergo Vescovi (tre didascalie).

**W5. Didascalie che descrivono l'ovvio, in maiuscolo mono** · peso medio
- Regola: didascalia che ripete quello che la foto mostra ("VASCA RETTANGOLARE MONOBLOCCO SOLLEVATA CON L'AUTOGRU") o che imita un cartiglio tecnico ("PISTA SELF MOD. 450 · PIANTA IN CM · 2 PANNELLI 228 × 650 × 20, ...").
- Mossa: niente didascalia, o il luogo e l'anno.
- Da noi: Gardens Pav.

**W6. Microcopy ripetuto** · peso basso
- Regola: lo stesso invito tre o più volte in home ("Richiedi informazioni", "Richiedi un'offerta"); F5 "Same text repeated inside one container".
- Da noi: Gardens Pav "Richiedi informazioni" 3 volte; Wirmec "Richiedi un'offerta" 3 volte.

### 4.6 Interazione e movimento

**M1. Sezioni in dissolvenza allo scorrimento, contatori che salgono, rimbalzi** · peso alto (in parte già vietato)
- Regola: F4 "Identical fade-in entrance on every section", F5 "Bounce or elastic easing", F7 "count-up stats".
- Da noi: nelle specifiche non ci sono; da verificare in Elementor (le animazioni d'ingresso sono un'opzione di ogni widget).

**M2. Microanimazioni uguali su ogni link** · peso basso
- Regola: la freccia che si sposta di qualche pixel al passaggio su ogni link (specifica di Gardens Pav, par. 3: "la freccia si sposta di 4 px a destra"); F4 "Scattered, uncoordinated micro-interactions".
- Mossa: il link si sottolinea, basta.

**M3. Barra di avanzamento del carosello** · peso basso
- Da noi: Benvegnù (barra rossa sotto i prodotti).

### 4.7 Immagini

**I1. Poche foto, piccole** · peso alto
- Regola: area coperta da immagini sotto il 30 % della home a 1440 (misura del paragrafo 5.1). Nessuna fonte esterna la misura; è il dato del nostro confronto, ed è il più netto.
- Perché: il modello non ha foto e compensa con grafica (paragrafo 3).
- Mossa: chiedere al cliente le foto vere prima di impaginare, o farle; dare a una foto metà schermo. Escofet 63 %, Krone 58 %, Trumpf 54 %, Hirschen 53 %, Hermle 48 %, Benvegnù 40 %.
- Da noi: Gardens Pav 9,6 %, Wirmec 15,7 %.

**I2. Foto stock, rendering, illustrazioni 3D, foto IA** · peso alto
- Regola: F4 parte II (dominante giallastra, pelle cerea, bokeh uniforme, illuminazione cinematografica, testo storpiato sullo sfondo), F6 "AI-illustration look".
- Da noi: le foto sono dell'azienda. I rendering delle vasche di Gardens Pav sono del catalogo: veri, ma su fondo grigio uniforme e tutti alla stessa scala hanno l'aspetto "3D da template"; meglio una foto della vasca in cantiere come apertura.

**I3. Prodotti scontornati tutti uguali** · peso basso
- Da noi: Wirmec (macchine scontornate su grigio o bianco). È la norma del settore (Komax, Hermle): si tiene, ma serve almeno una foto della macchina al lavoro o del reparto.

### 4.8 Dettagli

**D1. Trattino colorato corto sotto i titoli** · peso medio
- Regola: barra di 20-40 px nel colore del marchio sotto ogni H2. Nessuna fonte esterna la nomina; è un elemento tipico dei temi WordPress e dei widget "divisore" dei page builder, che i modelli ripetono quando lavorano in Elementor (osservazione nostra).
- Da noi: Wirmec, sotto 6 titoli.

**D2. Freccia → in ogni link** · peso medio
- Regola: più di 2 frecce scritte come carattere in una pagina (F7 "arrows on links"). Misura: Wirmec 20, Benvegnù 13, Gardens Pav 7; riferimenti 0-2.
- Mossa: il link si riconosce dalla sottolineatura; la freccia solo sul link che porta fuori (Zünd usa "↗" solo per le pagine delle fiere).

**D3. Puntino separatore "·" nelle etichette** · peso basso
- Regola: etichette composte "A · B" ("OPERE IN CALCESTRUZZO · LEGNARO (PD)", "0-1000 N · 50 mm/min"). Osservazione nostra: va insieme all'eyebrow (T3) e da solo conta poco.
- Da noi: Gardens Pav e Wirmec.

**D4. Bordo colorato a sinistra delle card, glassmorphism, emoji, icone Lucide** · peso alto (già vietati)
- Da noi: assenti.

---

## 5. Verifica sui nostri siti

### 5.1 Misure a confronto

Tutte le pagine a 1440 px, lette dal browser con `misura-segnali.cjs` (i nostri dalle anteprime HTML di `_prova/build/anteprima/01-home.html` e `BenvegnuSrl-Sito/anteprima/01-home.html`, uguali agli screenshot Elementor). "Etichette" = testi corti in maiuscolo sotto i 15 px (comprende menu e pulsanti, quindi va letto insieme al mono). "Frecce" = solo i caratteri →, ›, », ↗ scritti nel testo. "Fasce" = tratti di fondo uniforme a tutta larghezza alti più di 200 px.

| Pagina | Caratteri (quota del testo) | Mono | Etichette (in mono) | Frecce | Titoli col punto | Misure H2 | Filetti | Fasce | Area foto |
|---|---|---|---|---|---|---|---|---|---|
| **Gardens Pav** | Archivo 77 %, IBM Plex Mono 23 % | 22,5 % | 57 (57) | 7 | 5/13 | 1 | 97 | 8 | **9,6 %** |
| **Wirmec** | IBM Plex Sans 76 %, Plex Sans Condensed 14 %, Plex Mono 9 % | 9,4 % | 0 | 20 | 0/22 | 2 | 51 | 8 | **15,7 %** |
| **Benvegnù** | Barlow 85 %, Barlow Condensed 15 % | 0 | 54 (0) | 13 | 0/22 | 5 | 43 | 6 | **40,2 %** |
| Escofet (calcestruzzo, ES) | Suisse Int'l, Suisse Int'l Mono, Arial | 23,6 % | 64 (64) | 1 | 2/25 | | 30 | 2 | 63,3 % |
| Rieder (calcestruzzo, AT) | Tomato Grotesk, PP Grafier | 0 | 0 | 0 | 1/11 | | 0 | 10 | 54,6 % |
| Godelmann (calcestruzzo, DE) | Meta Pro | 0 | 0 | 0 | 2/16 | | 1 | | 39,4 % |
| Mall (vasche, DE) | Arial | 0 | 0 | 0 | 0/3 | | 15 | 5 | |
| Ulma (prefabbricati, ES) | Open Sans, Open Sans Condensed | 0 | 6 | 0 | 0/7 | | 9 | 4 | |
| Hermle (macchine, DE) | Roboto, Roboto Condensed | 0 | 21 | 0 | 0/7 | | 10 | 6 | 48,4 % |
| Zünd (macchine, CH) | IBM Plex Sans | 0 | 81 | 0 | 0/19 | | 10 | 5 | |
| Komax (macchine per cavo, CH) | Helvetica Now | 0 | 2 | 0 | 0/22 | | 13 | 2 | 14,2 % |
| Trumpf (macchine, DE) | Frutiger | 0 | 76 | 0 | 0/22 | | 21 | 4 | 53,9 % |
| Metzner (macchine per cavo, DE) | Frutiger Condensed | 0 | 0 | 0 | 0/5 | | 1 | 3 | |
| Hirschen (hotel, AT) | Korpus Grotesk | 0 | 0 | 1 | 0/2 | | 0 | | 52,9 % |
| Krone (hotel, AT) | Roboto Condensed, Roboto | 0 | 16 | 0 | 4/8 | | 2 | 3 | 58,0 % |
| Paxmontana (hotel, CH) | Fedra Sans, Fedra Serif | 0 | 8 | 0 | 0/2 | | 12 | | 37,0 % |
| Muottas Muragl (hotel, CH) | Roboto, Roboto Condensed, nyght Serif | 0 | 3 | 2 | 0/10 | | 8 | 2 | |
| Hotel Fex (hotel, CH) | Avenir, Cormorant Garamond | 0 | 0 | 1 | 0/7 | | 0 | | |

Celle vuote: misura non fatta o non affidabile (pagina con banner dei cookie o con scorrimento a schermate). Pfösl, Zirmerhof e Briol sono rimasti dietro il banner dei cookie o sono usciti vuoti e non sono in tabella.

Cosa dicono i numeri:
- nessun riferimento ha insieme mono, più di 30 filetti, frecce scritte e 8 fasce; Gardens Pav ha tutto;
- l'unico con tanto mono (Escofet) ha il 63 % di foto: lì il mono è una didascalia sotto immagini grandi, da noi è il tessuto della pagina;
- "etichette maiuscole" da sole non distinguono (Zünd 81, Trumpf 76 tra menu, date e pulsanti): distinguono quando sono in mono e stanno sopra i titoli.

### 5.2 Gardens Pav, home (`GardensPav-Sito/_prova/shots/el-01-home-desktop.png` e `-mobile.png`)

Posizioni in px dall'alto nello screenshot a 1440; i pezzi sono in `nostri/gp/el-01-home-desktop-N.jpg` (N = posizione / 1600).

| Punto | Dove (1440) | Segnali |
|---|---|---|
| Etichetta "OPERE IN CALCESTRUZZO · LEGNARO (PD)" sopra l'H1 | y 155, pezzo 0 | T2, T3, D3 |
| H1 in due frasi col punto, "Vasche e impianti ... acque. Piattaforme prefabbricate per autolavaggi." (a 390 px va su 6 righe) | y 215-280; mobile pezzo 0 | T4, W1 |
| Indice "Vasche monoblocco 17 MISURE →" e altre tre righe, con filetti | y 505-730 | L6, L3, D2, T2 |
| Due pulsanti, pieno e a contorno | y 790 | L7 |
| Didascalia "VASCA RETTANGOLARE MONOBLOCCO SOLLEVATA CON L'AUTOGRU" | y 920 | W5, T2 |
| Fascia a quattro colonne "SEDE E STABILIMENTO / TELEFONO E ORARI / TRASPORTO E POSA / CANTIERI" con etichette mono | y 980-1125 | L4, T3, L3 |
| Capo "VASCHE PREFABBRICATE MONOBLOCCO · MISURE ESTERNE IN CM, PESI IN TONNELLATE" con filetto a stanghette (si ripete in ogni sezione: y 2095, 3185, 4280, 4840, 5980) | y 1320 | L2, T3 |
| H2 "Undici misure rettangolari e sei circolari, da 2,30 a 50 mc." | y 1425 | T4, T6 |
| Quota "550 cm" e scheda "VASCA RETTANGOLARE 550" a quattro celle mono | y 1745-1880, pezzo 1 | K2, K3, T2 |
| "Dal dissabbiatore al depuratore biologico." a sinistra, paragrafo a destra | y 2190-2255 | L1, T4 |
| Griglia di 7 impianti con etichette mono "PORTATA da 3 a 38 l/s" | y 2310-2985 | T2, L3 |
| Fascia scura: tabella mono di 8 modelli, pianta quotata con didascalia mono a cartiglio, "0,88" e "0,40" in arancio | y 3265-4030, pezzo 2 | K2, K3, W5, L4, C3 |
| Quattro celle "C35/45 · XC4 ... · B450C · S4" | y 4390-4555 | L4, K2 |
| H2 "36 cantieri, da Aosta ad Avetrana. Cinque oltre confine." | y 5195, pezzo 3 | W1, T4 |
| Elenco di 36 città con sigle di provincia in mono | y 5460-5780 | K2, T2 |
| Contatti con etichette mono a sinistra ("TELEFONO", "EMAIL", "ORARI") | y 6080-6380 | T2, T3 |
| Piede a quattro colonne | y 6530 | L8 |

Conteggio: 22 segnali diversi, di cui 8 di peso alto (T1, T2, T3, C4, L1, L2, L3, I1). È il caso più marcato: la pagina è quasi tutta "scheda tecnica" e le foto coprono meno di un decimo.

Cosa cambiare, in ordine di effetto: (1) foto grandi del cantiere e del prodotto posato (almeno un terzo della pagina; le foto delle realizzazioni ci sono, 36 cantieri); (2) togliere IBM Plex Mono: cifre tabellari di Archivo per i numeri, nessuna etichetta sopra i titoli; (3) togliere i capi "a cartella" e due terzi dei filetti; (4) titoli senza punto; (5) tabelle complete nelle pagine prodotto, in home una frase per famiglia; (6) massimo 4 cambi di fondo.

### 5.3 Wirmec, home (`Wirmec-Sito/_prova/shots/el-01-home-desktop.png` e `-mobile.png`)

| Punto | Dove (1440) | Segnali |
|---|---|---|
| Hero diviso, due pulsanti, macchina scontornata su grigio | y 265-880, pezzo 0 | L7, I3 |
| Riga "Stazioni · Sezione cavo · Alimentazione cavo · Unità aggraffatrici" con valori mono ("fino a 5", "0,13-6 mm²") e "Scheda AM460 →" | y 740-880 | L4, T2, D2 |
| Fascia a sei colonne "WirTool ... 10 modelli →" con filetti verticali | y 955-1125 | L6, D2, L3 |
| "Una stazione, una lavorazione sul cavo" a sinistra, paragrafo a destra, trattino rosso sotto | y 1275-1390 | L1, D1 |
| Lavorazioni numerate 01-12 con filetti (a 390 px occupano circa due schermate) | y 1465-2240, pezzi 0-1 | L5, L3 |
| Fascia scura "WirAM, taglia spela aggraffa automatiche" con trattino rosso e 7 righe di modelli con specifiche mono e → | y 2440-3255, pezzo 1 | C4, D1, K2, T2, D2 |
| "W 1500" a 176 px, trattino rosso, tabella con valori mono | y 3540-4230, pezzo 2 | L4, D1, K2, T2 |
| Didascalia "W 1500, foto della brochure Wirmec." | y 4280 | W4 |
| Fascia grigia "WirTool, applicatori": tabella mono e "I dieci applicatori WirTool →" | y 4760-5330, pezzi 2-3 | C4, K2, D2 |
| "WirTest, il controllo dell'aggraffatura" a sinistra, paragrafo a destra, trattino rosso | y 5570-5690, pezzo 3 | L1, D1 |
| Didascalie "Foto della scheda AM210 futura", "Foto della scheda W200" | y 6090-6140 | W4 |
| "Richiedi un'offerta" (terza volta), telefono grande, agenti con numeri in mono | y 6620-6920, pezzo 4 | W6, T2 |
| Piede a quattro colonne | y 7215 | L8 |

Conteggio: 17 segnali diversi, 6 di peso alto (T1, T2, C4, L1, L3, I1). Meno marcato di Gardens Pav (niente etichette maiuscole, niente titoli col punto), ma ha la combinazione più riconoscibile del secondo tipo: famiglia IBM Plex con Mono, frecce dappertutto (20), trattini rossi.

Cosa cambiare: (1) via IBM Plex Mono, cifre tabellari nel Sans (`tabular-nums`); valutare se tenere IBM Plex Sans da solo, come Zünd, o una famiglia meno associata alle liste (decisione della ricerca sulle accoppiate); (2) via i 6 trattini rossi e le frecce, tranne su "Brochure in PDF"; (3) via la numerazione 01-12; (4) didascalie senza fonte; (5) una foto della macchina al lavoro o del reparto a tutta larghezza; (6) tabelle nelle schede, non in home.

### 5.4 Benvegnù, home: il sito giudicato "molto meglio" (`BenvegnuSrl-Sito/screenshot/elementor/01-home-desktop.jpg`)

Perché regge:
- un'idea sola e visiva: le foto in bianco e nero del magazzino e della sede, grandi (40 % della pagina), con il titolo "VIENI AL BANCO" a 144 px che si sovrappone alla foto (y 4345, pezzo 2);
- una superfamiglia sola, Barlow e Barlow Condensed (disegnata sulla segnaletica e sulle targhe californiane, [Google Fonts](https://fonts.google.com/specimen/Barlow); adatta a un fornitore da banco), nessun mono, nessun carattere delle liste;
- titoli di cinque misure diverse, quindi una gerarchia vera (T6 rispettato);
- contenuto di banco, non di brochure: codici e nomi di articoli veri ("2600 LIVERPOOL", "FORBICI LARIZ LAME CURVE"), marchi venduti.

Segnali residui, da togliere anche lì:
- eyebrow con trattino davanti, tre volte: "DAL CATALOGO" (y 2200), "RIVENDITORE AUTORIZZATO VIBRAM" (y 2905), "PER CHI LAVORIAMO" (y 3710) · T3;
- "IL CATALOGO" a sinistra e paragrafo a destra (y 960-1040) · L1;
- "329" a corpo enorme con "ARTICOLI VIBRAM AL BANCO" (y 2970-3080) · L4;
- 13 frecce scritte ("VEDI →", "TUTTO IL CATALOGO →", righe "SUOLE 177 →") · D2;
- fascia a quattro colonne di contatti con etichette maiuscole e filetti (y 5000-5190) e piede a quattro colonne · L3, L8;
- barra rossa di avanzamento del carosello (y 2640) · M3.

### 5.5 Albergo Vescovi, prototipi (`AlbergoVescovi-Sito/_prova/direzioni/*/proto-1440.png`)

Alle 17:08 sono state create le cartelle `lavoro/` e `luogo/` con le sole immagini; all'ultimo controllo (ore 17:33 UTC) i file `proto-1440.png` non esistono ancora, quindi la verifica dei prototipi non è stata fatta. Da applicare appena ci sono: la tabella del paragrafo 7 e `misura-segnali.cjs` su `proto.html`.

Verificato invece quello che c'è già, la prova delle accoppiate (`AlbergoVescovi-Sito/_prova/ricerca/accoppiate-prova.png`, ritaglio `nostri/av/accoppiate-0.jpg`):
- Newsreader (accoppiata B) è nella lista che Anthropic consiglia ai suoi modelli (F1): è un carattere che un sito fatto con Claude sceglie spesso · T1;
- in tutte e tre le colonne ci sono sottotitoli in maiuscolo spaziato sopra il testo ("SAUNA E BAGNO TURCO", "ORARI E PREZZI") · T3 (da tenere a uno per pagina);
- didascalie con la fonte ("La sauna. Servizio fotografico della scheda Booking.com.") · W4;
- righe "Su prenotazione 15:00 · 19:00" con filetti: qui sono informazione vera (orari e prezzi), si tengono, ma senza farne il motivo di ogni sezione · L3;
- pulsanti a pillola nella colonna A: non sono nella lista dei divieti, ma i pill sono un segnale citato (F4 "pill", F7 "pill badge").
Bene: il documento 02 scarta già "beige, ocra e Bembo" (C2), e le tre colonne usano foto vere dell'albergo.

---

## 6. Confronto con siti reali (screenshot di questa ricerca)

Screenshot in `shots/` e confronti in `mont/`. Cosa fanno, settore per settore, che i nostri non fanno.

**Macchine** (`mont/macchine.jpg`: [Hermle](https://www.hermle.de/en/), [Zünd](https://www.zund.com/it), [Komax](https://www.komaxgroup.com/), [Trumpf](https://www.trumpf.com/it_IT/); in più [Metzner](https://www.metzner.com/))
- Una famiglia aziendale (Frutiger, Helvetica Now, Roboto e Roboto Condensed, IBM Plex Sans) e nessun mono.
- Contenuto che ha una data e una persona: fiere con date, città e numero di stand (Zünd, `mont/zund-fiere.jpg`), storie di clienti con nome (Komax "The Story of Confecta"), notizie datate (Hermle, Komax). È il segnale "umano" più forte: un modello non inventa la fiera di Kortrijk del 4-6 ottobre 2026 con lo stand 4151.
- Foto di persone al lavoro e di reparti, a tutta larghezza (Hermle 48 %, Trumpf 54 %).
- Sono siti aziendali poco eleganti, con caroselli e banner, ma nessuno li scambierebbe per IA: il disordine dei contenuti veri è una firma.

**Calcestruzzo e prefabbricati** (`mont/calcestruzzo.jpg`: [Escofet](https://www.escofet.com/), [Rieder](https://www.rieder.cc/us/), [Godelmann](https://www.godelmann.de/), [Mall](https://www.mall.info/); in più [Ulma](https://www.ulmaarchitectural.com/it-it))
- Escofet (`mont/escofet-a.jpg`): il prodotto fotografato in uso, nelle piazze, a tutta pagina; titoli grandi ma in peso Light (45 px, un solo peso), in verde; mono solo per luoghi e menu. È il riferimento da cui è venuto il mono di Gardens Pav: preso il mono, lasciate le foto.
- Rieder: i campioni dei materiali come immagine principale, progetti con nome e città ("Soccer City Stadion Johannesburg, ZA"), una citazione firmata dal titolare (Wolfgang Rieder).
- Mall e Godelmann: impaginazione vecchia, un carattere solo (Arial, Meta), verde del marchio, molte foto di prodotto. Datati, ma non sintetici.

**Hotel di montagna** (`mont/hotel2.jpg`: [Hotel Fex](https://www.hotelfex.ch/), [Hirschen](https://www.hotel-hirschen-bregenzerwald.at/), [Paxmontana](https://www.paxmontana.ch/); in più [Krone](https://www.krone-hittisau.at/) e [Muottas Muragl](https://www.muottasmuragl.ch/de) in `mont/hotel.jpg`)
- Hirschen: fondo nero, foto d'atmosfera vere (piatti, sale illuminate, la casa), quasi niente testo, un carattere solo. Il 53 % è foto.
- Krone: mosaico di foto con etichette brevi (58 %).
- Paxmontana (`mont/pax-eventi.jpg`): eventi con nome, data e orario ("Harfen-Brunch mit Felix Widrig, Sonntag, 1. November 2026, 10.00 bis 13.30 Uhr"), superfamiglia Fedra Sans e Fedra Serif.
- Hotel Fex: impaginazione semplice, ma orari di apertura delle stagioni, orari del trasferimento, una citazione: informazione di casa, non di template.

---

## 7. Regole per i prossimi siti (controllo prima di consegnare)

Misura: `node /home/user/danielnistorr/_metodo/ricerca-caratteri/misura-segnali.cjs <cartella> <nome> file:///.../01-home.html` scrive `<nome>-1440-info.json` e gli screenshot; i valori `imgPct`, `monoPct`, `labels`, `arrows`, `headsDot`, `h2sizes`, `hairlines` vanno confrontati con le soglie qui sotto. Le fasce si contano a occhio sullo screenshot intero.

| # | Controllo | Soglia (home a 1440) | Segnale |
|---|---|---|---|
| 1 | Area coperta da foto | almeno 35 % | I1 |
| 2 | Caratteri | una famiglia o una superfamiglia; un secondo carattere solo per una funzione; nessun carattere principale delle liste di T1 | T1 |
| 3 | Monospazio | 0 % se il sito non vende software; altrimenti meno del 5 % e della stessa famiglia | T2 |
| 4 | Etichette maiuscole sopra i titoli | al massimo 1 (salvo date o luoghi) | T3 |
| 5 | Titoli col punto | al massimo 1; nessun titolo in due frasi | T4, W1 |
| 6 | Misure diverse degli H2 | almeno 3 | T6 |
| 7 | Fasce di fondo a tutta larghezza | al massimo 4, di altezze diverse | C4 |
| 8 | Titolo a sinistra e paragrafo a destra | al massimo 1 sezione | L1 |
| 9 | Filetti larghi più di 200 px | meno di 30 | L3 |
| 10 | Frecce scritte nei link | al massimo 2 | D2 |
| 11 | Numero grande con etichetta | al massimo 1, e solo se è il dato per cui il cliente viene scelto | L4 |
| 12 | Numerazioni 01, 02 | solo per una procedura in ordine | L5 |
| 13 | Tabelle in home | nessuna oltre le 4 righe | K2 |
| 14 | Didascalie | luogo e anno, mai la fonte delle foto del cliente | W4, W5 |
| 15 | Contenuto datato o con nome | almeno un elemento (fiera, evento, cantiere con anno, persona) | paragrafo 6 |
| 16 | Divieti del committente | tutti rispettati (viola, gradienti, emoji, Inter, bordo sinistro, vetro, tre box, badge, Lucide, shadcn, dissolvenza, fascio, sbiadimento, trattini lunghi, buzzword, corsivo serif) | T5, C1, K1, M1, D4 |

Regola d'insieme (da F6): un segnale isolato si può tenere se ha una ragione; due nella stessa schermata si correggono.
