# Belletti: analisi per la nuova home

Sito: https://www.bellettiascensori.it (crawl e screenshot del 24/10/2026: home, 19 pagine di menu, le 7 categorie prodotto con 17 sottocategorie aperte con i postback ASP.NET, 12 PDF). Fonti citate come URL + frase; le pagine del sito sono indicate con il percorso dopo `bellettiascensori.it/`. Testi grezzi in `_prova/crawl/pages/`, PDF in `assets/originali/pdf/`.

## 1. In breve

- **Chi**: Belletti S.r.l., Via della Tecnica 29, Mestrino (PD). Progetta, costruisce, installa e mantiene ascensori, montacarichi, montaoggetti, montauto, piattaforme elevatrici, scale mobili e le strutture metalliche o in vetro che li reggono. Fa anche servoscala (`assistenza.aspx`).
- **Da quando**: il mestiere dal 1908 ("Dal 1908 Belletti si occupa di ascensori.", depliant del 2008 e pagine pubblicitarie TOP del 2010). La srl attuale è del 22-23/11/1984 (LEI). Il fondatore Rodolfo Belletti installava ascensori "in tutta Europa, avventurandosi fino in Romania e in Russia nel primo dopoguerra"; poi il figlio Paolo e la nuora Elvira; nomi storici "Botti e Belletti", "Officine Meccaniche Belletti", "PBP Elevatori" (`chi-siamo.aspx`).
- **Oggi**: guidano "i fratelli Gaetano e Irma Belletti e l'Amm.re Delegato Ing. Andrea Viel". "Trenta addetti alle dirette dipendenze" (sito); i registri danno 31-33 dipendenti e un fatturato di circa 4,1-4,6 milioni (sez. 3).
- **Dove e per chi**: assistenza diretta "nelle province del Veneto e in parte del Friuli, con oltre venti tecnici", resto d'Italia tramite il Safety Lift Group. Clienti: condomini e amministratori, progettisti e architetti, enti pubblici (Galleria Cavour del Comune di Padova, ponte di Legnago), negozi e centri commerciali, case private (piattaforme, montauto).
- **Correzioni alla nota di partenza**: "terza generazione" è giusto (Rodolfo, Paolo ed Elvira, Gaetano e Irma), ma il sito dice "oltre tre generazioni" e "Un secolo di storia". Le foto vere di panoramici ci sono, però online sono quasi tutte di 500 px: le migliori stanno nel depliant del 2008 (fino a 948x1263). L'anno 2012 del sito non è scritto da nessuna parte: jQuery 1.4.4 è del 2010, l'informativa è aggiornata al 2015.
- **Il punto**: Belletti non è un rivenditore di cabine a catalogo. Disegna l'ascensore attorno all'edificio, spesso storico ("L'ascensore rispecchia il carattere dell'edificio in una sintesi armonica di sicurezza, di comfort e di stile."), e poi lo tiene in vita con un servizio 24 ore dal 1997. Il vetro dentro i palazzi antichi del Veneto è il loro soggetto più bello.

## 2. Il sito di oggi

**Pagine**: Home (`default.aspx`), Chi siamo (Un Secolo e Tre Generazioni, Mission, Vision), Prodotti (Ascensori, Montacarichi, Monta oggetti, Monta automobili, Piattaforme elevatrici, Scale mobili, Strutture metalliche), Assistenza, News (vuota), Download (Pubblicità, Redazionali, Certificazioni, DURC), Video gallery (3 video), Contatti (modulo e informativa lunga), Privacy.pdf.

