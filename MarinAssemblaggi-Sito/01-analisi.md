# Marin Assemblaggi: analisi per la nuova home

Sito: http://www.marinassemblaggi.it/ (crawl e screenshot del 20/10/2026). È una pagina unica con ancore; `galleria.html` risponde 404. Fonti citate come URL + frase.

## 1. In breve

- **Chi**: Marin Assemblaggi srl, via Emilia Romagna 26, 35020 Saonara (PD). La sede è a **Saonara**, non a Noventa Padovana: lo dicono i contatti, il piede, la mappa e i registri. "Noventa Padovana" resta solo nel `<title>` e in una frase di "Cosa facciamo", ed è un avanzo da correggere. La mappa di Google incorporata mette il punto in "Via Emilia e Romagna, 26, 35020 Villatora PD", cioè la frazione di Saonara vicino al casello di Padova Est.
- **Cosa fa davvero**: montaggio meccanico **per conto terzi**. Assembla "componenti metallici e in plastica" con presse, avvitatori a coppia controllata, marcatrici a punti e laser, e poi conta, termosalda ed etichetta per il confezionamento. Su richiesta costruisce anche le attrezzature di montaggio. Non progetta né produce un proprio prodotto.
- **Per chi**: aziende che mandano fuori il montaggio. Il sito non nomina nessun cliente. Le foto mostrano componenti per l'alta pressione (impugnature con la scritta "250 bar", innesti, valvole di regolazione in ottone, cartucce con o-ring, iniettori). Che il settore sia quello delle idropulitrici è una mia lettura delle foto, non è scritto da nessuna parte.
- **Da quando**: la srl è stata costituita il 20/12/2016 (companyreports.it). Il sito dice "da oltre venti anni", ma è un testo senza data: il codice di Analytics UA-59471417 colloca il sito intorno al 2015. Quindi prima della srl c'era quasi certamente un'altra ditta (sez. 9).
- **Quanti**: da 10 a 19 dipendenti, fatturato 2025 di € 616.069, costo del personale di € 424.929 (companyreports.it). È un reparto di montaggio vero, con le persone come costo principale.
- **Il punto**: Marin fa la parte che il cliente non vede, cioè il pezzo che arriva sciolto ed esce montato, avvitato alla coppia giusta, marcato e contato. Il loro materiale ha già un'immagine che lo racconta (sez. 4).

## 2. Il sito di oggi

**Pagine**: una sola pagina con le ancore Chi siamo, Cosa facciamo, Contatti, Dove siamo, più la mappa e il piede. Il link "Photo gallery" è commentato nel codice e la pagina non esiste.

**Testi veri essenziali (verbatim)**:
- Titolo: "Marin Assemblaggi", con sotto "Eseguiamo assemblaggi meccanici di precisione per conto terzi". Bottone: "click e scopri chi siamo".
- Meta description: "Marin Assemblaggi SRL a Saonara (PD). Eseguiamo assemblaggi meccanici di precisione per conto terzi."
- Chi siamo:
  - "La nostra ditta opera da oltre venti anni nel settore dell'assemblaggio meccanico per conto terzi ed esprime il meglio nella precisione e puntualità, tipico delle aziende Venete e caratteristico del Made in Italy. I nostri Committenti ve lo confermeranno."
  - "La nostra sede è situata in Via Emilia Romagna 26 a SAONARA (PD), a poche centinaia di metri dall'uscita autostradale Padova Est e a pochi minuti dal centro di Padova."
