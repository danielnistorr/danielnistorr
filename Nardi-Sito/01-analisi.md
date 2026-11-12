# Nardi: analisi per la nuova home

Sito: https://narditalia.com (crawl e screenshot del 24/10/2026: home, Azienda, Contatti, Prodotti, 4 categorie, 96 schede prodotto, privacy e cookie, libreria media di WordPress con 535 file, 3 PDF campione). Fonti citate come URL + frase; le pagine del sito sono indicate con il percorso dopo `narditalia.com/`. Copia delle pagine in `_prova/crawl/`, schede riassunte in `_prova/crawl/prodotti.json`.

## 1. In breve

- **Chi**: NARDI S.r.l. Unipersonale, Via S. Antonio 24/a, 35020 Tombelle di Saonara (PD). La nota di partenza è giusta su comune e frazione: Tombelle qui è frazione di Saonara, provincia di Padova (piede del sito, schede tecniche, dichiarazione di prestazione). Pagine Gialle e Virgilio la mettono per errore a "Vigonovo (VE)".
- **Da quando**: "La ditta Nardi nasce nel 1985" per iniziativa del "fondatore Sig. Benito Nardi che inizialmente si dedica esclusivamente alla creazione di stucchi artistici decorativi in gesso" (`azienda/`). Poi produce in proprio lo stucco e passa alle polveri.
- **Cosa fa davvero**: produce e confeziona polveri e paste per l'edilizia e il fai da te: stucchi, gessi (alabastrino, scagliola, bologna, murario, polvere ceramica), malte, cementi, calce, colle per piastrelle, rasanti, ossidi di ferro in polvere, più fissativi e qualche prodotto di terzi. ATECO "23.62 - Fabbricazione di prodotti in gesso per l'edilizia" (informazione-aziende.it). Ha una dichiarazione di prestazione CE (UNI EN 13279-1) per l'Artestucco E180.
- **Le linee**: 96 prodotti in quattro categorie: Briko Line 43 (scatole da 1 kg e secchielli da 750 g, per il fai da te), Artelinea 41 (buste argentate da 5 kg, sacchi da 20-25 kg, secchi: la linea professionale), Gli speciali 6, Altri prodotti 6. La home ne mostra 96, non 80.
- **Per chi**: "prodotti specifici dedicati sia al privato che al professionista" (`azienda/`); lo stand in fiera dice "prodotti per l'edilizia professionale e il fai da te". Vende attraverso i negozi: le forniture sono in cartoni ("Conf. da kg 1x12 pz") e "bancali da kg 720", e una foto mostra le scatole sullo scaffale di un punto vendita.
- **Quanti**: piccola. Fatturato 2025 "Tra 300.000 e 600.000 Euro" (informazione-aziende.it, dati iCRIBIS); dipendenti e metri quadri non pubblici.
- **Il punto**: le scatole Briko Line, con il motivo degli attrezzi a colori e un colore per famiglia, sono un oggetto grafico vero e riconoscibile. Dietro c'è una storia rara: un artigiano dello stucco decorativo in gesso diventato produttore di polveri.

## 2. Il sito di oggi

**Pagine**: Home, Azienda, Prodotti, Contatti; quattro categorie WooCommerce (`categoria-prodotto/briko-line`, `artelinea`, `gli-speciali`, `altri-prodotti`); 96 schede `shop/<linea>/<prodotto>/`, 89 con il PDF "SCHEDA TECNICA"; Privacy Policy, Cookie Policy; una copia inglese vuota (`en/home/`). "Note Legali" nel piede porta a una pagina 404 e "Privacy Policy" porta alla Cookie Policy.

