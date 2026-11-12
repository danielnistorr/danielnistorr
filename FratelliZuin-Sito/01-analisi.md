# Fratelli Zuin: analisi per la nuova home

Sito: https://www.fratellizuin.it/ (crawl, API WordPress e screenshot del 24/10/2026). Fonti citate come URL + frase. Testi del sito in `_prova/crawl/*.txt`, HTML in `_prova/crawl/*.html`.

## 1. In breve

- Impresa di famiglia di **movimento terra, lavori stradali, demolizioni e aspirazioni industriali** con escavatori a risucchio. Lavora per committenti pubblici (ha l'attestazione SOA per i lavori pubblici) e privati (noleggio cassoni scarrabili, "sistemazioni esterne anche di piccola entità").
- Sede operativa e amministrativa in **Via Bassette 6/A, Padova** (zona est, vicino al casello di Padova Est); sede legale in Via Torre 164, Padova.
- Storia: "La Ditta F.lli Zuin & C. snc nasce nel 1946" (home), fondata "dai tre fratelli Zuin nel cortile della loro casa" con il primo autocarro "DOGE" (azienda). Prima grande demolizione: "l'abbattimento dell'ex Foro Boario di Padova negli anni 1968-69".
- Correzione: la società attuale risulta "Fondazione 1977" nel registro (companyreports.it). Il 1946 è l'inizio dell'attività di famiglia: va bene in pagina come "dal 1946" perché lo scrive l'azienda, ma la data del registro è un'altra.
- Correzione: il sito non ha dieci anni. È un WordPress del **2020** (pagine create a giugno e luglio 2020), fatto su tema comprato e mai aggiornato nei testi ("da oltre 50 anni": nel 2026 sono 80).
- Quanti: nessun dato pubblico su dipendenti o fatturato (snc, nessun bilancio depositato). Nelle foto del sito ci sono almeno sette autocarri cassonati, due escavatori a risucchio, un'autobotte combinata, escavatori Hitachi e una pala CAT.
- Punto di forza nascosto: gli **escavatori a risucchio** ("scavi controllati e ideali per aspirare qualsiasi materiale: liquido, secco, solido e polveri anche in luoghi confinati"), il servizio più raro e più fotogenico, che in home non si vede.

## 2. Il sito di oggi

**Pagine** (menu: Home, Azienda, Servizi, Dove siamo, Contatti; più Privacy policy):
- Home: slider a tutta pagina con due foto, poi "Tre generazioni di esperienza", "Perché scegliere noi", tre servizi con foto.
- Azienda: tre paragrafi (L'inizio, L'evoluzione, I tempi odierni) e due foto.
- Servizi: elenco di nove voci e una galleria a scorrimento di sette foto di mezzi.
- Dove siamo: istruzioni stradali e due cartine GIF disegnate.
- Contatti: recapiti e modulo con consenso privacy.
- Residui del tema: "pagina-di-esempio", articoli "ciao-mondo" e "hello-world" ancora pubblicati (`_prova/crawl/pages.json`, `posts.json`).

**Testi veri essenziali (verbatim):**
- Slider: "F.LLI ZUIN SNC / movimento terra / lavori stradali / ASPIRAZIONI INDUSTRIALI".
- Home: "dal 1946 / tre generazioni di esperienza"; "La Ditta F.lli Zuin & C. snc nasce nel 1946, da oltre 50 anni, tre generazioni di esperienza nel settore del movimento terra e lavori stradali".
- SOA (home): "La Ditta F.LLI ZUIN & C. snc ha ottenuto l'attestazione di qualificazione alla esecuzione dei lavori pubblici dalle SOA (Società di Organismi di Attestazione)." Categorie e classifiche non indicate.
- Movimento terra: "Grazie all'impiego di mezzi moderni ed efficienti, di attrezzature Fratelli Zuin svolge varie lavorazioni."
- Lavori stradali: "Fratelli Zuin si occupa della realizzazione di strade, marciapiedi, piste ciclabili, rotatorie ed inoltre si occupa di manutenzione di strade e autostrade."
- Demolizioni: "l'abbattimento delle strutture avviene utilizzando macchinari quali martelli demolitori e pinze idrauliche."
- Servizi (elenco completo): "demolizioni / urbanizzazioni / noleggio cassoni scarrabili da 2 a 25 mc. / escavatori a risucchio industriali / formazione - sistemazione fognature / lavori stradali / movimento terra / ritiro del materiale proveniente da demolizioni e scavi / sistemazioni esterne anche di piccola entità".
- Azienda, L'inizio: "La Ditta nasce nel primo dopoguerra dai tre fratelli Zuin nel cortile della loro casa. L'attività inizia con il trasporto di materiale da costruzione trasportato con il loro primo autocarro "DOGE" a cui fa presto seguito l'acquisto di altri autocarri ed escavatori."
- Azienda, L'evoluzione: "anche i figli intraprendono la stessa attività entrando nella Società"; "la prima demolizione importante: l'abbattimento dell'ex Foro Boario di Padova negli anni 1968-69. Seguono la demolizione della sede Azienda del Gas di Via Trieste e altri lavori come la Formazione parziale dell'impianto di illuminazione del Prato della Valle sempre a Padova."
- Azienda, I tempi odierni (le macchine): "escavatori cingolati, gommati, mini escavatori, scarrabili anche di piccole dimensioni della larghezza di una automobile in grado di intervenire in qualsiasi situazione e spazio e soprattutto gli innovativi escavatori a risucchio".
- Sulle fiancate dei mezzi (foto gallery3 e gallery5): "ESCAVAZIONI ED ASPIRAZIONI A RISUCCHIO CONTROLLATO".
- Contatti: "Richiedi un preventivo gratuito".
- Nessun lavoro recente, nessun cliente, nessun numero di mezzi, nessuna certificazione oltre alla SOA.

**Tecnologia:**
- WordPress 5.6.22, tema Bridge (con tema figlio), WPBakery, Elementor e Slider Revolution 6.2.15 insieme.
- Caratteri Raleway, Open Sans, Roboto e Roboto Slab da Google, tutte le varianti caricate.
- Fatto da un'agenzia: le immagini decorative della home puntano ancora al dominio di prova "fratellizuin.it.netechlab.it".
- Nessuna meta description; viewport con "user-scalable=no" (impedisce lo zoom); nessun link tel:, solo mailto:.
- Banner cookie col consenso implicito ("Se decidi di continuare a leggere consideriamo che accetti").

**Problemi a 1440** (`_prova/attuale/home-1440.jpg`, `azienda-1440.jpg`):
- Apertura da tema: titolo in maiuscolo sottile e spaziato su foto scurita, pulsante "Maggiori informazioni" generico.
- Sotto, tre colonne foto più testo identiche e molta aria vuota senza contenuto; piede di due righe di testo grigio.
- Gli escavatori a risucchio, il servizio che li distingue, sono solo nella galleria di Servizi.
- Testo fermo al 2020 ("da oltre 50 anni").

**Problemi a 390** (`_prova/attuale/home-390.jpg`, `servizi-390.jpg`):
- Il banner cookie grigio copre un quarto dello schermo e il testo dei servizi.
- Titoli spezzati su tre o quattro righe ("COSA / OFFRONO I / F.LLI ZUIN").
- Il telefono nel piede non si tocca per chiamare; lo zoom è bloccato.

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale nel registro | "FRATELLI ZUIN SNC DI ZUIN ANTONIO, LUIGI, ANDREA & C.", forma "SOCIETA' IN NOME COLLETTIVO" | https://www.companyreports.it/f.lli_zuin_e_c._snc-00259210284 |
| Nome sul sito | "F.lli Zuin snc"; "La Ditta F.lli Zuin & C. snc" | piede di ogni pagina; home |
| P.IVA / CF | "P.IVA 00259210284" (CF uguale) | piede del sito; companyreports.it |
| REA | "REA PD 82662" | companyreports.it |
| ATECO | "42.11.00 - Costruzione di strade e autostrade" | companyreports.it |
| Fondazione | "Fondazione 1977" (registro); "nasce nel 1946" (sito) | companyreports.it; home |
| Sede legale | "Via Torre 164, 35129 Padova" | piede del sito; companyreports.it ("Via Torre, 164 - Padova (PD)") |
| Sede operativa | "Sede operativa e amministrativa: Via Bassette 6/A, 35129 Padova" | piede del sito; dove-siamo |
| Telefono / fax | "Tel.049/625336 - Fax.049/6458813" | piede del sito; contatti |
| Email | "info@fratellizuin.it" | piede del sito; contatti |
| PEC | non trovata (da cercare su INI-PEC) | |
| Capitale sociale | non pubblico (snc) | |
| Stato | "Attiva" | companyreports.it |
| SOA | dichiarata, categorie non indicate | home |
| Orari | non indicati sul sito | |
| Social | nessuno nel codice del sito e nessuno trovato in rete | `_prova/crawl/*.html` |

## 4. Materiale visivo

**Cosa è stato scaricato:**
- 36 file in `assets/originali/` (tutta la libreria media del sito utile, dall'API `wp-json/wp/v2/media`); inventario con misure, soggetto, provenienza, uso attuale e due voti (qualità e forza d'apertura) in `_prova/inventario-immagini.json`.
- Fogli di controllo: `_prova/fogli/foglio1-3.jpg`. Nessun video nel sito.

**Voti delle immagini vere (qualità / apertura):**
- Escavatore a risucchio MAN giallo con allestimento rosso e scritta, 1365x1024 (gallery3): **6 / 6**. Il soggetto più forte e più loro, ma luce bianca piatta e piazzale sporco.
- Retro dello stesso mezzo col tubo ad arco (gallery4): **6 / 5**. Bella forma, sfondo disordinato.
- Allestimento rosso e blu con "Via Bassette 6 - PD" dipinto (gallery5): **6 / 4**. Ottimo dettaglio, inquadratura tagliata.
- Autobotte combinata Iveco rossa (gallery2): **6 / 5**. Pulita e luminosa.
- Aspiratore Sibilla che scarica polvere bianca in montagna (gallery6): **7 / 5**. La più fotografica, ma il marchio in vista è del costruttore e il luogo non è Padova: provenienza da confermare.
- Hitachi arancio che carica un DAF (pagina-iniziale-1, 2000x1099): **6 / 5**. Scena vera, foschia di mezzogiorno.
- Pala CAT 928G sulle macerie (pagina-iniziale-2): **6 / 5**.
- Movimento terra, demolizioni, lavori stradali (1000x800): **6 / 4**, **6 / 4**, **5 / 3**. Vere ma piccole e affollate.
- Operaio in tuta bianca che aspira polveri in un capannone (1365-1024.png): **6 / 4**. Soggetto forte, luce torbida, provenienza da confermare.
- Parco autocarri allineati (gallery1): **5 / 3**. Metà foto è asfalto vuoto.
- Logo: timbro ovale "F.lli ZUIN & C. s.n.c. / MOVIMENTO TERRA / LAVORI STRADALI", raster da scansione 765x463 con bordi frastagliati: **4 / 0**.

**Da non usare mai** (sono nella libreria ma non sono loro): foto di repertorio Unsplash (troy-mortier, elmarie-van-rooyen, jamar-penny, lavori.jpg), stock HDR (header.jpg, macchine-movimento-terra), demo del tema (pale eoliche) e soprattutto una **foto di cronaca delle demolizioni di Triscina in Sicilia** (`1557089209-0-demolizioni-triscina-...jpg`, `demolizioni.jpg`): diritti di un giornale. Oggi nessuna di queste è in pagina.

**Giudizio: materiale 5 su 10, non regge da solo una home di alta gamma.** È vero e riconoscibile (mezzi col loro logo, il rosso dei cassoni, la scritta sul risucchio), ma sono scatti da compatta del 2015-2020, a luce piatta, in piazzali disordinati, al massimo 2000 px, senza persone e senza lavori finiti (strade, rotatorie, piste ciclabili). Per la proposta: gallery3 o gallery2 come oggetto vero se si accetta il limite, segnaposto esterni (sez. 6) per il resto, e nel LEGGIMI un servizio fotografico vero: il risucchio rosso fotografato di tre quarti su piazzale pulito con cielo coperto chiaro, il tubo ad arco in dettaglio, un cassone scarrabile piccolo "della larghezza di una automobile", un lavoro stradale finito visto dall'alto con drone, e le foto d'archivio di famiglia (il DOGE, il Foro Boario).

## 5. Due direzioni artistiche

Ispirazioni Graziella e N19: **non le uso**. Un'impresa di movimento terra non è moda né lusso; il registro giusto è quello delle grandi imprese e dei costruttori di macchine (sez. 7): fatti, mezzi, luce di cantiere, ordine. Ne tengo solo l'idea generale di aria e di un oggetto solo.

**Direzione A: "Il risucchio" (chiara, un solo oggetto)**
- Idea: prima schermata chiara color polvere di cava, con un solo mezzo vero grande e nitido, l'escavatore a risucchio rosso di tre quarti, e il titolo "Scavi controllati, dal 1946"; sotto, poche sezioni: servizi, storia in tre date, chiusura con foto.
- Immagini: i loro mezzi fotografati come prodotti (stile RSP: fondo chiaro, mezzo intero, ombra morbida), dettagli del tubo e della scritta "a risucchio controllato"; in proposta gallery3 e gallery2 schiarite, la benna di AO NURA come alternativa.
- Tipografia: Archivo (Google Fonts, OFL) semi espanso, 600, titolo intorno ai 96 px; testo in Archivo 400 a 18 px; cifre tabellari per "2 a 25 mc" e le date.
- Colore: fondo #F3F1EC, inchiostro #1B1B19, un solo accento rosso cassone #C41E1A (da misurare sul mezzo vero; il rosso del logo è #FF0000), grigio ghiaia #8A877F per le note.
- Gesto: l'elenco delle nove voci dei servizi; al tocco su una voce cambia la sola foto accanto e compare la frase vera di quella voce (nessuna animazione d'ingresso, cambio netto).