- Cosa facciamo:
  - "Si eseguono assemblaggi di componenti metallici e in plastica. La nostra ditta opera da molti anni nel settore ed è nota per la precisione, serietà e puntualità."
  - "Disponiamo dei seguenti macchinari:", seguito da un elenco di nove voci, riportato per intero:
    - "Presse idrauliche montate su tavola rotante con potenza di 6 tonnellate per eseguire cianfrinature e coniature"
    - "Avvitatori oliopneumatici con controllo di coppia da 3 a 60 N"
    - "Marcatrici a multipunto con campo di lavoro 70x90mm. con possibilità di inserimento loghi"
    - "Avvitatori elettrici con controllo di coppia da 3 a 15 N"
    - "Bilance contapezzi per confezionamento"
    - "Macchine termosaldatrici"
    - "Stampante per etichette personalizzabili"
    - "Disponibilità a costruire eventuali attrezzature atte al montaggio dei particolari"
    - "Marcatura Laser"
  - Nota: la coppia è scritta in "N", ma dovrebbe essere N·m (o N·cm). L'unità va chiesta prima di metterla in pagina.
- Dove siamo: "Ci troviamo nelle vicinanze del casello di Padova EST."
- Orari: "lunedì - venerdì mattina 8.30- 12.30 pomeriggio 13.30 - 17.30 sabato chiuso".
- Sul sito non ci sono certificazioni, numeri, clienti né settori. Dalle foto si capisce che la marcatrice laser è una Sisma serie EASY (`easy.jpg`, foto del costruttore).

**Tecnologia**:
- È un HTML statico su Apache (Register.it / dadapro). L'ultima modifica è del 29/04/2026, ma solo per il copyright "2026".
- Usa il tema "Freelancer" di Start Bootstrap su Bootswatch 3.3.1, jQuery 1.11.1 e Font Awesome 4. Il testo è in Open Sans, con il verde #56E13B per i link e il blu ardesia #2C3E50.
- C'è Google Analytics "UA-59471417-2" (analytics.js), un servizio dismesso.
- `contact_me.js` punta a `mail/contact_me.php`, ma nella pagina non c'è nessun modulo.
- **HTTPS non funziona**: il certificato è "*.dadapro.com" ed è scaduto il 25/10/2025. Il sito vive solo in http.
- Mancano robots.txt, sitemap e favicon (404).
- Nel piede ci sono i social: Facebook con `href="#"` (vuoto) e Google+ (chiuso dal 2019).
- Crediti: "sito realizzato da Sistema Service" (sistemaservicesnc.it); meta author "Roberto Parisotto".

**Problemi a 1440** (`_prova/attuale/home-1440.jpg`, prima schermata in `home-1440-prima-schermata.jpg`, pezzi in `p1440/`):
- La testata è una fascia blu ardesia alta 100 px. Il "logo" è la scritta in Open Sans bold.
- Lo slider è a 4 foto con frecce e puntini. Le foto sono da 1600x600 stirate a 1440x510, e il soggetto è tagliato in alto e in basso.
- Il titolo "MARIN ASSEMBLAGGI" è centrato in maiuscolo sotto lo slider; il bottone dice "click e scopri chi siamo".
- Sotto il titolo arriva subito un'altra foto di ottoni.
- Le sezioni sono tutte centrate su fondi blu alternati e il testo è grigio a 16 px.
- L'elenco delle macchine è un elenco puntato piccolo, seguito da cinque strisce di collage di altezze diverse: dittici, trittici, quattro verticali e le marcatrici scontornate.
- I contatti sono su tre righe con le etichette sottolineate a puntini. L'email è verde fluo #56E13B su blu, che non regge il contrasto AA.
- La mappa è a tutta larghezza. Nel piede ci sono due icone social morte e il copyright.
- La pagina è alta 6617 px senza dire più di cinque frasi.