**Testi veri essenziali (verbatim)**:
- Meta description: "Nardi Srl è il luogo ideale per trovare tutti i prodotti per il fai da te e per l'edilizia. Siamo a Tombelle di Saonara, in provincia di Padova."
- Azienda:
  - "La ditta Nardi nasce nel 1985 grazie all'iniziativa a allo spirito imprenditoriale del suo fondatore Sig. Benito Nardi che inizialmente si dedica esclusivamente alla creazione di stucchi artistici decorativi in gesso."
  - "Ben presto, per soddisfare le richieste del mercato, inizia a produrre in proprio lo stucco necessario all'applicazione dei manufatti, primo avvicinamento al mondo delle polveri che sarebbe diventato a breve la realtà aziendale."
  - "L'investimento in macchinari per la produzione dei vari formati segna la grande trasformazione dell'azienda che propone oggi una gamma di articoli molto vasta."
  - "dal 2011, grazie alla realizzazione di un impianto fotovoltaico, produce con energia pulita riducendo a zero le emissioni inquinanti."
- Home: colonne "Prodotti: Stucco, malta / Isolante/fissativo, additivo / Cemento, Gesso / Scagliola, segatura, mastice…"; "Orari: Dal lunedì al venerdì mattina: 8:00-12:00 pomeriggio: 14:00-18:00".
- Schede (struttura fissa: DESCRIZIONE, CAMPI DI IMPIEGO, FORNITURA con codici, CARATTERISTICHE TECNICHE):
  - Gesso alabastrino: "Viene impiegato per la produzione di manufatti in gesso, cornici, rosoni, stampi." "Tempo di inizio presa 15-25 min".
  - Gesso scagliola: "Gesso emidrato di elevata purezza e bianchezza", "idoneo per la realizzazione in opera di modanature e fregi in gesso di grosse dimensioni", "Tempo di inizio presa 60 - 90 min".
  - Gesso bologna: "stuccature su dorature, decorazioni plastiche e usi artistici di alto pregio".
  - Polvere ceramica bianca: "per la realizzazione di modelli di particolare durezza e precisione, per colonne, capitelli e statue".
  - Ossidi di ferro (blu, bruno, giallo, nero, rosso, verde, "gr 500x6 pz"): "Coloranti in polvere che si possono mescolare direttamente con malte a base cemento o gesso oppure alle pitture".
  - Artestucco L60: "Formulato con microsfere di vetro 3M®", "non ritira e non crepa".
  - Malta risanante idrorepellente: "particolarmente indicato per il restauro e il rifacimento degli intonaci di edifici".
  - Brikoll per parquettes: "Adesivo organico minerale certificato, eco-compatibile [...] ideale nel Green Building".
- Numeri: 96 prodotti, 715 voci "Cod." nelle forniture, 395 PDF (184 schede tecniche, 210 schede di sicurezza, 1 dichiarazione di prestazione). Nessuna certificazione aziendale e nessun elenco di macchine.
- Etichette delle confezioni (foto `BRIKO-LINE_ossido-ferro-rosso.jpg`): "MADE IN ITALY", "Reg. Impr. PD 02009150281". Frasi sulle scatole: "Lisciare decorare rifinire" (scagliola), "Ricostruire Livellare Tappare" (stucco cementizio).

**Tecnologia**:
- WordPress (generatore "WordPress 7.0.7") con plugin fermi: WooCommerce 7.1.2, All in One SEO 4.2.7.1, WPML 4.5.14, Contact Form 7 con reCAPTCHA. Tema "basicone" di Kreativeweb ("Powered by Kreativeweb", "© 2016"), Bootstrap, slider ResponsiveSlides. Verde del tema #45a488.
- **Sito compromesso**: la sitemap e l'API elencano **2809 articoli di spam** pubblicati da ottobre 2018 a marzo 2021 (prestiti "payday", "mail order brides", contenuti per adulti) e 717 categorie spam. Sono ancora online, per esempio `news/serbia-woman-help/` risponde 200 con il titolo "Serbia Woman Help - Nardi italia". È l'argomento più forte per rifare il sito (reputazione e motori di ricerca).
- Il modulo contatti cita il "D.Lgs 196/2003". L'icona Facebook in testata punta a "#".

