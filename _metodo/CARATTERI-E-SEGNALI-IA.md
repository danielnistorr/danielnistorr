# Caratteri e segnali da IA: cosa fare prima di progettare

Guida operativa per chi costruisce i siti della campagna (WordPress, Elementor gratuito, Google Fonts). Si legge prima della
direzione (METODO 2.3) e si usa di nuovo prima di consegnare. Riassume la ricerca del 6 ottobre 2026 in
`_metodo/ricerca-caratteri/`: `censimento-industria-servizi.md` (60 siti), `censimento-ospitalita-cibo.md` (30 siti),
`fonti-tipografiche.md` (fonti di mestiere), `segnali-ia.md` (catalogo dei segnali e misure). Le citazioni tra parentesi
rimandano a quei file; i link alle fonti esterne sono lì.

Strumenti: `_metodo/kit/segnali.sh` (misura, paragrafo f) e `_metodo/tavole-caratteri/` (una tavola per settore, paragrafo c).

Perché esiste: il committente ha giudicato i primi siti "IA LIKE". Gardens Pav e Wirmec non hanno i segnali della prima ondata
(viola, Inter, tre box), ma stanno dentro la seconda: monospazio, filetti, etichette, frecce, poche foto (segnali-ia 1).

---

## a. Le regole che contano di più, in ordine di effetto

1. **Foto vere, grandi: almeno il 35 % della home a 1440.** È la misura che separa meglio i nostri siti da quelli veri:
   Gardens Pav 9,6 %, Wirmec 15,7 %, Benvegnù 40,2 %; i nove riferimenti misurati stanno fra 37 e 63 % (Escofet 63,
   Krone 58, Trumpf 54, Hirschen 53, Hermle 48). Senza foto la pagina si riempie di tipografia, filetti e numeri, cioè
   dell'aspetto "IA" (segnali-ia 4.7, I1). Prima di impaginare: chiedere o fare le foto; una foto prende metà schermo.
2. **Una famiglia, o una superfamiglia; un secondo carattere solo con un compito fisso.** Industria e servizi: 16 siti di
   riferimento su 30 usano una famiglia, 12 ne usano due, uno tre; l'unico con quattro (Ezra) è anche quello col corsivo
   d'accento colorato. Ospitalità e cibo: 9 una, 17 due, 3 tre, sempre con ruoli fissi (censimenti, "In breve"). Il
   secondo carattere fa una cosa sola: i titoli, oppure i nomi delle collezioni, oppure i menu. Mai due caratteri nello
   stesso paragrafo (Butterick, fonti 1.2).
3. **Niente monospazio da programmazione.** 14 riferimenti su 15 misurati non hanno mono; l'unico (Escofet) usa il mono
   della sua superfamiglia per menu e luoghi, sotto foto al 63 %. Gardens Pav ha il 22,5 % del testo in IBM Plex Mono e 57
   etichette maiuscole tutte in mono; Wirmec il 9,4 % (segnali-ia 4.1, T2). Nei 30 siti di ospitalità il mono compare 4
   volte ed è sempre da macchina da scrivere (Prestige Elite, Cutive Mono, Pitch Sans), mai JetBrains, Fira Code o Plex
   Mono. I numeri tecnici si allineano con le cifre tabellari del carattere di testo (`font-variant-numeric: tabular-nums`).
4. **Titoli leggeri o regolari, non neri.** 22 siti di riferimento su 30 fanno i titoli grandi in peso 200-500 (sbp 200 a
   110 px, Q-Industrial 300 a 80 px, Salvatori e Dinesen 300, TRUMPF Light, Hadrian 400, WEIMA 500); nei siti generici
   prevalgono 600-900 (Unox Montserrat 900, IMA e Vention Inter 600). Nell'ospitalità il grassetto vero nei titoli
   compare in 3 siti su 30. Titoli grandi con interlinea 0,9-1,2 e spaziatura da -0,02 a -0,05em (censimento industria,
   "Cosa distingue i siti migliori").
5. **Niente "vestito da scheda tecnica".** Il contenuto dei nostri siti è buono (misure, norme, nomi); il problema è che
   ogni dato porta lo stesso vestito: etichetta mono maiuscola, filetto, freccia. Filetti larghi: Gardens Pav 97, Wirmec
   51, Benvegnù 43, riferimenti 0-30 (mediana 9). Frecce scritte: Wirmec 20, Benvegnù 13, Gardens Pav 7, riferimenti 0-2.
   In home: una frase con due o tre dati per prodotto, le tabelle nelle schede (Komax, Hermle, Trumpf: nessuna tabella in
   home). Lo spazio separa; il filetto solo dentro una tabella vera (segnali-ia 4.3, L3, K2, D2).
6. **Almeno un contenuto con una data o un nome.** È il segnale umano più forte dei riferimenti: fiera con date, città e
   stand (Zünd, Kortrijk 4-6 ottobre 2026, stand 4151), storia di un cliente con nome (Komax, Confecta), evento con giorno e
   orario (Paxmontana), cantiere con città e anno. Un modello non lo inventa; noi non dobbiamo inventarlo: lo prendiamo dal
   sito, dai social o dal cliente, e se manca va nel LEGGIMI tra le cose da chiedere (segnali-ia 6).
7. **Gerarchia vera: almeno tre misure di H2 e un solo elemento davvero grande.** Gardens Pav ha tutti gli H2 a 42 px,
   Wirmec a 48; Benvegnù cinque misure (32-144 px), con "VIENI AL BANCO" a 144 px sulla foto (segnali-ia T6).
8. **Al massimo quattro fasce di fondo, di altezze diverse.** I nostri 6-8 cambi di fondo quasi uguali; Escofet, Komax,
   Muottas Muragl 2 (segnali-ia C4). Un fondo per quasi tutta la pagina e un cambio deciso, oppure fasce date dalle foto.

Regola d'insieme: un segnale isolato si tiene se ha una ragione; due nella stessa schermata si correggono (Hallmark, F6).

---

## b. Caratteri da non usare come voce principale

"Voce principale" vuol dire il carattere del testo (più metà della pagina) o dei titoli. Il problema non è il carattere ma
il default: gli stessi nomi, scelti con una ragione, stanno in lavori pubblicati (fonti 3.6). Qui però si parte senza.

**Prima ondata: i default dei modelli, delle piattaforme e dei temi.**

| Caratteri | Motivo | Fonte |
|---|---|---|
| Inter, Inter Tight | "Almost always Inter is their primary type choice"; vietato dal committente | Pimp my Type 2026; 925Studios (fonti 1.5; segnali-ia F12) |
| Roboto, Roboto Slab | default del kit globale di Elementor (Roboto 600 primario, Roboto Slab 400 secondario, Roboto 400 testo, Roboto 500 accento) e Google Font più richiesto del web | `global-typography.php` di Elementor; Web Almanac 2025 (fonti 3.1, 3.2) |
| Open Sans, Lato, Arial | "Never use" nel cookbook Anthropic: sono la media del web | cookbook Anthropic (fonti 3.4) |
| Poppins, Montserrat | secondo e quarto Google Font più diffusi; "Montserrat is horribly overused" | Web Almanac 2025; Pimp my Type (fonti 1.5, 3.2) |
| Cardo (con Inter) | WordPress Twenty Twenty-Four | `theme.json` (fonti 3.1) |
| Manrope, Fira Code | WordPress Twenty Twenty-Five | `theme.json` (fonti 3.1) |
| Geist, Geist Mono | `create-next-app` di Vercel, base di v0 | fonti 3.1; Krebs (segnali-ia F3) |

