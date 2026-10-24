# Censimento dei caratteri: industria e servizi

Gruppo: costruttori di macchine e attrezzature, materiali per edilizia ed esterni, forniture tecniche B2B, studi medici e dentistici, studi tecnici. Rilevazione del 6 ottobre 2026 su 30 siti di riferimento, 27 siti di confronto e 3’altri casi.

Come sono stati letti i caratteri: pagina aperta con Playwright a 1440 px, stili calcolati di tutti i nodi di testo (famiglia, peso, corpo, interlinea, spaziatura, maiuscolo), elenco di `document.fonts`, file .woff2 scaricati dalla pagina e lettura della tabella `name` di ogni file (famiglia, fonderia, disegnatore, copyright). Quando il nome nel CSS è un alias (per esempio "fontReplica", "Q-R", "midnight") il nome vero viene dal file. Le alternative gratuite sono state scelte misurando altezza x, altezza delle maiuscole e larghezza media dei file originali contro circa 130 famiglie candidate di Google Fonts, poi confrontando a vista le tavole di prova.

Dati completi: `censimento-industria-servizi.json` (stessa cartella). Screenshot, file CSS e tavole di confronto: `/tmp/claude-0/-home-user-danielnistorr/89486122-32ef-5f21-add5-5cbe6108c543/scratchpad/ricerca-caratteri/industria-servizi/` (cartelle `shots`, `shots2`, `confronti`).

## In breve

