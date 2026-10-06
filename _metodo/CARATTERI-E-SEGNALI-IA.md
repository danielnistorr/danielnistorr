# Caratteri e segnali da IA: cosa fare prima di progettare

Guida operativa per chi costruisce i siti della campagna (WordPress, Elementor gratuito, Google Fonts). Si legge prima della
direzione (METODO 2.3) e si usa di nuovo prima di consegnare. Riassume la ricerca del 6 ottobre 2026 in
`_metodo/ricerca-caratteri/`: `censimento-industria-servizi.md` (60 siti), `censimento-ospitalita-cibo.md` (30 siti),
`fonti-tipografiche.md` (fonti di mestiere), `segnali-ia.md` (catalogo dei segnali e misure). Le citazioni tra parentesi
rimandano a quei file; i link alle fonti esterne sono lì. La guida è stata corretta dopo due revisioni indipendenti dello stesso
giorno: l'elenco dei rilievi applicati e respinti è in fondo ("Revisione").

Strumenti: `_metodo/kit/segnali.sh` (misura, paragrafo f) e `_metodo/tavole-caratteri/` (una tavola per settore, paragrafo c).

Perché esiste: il committente ha giudicato i primi siti "IA LIKE". Gardens Pav e Wirmec non hanno i segnali della prima ondata
(viola, Inter, tre box), ma stanno dentro la seconda: monospazio, filetti, etichette, frecce, poche foto (segnali-ia 1). E c'è
una terza trappola, che le prime tavole avevano: pagine bianche, educate e intercambiabili, vestite con il carattere di un
sito di lusso straniero sopra le foto di una piccola azienda veneta. Il carattere si sceglie accanto al logo vero e alle foto
vere del cliente, non al posto loro.

---

## a. Le regole che contano di più, in ordine di effetto

1. **Foto vere, grandi: almeno il 35 % della home a 1440.** È la misura che separa meglio i nostri siti da quelli veri:
   Gardens Pav 9,6 %, Wirmec 15,7 %, Benvegnù 40,2 %. Dei nove riferimenti misurati, otto stanno fra 37 e 63 % (Escofet 63,
   Krone 58, Rieder 55, Trumpf 54, Hirschen 53, Hermle 48, Godelmann 39, Paxmontana 37) e uno, Komax, è al 14,2 %: l'unica
   eccezione (segnali-ia 5.1). Senza foto la pagina si riempie di tipografia, filetti e numeri, cioè dell'aspetto "IA"
   (segnali-ia 4.7, I1). Prima di impaginare: chiedere o fare le foto; una foto prende metà schermo, e le foto vanno a filo,
   non chiuse in riquadri con il margine. La foto peggiore non va mai in apertura (postazioni scontornate, piatti col
   telefono, luci colorate delle cabine).
2. **Una famiglia, o una superfamiglia; un secondo carattere solo con un compito fisso.** Industria e servizi: 16 siti di
   riferimento su 30 usano una famiglia, 12 ne usano due, uno tre; l'unico con quattro (Ezra) è anche quello col corsivo
   d'accento colorato. Ospitalità e cibo: 9 una, 17 due, 3 tre e Il Pellicano quattro, sempre con ruoli fissi (censimenti,
   "In breve" e "I numeri del censimento"). Il secondo carattere fa una cosa sola: i titoli, oppure i nomi delle collezioni,
   oppure i menu. Mai due caratteri nello stesso paragrafo (Butterick, fonti 1.2).
3. **Niente monospazio da programmazione.** 14 riferimenti su 15 misurati non hanno mono; l'unico (Escofet) usa il mono
   della sua superfamiglia per menu e luoghi, sotto foto al 63 %. Gardens Pav ha il 22,5 % del testo in IBM Plex Mono e 57
   etichette maiuscole tutte in mono; Wirmec il 9,4 % (segnali-ia 4.1, T2). Nei 30 siti di ospitalità il mono compare 4
   volte: tre caratteri da macchina da scrivere (Prestige Elite, Cutive Mono, Pitch Sans) e un grottesco mono (Maison Neue
   Mono a Cervo), mai JetBrains, Fira Code o Plex Mono. I numeri tecnici si allineano con le cifre tabellari del carattere di
   testo (`font-variant-numeric: tabular-nums`).
4. **Titoli leggeri o regolari, non neri, salvo due casi dichiarati.** 22 siti di riferimento su 30 fanno i titoli grandi
   in peso 200-500 (sbp 200 a 110 px, Q-Industrial 300 a 80 px, Salvatori e Dinesen 300, TRUMPF Light, Hadrian 400; WEIMA
   ha le parole grandi dell'apertura in 400 a 130 px e l'h1 in 500); nei siti generici prevalgono 600-900 (Unox Montserrat
   900, IMA e Vention Inter 600). Nell'ospitalità il grassetto vero nei titoli compare in 3 siti su 30. I due casi: le
   macchine, dove i riferimenti del settore fanno i titoli in 700 (Festool DIN 700, Komax Helvetica Now 700, Metzner Frutiger
   700 maiuscolo), e il Leon d'Oro, dove l'800 maiuscolo viene dalla cartolina e dal logo. In tutti e due i casi titoli
   brevi, spaziatura da -0,01em in giù sotto il maiuscolo, una misura grande per pagina. Titoli grandi con interlinea
   0,9-1,2 e spaziatura da -0,01 a -0,04em (censimento industria, "Cosa distingue i siti migliori").
5. **Niente "vestito da scheda tecnica".** Il contenuto dei nostri siti è buono (misure, norme, nomi); il problema è che
   ogni dato porta lo stesso vestito: etichetta mono maiuscola, filetto, freccia. Filetti larghi, misurati nella ricerca:
   Gardens Pav 97, Wirmec 51, Benvegnù 43, riferimenti 0-30 (mediana 9). Con lo strumento corretto (paragrafo f), che non
   conta gli elementi fuori dalla finestra e i campi dei moduli: Gardens Pav 97, Wirmec 51, Benvegnù 27, Rieder 0, Mutina 3,
   Hermle 4, Trumpf 7. Frecce scritte: Wirmec 20, Benvegnù 13, Gardens Pav 7, riferimenti 0-2. In home: una frase con due o
   tre dati per prodotto, le tabelle nelle schede (Komax, Hermle, Trumpf: nessuna tabella in home). Lo spazio separa; il
   filetto solo dentro una tabella vera (segnali-ia 4.3, L3, K2, D2). Una tabella in home solo dove il dato è il prodotto:
   le misure delle vasche, i modelli delle macchine, il listino di un albergo; per camere, atelier, orari e appartamenti
   righe brevi o schede con la foto.
6. **Almeno un contenuto con una data o un nome.** È il segnale umano più forte dei riferimenti: fiera con date, città e
   stand (Zünd, Kortrijk 4-6 ottobre 2026, stand 4151), storia di un cliente con nome (Komax, Confecta), evento con giorno e
   orario (Paxmontana), cantiere con città e anno, la data da cui un appartamento è libero. Un modello non lo inventa; noi non
   dobbiamo inventarlo: lo prendiamo dal sito, dai social o dal cliente, e se manca va nel LEGGIMI tra le cose da chiedere
   (segnali-ia 6).
7. **Un solo elemento davvero grande.** Il titolo d'apertura da 90 px in su a 1440, oppure una foto a tutta larghezza con il
   titolo sopra; Benvegnù ha "VIENI AL BANCO" a 144 px sulla foto (segnali-ia T6). Gardens Pav ha tutti gli H2 a 42 px,
   Wirmec a 48. Più misure di H2 aiutano, ma non sono una regola: Rieder e Hermle hanno una misura sola di H2, Mutina una o
   due, e reggono con le foto. Per questo la soglia degli H2 è "da guardare" (paragrafo f).
8. **Poche fasce di fondo, di altezze diverse.** I nostri siti hanno 6-8 cambi di fondo quasi uguali; Escofet, Komax e
   Muottas Muragl 2. Ma anche Rieder ne ha 10, Hermle 6, Zünd e Mall 5 (segnali-ia 5.1): le fasce disturbano quando sono
   uguali e si alternano senza foto. Un fondo per quasi tutta la pagina e un cambio deciso, il campo nel colore della casa,
   oppure fasce date dalle foto.

Regola d'insieme: un segnale isolato si tiene se ha una ragione; due nella stessa schermata si correggono (Hallmark, F6).

---

## b. Caratteri da non usare come voce principale

"Voce principale" vuol dire il carattere del testo (più metà della pagina) o dei titoli. Il problema non è il carattere ma
il default: gli stessi nomi, scelti con una ragione, stanno in lavori pubblicati (fonti 3.6). Qui però si parte senza.

Criterio: va in lista b un carattere che è di serie in un modello, una piattaforma o un tema, oppure che un generatore offre
nel suo selettore accanto a Inter, oppure che i prompt "anti IA" e le liste SEO 2026 propongono al posto di Inter in più di
una fonte. Va nella lista di attenzione un carattere che compare in una sola lista SEO o in una variante di tema non di
serie: si usa solo con il suo riferimento e vestito come il riferimento, mai come risposta per tutto. Le classifiche di
Typewolf misurano l'uso tra i designer, non tra i generatori: le citiamo come nota, non come prova.

**Prima ondata: i default dei modelli, delle piattaforme e dei temi.**