**Testi veri essenziali (verbatim)**:
- Home: "Un secolo di storia, tre generazioni di passione, la proiezione verso il futuro di una realtà fatta di persone. Profonda conoscenza, garanzia di qualità, lo sguardo teso all'orizzonte. Belletti al servizio del cliente!"; "Focus On: Pensiamo che per presentarci bastino i lavori che abbiamo eseguito." (sotto non c'è nessun lavoro).
- Chi siamo: "Un lavoro, una passione e un orgoglio che durano da oltre tre generazioni"; "i mezzi tecnologici più moderni ed una rete di collaboratori esterni di comprovata fiducia"; "Belletti… trenta cuori e una sola anima!"
- Vision: "Affidabilità", "Qualità", "Sicurezza" con una frase ciascuna.
- Prodotti:
  - Ascensori: "MRL gearless oppure oleodinamico, trazione diretta o in taglia"; "capienza da 1 a 100 persone e velocità fino a 3,00 [m/s]"; sottocategorie Accessori, Cabine, Illuminazione, Panoramici, Pavimenti, Porte, Speciali.
  - Montacarichi: "movimentazione di carichi fino a 24.000 kg".
  - Montaoggetti: "soluzioni a partire da 12 kg", "anche ad uso alimentare".
  - Monta automobili: "ideali nei centri storici o dove non esiste possibilità di rampe"; Montautomobili tradizionali, Sollevatori a pantografo.
  - Piattaforme elevatrici: "per piccoli edifici residenziali o per portatori di handicap".
  - Scale e tappeti mobili: "per realtà commerciali e di grande traffico".
  - Strutture metalliche: "antisismiche calcolate per installazione all'interno o all'esterno"; Strutture cieche, in vetro esterno, in vetro interno, Speciali.
- Assistenza: "Dal 1997 è attivo il servizio di emergenza 24 ore ... 365 giorni all'anno"; call center "in accordo con le norme EN 81-28"; manutenzione preventiva, verifica semestrale, assistenza alla verifica biennale, manutenzione correttiva "su ogni tipologia di impianto di qualsiasi marca", servoscala.
- Depliant 2008 (28 pagine): "portate comprese tra 24 e 12.000 kg"; "Migliaia di realizzazioni"; "Dal 1997 Belletti opera in regime di Qualità Certificata"; furgoni con localizzatore satellitare; dipendenti con il titolo di "Maestro del Lavoro"; polizza "con massimale per sinistro pari a € 10.000.000,00"; "chiavi in mano".
- Lavori documentati, con dati tecnici (redazionali della rivista DiBaio in `download/redazionali`):
  - Galleria Cavour, Piazza Cavour, Padova (inaugurata "ad ottobre 2007"): "Ascensore oleodinamico in taglia laterale, Portata: Kg. 480, Capienza: n. 6 persone, Corsa: m 3,82, Fermate: n. 2, Velocità: 0,40 m/sec", vano "in acciaio inox".
  - Palazzo storico a Ca' Michiel, Venezia: cabina con "parete in vetro semicircolare verso corte, pavimento e parete laterale in mosaico Bisazza", "450 Kg", "6 persone".
  - Ex Scuderie di Villa Grimani Morosini "Cà della Nave", Martellago: ascensore "tondo" oleodinamico, "kg. 480", "5 persone", "Fermate: n. 4".
  - XXI Investimenti, Treviso: cabina con "pavimento in pietra (trachite)", acciaio inox "tela di lino" verde.
  - Video: "Ponte Principe Umberto, Legnago (VR)", ascensori panoramici sui due lati del ponte; "L'ascensore parte sui trampoli, Cannaregio (VE)".
- Certificazioni (PDF): DNV GL ISO 9001:2015, prima emissione "04 novembre 1997", copia online valida "24 ottobre 2018 - 24 ottobre 2021"; Eurofins, Allegato XI della direttiva 2014/33/UE, "ASCENSORI ELETTRICI E IDRAULICI", prima emissione 02-08-1999, copia online valida fino al 22-12-2024. Entrambe le copie online sono scadute.

**Tecnologia**: ASP.NET WebForms (`x-powered-by: ASP.NET`), modelli Dreamweaver (`#BeginLibraryItem`), jQuery 1.4.4 e jQuery Tools 1.2.5, impaginazione a tabelle larga 960 px, banner cookie "cookiecuttr", Matomo su webanalyticsportal.it. Autore "Immagica & Partner". Le gallerie prodotto si aprono con `__doPostBack`, quindi i motori non le vedono. I video sono embed Flash `youtube.com/v/...`, che non partono più. `site.webmanifest` dà 404. Nessun meta viewport.

**Problemi a 1440** (`_prova/attuale/home-1440.jpg`, `chi-siamo-`, `assistenza-`, `categoria-ascensori-`, `contatti-1440.jpg`):
- Colonna di 960 px in mezzo a un fondo grigio scuro. Il menu verde va su due righe ("CONTATTI" da solo sotto).
- Lo slider è largo 960x350, con quattro palloncini pastello numerati 1-4 come comandi.
- Le otto categorie sono tessere da 112x180 con il titolo su una fascia nera trasparente.
- "Focus On" promette i lavori, ma sotto non c'è niente; anche News è vuota.
- Il banner dei cookie copre l'indirizzo nel piede. Il piede dà spazio allo sponsor Pallavolo Padova; l'icona Twitter porta a "#". C'è ancora il fax.
- Le categorie mostrano miniature da 130 px. Refuso "Srutture metalliche". Il testo è grigio chiaro da 12-13 px.

**Problemi a 390** (`home-390.jpg`, `categoria-ascensori-390.jpg`): senza viewport la pagina si disegna larga 980 px e viene rimpicciolita. Testi minuscoli, menu e numeri di telefono non toccabili, metà schermata vuota, banner dei cookie in fondo.

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | BELLETTI S.R.L. | companyreports.it/belletti_srl-01263940288: "Ragione Sociale: BELLETTI S.R.L."; piede del sito "Belletti S.r.l." |
| P.IVA e CF | 01263940288 | piede: "C.F. - P.IVA e Reg. Imp. IT01263940288" |
| REA | PD 190779 | companyreports.it: "il numero REA PD 190779" |
| Capitale sociale | 167.000 € (da confermare se versato) | atoka.io/public/it/azienda/belletti-srl/477b2fb9801a: "Capitale sociale 167.0 K €" |
| Costituzione srl | 22/11/1984 (23:00 UTC, cioè il 23/11 ora italiana) | lei.bloomberg.com/leis/view/815600C64C2BE8829B73: "Entity Creation Date 1984-11-22 23:00:00"; atoka: "ANZIANITÀ 41 anni" |
| Inizio del mestiere | 1908 | `pdf/pubblicita/belletti_depliant.pdf` e `top_1.pdf`: "Dal 1908 Belletti si occupa di ascensori." |
| Indirizzo | Via della Tecnica, 29, 35035 Mestrino (PD) | piede del sito |
| Telefono | 049 5082430 | piede: "Tel. +39 049 5082430" |
| Assistenza tecnica | 049 9005131 | piede: "Assistenza Tecnica Tel. +39 049 9005131" |
| Fax | 049 9003778 | piede: "Fax +39 049 9003778" |
| Email | info@bellettiascensori.it | piede |
| PEC | non trovata | |
| ATECO | 28.22.01 Fabbricazione di ascensori, scale mobili e tappeti mobili | companyreports.it |
| Fatturato | 2025: 4.125.670 €, utile 373.758 €, costo del personale 1.539.356 €. Atoka: "RICAVI 4.6 M €" (2025) | companyreports.it; atoka.io. registroaziende.it (403 al nostro client, letto da un estratto di ricerca): 2022 3.193.192 €, 2023 4.283.274 € |
| Dipendenti | sito "Trenta addetti"; atoka "DIPENDENTI 33"; companyreports "da 20 a 49" | `chi-siamo.aspx`; atoka; companyreports |
| Persone | Gaetano e Irma Belletti, AD Ing. Andrea Viel | `chi-siamo.aspx` |
| Qualità | ISO 9001 dal 04/11/1997 (DNV GL, cert. CERT-02313-97-AQ-IND-SINCERT); Eurofins Allegato XI 2014/33/UE dal 02/08/1999 (EPT 0477.ASC.21/4706) | `pdf/certificazioni/` |
| Rete | Safety Lift Group | `chi-siamo.aspx`: "un gruppo di aziende selezionate appartenenti al Safety Lift Group" |
| Riconoscimenti | "Maestro del Lavoro" ad alcuni dipendenti; locandina "58a premiazione del lavoro e del progresso economico" della Camera di Commercio di Padova | depliant; `download/immagini/fn000055.jpg` |
| Sponsor | Pallavolo Padova | piede: "Official Sponsor" |

## 4. Materiale visivo

Ho scaricato 406 file (23 MB) in `assets/originali/`: 169 foto delle gallerie prodotto più 139 miniature, 35 foto estratte dal depliant, 56 file di grafica e testate, 12 PDF. Inventario con misure, URL, categoria del sito, soggetto e voti (qualità / forza come apertura) in `_prova/inventario-immagini.json`; fogli provino in `_prova/fogli/` (`gallerie-1..5`, `depliant-1`, `depliant-immagini-1`, `sito-foto-1`, `esterne-1`). I tre video stanno su YouTube e non li ho scaricati.

| Gruppo | Quanti | Misure | Qualità | Apertura | Giudizio |
|---|---|---|---|---|---|
| Depliant: Galleria Cavour di notte (`d-037`, `d-000`), facciata in vetro della sede (`d-051`), castelletto nero in un interno bianco (`d-009`) | 4 | 830-948 x 1145-1263 | 6-7 | 5 | Sono foto professionali e vere, con soggetti forti. Ma sono compresse in JPEG 2000 e restano morbide sopra i 700 px: vanno bene a mezza pagina, non a tutta larghezza |
| Depliant: torri e cabine in vetro, cabine tonde traforate, Ca' Michiel, montauto con Thunderbird rossa, furgone davanti alla sede, anziano e bambina sulla scala | 18 | 400-870 px | 5-6 | 2-4 | buone per le sezioni, piccole |
| Depliant: strisce verticali, ufficio, furgoni, sede dall'alto, tecnico al quadro | 13 | 146-633 px | 4-5 | 1-2 | di servizio |
| Gallerie prodotto: panoramici in vetro, scale elicoidali con cabina tonda viste dall'alto (`fn000008`, `fn000237`, `fn000239`), Ca' Michiel col mosaico blu (`fn000100`), torri accanto a palazzi storici | 25 circa | 360-500 px | 5 | 3-4 | I soggetti più belli che hanno, ma a 500 px non reggono più di una miniatura |
| Gallerie prodotto: cabine, porte, pulsantiere, montacarichi, vani in costruzione, foto da cantiere col flash | 130 circa | 250-500 px | 3-4 | 1-2 | documentazione, non fotografia |
| Gallerie: locandine, premiazioni, render "VS associati", Confindustria, kart, rugby | 16 | 425-1417 px | 2-3 | 0 | da non usare (alcune non sono loro) |
| Slider della home | 4 | 960x350 | 4 | 1-2 | tagli stretti delle stesse foto |
| Ritratti seppia della famiglia e foto di gruppo (`storia1-4`) | 4 | 227x227 | 3 | 1 | Valgono molto per la storia, ma vanno chieste in originale |
| Logo | 4 | SVG vettoriale + PNG | buona | | vedi sez. 8 |

**Verdetto**: il materiale **non regge** da solo una home di alta gamma, ma è il migliore trovato finora in questa zona per i soggetti. In media vale 4 su 10; le quattro foto del depliant arrivano a 6-7. Il problema è la risoluzione, non lo sguardo: qualcuno nel 2008 ha fotografato bene la Galleria Cavour e la sede. Per la proposta: segnaposto esterni per l'apertura (sez. 6) e le foto del depliant a mezza misura per i lavori veri. Per il sito vero bisogna chiedere gli originali del fotografo del depliant (Galleria Cavour, sede, Ca' Michiel). Poi servono due giorni di fotografia: un panoramico in un palazzo storico di giorno, a luce naturale; una cabina finita in officina; un tecnico al lavoro; la sede.