**Direzione B: "Padova vista dall'alto" (chiara, documentaria)**
- Idea: la città costruita e rifatta da tre generazioni: prima schermata con una foto zenitale di una rotatoria o di una strada nuova a tutta larghezza, titolo sopra a sinistra "Tre generazioni di strade a Padova"; poi la storia in quattro tappe vere (1946 il DOGE, 1968-69 Foro Boario, Azienda del Gas di Via Trieste, Prato della Valle).
- Immagini: drone a picco su lavori finiti e cantieri (segnaposto Iain, Mowinkel, McLendon, Delputte), foto d'archivio di famiglia in bianco e nero da chiedere, i mezzi veri solo nella sezione servizi.
- Tipografia: Bricolage Grotesque (Google Fonts, OFL) per i titoli, 700, compatto; IBM Plex Mono (OFL) per date, indirizzi e "mc"; testo in Bricolage 400.
- Colore: bianco calce #F7F6F2, asfalto #232321 solo per il testo e il piede, giallo segnaletica #E8B10F come unico accento sottile, rosso logo solo nel logo.
- Gesto: una riga di quattro anni; al tocco su un anno si apre sotto una sola riga di testo vero e la foto d'archivio corrispondente (bottone vero, tastiera compresa).

## 6. Immagini sostitutive

