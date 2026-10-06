# Censimento caratteri: ospitalità e cibo

Rilevazione del 6 ottobre 2026 su 30 siti reali di hotel di montagna, terme, alberghi di città, tenute, cantine, distillerie, ristoranti, pasticcerie, salumifici e caseifici, ceramica, gioielleria e arredo. Dati completi, per sito, in `censimento-ospitalita-cibo.json` (stessa cartella).

## Come è stato fatto

1. **Scelta dei siti.** Hotel e ristoranti con riconoscimenti verificabili: chiavi o stelle Michelin, The World's 50 Best, Fonts In Use, una nomination Awwwards. A questi si aggiungono aziende leader del proprio settore con un sito curato; per queste la scelta è editoriale ed è dichiarata come tale nel JSON. Alcuni siti sono geograficamente vicini al committente: Alajmo (Rubano, PD), Poli (Schiavon, VI), Zýmē (Valpolicella) e gli hotel altoatesini.
2. **Caratteri reali.** Ho scaricato HTML e CSS con curl, cercando `@font-face`, kit Adobe (use.typekit.net), Google Fonts e file self-hosted. Poi Playwright a 1440px: per ogni sito ho letto `getComputedStyle` di h1, h2, h3, p, nav a e button, la quota di testo visibile per famiglia e `document.fonts`. Ho anche salvato le schermate (prima e seconda vista).
3. **Misure.** Ho scaricato i file dei caratteri caricati da ogni pagina e 110 famiglie Google Fonts, e li ho misurati con fontTools: altezza della x, rapporto x/maiuscola, larghezza media delle minuscole, contrasto (spessore della o: lato contro sommità). Le alternative proposte sono le più vicine per misura, verificate a occhio su tavole di confronto.

Limiti:
- Awwwards blocca le richieste automatiche, quindi i premi Awwwards citati vengono dai risultati di ricerca e non da una lettura diretta della pagina.
- Ornellaia e Manincor aprono con un controllo dell'età: per loro i dati vengono soprattutto dal CSS.
- Le schermate stanno in `/tmp/claude-0/-home-user-danielnistorr/89486122-32ef-5f21-add5-5cbe6108c543/scratchpad/ricerca-caratteri/ospitalita-cibo/shots/` (`<id>.png` e `<id>_2.png`; tavole di confronto `_cmp1.png`...`_cmp5.png`).

## Tabella dei 30 siti

