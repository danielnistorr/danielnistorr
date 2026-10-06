# 01. Analisi del sito attuale (www.walles.it)

Analisi del 6 ottobre 2026. Legenda: **[Certo]** visto nella fonte, **[Probabile]** inferenza forte, **[Ipotesi]** da verificare con il cliente, **[DA CONFERMARE]** dato non verificabile da fonti pubbliche (va nel LEGGIMI).

Materiale di lavoro (fuori da git): crawl completo in `_prova/crawl/` (pagine IT e EN, mirror di tutte le risorse in `sito/`, fonti esterne in `fonti/`), testi estratti in `_prova/testi-verbatim.txt`, screenshot e misure in `_prova/attuale/` (`misure.json` dalla rete reale, `misure-screenshot.json` dal giro degli screenshot), inventario in `_prova/inventario-immagini.json`.

## In breve

- Sito PHP fatto a mano in stile 2010 (doctype XHTML 1.0, jQuery 1.4.2 del 2010, script Dreamweaver `MM_swapImage`, foglio `ie7.css` per Internet Explorer 7), con contenuti fermi e senza meta viewport: **a 390 px la pagina è larga 1001 px e viene rimpicciolita al 39%** (i paragrafi da 13 px arrivano a circa 5 px). Da computer è sobrio e ordinato: testata nera, fondo verde acqua sfumato, scarpa al centro. [Certo]
- È il sito di un calzaturificio vero, non di un rivenditore: **tre marchi propri** (Walles Club, Fratelli Giacometti, Marmolada), **quattro costruzioni dichiarate** (Goodyear, Norvegese, Mocassino tubolare, Blake) più le finiture a mano, e uno **spaccio aperto al pubblico** a Rossano Veneto con orari. [Certo]
- Patrimonio fotografico coerente ma piccolo: **42 foto prodotto 800x600** sullo stesso fondo verde acqua (con il codice modello stampato dentro la foto), **15 foto di lavorazione** a 534 px di altezza, 3 foto della sede a 802 px, 1 foto dello spaccio a 800 px. **Nessuna immagine supera gli 802 px**: niente è utilizzabile a tutta larghezza. [Certo]
- I testi istituzionali sono buoni e precisi sul mestiere (guardolo, increna, cucitura a treccia, piegoline): il nuovo sito li tiene, corretti. Tre testi di collezione esistono solo **dentro immagini** (e in commenti HTML nascosti). [Certo]
- Dati societari incoerenti: il piè di pagina riporta la P.IVA giusta (04576870242, WALLES SRL), ma "info legali" e la privacy policy indicano ancora **P.IVA 01518980246**, che nel registro LEI oggi è **FRATELLI GIACOMETTI SRL** di Bassano del Grappa (già WALLES S.R.L., cambio di nome dal 18 marzo 2025). [Certo]

## Pagine esistenti

La lingua si cambia con un modulo POST (`langch=it|en`) e una sessione PHP: le pagine inglesi hanno lo stesso URL delle italiane, tranne le tre collezioni. Nessuna sitemap, nessun robots.txt (entrambi 404).

| Pagina | URL | Contenuto | Stato |
|---|---|---|---|
| Home | `/` (anche `/index.php`) | slideshow di 3 foto 800x600 (Marmolada, Fratelli Giacometti, Walles Club) con il nome del marchio sotto, icone Instagram e Facebook | nessun testo, nessun H1 |
| Azienda | `/calzaturificio.html` | titolo, sottotitolo inglese, un paragrafo, 3 miniature 220x147 che aprono foto 802x534 | ok |
| Collezione | `/collezioni-walles.html` | frase introduttiva, 3 loghi 220x147 con motto | ok |
| Walles Club | `/collezione-walles-club.html` (EN `/collection-walles-club.html`) | galleria a miniature: cartello di testo + 13 foto modello | testo solo in immagine |
| Fratelli Giacometti | `/collezione-fratelli-giacometti.html` (EN `/collection-fratelli-giacometti.html`) | cartello + 10 foto modello | testo solo in immagine |
| Marmolada | `/collezione-marmolada.html` (EN `/collection-marmolada.html`) | cartello + 12 foto dello scarpone FG105 | testo solo in immagine |
| Lavorazione | `/lavorazioni-calzature-walles.html` | 5 schede a scomparsa (Goodyear, Norvegese, Mocassino tubolare, Blake, Finiture), 3 foto ciascuna | ok, 6 H1 nella stessa pagina |
| Social Wall | `/social-wall.html` | pagina Facebook incorporata + widget Instagram Elfsight | dipende da servizi esterni |
| Contatti | `/contatti-walles.html` | modulo (nome, oggetto, email, messaggio) + dati aziendali | modulo senza informativa |
| Outlet | `/outlet-walles.html` | foto dello spaccio, orari, indirizzo, telefoni, mappa statica che apre Google Maps | link "Ivana" rotto |
| Info legali | `/it/struttura/info.html` (EN `/en/struttura/info.html`), aperta in lightbox | dati societari e avvertenze sul copyright | P.IVA di un'altra società, CSS 404 |
| News | `/news-walles.html` | voce di menu commentata | 301 verso la home |
| Whistleblowing | `/Procedura_Whistleblowing.pdf` | procedura D. Lgs. 24/2023, Rev. 02 del 26/01/2024, 9 pagine | ok, da conservare |