**Problemi a 1440** (`_prova/attuale/home-1440.jpg`, pezzi in `p1440/`; anche `azienda-1440.jpg`, `prodotto-1440.jpg`):
- Prima schermata: barra con telefono, email, ricerca e icona Facebook grigia; logo verde piccolo; slider alto 260 px con "NARDI srl UNIPERSONALE" scritto dentro una texture di cemento. Nessun claim, nessun invito.
- Sotto, tre colonne minute (Azienda troncata a "Ben presto, per soddisfare le richieste del mercato…", Prodotti, Orari) e poi il catalogo intero: 96 riquadri con un bottone verde "SCOPRI DI PIÙ" ciascuno. Pagina alta 11.899 px.
- Le schede hanno resti WooCommerce in inglese ("Reviews (0)", "There are no reviews yet.", "You must be logged in to post a review", "Showing all 6 results", "Default sorting") e refusi ("carteggiarura", "Essicazione").
- "Polvere ceramica terracotta" usa la foto della polvere bianca.

**Problemi a 390** (`home-390.jpg`, mosaico `home-390-mosaico.jpg`, pezzi in `p390/`):
- Testata impilata: telefono, email, ricerca vuota e icona Facebook occupano i primi 340 px; il logo arriva a 380 px.
- Lo slider scende a circa 100 px di altezza e la scritta incisa diventa illeggibile.
- 96 prodotti uno sotto l'altro: la pagina è alta **35.592 px**.
- Il badge reCAPTCHA copre l'angolo in basso. Nessuno scorrimento orizzontale.

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | NARDI S.r.l. Unipersonale | piede di ogni pagina: "NARDI S.r.l. Unipersonale" |
| P.IVA e C.F. | 02009150281 | piede: "P.IVA: 02009150281"; intestazione delle schede tecniche: "Reg. Impr. PD, C.F. e P.IVA 02009150281" |
| REA | PD 197644 | intestazione PDF (`wp-content/uploads/2016/10/st-INTONACO-di-finitura-cementizio-liscio-bianco-1.pdf`): "R.E.A. PD n. 197644" |
| Capitale sociale | 50.000,00 euro i.v. | stessa intestazione: "Cap. Soc. € 50.000,00 i.v." |
| Indirizzo | Via S. Antonio, 24/a, 35020 Tombelle di Saonara (PD) | piede: "Via S. Antonio, 24/a 35020 Tombelle di Saonara (PD)"; mappa di `contatti/`: "Via Sant'Antonio, 24, 35020 Saonara PD" |
| Telefono (sito) | 049 8790626 | testata e piede: "Tel: 049 8790626", "Phone: 049 8790626" |
| Fax (sito) | 049 8304579 | piede: "Fax: 049 8304579" |
| Telefono e fax (PDF) | tel 049 8799070, fax 049 8790626 | intestazione schede tecniche: "tel 049 8799070 fax 049 8790626"; scheda di sicurezza Malta bianca (rev. 5, 01/07/2019): "Telefono: 049 8799070; Fax: 049 8790626". Reteimprese.it: "049 879 9070". In conflitto col sito (sez. 9) |
| Email | info@narditalia.com; sicurezza@narditalia.com | piede: "Email: info@narditalia.com"; scheda di sicurezza: "E-mail: sicurezza@narditalia.com" |
| PEC | non trovata | |
| Anno | 1985 | `azienda/`: "La ditta Nardi nasce nel 1985" |
| Fondatore | Benito Nardi | `azienda/`: "suo fondatore Sig. Benito Nardi" |
| Titolare attuale | forse Leonardo Nardi | reteimprese.it/rivestimenti/saonara/azienda/2644067: "Nardi Srl Unipersonale di Nardi Leonardo". Non confermato |
| Attività | 23.62 Fabbricazione di prodotti in gesso per l'edilizia | informazione-aziende.it/Azienda_NARDI-SRL-8359C: "23.62 - Fabbricazione di prodotti in gesso per l'edilizia", età "41 - 50 anni" |
| Fatturato | 2025 tra 300.000 e 600.000 euro | stessa pagina: "Tra 300.000 e 600.000 Euro" |
| Orari | lun-ven 8:00-12:00 e 14:00-18:00 | home: "Dal lunedì al venerdì mattina: 8:00-12:00 pomeriggio: 14:00-18:00" |
| Ambiente | fotovoltaico dal 2011 | `azienda/`: "dal 2011, grazie alla realizzazione di un impianto fotovoltaico" |
| Prestazione CE | Artestucco E180, UNI EN 13279-1, reazione al fuoco A1 | `wp-content/uploads/2016/10/DICHIARAZIONE-DI-PRESTAZIONE-E1803085.pdf`: "Dichiarazione di prestazione n. 1 - E180 - 2017" |
| Dipendenti, mq | non trovati | reportaziende 429, ufficiocamerale e registroaziende 403 |
| Social | nessuno verificato | l'icona Facebook del sito punta a "#"; nessuna pagina trovata con le ricerche |