Nove foto Unsplash in `assets/esterne/`, 2400 px sul lato lungo (1600-1772 sul corto per le verticali). Licenza verificata sulla pagina di ogni foto il 24/10/2026; autori e URL in `assets/CREDITI.md`; nessuna è già in un'altra home della campagna.
- Aspirazioni: squadra sotto il tubo di un escavatore a risucchio, bianco e nero (Hanlin Sun).
- Oggetto unico per A: benna di escavatore frontale su cielo chiaro (AO NURA).
- Lavori stradali: rulli rossi e vibrofinitrice su asfalto nuovo (Wolfgang Weiser).
- Dall'alto per B: rotatoria nuova e incrocio con marciapiedi (Iain, due foto); escavatore e autocarro su strada demolita (Brandon Mowinkel); cantiere di movimento terra con dumper (Shane McLendon); scavo in una via stretta tra le case (Eduard Delputte).
- Demolizioni: escavatore che abbatte un edificio in mattoni (Bruno BD).

## 7. Riferimenti di alta gamma

Prima schermata a 1440x900 e 390x844 in `riferimenti/<nome>-1440.jpg` e `-390.jpg` (JPEG 78).

1. **RSP**, costruttore tedesco di escavatori a risucchio (rsp-germany.com)
   - Alta gamma: il mezzo fotografato come un prodotto su fondo grigio chiaro, nitido, intero, con nome grande accanto; è esattamente "un oggetto vero e bello" e riguarda lo stesso mezzo di Zuin (RSP ha un rappresentante a Campodarsego, fonte infobuild.it).
   - Da non riprendere: la griglia a quattro riquadri con nastri arancio "Mehr erfahren", il bottone telefono fisso, troppi annunci insieme.