Domini collegati [Certo]: `walles.it` senza www risponde 200 con la stessa home (non reindirizza a www); `fratelligiacometti.com` e `fratelligiacometti.it` (anche con www) servono lo stesso identico sito (stessi 13.220 byte) e sono nel certificato; `www.walles.com` mostra la pagina predefinita di Plesk; `www.walles.it/admin/` reindirizza a `/admin/login.php` (pannello del sito, non provato oltre).

## Testi reali (verbatim, con i refusi originali)

Tutti i testi visibili sono in `_prova/testi-verbatim.txt` (IT e EN). Qui quelli che il nuovo sito userà.

**Testata e piè di pagina (tutte le pagine)**
1. Menu: "Azienda / Collezione / Lavorazione / Social Wall / Contatti / Outlet", lingue "it / en".
2. Piè di pagina: "WALLES SRL Unipersonale - P.IVA e C.F. 04576870242 · info legali - Privacy policy - Cookie policy - Whistleblowing".
3. Home, didascalie dello slideshow (testo `alt` mostrato sotto la foto): "Marmolada", "Fratelli Giacometti", "Walles Club".
4. Meta description (uguale su tutte le pagine): "Calzaturificio Walles - Dal 1959 Walles realizza calzature, scarpe di qualità secondo metodi tradizionali utilizzando una lavorazione artigianale italiana. Marchi Marmolada, Fratelli Giacometti e Walles Club".

**Azienda** (`/calzaturificio.html`)
5. Titolo: "Calzaturificio Walles" / sottotitolo in inglese anche nella versione italiana: "Classic style footwear made in Italy".
6. "Dal 1959 Walles realizza calzature di qualità secondo metodi tradizionali utilizzando una lavorazione artigianale italiana. Passato e futuro, passione e capacità imprenditoriale sono le basi per il successo del marchio, conosciuto per le sue calzature comode e pregevoli che portano con orgoglio il valore della tradizione, dello stile e della cultura italiana nel mondo. Oggi, dopo tre generazioni, i fratelli Giacometti guidano l'azienda unendo, ai valori irrinunciabili della tradizione e dell'esperienza, la conoscenza del mercato e la capacità di guardare avanti. Il cuore dell'azienda resta legato alla sapiente capacità del fare: i principi e le conoscenze che hanno radici nell'artigianalità sono un patrimonio forte, perfezionato ed affinato nel corso degli anni. Ogni fase viene eseguita con estrema cura, ogni gesto racconta la passione per i piccoli particolari che fanno la differenza. Ma è soltanto indossando una calzatura Walles che si scoprono la sua massima comodità e adattabilità al piede."

**Collezione** (`/collezioni-walles.html`)
7. "Dalle mani esperte di qualificati artigiani italiani, dai rigorosi metodi di lavorazione Goodyear, Blake, Norvegese, Mocassino tubolare nascono collezioni estremamente confortevoli dallo stile inconfondibile:"
8. Motti dei marchi: Walles Club "Il valore dell'eleganza"; Fratelli Giacometti "La tradizione artigianale e il gusto internazionale"; Marmolada "Lo stile indiscutibilmente di tendenza".