| Sito | Settore, paese | Titoli | Testo | Terzo carattere | Licenze | Alternative Google (titoli / testo) |
|---|---|---|---|---|---|---|
| [Forestis](https://www.forestis.it/) | hotel di montagna, IT | Brandon Text Light | lo stesso | nessuno | commerciale | Jost Light |
| [Gloriette Guesthouse](https://www.gloriette-guesthouse.com/) | hotel di montagna, IT | Eirlys Bold | Georgia (di sistema) | TT Norms, menu maiuscolo | commerciale + sistema | DM Serif Display / Georgia / Hanken Grotesk |
| [Milla Montis](https://www.hotel-milla-montis.com/) | hotel di montagna, IT | Optima nova Light | ITC Johnston Light | nessuno | commerciale | Belleza / Cabin |
| [Zirmerhof](https://www.zirmerhof.com/) | hotel storico, IT | Bembo | Raleway | nessuno | commerciale + Google | EB Garamond / Raleway |
| [Schwarzschmied](https://www.schwarzschmied.com/) | design hotel, IT | Livory | Livory | Novel Sans, menu maiuscolo | Adobe Fonts | Spectral / Fira Sans |
| [Cervo](https://cervo.swiss/) | resort di montagna, CH | Maison Neue Mono maiuscolo | Cutive Mono | nessuno | commerciale + Google | Azeret Mono / Cutive Mono |
| [7132 Vals](https://7132.com/) | hotel termale, CH | Stanley Thin | Stanley | nessuno | commerciale | Gelasio o Tinos |
| [Bad Ragaz](https://www.grandresort.ch/) | resort termale, CH | ABC Otto | ABC Marfa | nessuno | commerciale | Brygada 1918 / Instrument Sans |
| [Hotel Locarno](https://www.hotellocarno.com/) | hotel di città, IT | Ogg maiuscolo | Ogg | nessuno | commerciale | Gilda Display |
| [Il Palazzo Experimental](https://www.experimentalgroup.com/venice/il-palazzo-experimental) | hotel di città, IT | Nantes | Nantes | Linux Biolinum, menu | commerciale + libero GPL/OFL | Petrona / Biolinum self-hosted |
| [Il Pellicano](https://www.pellicanohotels.com/en/hotels/hotel-il-pellicano/) | hotel storico, IT | Rollerscript (a mano) | Prestige Elite (macchina da scrivere) | Monotype Modern Display, Helvetica Neue | Adobe Fonts | Cutive Mono / Courier Prime |
| [Borgo Pignano](https://www.borgopignano.com/) | tenuta, IT | Sang Bleu Sans Light | PP Neue Montreal | nessuno | commerciale | Belleza / Hanken Grotesk |
| [Reschio](https://www.reschio.com/) | tenuta, IT | Canela Condensed maiuscolo | FF Scala Sans | nessuno | commerciale | Libre Caslon Condensed / Alegreya Sans |
| [Manincor](https://www.manincor.com/) | cantina, IT | Cochin | Corporate S | font del marchio (Micado) | commerciale | Fanwood Text / Alegreya Sans |
| [Ornellaia](https://www.ornellaia.com/) | cantina, IT | Tobias | Tobias | Triptych corsivo (link) | commerciale | Gelasio / Young Serif |
| [Bründlmayer](https://www.bruendlmayer.at/) | cantina, AT | Garamond URW | Garamond URW | Proxima Nova, menu | commerciale | EB Garamond / Figtree o Lato |
| [Zýmē](https://www.zyme.it/) | cantina, IT | Didot maiuscolo | Scale (stretto, leggero) | nessuno | Adobe Fonts + file proprio | Bodoni Moda / Sofia Sans Condensed |
| [Poli Distillerie](https://www.poligrappa.com/) | grapperia, IT | Kabel | Kabel | Open Sans (notizie) | commerciale | Questrial |
| [noma](https://noma.dk/) | ristorante, DK | Reckless Neue | Reckless | Roobert (comandi) | commerciale | Source Serif 4 / Figtree |
| [Septime](https://www.septime-charonne.fr/) | ristorante, FR | Prestige Elite | Prestige Elite | nessuno | Adobe/commerciale | Cutive Mono |
| [Osteria Francescana](https://osteriafrancescana.it/) | ristorante, IT | Roboto Bold maiuscolo | Bodoni Moda | Open Sans | Google (self-hosted) | già Google |
| [Alajmo](https://alajmo.it/) | ristorante e negozio, IT (PD) | The Seasons maiuscolo | Futura PT | nessuno | Adobe Fonts | Gilda Display / Jost |
| [Pierre Hermé](https://www.pierreherme.com/) | pasticceria, FR | Jost (chiamato "Futura" nel CSS) | Jost | Open Sans (tema) | Google (self-hosted) | già Google |
| [Tartine](https://tartinebakery.com/) | panetteria, US | Pitch Sans (monospazio) | Pitch Sans | nessuno | commerciale | Sometype Mono / Courier Prime |
| [Joselito](https://joselito.com/) | salumificio, ES | SangBleu Kingdom | Euclid Circular B | nessuno | commerciale | Gilda Display / Albert Sans |
| [Guffanti](https://www.guffantiformaggi.com/) | affinatore di formaggi, IT | Apparat | Apparat | Playfair Display (solo popup) | Adobe Fonts | Instrument Sans |
| [Bitossi](https://www.bitossiceramiche.it/) | ceramica, IT | Catalogue | Catalogue (+ corsivo) | nessuno | commerciale | Literata |
| [Heath Ceramics](https://www.heathceramics.com/) | ceramica, US | Century Schoolbook | Benton Sans | Monotype Grotesque Bold Extended | commerciale | Gelasio / News Cycle |
| [Sophie Buhai](https://www.sophiebuhai.com/) | gioielleria, US | Univers | Univers | nessuno | commerciale | Public Sans |
| [Audo](https://audocph.com/) | arredo, DK | Century Old Style | Grot 12 | nessuno | Adobe/commerciale | Gelasio / Hanken Grotesk |

## I numeri del censimento

- **Famiglie per sito.** 9 siti usano una sola famiglia, 17 ne usano due, 3 ne usano tre e 1 (Il Pellicano) quattro, ognuna con un ruolo fisso.
- **Licenze.** Su 60 ruoli (titoli più testo), 41 sono caratteri commerciali, 12 Adobe Fonts, 6 Google o open source e 1 di sistema (Georgia). Gli unici siti con caratteri Google come voce principale sono Osteria Francescana, Pierre Hermé, Cervo (Cutive Mono) e Zirmerhof (Raleway). Nessuno dei 30 usa come voce principale Inter, Poppins, Montserrat, Playfair Display, Cormorant, Fraunces, DM Sans o un mono da programmazione.
- **Serif.** 18 siti su 30 hanno i titoli in serif. Il testo corrente è in serif o in monospazio in 14 siti su 30: Gloriette, Schwarzschmied, 7132, Locarno, Experimental, Ornellaia, Bründlmayer, noma, Bitossi, Francescana (per gli indirizzi) e i quattro siti in monospazio.
- **Monospazio.** 4 siti su 30, tutti di cibo o ospitalità: Cervo, Il Pellicano, Septime, Tartine. Sono caratteri da macchina da scrivere (Prestige Elite, Cutive Mono, Pitch Sans) o un grottesco mono (Maison Neue Mono), mai i mono da programmazione.
- **Maiuscolo.** Solo 7 siti mettono i titoli in maiuscolo: Locarno, Cervo, Reschio, Alajmo, Zýmē, Pierre Hermé e Francescana. Gli altri 23 scrivono i titoli in minuscolo, con la sola iniziale maiuscola, e tengono il maiuscolo spaziato per menu, bottoni ed etichette piccole, con spaziature da +0,08 a +0,33em.
- **Pesi.** Nei titoli prevalgono il regular o il leggero. Il grassetto vero nei titoli compare solo in Manincor (Cochin Bold), Gloriette (Eirlys Bold) e Francescana (Roboto Bold). Forestis usa un solo peso Light per tutto; 7132 ha il titolo in Thin.
- **Piattaforme.** WordPress per noma (lo dichiara nel piè di pagina), Osteria Francescana, Tartine e Guffanti; gli ultimi due usano Elementor. Tartine carica Pitch Sans da `wp-content/uploads` e lo assegna nelle tipografie globali di Elementor. Guffanti usa un kit Adobe Fonts dentro Elementor.

## Cosa ricorre per settore

**Hotel di montagna e alpini** (Forestis, Gloriette, Milla Montis, Zirmerhof, Schwarzschmied, Cervo)
- Pesi leggeri: Brandon Text Light, ITC Johnston Light, Optima nova Light, Raleway 300.
- Un serif classico o umanista per i titoli in minuscolo, a 46-72px con interlinea 1,1-1,2: Bembo, Livory, Eirlys, Optima.
- Il menu è quasi sempre in maiuscolo piccolo con spaziatura larga: Milla Montis +0,26em, Schwarzschmied +0,15em, Gloriette +0,13em, Zirmerhof +0,07em.
- Fanno eccezione Cervo, tutto in monospazio, e Forestis, che rinuncia del tutto al serif.
- Non ricorrono gradienti, grassetti o sans geometriche pesanti.

**Terme** (7132, Bad Ragaz)
- Serif contemporanei di tono "Times rivisto" (Stanley, ABC Otto) per titoli grandi, con interlinea 1,0-1,2.
- Bad Ragaz affianca un grottesco neutro per il testo e usa anche il corsivo d'accento su una parola: è il dettaglio che lo fa sembrare generico.

**Alberghi di città storici e piccoli hotel di famiglia** (Locarno, Il Palazzo Experimental, Il Pellicano)
- Un solo carattere espressivo che fa quasi tutto il lavoro: Ogg a Roma, Nantes a Venezia.
- Oppure un sistema "cartaceo" d'epoca: macchina da scrivere, scrittura a mano e didone a Porto Ercole.
- Il carattere richiama un oggetto dell'albergo (biglietti, cartoline, insegne).

**Tenute e agriturismi di alto livello** (Borgo Pignano, Reschio)
- Display serif o sans modulata leggera per i titoli (Sang Bleu Sans Light, Canela Condensed), con un grottesco o un umanista per il testo.
- Reschio porta il condensato in maiuscolo fino a 300px con interlinea 0,9.

**Cantine** (Manincor, Ornellaia, Bründlmayer, Zýmē)
- Il serif da libro domina: Cochin, Garamond, Tobias.
- Il corsivo serve per frasi intere: a Bründlmayer il 44% del testo visibile è corsivo, ma sono citazioni, non parole d'accento.
- La sans, quando c'è, è di servizio (Corporate S, Proxima Nova nei menu).
- Zýmē è l'eccezione veneta: didone gigante in maiuscolo con un grottesco stretto e sottile.

**Distillerie** (Poli; per confronto Nonino e Nardini, sotto)
- Il sito migliore del gruppo, Poli, regge su un solo geometrico d'epoca, Kabel (1927).
- I concorrenti diretti cadono nelle accoppiate da modello: Playfair con Josefin, Raleway con un corsivo calligrafico.

**Ristoranti** (noma, Septime, Osteria Francescana, Alajmo; per confronto St. JOHN)
- I migliori hanno una sola voce: noma è serif anche nel testo e nel menu; Septime è tutto macchina da scrivere e non ha titoli sopra i 24px; St. JOHN usa solo Georgia, di sistema.
- La celebrità non garantisce la tipografia: Francescana ha la combinazione più ordinaria del gruppo (Roboto con Bodoni Moda e Open Sans).

**Pasticcerie** (Pierre Hermé, Tartine; Alajmo vende anche dolci)
- Geometrico tipo Futura (Hermé, Alajmo) o monospazio dattilografico (Tartine).

**Salumi e formaggi** (Joselito, Guffanti)
- Joselito: serif barocco grande con una geometrica, un peso ciascuno.
- Guffanti: una sola famiglia, Apparat, in quattro pesi.

**Ceramica, gioielli, arredo** (Bitossi, Heath, Sophie Buhai, Audo)
- Cataloghi più che siti di marketing: un solo serif anche nei menu (Bitossi), un solo grottesco a 12-16px senza titoli (Sophie Buhai), un old style con un grottesco inglese (Audo).
- Heath ha un sistema a tre ruoli fissi: serif per i titoli, grottesco per tutto il resto, largo per gli eventi.

## Cosa distingue i siti migliori

1. **Poche famiglie, pochi pesi.** Joselito ha due famiglie con un peso ciascuno; Forestis e 7132 una famiglia sola. La gerarchia la fanno dimensione e spazio, non il grassetto.
2. **Il carattere ha una provenienza leggibile.** Septime e Il Pellicano evocano la macchina da scrivere, Manincor le incisioni del Settecento più la sans di Weidemann per Daimler, Heath il libro di scuola americano, Locarno la calligrafia del Novecento, Poli l'Art Déco. Il carattere racconta un'epoca o un oggetto prima ancora del testo.
3. **Il serif anche nel testo lungo.** Quasi metà dei siti non usa una sans per il testo corrente. Nei siti generati la regola implicita è il contrario: serif nei titoli, sans in tutto il resto.
4. **Titoli in minuscolo e senza grassetto.** Il maiuscolo spaziato è riservato a menu ed etichette piccole. Quando i titoli sono in maiuscolo, il carattere è stretto o display (Canela Condensed, Ogg, Didot, The Seasons) e l'interlinea scende a 0,9-1,1.
5. **Spaziatura negativa sui titoli grandi, positiva sul maiuscolo piccolo.** Borgo Pignano -0,03em, noma -0,02em, Joselito fino a -0,03em; menu da +0,08 a +0,33em.
6. **Il corsivo ha un compito fisso:** citazioni intere (Bründlmayer, Gloriette), sottotitoli (Bitossi), link (Ornellaia, Audo). Non una parola evidenziata dentro il titolo; l'unico caso del censimento è Bad Ragaz.
7. **Pochi gradini di dimensione.** Septime si ferma a 24px e Sophie Buhai a 16px; dall'altra parte Reschio arriva a 300px. Nessuno usa la scala modulare "da manuale" con sei titoli diversi in pagina.

## Accoppiate ricorrenti

| Schema | Esempi nel censimento | Versione con caratteri liberi |
|---|---|---|
| Serif rinascimentale o barocco + sans neutra di servizio | Bembo + Raleway, Garamond + Proxima Nova, Cochin + Corporate S, Century Old Style + Grot 12, SangBleu Kingdom + Euclid | EB Garamond + Hanken Grotesk; Fanwood Text + Alegreya Sans; Gelasio + Figtree |
| Una famiglia sola, serif | 7132 (Stanley), Locarno (Ogg), Bitossi (Catalogue), Ornellaia (Tobias, con Triptych solo per i link) | Literata, Gelasio o Gilda Display da soli |
| Una famiglia sola, sans | Forestis (Brandon Text Light), Pierre Hermé (Jost), Guffanti (Apparat), Sophie Buhai (Univers) | Jost Light; Instrument Sans; Public Sans |
| Monospazio da macchina da scrivere, da solo o con un grottesco | Septime, Tartine, Cervo, Il Pellicano | Cutive Mono o Courier Prime; Azeret Mono per i titoli |
| Display ad alto contrasto in maiuscolo + geometrico | Alajmo (The Seasons + Futura PT), Zýmē (Didot + Scale) | Gilda Display + Jost; Bodoni Moda + Sofia Sans Condensed |
| Due sans umaniste di epoche diverse | Milla Montis (Optima nova + ITC Johnston) | Belleza + Cabin |
| Serif editoriale per tutto, sans solo per i comandi | noma (Reckless + Roobert) | Source Serif 4 + Figtree |
| Condensato serif enorme + umanista | Reschio (Canela Condensed + Scala Sans) | Libre Caslon Condensed + Alegreya Sans |

## Alternative libere per i caratteri commerciali

Misure sull'em: altezza della x e larghezza media delle minuscole; il contrasto è il rapporto tra spessore e sottigliezza nella o.

| Commerciale (sito) | Misure originale | Alternativa Google 1 | Alternativa 2 | Cosa si perde |
|---|---|---|---|---|
| Brandon Text Light (Forestis) | x 0,462, larg. 0,479 | **Jost** (x 0,460, larg. 0,466) | Didact Gothic | terminali morbidi, calore |
| Eirlys Bold (Gloriette) | x 0,500, larg. 0,601, contr. 5,9 | **DM Serif Display** (parente di DM Sans, molto vista) | Gloock | grazie "gotiche", svolazzi |
| TT Norms (Gloriette) | x 0,480, larg. 0,503 | **Hanken Grotesk** (larg. 0,504) | Albert Sans | geometria più tonda |
| Optima nova Light (Milla Montis) | x 0,469, contr. 2,8 | **Belleza** (contr. 2,4) | Marcellus | pesi, corsivo, Light |
| ITC Johnston (Milla Montis) | x 0,453, larg. 0,483 | **Cabin** (ispirata a Johnston e Gill) | Alegreya Sans | il peso Light |
| Bembo (Zirmerhof) | x 0,396, larg. 0,447 | **EB Garamond** (x 0,405, larg. 0,437) | Cardo | nitidezza aldina |
| Livory (Schwarzschmied) | x 0,464, larg. 0,513, contr. 2,0 | **Spectral** (x 0,450, larg. 0,502, contr. 2,1) | Gelasio | grazie arrotondate |
| Maison Neue Mono (Cervo) | larg. 0,650 | **Azeret Mono** (larg. 0,650) | Fragment Mono (frequente nei siti Framer) | neutralità |
| Stanley (7132) | x 0,490, larg. 0,509 | **Gelasio** | Tinos (metrica Times) | grazie triangolari, peso Thin |
| ABC Otto (Bad Ragaz) | larg. 0,538, contr. 2,6 | **Brygada 1918** (larg. 0,533, contr. 2,6) | Libre Caslon Text | x più bassa |
| ABC Marfa (Bad Ragaz) | x 0,500, larg. 0,533 | **Instrument Sans** | Public Sans | quasi nulla |
| Ogg (Locarno) | contr. 8,2 | **Gilda Display** | Italiana (contr. 8,2) | il pennino largo, le pance |
| Nantes (Experimental) | x 0,473, contr. 2,9 | **Petrona** | Spectral | terminali a goccia di a e c |
| Prestige Elite (Septime, Pellicano) | larg. 0,600 | **Cutive Mono** (larg. 0,605) | Courier Prime | un po' di nero |
| Sang Bleu Sans Light (Borgo Pignano) | contr. 2,7, maiuscole alte | **Belleza** | Tenor Sans | Light, taglio nervoso |
| PP Neue Montreal (Borgo Pignano) | x 0,510 | **Hanken Grotesk** | Albert Sans | spaziatura stretta da titolo |
| Canela Condensed (Reschio) | larg. 0,329, contr. 5,1 | **Libre Caslon Condensed** (larg. 0,432) | Instrument Serif (abusato) | strettezza e contrasto |
| FF Scala Sans (Reschio) | x 0,453, larg. 0,460 | **Alegreya Sans** (larg. 0,445) | Cabin | larghezze condensate |
| Cochin (Manincor) | x 0,372, x/maiusc. 0,569 | **Fanwood Text** (x 0,385, 0,573) | Sorts Mill Goudy | corsivo ornato, Bold |
| Corporate S (Manincor) | larg. 0,447 | **Alegreya Sans** (larg. 0,445) | PT Sans | asciuttezza |
| Tobias (Ornellaia) | x 0,501, larg. 0,513 | **Gelasio** | Libre Caslon Text | carattere delle curve |
| Triptych (Ornellaia) | larg. 0,583 | **Young Serif** (larg. 0,579, senza corsivo) | Besley | il corsivo |
| Garamond URW (Bründlmayer) | x 0,418, larg. 0,436 | **EB Garamond** (larg. 0,437) | Cardo | quasi nulla |
| Proxima Nova (Bründlmayer) | x 0,483, larg. 0,489 | **Figtree** | Lato (non Montserrat) | dettagli minimi |
| Scale (Zýmē) | larg. 0,308 | **Sofia Sans Condensed** | Archivo Narrow | strettezza estrema |
| Kabel (Poli) | x 0,509 | **Questrial** | Didact Gothic | le stranezze di e, a, g |
| Reckless (noma) | x 0,502, contr. 2,3 | **Source Serif 4** | Gelasio | compattezza da rivista |
| Roobert (noma) | x 0,504, larg. 0,508 | **Figtree** (x 0,500, larg. 0,507) | Albert Sans | nulla nei corpi piccoli |
| The Seasons (Alajmo) | contr. 3,4 | **Gilda Display** | Antic Didone | terminali morbidi |
| Futura PT (Alajmo) | x 0,415 | **Jost** (lo usa Pierre Hermé al posto di Futura) | Josefin Sans | x un po' più alta |
| Pitch Sans (Tartine) | larg. 0,614 | **Sometype Mono** | Courier Prime | sapore da macchina da scrivere |
| SangBleu Kingdom (Joselito) | contr. 4,1 | **Gilda Display** | Antic Didone | nervosità barocca |
| Euclid Circular B (Joselito) | x 0,500, larg. 0,535 | **Albert Sans** (x 0,500, larg. 0,515) | Figtree (non Poppins né Outfit) | minimo |
| Apparat (Guffanti) | x 0,490, larg. 0,514 | **Instrument Sans** | Public Sans | angolosità |
| Catalogue (Bitossi) | larg. 0,576, contr. 1,9 | **Literata** (larg. 0,555, contr. 1,7) | Besley | sapore ottocentesco |
| Benton Sans (Heath) | x 0,527 | **News Cycle** (revival di News Gothic) | Libre Franklin | pesi |
| Century Schoolbook (Heath) | x 0,455 | **Gelasio** | Old Standard TT | aria da libro di scuola |
| Univers (Sophie Buhai) | x 0,502, larg. 0,534 | **Public Sans** | Instrument Sans (non Inter) | sistematicità della famiglia |
| Century Old Style (Audo) | x 0,489, larg. 0,487 | **Gelasio** (x 0,485, larg. 0,499) | Libre Caslon Text | poco |
| Grot 12 (Audo) | larg. 0,441 | **Hanken Grotesk** (più larga) | Familjen Grotesk | strettezza |

**Attenzione alle alternative abusate.** Le misure portano a volte verso caratteri della lista nera:
- Instrument Serif per Canela Condensed;
- Cormorant Garamond per Cochin;
- Montserrat per Proxima Nova;
- Inter per Univers e Neue Montreal;
- Poppins e Outfit per Euclid;
- IBM Plex Mono, l'equivalente Adobe di Pitch Sans secondo Typewolf.

Nel JSON sono segnalati con `abusato_dai_siti_generati: true` o nelle note. Anche DM Serif Display, pur fuori lista, è parente diretto di DM Sans.

Gelasio torna in sei confronti diversi: se diventa la risposta per tutto, diventa il nuovo carattere riconoscibile. Conviene alternarlo con Spectral, Literata, Brygada 1918, Petrona e Libre Caslon Text.

## Gruppo di confronto: siti esaminati e non inclusi

Rilevati con lo stesso metodo, sono utili per vedere che aspetto ha la tipografia "da modello" anche in aziende di prestigio.

| Sito | Caratteri rilevati | Nota |
|---|---|---|
| [Pension Briol](https://www.briol.it/) | Cormorant Garamond + Work Sans (Google) | pensione storica, tipografia generica |
| [Locanda Cipriani](https://locandacipriani.com/) | Cormorant Garamond per tutto (WordPress con Elementor) | il caso Elementor più vicino a quelli del committente |
| [Château Margaux](https://chateau-margaux.com/) | Cormorant Garamond corsivo nei titoli + Brandon Grotesque + Inter (Framer, carica anche Fragment Mono) | anche un Premier Grand Cru cade nel Cormorant corsivo |
| [Grappa Nonino](https://www.grappanonino.it/) | Playfair Display Bold + Josefin Sans | accoppiata da modello |
| [Distilleria Nardini](https://www.nardini.it/) | Raleway + Bickham Script + Hermes | corsivo calligrafico a 80-90px |
| [Pieropan](https://www.pieropan.it/) | Poppins + Bauer Bodoni | Poppins nel testo |
| [Pasticceria Biasetto](https://pasticceriabiasetto.it/) | Montserrat + Allura (WordPress con Elementor) | Padova; il contrario di Pierre Hermé |
| [Loison](https://loison.com/) | KoHo (Google), tutto maiuscolo | Vicenza |
| [QC Terme](https://www.qcterme.com/) | solo Montserrat | terme |
| [Laboratorio Paravicini](https://www.paravicini.it/) | solo Fraunces (Shopify) | ceramica; Fraunces è in lista nera |
| [Alois Lageder](https://aloislageder.eu/) | Amiri, Assistant, Brown, Neue Haas Unica, Miller Text | cinque famiglie senza regia |
| [St. JOHN](https://stjohnrestaurant.com/) | solo Georgia (di sistema) | esempio positivo: nessun file, voce chiarissima |
| [Trippa](https://www.trippamilano.it/) | Georgia + Droid Serif e Droid Sans | trattoria milanese, sito minimale |
| [Vigilius](https://vigilius.it/) | solo ModernGothic | hotel di montagna, una famiglia |
| [The Omnia](https://the-omnia.com/) | Canela Thin maiuscolo + Allianz | Zermatt |
| [Krug](https://www.krug.com/) | Apolline + Gotham + scrittura del marchio su misura | grande marchio, non replicabile |

## Indicazioni pratiche per WordPress ed Elementor

- **Caratteri liberi non Google.** Linux Biolinum (usato da Il Palazzo Experimental) e altri open source si servono in locale con il plugin gratuito [Custom Fonts](https://wordpress.org/plugins/custom-fonts/): oltre 400.000 installazioni attive, compatibile con Elementor secondo la sua pagina.
- **Caratteri Google in locale.** È quello che fanno Osteria Francescana (Bodoni Moda e Roboto nel tema) e Pierre Hermé (Jost): si evita di chiamare il CDN Google e si controllano i pesi.
- **Adobe Fonts** funziona dentro Elementor, come dimostra Guffanti. Sono su Adobe Fonts, tra quelli del censimento: Livory, Novel Sans, Prestige Elite, Rollerscript, Monotype Modern Display, Futura PT, The Seasons, Proxima Nova, Apparat, Century Old Style, Scale e Brandon Grotesque.
- **Caratteri dei temi.** Il tema Shopify di Alajmo carica Cormorant e Jost di serie anche se la pagina non li usa. Lo stesso succede con i temi WordPress: va controllato `document.fonts` sul sito finito.

## Fonti principali

- Riconoscimenti:
  - Guida Michelin: [Forestis](https://guide.michelin.com/us/en/hotels-stays/brixen/forestis-dolomites-11259), [Milla Montis](https://guide.michelin.com/en/hotels-stays/meransen%20/milla-montis-12451), [Schwarzschmied](https://guide.michelin.com/en/hotels-stays/lana/hotel-schwarzschmied-7905), [Cervo](https://guide.michelin.com/us/en/hotels-stays/zermatt/cervo-mountain-boutique-resort-12506), [7132](https://guide.michelin.com/us/en/hotels-stays/vals/7132-hotel-8526), [chiavi Italia: Locarno, Pellicano, Reschio](https://guide.michelin.com/en/article/travel/all-the-key-hotels-italy), [Il Palazzo Experimental](https://guide.michelin.com/fr/fr/hotels-stays/venice/il-palazzo-experimental-9199), [Le Calandre](https://guide.michelin.com/us/en/veneto/rubano/restaurant/le-calandre), [Septime](https://guide.michelin.com/en/ile-de-france/paris/restaurant/septime).
  - The World's 50 Best: [noma 2021](https://www.theworlds50best.com/stories/News/noma-worlds-best-restaurant-2021.html), [vincitori per anno](https://www.theworlds50best.com/stories/News/the-year-they-won-15-years-50-best.html), [Osteria Francescana](https://www.theworlds50best.com/awards/best-of-the-best/osteria-francescana.html).
  - Altri: [Fonts In Use, Heath Ceramics](https://fontsinuse.com/uses/2317/heath-ceramics-website), [Awwwards, Forestis](https://www.awwwards.com/sites/forestis-hotel-dolomites).
- Fonderie: le pagine sono citate nel JSON per ogni carattere. Le descrizioni dei caratteri Google vengono dai file ufficiali `DESCRIPTION.en_us.html` del repository [google/fonts](https://github.com/google/fonts) (per esempio [Cabin](https://raw.githubusercontent.com/google/fonts/main/ofl/cabin/DESCRIPTION.en_us.html), [Cutive Mono](https://raw.githubusercontent.com/google/fonts/main/ofl/cutivemono/DESCRIPTION.en_us.html), [News Cycle](https://raw.githubusercontent.com/google/fonts/main/ofl/newscycle/DESCRIPTION.en_us.html), [Fanwood Text](https://raw.githubusercontent.com/google/fonts/main/ofl/fanwoodtext/DESCRIPTION.en_us.html)). Le alternative Adobe vengono dalle schede Typewolf (per esempio [Ogg](https://www.typewolf.com/ogg), [Canela](https://www.typewolf.com/canela), [Optima](https://www.typewolf.com/optima)).
- Rilevazioni: i CSS e i file dei caratteri dei singoli siti sono elencati nel campo `fonti_caratteri` di ogni voce del JSON.