## 4. Materiale visivo

Scaricate le 139 immagini della libreria media (31 MB) in `assets/originali/`, più 4 copie del logo. Inventario con misure, soggetto, pagine e voti (qualità / forza come apertura, da 1 a 10) in `_prova/inventario-immagini.json`; fogli provino in `_prova/fogli/`. Nessun video.

| Gruppo | Quanti | Misure | Qualità | Apertura | Giudizio |
|---|---|---|---|---|---|
| Scatole Briko Line scontornate (motivo degli attrezzi, un colore per famiglia: verde petrolio scagliola, viola malte, giallo cemento rapido, arancio colle, rosa stucchi) | 25 | 1600x1226, prodotto alto circa 1000 px | 6 | 4 | il materiale migliore: oggetto vero, nitido, riconoscibile. Ma fondo grigio sfumato e riflesso finto da togliere; regge un oggetto a circa 500 px di altezza a 2x |
| Barattoli trasparenti degli ossidi di ferro con il pigmento visibile | 6 | 1600x1226 | 6 | 5 | il colore puro della polvere: il soggetto più forte per una home chiara |
| Secchielli, flaconi, bombolette Briko Line | 12 | 1600x1226 | 5 | 2 | corretti, poco caratteristici |
| Buste argentate, sacchi e secchi Artelinea | 41 | 1600x1226 | 5 | 2 | linea professionale con grafica povera; buste lucide che riflettono tutto |
| Foto di studio di tre buste argentate (`Q48A8102-scaled`, `Q48A8038-1`, `Q48A8140`) | 3 | 2560x1707, 1600x1600 | 6 | 2-3 | vere, ma fondale grigio sporco e riflessi duri |
| Magazzino con bancali di scatole Briko Line (`IMG_4232`) | 1 | 4272x2848 | 6 | 4 | l'unica foto grande vera dell'azienda; luce piatta, scaffali arancio dominanti |
| Scaffale di un negozio con le scatole in fila (`IMG_2282-136498`) | 1 | 1600x900 | 5 | 3 | da telefono, cartellini prezzo; mostra bene la gamma di colori |
| Facciata della sede decorata con il motivo Briko Line (`TESTATA6`) | 1 | 1920x700 | 5 | 4 | dettaglio solo loro (la facciata è la scatola), foto banale |
| Capannone di tre quarti, stand in fiera | 2 | 768 px | 3-4 | 1 | piccole |
| Slider con testo inciso (cemento, betoniera) | 2 | 1920x500 | 2-3 | 0 | da non usare; la betoniera sembra di repertorio |
| Prodotti di terzi (latta GESCOL, sacco solfato di calcio) | 2 | 1600x1226 | 4 | 0 | marchi non Nardi |
| Miniature 300x230 duplicate | 26 | 300x230 | 2 | 0 | doppioni |
| Logo, icone, favicon | 6 | fino a 500x139 | 0-5 | 0 | vedi sez. 8 |