## 5. Il soggetto visivo e due direzioni

**Cosa è bello da vedere**: il vano di vetro e acciaio inox dentro un palazzo antico, cioè il nuovo che "non invade né trasforma" (video Cannaregio). Poi la cabina tonda nel pozzo di una scala elicoidale vista dall'alto, che è un cerchio perfetto; la Galleria Cavour accesa di sera; i materiali della cabina (mosaico Bisazza, trachite, inox "tela di lino", vetro curvo). Infine la targa di cabina "BELLETTI n. 2796, 630 kg 8 persone" e le pulsantiere col marchio. **Il dettaglio solo loro**: la scheda tecnica dei lavori veri (portata, persone, corsa, fermate, velocità) e il logo, in cui le due L verdi sono un vano con la cabina a gradini.

**Direzione A, "Il carattere dell'edificio" (chiara, un solo oggetto)**
- Idea visiva: fondo bianco calce, un solo castelletto in vetro grande e nitido che sale fuori dalla prima schermata; titolo grande e corto preso dai loro testi, per esempio "Ascensori dal 1908", con sotto la loro frase "L'ascensore rispecchia il carattere dell'edificio". Tre legende sottili sul vetro (Struttura in acciaio inox, Vetro, Cabina 480 kg 6 persone), come nella home di Mario Agnoletto.
- Immagini: segnaposto d'apertura Gökalp (vano in vetro nell'atrio di calcestruzzo chiaro); poi i lavori veri dal depliant a mezza pagina (Galleria Cavour, Ca' Michiel, la sede); Borie (facciata bianca col vano in vetro) per le strutture.
- Tipografia: Geist per i titoli e il testo, Geist Mono piccolo per i dati tecnici ("480 kg", "0,40 m/s", "EN 81-28"). Sono di Google Fonts con licenza OFL; niente Inter.
- Colore: calce #F6F5F2, inchiostro #1B1D1F, grigio del logo #646567, verde del logo #009A54 solo per marchio e grafica grande (su bianco fa 3,7:1); per testi e link un verde più scuro #007A43 (5,4:1, AA).
- Gesto: un selettore "Galleria Cavour / Ca' Michiel / Cà della Nave / Legnago" cambia la foto e la riga della scheda tecnica, con dati verbatim dai redazionali. Il cambio è netto, senza transizioni.

**Direzione B, "Un secolo e tre generazioni" (sera, poi chiara)**
- Idea visiva: si apre sulla Galleria Cavour di notte, a tutta larghezza: il padiglione in vetro acceso, i passanti mossi, il palazzo caldo. È l'unico caso in cui il nero lo chiede davvero l'immagine. Sopra, un titolo bianco sottile, "Un secolo e tre generazioni", e un solo numero, "1908". Dalla seconda sezione la pagina torna chiara, come la home "Scintilla e spessore" di Tek.Lam.
- Immagini: per l'apertura serve la foto del depliant in originale (`d-037`), che oggi è troppo morbida; segnaposto Ota (cilindro in vetro nella scala elicoidale). Per la storia Charkoftaki ed Erdoğan (vecchie cabine in ferro), finché non arrivano i ritratti di famiglia in originale; Jeromin per la chiusura.
- Tipografia: Newsreader (Google, OFL) per i titoli, in tondo e mai in corsivo d'accento, più Instrument Sans (Google, OFL) per il testo e i numeri.
- Colore: notte #101214 solo in apertura, carta #F3F1EC, inchiostro #1C1C1C, verde #007A43 per l'unico invito; il verde chiaro del logo solo nel marchio.
- Gesto: una riga dei nomi, "Botti e Belletti / Officine Meccaniche Belletti / PBP Elevatori / Belletti". Al tocco su un nome compaiono il ritratto e la frase di Chi siamo; gli anni dei passaggi restano fuori finché non li confermano. Sotto, un solo invito, il numero dell'assistenza 24 ore con tel:.

**Ispirazioni Graziella e N19**: non le uso. Belletti è un costruttore e manutentore di impianti per condomini, progettisti ed enti, non un marchio di moda. Il registro giusto è quello dell'architettura e dell'ingegneria del vetro (sez. 7). Ne tengo solo l'idea di molta aria e poche parole.

## 6. Immagini sostitutive

Nove foto in `assets/esterne/`, al massimo 2400 px di lato. Su ogni pagina ho verificato la licenza: le Pexels sono "Free", le Unsplash "Free to use under the Unsplash License" e nessuna è Unsplash+. Nessuna compare nelle altre home della campagna (controllato per identificativo in tutti i CREDITI.md, elenco in `_prova/usate-campagna.txt`). Dettagli in `assets/CREDITI.md`, foglio in `_prova/fogli/esterne-1.jpg`.
- A, apertura: Gökalp, vano in vetro in un atrio chiaro (`pexels-35288711`). Altre per A: Borie facciata col vano in vetro, Didsss cilindro in vetro esterno (in basso c'è l'insegna di un negozio, da tagliare), yx b porte di piano in luce radente.
- B, apertura: Ota, cilindro in vetro dentro una scala elicoidale, in bianco e nero (`unsplash-8cF7x8gBVPI`). Altre per B: Charkoftaki cabina in ferro battuto, Erdoğan ascensore d'epoca nell'androne, Bruno BD cabina in vetro al buio.
- Comune, per la chiusura: Jeromin, vano panoramico contro il cielo al tramonto.
- Il repertorio non ha un ascensore in vetro dentro un palazzo veneto: quella foto la possono dare solo i loro lavori (Galleria Cavour, Ca' Michiel, Cannaregio). Nessuna foto mostra marchi di costruttori concorrenti.

## 7. Riferimenti di alta gamma nel mestiere

Prime schermate a 1440 e 390 in `riferimenti/<nome>-1440.jpg` e `-390.jpg` (qualità 78), con i caratteri letti dal codice in `<nome>-*.json`.

1. **Schindler Italia** (schindler.com/it, ascensori, pagina d'apertura sulla modernizzazione).
   - Alta gamma: un solo oggetto, la porta di piano in acciaio dentro una boiserie scura, simmetrica, con un titolo leggero in Frutiger Light. È esattamente il tema "ascensore nel palazzo".
   - Da non riprendere: il bottone rosso pieno, il menu ad hamburger anche su desktop, la foto di repertorio troppo scura.
2. **seele** (seele.com, facciate e strutture in vetro per l'architettura).
   - Alta gamma: bianco pieno, una superficie scultorea che riempie lo schermo, il logo minuscolo e un titolo in Univers. A 390 si legge il titolo nero grande su bianco. È il registro del vetro fatto bene.
   - Da non riprendere: l'hashtag come titolo, l'hamburger su desktop.
3. **Eckersley O'Callaghan** (eckersleyocallaghan.com, ingegneri del vetro strutturale).
   - Alta gamma: foto d'opera a tutta larghezza e un carattere proprio (New Rail Alphabet); il testo sotto è calmo e corto.
   - Da non riprendere: il carosello con le frecce, la notizia come apertura, il logo bianco poco leggibile sulla foto.
4. **Aritco** (aritco.com, ascensori per case e spazi pubblici, design svedese).
   - Alta gamma: un carattere disegnato apposta (Letterlift, maiuscolo spaziato), un colore caldo unico (sabbia e ottone), il prodotto trattato come arredo. Il video d'apertura nel nostro browser resta grigio: ho visto solo il titolo.
   - Da non riprendere: la chat che si apre da sola e copre metà schermo, il video che non carica, le quattro fasce marroni in basso.
5. **KONE Italia** (kone.it, ascensori).
   - Alta gamma: foto vera di persone che escono da una cabina, un titolo grande e corto ("Più di un semplice collegamento tra piani"), un solo bottone.
   - Da non riprendere: Inter ovunque, il bottone pillola blu con la freccia, la doppia barra di menu fitta.

Scartati: Maspero Elevatori (nero, maiuscolo, striscia di foto di altezze diverse), Stiltz e Vimec (impianto da tema, banner arancio, carosello), con miniature in `riferimenti/scartati/`; Kalea (bloccato da Cloudflare), Faraone e Cibes (pagina di verifica antirobot), IGV (il dominio igv.it porta a un'altra azienda).

## 8. Per il piede

- **Logo**: c'è il vettoriale vero. L'ho estratto dai tracciati della pagina 28 del depliant del 2008 (`assets/originali/logo-belletti-depliant.svg`, 26 tracciati, colori #646567 e #009A54, con la scritta "ASCENSORI"); confrontato col PDF reso a 600 dpi coincide (lo script è `_prova/script/logo_svg.py`). Rispetto al logo del sito manca solo la "®". Ci sono anche il PNG 512x512 della favicon (`logo-belletti-favicon-512.png`) e il PNG del sito da 200x69 (`logo-belletti-web-200x69.png`). Nel piede il grigio #646567 su bianco regge (5,8:1).
- **Menu e pagine di oggi**: Home page, Chi siamo (Mission, Vision), Prodotti (7 categorie), Assistenza, News, Download (Pubblicità, Redazionali, Certificazioni, DURC), Video gallery, Contatti, Privacy e Cookie Policy (PDF). Pagine sensate per il sito nuovo:
  - Azienda: Storia dal 1908, Lavori (Galleria Cavour, Ca' Michiel, Cà della Nave, Legnago, Cannaregio), Certificazioni.
  - Impianti: Ascensori, Panoramici e strutture in vetro, Montacarichi e montaoggetti, Montauto, Piattaforme elevatrici, Scale mobili.
  - Assistenza: Manutenzione, Emergenza 24 ore, Ammodernamento.
  - Contatti; Privacy; Cookie.
- **Social che esistono**:
  - YouTube https://www.youtube.com/@BellettiAscensori, verificato: tre video, "Cannaregio - L'ascensore parte sui trampoli", "Legnago - Ponte sull'Adige", "Piazza Cavour - Inaugurazione".
  - Facebook https://www.facebook.com/bellettiascensori, linkato dal sito; dal nostro client risponde errore 400, quindi è da verificare.
  - Twitter: l'icona porta a "#". LinkedIn e Instagram non trovati.
- **Newsletter**: **non ha senso**. Non c'è newsletter; la pagina News è vuota da anni e "Focus On" non ha mai avuto contenuti. Non ci sono fiere né cataloghi nuovi (il depliant è del 2008). I clienti sono condomini, progettisti ed enti che cercano un numero di telefono, non aggiornamenti. Al loro posto un link a Lavori e il numero dell'assistenza 24 ore ben visibile.
- **Riga legale**: Belletti S.r.l., Via della Tecnica 29, 35035 Mestrino (PD), P.IVA e CF 01263940288, REA PD 190779, capitale sociale 167.000 € (da confermare se interamente versato), PEC non trovata. Poi Privacy e Cookie.

## 9. Da confermare

- Il 1908: è l'anno in cui Rodolfo Belletti comincia a installare ascensori? Il sito dice "nel Novecento" e "primo dopoguerra".
- Gli anni di "Botti e Belletti", "Officine Meccaniche Belletti" e "PBP Elevatori", e il rapporto con la srl del 1984.
- I nomi sotto i ritratti seppia (`storia1-4`) e gli originali a risoluzione piena.
- Gli originali del fotografo del depliant 2008, con i diritti d'uso (Galleria Cavour, sede, Ca' Michiel, Thunderbird).
- Quali lavori si possono nominare e fotografare oggi; se Galleria Cavour, Ca' Michiel, Cà della Nave, XXI Investimenti, Legnago e Cannaregio sono tutti loro dalla progettazione alla posa.
- Il numero dei tecnici: "oltre venti" sul sito, "decine" nel depliant.
- I certificati aggiornati: le copie online di ISO 9001 (scaduta il 24/10/2021) ed Eurofins Allegato XI (scaduta il 22/12/2024) vanno sostituite. Il DURC online è del 2022.
- Il Safety Lift Group: esiste ancora e ha un sito? Il dominio safetylift.it non risponde.
- PEC, capitale versato, dipendenti esatti (30, 31 o 33).
- Se il fax 049 9003778 serve ancora.
- La pagina Facebook (attiva?) e se vogliono tenere lo sponsor Pallavolo Padova nel piede.
- I dati tecnici massimi: portata fino a 24.000 kg per i montacarichi sul sito, contro "tra 24 e 12.000 kg" nel depliant del 2008.
- Se fanno ancora scale mobili e servoscala in proprio o con partner.