2. **KIBAG**, materiali e costruzioni, Svizzera, dal 1926 (kibag.ch)
   - Alta gamma: persone vere della squadra in divisa davanti al mezzo, servizio fotografico vero, marchio forte, "100 est. 1926" come prova di durata (paragonabile al 1946 di Zuin).
   - Da non riprendere: il riquadro blu sopra la foto e le tre card coi servizi, foto troppo piena.
3. **Boskalis**, dragaggi e lavori marittimi (boskalis.com)
   - Alta gamma: una sola foto aerea luminosa e lunga, il lavoro visto dall'alto come un paesaggio: modello per la direzione B.
   - Da non riprendere: titolo maiuscolo bianco con ombra sopra la foto, bottone giallo, barra di servizio grigia.
4. **Van Oord**, lavori marittimi (vanoord.com)
   - Alta gamma: un solo mezzo enorme fotografato bene, titolo grande e sicuro, menu di cinque voci.
   - Da non riprendere: il titolo su sei righe sopra la foto e il fondo blu scuro; il riquadro "Highlighted" in basso.
5. **Sennebogen**, macchine per movimentazione (sennebogen.com)
   - Alta gamma: la macchina intera in luce di giorno su cielo chiaro, verde di marca coerente ovunque.
   - Da non riprendere: barra verde piena, titolo con contorno e ombra, quattro schede inclinate in basso, troppe icone laterali.