**Testi delle collezioni** (oggi solo dentro le immagini `intro.jpg` e in commenti HTML non visibili; trascritti dall'immagine e confrontati col commento)
9. Walles Club, "Il valore dell'eleganza": "Scegliere una calzatura Walles Club significa scegliere uno stile, una cultura e una tradizione fatta di dettagli spesso impercettibili, sempre irrinunciabili. I modelli in pellami pregiati ed esotici come coccodrillo, tejus, struzzo rappresentano l'accordo perfetto tra eleganza classica e attualità, ricerca di raffinatezza e armonia, nel rispetto delle norme internazionali CITES sul commercio delle specie selvatiche."
10. Fratelli Giacometti, "La tradizione artigianale e il gusto internazionale": "Ogni calzatura firmata Fratelli Giacometti è espressione di equilibrio ed eleganza senza tempo, uno specchio della personalità. L'ulilizzo della lavorazione Goodyear a mano, l'accuratezza nella scelta dei pellami migliori, unite all'eleganza rinnovata delle forme e alle finiture raffinate contribuiscono allo stile inconfondibile di questi modelli, veramente confortevoli e di lunga durata."
11. Marmolada, "Lo stile indiscutibilmente di tendenza": "Le calzature Marmolada sono dedicate a un mondo di appassionati che apprezzano la lavorazione a mano, l'esclusività dei materiali, il tocco provocante delle colorazioni e delle finiture vintage. Per questa linea i maestri calzolai Walles utilizzano tecniche di lavorazione storiche, eseguendo ogni fase con grande abilità. La lavorazione Norvegese, realizzata secondo tradizione esclusivamente a mano, è evidenziata dalla tipica cucitura a treccia. La colorazione a mano personalizzata su qualsiasi tipo di pellame e i trattamenti vintage regalano ad ogni calzatura un fascino unico e una indiscutibile personalità."
12. Testo stampato in ogni foto prodotto: "MODELLO <codice> / DESCRIZIONE Versione <n>" (codici in "Cosa fanno o vendono").

**Lavorazione** (`/lavorazioni-calzature-walles.html`)
13. Introduzione "Lavorazione": "Ogni scarpa realizzata a mano è un capolavoro pronto a sfidare il tempo. Porta con sé il fascino di lavorazioni che hanno secoli di storia, l'orgoglio di una cultura del fare che non è stata eguagliata dall'innovazione."
14. Goodyear, "La tecnica di lavorazione "a guardolo"": "Una calzatura perfetta, estremamente confortevole ed elegante, fatta per durare. Per la sua realizzazione Walles utilizza una lunga e delicata lavorazione di origine inglese, garanzia di eccezionale qualità: il metodo Goodyear. Nella lavorazione Goodyear il guardolo, una striscia di cuoio morbido, viene cucito al labbro dell'increna del sottopiede di cuoio, fissando insieme anche la tomaia e la fodera. Poi viene applicata e cucita la suola. Nell'intercapedine tra sottopiede e suola è collocata un'intersuola riempitiva. Il risultato finale, semplicemente perfetto, premia la grande abilità e l'estrema precisione necessari in questa tecnica di lavorazione."
15. Norvegese, "Il fascino di una lavorazione completamente a mano": "La Norvegese è una delle tecniche più complesse di costruzione: è una lavorazione laboriosa, che richiede tempi molto lunghi, fatta esclusivamente a mano. La sua realizzazione inizia dopo che la tomaia è stata abilmente sagomata sulla forma. Occorrono due cuciture per completare l'opera: la prima cucitura lega la tomaia al sottopiede, la seconda lega la tomaia alla suola. Il risultato è il profilo a treccia che disegna il bordo della scarpa con un tratto marcato e deciso ed offre una scarpa robusta e solida, pronta a sfidare il tempo."
16. Mocassino tubolare, "Una lavorazione avvolgente come un guanto": "Questa lavorazione è la quintessenza della morbidezza e della flessibilità. È realizzata da mani esperte con padronanza della tecnica artigianale, utilizzando pelli leggere ed elastiche, indispensabili per portare a termine con precisione questo tipo di lavorazione. Grazie alla cucitura su forma questa scarpa avvolge il piede nel modo più naturale, offrendo comodità di calzata e robustezza per camminare in piena libertà. Nella lavorazione tubolare la tomaia sale dal fondo fino a coprire i fianchi, e viene fissata allo specchio mediante una fitta serie di piegoline con la tipica cucitura eseguita a mano. All'interno della scarpa, che ormai ha già preso forma, viene inserito il sottopiede, mentre la suola viene applicata e cucita per ultima."
17. Blake, "La lavorazione per l'eleganza perfetta": "Nella lavorazione Blake l'assemblaggio della suola, del sottopiede e della tomaia avviene in un unico passaggio mediante una cucitura. Per eseguire questa operazione la scarpa deve essere tolta dalla forma. Viene poi rimessa in forma per completare le fasi successive: l'applicazione del tacco, la fresatura, la molatura e la tintura. Il risultato è una scarpa esteticamente perfetta, solida e confortevole."
18. Finiture, "Il tocco esclusivo Walles": "La colorazione è il tocco finale che esalta la complessa manualità di una lavorazione artigianale. Creme, colori, lucidi si alternano in un procedimento ancora una volta articolato in varie fasi. Spruzzato, scurito, sfumato, il colore viene applicato in modo da ottenere nuance originali ed esclusive che esaltano la vera personalità della scarpa. Il trattamento di finitura vintage, realizzato con tecniche esclusive, regala ad ogni calzatura un aspetto particolarmente vissuto, con effetto dall'invecchiamento al vintage estremo, ricco di fascino e storia."

**Contatti** (`/contatti-walles.html`)
19. Modulo: "Nome e Cognome (* campo richiesto) / Oggetto / E-mail (* campo richiesto) / Messaggio (* campo richiesto) / Invia messaggio".
20. "Dati aziendali / WALLES SRL Unipersonale / Via Ramon 70/D / 36028 Rossano Veneto (VI) Italia / Tel. +39 0424 540888 / Fax +39 0424 540890 / Ivana +39 328 3225066 / info@walles.it / P.IVA e C.F. 04576870242".

**Outlet** (`/outlet-walles.html`)
21. "Apertura / Lunedì: Chiuso / Martedì - Venerdì: 14.00 - 19.00 / Sabato: 9.00 - 13.00 / Domenica: Chiuso / Via Ramon 70/D - 36028 Rossano Veneto (Vicenza) / Tel. : +39 0424 235890 | Mail : outlet@walles.it | Ivana +39 328 3225066 / (clicca sulla mappa per ingrandirla)".

**Info legali** (`/it/struttura/info.html`)
22. "Dati societari / Ragione Sociale: Walles Srl / Sede Sociale: via Ramon 70/III - Rossano Veneto (VI) - Italy / P.IVA: IT01518980246", seguito da "Avvertenze su diritti d'autore e marchi registrati" (testo standard).

**Social Wall**: solo i titoli "Social Wall", "Facebook", "Instagram".

**Versione inglese**: traduzione completa delle stesse pagine (Company, Collections, Working, Contacts, Outlet); i cartelli delle collezioni in inglese sono le immagini `intro_en.jpg`.

Refusi e incoerenze da non riportare:
- "L'ulilizzo" (Fratelli Giacometti) per "L'utilizzo"; "l'estrema precisione necessari" (Goodyear) per "necessarie"; "Tel. :" e "Mail :" con lo spazio prima dei due punti.
- Sottotitolo inglese "Classic style footwear made in Italy" nella pagina italiana; voce "Lavorazione" al singolare per cinque lavorazioni.
- Inglese: "savoir-fare", "Messagge", "its has been effected", "Mocassin", "the asides"; la pagina Norwegian dice che la prima cucitura lega la tomaia "onto the leather sole" mentre l'italiano dice "al sottopiede".
- Il nome compare in quattro forme: "Calzaturificio Walles", "WALLES SRL Unipersonale", "Walles Srl", "Logo Walles s.r.l.". Nel nuovo sito: **Walles S.r.l.** per i dati legali, **Calzaturificio Walles** come nome d'uso. [DA CONFERMARE col cliente]
- Indirizzo in due forme: "Via Ramon 70/D" (piè di pagina, contatti, outlet, VIES) e "via Ramon 70/III" (info legali, privacy, commenti HTML). Si usa **Via Ramon 70/D**.
- Parole dei testi originali da riscrivere perché in `PAROLE_VIETATE`: "passione" (Azienda, due volte), "eccezionale" (Goodyear).

## Cosa fanno o vendono

**Calzaturificio di calzature classiche da uomo** con produzione propria a Rossano Veneto (VI). [Certo, sito e Registro Imprese: ATECO 15.20.1 Fabbricazione di calzature]

Marchi propri, dichiarati sul sito (meta description, pagina Collezione) [Certo]:

| Marchio | Motto sul sito | Cosa mostra la galleria | Costruzione citata |
|---|---|---|---|
| **Walles Club** | "Il valore dell'eleganza" | 13 modelli visibili (+5 nascosti): mocassini, monk, oxford, derby, chelsea; pellami esotici (coccodrillo, struzzo, lucertola, rettile) e vitello anticato | pellami esotici "nel rispetto delle norme internazionali CITES" |
| **Fratelli Giacometti** (logo "F.LLI Giacometti, MADE IN ITALY") | "La tradizione artigianale e il gusto internazionale" | 10 modelli visibili (+2 nascosti): oxford, doppia fibbia, polacchino in camoscio, mocassino con nappine, derby full brogue | "lavorazione Goodyear a mano" |
| **Marmolada** | "Lo stile indiscutibilmente di tendenza" | 12 versioni dello stesso scarpone da montagna FG105: cuoio anticato, invecchiato bianco e grigio, struzzo, camouflage, decori dipinti | "lavorazione Norvegese, realizzata secondo tradizione esclusivamente a mano", "cucitura a treccia" |

Codici modello letti nelle foto [Certo]: Walles Club 01405, 72410, 82407, 82404, 01104, 72149, 71118, 43116, 92152, 0365, 72177, 66201, 92159, 0413, 34106, 161106, POL1, POL2; Fratelli Giacometti FG231, FG241, FG221 (due foto), FG235, FG132, FG180, 0365 versioni 1-3, FRANGIA, GA versione 305; Marmolada FG105 versioni 1-12. Nessun prezzo, nessuna scheda, nessuna vendita online.

Lavorazioni descritte [Certo]: Goodyear (a guardolo), Norvegese (a mano, due cuciture, profilo a treccia), Mocassino tubolare (cucitura su forma, piegoline cucite a mano), Blake (cucitura unica fuori forma), Finiture (colorazione a mano spruzzata, scurita, sfumata; finitura vintage).

**Spaccio aziendale (Outlet)** aperto al pubblico in Via Ramon 70/D: martedì-venerdì 14.00-19.00, sabato 9.00-13.00, lunedì e domenica chiuso; tel. +39 0424 235890, outlet@walles.it. Google Maps conferma l'orario del martedì 14-19. [Certo] Cosa si vende allo spaccio (fine serie, campionari, prezzi) non è scritto da nessuna parte. [DA CONFERMARE]

Da fonti terze, da confermare prima di usarle [Ipotesi]:
- Fashion Press (Giappone, scheda marchio F.lli Giacometti): l'azienda è guidata da **Luigino Giacometti** (presidente e controllo qualità) e **Roberto Giacometti** (modelli, forme e montaggio); la tradizione di famiglia risale al lavoro a domicilio del nonno negli **anni 1890**; oltre ai marchi propri produce per **marchi terzi di alta gamma**; F.lli Giacometti e Marmolada sono venduti in Giappone da **Isetan Shinjuku Men's** e **Hankyu Men's Osaka**. [DA CONFERMARE]
- Il sito dice "Dal 1959" e "dopo tre generazioni": la data 1959 è dell'azienda, non verificata altrove. [DA CONFERMARE]

## Immagini usate oggi

Tutte scaricate alla massima risoluzione trovata in `assets/originali/` (78 file, 4,6 MB, `manifest.json` con URL di origine e sha1). Inventario completo con soggetto, qualità e larghezza massima in `_prova/inventario-immagini.json`. Nessuna versione più grande trovata: provati i nomi `_big`, `/big/`, `_hd`, numerazioni mancanti, cataloghi PDF (tutti 404). La Wayback Machine non è raggiungibile da questo ambiente (connessione chiusa dal proxy, `archive.org` risponde 429): da riprovare.

| Tipo | Quantità | Misura | Larghezza massima senza sgranare (1x / retina) | Giudizio | Uso nel nuovo sito |
|---|---|---|---|---|---|
| Foto prodotto delle tre collezioni, fondo verde acqua sfumato, luce da studio | 42 (35 visibili, 7 nascoste nei commenti) | 800x600 | 680 / 340 px (va tolto il testo stampato a destra) | nitide, fondo pulito, stesso set: è l'identità visiva del marchio. Il codice "MODELLO / DESCRIZIONE" è dentro la foto (x 690-770, y 255-355) | griglie prodotto a 3-4 colonne; il testo va coperto ricreando il fondo liscio o tagliando a 680 px |
| Slideshow home (scarpa singola o paio su verde acqua) | 4 (una commentata) | 800x600 | 800 / 400 px | molto spazio vuoto attorno, buone per ritagli larghi e bassi | aperture a mezza larghezza; non a tutta pagina |
| Foto di lavorazione (mani, mole, macchine Goodyear e Blake, pelli appese, tinture) | 15 | 354-802 px di larghezza, 534 di altezza (finiture1 640x480); 6 verticali da 354-401 px | 802 / 401 px al massimo; le verticali 355 / 177 px | autentiche e vive, colore e contrasto buoni; JPEG compressi (20-76 kB) | blocchi foto a mezza colonna o griglie da 3, mai a tutta larghezza |
| Foto della sede (esterno con bonsai potati a nuvola, uffici open space, montaggio in forma) | 3 | 802x534 | 802 / 401 px | l'esterno e il montaggio sono buoni, gli uffici poco caratterizzanti | Azienda: due foto a mezza colonna |
| Spaccio | 2 | 800x533 e 300x451 | 800 / 400 e 300 / 150 px | grandangolo con distorsione; la seconda è vecchia e non collegata | pagina Outlet a mezza colonna |
| Cartelli di testo delle collezioni (IT e EN) | 6 | 800x600 | non usare come immagini | testo chiuso in immagine | testi trascritti sopra, da rimettere in HTML |
| Loghi (Walles Club in testata 143x95, tre loghi marchio 220x147) | 4 | 143-220 px | 220 / 110 px | JPEG con bordi impastati, nessun vettoriale | servono i vettoriali dal cliente; nel frattempo ridisegno solo come segnaposto dichiarato |
| Mappa statica (ritaglio Google) | 1 | 200x150 | non usare | screenshot di mappa | sostituire con indicazioni testuali e link a Maps |
| Sfondo gradiente | 1 | 1024x769 | si ricrea in CSS | colore di riferimento **#93B1AF** (verde acqua) su testata **#000000**, Georgia | colore da valutare in 02 |

Foto esterne (`assets/esterne/manifest.json`): sulla scheda Google Maps "Calzaturificio Walles (S.R.L.)" (rivendicata dal proprietario, categoria Calzaturificio, voto 4,6) il payload pubblico espone una sola foto, di un utente (17 giugno 2024, 3024x4032, interno dello spaccio con scarponi appesi): solo riferimento, non usabile senza permesso. Facebook (400 senza login) e Instagram (429) non accessibili: nessuna foto. Nessun catalogo PDF pubblicato.

Giudizio: per il nuovo sito il materiale è **sufficiente per griglie prodotto e blocchi a mezza colonna, insufficiente per aperture a tutta larghezza**. Da chiedere al cliente gli originali dello shooting prodotto (le foto sono ritagli 800x600 di scatti da studio, l'originale è certamente più grande) e delle foto di lavorazione, e i loghi vettoriali. [Probabile]

## Problemi tecnici da segnalare al cliente

Misure prese il 6 ottobre 2026 con Chromium (Playwright) e curl. Le richieste fallite per "connection reset" del proxy di questo ambiente sono state ripetute e **non** sono contate come errori del sito.

MISURE_QUI

## Dati aziendali

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | WALLES SRL (sul sito: "WALLES SRL Unipersonale") | sito (piè di pagina, Contatti); aziende.it (dati Registro Imprese) [Certo] |
| P.IVA e C.F. | 04576870242 | sito; aziende.it; VIES citato da aziende.it [Certo] |
| REA | VI-414376 | aziende.it [Certo] |
| Forma e capitale | S.r.l., capitale sociale 100.000 euro | aziende.it [Certo] |
| ATECO | 15.20.1 Fabbricazione di calzature | aziende.it [Certo] |
| Sede | Via Ramon 70/D, 36028 Rossano Veneto (VI) | sito; aziende.it; Google Maps ("Via Ramon, 70") [Certo] |
| Telefono | +39 0424 540888; fax +39 0424 540890 | sito (Contatti); Google Maps (stesso numero) [Certo] |
| Cellulare | "Ivana" +39 328 3225066 | sito (Contatti, Outlet) [Certo]; chi sia Ivana e se va pubblicato [DA CONFERMARE] |
| Email | info@walles.it; spaccio outlet@walles.it | sito [Certo] |
| PEC | walles@legalmail.it | aziende.it (Registro Imprese) [Certo] |
| Codice SDI | SUBM70N | aziende.it [Certo] |
| Fatturato 2025 | 18.266.405 euro (fascia 10-25 milioni), utile 175.584 euro | aziende.it, bilancio 2025, aggiornamento 7 luglio 2026 [Certo] |
| Dipendenti | 104 (2025), fascia 100-249 | aziende.it [Certo] |
| Orari spaccio | martedì-venerdì 14.00-19.00, sabato 9.00-13.00, lunedì e domenica chiuso | sito; Google Maps (martedì 14-19) [Certo] |
| Orari uffici | non pubblicati | [DA CONFERMARE] |
| Anni di attività | "Dal 1959" (sito); "tre generazioni" (sito) | solo il sito [DA CONFERMARE] |
| Società collegata | FRATELLI GIACOMETTI SRL, C.F. 01518980246, Via C. Colombo 102, Bassano del Grappa; già WALLES S.R.L. (costituita nel 1982), nome e sede cambiati con effetto 18 marzo 2025 | registro LEI (lei.bloomberg.com, LEI 815600611E5C66B6AD46) [Certo]; rapporto con l'attuale WALLES SRL [Probabile: l'attività è passata alla nuova società] |
| Titolari | i fratelli Giacometti (sito); Luigino e Roberto Giacometti (Fashion Press) | [DA CONFERMARE i nomi] |
| Marchi | Walles Club, Fratelli Giacometti (F.LLI Giacometti), Marmolada | sito [Certo]; titolarità e registrazioni [DA CONFERMARE] |
| Certificazioni | nessuna dichiarata; solo il rispetto delle norme CITES per i pellami esotici (Walles Club) | sito [Certo] |
| Social | instagram.com/wallescalzature, facebook.com/wallescalzature | sito [Certo] |
| Google Maps | "Calzaturificio Walles (S.R.L.)", categoria Calzaturificio, voto 4,6, coordinate 45.70649, 11.81626 | Google Maps [Certo] |
| Whistleblowing | procedura pubblicata (PDF Rev. 02 del 26/01/2024) | sito [Certo] |

Fonti: https://www.walles.it/ (crawl del 6/10/2026); https://www.aziende.it/walles-srl; https://lei.bloomberg.com/leis/view/815600611E5C66B6AD46; https://www.iubenda.com/privacy-policy/20962260; https://www.google.com/maps?cid=2735344609995685235; https://www.fashion-press.net/brands/793.

## URL vecchi

Per `plugin/redirect-301.csv` (le destinazioni si decidono in 03). Tutti gli URL rispondono 200 salvo dove indicato.

```
/                                        home (anche /index.php)
/index.php
/calzaturificio.html                     Azienda
/collezioni-walles.html                  Collezione
/collezione-walles-club.html             Walles Club (IT)
/collezione-fratelli-giacometti.html     Fratelli Giacometti (IT)
/collezione-marmolada.html               Marmolada (IT)
/collection-walles-club.html             Walles Club (EN)
/collection-fratelli-giacometti.html     Fratelli Giacometti (EN)
/collection-marmolada.html               Marmolada (EN)
/lavorazioni-calzature-walles.html       Lavorazione
/social-wall.html                        Social Wall
/contatti-walles.html                    Contatti
/outlet-walles.html                      Outlet
/news-walles.html                        oggi 301 verso /
/it/struttura/info.html                  Info legali IT (aperta con ?iframe=true&width=800&height=400)
/en/struttura/info.html                  Info legali EN
/Procedura_Whistleblowing.pdf            da mantenere allo stesso indirizzo o reindirizzare
```

Host da reindirizzare a `https://www.walles.it/`: `walles.it` (oggi 200 senza redirect), `fratelligiacometti.com`, `www.fratelligiacometti.com`, `fratelligiacometti.it`, `www.fratelligiacometti.it` (oggi copia identica del sito; meglio un 301 verso la pagina del marchio). Le 185 immagini sotto `/img/` sono elencate in `_prova/crawl/risorse-log.json`: le foto prodotto possono essere indicizzate in Google Immagini, si possono reindirizzare in blocco alle pagine collezione.