**Verdetto**: il materiale **regge solo in parte** una home di alta gamma, voto medio 4,5 su 10. Le scatole Briko Line sono un vero oggetto da mettere in scena, ma sono rendering scontornati da catalogo, piccoli per un'apertura a tutta altezza. Non esiste una foto della polvere, delle mani al lavoro, dei manufatti in gesso né della produzione. Per la proposta: una scatola Briko Line ripulita (fondo tolto, riflesso tolto) come oggetto protagonista, più segnaposto esterni (sez. 6). Per il sito vero serve mezza giornata di still life: una scatola frontale in luce naturale; la polvere versata davanti alla sua scatola; i sei ossidi in sei mucchietti; un rosone colato con l'alabastrino; le mani con spatola e stucco; il magazzino e la facciata con un cielo migliore.

## 5. Due direzioni artistiche

Le ispirazioni Graziella e N19 qui non servono: Nardi fa polveri per l'edilizia e il fai da te, non moda né lusso. Ne tengo solo la pulizia generale, nessuna scelta specifica.

**Direzione A, "Una scatola sola" (chiara, un oggetto vero protagonista)**
- Idea visiva: prima schermata color gesso con una sola scatola Briko Line grande e nitida, di tre quarti, e un titolo grande e sicuro accanto; il racconto (dal 1985, dallo stucco decorativo alle polveri) in poche righe. Sotto, le famiglie di prodotto in una riga pulita e la chiusura con la foto del muro finito.
- Immagini: scatole e secchielli Briko Line ripuliti dal fondo, con ombra morbida vera; una sola foto d'ambiente in chiusura (segnaposto Pkseva, luce su parete intonacata, poi la loro facciata rifotografata).
- Tipografia: Bricolage Grotesque (Google Fonts, OFL; il nome richiama il bricolage) a 600 per titoli da 96-120 px; Instrument Sans (Google Fonts, OFL) per testi e cifre. Nessuna delle due è usata nelle home finite della campagna.
- Colore: fondo gesso #F4F1EA, inchiostro #1B1A17, verde Nardi scurito #276E59 per i link (5,4:1 sul fondo; il #45a488 del sito si ferma a 2,7:1); i colori pieni arrivano solo dalle scatole.
- Gesto: una riga di sei famiglie (Stucchi, Gessi, Malte, Cementi, Colle, Ossidi); un tocco cambia di colpo la scatola protagonista e la sua frase vera ("Lisciare decorare rifinire"), senza transizioni.

**Direzione B, "Dal gesso al pezzo" (chiara, materica ed editoriale)**
- Idea visiva: la storia del fondatore come filo: dalla polvere bianca ai manufatti in gesso. Apertura bianca con un solo mucchio di polvere in luce radente e il titolo in alto; poi i gessi per quello che diventano, con le parole delle schede ("cornici, rosoni, stampi"; "colonne, capitelli e statue"; "stuccature su dorature").
- Immagini: macro della polvere e dei pigmenti su fondi pieni (segnaposto Kovalets, ArtHouse, Cris CL), le cornici in luce radente (Weinkauf), le mani con la spatola (Bughdaryan); poi le loro foto nuove.
- Tipografia: Newsreader (Google Fonts, OFL) diritta, mai corsiva, per titoli grandi; Instrument Sans piccolo per dati tecnici, codici e tempi.
- Colore: bianco gesso #FAF8F4, grigio cemento #6B6964 per i testi secondari, testo #22201C, un solo accento rosso ossido #9E3F28 (dal loro ossido di ferro rosso), verificato AA.
- Gesto: una scala dei tempi di presa da 0 a 90 minuti; toccando un gesso (alabastrino 15-25, polvere ceramica 20-25, stucco interno 60, scagliola 60-90) si accende la sua fascia e compare il suo uso verbatim. Dati veri, utili al cliente.