**Seconda ondata: i caratteri che i prompt "anti IA" e le liste 2026 propongono al posto di Inter**, oggi riconoscibili quanto
Inter perché ogni modello li sceglie quando gli si vieta Inter.

| Caratteri | Motivo | Fonte |
|---|---|---|
| Space Grotesk, Space Mono, JetBrains Mono | coppie "tecniche" consigliate ai modelli; Space Grotesk anche negli Awwwards recenti (INTECH) | cookbook Anthropic; Krebs (segnali-ia F1, F3); censimento industria |
| IBM Plex (Sans, Condensed, Serif, Mono) | "Technical: IBM Plex family" nel cookbook; Plex Mono "generico e abusato" | cookbook (fonti 3.4); Kucharski (segnali-ia F11); è Wirmec e il mono di Gardens Pav |
| Playfair Display, Fraunces, Crimson Pro, Newsreader, Source Sans 3 | lista "Distinctive" e "Editorial" che Anthropic dà ai suoi modelli | cookbook e blog Anthropic (segnali-ia F1; fonti 3.4) |
| Instrument Serif, Instrument Sans, Syne, Bricolage Grotesque | "font da template" misurati su 1.590 pagine; Instrument Serif col corsivo d'accento | Krebs (segnali-ia F3); Vadgama (fonti 3.4) |
| DM Sans, DM Serif Display, Plus Jakarta Sans, Outfit, Sora, Unbounded, Cormorant Garamond | liste SEO 2026 copiate dai generatori e coppie "Playfair + Inter", "Cormorant + Montserrat" | madegooddesigns, muz.li (fonti 3.3, 3.5) |
| Satoshi, Clash Display, Cabinet Grotesk (Fontshare) | stile "Startup" del cookbook; Satoshi negli Awwwards 2026 (SkyClinics) | fonti 3.4; censimento industria |