- Su 30 siti curati, 28 usano almeno un carattere commerciale (le eccezioni sono Arup con Spectral e Machina Labs con Roboto e Roboto Mono); nessuno usa Inter per i titoli. I caratteri dei titoli più ricorrenti sono grotesk neutre (Söhne, Atlas Grotesk, Suisse Int'l, Helvetica Now, Neue Montreal, Matter) e, nel medicale, serif da display (Nantes, GT Super, Heldane, Financier, Teodor).
- Il segnale più netto non è quale carattere, ma quale peso: 22 siti su 30 fanno i titoli grandi in peso 200-500 (ExtraLight, Light, Book, Regular, Medium). Nei siti di confronto prevalgono 600-900.
- Una sola famiglia basta: 16 siti di riferimento usano una famiglia (comprese le varianti mono o larghe dello stesso disegno), 12 ne usano due, McMaster-Carr tre; solo Ezra arriva a quattro ed è anche quello che usa il corsivo serif d’accento colorato.
- Il terzo carattere, quando c’è, ha un compito preciso: monospazio maiuscolo per menu, etichette, date e luoghi (Hadrian, Escofet, Machina Labs) oppure una larga per i nomi di prodotto (Formlabs, Hadrian).
- Il maiuscolo è quasi sempre piccolo (10-16 px) con spaziatura 0.05-0.1em, oppure in mono. Il maiuscolo grande compare in pochi casi e sempre con un carattere adatto: la larga Midnight Sans (Formlabs), il mono (Machina Labs), il serif SangBleu con spaziatura negativa (Laminam), la Frutiger spaziata come un logo (Lanserhof), il taglio solo maiuscole di Komax.
- Titoli grandi con interlinea tra 0.9 e 1.2 e spaziatura negativa da -0.02 a -0.05em (Hadrian, Q-Industrial, Formlabs, Parsley; Arup arriva a -0.07em). Eccezioni volute: sbp e Florim aprono la spaziatura anche nei titoli.
- Testo corrente quasi sempre tra 16 e 20 px con interlinea 1.5-1.8; i siti più calmi (Mutina, sbp, One Medical) stanno a 1.75-1.8, quelli da catalogo (Festool, McMaster-Carr) sotto 1.35.
- Le aziende venete e italiane del settore viste qui (Carel, Unox, Breton, Fiorentini, Dallan, Ideal Work, Margraf, Antolini, Salvagnini, IMA, Elesa, 41zero42) usano tutte caratteri gratuiti generici: Inter, Open Sans, Roboto, Lato, Montserrat, DM Sans, Noto Sans, Titillium. Bisazza affianca Bebas Neue a Gordita, Comau usa Helvetica Neue senza un sistema. Un carattere scelto con cura basta già a distinguersi sul territorio.
- Anche i premi recenti non garantiscono: INTECH (Awwwards 2025) usa Space Grotesk, OSE Engineering (Awwwards 2026) usa Geist + Space Mono, SkyClinics (Awwwards 2026) usa Satoshi. Sono i caratteri che oggi fanno "sito generato".
- Due siti premiati servono in produzione file di prova ("Matter TRIAL" su Q-Industrial, "TestFoundersGrotesk" su Palet): da non imitare, la licenza web va comprata.

## I 30 siti di riferimento

| # | Sito | Settore | Paese | Titoli | Testo | Terzo carattere e uso | Licenza | Riconoscimento |
|---|---|---|---|---|---|---|---|---|
| 1 | [WEIMA Maschinenbau](https://weima.com/) | macchine: trituratori, presse per bricchette e disidratazione | Germania | Okomito Medium 500 | Okomito Light 300 | nessuno | Okomito: commerciale | [Awwwards Site of the Day (sito di Studio Naam)](https://weima.com/us/amazing-news-amazing-feedback-site-of-the-day-and-developers-award/) |
| 2 | [Hadrian Automation](https://www.hadrian.co/) | fabbriche automatizzate di componenti di precisione (aerospazio, difesa) | USA | Söhne 400 (Buch) | Söhne 400 | Söhne Mono 400 e Söhne Breit 400: Mono maiuscolo 12-16px per menu, bottoni, orari delle sedi; Breit maiuscolo 16-18px per i titoletti di sezione | Söhne, Söhne Mono, Söhne Breit: commerciale | [nessun premio web verificato; scelto come sito curato di un produttore molto citato](https://www.hadrian.co/) |
| 3 | [Formlabs](https://formlabs.com/) | stampanti 3D professionali (SLA, SLS) | USA | Midnight Sans RD Pro 48 (larghezza espansa) maiuscolo, hero; Supreme 500 per i titoli di sezione | Supreme 400 | Midnight Sans: maiuscolo largo per hero, nomi prodotto (FUSE, X1) e testo dei bottoni | Supreme: gratuito su Fontshare (licenza ITF Free Font); Midnight Sans: commerciale | [leader di settore; nessun premio web verificato](https://formlabs.com/) |
| 4 | [Komax Group](https://www.komaxgroup.com/) | macchine per la lavorazione di cavi e cablaggi | Svizzera | Helvetica Now Display 700 | Helvetica Now Display 400 | Helvetica Neue LT Cut Bold: claim rotanti della hero 54-64px, un taglio solo maiuscole | Helvetica Now Display: commerciale; Helvetica Neue LT Cut: commerciale | [leader mondiale del settore cablaggi; nessun premio web verificato](https://www.komaxgroup.com/) |
| 5 | [Festool](https://www.festool.com/) | elettroutensili professionali | Germania | DIN (FF DIN di Albert-Jan Pool) 700 | DIN 400 | nessuno | DIN (file "DIN W02"): commerciale | [marchio di riferimento per artigiani; nessun premio web verificato](https://www.festool.com/) |
| 6 | [TRUMPF](https://www.trumpf.com/) | macchine utensili e laser per lamiera | Germania | Frutiger 45 Light | Frutiger 45 Light | Frutiger 65 Bold: nomi macchina, h3 e bottoni maiuscoli 12-13px | Frutiger: commerciale | [leader mondiale lavorazione lamiera; nessun premio web verificato](https://www.trumpf.com/) |
| 7 | [Machina Labs](https://machinalabs.ai/) | formatura robotizzata di lamiera (strutture metalliche) | USA | Roboto Mono 500 maiuscolo | Roboto 300-400 | Roboto Mono: menu con barra davanti (/CAPABILITIES), titoli di settore, citazioni | Roboto, Roboto Mono: open source, Google Fonts | [nessun premio web verificato; scelto per l’uso del monospazio](https://machinalabs.ai/) |
| 8 | [Weidmüller](https://www.weidmueller.com/) | connessioni elettriche, morsetti, utensili per cavi | Germania | carattere aziendale "weidmuellerCond" (grotesk condensata) 400 | carattere aziendale "weidmueller" 400 | nessuno | weidmueller / weidmuellerCond: proprietaria | [leader di settore (connettività industriale); nessun premio web verificato](https://www.weidmueller.com/) |
| 9 | [McMaster-Carr](https://www.mcmaster.com/) | forniture tecniche B2B (catalogo di oltre 400.000 componenti) | USA | Futura LT Pro Bold Condensed maiuscolo (menu e comandi) | Helvetica Neue eText Pro 400 e 700 | DIN Next LT Pro Medium: messaggi e intestazioni a 16px | Helvetica Neue eText, Futura LT, DIN Next: commerciale | [citato spesso come miglior sito di e-commerce industriale (caso studio IA Collaborative)](https://www.iacollaborative.com/results/mcmaster-carr) |
| 10 | [Q-Industrial](https://www.q-industrial.com/) | vernici e rivestimenti industriali | Germania e Ucraina (sito in inglese per la Germania e in ucraino) | Matter Light 300 | Matter Regular 400 | nessuno | Matter: commerciale; il sito serve file "Matter TRIAL" (versione di prova) | [Awwwards Site of the Day, 2 giugno 2024](https://www.awwwards.com/sites/q-industrial) |
| 11 | [Salvatori](https://www.salvatoriofficial.com/) | pietra naturale per rivestimenti, bagno, arredo | Italia | Atlas Grotesk Light 300 | Atlas Grotesk Light 300 e Regular 400 | Atlas Grotesk 500 maiuscolo: etichette 10px con spaziatura 1px (0.1em) | Atlas Grotesk: commerciale | [azienda premiata per il prodotto (Compasso d’Oro, menzione 2014); nessun premio web verificato](https://en.wikipedia.org/wiki/Salvatori_(design)) |
| 12 | [Dinesen](https://dinesen.com/) | pavimenti e rivestimenti in legno massiccio | Danimarca | Atlas Grotesk Light 300 | Atlas Grotesk Light 300 | nessuno | Atlas Grotesk: commerciale | [marchio di riferimento dei pavimenti in legno; nessun premio web verificato](https://dinesen.com/) |
| 13 | [Escofet (Molins)](https://www.escofet.com/) | arredo urbano e pavimentazioni in calcestruzzo prefabbricato | Spagna | Suisse Int'l Book e Light | Suisse Int'l Regular | Suisse Int'l Mono: menu maiuscolo, didascalie dei progetti (luogo, città, paese), date | Suisse Int'l, Suisse Int'l Mono: commerciale | [azienda storica del design urbano a Barcellona; nessun premio web verificato](https://www.escofet.com/) |
| 14 | [Rieder](https://www.rieder.cc/) | pannelli di facciata in calcestruzzo fibrorinforzato | Austria | PP Grafier Display 400 | Tomato Grotesk 400 | nessuno | PP Grafier: commerciale; Tomato Grotesk: commerciale | [nessun premio web verificato; scelto per l’accoppiata serif da display e grotesk](https://www.rieder.cc/) |
| 15 | [Mosa](https://mosa.com/) | piastrelle ceramiche | Paesi Bassi | TheSans 700 | TheSans 500 (Plain) | TheSerif: caricata, superfamiglia della sans (non visibile in prima schermata) | TheSans / TheSerif: commerciale | [marchio di riferimento per architetti; nessun premio web verificato](https://mosa.com/) |
| 16 | [Mutina](https://www.mutina.it/) | piastrelle e superfici ceramiche d’autore | Italia | Futura PT 400 | Futura PT 400 | Futura PT 700 maiuscolo: menu 15px e bottoni | Futura PT: commerciale / abbonamento Adobe | [marchio di design (collaborazioni con designer come Ronan Bouroullec); nessun premio web verificato](https://www.mutina.it/downloads/16088/1697/PR_Mutina_Ronan_Bouroullec_EN.pdf) |
| 17 | [Florim](https://www.florim.com/) | gres porcellanato e lastre ceramiche | Italia | PP Neue Montreal 400 | PP Neue Montreal 400 | nessuno | PP Neue Montreal: commerciale | [tra i maggiori produttori del distretto di Sassuolo; nessun premio web verificato](https://www.florim.com/) |
| 18 | [Laminam](https://www.laminam.com/) | lastre ceramiche di grande formato | Italia | SangBleu Empire 400 maiuscolo | Work Sans 400 | SangBleu Empire: numeri 01-05 del selettore e voci di menu a 24px | SangBleu Empire: commerciale; Work Sans: open source, Google Fonts | [nessun premio web verificato; scelto per l’uso del serif da display](https://www.laminam.com/) |
| 19 | [Tend](https://www.hellotend.com/) | studi dentistici | USA | Nantes 700 (e 400) | Founders Grotesk 400 | Founders Grotesk 600 maiuscolo: bottoni (BOOK NOW) con spaziatura 1.2px (0.08em) | Nantes: commerciale; Founders Grotesk: commerciale | [identità di marca premiata Red Dot; marca e spazi progettati con l’agenzia Mythology (mythology.com/project/tend)](https://www.red-dot.org/project/tend-49427) |
| 20 | [One Medical (Amazon)](https://www.onemedical.com/) | poliambulatori di medicina di base | USA | GT Super Display 500-600 (versione "One GT Super") | Ginto 200 | Ginto 600 maiuscolo: etichette 14px con spaziatura 1.4px (0.1em) | GT Super: commerciale (versione personalizzata); Ginto: commerciale | [nessun premio web verificato; marchio medicale tra i più curati negli USA](https://www.onemedical.com/) |
| 21 | [Ezra (Function Health)](https://ezra.com/) | centri di risonanza magnetica preventiva | USA | Financier Display Light 300 (con corsivo) | Inter 400 | F37 Beckett e FT Base: Beckett per sottotitoli e occhielli maiuscoli 12px, FT Base per paragrafi di componenti | Financier Display: commerciale; F37 Beckett: commerciale; FT Base: commerciale; Inter: open source | [nessun premio web verificato](https://ezra.com/) |
| 22 | [Lanserhof](https://lanserhof.com/) | centri medici di prevenzione e medicina integrata | Austria / Germania | Neue Frutiger World 450 maiuscolo + Frutiger Serif Light Italic | Neue Frutiger World 300 | Frutiger Serif LT Pro: corsivo per la prima riga della hero e i nomi dei programmi | Neue Frutiger World: commerciale; Frutiger Serif: commerciale | [nessun premio web verificato; marchio di riferimento della medicina preventiva di lusso](https://lanserhof.com/) |
| 23 | [Dębski Clinic](https://www.debskiclinic.pl/) | clinica privata multispecialistica | Polonia | Heldane Display Medium 500 | Basier Circle 400 | nessuno | Heldane Display: commerciale; Basier Circle: commerciale | [Awwwards Honorable Mention, 24 ottobre 2023 (studio Targa)](https://www.awwwards.com/sites/debski-clinic) |
| 24 | [Parsley Health](https://www.parsleyhealth.com/) | studi di medicina funzionale | USA | Teodor Light 300 | Euclid Circular B 400 | nessuno | Teodor: commerciale; Euclid Circular B: commerciale | [nessun premio web verificato](https://www.parsleyhealth.com/) |
| 25 | [schlaich bergermann partner (sbp)](https://www.sbp.de/) | ingegneria strutturale | Germania | FF Mark ExtraLight 200 | FF Mark 200-400 | nessuno | FF Mark: commerciale | [studio di ingegneria strutturale tra i più noti al mondo; nessun premio web verificato](https://www.sbp.de/) |
| 26 | [Eckersley O'Callaghan](https://www.eocengineers.com/) | ingegneria strutturale e facciate in vetro | Regno Unito | New Rail Alphabet Bold | New Rail Alphabet Light | nessuno | New Rail Alphabet: commerciale | [nessun premio web verificato; studio noto per le strutture in vetro](https://www.eocengineers.com/) |
| 27 | [Werner Sobek](https://www.wernersobek.com/) | ingegneria strutturale, facciate, sostenibilità | Germania | Futura T Demi | Futura T Book | nessuno | Futura T: commerciale | [nessun premio web verificato; studio di ingegneria di fama internazionale](https://www.wernersobek.com/) |
| 28 | [Arup](https://www.arup.com/) | ingegneria multidisciplinare | Regno Unito | Spectral 400 | Arial 400 | nessuno | Spectral: open source, Google Fonts; Arial: di sistema | [nessun premio web verificato; tra i maggiori studi di ingegneria al mondo](https://www.arup.com/) |
| 29 | [Webb Yates Engineers](https://webbyates.com/) | ingegneria strutturale, civile e impianti | Regno Unito | Larken 400 | Geograph 400 | Geograph Bold: nomi dei progetti nelle didascalie | Larken: commerciale / abbonamento Adobe; Geograph: commerciale | [nessun premio web verificato](https://webbyates.com/) |
| 30 | [EFLA Consulting Engineers](https://www.efla-engineers.com/) | ingegneria e consulenza tecnica | Islanda | Replica Bold 700 | Replica Regular 400 | Domaine Text 400: titoletti di sezione e testi di servizio 15-20px | Replica: commerciale; Domaine Text: commerciale | [Awwwards Honorable Mention, 19 gennaio 2024 (studio Hugsmidjan)](https://www.awwwards.com/sites/efla-engineers) |

### Come lo usano (scala, interlinea, maiuscolo, numeri)

| Sito | Pesi | Scala dei titoli | Testo | Maiuscolo e spaziatura | Numeri | Famiglie | Dove il carattere fa la differenza |
|---|---|---|---|---|---|---|---|
| WEIMA Maschinenbau | 300, 400, 500, 600, 700 | parole chiave della hero a 130px, interlinea 0.95, spaziatura -2px (circa -0.015em); h1 65px/1.1; h2 21px | testo 16px/24px (1.5) con spaziatura +0.2px su tutto il sito | nessun maiuscolo: gerarchia solo con dimensione e peso | nessun trattamento particolare | 1 | una sola famiglia; il testo in Light con tracking leggermente aperto rende il tono tecnico ma non freddo; titoli enormi in Medium, mai in Bold |
| Hadrian Automation | 400 in pagina (caricati anche 500 Kräftig e 600 Halbfett) | h1 72px con interlinea 1.0 e spaziatura -2.16px (-0.03em); 64px e 36px con lo stesso rapporto; sottotitolo 20px | titoli a 1.0, testo 20px/21.4px | maiuscolo solo nel mono e nella versione larga, a spaziatura normale perché il mono è già aperto | orari e dati in Söhne Mono | 1 | tre larghezze dello stesso disegno (normale, larga, mono) e un solo peso: il sistema sembra un catalogo tecnico; bottoni a filo con testo mono |
| Formlabs | Supreme 400, 500, 600 (+ corsivo); Midnight 400-600 | hero 48px/56px maiuscolo; titoli di sezione 32px/38.4px con spaziatura -1.28px (-0.04em); card 20-24px | testo 14-16px con interlinea 1.5-1.6 | maiuscolo solo nel carattere largo, che regge il maiuscolo senza spaziatura aggiunta; etichette Supreme 14px a +1.4px (0.1em) | nomi prodotto con cifre (X1, Form 4) nel carattere largo | 2 | una grotesk da lavoro per tutto e un carattere largo riservato ai nomi di prodotto: il largo fa da marchio senza invadere il testo |
| Komax Group | 400, 500, 700 | h1 96px con interlinea 1.0; claim 64px/72px; titoli card 16-20px bold | testo 16-18px su 24-28px | maiuscolo pesante senza spaziatura, ritagliato dentro forme oblique | nessun trattamento | 1 | la versione Display di Helvetica Now (spaziatura stretta di fabbrica) dà ai titoli un aspetto più denso del solito Helvetica/Arial |
| Festool | 400, 500, 700 | titolo principale 43px/52.8px bold; sottotitoli 26px/39px 500 | testo 18px/24px (1.33): stretto, da catalogo | nessun maiuscolo | cifre DIN, già tecniche di loro | 1 | DIN porta con sé il mondo delle targhe e delle norme tecniche: basta lei, senza decorazioni |
| TRUMPF | 45 Light, 55 Roman, 65 Bold | h1 e h2 34px/47.6px in Light: i titoli non sono mai grassetti | testo 18px/28.8px (1.6) | Bold maiuscolo piccolo per i comandi, quasi senza spaziatura | nessun trattamento | 1 | titoli in Light e nomi prodotto in Bold: il contrasto di peso fa tutta la gerarchia |
| Machina Labs | Roboto 300, 400, 700; Roboto Mono 300-700 | h1 72px/82px maiuscolo mono; h2 36px/44px mono minuscolo | testo 18-20px su 28-31px (1.55) | mono maiuscolo senza spaziatura aggiunta (il mono è già largo) | timecode video e dati in mono | 2 | il mono usato come voce da titolo dà l’aria di specifica tecnica; il testo resta in Roboto leggero |
| Weidmüller | 400, 600, 700 | h1 64px/70.4px condensato a peso normale; h2 48px; titoli card 18-24px bold condensato | testo 18px/27px (1.5) | condensato maiuscolo senza spaziatura per CTA | nessun trattamento | 1 | titoli condensati a peso normale (non bold): molto testo in poco spazio, tono da scheda tecnica |
| McMaster-Carr | Helvetica 400, 500, 700 | nessun titolo grande: tutto tra 11 e 16px | 11-13px su 14-17px: densissimo, da catalogo cartaceo | Futura Bold Condensed maiuscola per i comandi principali (ORDER, BROWSE CATALOG) | Helvetica eText, pensata per schermo a corpo piccolo | 3 | il carattere lavora a corpo piccolo: eText è disegnata per leggibilità su schermo, il condensato separa i comandi dal catalogo |
| Q-Industrial | 300, 400, 500 | h1 80px con interlinea 0.9 e spaziatura -4px (-0.05em); h2 85px; h3 55px a -0.04em | testo 12-21px a interlinea 1.0-1.2, molto compatto | nessun maiuscolo; menu in pillole con bordo | nessun trattamento | 1 | titoli enormi in Light con spaziatura molto negativa: il peso leggero e la stretta fanno sembrare il testo un logo |
| Salvatori | 100, 300, 400, 500, 700 | h1 64px/74px (1.16) in Light; sottotitolo 24px/34px Light | testo 14-16px su 18-25px | maiuscolo 10px a 0.1em per le etichette | nessun trattamento | 1 | grotesk dalle maiuscole alte (altezza H 0.765) usata leggera: titoli grandi ma sottili, molta aria |
| Dinesen | 300 (titoli e testo), 700 per i comandi | h1 64px/73.6px in Light; sottotitolo 25px/36px | testo 15px, interlinea normale | bottoni bold maiuscoli 15px | nessun trattamento | 1 | un solo peso leggero per quasi tutto: il sito lascia parlare le fotografie del legno |
| Escofet (Molins) | Light, Regular, Book, Medium | titoli di sezione 38-40px maiuscolo Book; frasi 45-55px Light | testo 16px/20px; mono 14px/21px | maiuscolo con spaziatura leggermente negativa (-0.176px), insolito e compatto | date e luoghi in mono | 1 | tutto il sistema di navigazione in mono maiuscolo grigio: sembra la targhetta di un elemento prefabbricato; logo in gotico come unico ornamento |
| Rieder | Grafier 400; Tomato 400, 700 | titolo hero 96.6px/101px (1.05) in basso a sinistra sulla foto; h2 40px/48px | testo 16-24px su 19-33px | quasi assente | nessun trattamento | 2 | un serif da display ad alto contrasto, grandissimo e leggero, contro facciate fotografate: il materiale grezzo e il titolo elegante si equilibrano |
| Mosa | 400, 500, 700 | h1 72px/79px bold; h3 57.6px; sottotitoli 33.6px regular | testo 16px/25.9px (1.62) | nessuno | impostano font-variant-numeric: lining-nums perché TheSans ha cifre minuscole di default | 1 | umanista con superfamiglia serif: calda ma tecnica; la cura delle cifre è un dettaglio da tipografi |
| Mutina | 400, 500, 600, 700 | titoli 58px/69.6px a peso normale, mai bold | testo 17.6px/32px (1.8): molto arioso | menu Futura Bold maiuscola 15px senza spaziatura aggiunta | date in Futura (22.09.26) | 1 | Futura usata a peso normale nei titoli e bold solo nel menu; interlinea molto ampia nel testo; logo in serif classico |
| Florim | 400, 500, 700 | h1 60px/64px (1.07); titoli secondari 28-34px | testo 14-16px a 1.5 | maiuscolo 500 a 14px con spaziatura +0.01em | nessun trattamento | 1 | spaziatura positiva +0.01em applicata ovunque, anche ai titoli: il contrario dell’abitudine di stringere |
| Laminam | SangBleu 400-600; Work Sans 400, 600, 700 | nomi collezione 96px/105.6px maiuscolo con spaziatura -3.84px (-0.04em) | testo 14-16px a 1.5 | maiuscolo serif grande con spaziatura negativa: raro e riconoscibile | numeri di slide in serif dentro pillole fotografiche | 2 | il serif è riservato ai nomi delle collezioni, come su un catalogo di moda; il testo resta una sans gratuita |
| Tend | Nantes 400, 700; Founders 300-600 | h1 63px/75px (1.19) centrato; h2 48px/62px; frase 33px con alcune parole in Bold nella stessa riga | testo 17px/24.65px con spaziatura +0.17px | bottoni maiuscoli a 0.08em | telefono nel bottone in Founders | 2 | l’accento sulle parole si fa con il grassetto dello stesso serif, non con un corsivo; colore verde salvia sul serif |
| One Medical (Amazon) | GT Super 500, 600; Ginto 200, 300, 600, 700 | h1 72px/72px (1.0); h2 88px/94px; titoli card 50px/53.5px | testo 18px/31.5px (1.75) in peso 200 | etichette 600 a 0.1em | prezzo in Ginto bold dentro il testo | 2 | serif da display pesante e caldo per i titoli, sans geometrica sottilissima per il testo con interlinea alta |
| Ezra (Function Health) | Financier 300; Inter 400-700; Beckett 400, 600 | h1 88px/88px (1.0) con spaziatura -0.88px (-0.01em) | testo 16-18px/25.6-28.8px (1.6) | occhielli piccoli maiuscoli in Beckett | prezzo nel testo in Inter | 4 | bel serif da titolo, ma quattro famiglie e il corsivo d’accento colorato: è lo schema che i generatori copiano |
| Lanserhof | 300, 400, 450, 500, 700, 800 | hero 69px maiuscolo + 60px corsivo; titoli card 20px Black | testo 16-18px su 24-28px con spaziatura +0.2px | maiuscolo grande e spaziato nella hero, come un logo | nessun trattamento | 2 | sans e serif della stessa superfamiglia Frutiger: il corsivo funziona perché è parente della sans, non un carattere preso a caso |
| Dębski Clinic | Heldane 500; Basier 400, 500, 700 | hero 95px/104.7px (1.1) su tre righe sfalsate; h1 63px; h3 47.6px | testo 19.8px/29.7px (1.5) con spaziatura -0.04em | nessuno | recensioni (892+) in Basier | 2 | serif rinascimentale a peso medio, grande, con righe a rientri diversi: composizione da manifesto, non da template |
| Parsley Health | Teodor 300; Euclid 300-700 | h1 64px/71.7px (1.12) con spaziatura -1.28px (-0.02em); h2 48px; h3 38px | testo 18px/27px (1.5) | nessuno | nel menu impostano lining-nums e tabular-nums | 2 | serif sottile da display per i titoli, sans geometrica per tutto il resto; nessun corsivo d’accento |
| schlaich bergermann partner (sbp) | 200, 300, 400, 500, 600 | hero 110px/132px in ExtraLight; h1 67px/80px con spaziatura +1px | testo 19px/34px (1.8) con spaziatura +0.5px | date in maiuscolo 500 12px | date in maiuscolo 500 | 1 | geometrica in peso ExtraLight a 110px: elegante come un disegno strutturale; tracking positivo anche nei titoli. Sito fatto con WordPress ed Elementor |
| Eckersley O'Callaghan | Light e Bold | titolo 34px/36px (1.06) bold | testo 14-20px su 17-25px | nessuno | nessun trattamento | 1 | il carattere della segnaletica ferroviaria britannica in soli due pesi: identità locale e tecnica senza effetti |
| Werner Sobek | Book e Demi | h1 48px/55.7px (1.16) Demi; testo introduttivo 42px/50px Book | testo 16-28px | nessuno | nessun trattamento | 1 | testo introduttivo grandissimo (42px) in Book: la frase d’apertura fa da titolo |
| Arup | Spectral 400; Arial 400 | h1 68px/74.8px con spaziatura -4.76px (-0.07em, molto stretta); domande 28-50px | testo 16-20px a 1.3-1.4 | nessuno | nessun trattamento | 2 | serif da lettura usato grande e stretto per titoli che sono domande; il resto è Arial di sistema, scelta voluta di neutralità |
| Webb Yates Engineers | Larken 400; Geograph 400, 500, 700 | frase d’apertura 49px/62px (1.27) centrata sulla foto; voci di menu 37px in Larken | testo 17px/23px | nessuno | nessun trattamento | 2 | un serif morbido per la dichiarazione e per il menu, una geometrica sobria per le didascalie: lo studio tecnico parla come un editore |
| EFLA Consulting Engineers | Replica 400, 700; Domaine 400 | h2 94px/103.4px (1.1) bold; h3 32px | testo 21-27px su 31-35px (1.3-1.5) | nessuno | impostano tabular-nums su tutto | 2 | grotesk con angoli tagliati (Replica) usata grande; un serif da testo come voce secondaria |

## Cosa ricorre per settore

**Macchine e attrezzature** (WEIMA, Hadrian, Formlabs, Komax, Festool, TRUMPF, Machina Labs, Weidmüller). Grotesk neutre o tecniche, spesso storiche e con licenza: Helvetica Now, Frutiger, DIN, Söhne. Il tono tecnico arriva da tre strumenti: un monospazio per etichette, orari e menu (Hadrian, Machina Labs); una versione larga o condensata per nomi di prodotto e comandi (Formlabs, Hadrian, Weidmüller, McMaster-Carr); titoli in peso normale o leggero, non in nero (TRUMPF Light, Hadrian 400, WEIMA 500). Nessuno usa serif.

**Forniture tecniche B2B** (McMaster-Carr, Q-Industrial). Due estremi: McMaster-Carr lavora tutto a 11-16 px con tre famiglie Linotype (Helvetica eText per leggere, Futura condensata per i comandi, DIN Next per i messaggi); Q-Industrial fa il contrario, una sola geometrica (Matter) in Light a 80 px con spaziatura -0.05em.

**Materiali per edilizia ed esterni** (Salvatori, Dinesen, Escofet, Rieder, Mosa, Mutina, Florim, Laminam). Due famiglie di scelte. La prima: una grotesk raffinata in peso leggero per tutto (Atlas Grotesk per Salvatori e Dinesen, Neue Montreal per Florim, Suisse per Escofet, Futura PT per Mutina, TheSans per Mosa). La seconda: un serif da display riservato ai nomi delle collezioni o alla frase della hero, con una sans per il resto (SangBleu + Work Sans per Laminam, Grafier + Tomato Grotesk per Rieder). Il serif non si usa mai per il testo.

**Studi medici e dentistici** (Tend, One Medical, Ezra, Lanserhof, Dębski Clinic, Parsley Health). Qui ricorre sempre la stessa struttura: serif da display per i titoli e sans geometrica o grotesk per il testo (Nantes + Founders Grotesk, GT Super + Ginto, Heldane + Basier Circle, Teodor + Euclid, Financier + Inter, Frutiger Serif + Neue Frutiger). E la stessa struttura che i generatori ripetono con Playfair, Fraunces o Instrument Serif + Inter: quello che separa i siti veri è la scelta del serif (mai Playfair o Cormorant), il peso (Tend usa il grassetto per l’accento, Dębski il Medium, Parsley il Light) e la composizione (righe sfalsate da manifesto in Dębski). Ezra e Lanserhof usano il corsivo serif d’accento: in Lanserhof funziona perché il corsivo è della stessa superfamiglia della sans; in Ezra e in Dentologie (tra i siti di confronto) è lo stampo che il committente vieta.

**Studi tecnici e di ingegneria** (sbp, Eckersley O'Callaghan, Werner Sobek, Arup, Webb Yates, EFLA). Geometriche classiche (FF Mark, Futura T), un grotesk di segnaletica (New Rail Alphabet), e in tre casi un serif per la frase d’apertura (Spectral per Arup, Larken per Webb Yates, Domaine come voce secondaria per EFLA). sbp è costruito con WordPress ed Elementor e carica un carattere commerciale self-hosted: la stessa piattaforma che usiamo noi.

## Cosa distingue i siti migliori

- **Peso dei titoli.** Titoli grandi in 200-500: sbp (ExtraLight 200 a 110 px), Q-Industrial (Light 300 a 80 px), Salvatori e Dinesen (Light 300 a 64 px), TRUMPF (Light), Parsley (Light), Hadrian (400), Mutina (400), Florim (400), Rieder (400), WEIMA (500), Dębski (500). I siti generici fanno l’opposto: Unox Montserrat 900, Holcim Black, Coffman Rubik 900 corsivo, IMA e Vention Inter 600.
- **Interlinea dei titoli vicina a 1.** Hadrian 1.0, One Medical 1.0, Komax 1.0, Ezra 1.0, Q-Industrial 0.9, WEIMA 0.95, Rieder 1.05, Florim 1.07. Il caso contrario è IMA: titoli a 50 px con interlinea 1.5, come fossero paragrafi.
- **Spaziatura calibrata, non di default.** Negativa sui titoli grandi (-0.02/-0.05em), positiva sul testo piccolo e sulle etichette (+0.01em Florim e Tend, +0.1em per le etichette maiuscole di Salvatori e One Medical).
- **Un compito per ogni carattere.** Quando ci sono due o tre famiglie, ognuna ha un lavoro: Laminam usa il serif solo per i nomi delle collezioni, Escofet il mono solo per navigazione e didascalie, Formlabs la larga solo per prodotti e bottoni.
- **Cura dei numeri.** Mosa forza le cifre maiuscole (TheSans ha cifre minuscole di default), EFLA imposta le cifre tabellari su tutto, Parsley usa cifre allineate e tabellari nel menu, Hadrian mette gli orari in mono.
- **Accento senza corsivo.** Tend mette in grassetto alcune parole dentro una frase in regular dello stesso serif; Dębski sposta le righe del titolo; WEIMA alterna Medium e Regular. Il corsivo serif colorato compare solo in Ezra e Lanserhof (e, tra i confronti, in Dentologie).
- **Pochi effetti tipografici.** Nelle 18 prime schermate guardate una per una non ci sono testi in gradiente né emoji nei titoli; l’unica etichetta sopra un titolo è il nome prodotto FUSE X1 di Formlabs, che è un logo di prodotto. La personalità viene dal disegno del carattere e dalla misura.

## Accoppiate ricorrenti

| Schema | Esempi reali | Equivalente libero proposto |
|---|---|---|
| Una grotesk sola in 2-3 pesi, titoli leggeri | Atlas Grotesk (Salvatori, Dinesen), Neue Montreal (Florim), Okomito (WEIMA), Matter (Q-Industrial), FF Mark (sbp), Frutiger (TRUMPF), DIN (Festool) | Libre Franklin o Public Sans; Instrument Sans; Hanken Grotesk; Figtree; Kumbh Sans; Hind; Barlow |
| Grotesk + monospazio della stessa famiglia per etichette e menu | Söhne + Söhne Mono (Hadrian), Suisse Int'l + Suisse Mono (Escofet), Roboto + Roboto Mono (Machina Labs) | Schibsted Grotesk + Fragment Mono; Archivo + Chivo Mono |
| Grotesk + versione larga per nomi prodotto | Söhne + Söhne Breit (Hadrian), Supreme + Midnight Sans (Formlabs) | Archivo a larghezza 100 e 125 (una sola famiglia); Chivo + Unbounded |
| Serif da display per titoli + sans geometrica per testo (medicale) | Nantes + Founders Grotesk (Tend), GT Super + Ginto (One Medical), Heldane + Basier (Dębski), Teodor + Euclid (Parsley) | Newsreader + Schibsted Grotesk; Gloock + Figtree; EB Garamond + Albert Sans; Libre Caslon Display + Figtree |
| Serif da display solo per nomi o frase della hero + sans di servizio (materiali, studi) | SangBleu + Work Sans (Laminam), Grafier + Tomato (Rieder), Larken + Geograph (Webb Yates), Spectral + Arial (Arup) | Noto Serif Display + Work Sans; Prata + Golos Text; Gelasio + Albert Sans; Spectral + un carattere di sistema |
| Superfamiglia sans + serif | TheSans + TheSerif (Mosa), Neue Frutiger + Frutiger Serif (Lanserhof) | Source Sans 3 + Source Serif 4 |

## Alternative libere su Google Fonts

Per ogni carattere commerciale le 1-2 alternative più vicine. "Rischio IA" segnala i caratteri della lista abusata (Inter e famiglia, Poppins, Montserrat, Playfair Display, Space Grotesk, DM Sans, Manrope, Plus Jakarta Sans, Outfit, Sora, Cormorant, Fraunces, Instrument Serif, IBM Plex Mono, JetBrains Mono) o di moda negli ultimi due anni.

| Commerciale (sito) | Alternativa | Perché | Cosa si perde | Rischio IA |
|---|---|---|---|---|
| Okomito (WEIMA Maschinenbau) | [Hanken Grotesk](https://fonts.google.com/specimen/Hanken+Grotesk) | stesso disegnatore (Alfredo Marco Pradil); altezza x 0.49 contro 0.51, stessi terminali piatti | Hanken è più largo e spaziato: stringere a -0.01em; mancano le alternative di Okomito | no |
| Okomito (WEIMA Maschinenbau) | [Funnel Sans](https://fonts.google.com/specimen/Funnel+Sans) | proporzioni misurate quasi uguali (x 0.50, maiuscole 0.68) | forme un po’ più morbide | no |
| Söhne (Hadrian Automation) | [Schibsted Grotesk](https://fonts.google.com/specimen/Schibsted+Grotesk) | grotesk con sperone sulla G come Söhne; altezza x 0.527 contro 0.523 | un po’ più largo; meno finezza nella spaziatura dei titoli | no |
| Söhne + Söhne Breit (Hadrian Automation) | [Archivo](https://fonts.google.com/specimen/Archivo) | ha l’asse di larghezza: a wdth 100 per i titoli e a 125 per le etichette larghe, una sola famiglia come Söhne | il tono è più da quotidiano, meno svizzero | no |
| Söhne Breit (Hadrian Automation) | [Mona Sans](https://fonts.google.com/specimen/Mona+Sans) | a larghezza 125 è la più vicina alla Breit nel confronto visivo | nata per GitHub: si vede su siti di software | no |
| Söhne Mono (Hadrian Automation) | [Fragment Mono](https://fonts.google.com/specimen/Fragment+Mono) | monospazio costruito su una grotesk neutra, altezza x 0.524 come Söhne Mono | meno pesi | no |
| Midnight Sans (Formlabs) | [Unbounded](https://fonts.google.com/specimen/Unbounded) | larga e geometrica, a peso 500 il colore è quasi identico | Unbounded è più tonda e più giocosa | no |
| Midnight Sans (Formlabs) | [Mona Sans](https://fonts.google.com/specimen/Mona+Sans) | a larghezza 125 e peso 600 ha la stessa compattezza verticale | meno estesa della Midnight 48 | no |
| Supreme (Formlabs) | [Chivo](https://fonts.google.com/specimen/Chivo) | grotesk compatta con proporzioni simili (x 0.51) | Supreme si può usare gratis da Fontshare con un link CSS: l’alternativa serve solo se si vuole restare su Google Fonts | no |
| Helvetica Now Display (Komax Group) | [Instrument Sans](https://fonts.google.com/specimen/Instrument+Sans) | neo-grotesk con terminali orizzontali e proporzioni vicine (x 0.51) | meno pesi ottici; il nome è lo stesso di Instrument Serif, che però non c’entra | no |
| Helvetica Now Display (Komax Group) | [Inter Tight](https://fonts.google.com/specimen/Inter+Tight) | nel confronto visivo è la più vicina | è la famiglia Inter: la tipografia più riconoscibile dei siti generati | sì |
| DIN (Festool) | [Barlow](https://fonts.google.com/specimen/Barlow) | ispirata alle targhe e alla segnaletica, altezza x 0.506 contro 0.492, larghezza simile | angoli leggermente arrotondati, meno rigida | no |
| DIN (Festool) | [Sofia Sans](https://fonts.google.com/specimen/Sofia+Sans) | impianto DIN con più calore, ha anche Condensed e Semi Condensed | più umanista | no |
| Frutiger (TRUMPF) | [Hind](https://fonts.google.com/specimen/Hind) | disegno di impronta Frutiger; altezza x 0.508 contro 0.510 | Hind è più stretta; poche varianti | no |
| Frutiger (TRUMPF) | [Source Sans 3](https://fonts.google.com/specimen/Source+Sans+3) | umanista aperta con molti pesi e corsivi | più stretta e più fredda | no |
| Roboto Mono (Machina Labs) | [Chivo Mono](https://fonts.google.com/specimen/Chivo+Mono) | mono con più carattere a pari ingombro | Roboto Mono è già gratuito; Chivo Mono è meno visto | no |
| weidmuellerCond (Weidmüller) | [Archivo Narrow](https://fonts.google.com/specimen/Archivo+Narrow) | grotesk stretta con lo stesso ingombro | disegno meno personale | no |
| weidmuellerCond (Weidmüller) | [Roboto Condensed](https://fonts.google.com/specimen/Roboto+Condensed) | ampia gamma di pesi, legge bene a 16px nel menu | molto diffusa nei temi WordPress | no |
| Helvetica Neue eText (McMaster-Carr) | [Arimo](https://fonts.google.com/specimen/Arimo) | stessa larghezza e altezza x grande di Helvetica/Arial | Arimo è un Arial: perde la G e la R di Helvetica | no |
| Futura Bold Condensed (McMaster-Carr) | [Barlow Condensed](https://fonts.google.com/specimen/Barlow+Condensed) | condensato geometrico-tecnico a peso 600 | meno contrasto tra tondi e aste | no |
| DIN Next (McMaster-Carr) | [Barlow](https://fonts.google.com/specimen/Barlow) | impianto DIN | angoli più morbidi | no |
| Matter (Q-Industrial) | [Figtree](https://fonts.google.com/specimen/Figtree) | geometrico-grotesk con altezza x 0.50 come Matter | meno contrasto nelle curve | no |
| Matter (Q-Industrial) | [Albert Sans](https://fonts.google.com/specimen/Albert+Sans) | stessa famiglia di forme, pesi da 100 a 900 | un po’ più larga | no |
| Matter (Q-Industrial) | [DM Sans](https://fonts.google.com/specimen/DM+Sans) | nel confronto visivo è la più vicina | una delle sans più usate dai siti generati | sì |
| Atlas Grotesk (Salvatori) | [Libre Franklin](https://fonts.google.com/specimen/Libre+Franklin) | è la gratuita con le maiuscole più alte (0.742) e la stessa altezza x (0.53) | disegno americano, meno svizzero | no |
| Atlas Grotesk (Salvatori) | [Public Sans](https://fonts.google.com/specimen/Public+Sans) | stessa impostazione, maiuscole alte, molti pesi leggeri | più istituzionale (nata per il governo USA) | no |
| Atlas Grotesk (Dinesen) | [Libre Franklin](https://fonts.google.com/specimen/Libre+Franklin) | maiuscole alte e altezza x uguale | meno raffinata nei pesi leggeri | no |
| Atlas Grotesk (Dinesen) | [Public Sans](https://fonts.google.com/specimen/Public+Sans) | ha Thin ed ExtraLight per titoli sottili | tono più neutro | no |
| Suisse Int'l (Escofet (Molins)) | [Schibsted Grotesk](https://fonts.google.com/specimen/Schibsted+Grotesk) | ritmo e altezza x vicini (0.527 contro 0.538) | meno pesi intermedi (Book) | no |
| Suisse Int'l Mono (Escofet (Molins)) | [Fragment Mono](https://fonts.google.com/specimen/Fragment+Mono) | mono su base grotesk neutra, la più vicina nel confronto visivo | un solo peso | no |
| Suisse Int'l (Escofet (Molins)) | [Inter](https://fonts.google.com/specimen/Inter) | nel confronto visivo è quasi identica | è il carattere che il committente vieta | sì |
| PP Grafier (Rieder) | [Prata](https://fonts.google.com/specimen/Prata) | alto contrasto e grazie a cuneo, la più vicina tra le gratuite | Grafier ha dettagli più eccentrici | no |
| PP Grafier (Rieder) | [Gilda Display](https://fonts.google.com/specimen/Gilda+Display) | leggero e alto contrasto | più classico | no |
| Tomato Grotesk (Rieder) | [Golos Text](https://fonts.google.com/specimen/Golos+Text) | grotesk morbida con proporzioni simili | perde le stranezze di Tomato (Q, y) | no |
| Tomato Grotesk (Rieder) | [Bricolage Grotesque](https://fonts.google.com/specimen/Bricolage+Grotesque) | ha le stesse irregolarità volute | molto di moda nel 2024-2025, rischia di sembrare già visto | sì |
| TheSans + TheSerif (Mosa) | [Source Sans 3](https://fonts.google.com/specimen/Source+Sans+3) | umanista aperta; con Source Serif 4 forma una superfamiglia come TheSans/TheSerif | meno personalità nelle curve | no |
| TheSans (Mosa) | [Fira Sans](https://fonts.google.com/specimen/Fira+Sans) | umanista con cifre e pesi completi, larghezza simile | tono più da interfaccia (nata per Firefox OS) | no |
| Futura PT (Mutina) | [Jost](https://fonts.google.com/specimen/Jost) | ispirata a Futura, stesse a e g a un piano, maiuscole geometriche | altezza x più alta (0.46 contro 0.42) | no |
| Futura PT (bold) (Mutina) | [League Spartan](https://fonts.google.com/specimen/League+Spartan) | per menu e titoli pesanti | nei pesi leggeri è diversa | no |
| PP Neue Montreal (Florim) | [Instrument Sans](https://fonts.google.com/specimen/Instrument+Sans) | neo-grotesk stretta e pulita, vicina nel confronto visivo | meno pesi sottili | no |
| PP Neue Montreal (Florim) | [Schibsted Grotesk](https://fonts.google.com/specimen/Schibsted+Grotesk) | stesse proporzioni di base | più larga di Montreal | no |
| PP Neue Montreal (Florim) | [Inter Tight](https://fonts.google.com/specimen/Inter+Tight) | la più vicina a vista | famiglia Inter | sì |
| SangBleu Empire (Laminam) | [Noto Serif Display](https://fonts.google.com/specimen/Noto+Serif+Display) | alto contrasto e grazie affilate, ottima in maiuscolo grande | meno tagliente | no |
| SangBleu Empire (Laminam) | [Bodoni Moda](https://fonts.google.com/specimen/Bodoni+Moda) | contrasto forte, adatto a nomi brevi | più didone e più classica | no |
| SangBleu Empire (Laminam) | [Playfair Display](https://fonts.google.com/specimen/Playfair+Display) | vicina a vista | tra i serif più abusati | sì |
| Nantes (Tend) | [Newsreader](https://fonts.google.com/specimen/Newsreader) | serif contemporaneo con dettagli taglienti e asse ottico | Nantes ha più personalità nelle grazie | no |
| Nantes (Tend) | [Petrona](https://fonts.google.com/specimen/Petrona) | serif con le stesse irregolarità misurate | meno pesi pesanti | no |
| Founders Grotesk (Tend) | [Schibsted Grotesk](https://fonts.google.com/specimen/Schibsted+Grotesk) | grotesk di impianto ottocentesco | Founders ha l’altezza x molto bassa (0.437): nessuna gratuita la imita bene | no |
| GT Super Display (One Medical (Amazon)) | [Gloock](https://fonts.google.com/specimen/Gloock) | alto contrasto e grazie a cuneo, molto vicina a vista | meno pesi (solo regular) | no |
| GT Super Display (One Medical (Amazon)) | [DM Serif Display](https://fonts.google.com/specimen/DM+Serif+Display) | stesso colore pesante | più stretta | no |
| Ginto (One Medical (Amazon)) | [Figtree](https://fonts.google.com/specimen/Figtree) | geometrica con proporzioni misurate quasi identiche (x 0.50, larghezza 0.51) | meno personalità nella a e nella g | no |
| Financier Display (Ezra (Function Health)) | [Libre Caslon Display](https://fonts.google.com/specimen/Libre+Caslon+Display) | stessa altezza x piccola e contrasto alto, la più vicina a vista | un solo peso | no |
| Financier Display (Ezra (Function Health)) | [Newsreader](https://fonts.google.com/specimen/Newsreader) | a corpo grande e peso 300 ha lo stesso colore | più larga | no |
| Neue Frutiger World (Lanserhof) | [Hind](https://fonts.google.com/specimen/Hind) | impronta Frutiger, altezza x 0.508 contro 0.510 | meno pesi | no |
| Frutiger Serif + Neue Frutiger (Lanserhof) | [Source Serif 4](https://fonts.google.com/specimen/Source+Serif+4) | con Source Sans 3 si ricostruisce una superfamiglia sans e serif | tono più editoriale | no |
| Heldane Display (Dębski Clinic) | [EB Garamond](https://fonts.google.com/specimen/EB+Garamond) | stesse radici rinascimentali, altezza x bassa | più storica e meno nitida; usare 500-600 | no |
| Heldane Display (Dębski Clinic) | [Crimson Pro](https://fonts.google.com/specimen/Crimson+Pro) | garalde con buoni pesi medi | più da testo che da display | no |
| Heldane Display (Dębski Clinic) | [Cormorant Garamond](https://fonts.google.com/specimen/Cormorant+Garamond) | simile a vista | tra i serif più abusati | sì |
| Basier Circle (Dębski Clinic) | [Albert Sans](https://fonts.google.com/specimen/Albert+Sans) | geometrica con proporzioni vicine (x 0.50) | meno compatta | no |
| Teodor (Parsley Health) | [Libre Caslon Display](https://fonts.google.com/specimen/Libre+Caslon+Display) | serif da display leggero con altezza x bassa | più classico | no |
| Teodor (Parsley Health) | [Newsreader](https://fonts.google.com/specimen/Newsreader) | a peso 300 e grande corpo ha un colore simile | più largo | no |
| Euclid Circular B (Parsley Health) | [Figtree](https://fonts.google.com/specimen/Figtree) | geometrica vicina per proporzioni | meno caratterizzata | no |
| Euclid Circular B (Parsley Health) | [Plus Jakarta Sans](https://fonts.google.com/specimen/Plus+Jakarta+Sans) | simile a vista | abusata | sì |
| FF Mark (schlaich bergermann partner (sbp)) | [Kumbh Sans](https://fonts.google.com/specimen/Kumbh+Sans) | geometrica larga con maiuscole uniformi, vicina nel confronto visivo | meno pesi sottili sotto il 200 | no |
| FF Mark (schlaich bergermann partner (sbp)) | [Albert Sans](https://fonts.google.com/specimen/Albert+Sans) | geometrica con pesi da 100 | più stretta | no |
| New Rail Alphabet (Eckersley O'Callaghan) | [Public Sans](https://fonts.google.com/specimen/Public+Sans) | neo-grotesk aperta, altezza x alta come New Rail (0.53) | perde il legame con la segnaletica | no |
| New Rail Alphabet (Eckersley O'Callaghan) | [Schibsted Grotesk](https://fonts.google.com/specimen/Schibsted+Grotesk) | stesso ritmo | più grottesca | no |
| Futura T (Werner Sobek) | [Jost](https://fonts.google.com/specimen/Jost) | ispirata a Futura, la gratuita più vicina | altezza x un po’ più alta | no |
| Larken (Webb Yates Engineers) | [Gelasio](https://fonts.google.com/specimen/Gelasio) | serif con curve morbide e proporzioni vicine | meno calligrafica | no |
| Larken (Webb Yates Engineers) | [Newsreader](https://fonts.google.com/specimen/Newsreader) | serif contemporaneo con asse ottico | più sobria | no |
| Larken (Webb Yates Engineers) | [Fraunces](https://fonts.google.com/specimen/Fraunces) | la più vicina a vista | abusata dai siti generati | sì |
| Geograph (Webb Yates Engineers) | [Albert Sans](https://fonts.google.com/specimen/Albert+Sans) | geometrica con altezza x 0.50 come Geograph | meno dettagli | no |
| Replica (EFLA Consulting Engineers) | [Chivo](https://fonts.google.com/specimen/Chivo) | grotesk compatta e decisa, vicina nel confronto visivo | perde i tagli angolari | no |
| Replica (EFLA Consulting Engineers) | [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk) | ha i tagli angolari | abusata dai siti generati | sì |
| Domaine Text (EFLA Consulting Engineers) | [Brygada 1918](https://fonts.google.com/specimen/Brygada+1918) | serif da testo con proporzioni misurate vicine | più storica | no |
| Domaine Text (EFLA Consulting Engineers) | [Newsreader](https://fonts.google.com/specimen/Newsreader) | serif contemporaneo | meno contrasto | no |

Misure di riferimento (altezza x / altezza maiuscole / larghezza media minuscole, in frazioni del corpo), lette dai file: Söhne 0.523/0.718/0.507; Schibsted Grotesk 0.527/0.703/0.526; Atlas Grotesk 0.527/0.765/0.535; Libre Franklin 0.530/0.742/0.529; Okomito Light 0.512/0.690/0.491; Hanken Grotesk 0.493/0.697/0.504; Frutiger Light 0.510/0.698/0.476; Hind Light 0.508/0.674/0.477; DIN 0.492/0.712/0.493; Barlow 0.506/0.700/0.487; Ginto Light 0.500/0.700/0.509; Figtree 0.500/0.700/0.507; Founders Grotesk 0.437/0.630/0.449 (nessuna gratuita ha un’altezza x così bassa); FuturaT 0.416/0.667/0.434; Jost 0.460/0.700/0.466.

Due caratteri commerciali di questo censimento si possono usare gratis senza Google: **Supreme** (Formlabs) e **Satoshi** (SkyClinics) sono serviti da Fontshare con un link CSS come Google Fonts, per esempio `https://api.fontshare.com/v2/css?f[]=supreme@400,700&display=swap` (verificato, risponde con i @font-face). Satoshi però è già molto diffuso. **Futura PT** (Mutina) e **Larken** (Webb Yates) sono su Adobe Fonts, che richiede un abbonamento del cliente.

## Il confronto: leader con caratteri generici

| Sito | Settore | Paese | Titoli | Testo | Nota |
|---|---|---|---|---|---|
| [IMA Group](https://imagroup.com/) | macchine automatiche per packaging | Italia | Inter 600 | Inter 400 | h1 50px/75px (1.5) in 600: interlinea da paragrafo sui titoli |
| [Vention](https://vention.io/) | automazione industriale | Canada | Inter 600 | Inter 400 | h1 72px/90px; tutto Inter, nessun secondo carattere |
| [Carel](https://www.carel.com/) | controlli per HVAC e refrigerazione | Italia (Registro Imprese di Padova) | Open Sans 700 maiuscolo | Open Sans 400 | titoli maiuscoli bold con spaziatura 1-3px |
| [Salvagnini](https://www.salvagninigroup.com/) | macchine per lamiera | Italia | Noto Sans 700 e Noto Serif 700 | Noto Sans 400 | unico tocco proprio: "Salvagnini Display" solo per una cifra (25 anni) |
| [Comau](https://www.comau.com/) | robotica e automazione | Italia | Helvetica Neue 400-700 | sans-serif di sistema | Helvetica Neue (Linotype) usata senza un sistema: titoli a 60px/60px, testo in font di sistema |
| [Unox](https://www.unox.com/) | forni professionali | Italia (Cadoneghe, PD) | Montserrat 900 | Roboto 400 | Montserrat Black per i nomi prodotto, Roboto per il testo: la coppia più comune dei temi |
| [Breton](https://breton.it/) | macchine per pietra e metallo | Italia (Castello di Godego, TV) | Roboto 700 | Roboto 400 | carica un "BretonType" che non usa in prima schermata |
| [Pietro Fiorentini](https://www.fiorentini.com/) | tecnologie per gas e fluidi | Italia (Arcugnano, VI) | Inter 700 | Inter 400 | Inter servito come file statici per ogni peso |
| [Dallan](https://www.dallan.com/) | linee per profilatura di coil | Italia (Castelfranco Veneto, TV) | Lato 700 | Lato 300 | tema WordPress con Lato e Font Awesome |
| [Universal Robots](https://www.universal-robots.com/) | robot collaborativi | Danimarca | Oswald 700 | Roboto Flex 300 | Oswald condensato bold, diffusissimo nei temi |
| [igus](https://www.igus.com/) | catene portacavi, cuscinetti in polimero | Germania | Roboto 700 | Roboto 400 | tutto Roboto |
| [Elesa](https://www.elesa.com/) | componenti per l’industria meccanica | Italia | Open Sans 700 | Open Sans 400 | tutto Open Sans, anche il corsivo bold per i link |
| [Bobst](https://www.bobst.com/) | macchine per packaging | Svizzera | Noto Sans 300 e 700 | Noto Sans 300 | h1 90px che mescola Light e Bold nella stessa frase |
| [Ideal Work](https://www.idealwork.com/) | superfici in calcestruzzo | Italia (Riese Pio X, TV) | DM Sans 700 | DM Sans 400 | DM Sans, tra le più abusate dai siti generati |
| [Margraf](https://www.margraf.it/) | marmi per architettura | Italia (Gambellara, VI) | Gantari 500 | Gantari 300 | Google Fonts recente, un solo carattere |
| [Antolini](https://www.antolini.com/) | pietre naturali | Italia (Sant’Ambrogio di Valpolicella, VR) | Lato 400 maiuscolo spaziato (0.15em) | Lato Light | Lato servito da Adobe Fonts, maiuscolo molto spaziato |
| [Bisazza](https://www.bisazza.com/) | mosaico | Italia (Montecchio Maggiore, VI) | Bebas Neue maiuscolo spaziato | Gordita | Bebas Neue: il condensato dei poster gratuiti |
| [Equitone](https://www.equitone.com/) | lastre in fibrocemento per facciate | Belgio (gruppo Etex) | Montserrat 400 | Montserrat 400 | tutto Montserrat |
| [Petersen Tegl](https://www.petersen-tegl.dk/) | mattoni | Danimarca | Nunito Sans 600-900 maiuscolo | Nunito Sans 400 | un marchio famosissimo tra gli architetti con un sito da tema |
| [41zero42](https://www.41zero42.com/) | ceramica | Italia | Titillium Web 700 | Titillium Web 400 | Titillium: carattere universitario gratuito |
| [Santagostino](https://www.santagostino.it/) | poliambulatori privati | Italia | Source Sans Pro 400-700 | Lato 400 | due sans quasi uguali insieme |
| [Dentologie](https://www.dentologie.com/) | studi dentistici | USA | Playfair Display 400 con parola in corsivo | Inter 400 | Playfair + Inter + corsivo d’accento: lo schema esatto dei siti generati |
| [SkyClinics](https://skyclinics.al/) | dentista e medicina estetica | Albania | Satoshi 200-300 | Satoshi 400 | Awwwards HM 2026; Satoshi (Fontshare) maiuscolo molto spaziato: carattere ormai di moda |
| [knippershelbig](https://www.knippershelbig.com/) | ingegneria strutturale e facciate | Germania | Plus Jakarta Sans 400 | Plus Jakarta Sans 400 | Plus Jakarta Sans, nella lista dei caratteri abusati |
| [Coffman Engineers](https://www.coffman.com/) | ingegneria | USA | Rubik 900 corsivo maiuscolo | Rubik 300-400 | presente in una raccolta di utenti su Awwwards, ma con Rubik Black corsivo maiuscolo |
| [INTECH](https://www.beintech.fr/) | studio tecnico (strutture, fluidi) | Francia | Space Grotesk 300-700 | Funnel Sans | Awwwards HM 2025 con Space Grotesk, carattere abusato |
| [OSE Engineering](https://www.ose-engineering.fr/) | ingegneria e decarbonizzazione | Francia | Geist 500 maiuscolo | Geist 300; Space Mono per il menu | Awwwards HM 2026 con Geist + Space Mono, la coppia dei siti di software |

Altri casi rilevati, non inclusi nei 30:

- [Hilti](https://www.hilti.com/), utensili e fissaggi (Liechtenstein): carattere aziendale "Hilti" (URW, 2016) Roman e Bold; titoli 44-77px bold, interlinea 1.0.
- [Holcim](https://www.holcim.com/), cemento e materiali da costruzione (Svizzera): carattere aziendale "Holcim Type" (supertype, 2021); titoli maiuscoli Black 32-36px; testo 19px.
- [Palet](https://palet.shop/), piastrelle smaltate su misura (n.d.): Founders Grotesk (Klim) + Founders Grotesk Condensed; Awwwards HM 2024; serve anche un file "TestFoundersGrotesk" di prova; h1 96px con interlinea 0.85.

## Note pratiche per WordPress ed Elementor

- Elementor gratuito elenca i Google Fonts; per i caratteri self-hosted (per esempio un .woff2 scaricato da Google, o Supreme da Fontshare) serve un @font-face nel tema figlio o un plugin per caratteri personalizzati. sbp.de dimostra che un sito di alto livello su Elementor è possibile con un carattere caricato in locale.
- Molte alternative proposte sono variabili (Archivo con asse di larghezza, Mona Sans, Newsreader con asse ottico): conviene caricarle come file locali variabili, così i pesi intermedi (450, 350) usati dai siti di riferimento sono disponibili.
- Per i numeri: Mosa, EFLA e Parsley impostano `font-variant-numeric` (lining-nums, tabular-nums). Nei file serviti da Google le cifre tabellari (tnum) ci sono in Schibsted Grotesk, Archivo, Public Sans, Figtree, Instrument Sans, Barlow, Jost, Newsreader e Gloock; mancano in Hanken Grotesk, Libre Franklin, Hind, Albert Sans e Source Sans 3 (verificato sui file scaricati dall’API).

## Limiti

- Neko Health e Knipex hanno bloccato il browser automatico (controllo di sicurezza), Swiss Smile ha risposto 502: esclusi. Lithos Design e Grassi Pietre (Vicenza) hanno un captcha: esclusi.
- I caratteri di Weidmüller non si sono potuti identificare (file protetti); Arup ha dato uno screenshot vuoto, ma gli stili calcolati sono stati letti.
- Le misure descrivono il primo schermo e la home; pagine interne possono usare altri pesi.
- Il riconoscimento è stato verificato per WEIMA, Q-Industrial, Dębski Clinic, EFLA, Tend e McMaster-Carr; per gli altri è indicato "nessun premio web verificato" e la scelta si basa sulla qualità tipografica osservata.

## Fonti

- https://a2-type.co.uk/new-rail-alphabet
- https://abcdinamo.com/typefaces/ginto
- https://api.fontshare.com/v2/css?f[]=supreme@400,700&display=swap
- https://atipofoundry.com/fonts/basier
- https://breton.it/
- https://commercialtype.com/catalog/atlas
- https://dinesen.com/
- https://displaay.net/typeface/matter
- https://displaay.net/typeface/teodor
- https://en.wikipedia.org/wiki/Salvatori_(design)
- https://ezra.com/
- https://fonts.adobe.com/fonts/futura-pt
- https://fonts.adobe.com/fonts/larken
- https://fonts.google.com/specimen/Albert+Sans
- https://fonts.google.com/specimen/Archivo
- https://fonts.google.com/specimen/Archivo+Narrow
- https://fonts.google.com/specimen/Arimo
- https://fonts.google.com/specimen/Barlow
- https://fonts.google.com/specimen/Barlow+Condensed
- https://fonts.google.com/specimen/Bodoni+Moda
- https://fonts.google.com/specimen/Bricolage+Grotesque
- https://fonts.google.com/specimen/Brygada+1918
- https://fonts.google.com/specimen/Chivo
- https://fonts.google.com/specimen/Chivo+Mono
- https://fonts.google.com/specimen/Cormorant+Garamond
- https://fonts.google.com/specimen/Crimson+Pro
- https://fonts.google.com/specimen/DM+Sans
- https://fonts.google.com/specimen/DM+Serif+Display
- https://fonts.google.com/specimen/EB+Garamond
- https://fonts.google.com/specimen/Figtree
- https://fonts.google.com/specimen/Fira+Sans
- https://fonts.google.com/specimen/Fragment+Mono
- https://fonts.google.com/specimen/Fraunces
- https://fonts.google.com/specimen/Funnel+Sans
- https://fonts.google.com/specimen/Gelasio
- https://fonts.google.com/specimen/Gilda+Display
- https://fonts.google.com/specimen/Gloock
- https://fonts.google.com/specimen/Golos+Text
- https://fonts.google.com/specimen/Hanken+Grotesk
- https://fonts.google.com/specimen/Hind
- https://fonts.google.com/specimen/Instrument+Sans
- https://fonts.google.com/specimen/Inter
- https://fonts.google.com/specimen/Inter+Tight
- https://fonts.google.com/specimen/Jost
- https://fonts.google.com/specimen/Kumbh+Sans
- https://fonts.google.com/specimen/League+Spartan
- https://fonts.google.com/specimen/Libre+Caslon+Display
- https://fonts.google.com/specimen/Libre+Franklin
- https://fonts.google.com/specimen/Mona+Sans
- https://fonts.google.com/specimen/Newsreader
- https://fonts.google.com/specimen/Noto+Serif+Display
- https://fonts.google.com/specimen/Petrona
- https://fonts.google.com/specimen/Playfair+Display
- https://fonts.google.com/specimen/Plus+Jakarta+Sans
- https://fonts.google.com/specimen/Prata
- https://fonts.google.com/specimen/Public+Sans
- https://fonts.google.com/specimen/Roboto+Condensed
- https://fonts.google.com/specimen/Roboto+Mono
- https://fonts.google.com/specimen/Schibsted+Grotesk
- https://fonts.google.com/specimen/Sofia+Sans
- https://fonts.google.com/specimen/Source+Sans+3
- https://fonts.google.com/specimen/Source+Serif+4
- https://fonts.google.com/specimen/Space+Grotesk
- https://fonts.google.com/specimen/Spectral
- https://fonts.google.com/specimen/Unbounded
- https://fonts.google.com/specimen/Work+Sans
- https://fontsource.org/fonts/hanken-grotesk/about
- https://formlabs.com/
- https://imagroup.com/
- https://klim.co.nz/fonts/domaine-text/
- https://klim.co.nz/fonts/financier-display/
- https://klim.co.nz/fonts/founders-grotesk/
- https://klim.co.nz/fonts/geograph/
- https://klim.co.nz/fonts/heldane-display/
- https://klim.co.nz/fonts/soehne/
- https://lanserhof.com/
- https://lineto.com/typefaces/replica
- https://luzi-type.ch/nantes
- https://machinalabs.ai/
- https://mosa.com/
- https://palet.shop/
- https://pangrampangram.com/products/grafier
- https://pangrampangram.com/products/neue-montreal
- https://skyclinics.al/
- https://thedesignersfoundry.com/tomato-grotesk
- https://vention.io/
- https://webbyates.com/
- https://weima.com/
- https://weima.com/us/amazing-news-amazing-feedback-site-of-the-day-and-developers-award/
- https://www.41zero42.com/
- https://www.antolini.com/
- https://www.arup.com/
- https://www.awwwards.com/BroworksDesign/collections/industry-websites/
- https://www.awwwards.com/sites/debski-clinic
- https://www.awwwards.com/sites/efla-engineers
- https://www.awwwards.com/sites/intech-technical-engineering
- https://www.awwwards.com/sites/ose-engineering
- https://www.awwwards.com/sites/palet-bespoke-ceramic-tiles
- https://www.awwwards.com/sites/q-industrial
- https://www.awwwards.com/sites/sky-clinics
- https://www.beintech.fr/
- https://www.bisazza.com/
- https://www.bobst.com/
- https://www.carel.com/
- https://www.coffman.com/
- https://www.comau.com/
- https://www.creativeboom.com/news/type-foundry-klim-launches-a-new-typeface-soehne-along-with-a-gorgeous-new-website/
- https://www.dallan.com/
- https://www.debskiclinic.pl/
- https://www.dentologie.com/
- https://www.efla-engineers.com/
- https://www.elesa.com/
- https://www.eocengineers.com/
- https://www.equitone.com/
- https://www.escofet.com/
- https://www.face37.com/beckett
- https://www.festool.com/
- https://www.fiorentini.com/
- https://www.florim.com/
- https://www.fontshare.com/fonts/supreme
- https://www.grillitype.com/typeface/gt-super
- https://www.hadrian.co/
- https://www.hellotend.com/
- https://www.hilti.com/
- https://www.holcim.com/
- https://www.iacollaborative.com/results/mcmaster-carr
- https://www.idealwork.com/
- https://www.igus.com/
- https://www.knippershelbig.com/
- https://www.komaxgroup.com/
- https://www.laminam.com/
- https://www.lucasfonts.com/fonts/thesans
- https://www.margraf.it/
- https://www.mcmaster.com/
- https://www.monotype.com/fonts/helvetica-now
- https://www.monotype.com/fonts/neue-frutiger-world
- https://www.mutina.it/
- https://www.mutina.it/downloads/16088/1697/PR_Mutina_Ronan_Bouroullec_EN.pdf
- https://www.myfonts.com/collections/ff-din-font-fontfont
- https://www.myfonts.com/collections/frutiger-font-linotype
- https://www.myfonts.com/collections/frutiger-serif-font-linotype
- https://www.myfonts.com/collections/midnight-sans-variable-font-colophon-foundry
- https://www.myfonts.com/fonts/hanken-designco/okomito-next
- https://www.myfonts.com/pages/linotype-ff-mark
- https://www.mythology.com/project/tend
- https://www.onemedical.com/
- https://www.ose-engineering.fr/
- https://www.parsleyhealth.com/
- https://www.petersen-tegl.dk/
- https://www.q-industrial.com/
- https://www.red-dot.org/project/tend-49427
- https://www.rieder.cc/
- https://www.salvagninigroup.com/
- https://www.salvatoriofficial.com/
- https://www.santagostino.it/
- https://www.sbp.de/
- https://www.swisstypefaces.com/fonts/euclid/
- https://www.swisstypefaces.com/fonts/sangbleu/
- https://www.swisstypefaces.com/fonts/suisse/
- https://www.trumpf.com/
- https://www.universal-robots.com/
- https://www.unox.com/
- https://www.weidmueller.com/
- https://www.wernersobek.com/