**Problemi a 390** (`home-390.jpg`, pezzi in `p390/`):
- Lo slider è alto 145 px e i pezzi sono minuscoli.
- La foto sotto il titolo diventa una striscia di 230x75.
- I collage diventano francobolli da 120 px.
- I titoli "COSA FACCIAMO" vanno a capo su due righe a 44 px.
- Il bottone "torna su" copre il copyright.
- Non c'è scorrimento orizzontale. Telefono ed email non sono link (`tel:` assente, solo `mailto:`).

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Marin Assemblaggi SRL / "MARIN ASSEMBLAGGI S.R.L." | piede del sito: "Marin Assemblaggi SRL"; companyreports.it/marin_assemblaggi_srl-05025290288: "MARIN ASSEMBLAGGI S.R.L." |
| Forma | società a responsabilità limitata | companyreports.it (stessa pagina): "SOCIETA' A RESPONSABILITA' LIMITATA" |
| P.IVA / CF | 05025290288 | piede: "P.IVA 05025290288"; companyreports.it: "Codice Fiscale 05025290288" |
| REA | PD 437367 | companyreports.it: "il numero REA PD 437367" (aggregatore, non visura) |
| Indirizzo | Via Emilia Romagna 26, 35020 Saonara (PD) | sito, Contatti: "Via Emilia Romagna 26 35020 SAONARA (PD)"; mappa: "Villatora PD" |
| Telefono e fax | 049 8070512 (stesso numero) | Contatti: "Tel: (+39) 049.8070512 Fax: (+39) 049.8070512"; piede: "Tel./Fax 049. 8070512" |
| Email | info@marinassemblaggi.it | Contatti e piede, con `mailto:` |
| PEC | non trovata | |
| Orari | lun-ven 8.30-12.30 e 13.30-17.30, sabato chiuso | Contatti: "ORARI APERTURA lunedì - venerdì mattina 8.30- 12.30 pomeriggio 13.30 - 17.30 sabato chiuso" |
| Costituzione | 20/12/2016 | companyreports.it: "La data di costituzione è 20/12/2016" |
| Attività da sito | "da oltre venti anni" | Chi siamo (testo senza data, sito del 2015 circa) |
| ATECO | 28.29.99 | companyreports.it: "28.29.99 - Fabbricazione di altre macchine varie di impiego generale n.c.a." |
| Dipendenti | da 10 a 19 | companyreports.it: "N. Dipendenti da 10 a 19" |
| Fatturato | € 616.069 (2025); utile € 1.022; personale € 424.929 | companyreports.it: "Fatturato € 616.069 (2025)", "Risultato d'esercizio € 1.022", "Costo del personale € 424.929" |
| Altro sui conti | 2024 "Tra 300.000 e 600.000 Euro", "+5,89% rispetto a 2023"; capitale "aumentato del 400%" nel 2024 | informazione-aziende.it/Azienda_MARIN-ASSEMBLAGGI-SRL (da un estratto di ricerca: la pagina risponde 429) |
| Capitale sociale | cifra non trovata | |
| Social | nessuno attivo | piede: Facebook `href="#"`, Google+ chiuso; la ricerca non trova pagine |

## 4. Materiale visivo

Ho scaricato 11 foto (1,2 MB) in `assets/originali/`. L'inventario, con misure, soggetto e voti (qualità / forza come apertura, da 1 a 10), è in `_prova/inventario-immagini.json`; il foglio provino è in `_prova/fogli/originali.jpg`. Non ci sono video. Sei foto da studio portano nell'EXIF "KeKKo-clicK": c'è stato un fotografo vero.