## 8. Per il piede

- **Logo** (miglior qualità trovata): `assets/originali/logo-zuin-nero-765x463.png` e `logo-zuin-bianco-765x463.png` (logo_zuin2.png e logo_zuin.png del sito), più `logo-zuin-rosso-favicon-512.png` (icona del sito, rosso #FF0000). Nessun SVG nel codice, nessun PDF o catalogo. È la scansione di un timbro ovale con lettere arrotondate e bordi frastagliati: un SVG va ridisegnato a mano e approvato, altrimenti si usa il PNG a 2x (765 px bastano per un logo a 180-300 px).
- **Voci di menu e pagine di oggi**: Home, Azienda, Servizi, Dove siamo, Contatti, Privacy policy (la cookie policy è dentro la privacy policy). Pagine da prevedere nel sito nuovo, da elencare nel LEGGIMI: Azienda (storia), Servizi con le nove voci (o le quattro famiglie: movimento terra, lavori stradali, demolizioni, aspirazioni), Noleggio scarrabili, Dove siamo, Contatti, Privacy, Cookie.
- **Colonne possibili**: Azienda (Chi siamo, La storia dal 1946, Dove siamo); Servizi (Movimento terra, Lavori stradali, Demolizioni, Escavatori a risucchio, Fognature, Noleggio cassoni scarrabili); Contatti (telefono con tel:, fax, email con mailto:, sede operativa con link alla mappa, sede legale). Niente colonna Seguici: **nessun social** esiste.
- **Newsletter: non ha senso.** Nessuna notizia, fiera, catalogo o collezione; i clienti sono enti e imprese che chiamano per un preventivo, e i privati chiedono un cassone o un piccolo lavoro, non aggiornamenti periodici.
- **Riga legale**: FRATELLI ZUIN SNC DI ZUIN ANTONIO, LUIGI, ANDREA & C. (oppure "F.lli Zuin & C. snc" come sul sito, da decidere con loro), P.IVA 00259210284, REA PD 82662; capitale sociale non pubblico (snc); PEC non trovata; Privacy, Cookie.

## 9. Da confermare

- Anno: il sito dice 1946, il registro "Fondazione 1977". In pagina "dal 1946" e "tre generazioni" come scrive l'azienda; chiedere se va detto anche altro.
- Nome da mostrare nel piede: ragione sociale completa del registro o "F.lli Zuin & C. snc" del sito.
- SOA: categorie, classifiche e scadenza dell'attestazione (verifica su ANAC o richiesta all'azienda); prima di confermarle in pagina si scrive solo "attestazione SOA per i lavori pubblici".
- Numero di mezzi, di escavatori a risucchio e di persone: nessun dato pubblico, non scrivere numeri.
- Provenienza delle foto gallery6 e 1365-1024-1 (aspiratore Sibilla in montagna) e 1365-1024.png (operaio che aspira in un capannone): loro cantieri o foto del costruttore?
- PEC, orari di ufficio e di apertura del piazzale, numero di cellulare per le urgenze se esiste.
- Fax 049/6458813 ancora attivo?
- "Manutenzione di strade e autostrade": chiedere un paio di lavori recenti veri da citare (committente, luogo, anno) e foto.
- Foto d'archivio di famiglia (autocarro DOGE, Foro Boario 1968-69, Azienda del Gas di Via Trieste, Prato della Valle) e permesso di pubblicarle.
- Logo: va ridisegnato in vettoriale? Serve un file originale dalla tipografia o dal carrozziere che dipinge i mezzi.
- Servizio fotografico vero dei mezzi e di un lavoro finito (vedi sez. 4) per sostituire i segnaposto.