**Tic di casa, da non riproporre come prima scelta:** Archivo con IBM Plex Mono (Gardens Pav), IBM Plex intera (Wirmec),
Barlow e Barlow Condensed (Benvegnù), Source Serif 4 con Schibsted Grotesk (Albergo Vescovi), Libre Franklin (Leon d'Oro).
Gelasio torna in sei confronti del censimento ospitalità: usarlo una volta, non come risposta per tutto.

Controllo: `segnali.sh` segnala come DA CORREGGERE (soglia 2) ogni carattere di queste tabelle che fa il testo principale,
i titoli o almeno il 10 % del testo.

---

## c. Scelte per i sette settori

Ogni settore ha una scelta raccomandata e due alternative, tutte diverse tra settori e tutte nell'elenco dei Google Fonts di
Elementor 4.3.3 (`includes/fonts.php`, verificato). Le famiglie e i pesi indicati sono stati chiamati sull'API css2 di Google
il 6 ottobre 2026: tutte le richieste rispondono 200 con i pesi chiesti; le cifre tabellari sono state lette nei file serviti.
La riga `family=` è quella da mettere nell'URL `https://fonts.googleapis.com/css2?family=...&display=swap`.

Come leggere le scale: `famiglia peso · px a 1440/1024/390 · interlinea · spaziatura in em`; `MAIUSC.` solo dove il maiuscolo
è previsto. Display: il titolo della home o il nome di una collezione, una volta per pagina. h1: il titolo delle pagine
interne. Il paragrafo d'apertura usa la misura dell'h3 con il peso del testo. Etichetta: menu, bottoni, intestazioni di
tabella. Le misure a 1024 valgono per il tablet; quelle a 390 per il telefono. In Elementor: Impostazioni del sito,
Tipografia globale, con i valori per desktop, tablet e mobile.

### c1. Macchine e industria

Tavola: `tavole-caratteri/01-macchine.html` (testi e foto di Wirmec).

- **Raccomandata: Hanken Grotesk.** `family=Hanken+Grotesk:ital,wght@0,400;0,500;1,400`. Riferimento: WEIMA Maschinenbau (weima.com), trituratori e presse, Awwwards Site of the Day, carattere originale Okomito (Hanken Design Co.): stesso disegnatore (Alfredo Marco Pradil); altezza x 0,493 contro 0,512, terminali piatti. WEIMA: titoli enormi in Medium mai in Bold, testo Light con +0,2 px, nessun maiuscolo, una famiglia. Numeri: cifre tabellari già di default nel file Google. Non fare: titoli in 600-800; etichette maiuscole; un monospazio accanto; spaziatura negativa sul testo. È anche in una lista SEO 2026 (madegooddesigns): regge solo vestita come WEIMA.
- **Alternativa 1: Sofia Sans.** `family=Sofia+Sans:ital,wght@0,400;0,600;0,700;1,400`. Riferimento: Festool (festool.com), elettroutensili professionali, carattere originale FF DIN (Albert-Jan Pool): impianto DIN con più calore, cifre tabellari. Festool: titoli DIN 700 a 43 px, sottotitoli 500, testo 18/24, nessun maiuscolo, una famiglia sola. Numeri: tnum nel file Google (font-variant-numeric: tabular-nums). Non fare: Sofia Sans Condensed accanto: è lo schema Barlow + Barlow Condensed di Benvegnù; titoli in maiuscolo.
- **Alternativa 2: Chivo.** `family=Chivo:ital,wght@0,300;0,400;0,500;1,300`. Riferimento: Formlabs (formlabs.com), stampanti 3D; EFLA (efla-engineers.com), ingegneria, carattere originale Supreme (Formlabs), Replica (EFLA): grotesk compatta con x 0,51 come Supreme. Formlabs: titoli di sezione 500 a 32 px con -0,04em, etichette 14 px a +0,1em in maiuscolo; EFLA mette le cifre tabellari su tutto. Numeri: cifre tabellari già di default. Non fare: un monospazio o filetti a ogni riga: Chivo è della stessa fonderia di Archivo e ricadrebbe nello schema di Gardens Pav; non usarla per Gardens Pav.

| ruolo | Hanken Grotesk | Sofia Sans | Chivo |
|---|---|---|---|
| display | Hanken 500 · 92/72/46 · 0,98 · -0,025 | Sofia 700 · 80/64/42 · 1 · -0,01 | Chivo 500 · 84/66/44 · 1 · -0,035 |
| h1 | Hanken 500 · 60/48/34 · 1,06 · -0,02 | Sofia 700 · 54/44/32 · 1,05 · -0,005 | Chivo 500 · 56/46/32 · 1,05 · -0,03 |
| h2 | Hanken 500 · 40/34/28 · 1,12 · -0,015 | Sofia 600 · 36/30/26 · 1,12 · 0 | Chivo 500 · 36/30/26 · 1,15 · -0,02 |
| h3 | Hanken 500 · 22/21/20 · 1,3 · 0 | Sofia 600 · 22/21/20 · 1,25 · 0 | Chivo 500 · 21/20/19 · 1,3 · 0 |
| testo | Hanken 400 · 18/17/17 · 1,55 · +0,005 | Sofia 400 · 18/18/17 · 1,45 · +0,005 | Chivo 300 · 19/18/17 · 1,55 · 0 |
| piccolo | Hanken 400 · 15/15/14 · 1,45 · +0,005 | Sofia 400 · 15/15/14 · 1,4 · +0,01 | Chivo 400 · 15/15/14 · 1,45 · 0 |
| etichetta | Hanken 500 · 15/15/15 · 1,2 · 0 | Sofia 600 · 15/15/15 · 1,2 · +0,01 | Chivo 500 · 13/13/13 · 1,2 · +0,08 · MAIUSC. |

### c2. Materiali, edilizia ed esterni

Tavola: `tavole-caratteri/02-materiali.html` (testi e foto di Gardens Pav).

- **Raccomandata: Jost.** `family=Jost:ital,wght@0,400;0,500;0,600;1,400`. Riferimento: Mutina (mutina.it), piastrelle e superfici ceramiche, carattere originale Futura PT: Jost è disegnata su Futura (a e g a un piano, maiuscole geometriche). Mutina: titoli 58/69,6 a peso normale e mai in grassetto, testo 17,6/32, menu Futura Bold maiuscolo a 15 px. Numeri: tnum nel file Google. Non fare: titoli in grassetto; maiuscolo per frasi intere; testo sotto 16 px (altezza x 0,46).
- **Alternativa 1: Public Sans.** `family=Public+Sans:ital,wght@0,300;0,400;0,500;1,400`. Riferimento: Salvatori (salvatoriofficial.com), pietra naturale; Dinesen (dinesen.com), pavimenti in legno, carattere originale Atlas Grotesk Light: maiuscole alte e molti pesi leggeri come Atlas; Libre Franklin è più vicina ma non ha cifre tabellari. Salvatori: titoli 64/74 in Light, etichette 500 maiuscolo a 0,1em. Numeri: tnum nel file Google. Non fare: titoli sopra il 300; più di una etichetta maiuscola per sezione; testo in 300 sotto 18 px.
- **Alternativa 2: Prata + Golos Text.** `family=Prata&family=Golos+Text:wght@400;500;600`. Riferimento: Rieder (rieder.cc), pannelli di facciata in calcestruzzo fibrorinforzato, carattere originale PP Grafier Display + Tomato Grotesk: Prata è la gratuita più vicina a Grafier (alto contrasto, grazie a cuneo); Golos Text ha le proporzioni di Tomato. Rieder: titolo 96,6/101 sulla foto, il resto in grotesk. Numeri: solo in Golos Text (tnum); Prata ha cifre proporzionali. Non fare: Prata sotto 28 px o in corsivo (non esiste: font-synthesis: none); prezzi e misure in Prata.

| ruolo | Jost | Public Sans | Prata + Golos Text |
|---|---|---|---|
| display | Jost 400 · 84/66/44 · 1,04 · -0,01 | Public 300 · 80/64/42 · 1,04 · -0,02 | Prata 400 · 92/70/44 · 1,04 · -0,01 |
| h1 | Jost 400 · 58/48/34 · 1,1 · -0,005 | Public 300 · 58/48/34 · 1,1 · -0,015 | Prata 400 · 60/48/34 · 1,1 · -0,005 |
| h2 | Jost 400 · 40/34/28 · 1,18 · 0 | Public 300 · 40/34/28 · 1,18 · -0,01 | Prata 400 · 40/34/28 · 1,18 · 0 |
| h3 | Jost 500 · 22/21/20 · 1,3 · 0 | Public 500 · 20/20/19 · 1,35 · 0 | Golos 600 · 20/20/19 · 1,3 · 0 |
| testo | Jost 400 · 18/18/17 · 1,75 · +0,005 | Public 400 · 17/17/16 · 1,6 · 0 | Golos 400 · 18/17/16 · 1,55 · 0 |
| piccolo | Jost 400 · 15/15/14 · 1,55 · +0,01 | Public 400 · 14/14/14 · 1,5 · +0,005 | Golos 400 · 15/15/14 · 1,45 · 0 |
| etichetta | Jost 600 · 14/14/13 · 1,2 · +0,06 · MAIUSC. | Public 500 · 12/12/12 · 1,2 · +0,1 · MAIUSC. | Golos 500 · 14/14/14 · 1,2 · +0,01 |

### c3. Hotel di montagna e di città

Tavola: `tavole-caratteri/03-hotel.html` (testi e foto di Albergo Vescovi, Asiago).

- **Raccomandata: Spectral.** `family=Spectral:ital,wght@0,300;0,400;0,500;1,400`. Riferimento: Hotel Schwarzschmied (schwarzschmied.com), Lana, chiave Michelin, carattere originale Livory: misure vicinissime: x 0,450 contro 0,464, larghezza 0,502 contro 0,513, contrasto 2,1 contro 2,0. Schwarzschmied: un serif per titoli e testo, h1 72/1,14, due soli pesi, menu maiuscolo a +0,15em. Numeri: cifre tabellari già di default. Non fare: fondo crema con accento terracotta (seconda ondata); parole in corsivo nei titoli; più di due pesi in pagina.
- **Alternativa 1: Petrona.** `family=Petrona:ital,wght@0,300;0,400;0,600;1,400`. Riferimento: Il Palazzo Experimental (experimentalgroup.com), Venezia, albergo di città, carattere originale Nantes: serif con le stesse irregolarità di Nantes (x 0,443 contro 0,473). Experimental: Nantes per il 79 % del testo, titoli da 32 a 120 px con interlinea 1,1-1,2. Numeri: tnum nel file Google. Non fare: Newsreader al suo posto (lista dei modelli); una parola in corsivo nel titolo.
- **Alternativa 2: Belleza + Cabin.** `family=Belleza&family=Cabin:ital,wght@0,400;0,500;0,600;1,400`. Riferimento: Hotel Milla Montis (hotel-milla-montis.com), Maranza, Michelin, carattere originale Optima nova Light + ITC Johnston: Belleza è un’umanista modulata come Optima (contrasto 2,4 contro 2,8); Cabin è ispirata a Johnston e Gill. Milla Montis: titolo 70/1,19, testo 20/1,4, menu Johnston maiuscolo a +0,264em. Numeri: Cabin non ha cifre tabellari: prezzi e orari in righe brevi, non in colonna. Non fare: grassetto in Belleza (un peso solo); colonne di numeri in Cabin.

| ruolo | Spectral | Petrona | Belleza + Cabin |
|---|---|---|---|
| display | Spectral 300 · 72/58/40 · 1,08 · -0,01 | Petrona 300 · 76/60/40 · 1,05 · -0,02 | Belleza 400 · 70/56/38 · 1,1 · 0 |
| h1 | Spectral 400 · 52/44/32 · 1,12 · -0,005 | Petrona 400 · 54/44/32 · 1,1 · -0,01 | Belleza 400 · 50/42/30 · 1,15 · 0 |
| h2 | Spectral 400 · 38/32/27 · 1,18 · 0 | Petrona 400 · 36/32/26 · 1,18 · -0,005 | Belleza 400 · 34/30/25 · 1,2 · 0 |
| h3 | Spectral 500 · 22/21/20 · 1,3 · 0 | Petrona 600 · 21/20/19 · 1,3 · 0 | Cabin 600 · 20/19/18 · 1,3 · 0 |
| testo | Spectral 400 · 19/18/17 · 1,6 · 0 | Petrona 400 · 18/18/17 · 1,6 · 0 | Cabin 400 · 17/17/16 · 1,6 · +0,005 |
| piccolo | Spectral 400 · 15/15/15 · 1,5 · +0,01 | Petrona 400 · 15/15/14 · 1,5 · +0,005 | Cabin 400 · 14/14/14 · 1,5 · +0,01 |
| etichetta | Spectral 500 · 13/13/12 · 1,2 · +0,12 · MAIUSC. | Petrona 600 · 13/13/12 · 1,2 · +0,08 · MAIUSC. | Cabin 500 · 12/12/12 · 1,2 · +0,22 · MAIUSC. |

### c4. Ristoranti, agriturismi, cantine, salumi

Tavola: `tavole-caratteri/04-ristoranti.html` (testi e foto di Albergo Ristorante Leon d’Oro, Este).

- **Raccomandata: EB Garamond.** `family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400`. Riferimento: Weingut Bründlmayer (bruendlmayer.at), cantina, Kamptal, carattere originale Garamond URW: larghezza 0,437 contro 0,436: non si perde quasi nulla. Bründlmayer: Garamond per titoli e testo (19,8 px), corsivo solo per citazioni intere, menu maiuscolo a +0,25em. Numeri: cifre tabellari già di default. Non fare: crema con terracotta; corsivo per le parole d’accento; testo sotto 18 px (altezza x 0,40).
- **Alternativa 1: Fanwood Text + Alegreya Sans.** `family=Fanwood+Text:ital@0;1&family=Alegreya+Sans:ital,wght@0,400;0,500;0,700;1,400`. Riferimento: Manincor (manincor.com), cantina, Caldaro, carattere originale Cochin + Corporate S: Fanwood Text ha x 0,385 contro 0,372 e lo stesso rapporto x/maiuscola di Cochin (0,573 contro 0,569); Alegreya Sans ha la larghezza di Corporate S (0,445 contro 0,447). Manincor: Cochin a 90 e 46 px, testo in Corporate S, occhielli a +3 px. Numeri: solo in Alegreya Sans (tnum), con lining-nums: di default le sue cifre sono minuscole. Non fare: Fanwood sotto 26 px o in grassetto (un peso solo); prezzi in Fanwood.
- **Alternativa 2: Questrial.** `family=Questrial`. Riferimento: Poli Distillerie (poligrappa.com), Schiavon (VI), carattere originale Kabel: Questrial è misurata su Kabel (x 0,500 contro 0,509): un geometrico d’epoca, Art Déco. Poli: Kabel per tutto, testo 17 px a +0,03em; la scala dei titoli lì è piatta, qui no. Numeri: cifre tabellari già di default. Non fare: grassetto (sarebbe finto: font-synthesis: none); titoli piccoli come Poli: serve un titolo grande vero.

| ruolo | EB Garamond | Fanwood Text + Alegreya Sans | Questrial |
|---|---|---|---|
| display | EB Garamond 400 · 78/62/42 · 1,05 · -0,01 | Fanwood 400 · 76/60/40 · 1,05 · -0,01 | Questrial 400 · 72/58/38 · 1,05 · -0,015 |
| h1 | EB Garamond 400 · 56/46/34 · 1,1 · -0,005 | Fanwood 400 · 54/44/32 · 1,1 · -0,005 | Questrial 400 · 52/42/30 · 1,1 · -0,01 |
| h2 | EB Garamond 500 · 38/32/27 · 1,15 · 0 | Fanwood 400 · 38/32/27 · 1,15 · 0 | Questrial 400 · 34/30/25 · 1,2 · 0 |
| h3 | EB Garamond 600 · 23/22/21 · 1,25 · 0 | Alegreya Sans 500 · 21/20/19 · 1,3 · 0 | Questrial 400 · 22/21/20 · 1,3 · 0 |
| testo | EB Garamond 400 · 20/19/18 · 1,55 · 0 | Alegreya Sans 400 · 19/18/17 · 1,55 · 0 | Questrial 400 · 18/17/17 · 1,6 · +0,015 |
| piccolo | EB Garamond 400 · 16/16/15 · 1,45 · +0,005 | Alegreya Sans 400 · 15/15/15 · 1,45 · 0 | Questrial 400 · 15/15/14 · 1,5 · +0,02 |
| etichetta | EB Garamond 500 · 14/14/13 · 1,2 · +0,1 · MAIUSC. | Alegreya Sans 500 · 13/13/13 · 1,2 · +0,12 · MAIUSC. | Questrial 400 · 13/13/13 · 1,2 · +0,12 · MAIUSC. |

### c5. Moda, sposa, fiori, gioielli

Tavola: `tavole-caratteri/05-moda.html` (testi e foto di rosyGarbo, atelier sposa, Padova).

- **Raccomandata: Noto Serif Display + Work Sans.** `family=Noto+Serif+Display:wght@300;400&family=Work+Sans:ital,wght@0,400;0,500;1,400`. Riferimento: Laminam (laminam.com), lastre ceramiche di grande formato, carattere originale SangBleu Empire + Work Sans: serif ad alto contrasto, grazie affilate, regge il maiuscolo grande. Laminam: SangBleu maiuscolo solo per i nomi delle collezioni (96 px, -0,04em), «come su un catalogo di moda»; Work Sans è il carattere che Laminam usa davvero per il testo. Numeri: cifre tabellari di default nel serif; Work Sans con tnum. Non fare: maiuscolo serif fuori dal nome della collezione; Playfair al suo posto; Work Sans nei titoli.
- **Alternativa 1: Literata.** `family=Literata:ital,opsz,wght@0,7..72,300;0,7..72,400;0,7..72,600;1,7..72,400`. Riferimento: Bitossi Ceramiche (bitossiceramiche.it), Montelupo Fiorentino, carattere originale Catalogue: larghezza 0,555 contro 0,576, contrasto 1,7 contro 1,9. Bitossi: un serif solo anche per menu e bottoni, corsivo per i sottotitoli: sembra un catalogo stampato. Numeri: tnum nel file Google. Non fare: corsivo dentro i titoli; una sans di servizio accanto: la forza è il serif ovunque.
- **Alternativa 2: Bodoni Moda.** `family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;1,6..96,400`. Riferimento: Zýmē (zyme.it), cantina, Valpolicella; Osteria Francescana (osteriafrancescana.it), carattere originale Didot (Zýmē) e Bodoni Moda stesso (Francescana, per il testo): didone ad alto contrasto con asse ottico; lo stesso carattere fa il titolo maiuscolo come il Didot di Zýmē e il testo a 18 px con interlinea 1,6 come Francescana. Numeri: tnum nel file Google. Non fare: testo sotto 17 px; fondo crema; corsivo d’accento.

| ruolo | Noto Serif Display + Work Sans | Literata | Bodoni Moda |
|---|---|---|---|
| display | Noto Serif D. 400 · 84/64/40 · 1,04 · -0,03 · MAIUSC. | Literata 300 · 72/58/40 · 1,04 · -0,02 | Bodoni 400 · 80/62/40 · 1 · -0,01 · MAIUSC. |
| h1 | Noto Serif D. 400 · 54/44/32 · 1,1 · -0,01 | Literata 400 · 50/42/30 · 1,1 · -0,01 | Bodoni 400 · 52/42/30 · 1,08 · -0,01 |
| h2 | Noto Serif D. 400 · 38/32/27 · 1,15 · -0,005 | Literata 400 · 34/30/25 · 1,18 · -0,005 | Bodoni 400 · 36/30/26 · 1,15 · 0 |
| h3 | Work Sans 500 · 19/18/18 · 1,35 · 0 | Literata 600 · 20/19/18 · 1,3 · 0 | Bodoni 500 · 21/20/19 · 1,3 · 0 |
| testo | Work Sans 400 · 17/16/16 · 1,65 · 0 | Literata 400 · 18/17/17 · 1,6 · 0 | Bodoni 400 · 18/17/17 · 1,6 · +0,005 |
| piccolo | Work Sans 400 · 14/14/14 · 1,5 · +0,01 | Literata 400 · 15/15/14 · 1,5 · 0 | Bodoni 400 · 15/15/14 · 1,5 · +0,02 |
| etichetta | Work Sans 500 · 12/12/12 · 1,2 · +0,14 · MAIUSC. | Literata 500 · 15/15/14 · 1,2 · 0 | Bodoni 500 · 12/12/12 · 1,2 · +0,16 · MAIUSC. |

### c6. Salute e servizi alla persona

Tavola: `tavole-caratteri/06-salute.html` (testi e foto di Oltreoceano, centri sole).

- **Raccomandata: Gloock + Figtree.** `family=Gloock&family=Figtree:ital,wght@0,400;0,500;0,600;1,400`. Riferimento: One Medical (onemedical.com), poliambulatori, carattere originale GT Super Display + Ginto: Gloock ha l’alto contrasto e le grazie a cuneo di GT Super; Figtree le proporzioni di Ginto (x 0,500, larghezza 0,507 contro 0,509). One Medical: titoli 72/1,0, testo 18/31,5, etichette 600 a 14 px e +0,1em. Numeri: solo in Figtree (tnum); Gloock ha cifre proporzionali. Non fare: una parola del titolo in corsivo o in colore (Ezra, Dentologie); Gloock sotto 26 px; Playfair o Fraunces con Inter.
- **Alternativa 1: Libre Caslon Display + Albert Sans.** `family=Libre+Caslon+Display&family=Albert+Sans:ital,wght@0,400;0,600;1,400`. Riferimento: Parsley Health (parsleyhealth.com), studi medici, carattere originale Teodor Light + Euclid Circular B: Libre Caslon Display ha l’altezza x bassa e il colore leggero di Teodor; Albert Sans le proporzioni di Euclid (x 0,500, larghezza 0,515 contro 0,535). Parsley: titoli 64/71,7 a -0,02em, testo 18/27, nessun corsivo d’accento. Numeri: Albert Sans non ha cifre tabellari: orari in righe brevi. Non fare: Libre Caslon Display sotto 30 px (non regge); colonne di numeri in Albert Sans.
- **Alternativa 2: Hind.** `family=Hind:wght@400;500;600`. Riferimento: Lanserhof (lanserhof.com), medicina preventiva, carattere originale Neue Frutiger World: impronta Frutiger, x 0,508 contro 0,510. Lanserhof: apertura in maiuscolo spaziato come un logo (69 px), testo leggero 16-18 px con +0,2 px. Numeri: Hind non ha cifre tabellari: niente colonne di prezzi. Non fare: un corsivo serif accanto (Lanserhof lo fa con il Frutiger Serif della stessa superfamiglia, Hind non ce l’ha); colonne di numeri.

| ruolo | Gloock + Figtree | Libre Caslon Display + Albert Sans | Hind |
|---|---|---|---|
| display | Gloock 400 · 76/60/40 · 1,02 · -0,01 | Caslon D. 400 · 80/62/42 · 1,04 · -0,02 | Hind 400 · 56/46/32 · 1,05 · +0,06 · MAIUSC. |
| h1 | Gloock 400 · 54/44/32 · 1,06 · -0,005 | Caslon D. 400 · 60/48/36 · 1,08 · -0,02 | Hind 400 · 46/40/30 · 1,12 · -0,005 |
| h2 | Gloock 400 · 38/32/27 · 1,12 · 0 | Caslon D. 400 · 44/36/30 · 1,12 · -0,01 | Hind 400 · 34/30/25 · 1,18 · 0 |
| h3 | Figtree 600 · 20/19/18 · 1,3 · 0 | Albert 600 · 20/19/18 · 1,3 · 0 | Hind 600 · 20/19/18 · 1,3 · 0 |
| testo | Figtree 400 · 18/17/17 · 1,7 · 0 | Albert 400 · 18/17/16 · 1,55 · 0 | Hind 400 · 18/17/17 · 1,6 · +0,01 |
| piccolo | Figtree 400 · 15/15/14 · 1,5 · +0,005 | Albert 400 · 15/15/14 · 1,45 · 0 | Hind 400 · 15/15/14 · 1,5 · +0,01 |
| etichetta | Figtree 600 · 13/13/13 · 1,2 · +0,1 · MAIUSC. | Albert 600 · 14/14/13 · 1,2 · +0,03 | Hind 600 · 12/12/12 · 1,2 · +0,12 · MAIUSC. |

### c7. Casa e immobiliare

Tavola: `tavole-caratteri/07-casa.html` (testi e foto di Tutto Affitti, Villatora di Saonara).

- **Raccomandata: Gelasio + Familjen Grotesk.** `family=Gelasio:ital,wght@0,400;0,500;1,400&family=Familjen+Grotesk:ital,wght@0,400;0,500;0,600;1,400`. Riferimento: Audo Copenhagen (audocph.com), arredo, carattere originale Century Old Style + Grot 12: Gelasio ha le misure di Century Old Style (x 0,485 contro 0,489, larghezza 0,499 contro 0,487); Familjen Grotesk è un grottesco di tradizione inglese come Grot 12. Audo: il grottesco copre il 61 % del testo, menu maiuscolo a 14 px. Numeri: tnum in tutti e due; nei prezzi Familjen Grotesk. Non fare: Familjen Grotesk nei titoli grandi (le ink trap datano il lavoro); Gelasio come risposta per tutto (torna in sei confronti del censimento).
- **Alternativa 1: Old Standard TT + News Cycle.** `family=Old+Standard+TT:ital,wght@0,400;0,700;1,400&family=News+Cycle:wght@400;700`. Riferimento: Heath Ceramics (heathceramics.com), stoviglie e piastrelle, Sausalito, carattere originale Century Schoolbook + Benton Sans: Old Standard TT è un moderno ottocentesco della famiglia di Century; News Cycle è il revival di News Gothic, da cui viene Benton Sans. Heath: serif per i titoli, grottesco 12-14 px a +0,04em per tutto il resto. Numeri: News Cycle non ha cifre tabellari e ha due pesi: prezzi in righe brevi. Non fare: colonne di numeri in News Cycle; più di due pesi.
- **Alternativa 2: Kumbh Sans.** `family=Kumbh+Sans:wght@200;300;400;500`. Riferimento: schlaich bergermann partner (sbp.de), ingegneria strutturale, fatto con WordPress ed Elementor, carattere originale FF Mark: geometrica larga con maiuscole uniformi, vicina a FF Mark nel confronto visivo. sbp: apertura in ExtraLight 200 a 110 px, spaziatura positiva anche sui titoli, testo 19/34 a +0,5 px. Numeri: Kumbh Sans non ha cifre tabellari: prezzi in scheda, non in colonna. Non fare: colonne di prezzi; peso 200 sotto i 60 px; corsivi (non ci sono: font-synthesis: none).

| ruolo | Gelasio + Familjen Grotesk | Old Standard TT + News Cycle | Kumbh Sans |
|---|---|---|---|
| display | Gelasio 400 · 70/56/38 · 1,06 · -0,01 | Old Standard 400 · 68/54/36 · 1,06 · -0,01 | Kumbh 200 · 88/70/44 · 1,12 · +0,005 |
| h1 | Gelasio 400 · 50/42/30 · 1,1 · -0,005 | Old Standard 400 · 48/40/30 · 1,1 · -0,005 | Kumbh 300 · 56/46/32 · 1,16 · +0,01 |
| h2 | Gelasio 500 · 34/30/25 · 1,15 · 0 | Old Standard 400 · 34/30/25 · 1,15 · 0 | Kumbh 300 · 38/32/27 · 1,2 · +0,01 |
| h3 | Familjen 600 · 19/18/18 · 1,3 · 0 | News Cycle 700 · 19/18/18 · 1,3 · 0 | Kumbh 500 · 20/19/18 · 1,35 · +0,01 |
| testo | Familjen 400 · 17/17/16 · 1,6 · 0 | News Cycle 400 · 17/17/16 · 1,55 · +0,01 | Kumbh 400 · 18/17/17 · 1,8 · +0,02 |
| piccolo | Familjen 400 · 15/15/14 · 1,45 · +0,01 | News Cycle 400 · 15/15/14 · 1,45 · +0,02 | Kumbh 400 · 15/15/14 · 1,6 · +0,02 |
| etichetta | Familjen 500 · 13/13/13 · 1,2 · +0,06 · MAIUSC. | News Cycle 700 · 13/13/13 · 1,2 · +0,08 · MAIUSC. | Kumbh 500 · 12/12/12 · 1,2 · +0,08 · MAIUSC. |
---

## d. Regole d'uso tipografico

- **Quante famiglie.** Una; due se la seconda fa una cosa che la prima non sa fare (titoli, nomi, menu); tre solo con un
  ruolo marginale e fisso. Accoppiare per scheletro, non per etichetta: stessa superfamiglia, stesso disegnatore, oppure
  contrasto netto di scheletro e di contrasto; mai due caratteri simili in superficie e diversi nella costruzione (Poppins
  con Open Sans) (fonti 1.1, 1.5, 4.1).
- **Pesi.** Un peso per i titoli (300-500), due per il testo (400 e 600, o 400 e 500). Non 400 accanto a 600 senza un
  terzo livello, e nemmeno 100 contro 900 con "salti di 3x": è la ricetta del cookbook che ha creato la seconda ondata
  (fonti 4.2, 4.5). Il grassetto per l'enfasi nel testo; nei titoli si cambia misura e spazio, non peso.
- **Corsivi veri.** Caricare il corsivo (`ital`) quando il testo lo usa; corsivo solo per citazioni intere, titoli di opere,
  sottotitoli (Bründlmayer, Bitossi), mai per una parola del titolo (divieto). Prata, Belleza, Gloock, Libre Caslon Display,
  Questrial, Hind e Kumbh Sans non hanno corsivo: nel CSS aggiuntivo `font-synthesis: none`, così il browser non lo inventa.
- **Numeri.** Prezzi, orari, misure e dati in colonna: `font-variant-numeric: tabular-nums lining-nums`. Nel testo corrente
  cifre proporzionali. Alegreya Sans e Gelasio hanno di default le cifre minuscole: nei bottoni, nei titoli in maiuscolo e
  nelle tabelle forzare `lining-nums`. L'API Google toglie numeri minuscoli, maiuscoletto e forme per maiuscolo; le cifre
  tabellari restano quasi sempre. Senza `tnum` e con cifre proporzionali (letto nei file serviti il 6/10/2026): Libre
  Franklin, Hind, Cabin, Albert Sans, Kumbh Sans, News Cycle, Prata, Libre Caslon Display. Hanken Grotesk oggi ha cifre
  tabellari di default (il censimento la dava senza). Intervalli col trattino breve legato alle cifre da U+2060 (word
  joiner) perché non vada a capo; spazio indivisibile tra numero e unità (16&nbsp;m², 8&nbsp;m/s); mai U+2014.
- **Corpo e interlinea.** Testo 16-20 px (Butterick 15-25); con altezza x bassa (EB Garamond 0,40, Fanwood, Jost) 18-20 px.
  Interlinea del testo 1,45-1,8 (i siti calmi 1,75-1,8, i cataloghi sotto 1,4); titoli grandi 0,95-1,15; su mobile un po'
  più stretta (Google Fonts Knowledge, fonti 1.1; censimento industria).
- **Misura della riga.** 45-75 caratteri, 66 ideale. In Elementor: larghezza massima del widget di testo, circa 34em per il
  paragrafo d'apertura e 44em per la lettura, da tarare sul carattere (prova di Butterick: due o tre alfabeti minuscoli).
- **Maiuscolo.** Solo per meno di una riga: menu, bottoni, intestazioni brevi, il nome di una collezione. Piccolo e spaziato
  +0,05/+0,12em (fino a +0,25em nei menu degli alberghi alpini); grande e serif con spaziatura nulla o negativa (Laminam
  -0,04em). Mai paragrafi in maiuscolo, mai un'etichetta maiuscola sopra ogni titolo. 23 siti di ospitalità su 30 scrivono i
  titoli in minuscolo con la sola iniziale maiuscola.
- **Spaziatura.** Negativa solo sui titoli da 26-28 px in su; positiva sul maiuscolo piccolo; mai sul minuscolo del testo, salvo i
  caratteri disegnati larghi (sbp +0,5 px su FF Mark).
- **Titoli.** `text-wrap: balance` sui titoli, `pretty` sui paragrafi; niente punto finale; titoli descrittivi.
- **In Elementor.** Elementor carica i Google Fonts con la vecchia API (`css?family=Nome:100,100italic,...,900italic`), che
  dà istanze statiche: l'asse ottico di Literata e Bodoni Moda resta al valore predefinito. Per averlo, caricare il link
  `css2` della tavola nel tema figlio o ospitare i file variabili con il plugin Custom Fonts, e togliere quel carattere dal
  kit. "Load Google Fonts Locally" (spento di default dalla 3.32.1) evita le richieste a Google per il GDPR. Il kit nasce con
  Roboto e Roboto Slab: va cambiato in Impostazioni del sito prima di costruire.
- **Fontshare.** Si può usare con un link CSS solo un carattere a licenza libera e va detto: Supreme (il carattere di
  Formlabs) si carica con `https://api.fontshare.com/v2/css?f[]=supreme@400,500&display=swap` (licenza ITF Free Font,
  gratuita anche per uso commerciale, ma il cliente deve scaricarla a suo nome); non è nell'elenco di Elementor, quindi
  serve un `@font-face` o Custom Fonts. Satoshi, Clash Display e Cabinet Grotesk no: seconda ondata.

---

## e. Catalogo dei segnali da IA

Fonti, cause ed esempi in `segnali-ia.md` (paragrafo 4). Soglie per una home a 1440. "Vietato" = divieto del committente.

| Segnale | Regola verificabile (soglia) | Mossa sostitutiva |
|---|---|---|
| Carattere delle liste (b) | testo, titoli o 10 % del testo in un carattere delle tabelle b | partire dal riferimento del settore (c) |
| Monospazio come "sapore tecnico" | più di 0 % in un sito che non vende software; etichette `mono uppercase` | cifre tabellari del carattere di testo |
| Etichetta maiuscola sopra il titolo | più di 1 per pagina (non contano data, luogo, codice) | il titolo dice già dove siamo |
| Parola d'accento in corsivo, altro carattere o colore | anche una (vietato) | grassetto dello stesso carattere dentro una frase, o niente |
| Gerarchia piatta | meno di 3 misure di H2; titoli tutti 600 e testo 400 | un solo elemento grande; titoli 300-500 |
| Titoli neri a spaziatura zero | titoli sopra 40 px in 700-900 con spaziatura 0 | 200-500 e -0,02/-0,05em |
| Viola, indaco, gradienti, testo in gradiente | uno (vietato) | colore del marchio o del materiale |
| Palette della seconda ondata | crema o beige con serif e terracotta (circa #D97757); nero con verde acido; smeraldo | bianco e il colore del soggetto (i campioni di Rieder, il verde del logo) |
| Un accento per tutto | stesso colore saturo su bottoni, link, numeri, trattini, frecce | colore su bottone e logo; il resto prende tono dalle foto |
| Fasce alterne regolari | più di 4 fasce di fondo a tutta larghezza, di altezza simile | un fondo e un cambio deciso, o fasce di foto |
| Titolo a sinistra, paragrafo a destra | in più di 1 sezione | titolo e testo nella stessa colonna, la foto guida |
| Capo di sezione "a cartella" | etichette agli estremi e filetto con le stanghette | nessuna testata ripetuta |
| Filetti ovunque | 30 o più bordi sottili larghi più di 200 px | lo spazio; il filetto solo in tabella |
| Numero grande con etichetta | più di 1, o un numero senza fonte | il numero dentro una frase |
| Numerazioni 01, 02, 03 | davanti a voci che non sono una procedura | numerare solo i passi veri |
| Indice a righe con conteggio e freccia | "Vasche monoblocco 17 MISURE →" | categorie come foto cliccabili (Hermle, Benvegnù) |
| Hero diviso con due bottoni | testo e immagine a metà, pieno più contorno | un'azione sola, o nessuna |
| Tabelle complete in home | più di 4 righe di dati | due o tre dati in una frase; tabelle nelle schede |
| Disegni rifatti con quote mono | cartiglio finto in grafica | disegno dell'azienda o foto del prodotto posato |
| Poche foto, piccole | area foto sotto il 35 % | foto vere, una a metà schermo |
| Foto stock, render 3D, foto IA | una spacciata per l'azienda | foto dell'azienda; il brief delle foto mancanti nel LEGGIMI |
| Badge sopra il titolo, tre box con icona, card col bordo sinistro, vetro, emoji, Lucide, shadcn | uno (vietati) | contenuto vero in testo e foto |
| Trattino colorato sotto ogni H2 | più di 1 | niente: lo spazio basta |
| Frecce scritte nei link | più di 2 | sottolineatura; la freccia solo per un link esterno |
| Puntino separatore nelle etichette | "A · B" ripetuto | una frase con la virgola |
| Dissolvenze, contatori che salgono, rimbalzi, fascio sul cursore | uno (vietati) | in Elementor nessun "Animazione d'ingresso" e nessun effetto di movimento |
| Hover che sbiadisce, freccia che si sposta | `opacity` nell'hover (vietato) | cambio di colore pieno |
| Titolo in due frasi col punto ("X. Y.") | più di 1 titolo col punto; nessuno in due frasi | titolo descrittivo senza punto |
| "Non solo X, ma Y", "non è X, è Y" | uno | dire la cosa |
| Regola del tre | tre aggettivi o verbi ornamentali in fila | uno solo, o i fatti (tre lavorazioni vere vanno bene) |
| Parole da brochure | eccellenza, passione, soluzioni, innovazione, a 360°, leader, know-how, mission, "è importante sottolineare" (vietato) | misure, nomi, luoghi, date |
| Didascalia con la fonte | "foto della brochure", "servizio fotografico Booking" | luogo e anno, o niente; la fonte nel LEGGIMI |
| Didascalia dell'ovvio in maiuscolo | "VASCA RETTANGOLARE SOLLEVATA CON L'AUTOGRU" | niente, o luogo e anno |
| Lo stesso invito ripetuto | lo stesso bottone 3 o più volte in home | un invito e il telefono a vista |
| Trattino lungo | U+2014 anche una volta (vietato) | virgola, due punti, punto |

---

## f. Soglie misurabili e come si misura

```
_metodo/kit/segnali.sh <url> <cartella-uscita> [nome]
_metodo/kit/segnali.sh GardensPav-Sito/_prova/build/anteprima/01-home.html /tmp/segnali gardenspav
_metodo/kit/segnali.sh http://127.0.0.1:8090/ /tmp/segnali home-wp
```

Il comando (copia anche in `scratchpad/kit/`) lancia `misura-segnali.cjs` a 1440, lo stesso script della ricerca, che scrive
`<nome>-1440-info.json`, `-top.png` e la pagina intera `<nome>-1440.png`; poi `segnali-soglie.cjs` misura il resto, stampa
una riga per soglia ("OK" o "DA CORREGGERE" con il valore), scrive `<nome>-1440-soglie.json` ed esce con 1 se una soglia
non passa (2 se la pagina non si apre). Un percorso locale diventa `file://`. Si misura l'anteprima HTML e poi il WordPress:
le animazioni d'ingresso di Elementor si vedono solo lì.

| # | Soglia (home a 1440) | Come la misura lo script |
|---|---|---|
| 1 | area foto almeno 35 % | celle di 20 px coperte da img, video, iframe e sfondi con immagine più grandi di 120 px |
| 2 | una famiglia o superfamiglia, nessuna della lista b | quota di testo per famiglia (da 2 %), raggruppate per la prima parola del nome; lista b sul testo principale, sui titoli e su ogni famiglia da 10 % |
| 3 | monospazio 0 % | famiglie con mono, code, courier, consol, menlo nel nome |
| 4 | al massimo 1 etichetta maiuscola sopra un titolo | testo maiuscolo fino a 15,5 px e 70 caratteri, entro 100 px sopra un h1-h3, fuori da menu, link e piede; quelle con cifre (date, codici) non contano |
| 5 | al massimo 1 titolo col punto; nessuno in due frasi; nessun "non solo ... ma" | h1-h3 e testo visibile |
| 6 | almeno 3 misure di H2 | corpi distinti degli H2 visibili |
| 7 | al massimo 4 fasce di fondo | colore pieno largo almeno il 95 % della finestra e alto più di 200 px; le foto interrompono ma non contano. Approssimata: guardare lo screenshot |
| 8 | al massimo 1 sezione con titolo a sinistra e paragrafo a destra | H2 più stretto del 62 % con un paragrafo di 80 caratteri alla sua destra |
| 9 | meno di 30 filetti | bordi superiori o inferiori da 1-2 px su elementi larghi più di 200 px |
| 10 | al massimo 2 frecce | caratteri → ↗ › » nel testo |
| 11 | al massimo 1 numero grande | testo di sole cifre e unità da 40 px in su |
| 12 | numerazioni solo per una procedura | voci 01, 02...: oltre 2 è DA CORREGGERE; se sono passi veri si tengono e si scrive perché nel LEGGIMI |
| 13 | nessuna tabella oltre 4 righe | righe delle tabelle visibili |
| 14 | didascalie senza la fonte | "foto/immagine ... brochure, scheda, Booking, catalogo, sito, pdf", "fonte:" |
| 15 | almeno un contenuto datato o con nome | date e anni 1950-2039 fuori dal piede e dalle righe legali; i nomi di persona si guardano a occhio |
| 16 | divieti | U+2014, emoji nei titoli, gradienti e testo in gradiente, backdrop-filter, bordo solo a sinistra, svg Lucide, classi d'ingresso (elementor-invisible, animated, aos), `:hover` con opacity, parole da brochure; corsivo serif, tre box e badge a occhio |

Una pagina è pronta quando `segnali.sh` esce con 0 e lo screenshot guardato a pezzi (`slice.py`) non mostra i segnali della
tabella e che lo script non vede (palette, hero a due bottoni, didascalie dell'ovvio, testi).

**Esiti delle prove del 6 ottobre 2026** (uscite complete nella cartella di lavoro `scratchpad/guida-car/segnali/`):

| Pagina | Esito | Soglie DA CORREGGERE, con il valore misurato |
|---|---|---|
| Benvegnù, `BenvegnuSrl-Sito/anteprima/01-home.html` | 4 su 16, uscita 1 | 4 etichette sopra i titoli: 2 ("DAL CATALOGO", "PER CHI LAVORIAMO"); 7 fasce: 6; 9 filetti: 43; 10 frecce: 13. Passano: foto 40,2 %, Barlow 85 % e Barlow Condensed 15 %, mono 0 %, 5 misure di H2, 1 titolo a sinistra ("IL CATALOGO"), 1 numero grande ("329"), una data (1980) |
| Gardens Pav, `GardensPav-Sito/_prova/build/anteprima/01-home.html` | 11 su 16, uscita 1 | 1 foto 9,6 %; 2 IBM Plex Mono 22,5 % (lista b); 3 mono 22,5 %; 4 etichette 5; 5 titoli col punto 5 su 13, 2 in due frasi; 6 H2 una misura (42 px); 7 fasce 8; 9 filetti 97; 10 frecce 7; 11 numeri grandi 2 ("0,88", "0,40"); 13 tabella di 9 righe. Passano: 1 titolo a sinistra, nessuna numerazione, didascalie, una data, divieti |
| Wirmec, `Wirmec-Sito/_prova/build/anteprima/01-home.html` (in più) | 10 su 16, uscita 1 | 1 foto 15,7 %; 2 IBM Plex Sans e Condensed (lista b); 3 mono 9,4 %; 6 H2 due misure; 7 fasce 8; 8 titolo a sinistra in 2 sezioni; 9 filetti 51; 10 frecce 20; 12 numerazione di 9 voci; 14 "W 1500, foto della brochure Wirmec." |

I valori coincidono con quelli della ricerca (segnali-ia 5.1), salvo le etichette: lo script conta solo quelle sopra un
titolo, non i menu e i bottoni.

---

## g. Note per i siti già avviati

**Gardens Pav** (11 soglie su 16). In ordine di effetto: (1) foto delle realizzazioni grandi, almeno un terzo della home:
le migliori a 1600 px sono Altivole, Pistoia, San Lazzaro, Milano, Cornate d'Adda, Aosta; (2) via IBM Plex Mono: o Archivo
da solo con le sue cifre tabellari, o la tipografia del settore (c2: Jost come Mutina, nella tavola 02 con i contenuti di
Gardens Pav); non Chivo, che è della stessa fonderia; (3) via i capi "a cartella" e due terzi dei filetti, una sola etichetta;
(4) titoli senza punto, H1 in una frase; (5) in home una tabella di 4 righe al massimo, il resto nelle schede; (6) quattro
fasce al massimo e H2 di tre misure.

**Wirmec** (10 su 16). IBM Plex è nella lista b: la strada è c1 (Hanken Grotesk come WEIMA, tavola 01 con i testi e le foto
di Wirmec); se si tiene Plex, almeno via Plex Mono (9,4 %) con `tabular-nums` nel Sans. Poi: via le 20 frecce (resta
quella di "Brochure in PDF") e i 6 trattini rossi sotto i titoli; via la numerazione 01-12 delle lavorazioni, che non sono una
sequenza; una sola sezione con titolo a sinistra; didascalie con luogo o macchina, non "foto della brochure"; la postazione
AM600 Vantage (1600 px) o un reparto a tutta larghezza.

**Benvegnù** (4 su 16), il sito giudicato "molto meglio": regge su foto al 40 %, una superfamiglia e cinque misure di titoli.
Residui da togliere: le etichette con il trattino davanti ("DAL CATALOGO", "PER CHI LAVORIAMO", e "RIVENDITORE AUTORIZZATO
VIBRAM" sopra il 329), 13 frecce, 43 filetti (contatti a quattro colonne e piede), 6 fasce, la barra rossa del carosello. Il
"329" e "IL CATALOGO" a sinistra sono al limite (uno ciascuno): si tengono solo se sono la cosa per cui il cliente viene
scelto. Barlow resta di Benvegnù e non si ripropone.

**Albergo Vescovi.** Scelta "Abete": Source Serif 4 600 per i titoli e Schibsted Grotesk per il testo (02, paragrafo 4).
Nessuna delle due è nella lista b, ma Source Serif 4 è la sorella di Source Sans 3, che lo è: il testo resta in Schibsted.
Da correggere prima del prototipo: titoli in 400, non 600 (gli alberghi alpini di riferimento usano regolare o leggero:
Schwarzschmied, Milla Montis, Forestis); "CAMERE" e "BENESSERE" in maiuscolo vanno bene come titoli, non come etichette sopra
un altro titolo; via le didascalie con "Servizio fotografico della scheda Booking.com"; bottoni ad angoli quasi vivi, non a
pillola; Newsreader (accoppiata B) è nella lista b e resta fuori. La tavola 03 mostra le alternative del settore con i testi e
le foto del Vescovi (Spectral come Schwarzschmied, Petrona per un albergo di città come il Garibaldi, Belleza e Cabin per i
rifugi). I prototipi `_prova/direzioni/*/proto.html` non esistono ancora: appena ci sono, `segnali.sh` su ognuno.

**Leon d'Oro.** Scelta "Facciata": Libre Franklin 800 maiuscolo per i titoli, 400 e 600 per il testo (02, paragrafo 4).
Libre Franklin non ha cifre tabellari (verificato anche qui): il listino va in righe con il prezzo allineato a destra, come
nella tavola, non in colonne di cifre. L'800 maiuscolo va contro la regola 4: si tiene perché viene dalle scritte della
cartolina e del logo, solo per titoli di una o due parole e con una misura grande per pagina; tutto il resto in 400-600.
La tavola 04 prova il settore sul listino 2026 e sulle foto del Leon d'Oro: se la famiglia preferisce un serif, la strada è
EB Garamond (come Bründlmayer), non Gelasio. Da qui in avanti Libre Franklin è un carattere di casa: non per altri siti.