| Foto | Misure | Qualità | Apertura | Giudizio |
|---|---|---|---|---|
| `8407.1600.jpg`: corpi in ottone, sfere d'acciaio, bossolo con sfera montata, su bianco a specchio | 1600x600 | 7 | **7** | la migliore e la più loro. Chiara e con pochi pezzi, mostra lo sciolto accanto al montato (la sfera libera e la sfera nella sede). È piccola: regge a 1x su circa 1000 px di larghezza, non a 2x |
| `8447.1600.jpg`: tavola di innesti, impugnature "250 bar", cartucce, o-ring | 1600x600 | 7 | 6 | nitida ma affollata, va ritagliata. Si leggono i marchi dei pezzi |
| `slide2.jpg`: cumulo di bussole in ottone con o-ring montato | 1600x600 | 7 | 5 | una texture calda: buona per la chiusura, non per l'apertura |
| `slide3.jpg`: tappi inox con o-ring, su bianco | 1600x600 | 6 | 5 | pulita, grigia, con un alone aggiunto ai lati |
| `37.1200.jpg`: macro di un corpo valvola in ottone | 1200x400 | 6 | 4 | piccola; il pomello rosso è di un prodotto finito |
| `2.1200.jpg`, `3img.1200.jpg`, `img3.jpg`: dittici e trittici montati | 1200 di base, pezzi da 300-600 px | 4-6 | 1-3 | collage, non foto. La terza di `img3` è da telefono e va esclusa |
| `MAC_2x.jpg`, `MAC_4.jpg`: avvitatore con alimentatore Quicher, centralina, pressa su tavola rotante, presse pneumatiche, marcatrice a punti | pezzi da 295x442 a 600x395 | 5 | 2 | vere e preziose come prova delle macchine, ma con luce piatta, ambienti disordinati e piccole |
| `easy.jpg`: marcatrici Sisma EASY scontornate | 1200x486 | 5 | 1 | foto del costruttore, non loro |
| Logo | nessuno | | | c'è solo la scritta Open Sans della testata (`logo-scritta-testata-2x.png`) |

**Verdetto**:
- Il materiale **regge a metà**, con una media di 5,5 su 10.
- Per una prima schermata chiara con un solo oggetto, `8407` ha il soggetto giusto, la luce giusta e il racconto giusto (sciolto e montato). Ha un solo limite: la risoluzione.
- Le foto del reparto dicono la verità, ma non sono belle.
- Per la proposta bastano `8407` (ritagliata, a 1x), `slide2` per la chiusura e un paio di segnaposto (sez. 6).
- Per il sito vero serve una mezza giornata con lo stesso fotografo:
  - lo stesso set di `8407` a 6000 px;
  - tre "sciolto e montato" su bianco;
  - una sequenza dal reparto con le mani all'avvitatore e alla pressa, su fondo pulito.

## 5. Due direzioni artistiche

Graziella e N19: **non le uso**. È montaggio conto terzi B2B, senza moda né lusso. Ne tengo solo la regola generale di molta aria ed etichette piccole, cosa che la ricetta del committente chiede già.

**Direzione A, "Sciolto e montato" (chiara, un solo oggetto vero)**
- Idea visiva: su carta bianca calda, i cinque pezzi di `8407` grandi e nitidi a destra, con il riflesso a specchio. Il titolo grande a sinistra è "Assemblaggi meccanici di precisione" e sotto c'è una riga dal sito: "per conto terzi, a Saonara". Legende numerate a filo sottile sui pezzi: corpo in ottone, sfera d'acciaio, sede, pezzo montato.
- Immagini: le loro foto da studio su bianco (`8407` in apertura, `slide3`, i ritagli di `8447`); segnaposto Mastars ed EnCata. La chiusura è la foto `slide2` a tutta larghezza.
- Tipografia: una grotesk precisa e asciutta, per esempio Switzer o General Sans (Fontshare, ITF Free Font), con titoli da 96-120 px e peso 400, più una mono piccola come IBM Plex Mono (OFL) per i dati: "6 t", "3-60", "70x90 mm".
- Colore: carta #F4F3EF, inchiostro #1B1D1F, acciaio #8A9097 per le legende, ottone #8C6A2B solo per i numeri e i filetti (AA su carta per il testo grande). Niente blu ardesia né verde fluo.
- Gesto: un interruttore "Sciolto / Montato" sotto la foto, con taglio netto e senza dissolvenza. Mostra i pezzi separati o il pezzo finito: oggi lo fa un ritaglio diverso della stessa foto, domani due scatti rifatti.