## 6. Immagini sostitutive

Nove foto in `assets/esterne/`, lato lungo 2400 px o meno; licenza letta sulla pagina di ogni foto (sette Unsplash "Free to use under the Unsplash License", due Pexels "Free"); autori e URL in `assets/CREDITI.md`. Nessuna è già usata nelle altre home della campagna; nessuna è generata dall'IA.
- Per A: luce su parete intonacata (Pkseva, chiusura), ombre di foglie su parete rasata (Czerwinski, fondo luminoso), mucchietto di pigmento blu su giallo (ArtHouse, Pexels).
- Per B: mucchio di polvere bianca (Kovalets), cornici bianche a soffitto (Weinkauf), parete con segni di spatola (Hydra 4x), barattoli di pigmenti (Cris CL; etichette da controllare), pigmento blu nel sacco (Cusido, Pexels).
- Comune: mani con spatole e stucco (Bughdaryan).
- L'oggetto protagonista della direzione A resta una scatola vera di Nardi, non un segnaposto.

## 7. Riferimenti di alta gamma nel mestiere

Prime schermate a 1440 e 390 in `riferimenti/<nome>-1440-prima-schermata.jpg` e `-390-`, JPEG qualità 78, prese il 24/10/2026 (proxy con uscita dagli Stati Uniti: alcuni siti mostrano avvisi di paese). Font letti dal codice.

1. **Farrow & Ball** (farrow-ball.com, pitture). Di alta gamma: un'immagine d'ambiente calda a tutta larghezza, un titolo umanista corto ("The Colors of Autumn", Verlag), un solo bottone; il prodotto è il colore, non la latta. Da non riprendere: barra promozionale azzurra, chat flottante, a 390 il video va in errore.
2. **Bauwerk Colour** (bauwerkcolour.com, pitture a calce). Di alta gamma: dittico foto più campo pieno del colore protagonista, una frase in chiaro, il nome del colore ("Paprika", "Nougat") in un angolo: il colore come materia. Da non riprendere: due barre di avvisi sopra la testata, la linguetta "Feedback", Roboto.
3. **Kerakoll** (kerakoll.com, stucchi, colle e malte: lo stesso mestiere di Nardi, Sassuolo). Di alta gamma: il marchio enorme in basso a sinistra, titolo serif a destra, menu di quattro voci, Graphik e Larish. Da non riprendere: l'immagine del carosello non era caricata (resta grigia), carosello a quattro tacche, il selettore di paese all'ingresso.
4. **Stevensons of Norwich** (stevensons-of-norwich.co.uk, modanature in gesso dal 1982). Il mestiere d'origine di Benito Nardi: prima schermata con un lavoro vero (un teatro), riga "Artisans in decorative plaster", Sorts Mill Goudy. Da non riprendere: l'emblema "40 years" sopra la foto, il testo giustificato in maiuscolo spaziato, il logo che a 390 non carica.
5. **Mylands** (mylands.com, pitture, Londra). Di alta gamma: titolo serif sottile spaziato ("HUGUENOT", FreightText ed Engravers Gothic), numero del colore come etichetta, foto di un interno vero, molto bianco intorno. Da non riprendere: il riquadro bianco sopra la foto, il popup di paese, le tre barre di servizio.

Aperti e scartati: Little Greene (verifica Cloudflare), Matteo Brioni e Coat (non raggiungibili dal proxy), Backdrop (immagini rotte), ClayTec (cookie e slider da catalogo), Oikos e Novacolor (banner cookie e pagina vuota), Graphenstone (impianto generico, Montserrat). Nessuno dei siti trovati mette in scena una confezione come oggetto: la direzione A lo fa per prima.

## 8. Per il piede