| Caratteri | Motivo | Fonte |
|---|---|---|
| Inter, Inter Tight | "Almost always Inter is their primary type choice"; vietato dal committente | Pimp my Type 2026; 925Studios (fonti 1.5; segnali-ia F12) |
| Roboto, Roboto Slab | default del kit globale di Elementor (Roboto 600 primario, Roboto Slab 400 secondario, Roboto 400 testo, Roboto 500 accento) e Google Font più richiesto del web | `global-typography.php` di Elementor; Web Almanac 2025 (fonti 3.1, 3.2) |
| Open Sans, Lato, Arial | "Never use" nel cookbook Anthropic: sono la media del web | cookbook Anthropic (fonti 3.4) |
| Poppins, Montserrat | secondo e quarto Google Font più diffusi; "Montserrat is horribly overused" | Web Almanac 2025; Pimp my Type (fonti 1.5, 3.2) |
| Cardo, Instrument Sans (con Inter) | WordPress Twenty Twenty-Four (Instrument Sans nelle varianti Ember, Ice, Maelstrom) | `theme.json` e `styles/*.json` (fonti 3.1; cartella `wp-content/themes/twentytwentyfour/assets/fonts`) |
| Manrope, Fira Code | WordPress Twenty Twenty-Five | `theme.json` (fonti 3.1) |
| Geist, Geist Mono | `create-next-app` di Vercel, base di v0 | fonti 3.1; Krebs (segnali-ia F3) |
| Figtree | carattere di serie di Laravel (Breeze 2.x, pagina di benvenuto di Laravel 11: `figtree:400,500,600`) e dei preset di shadcn/ui | verificato da un revisore il 6/10/2026 |

**Seconda ondata: i caratteri che i generatori offrono e che i prompt "anti IA" e le liste 2026 propongono al posto di
Inter**, oggi riconoscibili quanto Inter perché ogni modello li sceglie quando gli si vieta Inter.

| Caratteri | Motivo | Fonte |
|---|---|---|
| Public Sans, Work Sans, Be Vietnam Pro, Epilogue, Lexend, Spline Sans, Noto Serif | i 12 caratteri di Google Stitch sono questi più Inter, Manrope, Newsreader, Plus Jakarta Sans e Space Grotesk; Work Sans è anche 5ª nel Typewolf 2026 e in muz.li | steegle.com/ai/insights/stitch (letto il 6/10/2026) |
| EB Garamond, Lora, Merriweather, Nunito Sans, Raleway, Noto Sans, Oxanium | preset dei temi di shadcn/ui, accanto a Inter, Geist, DM Sans, Playfair e Figtree; EB Garamond anche in madegooddesigns | `apps/v4/lib/font-definitions.ts` di shadcn/ui |
| Space Grotesk, Space Mono, JetBrains Mono | coppie "tecniche" consigliate ai modelli; Space Grotesk anche negli Awwwards recenti (INTECH) | cookbook Anthropic; Krebs (segnali-ia F1, F3); censimento industria |
| IBM Plex (Sans, Condensed, Serif, Mono) | "Technical: IBM Plex family" nel cookbook; Plex Mono "generico e abusato" | cookbook (fonti 3.4); Kucharski (segnali-ia F11); è Wirmec e il mono di Gardens Pav |
| Playfair Display, Fraunces, Crimson Pro, Newsreader, Source Sans 3 | lista "Distinctive" e "Editorial" che Anthropic dà ai suoi modelli | cookbook e blog Anthropic (segnali-ia F1; fonti 3.4) |
| Instrument Serif, Syne, Bricolage Grotesque | "font da template" misurati su 1.590 pagine; Instrument Serif col corsivo d'accento | Krebs (segnali-ia F3); Vadgama (fonti 3.4) |
| DM Sans, DM Serif Display, Plus Jakarta Sans, Outfit, Sora, Unbounded, Cormorant Garamond | liste SEO 2026 copiate dai generatori e coppie "Playfair + Inter", "Cormorant + Montserrat" | madegooddesigns, muz.li (fonti 3.3, 3.5) |
| Satoshi, Clash Display, Cabinet Grotesk (Fontshare) | stile "Startup" del cookbook; Satoshi negli Awwwards 2026 (SkyClinics) | fonti 3.4; censimento industria |

**Lista di attenzione**: si usano solo dove la guida li mette, con il riferimento indicato.

| Carattere | Dove compare | Nella guida |
|---|---|---|
| Jost | varianti di stile di Twenty Twenty-Four (Ember, Ice, Maelstrom); tema Shopify di serie di Alajmo | c2, per Gardens Pav |
| Hanken Grotesk | lista madegooddesigns 2026 | c1, alternativa per Wirmec |
| Spectral | muz.li; 26ª nel Typewolf 2026 | c3, per Hotel Garibaldi |
| Albert Sans | lista madegooddesigns 2026 | c7, per Tutto Affitti |
| Alegreya Sans | 11ª nel Typewolf 2026 (solo nota) | c4, con Fanwood Text |
| Noto Serif Display | parente di Noto Serif, che sta in Stitch e in shadcn | c5, solo titoli grandi |
| Literata, Familjen Grotesk, Chivo | Literata nelle varianti di Twenty Twenty-Five; Familjen in madegooddesigns; Chivo 34ª nel Typewolf | non più nella guida |

Nessuna prova di moda trovata dai revisori per Sofia Sans, Prata, Golos Text, Petrona, Gelasio, Fanwood Text, Hind e Libre
Caslon Display; Libre Franklin e Kumbh Sans non sono in nessuna delle liste lette.

**Tic di casa, da non riproporre come prima scelta:** Archivo con IBM Plex Mono (Gardens Pav), IBM Plex intera (Wirmec),
Barlow e Barlow Condensed (Benvegnù), Source Serif 4 con Schibsted Grotesk (Albergo Vescovi), Libre Franklin (Leon d'Oro, dove
resta la scelta del cliente). Gelasio torna in sei confronti del censimento ospitalità: la guida la usa una volta sola (c3).