**Direzione B, "Coppia giusta" (scura ma pulita, i numeri protagonisti)**
- Idea visiva: grafite piena e una sola foto metallica in luce radente, cioè le sfere d'acciaio (segnaposto Ferreira) o le bussole di `slide2`. Al posto del titolo-slogan c'è la scheda del reparto: le macchine vere del loro elenco con il loro numero grande (6 t, 3-60, 3-15, 70x90 mm).
- Immagini: macro di metallo su nero, i perni in fila di Westbeek, le mani al montaggio di Auto Tech. Le foto del reparto `MAC_4` vanno in monocromo, piccole e in fila regolare.
- Tipografia: Archivo (Google Fonts, OFL), con la larghezza espansa per i numeri a 160-200 px e la normale per il testo; numeri tabellari.
- Colore: grafite #15171A, acciaio chiaro #D5D9DD per il testo (AA), ottone #C9A25A per un solo accento. Il contrasto resta alto e non ci sono grigi su grigio.
- Gesto: un selettore delle macchine (Presse, Avvitatori, Marcatura, Confezionamento). Il numero grande e la riga verbatim cambiano al clic, con un cambio netto.

Al committente piace la A: è chiara, ha un pezzo vero e le legende come Mario Agnoletto. La B va tenuta solo se il fotografo rifà le macro su nero.

## 6. Immagini sostitutive