- **Logo**: esiste solo raster. Il migliore è `assets/originali/logo-nardi-bianco-500x139.png` (corsivo "nardi" bianco su trasparente, regge 250x70 a 2x); poi `logo-nardi-verde-250x70.jpg` (verde su bianco), `logo-nardi-grigio-pdf-540x117.jpg` e `logo-nardi-intestazione-pdf-869x152.jpg` (dalle schede tecniche, con ragione sociale, REA e capitale). Favicon 16x16. Nessun SVG nel codice, nessun PDF vettoriale nei campioni aperti. Il corsivo è a mano libera: ricostruirlo in SVG non sarebbe fedele senza il file originale (chiederlo, sez. 9). Nella proposta va il PNG bianco su fondo scuro, oppure il verde a 2x.
- **Voci e pagine di oggi**: Home, Azienda, Prodotti, Contatti; nel piede "I nostri prodotti: Briko Line, Artelinea, Gli Speciali, Altri prodotti"; "Note Legali" (404), "Privacy Policy" (porta alla cookie), "Cookie Policy".
- **Pagine del sito nuovo** da collegare dal piede: Azienda (storia e fotovoltaico), Prodotti con le quattro linee, Schede tecniche e di sicurezza (i 395 PDF esistono già), Dove siamo e Contatti, Privacy, Cookie.
- **Colonne proposte**: Azienda (La storia dal 1985, Energia dal sole, Dove siamo); Prodotti (Briko Line, Artelinea, Gli speciali, Altri prodotti, Schede tecniche); Contatti (telefono, email, indirizzo con mappa, orari lun-ven 8-12 e 14-18). **Seguici: nessuna colonna**, perché non ho trovato social veri e l'icona Facebook del sito punta a "#".
- **Newsletter: no.** Nessuna notizia, catalogo sfogliabile, fiera datata o collezione da annunciare; i clienti comprano nei negozi e il rivenditore ordina per telefono. Nella NOTA: un invito "Chiedi dove trovarli" o "Diventa rivenditore" sarebbe più utile di una newsletter.
- **Riga legale**: NARDI S.r.l. Unipersonale, P.IVA e C.F. 02009150281, REA PD 197644, Cap. Soc. 50.000,00 euro i.v., Privacy, Cookie. PEC non trovata.

## 9. Da confermare

- **Telefono e fax**: il sito dà tel 049 8790626 e fax 049 8304579; schede tecniche (2016), scheda di sicurezza (2019) e Reteimprese danno tel 049 8799070 e il 049 8790626 come fax. Quale numero va in grande?
- **Pulizia del sito**: i 2809 articoli spam e le 717 categorie spam sono ancora pubblici. Va detto con tatto nella proposta e serve la bonifica prima di qualsiasi migrazione (e i 301 delle schede).
- Titolare attuale (Leonardo Nardi secondo Reteimprese?) e se Benito Nardi è ancora in azienda.
- Anno di costituzione della srl rispetto al 1985 della ditta; PEC; dipendenti; metri quadri; macchinari ("investimento in macchinari per la produzione dei vari formati").
- La frase "riducendo a zero le emissioni inquinanti": è una dichiarazione ambientale forte, da usare solo se l'azienda la conferma (potenza dell'impianto, quota coperta).
- Se Nardi produce davvero tutti i 96 articoli o ne confeziona e rivende una parte (latta GESCOL e solfato di calcio di terzi; schiuma poliuretanica, rete, secchielli).
- Dove si comprano: elenco o zone dei rivenditori, catene servite, vendita diretta in sede ai privati?
- Fiera dello stand e anno; se partecipano ancora a fiere.
- Social: esiste una pagina Facebook vera?
- Logo vettoriale e file di stampa delle scatole (servono per scontornare bene o rifare i rendering in grande).
- Diritti di `slide-nardi-2.jpg` (betoniera, forse repertorio) e chi ha fatto i rendering delle confezioni e le foto "Q48A".
- Se le schede tecniche (aggiornate al 2016-2019) sono ancora valide e quali prodotti sono fuori produzione.
- La copia inglese del sito (`en/home/`): serve una versione in inglese?