**Riferimenti con un carattere della lista b.** Zünd (IBM Plex Sans al 97,2 % del testo) e Hermle (Roboto all'81,8 %) sono
riferimenti per l'impaginazione e i contenuti (la fiera con le date, le categorie in foto), non per il carattere: `segnali.sh`
dà a Hermle la soglia 2 da correggere, ed è giusto, perché noi partiamo senza la loro ragione.

Controllo: `segnali.sh` segnala come DA CORREGGERE (soglia 2) ogni carattere della lista b che fa il testo principale, i
titoli o almeno il 10 % del testo; riconosce anche i nomi con suffissi ("Inter Variable", "Satoshi-Variable", i nomi generati
da next/font).

---

## c. Scelte per i sette settori

Ogni settore ha una scelta raccomandata e, dove c'è un riferimento misurato, una o due alternative; ogni scelta è pensata per
un'azienda della campagna e la tavola la mostra con i testi, le foto e il logo di quell'azienda. Nessuna famiglia si ripete
tra settori (Hind fa il testo di tutte e due le scelte del settore salute). Tutte le famiglie sono nell'elenco dei Google
Fonts di Elementor 4.3.3 (`includes/fonts.php`, verificato); le righe `family=` sono state chiamate sull'API css2 di Google il
6 ottobre 2026 dopo la revisione e rispondono tutte 200 con i pesi chiesti; le cifre tabellari sono state lette nei file
serviti. La riga `family=` è quella da mettere nell'URL `https://fonts.googleapis.com/css2?family=...&display=swap` e carica
solo i pesi che i ruoli usano.

Come leggere le scale: `famiglia peso · px a 1440/1024/390 · interlinea · spaziatura in em`; `MAIUSC.` solo dove il maiuscolo
è previsto. Display: il titolo d'apertura della home o il nome di una collezione, una volta per pagina. h1: il titolo delle
pagine interne. Il paragrafo d'apertura usa la misura dell'h3 (più 1 px) con il peso del testo. Etichetta: menu, bottoni,
intestazioni di tabella; il menu è in minuscolo salvo dove il riferimento lo fa maiuscolo (Schwarzschmied, Frankel). Le
misure a 1024 valgono per il tablet; quelle a 390 per il telefono. In Elementor: Impostazioni del sito, Tipografia globale,
con i valori per desktop, tablet e mobile.

### c1. Macchine e industria

Tavola: `tavole-caratteri/01-macchine.html` (testi, foto e logo di Wirmec).

- **Raccomandata, per Wirmec: Sofia Sans.** `family=Sofia+Sans:ital,wght@0,400;0,600;0,700;1,400`. Riferimento: Festool (festool.com), elettroutensili; Metzner (metzner.com), macchine per tagliare e spelare cavi, sito fatto con WordPress; carattere originale FF DIN (Festool), Frutiger 47 Light Condensed (Metzner): impianto DIN con più calore e cifre tabellari. Festool, misurato dal vivo: titoli DIN 700 a 43/52,8 px in minuscolo, testo 400 18/24, una famiglia. Metzner, concorrente diretto di Wirmec: una famiglia per il 97,5 % del testo, titoli 700 maiuscoli a 50 px, testo Light 20,8/31,2. Nel settore macchine i titoli in 700 sono la regola dei riferimenti (Festool, Komax, Metzner): qui la regola a.4 non vale. Numeri: tnum nel file Google: font-variant-numeric: tabular-nums. Non fare: Sofia Sans Condensed o Semi Condensed accanto (rifà lo schema Barlow + Barlow Condensed di Benvegnù); titoli in maiuscolo lunghi; spaziatura zero sui titoli in 700 sopra i 40 px.
- **Alternativa 1, per Wirmec (applicatori e presse da banco): Hanken Grotesk.** `family=Hanken+Grotesk:ital,wght@0,400;0,500;1,400`. Riferimento: WEIMA Maschinenbau (weima.com), trituratori e presse, Awwwards Site of the Day; carattere originale Okomito (Hanken Design Co.): stesso disegnatore (Alfredo Marco Pradil); altezza x 0,493 contro 0,512, terminali piatti. WEIMA, misurato dal vivo: le parole grandi dell’apertura in 400 a 130 px, l’h1 in 500 a 65 px, testo Light 300 16/24 con +0,2 px, nessun maiuscolo, una famiglia. Numeri: cifre tabellari già di default nel file Google. Non fare: titoli in 600-800; etichette maiuscole; un monospazio accanto; un titolo grande sotto gli 80 px (a 60-90 px Hanken sembra un’interfaccia). Attenzione: è in una lista SEO 2026 (madegooddesigns): regge solo vestita come WEIMA, con un titolo davvero grande.

Uscita dopo la revisione: Chivo (Formlabs, EFLA). Il suo riferimento Supreme non è a licenza libera (punto d, Fontshare); Chivo è della stessa fonderia di Archivo, il carattere di Gardens Pav, ed era la variante più anonima. Una terza scelta arriva solo con un riferimento del settore misurato: Komax (Helvetica Now), concorrente diretto di Wirmec, porta a Instrument Sans e Inter Tight, tutte e due in lista b.

| ruolo | Sofia Sans | Hanken Grotesk |
|---|---|---|
| display | Sofia 700 · 96/76/48 · 0,98 · -0,02 | Hanken 400 · 128/88/52 · 0,94 · -0,035 |
| h1 | Sofia 700 · 64/52/36 · 1,02 · -0,015 | Hanken 500 · 64/50/36 · 1,04 · -0,02 |
| h2 | Sofia 700 · 44/36/30 · 1,08 · -0,01 | Hanken 500 · 42/34/28 · 1,1 · -0,015 |
| h3 | Sofia 600 · 22/21/20 · 1,25 · 0 | Hanken 500 · 22/21/20 · 1,3 · 0 |
| testo | Sofia 400 · 19/18/17 · 1,5 · 0 | Hanken 400 · 18/17/17 · 1,55 · 0 |
| piccolo | Sofia 400 · 15/15/14 · 1,4 · 0 | Hanken 400 · 15/15/14 · 1,45 · 0 |
| etichetta | Sofia 600 · 16/16/15 · 1,2 · 0 | Hanken 500 · 16/16/15 · 1,2 · 0 |

### c2. Materiali, edilizia ed esterni

Tavola: `tavole-caratteri/02-materiali.html` (testi, foto e logo di Gardens Pav, Marmi Sgambaro).

- **Raccomandata, per Gardens Pav: Jost.** `family=Jost:ital,wght@0,400;0,500;1,400`. Riferimento: Mutina (mutina.it), piastrelle; Werner Sobek (wernersobek.com), ingegneria strutturale; carattere originale Futura PT (Mutina), Futura T (Werner Sobek): Jost è disegnata su Futura (a e g a un piano, maiuscole geometriche), e il logo GARDENS-PAV è un geometrico della stessa famiglia di forme. Mutina, misurato dal vivo: titoli 400 a 58/69,6, testo 16/32 e 18/21,6, menu Futura 700 maiuscolo a 15 px. Werner Sobek: titoli in Futura Demi. Qui titoli in 500, fra i due: a 400 Jost è leggero, da arredo. Numeri: tnum nel file Google. Non fare: titoli in grassetto; maiuscolo per frasi intere; testo sotto 17 px (altezza x 0,46); menu maiuscolo spaziato. Attenzione: è nelle varianti di stile di Twenty Twenty-Four (Ember, Ice, Maelstrom) e nei temi Shopify di serie (Alajmo): regge solo con il logo geometrico di Gardens Pav e foto di cantiere grandi.
- **Alternativa 1, per Marmi Sgambaro: Prata + Golos Text.** `family=Prata&family=Golos+Text:wght@400;500;600`. Riferimento: Rieder (rieder.cc), pannelli di facciata in calcestruzzo fibrorinforzato; clienti architetti, come quelli di Sgambaro; carattere originale PP Grafier Display + Tomato Grotesk: Prata è la gratuita più vicina a Grafier (alto contrasto, grazie a cuneo); Golos Text ha le proporzioni di Tomato. Rieder, misurato dal vivo: Tomato Grotesk per il 93,5 % del testo, Grafier solo per pochi titoli grandi sulla foto. Qui Prata fa solo i nomi delle pietre e i titoli, come un cartellino di campionario. Numeri: solo in Golos Text (tnum); Prata ha cifre proporzionali. Non fare: Prata sotto 28 px, per frasi lunghe o in corsivo (non esiste: font-synthesis: none); misure e spessori in Prata.

Uscita dopo la revisione: Public Sans (Salvatori, Dinesen), passata in lista b (è tra i 12 caratteri di Google Stitch e nei preset di shadcn). Per Zoccarato Serramenti e Acquatest manca ancora un riferimento del settore misurato.

| ruolo | Jost | Prata + Golos Text |
|---|---|---|
| display | Jost 500 · 116/84/50 · 0,98 · -0,02 | Prata 400 · 104/76/46 · 1 · -0,01 |
| h1 | Jost 500 · 60/48/34 · 1,06 · -0,01 | Prata 400 · 60/48/34 · 1,08 · -0,005 |
| h2 | Jost 500 · 42/34/28 · 1,12 · -0,005 | Prata 400 · 42/34/30 · 1,12 · 0 |
| h3 | Jost 500 · 22/21/20 · 1,3 · 0 | Golos 600 · 20/20/19 · 1,3 · 0 |
| testo | Jost 400 · 19/18/17 · 1,65 · 0 | Golos 400 · 18/17/17 · 1,55 · 0 |
| piccolo | Jost 400 · 15/15/15 · 1,5 · 0 | Golos 400 · 15/15/14 · 1,45 · 0 |
| etichetta | Jost 500 · 16/16/15 · 1,2 · 0 | Golos 500 · 16/15/15 · 1,2 · 0 |

### c3. Hotel di montagna e di città

Tavola: `tavole-caratteri/03-hotel.html` (testi, foto e logo di Albergo Vescovi, Hotel Garibaldi).

- **Raccomandata, per Albergo Vescovi, Asiago: Petrona.** `family=Petrona:ital,wght@0,400;0,500;1,400`. Riferimento: Il Palazzo Experimental (experimentalgroup.com), Venezia; carattere originale Nantes: serif con le stesse irregolarità di Nantes (x 0,443 contro 0,473), caldo e pieno anche a 18 px. Experimental: Nantes per il 79 % del testo, titoli da 32 a 120 px con interlinea 1,1-1,2. Una famiglia per tutto: titoli 500, testo 400, menu in minuscolo. Numeri: tnum nel file Google. Non fare: Newsreader al suo posto (lista b); una parola in corsivo nel titolo; titoli sotto il 400.
- **Alternativa 1, per Hotel Garibaldi, Padova: Spectral.** `family=Spectral:ital,wght@0,400;0,500;1,400`. Riferimento: Hotel Schwarzschmied (schwarzschmied.com), Lana; Arup (arup.com) usa Spectral stesso per i titoli; carattere originale Livory (Schwarzschmied): misure vicine a Livory: x 0,450 contro 0,464, larghezza 0,502 contro 0,513, contrasto 2,1 contro 2,0. Schwarzschmied, misurato dal vivo: Livory h1 72/82 e menu maiuscolo a +0,15em; il 51 % del testo della home è però Novel Sans 600 maiuscolo a 15 px (menu, offerte, indirizzo). Per un albergo di città Spectral si usa in 400 e 500: in 300 sembra un libro. Numeri: cifre tabellari già di default. Non fare: peso 300; fondo crema con accento terracotta; parole in corsivo nei titoli. Attenzione: è nelle liste di muz.li e al 26° posto del Typewolf 2026: non va usata come risposta per ogni albergo.
- **Alternativa 2, per Albergo Vescovi (il ristorante) e le locande dell’Altopiano: Gelasio.** `family=Gelasio:ital,wght@0,400;0,500;1,400`. Riferimento: Hotel Waldhaus Sils (waldhaus-sils.ch), albergo di famiglia alla quinta generazione, riferimento già scelto nel 02 di Albergo Vescovi; carattere originale Larken (titoli): il censimento la dà come la più vicina a Larken (curve morbide, proporzioni vicine). Waldhaus Sils, misurato dal vivo: Larken 400 maiuscolo a 76 e 46 px per i titoli, il resto in Inter (che qui non si copia). Qui Gelasio fa titoli e testo, in minuscolo. Numeri: tnum nel file Google; cifre minuscole di default: lining-nums nei prezzi e negli orari. Non fare: usarla come risposta per tutto (torna in sei confronti del censimento: qui e basta); titoli maiuscoli lunghi; corsivo nei titoli.

Uscita dopo la revisione: Belleza + Cabin (Milla Montis): Cabin è datata e senza cifre tabellari, Belleza ha un peso solo. Spectral resta, ma passa all’albergo di città e in 400-500 (in 300 a 72 px sembrava un libro).

| ruolo | Petrona | Spectral | Gelasio |
|---|---|---|---|
| display | Petrona 500 · 104/76/48 · 1 · -0,015 | Spectral 400 · 96/72/46 · 1,02 · -0,015 | Gelasio 500 · 100/74/46 · 1,02 · -0,015 |
| h1 | Petrona 500 · 58/46/34 · 1,06 · -0,01 | Spectral 400 · 56/46/34 · 1,08 · -0,01 | Gelasio 500 · 56/46/34 · 1,08 · -0,01 |
| h2 | Petrona 500 · 40/34/29 · 1,12 · -0,005 | Spectral 400 · 40/34/29 · 1,14 · -0,005 | Gelasio 500 · 40/34/29 · 1,14 · -0,005 |
| h3 | Petrona 500 · 22/21/20 · 1,3 · 0 | Spectral 500 · 22/21/20 · 1,3 · 0 | Gelasio 500 · 22/21/20 · 1,3 · 0 |
| testo | Petrona 400 · 19/18/18 · 1,6 · 0 | Spectral 400 · 19/18/18 · 1,6 · 0 | Gelasio 400 · 18/18/17 · 1,65 · 0 |
| piccolo | Petrona 400 · 15/15/15 · 1,5 · 0 | Spectral 400 · 15/15/15 · 1,5 · 0 | Gelasio 400 · 15/15/15 · 1,5 · 0 |
| etichetta | Petrona 500 · 17/17/16 · 1,2 · 0 | Spectral 500 · 13/13/13 · 1,2 · +0,12 · MAIUSC. | Gelasio 500 · 17/17/16 · 1,2 · 0 |

### c4. Ristoranti, agriturismi, cantine, salumi

Tavola: `tavole-caratteri/04-ristoranti.html` (testi, foto e logo di Leon d’Oro, Salumificio Fontana).

- **Raccomandata, per Albergo Ristorante Leon d’Oro, Este: Libre Franklin.** `family=Libre+Franklin:ital,wght@0,400;0,600;0,800;1,400`. Riferimento: le scritte del Leon d’Oro: la cartolina storica e il logo (scelta "Facciata" del 02); carattere originale lettering della cartolina e del logo, bastoni neri maiuscoli: la scelta viene dal materiale del cliente, non da un sito di lusso: titoli brevi in 800 maiuscolo come la cartolina, il giallo della facciata come campo, il verde delle persiane per il bottone. Numeri: Libre Franklin non ha cifre tabellari: il listino va in righe con il prezzo allineato a destra. Non fare: 800 per titoli di più di tre parole; maiuscolo nel testo; un serif accanto.
- **Alternativa 1, per Salumificio Fontana, Este: Fanwood Text + Alegreya Sans.** `family=Fanwood+Text:ital@0;1&family=Alegreya+Sans:ital,wght@0,400;0,500;1,400`. Riferimento: Manincor (manincor.com), cantina, Caldaro; carattere originale Cochin + Corporate S: Fanwood Text ha x 0,385 contro 0,372 e lo stesso rapporto x/maiuscola di Cochin (0,573 contro 0,569); Alegreya Sans ha la larghezza di Corporate S (0,445 contro 0,447). Manincor: Cochin a 90 e 46 px, testo in Corporate S, occhielli a +3 px. Un serif d’archivio per un’azienda del 1941 con le foto in bianco e nero. Numeri: solo in Alegreya Sans (tnum), con lining-nums: di default le cifre minuscole sono anche in Fanwood Text e in Alegreya Sans. Non fare: Fanwood sotto 26 px o in grassetto (un peso solo); prezzi e date in Fanwood. Attenzione: Alegreya Sans è all’11° posto del Typewolf 2026: va con Fanwood, non da sola.

Uscite dopo la revisione: EB Garamond (Bründlmayer), passata in lista b (preset di shadcn, lista madegooddesigns), e Questrial (Poli: un peso solo, un geometrico freddo). Per le cantine (Cantina Dotto, Villa Pollini) manca un riferimento: Bründlmayer porta a EB Garamond e Cardo, tutte e due in lista b; Ornellaia (Tobias) porta a Gelasio, già usata negli alberghi.

| ruolo | Libre Franklin | Fanwood Text + Alegreya Sans |
|---|---|---|
| display | Franklin 800 · 84/64/42 · 1 · 0 · MAIUSC. | Fanwood 400 · 96/72/46 · 1,02 · -0,01 |
| h1 | Franklin 800 · 56/46/34 · 1,04 · 0 · MAIUSC. | Fanwood 400 · 56/46/34 · 1,08 · -0,005 |
| h2 | Franklin 800 · 40/34/28 · 1,08 · 0 · MAIUSC. | Fanwood 400 · 42/34/30 · 1,12 · 0 |
| h3 | Franklin 600 · 22/21/20 · 1,3 · 0 | Alegreya Sans 500 · 21/20/19 · 1,3 · 0 |
| testo | Franklin 400 · 18/18/17 · 1,6 · 0 | Alegreya Sans 400 · 19/19/18 · 1,55 · 0 |
| piccolo | Franklin 400 · 15/15/15 · 1,5 · 0 | Alegreya Sans 400 · 16/16/15 · 1,45 · 0 |
| etichetta | Franklin 600 · 16/16/15 · 1,2 · 0 | Alegreya Sans 500 · 17/17/16 · 1,2 · 0 |

### c5. Moda, sposa, fiori, gioielli

Tavola: `tavole-caratteri/05-moda.html` (testi, foto e logo di rosyGarbo).

- **Raccomandata, per rosyGarbo, atelier sposa, Padova: Noto Serif Display + Kumbh Sans.** `family=Noto+Serif+Display:wght@300&family=Kumbh+Sans:wght@300;400`. Riferimento: Danielle Frankel Studio (daniellefrankelstudio.com), abiti da sposa, New York, riferimento del 02 di Rosy Garbo; le testate delle collezioni di Rosy Garbo; carattere originale Canela Light (Frankel); senza grazie sottile maiuscolo delle testate ("venice VENEZIA"): Frankel, misurato dal vivo: un solo serif dritto e leggero (Canela Light) per il 99 % del testo, titoli in minuscolo, menu maiuscolo a 12 px con +1,5 px. Noto Serif Display in 300 ha la stessa luce, con grazie affilate e alto contrasto. I nomi delle collezioni in Kumbh Sans 300 maiuscolo, come le testate che Rosy Garbo ha già (geometrico sottile); Kumbh fa anche il testo. Numeri: Kumbh Sans non ha cifre tabellari: indirizzi e telefoni in righe brevi. Non fare: maiuscolo nel serif; Noto Serif Display sotto 32 px; corsivo; più di due pesi di Kumbh. Attenzione: Noto Serif Display è parente di Noto Serif, che sta nei selettori di Google Stitch e di shadcn: solo il taglio Display, solo per titoli grandi in minuscolo.

Uscite dopo la revisione: Work Sans (lista b: Google Stitch, 5ª nel Typewolf 2026, muz.li), Literata (il carattere di Google Play Libri, nelle varianti di Twenty Twenty-Five: sembra un e-book) e Bodoni Moda (la scelta "lusso" più prevedibile; in Elementor perde l’asse ottico). Per fiori (Rizzo) e gioielli manca un riferimento: Sophie Buhai, la gioielleria del censimento, usa Univers, che porta a Public Sans e Instrument Sans, tutte e due in lista b.

| ruolo | Noto Serif Display + Kumbh Sans |
|---|---|
| display | Noto Serif D. 300 · 96/72/46 · 1,04 · -0,015 |
| h1 | Noto Serif D. 300 · 58/46/36 · 1,08 · -0,01 |
| h2 | Noto Serif D. 300 · 44/36/32 · 1,12 · -0,005 |
| h3 | Kumbh 300 · 24/22/20 · 1,2 · +0,12 · MAIUSC. |
| testo | Kumbh 400 · 17/17/16 · 1,7 · +0,01 |
| piccolo | Kumbh 400 · 14/14/14 · 1,55 · +0,01 |
| etichetta | Kumbh 400 · 13/13/13 · 1,2 · +0,12 · MAIUSC. |

### c6. Salute e servizi alla persona

Tavola: `tavole-caratteri/06-salute.html` (testi, foto e logo di Oltreoceano, Centro Dentale Vanuzzo).

- **Raccomandata, per Oltreoceano, centri sole: Hind.** `family=Hind:wght@400;500;600`. Riferimento: Lanserhof (lanserhof.com), medicina preventiva; TRUMPF (trumpf.com), che usa Frutiger Light in minuscolo per tutto il sito; carattere originale Neue Frutiger World (Lanserhof), Frutiger 45 Light (TRUMPF): impronta Frutiger, il carattere della segnaletica: x 0,508 contro 0,510. Lanserhof: titoli Neue Frutiger 450, testo leggero 16-18 px. Qui in minuscolo, titoli 500: niente maiuscolo spaziato da spa. Numeri: Hind non ha cifre tabellari: orari in righe brevi, uno per riga. Non fare: maiuscolo spaziato nei titoli; un corsivo serif accanto (Lanserhof ha il Frutiger Serif, Hind no); colonne di numeri.
- **Alternativa 1, per Centro Dentale Vanuzzo, Padova: Libre Caslon Display + Hind.** `family=Libre+Caslon+Display&family=Hind:wght@400;600`. Riferimento: Parsley Health (parsleyhealth.com), studi medici; carattere originale Teodor Light (Parsley, titoli): Libre Caslon Display ha l’altezza x bassa e il colore leggero di Teodor. Parsley, misurato dal vivo: titoli 64/71,7 a -0,02em, testo 18/28,8 a -0,02em, nessun corsivo d’accento. Il testo resta in Hind, la stessa voce di servizio di Oltreoceano: lo studio dentistico aggiunge solo i titoli in serif. Numeri: Hind non ha cifre tabellari: orari e telefoni in righe brevi. Non fare: Libre Caslon Display sotto 30 px (non regge); una parola del titolo in corsivo o in colore (Ezra, Dentologie); foto di repertorio.

Uscita dopo la revisione: Gloock + Figtree (One Medical). Figtree è il carattere di serie di Laravel (Breeze 2.x, pagina di benvenuto di Laravel 11) e dei preset di shadcn: lista b. Gloock è un titolo da rivista, nero e pesante. Albert Sans passa alla casa (c7): per Vanuzzo il testo resta in Hind, la voce del settore.

| ruolo | Hind | Libre Caslon Display + Hind |
|---|---|---|
| display | Hind 500 · 92/70/44 · 1,02 · -0,015 | Caslon D. 400 · 96/72/46 · 1,04 · -0,02 |
| h1 | Hind 500 · 56/46/34 · 1,08 · -0,01 | Caslon D. 400 · 60/48/36 · 1,08 · -0,02 |
| h2 | Hind 500 · 40/34/29 · 1,14 · -0,005 | Caslon D. 400 · 46/38/32 · 1,12 · -0,01 |
| h3 | Hind 600 · 20/19/18 · 1,3 · 0 | Hind 600 · 20/19/18 · 1,3 · 0 |
| testo | Hind 400 · 18/18/17 · 1,6 · 0 | Hind 400 · 18/18/17 · 1,6 · 0 |
| piccolo | Hind 400 · 15/15/15 · 1,5 · 0 | Hind 400 · 15/15/15 · 1,5 · 0 |
| etichetta | Hind 600 · 16/16/15 · 1,2 · 0 | Hind 600 · 16/16/15 · 1,2 · 0 |

### c7. Casa e immobiliare

Tavola: `tavole-caratteri/07-casa.html` (testi, foto e logo di Tutto Affitti).

- **Raccomandata, per Tutto Affitti, Villatora di Saonara: Albert Sans.** `family=Albert+Sans:ital,wght@0,300;0,400;0,500;1,300`. Riferimento: Abitare Co. (abitareco.it), progetti immobiliari, Milano; carattere originale Circular Std (testo e dati): Albert Sans ha le proporzioni di Euclid Circular B (x 0,500, larghezza 0,515 contro 0,535), la stessa famiglia di forme di Circular. Abitare Co., misurato dal vivo: Circular Std per il 77 % del testo, testo 300 a 22/30, nomi dei progetti 500 a 24 px, titoli in un serif da display (PP Pangaia) che qui non serve: una famiglia sola. Numeri: Albert Sans non ha cifre tabellari: superficie, prezzo e data in una scheda per appartamento, non in colonna. Non fare: tabelle di appartamenti; titoli sopra il 500; testo in 300 sotto 18 px. Attenzione: è in una lista SEO 2026 (madegooddesigns): regge con le foto vere e le date di disponibilità.

Uscite dopo la revisione: Gelasio + Familjen Grotesk (Audo: insieme fanno un blog; Gelasio passa agli alberghi), Old Standard TT + News Cycle (Heath) e Kumbh Sans (sbp, ingegneria; passa alla moda, c5). Public Sans, proposta da un revisore con Inigo come riferimento, è in lista b, e Inigo misurato dal vivo usa Adobe Caslon per il 65 % del testo, non un grottesco. Per Callegari Tende manca un riferimento del settore misurato.

| ruolo | Albert Sans |
|---|---|
| display | Albert 500 · 112/80/48 · 0,98 · -0,025 |
| h1 | Albert 500 · 60/48/34 · 1,04 · -0,015 |
| h2 | Albert 500 · 42/34/28 · 1,1 · -0,01 |
| h3 | Albert 500 · 22/21/20 · 1,3 · 0 |
| testo | Albert 300 · 20/19/18 · 1,5 · 0 |
| piccolo | Albert 400 · 15/15/15 · 1,45 · 0 |
| etichetta | Albert 500 · 16/16/15 · 1,2 · 0 |

---

## d. Regole d'uso tipografico

- **Quante famiglie.** Una; due se la seconda fa una cosa che la prima non sa fare (titoli, nomi, menu); tre solo con un
  ruolo marginale e fisso. Accoppiare per scheletro, non per etichetta: stessa superfamiglia, stesso disegnatore, oppure
  contrasto netto di scheletro e di contrasto; mai due caratteri simili in superficie e diversi nella costruzione (Poppins
  con Open Sans) (fonti 1.1, 1.5, 4.1).
- **Pesi.** Al massimo tre pesi per famiglia, e ogni peso con un compito: uno per i titoli (lo stesso per apertura, h1 e h2,
  oppure l'apertura un gradino più leggera, come WEIMA: 400 sopra 500), uno per il testo, uno di enfasi per h3, menu e
  bottoni (500 o 600). Mai salti da 100 a 900, la ricetta "salti di 3x" del cookbook che ha creato la seconda ondata (fonti
  4.2, 4.5). Il grassetto per l'enfasi nel testo; nei titoli si cambia misura e spazio, non peso. Tutte le scale del paragrafo
  c rispettano la regola.
- **Corsivi veri.** Caricare il corsivo (`ital`) quando il testo lo usa; corsivo solo per citazioni intere, titoli di opere,
  sottotitoli interi (Bitossi), mai per una parola del titolo (divieto). Bründlmayer non è un esempio di sobrietà: lì il testo
  prevalente è Garamond URW corsivo a 24,75/32,2 px (il 28 % del testo) e sotto i titoli c'è un sottotitolo corsivo rosso
  mattone (#A74948) su fondo #FDFDF6: proprio la combinazione crema, mattone e corsivo che la seconda ondata ripete. Prata,
  Golos Text, Libre Caslon Display, Hind e Kumbh Sans non hanno corsivo, e delle famiglie usate in c Noto Serif Display è
  caricata senza: nel CSS aggiuntivo `font-synthesis: none`, così il browser non lo inventa.
- **Numeri.** Prezzi, orari, misure e dati in colonna: `font-variant-numeric: tabular-nums lining-nums`. Nel testo corrente
  cifre proporzionali. Fanwood Text, Alegreya Sans e Gelasio hanno di default le cifre minuscole (in Fanwood il 3, 4, 5, 7 e 9
  scendono di 0,22em): nei bottoni, nei titoli in maiuscolo, nelle tabelle e negli orari forzare `lining-nums`. L'API Google
  toglie numeri minuscoli alternativi, maiuscoletto e forme per maiuscolo; le cifre tabellari restano quasi sempre. Senza
  `tnum` e con cifre proporzionali (letto nei file serviti il 6/10/2026): Libre Franklin, Hind, Albert Sans, Kumbh Sans,
  Prata, Libre Caslon Display. Hanken Grotesk oggi ha cifre tabellari di default (il censimento la dava senza). Intervalli col
  trattino breve legato alle cifre da U+2060 (word joiner) perché non vada a capo; spazio indivisibile tra numero e unità
  (16&nbsp;m², 8&nbsp;m/s, €&nbsp;50,00), tra i gruppi di un numero di telefono e dopo le parole di una lettera ("a&nbsp;900
  metri"): un a capo sbagliato fa sembrare brutto il carattere che si sta giudicando. Mai U+2014.
- **Corpo e interlinea.** Testo 16-20 px (Butterick 15-25); con altezza x bassa (Fanwood Text 0,385, usata
  qui solo per i titoli) 18-20 px. Interlinea del testo 1,45-1,8 (i siti calmi 1,75-1,8, i cataloghi sotto 1,4); titoli grandi 0,95-1,15;
  su mobile un po' più stretta (Google Fonts Knowledge, fonti 1.1; censimento industria).
- **Misura della riga.** 45-75 caratteri, 66 ideale. In Elementor: larghezza massima del widget di testo, circa 34em per il
  paragrafo d'apertura e 40-44em per la lettura, da tarare sul carattere (prova di Butterick: due o tre alfabeti minuscoli).
- **Maiuscolo.** Solo per meno di una riga: menu, bottoni, intestazioni brevi, il nome di una collezione, i titoli di due o
  tre parole del Leon d'Oro. Piccolo e spaziato da +0,05 a +0,15em (fino a +0,25em nei menu degli alberghi alpini); grande con
  spaziatura nulla o negativa (Laminam -0,04em). Mai paragrafi in maiuscolo, mai un'etichetta maiuscola sopra ogni titolo. 23
  siti di ospitalità su 30 scrivono i titoli in minuscolo con la sola iniziale maiuscola. Il menu maiuscolo spaziato con il
  bottone scuro rettangolare è la firma del "modello elegante": il menu va in minuscolo, salvo dove il riferimento lo fa
  maiuscolo, e il bottone prende il colore della casa.
- **Spaziatura.** Negativa sui titoli da 28 px in su (da -0,005 a -0,035em); positiva sul maiuscolo piccolo; zero sul
  minuscolo del testo, salvo i caratteri disegnati larghi (Kumbh Sans +0,01em, come sbp +0,5 px su FF Mark).
- **Titoli.** `text-wrap: balance` sui titoli, `pretty` sui paragrafi; niente punto finale; titoli descrittivi, con un fatto
  ("Il venerdì, pesce", "Marmo San Pietro"), non con una frase da brochure.
- **Il carattere accanto al logo vero.** Si sceglie guardando il logo e le foto del cliente insieme: Jost accanto al
  geometrico di GARDENS-PAV, Libre Franklin accanto alle scritte del Leon d'Oro, il serif leggero accanto al logo con grazie
  di rosyGarbo. Le tavole mostrano il logo, non il nome scritto col carattere.
- **In Elementor.** Elementor carica i Google Fonts con la vecchia API (`css?family=Nome:100,100italic,...,900italic`), che
  dà istanze statiche: un asse ottico resta al valore predefinito. Nessuna delle scelte del paragrafo c ne ha bisogno; se un
  giorno servisse, si carica il link `css2` nel tema figlio o si ospitano i file variabili con il plugin Custom Fonts, e si
  toglie quel carattere dal kit. "Load Google Fonts Locally" (spento di default dalla 3.32.1) evita le richieste a Google per
  il GDPR. Il kit nasce con Roboto e Roboto Slab: va cambiato in Impostazioni del sito prima di costruire. Elementor 4.3.3 ha
  di serie `.elementor-social-icon:hover{opacity:.9}`: con le icone social in pagina va annullata nel CSS aggiuntivo
  (`opacity:1`), altrimenti è un bottone che sbiadisce (divieto) e `segnali.sh` lo segnala.
- **Fontshare.** Si può usare con un link CSS solo un carattere a licenza libera, e va detto. Nessuna scelta di questa guida
  lo usa. Supreme (il carattere di Formlabs) non lo è: Fontshare lo classifica "Closed Source" con la ITF Free Font License,
  che è gratuita ma non trasferibile, vieta di rendere il file disponibile a terzi e dice che l'API di Fontshare non fa parte
  dei diritti concessi. Satoshi, Clash Display e Cabinet Grotesk sono in lista b.

---

## e. Catalogo dei segnali da IA

Fonti, cause ed esempi in `segnali-ia.md` (paragrafo 4). Soglie per una home a 1440. "Vietato" = divieto del committente.

| Segnale | Regola verificabile (soglia) | Mossa sostitutiva |
|---|---|---|
| Carattere delle liste (b) | testo, titoli o 10 % del testo in un carattere della lista b | partire dal riferimento del settore (c) |
| Monospazio come "sapore tecnico" | più di 0 % in un sito che non vende software; etichette `mono uppercase` | cifre tabellari del carattere di testo |
| Etichetta maiuscola sopra il titolo | più di 1 per pagina (non contano data, luogo, codice) | il titolo dice già dove siamo |
| Parola d'accento in corsivo, altro carattere o colore | anche una (vietato) | grassetto dello stesso carattere dentro una frase, o niente |
| Gerarchia piatta | nessun elemento davvero grande; meno di 3 misure di H2 da guardare | un solo elemento grande; titoli 300-500 |
| Titoli neri | titoli sopra 40 px in 700-900 con spaziatura da -0,01em in su, fuori dai due casi della regola a.4 | 300-500 e -0,02/-0,04em |
| Viola, indaco, gradienti, testo in gradiente | uno (vietato) | colore del marchio o del materiale |
| Palette della seconda ondata | crema o beige con serif e terracotta (circa #D97757); nero con verde acido; smeraldo | bianco e il colore del soggetto (il giallo della facciata, il verde del logo) |
| Un accento per tutto | stesso colore saturo su bottoni, link, numeri, trattini, frecce | colore su bottone e logo; il resto prende tono dalle foto |
| Fasce alterne regolari | più di 4 fasce di fondo a tutta larghezza, di altezza simile (da guardare) | un fondo e un cambio deciso, o fasce di foto |
| Titolo a sinistra, paragrafo a destra | in più di 1 sezione | titolo e testo nella stessa colonna, la foto guida |
| Capo di sezione "a cartella" | etichette agli estremi e filetto con le stanghette | nessuna testata ripetuta |
| Filetti ovunque | 30 o più bordi sottili larghi più di 200 px | lo spazio; il filetto solo in tabella |
| Numero grande con etichetta | più di 1, o un numero senza fonte | il numero dentro una frase |
| Numerazioni 01, 02, 03 | davanti a voci che non sono una procedura | numerare solo i passi veri |
| Indice a righe con conteggio e freccia | "Vasche monoblocco 17 MISURE →" | categorie come foto cliccabili (Hermle, Benvegnù) |
| Hero diviso con due bottoni | testo e immagine a metà, pieno più contorno | un'azione sola, o nessuna |
| Tabelle complete in home | più di 4 righe di dati; una tabella per camere, atelier, orari | due o tre dati in una frase; schede con la foto |
| Disegni rifatti con quote mono | cartiglio finto in grafica | disegno dell'azienda o foto del prodotto posato |
| Poche foto, piccole, chiuse in riquadri | area foto sotto il 35 %; foto mai a filo | foto vere, una a metà schermo, a filo |
| Foto stock, render 3D, foto IA | una spacciata per l'azienda | foto dell'azienda; il brief delle foto mancanti nel LEGGIMI |
| Badge sopra il titolo, tre box con icona, card col bordo sinistro, vetro, emoji, Lucide, shadcn | uno (vietati) | contenuto vero in testo e foto |
| Trattino colorato sotto ogni H2 | più di 1 | niente: lo spazio basta |
| Frecce scritte nei link | più di 2 (le virgolette « » non contano) | sottolineatura; la freccia solo per un link esterno |
| Puntino separatore nelle etichette | "A · B" ripetuto | una frase con la virgola |
| Dissolvenze, contatori che salgono, rimbalzi, fascio sul cursore | uno (vietati) | in Elementor nessun "Animazione d'ingresso" e nessun effetto di movimento |
| Hover che sbiadisce, freccia che si sposta | `opacity` sotto 1 nell'hover di un link o di un bottone (vietato) | cambio di colore pieno |
| Titolo in due frasi col punto ("X. Y.") | più di 1 titolo col punto; nessuno in due frasi | titolo descrittivo senza punto |
| "Non solo X, ma Y", "non è X, è Y" | uno | dire la cosa |
| Regola del tre | tre aggettivi o verbi ornamentali in fila | uno solo, o i fatti (tre lavorazioni vere vanno bene) |
| Parole da brochure | eccellenza, passione, soluzioni, innovazione, a 360°, leader, know-how, mission, all'avanguardia, "è importante sottolineare", "clima di cortesia", "trentennale esperienza", "linee raffinate" (vietato) | misure, nomi, luoghi, date |
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

Il comando (copia identica in `scratchpad/kit/`) lancia `misura-segnali.cjs` a 1440, che scrive `<nome>-1440-info.json`,
`-top.png` e la pagina intera `<nome>-1440.png`; poi `segnali-soglie.cjs` misura il resto, stampa una riga per soglia e scrive
`<nome>-1440-soglie.json`. Ogni riga è OK, DA CORREGGERE (soglia bloccante: separa i nostri siti dai riferimenti misurati) o DA
GUARDARE (soglia indicativa: anche siti veri la superano). Esce con 0 se nessuna soglia bloccante fallisce, con 1 se almeno una
fallisce, con 2 se la pagina non si apre, risponde con un errore o non ha testo (provato con `http://127.0.0.1:1/`). Un percorso
locale diventa `file://`. Si misura l'anteprima HTML e poi il WordPress: le animazioni d'ingresso di Elementor si vedono solo
lì. `misura-segnali.cjs` del kit è la versione corretta dopo la revisione; quella in `ricerca-caratteri/` è rimasta com'era,
perché documenta come sono state prese le misure della ricerca.

Cosa conta e cosa no, per tutte le soglie: solo elementi visibili (anche gli antenati) e dentro la finestra in orizzontale,
quindi non i pannelli fuori schermo né le schede del carosello che non si vedono; non il testo dei banner dei cookie (che lo
script prova a chiudere con bottoni, link o testo "OK"); non i campi dei moduli.

| # | Soglia (home a 1440) | Tipo | Come la misura lo script |
|---|---|---|---|
| 1 | area foto almeno 35 % | bloccante | celle di 20 px coperte da img, video, canvas e sfondi con immagine più grandi di 120 px; gli iframe (mappe) si contano a parte e non entrano |
| 2 | nessun carattere della lista b come testo principale, titoli o 10 % del testo | bloccante | nomi ripuliti da pesi, suffissi e codici ("Inter Variable", "Satoshi-Variable", "__Inter_a1b2c3") e confrontati con la lista b |
| 3 | monospazio 0 % | bloccante | famiglie con mono, code, courier, consol, menlo nel nome |
| 4 | al massimo 1 etichetta maiuscola sopra un titolo | bloccante | testo maiuscolo fino a 15,5 px e 70 caratteri, entro 100 px sopra un h1-h3, fuori da menu, testata, piede, link e bottoni e senza link dentro; quelle con cifre (date, codici) non contano, i luoghi si guardano a occhio |
| 5 | al massimo 1 titolo col punto; nessuno in due frasi; nessun "non solo ... ma" | bloccante | h1-h3 e testo visibile |
| 6 | almeno 3 misure di H2 | da guardare | corpi distinti degli H2 visibili |
| 7 | al massimo 4 fasce di fondo | da guardare | colore pieno quasi opaco (alfa da 0,9) largo almeno il 95 % della finestra e alto più di 200 px; foto e velature non contano |
| 8 | al massimo 1 sezione con titolo a sinistra e paragrafo a destra | da guardare | H2 più stretto del 62 % con un paragrafo di 80 caratteri alla sua destra |
| 9 | meno di 30 filetti | bloccante | bordi superiori o inferiori da 1-2 px su elementi larghi più di 200 px |
| 10 | al massimo 2 frecce | bloccante | → ↗ ↘ ⟶ ➔ ➜ ⇢ ovunque; › e » solo dentro un link o un bottone, mai nelle virgolette «» né nelle briciole di pane |
| 11 | al massimo 1 numero grande | da guardare | testo di sole cifre e unità da 40 px in su |
| 12 | numerazioni solo per una procedura | da guardare | voci 01, 02...: oltre 2 si guarda; se sono passi veri si tengono e si scrive perché nel LEGGIMI |
| 13 | nessuna tabella oltre 4 righe di dati | bloccante | righe del corpo delle tabelle visibili |
| 14 | didascalie senza la fonte | bloccante | "foto/immagine ... brochure, scheda, Booking, catalogo, sito, pdf", "fonte:" |
| 15 | almeno un contenuto datato o con nome | da guardare | anni 1850-2039 e date nei nodi di testo (anche nei paragrafi con un link), fuori dal piede, dai banner, dai numeri di telefono, dalle righe legali e dai riferimenti normativi (D.M., D.Lgs., Regolamento UE, UNI EN); stampa il contesto di ogni data; i nomi di persona si guardano a occhio |
| 16 | divieti | bloccante | U+2014, emoji nei titoli, testo in gradiente, gradienti viola-blu (tinta 220-320), backdrop-filter, bordo solo a sinistra, svg Lucide, classi e attributi d'ingresso (elementor-invisible, animated, aos, wow, fade-in, data-aos) e animazioni CSS che partono da opacità 0, `:hover` con opacità sotto 1 su un link o un bottone visibile, parole da brochure (anche con l'apostrofo tipografico); gli altri gradienti e i fogli di stile di altri domini non letti escono come nota; corsivo serif, tre box e badge a occhio |
| 17 | una famiglia o una superfamiglia, una seconda solo con un compito | da guardare | quota di testo per famiglia (da 2 %), raggruppata per nome ripulito (Frutiger-Light e Frutiger-Bold insieme; PP Grafier e PP Neue Montreal separati) |
| 18 | titoli neri | da guardare | titoli sopra 40 px in 700-900 con spaziatura da -0,01em in su; si tengono solo nei due casi della regola a.4 |

Una pagina è pronta quando `segnali.sh` esce con 0, ogni riga DA GUARDARE ha una ragione scritta nel LEGGIMI, e lo screenshot
guardato a pezzi (`slice.py`) non mostra i segnali della tabella e che lo script non vede (palette, hero a due bottoni,
didascalie dell'ovvio, testi, foto peggiore in apertura).

**Esiti del 6 ottobre 2026, con lo strumento corretto** (uscite complete nella cartella di lavoro `scratchpad/revisione/finale/`):

| Pagina | Esito | DA CORREGGERE (bloccanti) | DA GUARDARE |
|---|---|---|---|
| Benvegnù, `BenvegnuSrl-Sito/anteprima/01-home.html` | 2 su 10, uscita 1 | 4 etichette sopra i titoli: 2 ("DAL CATALOGO", "PER CHI LAVORIAMO"); 10 frecce: 13 | 7 fasce: 6. Passano: foto 40,2 %, Barlow 87,7 % e Barlow Condensed 12,3 %, mono 0 %, filetti 27 (43 nella ricerca: le 8 schede del carosello fuori dalla finestra non contano più), 5 misure di H2, una data (1980) |
| Gardens Pav, `GardensPav-Sito/_prova/build/anteprima/01-home.html` | 8 su 10, uscita 1 | 1 foto 9,6 %; 2 IBM Plex Mono (lista b); 3 mono 22,5 %; 4 etichette 5; 5 titoli col punto 5 su 13, 2 in due frasi; 9 filetti 97; 10 frecce 7; 13 tabella di 8 righe di dati | 6 H2 di una misura (42 px); 7 fasce 8; 11 numeri grandi 2 ("0,88", "0,40"); 15 nessuna data: il "14/06/1989" che faceva passare la soglia è il D.M. 236 |
| Wirmec, `Wirmec-Sito/_prova/build/anteprima/01-home.html` | 6 su 10, uscita 1 | 1 foto 15,7 %; 2 IBM Plex Sans e Condensed (lista b); 3 mono 9,4 %; 9 filetti 51; 10 frecce 20; 14 "W 1500, foto della brochure Wirmec." | 6 H2 di due misure; 7 fasce 8; 8 titolo a sinistra in 2 sezioni; 12 numerazione di 9 voci |
| Rieder (rieder.cc/us) | 0, uscita 0 | nessuna | H2 di una misura, 10 fasce, nessuna data |
| Mutina (mutina.it) | 0, uscita 0 | nessuna | H2 di una misura |
| Hermle (hermle.de/en) | 1, uscita 1 | 2 Roboto (lista b) | H2 di una misura, 6 fasce |
| TRUMPF (trumpf.com/it_IT) | 1, uscita 1 | 16 parole da brochure ("soluzione", "soluzioni", "innovazione") | H2 di due misure, 3 numeri grandi |
| Tavole 03, 05, 07 | 0, uscita 0 | nessuna | "famiglie" (per forza: due o tre scelte e la cornice), H2 |
| Tavole 01, 02, 04, 06 | 1, uscita 1 | solo 1, area foto: 21,1 %, 33,7 %, 25,3 %, 22,0 % | come sopra; nella 04 anche i titoli in 800 (il caso dichiarato del Leon d'Oro) |

Le pagine di prova di un revisore (`critica-fatti/prova/`) danno quello che devono: la dissolvenza con `@keyframes` da opacità 0
viene trovata, tre citazioni «» non contano come frecce, il pannello fuori schermo e i suoi campi non contano come filetti né
come bordo sinistro, il banner dei cookie in Arial non entra nelle quote; nella seconda pagina 1985 e 2024 vengono letti nel
paragrafo con il link e il "2016/679" del banner no. `http://127.0.0.1:1/` esce con 2.

Le tavole sotto il 35 % sono quelle delle aziende che non hanno foto grandi: Wirmec (le foto vere più larghe sono di 800-951
px, il resto è scontornato), il Leon d'Oro (sala 1.200 px, piatti 750-960) e Oltreoceano (464 px). Non è un difetto della
tavola da nascondere: è la prima cosa da chiedere a quei clienti. I valori della ricerca (segnali-ia 5.1) restano quelli presi
con la prima versione dello strumento; cambiano solo i filetti di Benvegnù.

---

## g. Note per i siti già avviati

**Gardens Pav** (8 soglie bloccanti). In ordine di effetto: (1) foto delle realizzazioni grandi e a filo, almeno un terzo della
home: le migliori sono Altivole, Pistoia, San Lazzaro di Savena, Milano, Cornate d'Adda, Aosta, e l'autogru col logo in
apertura (tavola 02); (2) via IBM Plex Mono: Jost come Mutina, con il logo geometrico (tavola 02), oppure Archivo da solo con
le sue cifre tabellari; non Chivo, che è della stessa fonderia; (3) via i capi "a cartella" e due terzi dei filetti, una sola
etichetta, "m³" e non "mc"; (4) titoli senza punto, H1 in una frase; (5) in home una tabella di 4 righe al massimo, il resto
nelle schede; (6) un contenuto con una data vera (un cantiere con l'anno): il D.M. del 1989 non conta. Fasce e H2 da guardare.

**Wirmec** (6 bloccanti). IBM Plex è nella lista b: la strada è c1, Sofia Sans come Festool e Metzner (titoli 700 in
minuscolo), oppure Hanken Grotesk come WEIMA con un titolo davvero grande; tavola 01 con il logo e i testi di Wirmec. Se si
tiene Plex, almeno via Plex Mono (9,4 %) con `tabular-nums` nel Sans. Poi: via le 20 frecce (resta quella di "Brochure in PDF")
e i 6 trattini rossi sotto i titoli; via la numerazione 01-12 delle lavorazioni, che non sono una sequenza; una sola sezione
con titolo a sinistra; didascalie con luogo o macchina, non "foto della brochure". Le foto: chiedere il reparto e i cavi
lavorati in primo piano (come Metzner); la postazione AM600 Vantage scontornata non va in apertura.

**Benvegnù** (2 bloccanti), il sito giudicato "molto meglio": regge su foto al 40 %, una superfamiglia e cinque misure di
titoli. Residui da togliere: le etichette con il trattino davanti ("DAL CATALOGO", "PER CHI LAVORIAMO", e "RIVENDITORE
AUTORIZZATO VIBRAM" sopra il 329), le 13 frecce, la barra rossa del carosello; da guardare le 6 fasce e i 27 filetti (sotto la
soglia, ma vicini). Il "329" e "IL CATALOGO" a sinistra sono al limite (uno ciascuno): si tengono solo se sono la cosa per cui il
cliente viene scelto. Barlow resta di Benvegnù e non si ripropone.

**Albergo Vescovi.** Il 02 ha scelto "Abete": Source Serif 4 600 per i titoli e Schibsted Grotesk per il testo (paragrafo 4).
Source Serif 4 è la sorella di Source Sans 3, che è in lista b. La guida consiglia di portare in 2.3 Petrona, una famiglia sola, titoli 500 e menu in minuscolo, con il logo
tondo verde e la foto invernale (tavola 03); Gelasio, come Waldhaus Sils (già nel 02), è l'alternativa per il ristorante. Se
resta Abete: titoli in 400, non 600. In ogni caso: via le didascalie con "Servizio fotografico della scheda Booking.com";
bottoni ad angoli quasi vivi, non a pillola; Newsreader (accoppiata B) è nella lista b e resta fuori; le camere si mostrano con
le foto, non in tabella. I prototipi `_prova/direzioni/*/proto.html` non esistono ancora: appena ci sono, `segnali.sh` su ognuno.

**Leon d'Oro.** La scelta "Facciata" del 02 è la raccomandata di c4: Libre Franklin 800 maiuscolo per i titoli di due o tre
parole, 400 e 600 per il testo, il giallo della facciata come campo e il verde delle persiane per il bottone. Libre Franklin
non ha cifre tabellari (verificato): il listino va in righe con il prezzo allineato a destra, come nella tavola. L'800 va
contro la regola 4 e si tiene perché viene dalle scritte della cartolina e del logo. In apertura la sala con le travi, non il
baccalà; titoli con i fatti ("Il venerdì, pesce"), mai "una cucina di famiglia, come una volta" o "nel clima di cortesia
e disponibilità". Da qui in avanti Libre Franklin è un carattere di casa: non per altri siti.

**Altri 02 già scritti con caratteri della lista b o della guida** (da rivedere prima della 2.3): Marmi Sgambaro propone
Space Mono per i cartellini (monospazio e lista b; la tavola 02 prova Prata + Golos Text sui suoi marmi); Villa Pollini propone
DM Sans e Instrument Sans; Piovene Porto Godi Source Sans 3 e Instrument Sans; Callegari Tende DM Mono accanto a Hanken Grotesk,
che la guida usa per Wirmec; Rosy Garbo Newsreader (lista b) e Libre Franklin (di casa al Leon d'Oro), mentre la tavola 05
prova Noto Serif Display con Kumbh Sans.

---

## Revisione

Due revisioni indipendenti del 6 ottobre 2026: una sui fatti (46 rilievi più il controllo di U+2014, numerati come nel loro
testo) e una sul gusto (11 rilievi generali più quelli per settore). Ogni rilievo è stato verificato; dove serviva, rifatto
dal vivo (Metzner, Inigo, Abitare Co., Waldhaus Sils, Danielle Frankel, Sophie Buhai, Google Stitch, le pagine di prova).
Una riga per rilievo.

**Fatti: applicati**

- **1.** Supreme non è a licenza libera ("Closed Source", ITF Free Font License non trasferibile): tolti Supreme e Chivo, nota in d (Fontshare).
- **2.** Bründlmayer: testo prevalente in corsivo 24,75/32,2 e sottotitoli corsivi mattone su crema; corretto in d, non più esempio di sobrietà.
- **3.** Milla Montis, misure del testo sbagliate: uscita dalla guida insieme a Belleza + Cabin.
- **4.** Schwarzschmied, il 51 % del testo è Novel Sans 600 maiuscolo: scritto in c3.
- **5.** WEIMA, le parole grandi sono in 400 a 130 px e l'h1 in 500: corretto in a.4 e c1.
- **6.** One Medical, etichette inesistenti: uscita dalla guida con Gloock + Figtree.
- **7.** Parsley, testo 18/28,8 a -0,02em: corretto in c6.
- **8.** Poli, Open Sans al 23,8 %: uscita dalla guida con Questrial.
- **9.** Francescana, Bodoni Moda 500 a +0,139em: uscita dalla guida con Bodoni Moda.
- **10.** Mutina, testo 16/32 e 18/21,6: corretto in c2.
- **11.** Zünd e Hermle con caratteri della lista b: scritto in b.
- **12.** Literata 500 non caricato: Literata è uscita dalla guida.
- **13.** Gloock ha tnum: Gloock è uscita dalla guida.
- **14.** Fanwood Text ha le cifre minuscole di default: aggiunto in d.
- **15.** Golos Text senza corsivo: aggiunto in d (News Cycle è uscita).
- **16.** Jost e Literata nei temi di serie di WordPress: Jost in lista di attenzione con la nota, Literata fuori.
- **17.** Selettori dei generatori: Stitch verificato (12 caratteri); Public Sans, Work Sans, EB Garamond e Figtree in lista b.
- **18.** Liste SEO: Hanken, Spectral e Albert Sans in lista di attenzione; Typewolf citato come nota sull'uso tra designer.
- **19.** Le soglie non separavano Benvegnù dai riferimenti: ora bloccanti e da guardare; Benvegnù 2, Rieder e Mutina 0.
- **20.** Soglie non tarate: H2, fasce, date e numero di famiglie da guardare, insieme a titolo a sinistra, numeri grandi, numerazioni e titoli neri.
- **21.** Komax omesso nell'area foto: scritto in a.1 (otto riferimenti su nove fra 37 e 63 %, Komax 14,2 %).
- **22.** Raggruppamento delle famiglie solo sugli spazi: nomi ripuliti da trattini, pesi e suffissi, prefissi di fonderia a due parole.
- **23.** Hover con opacità: contano solo opacità sotto 1 su link o bottoni visibili; fogli non letti in nota; icone social di Elementor in d.
- **24.** Ogni gradiente falliva la soglia: ora solo testo in gradiente e tinte viola-blu; gli altri in nota.
- **25.** Elementi fuori schermo e campi dei moduli contati: esclusi (misura-segnali versione 2).
- **26.** Date lette solo negli elementi senza figli: ora nodi di testo, senza banner, norme e telefoni; Gardens Pav non passa più per il D.M.
- **27.** » e › contati come frecce: solo dentro link e bottoni, mai nelle virgolette né nelle briciole di pane.
- **28.** Banner dei cookie nelle quote e non chiusi: esclusi dalle quote, chiusura anche con link e testo "OK".
- **30.** Velature contate come fasce: non conta un fondo con alfa sotto 0,9.
- **31.** Parole da brochure mancanti e apostrofo tipografico: aggiunte "soluzioni", "è importante sottolineare", apostrofo ’.
- **32.** Dissolvenze CSS non viste: si leggono le `@keyframes` che partono da opacità 0 e le classi fade, data-aos, data-sal.
- **33.** Nomi della lista b con suffissi: riconosciuti ("Inter Variable", "Satoshi-Variable", next/font).
- **34.** Area foto con iframe e immagini trasparenti: iframe a parte, controllo di visibilità sugli antenati.
- **35.** Codice d'uscita 2 falso: ora 2 se la pagina non si apre, risponde con un errore o non ha testo (provato).
- **36.** Peso dei titoli non misurato e commento "mono <= 5 %": aggiunta la soglia 18, commento corretto a 0 %.
- **37.** Regola dei pesi contraddittoria: riscritta in d, scale ricontrollate.
- **38.** Spectral in tre pesi: ora 400 e 500.
- **40.** Spaziatura positiva sul testo: tutte a 0, salvo Kumbh Sans (disegno largo, +0,01em).
- **41.** Regole sulle misure: Jost tolta dalle altezze x basse, maiuscolo piccolo +0,05/+0,15em; Work Sans, Bodoni e Literata fuori.
- **42.** Etichette "per sezione" e "per pagina": una regola sola, al massimo 1 per pagina.
- **43.** Bründlmayer contro c4: risolto con il punto 2.
- **44.** Riferimenti fuori settore: Frankel per la sposa, Metzner per le macchine, Abitare Co. per la casa; fiori e gioielli restano senza.
- **45.** Numeri del censimento (Cervo, Il Pellicano): corretti in a.2 e a.3.
- **46.** Tavole: accento 07 preso dalle tende e dagli scuri delle Dimore del Cuore (#2F5A4F), frasi da brochure tolte, pesi inutili tolti.
- **47.** U+2014 in `controlla.mjs` (due copie): `String.fromCharCode(0x2014)`; lo stesso con `'\u2014'` nei build.py di Benvegnù, Gardens Pav e Wirmec e nei tre script di `_prova`.

**Fatti: respinti o applicati in parte**

- **29.** Etichette: esclusi i contenitori con un link (il "READ MORE" di Rieder); le categorie delle notizie di TRUMPF erano dentro link e cadono; i luoghi restano da guardare a occhio, perché lo script non li distingue da un'etichetta.
- **39.** Sofia Sans in 700 contro la regola a.4: respinto come errore, applicato come chiarimento: la regola a.4 ora dichiara l'eccezione delle macchine (Festool, Komax, Metzner in 700), con spaziatura da -0,01em in giù.

**Gusto: applicati**

- **G1.** Lo stesso schema in tutte le varianti: tre aperture diverse (campo nel colore della casa, titolo grande sopra la foto a filo, titolo sulla foto), titoli da 84 a 128 px.
- **G2.** Il nome scritto al posto del logo: loghi veri per Wirmec, Gardens Pav, Albergo Vescovi, Hotel Garibaldi, rosyGarbo, Salumificio Fontana; gli altri non hanno un logo pulito nel repository.
- **G3.** Foto chiuse in riquadri: foto a filo e file di foto a tutta larghezza; area foto delle tavole fra 21 e 37 %.
- **G4.** Le foto peggiori in apertura: in apertura la sala con le travi, l'autogru col logo, la neve, la reception con le poltrone rosse; via postazione scontornata, baccalà, sauna rosa, lettino viola, cucina col frigo, sposa tagliata.
- **G5.** Menu maiuscolo spaziato e bottone scuro ovunque: menu in minuscolo salvo Schwarzschmied e Frankel, bottoni nel colore della casa.
- **G6.** Scala timida: aperture da 84 a 128 px.
- **G7.** Tabella a destra in tutti i settori: tabelle solo per Wirmec, Gardens Pav e il listino del Leon d'Oro; altrove righe brevi o schede con la foto.
- **G8.** Nessuno spazio indivisibile: numero e unità, euro, telefoni, parole di una lettera, "1°"; regola in d.
- **G9.** A 390 la prima schermata è solo testo: la foto viene prima del titolo.
- **G10.** Testi: via le frasi da brochure, titolo Wirmec con le virgole, orari dal lunedì al sabato con la nota sulla domenica che il sito non indica.
- **G11.** Foto prese da /tmp: copie ridotte in `tavole-caratteri/foto/`, oppure percorsi relativi agli `assets/web` del repository.
- Macchine: Sofia Sans raccomandata, Hanken alternativa, Chivo fuori; apertura con il doppio cavo della AM600 e la micrografia della sezione (il reparto non ha foto).
- Materiali: Jost resta, titoli 500, menu minuscolo, "autolavaggi", "m³"; Prata + Golos Text passa a Marmi Sgambaro; foto di cantiere a filo.
- Hotel: Petrona raccomandata per il Vescovi, Spectral in 400-500 per il Garibaldi, Gelasio al posto di Belleza + Cabin (Waldhaus verificato: Larken 400 maiuscolo); logo, verde, foto invernale, camere in foto.
- Ristoranti: Libre Franklin del 02 raccomandata, Fanwood + Alegreya Sans al Salumificio Fontana, Questrial fuori, sala con le travi e titoli con i fatti.
- Moda: Noto Serif Display 300 in minuscolo con Danielle Frankel come riferimento (Canela Light al 99 %), Literata e Bodoni fuori, foto alla loro misura in campo nero.
- Salute: Gloock + Figtree fuori, Figtree in lista b; Hind per Oltreoceano in minuscolo; variante per il Centro Dentale Vanuzzo con Libre Caslon Display; orari in ordine.
- Casa: Gelasio + Familjen, Old Standard + News Cycle e Kumbh Sans 200 fuori; ogni appartamento in una scheda con la data da cui è libero.

**Gusto: respinti o applicati in parte**

- Macchine, Sofia Sans Semi Condensed per i nomi dei modelli: respinto, rifà lo schema Barlow + Barlow Condensed di Benvegnù.
- Macchine, Metzner "fatto con Elementor": non verificato; misurato WordPress con WP Rocket.
- Materiali, Public Sans alla casa: respinto, è in lista b (Stitch, shadcn).
- Ristoranti, EB Garamond a Cantina Dotto e Villa Pollini: respinto, è in lista b (preset di shadcn, madegooddesigns); le cantine restano senza scelta finché non c'è un riferimento.
- Moda, Work Sans per i nomi delle collezioni: respinto (lista b, Google Stitch); i nomi vanno in Kumbh Sans 300 maiuscolo, come le testate di Rosy Garbo; il campo argento non serve in una porzione sola.
- Salute, Albert Sans per Vanuzzo: in parte; Albert Sans passa alla casa e il testo di Vanuzzo resta in Hind. Titoli di Hind in 500, non 600 (Lanserhof 450, regola a.4).
- Casa, Public Sans una famiglia come Inigo: respinto; Inigo misurato dal vivo usa Adobe Caslon per il 65 % del testo e Söhne solo per etichette maiuscole da 12 px. Al suo posto Albert Sans come Abitare Co. (Circular Std al 77 %, testo 300 a 22/30).
- Casa, Libre Caslon Display per "Le Dimore del Cuore": respinto, è già nella salute e nessuna famiglia si ripete tra settori.
- Scala: gli H2 restano di una misura per scelta, perché ogni scelta è una porzione di pagina; la soglia è da guardare.