Ci sono 9 foto in `assets/esterne/` a 2400 px: 6 Unsplash e 3 Pexels, con la licenza controllata sulla pagina il 20/10/2026. Nessuna è Unsplash+ o IA, e nessuna è già usata nella campagna (controllo fatto su tutti i `*-Sito/assets/CREDITI.md`). URL, autori e note sono in `assets/CREDITI.md`.
- Per A: Mastars (alberi, ingranaggi, bussole su bianco, l'alternativa all'apertura se `8407` non si può usare), EnCata (flange su disegno), Fish Steak Fries (dadi in ottone), Nic Wood (ogive in ottone), Westbeek (calibro al banco).
- Per B: Ferreira (sfere d'acciaio su scuro, apertura), Westbeek (perni in fila), Auto Tech (mani che montano), Opt Lasers (testa laser; foto indicativa, non è una marcatrice in fibra).
- Manca una foto dell'avvitatura a coppia controllata e della pressa su tavola rotante: queste vanno fatte dal vero da Marin.

## 7. Riferimenti di alta gamma nel mestiere

Prime schermate a 1440 e 390 in `riferimenti/` (JPEG q78), viste il 20/10/2026. I font sono letti dal codice.

1. **Sisma** (sisma.com, laser e macchine per oreficeria; è il costruttore della marcatrice di Marin).
   - Alta gamma: la macchina fotografata come un gioiello su nero, il logo con il segno oro, sei voci di menu corte.
   - Da non riprendere: lo slider con le frecce; il titolo in Montserrat 300 maiuscolo oro sopra la foto, che si legge male; a 390 il pannello dei cookie copre tutta la schermata anche dopo il rifiuto.
2. **FSB** (fsb.de, maniglie e ferramenta, Brakel).
   - Alta gamma: un solo pezzo di metallo enorme e nitido, con un'ombra morbida e la grana vera della superficie. Il carattere è Traffic e il logo è un segno minimo. A 390 il pezzo resta protagonista in un quadrato. È la lezione giusta per `8407`.
   - Da non riprendere: la barra gialla acida "Product Finder", i 200 px bianchi vuoti sopra la foto, il fondo scuro sfumato.
3. **Olivari** (olivari.it, maniglie dal 1911).
   - Alta gamma: la maniglia satinata a tutta pagina in luce radente, con il prodotto che parla da solo. A 390 c'è un taglio verticale con il titolo sovrapposto.
   - Da non riprendere: il menu maiuscolo spaziato bianco sulla foto (contrasto), i puntini dello slider, il corsivo per le parole d'accento.
4. **Fantini** (fantini.it, rubinetti in ottone).
   - Alta gamma: "WELL MADE IN ITALY" in Messina Sans a 115 px su tutta la larghezza, tre titoletti in basso come indice, "Manifattura italiana" come etichetta. È la sicurezza tipografica che serve ad A.
   - Da non riprendere: il video del lago al posto del prodotto, la testata doppia piena di icone, il banner dei cookie a due passaggi.
5. **LEMO** (lemo.com, connettori push-pull di precisione, Svizzera).
   - Alta gamma: il titolo "EMPOWERING CONNECTIVITY" in Suisse Intl 700 a 160 px, su due righe bianco e blu, su un grigio chiaro sfumato, con un filetto verticale che scende verso il contenuto. È il rigore svizzero della precisione.
   - Da non riprendere: la prima schermata è un video che nel Chromium di prova resta vuoto (si vede solo il fondo); il bottone blu pieno; la fila di icone nella testata.

Scartati:
- Bossard e Mikron: hero da catalogo e da gruppo industriale, con un riquadro bianco sopra la foto.
- Swagelok: persone in posa e icone in fila.
- Teenage Engineering: fuori registro.
- Brovedani: dominio in vendita.
- Lauener, Fischer Connectors, Elesa e Kern: non si aprono dal browser di prova (errore o controllo anti-bot).

## 8. Per il piede

- **Logo**: non esiste sul sito. Non c'è un'immagine, un SVG, una favicon o un'icona d'app; il marchio è la scritta "MARIN ASSEMBLAGGI" in Open Sans 700 bianca su #2C3E50, salvata a 2x in `assets/originali/logo-scritta-testata-2x.png` solo come documento. Va chiesto se esiste un logo (carta intestata, insegna, furgoni). Senza logo, il piede userà la ragione sociale composta nel carattere della pagina, senza inventare un marchio.
- **Voci di menu e pagine di oggi**: Chi siamo, Cosa facciamo, Contatti, Dove siamo (ancore della pagina unica); "Photo gallery" è disattivata e restituisce 404.
- **Pagine del sito nuovo** (per le colonne di link):
  - Lavorazioni: Assemblaggio, Avvitatura a coppia controllata, Cianfrinatura e coniatura, Marcatura laser e a punti, Confezionamento ed etichette, Attrezzature di montaggio;
  - Azienda: Chi siamo, Il reparto (macchine), Dove siamo;
  - Contatti: telefono, email, indirizzo con la mappa, orari;
  - in fondo: Privacy, Cookie.
- **Social**: nessuno che esista davvero. Facebook è un link vuoto (`#`) e Google+ (`plus.google.com/u/0/103481430714990084914`) è chiuso dal 2019. La colonna "Seguici" non va messa.
- **Newsletter**: **non ha senso**. Marin è un terzista B2B: non ha prodotti propri, notizie, fiere, cataloghi né clienti privati, e chi lo cerca telefona. Nella NOTA andrà una riga che lo spiega.
- **Riga legale**: Marin Assemblaggi S.r.l., P.IVA e C.F. 05025290288, Via Emilia Romagna 26, 35020 Saonara (PD). REA PD 437367 da confermare con la visura. Capitale sociale e PEC non trovati. Poi Privacy e Cookie.

## 9. Da confermare

- La sede e il nome del comune nel titolo: Saonara (o Villatora di Saonara). Togliere "Noventa Padovana": era forse una sede precedente?
- L'anno di inizio dell'attività e la ditta prima della srl del 2016: "da oltre venti anni" da quando?
- REA PD 437367, il capitale sociale e la PEC: servono dalla visura.
- L'unità della coppia degli avvitatori ("da 3 a 60 N" e "da 3 a 15 N": sono N·m? N·cm?).
- Se esiste un logo vettoriale.
- I diritti delle foto di "KeKKo-clicK" per il sito nuovo, e se si possono mostrare i pezzi dei clienti (si leggono scritte e marchi).
- I settori e i clienti tipo (alta pressione? idropulitrici? altro?) e se si possono nominare.
- Se il fax è ancora attivo (è lo stesso numero del telefono).
- Le marcatrici: oltre alla laser Sisma EASY, quale marcatrice a punti è (quella con il display nella foto `MAC_4`)?
- Se ci sono certificazioni (ISO 9001 o altre), lotti minimi e massimi, tempi di consegna: sul sito non c'è nessun numero.
- Se si può fotografare il reparto con le persone.
