# S: i concorrenti migliori del gruppo servizi tecnici e imprese

Ricerca del 3 novembre 2026 per le 10 aziende del gruppo S. Per ogni mestiere ho cercato aziende che fanno lo stesso lavoro, di fascia alta, con il sito più curato che sono riuscito a trovare: in Germania, Svizzera, Austria, Regno Unito e Stati Uniti. Dove possibile ho preferito l'azienda di famiglia alla multinazionale.

**Metodo**
- Ricerca con WebSearch (in tedesco, inglese, olandese e italiano). Per questi mestieri Awwwards non dà niente: nessuna carrozzeria, officina di carrelli, ascensorista o impresa di spurgo premiata. Il vicino più prossimo, Knupfer Metallbau, è già in `awwwards.md`.
- Ho aperto con Playwright circa 45 siti candidati. Ne tengo **21**. Gli scarti sono elencati più sotto, con il motivo.
- Le schermate sono in `alto/S/`: `<sito>-1440.jpg` è la prima schermata 1440x900, `<sito>-1440-intera.jpg` la pagina intera (tagliata a 9000 px), `<sito>-390.jpg` la prima schermata 390x844. Le ho guardate a pezzi, in colonne fatte con PIL. Ho guardato così anche le 10 home nostre in `screenshot/home/`.
- Famiglie, misure, pesi e interlinee dei caratteri li ho letti dal DOM, con il primo titolo e il primo paragrafo visibili. Margini e quote della foto li ho stimati sulle schermate, quindi sono approssimativi.

**Limiti delle schermate**
- Il Chromium del container non riproduce i video H.264. Per questo l'apertura è vuota (grigia o nera) su Eberhard, Kraftwerk, Brandenburg ed Emch, e il primo slide di Schmitt + Sohn cade su una notizia. Dove serviva, l'ho descritta da quello che resta: titolo, cornice, poster.
- Cookie e finestre li ho chiusi quando si poteva. Su Alberts il velo grigio della finestra dei cookie resta sopra la pagina, che si legge lo stesso. Su Jacksons, a 390, resta la finestra "Welcome to Jacksons, how can we help?", che è parte del sito e ne parlo nella scheda.
- Willenbrock, Alpine, Alberts e BELFOR non si lasciano fotografare per intero in un colpo solo. La loro pagina intera è fatta di schermate 1440x900 impilate, per cui la testata fissa si ripete.

**Siti scartati e perché**
- Turner Body Shop, Livingston Collision, Town 2 Auto Body (carrozzerie USA): modelli da agenzia locale, foto scure, bottoni ovunque.
- Carrosserie Neeser, Holdener, Aeschlimann, Maier, Schenkel Weibel, Heinz Volk & Sohn (carrozzerie svizzere e tedesche): modelli Divi o WordPress senza disegno proprio. Riegelhof non si carica (pagina bianca). Winiger risponde 502.
- Premium Lift Truck (carrelli, USA): l'apertura è una parete di medaglie "Royal Source".
- Gruma (carrelli): portale con negozio online.
- Heide-Flex (tubi oleodinamici): sito in Times di sistema, senza foto.
- Polygon, Heras: multinazionali con il sito da portale.
- Black Equipment, Eigenmann: bloccati da Cloudflare. Hydraquip: "429 Too Many Requests". Raab: 502. Kuipers Heftrucks, Stapler-Service Schütze, Hoffmann Fördertechnik, Schauer Stapler, Wybo: non raggiungibili dal proxy.

Dove un sito scartato ha un dato utile, lo cito.

**In una frase**: in questo gruppo i siti migliori non vincono con la grafica ma con tre cose. La prima è una foto vera, larga, della squadra o del mezzo, con il marchio addosso. La seconda sono i nomi: delle persone, dei lavori, dei clienti. La terza è un numero d'emergenza separato e sempre in vista. Le nostre home hanno già la parte d'uso, spesso meglio di loro: orari, moduli divisi per bisogno, cosa mandare. Mancano le facce, i nomi, la foto grande. E l'apertura è sempre la stessa: titolo a sinistra, foto a destra, due bottoni, fila di ingressi sotto.

---

## 1. Le nostre aziende, una per una

### Serenissima Service (Padova, zona industriale)
Carrozzeria, officina meccanica e meccatronica, elettrauto, cristalli, grandine, soccorso stradale e auto sostitutive in una sede sola di 3000 mq, con 9 cabine di verniciatura. Fiduciaria di 26-27 compagnie, nata nel 1993 da un ramo di una carrozzeria degli anni Sessanta.
- **Auto Bayertz** (Düsseldorf, dal 1945, terza generazione): carrozzeria e verniciatura con soccorso 24 ore, auto sostitutiva gratuita e liquidazione diretta con le assicurazioni. È lo stesso servizio "pensiamo a tutto noi", e il sito è il più completo del mestiere che ho trovato.
- **Geser** (Altdorf, Uri, dal 1960): carrozzeria e verniciatura con soccorso stradale, molto più piccola. La tengo perché apre con la sola foto della cabina di verniciatura a tutta pagina.
- Il loro sito fa X che la nostra home non fa:
  - **Auto Bayertz** mette le persone con il nome e la foto: Timo e Nicolas Bayertz, che guidano l'azienda, e l'assistente di servizio, in tre ritratti uguali. Racconta la storia con il nome del fondatore (Willy Bayertz, 1945) e mostra il reparto in una galleria di 12 foto quadrate, tutte dello stesso fotografo. La nostra home ha i numeri (3000 mq, 9 cabine, 12 ponti) ma nessuna faccia e nessun nome.
  - **Geser** apre con la cabina di verniciatura vuota a tutta larghezza e il titolo sopra. La nostra home apre con il carro attrezzi a metà schermo, accanto al testo, e le 9 cabine non si vedono mai in grande.

### Unicar (Padova, via Canada 12)
Officina di assistenza, ricambi e controlli per carrelli elevatori di ogni marca (soprattutto BT e Cesab, oggi Toyota), con i furgoni presso il cliente. È la consociata d'assistenza di Cami2, che vende e noleggia.
- **Hesse Fördertechnik** (Wietze, vicino a Celle, a conduzione familiare dal 1996): assistenza carrelli di ogni marca, con il servizio mobile e l'officina. È la più vicina per misura e per mestiere.
- **Willenbrock** (concessionario Linde Material Handling nel nord della Germania): la tengo come esempio di quello che succede quando l'officina sparisce dietro al marchio del costruttore, il rischio di Unicar con Toyota e Cami2.
- Il loro sito fa X che la nostra home non fa:
  - **Hesse** riassume il patto in tre parole sotto il titolo, "Markenunabhängig. Persönlich. Vor Ort." (indipendente dalla marca, di persona, sul posto), e lo chiude con un motto che torna due volte: "Reparieren statt Ersetzen", riparare invece di sostituire. La nostra home ha un titolo forte, "Consulenti, più che riparatori", ma nessuna frase che ritorni. Ha poi un modulo in 9 passi che si apre con "Worum geht es bei Ihrer Anfrage?" e chiede "ein Foto des Typenschilds". La nostra chiede la targhetta solo per i ricambi.
  - **Willenbrock** mette in prima schermata quattro ingressi per quello che uno vuole fare: noleggiare, comprare, trovare il proprio referente, lavorare lì. La nostra home ha gli ingressi per servizio, non "trova il tuo tecnico".

### Eurotecnica Salmaso (Padova, via Lussemburgo 48)
Progetta, vende, installa e noleggia impianti audio e video per sale consiliari, aule, teatri e chiese. Fa service per convegni (amplificazione, traduzione simultanea, riprese, streaming) e ha un negozio, l'"emporio dell'audio". Quattro dipendenti, abilitata MePA.
- **Habegger** (Svizzera): tecnica e produzione per eventi, allestimenti e sale. È molto più grande, ma fa lo stesso lavoro "service più impianti" e ha il sito più curato del mestiere.
- **Kraftwerk Living Technologies** (Wels, Austria): integratore di sistemi audio e video, impianti fissi e attrazioni multimediali. Lo tengo come esempio negativo: la home è solo un video.
- Il loro sito fa X che la nostra home non fa:
  - **Habegger** dà a ogni lavoro il nome del cliente e dell'evento sotto una foto grande ("Hecht «LOVERS» Tour 2025/26", "Julius Bär «Open House»", "Seaside Festival"). Apre con un tecnico di spalle, con il nome Habegger sulla maglia. La nostra home mostra sale belle ma senza il nome di chi le usa.
  - **Kraftwerk** elenca ogni sede con la ragione sociale, l'indirizzo, il telefono e l'email, tutte uguali. Da noi la sede e il negozio stanno in fondo, ma il negozio non ha un suo blocco con orari e telefono separati dall'ufficio impianti.

### Fratelli Zuin (Padova Est, via Bassette 6/A)
Scavi e movimento terra, cassoni scarrabili da 2 a 25 m³, demolizioni, fognature e spurgo, strade, escavatori a risucchio. Impresa di famiglia dal 1946, con l'attestazione SOA per i lavori pubblici.
- **Eberhard** (Kloten, Zurigo, terza generazione, da oltre 70 anni): scavi, demolizioni, bonifiche, riciclaggio dei materiali da costruzione e "Saugtechnik", cioè gli escavatori a risucchio. È lo stesso mestiere, più grande.
- **Brandenburg** (Elmhurst, Illinois, dal 1968): demolizioni, bonifiche e preparazione dei siti, con sette sedi regionali.
- Il loro sito fa X che la nostra home non fa:
  - **Eberhard** mostra le referenze come foto grandi con il nome del cantiere e il luogo ("GISA Siedlung, Binzmühlestrasse 292, Zürich Affoltern", "Rathausbrücke, Zürich"). In testata mette la voce "Notfalldienste", il servizio d'emergenza. La nostra home ha i lavori a Padova (ex Foro Boario 1968-69, sede dell'Azienda del Gas, Prato della Valle) solo come righe di testo, senza foto.
  - **Brandenburg** apre con il nome di un lavoro e il suo film ("Demolition of the Johnsonville Fossil"), non con l'elenco dei servizi. La nostra home apre con l'elenco ("Scavi, cassoni scarrabili, strade e fognature").

### Nord Service (Mestrino, via Levico 20)
Riporta a nuovo la carrozzeria di macchine da lavoro: sabbiatura a secco con garnet, fondi e vernici a liquido, vetroresina, carpenteria, vetri. Lavora sulla macchina intera o sul singolo pezzo. Padre e figlio, Stefano e Leonardo Barbieri.
- **Alpine Painting & Sandblasting** (Paterson, New Jersey, di famiglia dal 1975): verniciatura e sabbiatura industriale, con un reparto chiuso accanto alla sede per i mezzi pesanti e i pezzi grandi.
- **Cleveland Brothers** (concessionario Caterpillar in Pennsylvania): la loro pagina "Paint & Blasting" (non la home) è la descrizione più chiara che ho trovato di un reparto che rivernicia macchine movimento terra di ogni marca.
- Il loro sito fa X che la nostra home non fa:
  - **Alpine** mette nella prima schermata la foto, il nome e il numero diretto di chi fa i preventivi. In home ha un caso con il cliente nominato ("Project: Exterior asphalt plant painting, Haledon, N.J. Client: Braen Stone") e la squadra in cinque ritratti con nome e ruolo. La nostra home nomina Stefano e Leonardo Barbieri, ma senza la faccia.
  - **Cleveland Brothers** dà le misure della cabina, "65' x 35' x 30'", e dice che cosa ci entra: cassoni ribaltabili, rimorchi, motori, macchine di ogni marca. La nostra home dice "tutta la macchina o un pezzo solo", ma non dice fin dove arriva la cabina.

### Belletti Ascensori (Mestrino, via della Tecnica 29)
Ascensori, montacarichi, piattaforme, servoscala, scale mobili, ammodernamento e assistenza 24 ore. Il mestiere è di famiglia dal 1908, oggi con circa 30 addetti.
- **Emch Aufzüge** (Berna, della stessa famiglia dal 1880, circa 200 persone): "Schweizer Manufaktur für Lift- und Hebetechnik", con impianti su misura, ammodernamento e servizio.
- **Schmitt + Sohn Aufzüge** (Norimberga, dal 1861, sei generazioni): ascensori nuovi, servizio e ammodernamento in tutta Europa.
- Il loro sito fa X che la nostra home non fa:
  - **Emch** divide l'ammodernamento in casi con i limiti tecnici. Distingue la modernizzazione, la trasformazione, l'impianto sostitutivo ("Förderhöhen bis 30m", "Nutzlast zwischen 180 und 1600kg") e il nuovo ascensore in un edificio esistente. Ogni caso ha il suo elenco. Fotografa gli impianti come architettura, e per "Individualanlage" usa uno schizzo a matita. La nostra home ha i lavori con i dati tecnici (e in questo è più avanti), ma l'ammodernamento è un blocco unico.
  - **Schmitt + Sohn** fa scegliere per tipo di edificio ("Für welchen Gebäudetypen ist der Aufzug geplant?": abitazioni, edifici commerciali, sanità, altro) e tiene "Service24: (0800) 24-00-365" nella barra in alto di ogni pagina. La nostra home divide gli impianti per prodotto (ascensori, piattaforme, montacarichi), che è la lingua del costruttore e non di chi ha un condominio.

### La Termica (Mestrino, via Bologna 6)
Vende, progetta, installa e mantiene canne fumarie in inox e in rame per case, condomini e industria. Fa videoispezione, spazzacamino e intubamento, costruisce armadi su misura in inox e vende stufe. Ha un magazzino di oltre 500 mq. Famiglia Camporese, dal 1978.
- **KÖGEL Schornsteine** (Backnang, dal 1918, terza generazione): progetta, costruisce, monta e risana camini, con lo showroom di caminetti "KÖGEL Feuerland".
- **Jeremias** (costruttore tedesco di sistemi di scarico fumi in acciaio inox): non posa, produce. Lo tengo per gli strumenti tecnici che offre in home.
- Il loro sito fa X che la nostra home non fa:
  - **KÖGEL** fa scegliere in apertura tra "Privatkunden" e "Geschäftskunden" e mostra in grande un fascio di camini industriali in inox contro il cielo. La nostra home ha sei problemi di casa numerati (stufa, canna da pulire, fumo in casa) e mette il condominio e l'industria solo nei lavori, più in basso.
  - **Jeremias** mette in home gli strumenti: la ricerca del camino, il listino interattivo, i download e il calcolo dell'altezza secondo le norme ("Höhenberechnung nach VDI und BImSchV"). La nostra home ha le serie a magazzino con i PDF, ma non dice se fanno il calcolo della canna secondo la norma (va chiesto, non si scrive senza conferma).

### Recinzioni Formentin (Villatora di Saonara, via Lombardia 17)
Recinzioni complete dalla vendita alla posa: rete metallica, pannelli, sistemi Betafence, cancelli, ringhiere. Produce in casa reti ondulate, colonne, ringhiere e inferriate, e ha un negozio di attrezzature edili. Dai primi anni Settanta.
- **Jacksons Fencing** (Ashford, Kent, dal 1947, terza generazione): produce e posa recinzioni in legno e in acciaio e cancelli, con una rete di posatori approvati.
- **Gust. Alberts** (Herscheid, dal 1852): produce recinzioni, ferramenta e profili, con un servizio fotografico di campagna.
- Il loro sito fa X che la nostra home non fa:
  - **Jacksons** mette la garanzia in cifre accanto al titolo ("Premium fencing with a 25 year guarantee", con il bollino dei 25 anni) e offre la guida stampata per posta ("The Good Fencing Guide", "free copy by post"). Ha i calcolatori di recinzione, cancello e pedana, e i lavori con il nome ("Martello Tower No 25 restoration project, Dymchurch"). La nostra home divide già bene privati, aziende, impianti e imprese, ma non dice nessuna garanzia (va chiesta all'azienda).
  - **Alberts** dice dove produce, "Made in Herscheid", con la foto di un saldatore al lavoro, e chiude con una frase sola: "Gemacht, um zu halten" (fatto per tenere). La nostra home dice "dalla vendita alla posa", ma il fatto che le reti ondulate le fanno loro, a Villatora, non è in apertura.

### F.R.A.M.O. (Saonara, via Liguria 32)
Officina che costruisce su misura tubi oleodinamici raccordati per alte pressioni, da 3/16" a 3", anche da campione. Accanto c'è un banco con 600 mq di magazzino per raccordi, valvole, pompe e pneumatica. Di famiglia, dal 1986.
- **HANSA-FLEX** (Brema, di famiglia, "64 Jahre Systempartner"): tubi idraulici, raccordi e servizio. È grande, ma è il riferimento del mestiere e resta della famiglia fondatrice.
- **Pirtek UK** (rete di 86 centri nel Regno Unito e in Irlanda): sostituzione dei tubi sul posto e banco di vendita. Non è di famiglia (è una rete in franchising), ma ha il sito più "da studio" del gruppo.
- Il loro sito fa X che la nostra home non fa:
  - **HANSA-FLEX** dà a ogni tubo un codice (X-CODE) per rifarlo identico e mostra il servizio mobile con il furgone e il tecnico. La nostra home ha "Porta il tubo vecchio: te lo rifacciamo identico", ma non dice che cosa resta al cliente dopo: un numero, un'etichetta, la scheda del tubo (va chiesto se lo fanno).
  - **Pirtek** usa come immagine di prodotto la foto da vicino della guaina con la scritta stampata ("PFM25-10 16MM (5/8") WP 250Bar (3600psi)"). Mette didascalie con le coordinate del luogo ("Location 51° 31' 39.756" N") e un fondo a quadretti da carta tecnica. La nostra home ha il grande riquadro giallo con "da 3/16" fino a 3"", che funziona, ma le foto dei tubi sono piccole e senza didascalia.

### Oby Group Italia (Longare, Vicenza)
Ripristino dopo un sinistro (incendio, allagamento, grandine), dalla messa in sicurezza alla ricostruzione e alle pratiche. Fa bonifiche industriali, amianto, lavori in fune e la Copertura Sicura Starflex per le compagnie. Otto dipendenti, dal 2018.
- **Restore Construction** (area di Chicago, della stessa famiglia da oltre 40 anni): ripristino dopo incendio, acqua e tempesta, con la gestione della pratica assicurativa.
- **BELFOR Svizzera** (filiale del gruppo BELFOR): multinazionale, ma il sito svizzero è il più ordinato del mestiere e parla anche alle compagnie e agli amministratori.
- **Dalworth Restoration** (Dallas-Fort Worth, dal 1976, di famiglia): sito da motore di ricerca, lo tengo per un solo blocco utile.
- Il loro sito fa X che la nostra home non fa:
  - **Restore** apre con la squadra intera, una dozzina di persone con la polo del marchio davanti alla sede, e il numero da chiamare in una barra in alto. La nostra home apre con il tetto bruciato visto dal drone, che spaventa invece di calmare.
  - **BELFOR** tiene il numero "24H/24H Hotline 0800 808 118" fisso in basso a destra in ogni schermata. Accanto a "Ansprechperson finden" mette il secondo bottone "Schadenmeldung", segnala un danno, e mostra con nome e ruolo le sette persone che dirigono. La nostra home ha i due numeri in testata, ma nessuna faccia.
  - **Dalworth** ha un blocco "Works Directly with Your Insurance Company" con i loghi delle compagnie. La nostra home ha la strada "Compagnie assicurative", ma senza nomi (vanno chiesti all'azienda).

---

## 2. Le schede dei 21 siti

Le misure sono a 1440 px. "Foto" vuol dire la quota della prima schermata 1440x900 occupata dall'immagine più grande (misurata nel DOM).

### Auto Bayertz
- **Indirizzo**: https://www.auto-bayertz.de/ (Düsseldorf).
- **Cosa fa**: carrozzeria e verniciatura dal 1945, terza generazione. Fa soccorso 24 ore, auto sostitutiva gratuita, liquidazione diretta con le assicurazioni, cristalli, levabolli, smart repair, ritiro dei leasing.
- **Prima schermata**:
  - testata bianca sottile: logo, sei voci (Leistungen, Ablauf, Galerie, Team, FAQ, Kontakt), telefono e bottone verde a pillola "Termin buchen";
  - sotto, la foto a tutta larghezza (un'auto incidentata da vicino, scurita), che prende l'88%;
  - titolo a sinistra su due righe, maiuscolo, la seconda in verde;
  - un paragrafo di quattro righe sulla storia, due bottoni (prenota online, telefono) e tre piccole promesse con icona (24 h Notfallservice, Kostenloser Ersatzwagen, 6 Jahre Garantie);
  - in fondo un nastro che scorre: "Direktabrechnung mit allen Versicherungen · Alle Fahrzeugmarken · Herstellergarantie bleibt erhalten · Original-Ersatzteile";
  - circa 12 elementi, più l'etichetta a pillola sopra il titolo.
- **Struttura**:
  1. apertura e nastro;
  2. "Alles für Karosserie & Lack aus einer Hand", sei schede con foto (cinque servizi e "Akuter Unfall?");
  3. "In vier Schritten wieder mobil", quattro passi numerati 01-04 (Melden, Abschleppen & Ersatzwagen, Reparatur & Lackierung, Übergabe mit Garantie);
  4. "Wir kümmern uns um alles", sei schede con icona e l'etichetta "kostenlos" su quelle gratuite;
  5. fascia scura "Unfall gehabt? Wir sind sofort für Sie da." con il telefono;
  6. storia "Familienhandwerk seit 1945" con foto e quattro cifre (1945, 80 Jahre, 3.000 m², 6 Jahre Garantie);
  7. galleria "Impressionen aus unserer Werkstatt", 12 foto quadrate e "Alle 14 Bilder anzeigen";
  8. squadra: tre ritratti con nome e ruolo;
  9. domande frequenti, contatti, piede (oltre i 9000 px).
- **Fotografia**: un servizio vero nel reparto, con la stessa luce fredda delle cabine, persone in tuta e maschera, movimento mosso. Le foto sono quadrate con gli angoli arrotondati. I ritratti sono in bianco e nero su fondo nero, da studio. In tutto circa 25 foto, tutte loro.
- **Tipografia**:
  - Roboto Condensed 900 maiuscolo per i titoli: 72/75 in apertura, 43/45 nelle sezioni;
  - Roboto 20/32,5 per il testo;
  - nomi delle schede 20/600;
  - a 390 il titolo è 36/37.
- **Colori**: fondo bianco verdognolo (#f4f7f5), nero verde scuro per le fasce, un verde pieno per bottoni e accenti.
- **Griglia e margini**: contenitore centrato di circa 1100 px (margini circa 170), schede a tre e a quattro colonne.
- **Dettagli da studio**:
  - i passi numerati in grande, grigio chiaro, nell'angolo della scheda;
  - l'etichetta "kostenlos" solo dove è vero;
  - la galleria tutta dello stesso servizio;
  - i nomi delle persone con il ruolo.
  - Difetti: un'etichetta a pillola con icona sopra ogni titolo, schede con icona in fila, lineette lunghe nei titoli. Sono tre divieti del committente.
  - Cosa non c'è: nomi di compagnie, recensioni con nome.
- **Prove**: anno e nome del fondatore, terza generazione con i nomi, 3.000 m², garanzia di 6 anni, liquidazione diretta con tutte le assicurazioni.
- **Contatto**: telefono in testata e in tre fasce (5 link `tel:`), prenotazione online, numero d'emergenza 24 ore.
- **Si trasferisce**:
  - i ritratti con nome e ruolo e la storia con il nome del fondatore (Serenissima: i soci, se l'azienda li dà);
  - la galleria del reparto in una serie sola, quadrata (Serenissima ha le foto del 2015 delle cabine Metron, Henergy e CIA);
  - "gratis" scritto solo dove è vero (l'auto sostitutiva, nessun anticipo).
- **Non si trasferisce**: le etichette a pillola sopra i titoli, le schede con icona, il nastro che scorre (è movimento senza informazione).

### Geser
- **Indirizzo**: https://geser.swiss/ (Flüelerstrasse 134, Altdorf).
- **Cosa fa**: carrozzeria e verniciatura per tutte le marche dal 1960, gestione del sinistro, auto sostitutiva, soccorso stradale.
- **Prima schermata**:
  - testata bianca con il logo e sei voci maiuscole piccole (Home, Beratung im Schadenfall, Dienstleistungen, Team, Kontakt, Versicherungspartner);
  - sotto, la cabina di verniciatura vuota, bianca, fotografata in asse: prende il 92%;
  - un filetto nero corto, il titolo su tre righe a sinistra, un riquadro bianco velato con due righe e un bottone nero a pillola "Kontakt aufnehmen";
  - sei elementi.
- **Struttura**:
  1. apertura;
  2. "Carrosserie & Spritzwerk für alle Automarken" e la riga sulle assicurazioni;
  3. tre schede con icona e "Jetzt anrufen";
  4. "Über uns" con la facciata in un cerchio;
  5. "Kundendienst" e tre schede sfalsate numerate 01-03 (Schadenmanagement, Mobilität, Abschleppdienst);
  6. "Beratung im Schadenfall" con tre punti;
  7. giro virtuale in 3D (incorporato, bloccato senza consenso);
  8. una recensione con nome;
  9. indirizzo e modulo sopra la foto del reparto, piede.
- **Fotografia**: tre foto vere (cabina, facciata, reparto), prese bene, in luce piatta.
- **Tipografia**:
  - DM Serif Display 66/72 peso 500 per i titoli, 48 nelle sezioni;
  - Josefin Sans 18/30 in grassetto per il testo, che si legge male;
  - a 390 il titolo è 24/26, troppo piccolo.
- **Colori**: bianco, grigio chiaro, lavanda e verde menta pastello, nero per i bottoni.
- **Griglia e margini**: margini di circa 180, cerchi decorativi sparsi.
- **Dettagli da studio**: la foto d'apertura senza niente dentro, la voce "Beratung im Schadenfall" nel menu, la numerazione 01-03. Cosa non c'è: cifre, nomi.
- **Prove**: "seit 1960", "einer der ersten Carrosseriebetriebe im Kanton Uri", partner delle assicurazioni, una recensione.
- **Contatto**: un bottone in apertura, telefono e indirizzo in fondo, modulo con una somma da risolvere.
- **Si trasferisce**: la cabina di verniciatura a tutta larghezza come foto d'apertura (Serenissima ne ha nove) e la voce di menu "Che cosa fare dopo un incidente".
- **Non si trasferisce**: il serif da manifesto, i colori pastello, i cerchi, le tre schede con icona.

### Hesse Fördertechnik
- **Indirizzo**: https://www.hesse-foerdertechnik.de/ (Steinförder Str. 46, Wietze; titolare Hinrich Hesse).
- **Cosa fa**: riparazione, manutenzione, controlli di sicurezza (UVV), rigenerazione delle batterie e formazione dei carrellisti, per carrelli di ogni marca. Fa anche noleggio e vendita di usato.
- **Prima schermata**:
  - nessuna foto (0%);
  - menu centrato in alto, di cinque voci; nella schermata il logo non si vede;
  - titolo centrato su due righe, blu scuro: "Ihr zuverlässiger Gabelstaplerservice in Celle und Umgebung";
  - in corsivo grassetto "Markenunabhängig. Persönlich. Vor Ort.", un paragrafo, poi il motto "Reparieren statt Ersetzen.";
  - due bottoni: "Service anfragen" pieno e il telefono 05146 92364 a contorno;
  - otto elementi.
- **Struttura**:
  1. apertura;
  2. sei schede (Reparatur, Wartung, Prüfungen, Schulung, Vermietung, Verkauf), con le immagini che nella schermata restano riquadri lavanda vuoti;
  3. fascia blu: "Reparieren statt Ersetzen", "Aus Wietze bei Ihnen im Einsatz", "Sie brauchen Unterstützung?";
  4. richiesta in 9 passi, il primo "Worum geht es bei Ihrer Anfrage?" con cinque risposte;
  5. piede con titolare, indirizzo, telefono, email.
- **Fotografia**: nessuna foto visibile.
- **Tipografia**: Montserrat ovunque, titolo 48/62 peso 400, schede 24/31, testo 18/29; a 390 il titolo è 36/47.
- **Colori**: bianco, blu oltremare (#00008b circa), lavanda.
- **Griglia e margini**: colonna centrata di circa 1000 px.
- **Dettagli da studio**: il motto che torna, il modulo a passi che chiede "Standort, Hersteller und das Modell Ihres Staplers" e "ein Foto des Typenschilds". Cosa non c'è: foto, cifre, nomi oltre al titolare.
- **Prove**: dal 1996, famiglia, officina propria, servizio mobile.
- **Contatto**: telefono in apertura, modulo guidato, WhatsApp, email.
- **Si trasferisce**:
  - le tre parole del patto sotto il titolo (per Unicar: "Ogni marca. Di persona. In azienda.", solo se l'azienda lo sottoscrive);
  - un motto che torna (Unicar ha già "Consulenti, più che riparatori");
  - la foto della targhetta chiesta subito nel modulo del guasto, non solo nei ricambi.
- **Non si trasferisce**: la pagina senza foto e i riquadri vuoti, che sembrano un lavoro non finito.

### Willenbrock
- **Indirizzo**: https://www.willenbrock.de/de/.
- **Cosa fa**: concessionario Linde Material Handling: vendita, noleggio, usato, assistenza, negozio online, academy.
- **Prima schermata**:
  - doppio logo, Linde e Willenbrock;
  - barra rossa "Kontakt" e voci di servizio;
  - quattro voci di menu;
  - un carosello con un'immagine in 3D di carrelli automatici (28%) e "Automation Experience 2026";
  - cinque linguette del carosello;
  - quattro riquadri grigi con icona (Gabelstapler mieten, Gabelstapler kaufen, Ansprechpartner finden, Arbeitsplatz finden);
  - circa 15 elementi.
- **Struttura**: carosello, quattro riquadri, "Intralogistiklösungen für Lager und Betrieb" (Magazin, Shop, Newsletter), tre schede di valori (Produktivität, Sicherheit, Ergonomie), tre schede con foto (Gebrauchtstapler, Kurzzeitmiete, Wartung und Reparatur), comunicati stampa Linde, piede.
- **Fotografia**: immagini 3D e foto di repertorio del costruttore. L'officina non si vede.
- **Tipografia**: Dax (carattere di Linde) 48/60 per i titoli, Daxline 17/30 per il testo.
- **Colori**: rosso Linde, grigio chiaro, bianco.
- **Griglia e margini**: contenitore di circa 1200 px.
- **Dettagli da studio**: nessuno proprio. Il marchio del concessionario sparisce dietro a quello del costruttore.
- **Prove**: quelle di Linde.
- **Contatto**: "Ansprechpartner finden", cioè trovare il proprio referente; chat.
- **Si trasferisce**: un ingresso "Trova il tuo tecnico o il tuo referente" per zona, se Unicar divide i tecnici per zona.
- **Non si trasferisce**: tutto il resto. È l'esempio di che cosa evitare per Unicar, che deve restare l'officina con le sue persone e non diventare una pagina Toyota o Cami2.

### Habegger
- **Indirizzo**: https://www.habegger.ch/de/.
- **Cosa fa**: tecnica per eventi, allestimenti, spazi espositivi, gestione di sedi, produzione video; fornitore svizzero della "Live-Kommunikation".
- **Prima schermata**:
  - foto a tutta pagina (100%): un tecnico di spalle, con la scritta HABEGGER sulla maglia, davanti a un anello di luci viola;
  - logo piccolo in alto a sinistra, solo ricerca e menu a destra;
  - un riquadro scuro con "Cultivating WOW." e una riga;
  - sotto, cinque riquadri con foto e nome (Veranstaltung, Ausstellung, Erlebnisraum, Venue, Filmproduktion);
  - otto elementi.
- **Struttura**:
  1. apertura;
  2. "Spotlight", sei novità;
  3. "Referenzen", sei progetti con il nome del cliente;
  4. "Behind the Scenes", tre storie;
  5. "5 Steps zum Wow-Erlebnis";
  6. "Unsere Leistungen" con un diagramma a linea colorata (Creation, Project Management, Event Technology, Constructions, Venue Services, Interactive Solutions, Security);
  7. Academy (whitepaper);
  8. premi ("Ohne Fleiss kein Preis", sei loghi);
  9. "So erreichst du uns" con email, telefono +41 43 388 78 78 e sedi; piede.
- **Fotografia**: foto vere dei loro eventi e dei magazzini, molto contrastate e colorate, quasi tutte di sera. Il tecnico con la maglia del marchio torna più volte. Circa 30 foto.
- **Tipografia**: DIN, titolo 60/66 peso 700, riquadri 23/29, testo 18/25. Sotto ogni titolo di sezione c'è un filetto corto dorato. A 390 il titolo è 40/44.
- **Colori**: antracite (#2d2e2f) per le fasce, bianco, oro come accento.
- **Griglia e margini**: margini di circa 150, griglia a tre colonne.
- **Dettagli da studio**:
  - il filetto dorato fisso sotto i titoli;
  - le referenze sempre con il nome del cliente e dell'evento;
  - il dietro le quinte.
  - Difetti: il motto in inglese "Cultivating WOW", le icone dei cinque passi.
- **Prove**: clienti con il nome (Julius Bär, Hecht), premi, sedi.
- **Contatto**: in fondo, email e telefono; menu "Kontakt".
- **Si trasferisce**:
  - le sale e gli eventi con il nome del committente e del luogo (Eurotecnica: sale consiliari, chiese, università, se l'azienda dà i nomi e il permesso);
  - il tecnico al lavoro come foto d'apertura, quando ci sarà il servizio fotografico;
  - il filetto fisso sotto i titoli come segno di sistema.
- **Non si trasferisce**: il fondo antracite su tutta la pagina (per una ditta di quattro persone diventa scenografia), i motti in inglese, il diagramma colorato.

### Kraftwerk Living Technologies
- **Indirizzo**: https://www.kraftwerk.at/ (Maria-Theresia-Strasse 49, Wels).
- **Cosa fa**: integrazione di sistemi audio e video professionali, prodotti di visualizzazione, attrazioni multimediali, con sedi in Austria, Cina, Emirati, Arabia Saudita e Sudafrica.
- **Prima schermata**:
  - testata nera con il logo e il motto "Transforming ideas, exceeding limits";
  - video a tutta pagina (100%, nella schermata grigio);
  - riga rossa maiuscola piccola e titolo bianco in Rubik 36/41: "Where creative media technology solutions come to life and immersive experiences are redefined!";
  - una freccia; quattro elementi.
- **Struttura**: video, elenco delle sedi ("KLT Global") con ragione sociale, indirizzo, telefono ed email ciascuna, piede. Fine (2836 px).
- **Fotografia**: solo il video.
- **Tipografia**: Rubik 36/500 e 14/300.
- **Colori**: nero, rosso, bianco.
- **Griglia e margini**: margini di circa 45, molto stretti.
- **Dettagli da studio**: nessuno, a parte l'elenco ordinato delle sedi.
- **Prove**: le sedi nel mondo.
- **Contatto**: un blocco per sede, tutti uguali.
- **Si trasferisce**: il blocco di contatto uguale per ogni sede o reparto (Eurotecnica: impianti, service e negozio).
- **Non si trasferisce**: la home affidata a un video. Se il video non parte (come qui), non resta niente.

### Eberhard
- **Indirizzo**: https://eberhard.ch/ (Steinackerstrasse 56, Kloten).
- **Cosa fa**: impresa di famiglia alla terza generazione, da oltre 70 anni. Scavi, demolizioni, bonifiche, materiali da costruzione riciclati, "Saugtechnik und Gleisbausupport".
- **Prima schermata**:
  - video a tutta pagina (100%, nella schermata scuro);
  - in alto il logo giallo e blu in un riquadro;
  - a destra "Notfalldienste", "Enkelfähigkeit", "Kontakt", "Suche" e il bottone giallo "Menü";
  - in basso a sinistra il titolo "Pionierleistungen in Bau und Umwelt" su due righe e tre bottoni petrolio a pillola (Leistungen, Referenzen, Karriere);
  - otto elementi.
- **Struttura**:
  1. apertura;
  2. "Mit Pioniergeist für eine enkelfähige Zukunft" con un diagramma circolare;
  3. notizie in fila con foto (la tv locale, il grande escavatore, la mascotte all'aeroporto);
  4. "Leistungen", sei riquadri con icona;
  5. "Referenzen", quattro foto grandi con nome del cantiere e luogo;
  6. quattro riquadri (collaboratori, società, area clienti, impegno);
  7. un bambino con il casco giallo, "Enkelfähig seit Generationen";
  8. gli apprendisti in divisa sul grader giallo;
  9. "Engagiert wie Eberhard", tre progetti;
  10. piede giallo con le società del gruppo.
- **Fotografia**: foto vere dei cantieri e dei mezzi con la livrea gialla, persone con la maglietta del marchio, luce di giorno. Circa 15 foto.
- **Tipografia**: Figtree, titolo 52/63 peso 700, sezioni 32/42, testo 23/33 (grande, si legge bene); a 390 il titolo è 34/44.
- **Colori**: giallo Eberhard, petrolio, bianco, grigio chiaro.
- **Griglia e margini**: contenitore stretto, di circa 950 px (margini circa 245).
- **Dettagli da studio**:
  - "Notfalldienste" come prima voce della testata;
  - le referenze con l'indirizzo preciso;
  - le persone vere con la livrea.
  - Difetti: la parola d'ordine "enkelfähig" ripetuta, i riquadri con icona.
- **Prove**: tre generazioni, 70 anni, cantieri con il nome, società del gruppo.
- **Contatto**: emergenze in testata, "Kontakt", telefono nel piede.
- **Si trasferisce**:
  - i lavori con foto, nome e via (Zuin: ex Foro Boario, Prato della Valle, sede dell'Azienda del Gas, con le foto se ci sono);
  - la voce di pronto intervento per lo spurgo, se Zuin lo fa;
  - i mezzi con la livrea come foto principale.
- **Non si trasferisce**: il video d'apertura (non ci sono riprese) e lo slogan ecologico.

### Brandenburg
- **Indirizzo**: https://www.brandenburg.com/ (Elmhurst, Illinois).
- **Cosa fa**: demolizioni, anche di centrali elettriche e nucleari, bonifiche, amianto, recupero dei materiali, preparazione dei siti, emergenze. Dal 1968, con sette sedi regionali.
- **Prima schermata**:
  - testata bianca con il logo verde e sette voci;
  - carosello di filmati, uno per lavoro (100%);
  - titolo maiuscolo Rubik 64/64 peso 700 con il nome del lavoro, "Demolition of the Johnsonville Fossil", e il bottone play rotondo verde;
  - quattro elementi.
- **Struttura**:
  1. carosello dei lavori ("Rex Brown Steam Electric Station Demolition");
  2. Mission statement, Vision statement, About, in testo grigio chiaro centrato;
  3. "Safety First" con la foto della squadra in giubbotto e il programma OSHA VPP;
  4. fascia verde "Full service turnkey contractor";
  5. "Services offered", dieci riquadri con foto e nome;
  6. piede con le sette sedi, ognuna con indirizzo e telefono.
- **Fotografia**: foto vere di demolizioni e di squadre, di qualità mista, quadrate nei servizi.
- **Tipografia**: Rubik, titoli 64 maiuscoli con spaziatura 2, sezioni 30/45, testo 16/29 peso 300 grigio chiaro (contrasto basso).
- **Colori**: verde Brandenburg, bianco, grigio.
- **Griglia e margini**: testo centrato in una colonna di circa 700 px.
- **Dettagli da studio**: il lavoro con il nome proprio al posto dello slogan. Cosa non c'è: lavori con l'anno.
- **Prove**: ISO 9001 e 14001, OSHA VPP Star, flotta "in excess of $150,000,000", oltre 200 progetti l'anno.
- **Contatto**: sette sedi con il telefono, numero verde.
- **Si trasferisce**: aprire con un lavoro con il nome ("Demolizione dell'ex Foro Boario, 1968-69"), se c'è la foto; le dieci tessere quadrate dei servizi tutte con foto.
- **Non si trasferisce**: mission e vision, il testo grigio chiaro, il carosello.

### Alpine Painting & Sandblasting
- **Indirizzo**: https://www.alpinepainting.com/ (17 Florida Ave, Paterson, New Jersey).
- **Cosa fa**: verniciatura e sabbiatura industriale e commerciale, pavimenti in resina, saldatura; reparto chiuso per sabbiare e verniciare in sede mezzi pesanti e grandi pezzi.
- **Prima schermata**:
  - testata scura con il logo, telefono (866) 596-0349 e due bottoni rossi ("Now hiring", "Request estimate"), nove voci;
  - carosello di foto vere a tutta larghezza (100%), con titolo centrato in Oswald 70 maiuscolo ("Industrial Painting") e un bottone blu;
  - sotto, sei tessere con foto (Commercial, Flooring, Industrial, Shop services, Welding) e una tessera "Get an estimate" con foto, nome e interno del preventivista;
  - circa 15 elementi.
- **Struttura**:
  1. carosello e tessere;
  2. notizie, recensioni e chi siamo in tre colonne colorate;
  3. video;
  4. portfolio;
  5. squadra, cinque ritratti tondi con nome e ruolo;
  6. caso con il cliente nominato;
  7. associazioni (NACE, AMPP, ABC) e premi per la sicurezza;
  8. modulo di preventivo lungo, con il caricamento delle foto;
  9. mappa della zona servita; piede.
- **Fotografia**: foto vere di cantiere e di reparto, di qualità mista; ritratti in posa.
- **Tipografia**: tre famiglie, Oswald 70/70 maiuscolo, Montserrat per i menu, Lato 14/20 per il testo (troppo piccolo).
- **Colori**: rosso, blu, grigio scuro.
- **Griglia e margini**: contenitore di circa 1200 px.
- **Dettagli da studio**: il preventivista con la faccia e l'interno in prima schermata; il caso con cliente e luogo. Difetti: tre caratteri, colori a blocchi, caroselli.
- **Prove**: dal 1975, cliente nominato, associazioni di settore, premi per la sicurezza.
- **Contatto**: telefono in testata (6 link `tel:`), il nome di chi fa i preventivi, il modulo con le foto.
- **Si trasferisce**: il nome e la faccia di chi risponde ai preventivi (Nord: Leonardo o Stefano Barbieri) e un lavoro raccontato come caso (macchina, problema, passi, consegna). Nord ha già "Un apripista CAT D8R in tre passi", che è a metà strada.
- **Non si trasferisce**: il cliente con il nome se l'azienda non lo autorizza (per Nord, Tabarelli non va scritto), i caroselli, i blocchi colorati.

### Cleveland Brothers (pagina Paint & Blasting)
- **Indirizzo**: https://www.clevelandbrothers.com/services/paint-blasting (Harrisburg, Pennsylvania).
- **Cosa fa**: concessionario Caterpillar. In questa pagina: sabbiatura e verniciatura di macchine movimento terra di ogni marca, cassoni, rimorchi e motori, con i colori e le scritte del cliente.
- **Prima schermata**:
  - testata nera con il logo, sette voci e la ricerca;
  - foto di una pala gommata Cat all'aperto sotto un cielo da temporale (59%);
  - filetto giallo corto, titolo "Paint & Blasting Services" in Roboto Condensed 56/70 maiuscolo, bianco e giallo, un bottone giallo;
  - sei elementi.
- **Struttura**:
  1. apertura;
  2. "High-Quality Heavy Equipment Painting Services", con le misure della cabina e la foto della pala dentro;
  3. "Comprehensive Painting & Blasting Services", tre capacità (sabbiatura, vernici di specifica militare, ambiente chiuso);
  4. "Our Process", cinque passi numerati, dalla pulizia al protettivo;
  5. "Rebrand or Refresh Your Equipment", colori e scritte su misura;
  6. piede.
- **Fotografia**: tre foto vere della cabina, vuota e con la macchina dentro, in luce fredda, tutte della stessa misura (4:3).
- **Tipografia**: Roboto Condensed 700, titoli 40/50, testo Arial 16/24.
- **Colori**: nero, giallo Cat, bianco.
- **Griglia e margini**: margini di circa 130, due colonne foto e testo alternate.
- **Dettagli da studio**: il filetto giallo sopra ogni titolo; le misure in piedi.
- **Prove**: "65' x 35' x 30'", "one of the largest in the area".
- **Contatto**: un bottone "Request More Information".
- **Si trasferisce**:
  - le misure della cabina e "che cosa ci entra" (Nord: da chiedere);
  - il processo in passi numerati con una foto per passo (Nord ce l'ha già con il D8R);
  - la fila di foto tutte nello stesso formato.
- **Non si trasferisce**: niente di particolare; è una pagina di servizio di un concessionario, non una home.

### Emch Aufzüge
- **Indirizzo**: https://www.emch.com/ (Fellerstrasse, Berna-Bümpliz).
- **Cosa fa**: costruisce in proprio ascensori su misura, di design e speciali, ammodernamenti, trasformazioni, servizio e allarme in cabina. È della stessa famiglia dal 1880.
- **Prima schermata**:
  - logo in un quadrato blu con "Swiss Made" a sinistra;
  - tre voci (Lift, Magazin, Unternehmen), ricerca e menu;
  - video d'atmosfera a tutta pagina (100%, nella schermata bianco);
  - riquadro blu in basso a sinistra: "Willkommen bei der Schweizer Manufaktur für Lift- und Hebetechnik.";
  - una chat "Stellen Sie Ihre Fragen an mich";
  - cinque elementi.
- **Struttura**:
  1. apertura;
  2. "Mehr als ein Lift." (testo);
  3. Neuanlagen, Designanlagen, Spezialanlagen;
  4. foto grande dell'ascensore verde in vetro nella scala a chiocciola;
  5. Modernisierung, con Liftmodernisierung e Liftumbau, ognuno con il suo elenco;
  6. Ersatzanlage, Lifteinbau in un edificio esistente, con le misure;
  7. foto dell'ascensore in vetro in una boutique;
  8. Individualanlage, con uno schizzo a matita;
  9. riquadro blu "Service" ("seit 1880", picchetto 24 ore, 365 giorni), Wartung, Reparatur, Lift-Notruf-System;
  10. altre foto, piede.
- **Fotografia**: foto d'architettura degli impianti montati, fatte da professionisti, con molta luce e prospettive centrate. Circa 10 foto e uno schizzo.
- **Tipografia**: Prelo peso 300, titoli 42/52, sottotitoli 22/33 peso 200; Roboto 18/30 peso 300 per il testo. Tutto leggero; a 390 il titolo è 21/26.
- **Colori**: bianco, blu Emch per i riquadri, grigio.
- **Griglia e margini**: margini di circa 160, molto bianco tra i blocchi, due colonne di testo.
- **Dettagli da studio**:
  - lo schizzo a matita come immagine del progetto;
  - pesi leggeri;
  - le misure tecniche dentro il testo ("bis 30m", "180 und 1600kg");
  - casi di ammodernamento separati.
  - Cosa non c'è: cifre aziendali messe in fila, numeri di telefono grandi.
- **Prove**: "seit 1880", "grösste unabhängige KMU in der Schweiz mit eigener Fertigung", impianti d'autore fotografati.
- **Contatto**: menu, chat, servizio 24 ore detto nel testo.
- **Si trasferisce**:
  - dividere l'ammodernamento in casi con i loro limiti (Belletti ha le schede tecniche e i PDF);
  - fotografare gli impianti come architettura (Belletti ha già Galleria Cavour, Ca' Michiel, Ca' della Nave);
  - lo schizzo o il disegno tecnico proprio, se esiste, accanto alla foto.
- **Non si trasferisce**: il testo leggero e piccolo (si legge male), la chat.

### Schmitt + Sohn Aufzüge
- **Indirizzo**: https://www.schmitt-aufzuege.de/ (Norimberga).
- **Cosa fa**: costruisce ascensori per persone, merci e letti, fa servizio e ammodernamento. Famiglia da sei generazioni, dal 1861, con stabilimenti in Germania e Portogallo.
- **Prima schermata**:
  - barra nera in alto: "Service24: (0800) 24-00-365", area clienti, lingue;
  - testata bianca con il marchio S+ e sette voci;
  - foto a tutta larghezza di un tecnico nel vano che guarda in su, in luce blu (77%);
  - fascia nera con una notizia in Open Sans 44/48 peso 300 (il carosello);
  - sotto, tre voci (Aufzüge, Service, Karriere);
  - sei elementi.
- **Struttura**:
  1. carosello;
  2. tre riquadri con foto (Aufzüge, Service, Karriere);
  3. il marchio grande, "Aktualisiertes Markensignet";
  4. una frase a 26 px: "Als Familienunternehmen begeistern wir seit 6 Generationen";
  5. elenco dei fatti: impianti certificati, "über 160 Jahren", paesi, stabilimenti ISO 9001; video;
  6. "Finden Sie Ihr Produkt": la prima domanda è il tipo di edificio;
  7. progetti scelti;
  8. vita dell'azienda (giubilari, apprendisti, corsa aziendale);
  9. piede.
- **Fotografia**: servizio vero sui tecnici e sui giovani, con il marchio sul casco; foto di prodotto in studio.
- **Tipografia**: Open Sans peso 300 ovunque, 44/48 i titoli, 16/24 il testo.
- **Colori**: nero, bianco, grigio, una riga blu.
- **Griglia e margini**: margini di circa 210, contenitore di circa 1000 px.
- **Dettagli da studio**:
  - il numero del servizio nella barra in alto, sempre;
  - la domanda "per quale edificio?";
  - il marchio grande da solo, su bianco.
  - Difetti: il carosello d'apertura con le notizie.
- **Prove**: sei generazioni, 160 anni, ISO 9001, paesi.
- **Contatto**: numero 24 ore fisso in alto, referenti per zona, area clienti.
- **Si trasferisce**:
  - la scelta per tipo di edificio (Belletti: condominio, casa, negozio e ufficio, struttura sanitaria, industria) al posto o accanto alla scelta per prodotto;
  - il numero dei guasti in una barra sottile sempre visibile (Belletti ce l'ha già come bottone).
- **Non si trasferisce**: il carosello di notizie in apertura, il peso 300 ovunque.

### KÖGEL Schornsteine
- **Indirizzo**: https://koegel-schornsteine.de/ (Backnang).
- **Cosa fa**: dal 1918, terza generazione: progetta, costruisce, monta, risana, demolisce e smaltisce camini, anche industriali in acciaio. Vende stufe e caminetti nello showroom "KÖGEL Feuerland".
- **Prima schermata**:
  - testata grigio scuro con il logo arancio, ricerca e menu;
  - foto calda di una donna davanti al fuoco (67%, sembra repertorio);
  - al centro "Bitte wählen Sie einen Geschäftsbereich" e due bottoni (Privatkunden, Geschäftskunden);
  - fascia arancio "Willkommen im KÖGEL Feuerland" e bottone "Kontakt";
  - cinque elementi.
- **Struttura**:
  1. apertura;
  2. "Über 100 Jahre Perfektion" (testo);
  3. quattro riquadri con icona (Erfahrung, Qualität, Design, Innovation);
  4. foto larga di un fascio di camini industriali in inox, "Nichts ist zu kompliziert." e "Schreiben Sie uns!";
  5. loghi dei produttori (Spartherm, Kalfire, Brunner);
  6. piede con il telefono.
- **Fotografia**: la donna al fuoco (atmosfera) e i camini industriali (lavoro vero). Due foto.
- **Tipografia**: Roboto, titoli 32/42 peso 300 e 500, testo 15/24.
- **Colori**: arancio KÖGEL, grigio scuro, bianco.
- **Griglia e margini**: contenitore di circa 1200 px.
- **Dettagli da studio**: la scelta privato o impresa come prima cosa; la frase "Nichts ist zu kompliziert". Difetti: quattro valori con icona (Qualità, Design, Innovazione) e parole d'ordine.
- **Prove**: dal 1918, produttori rappresentati.
- **Contatto**: "Kontakt" in apertura, telefono nel piede.
- **Si trasferisce**:
  - la prima scelta tra casa e condominio o impresa (La Termica vende "al dettaglio e all'ingrosso" e lavora per l'industria);
  - la foto dei camini autoportanti in inox contro il cielo come immagine forte (La Termica ne ha circa 320 nelle gallerie).
- **Non si trasferisce**: la foto d'atmosfera al caminetto, i quattro valori con icona.

### Jeremias
- **Indirizzo**: https://jeremias.de/.
- **Cosa fa**: costruisce sistemi di scarico fumi e camini in acciaio inox, a parete singola e doppia, industriali e per la casa. Lavora con le metalliche.
- **Prima schermata**:
  - testata su due righe: logo, ricerca, "My Jeremias", lingue; menu (Produkte, Einsatzbereiche, Metallverarbeitung, Downloads, Service, Kontakt);
  - immagine in 3D di una villa con il camino e di uno stabilimento (73%), con due etichette cliccabili ("Lösungen für die Industrie", "Elementschornsteine");
  - barra di icone a destra;
  - sotto, "Jeremias in Zahlen";
  - circa 14 elementi.
- **Struttura**:
  1. immagine con etichette;
  2. quattro cifre con icona disegnata (sedi produttive, referenze, collaboratori, paesi). I numeri si contano da soli e cambiano mentre si guarda: alla prima visita ho letto 10+ e 100000+, alla seconda 8+ e 73570+;
  3. notizie a linguette (listino interattivo, un progetto per un panificio industriale, un'acquisizione, il calcolo dell'altezza secondo VDI e BImSchV);
  4. il listino interattivo;
  5. quattro riquadri (Schornsteinsuche, Downloads, Jobs & Karriere, Newsletter);
  6. piede blu.
- **Fotografia**: immagini in 3D e foto di prodotto.
- **Tipografia**: Gotham, titolo 44 maiuscolo peso Light, testo Gotham Book 15/20.
- **Colori**: blu Jeremias, bianco.
- **Griglia e margini**: margini di circa 30, quasi al bordo.
- **Dettagli da studio**: gli strumenti tecnici in home (ricerca del camino, listino, calcolo dell'altezza). Difetti: il 3D, le cifre che contano, le icone disegnate.
- **Prove**: cifre, norme citate.
- **Contatto**: telefono ed email nel piede.
- **Si trasferisce**: il servizio tecnico detto con il nome della norma (La Termica: dimensionamento e messa a norma, solo se lo fanno e con la norma giusta), e i cataloghi in un posto solo (La Termica ha 17 PDF).
- **Non si trasferisce**: il 3D al posto della foto (divieto del committente), i contatori animati.

### Jacksons Fencing
- **Indirizzo**: https://www.jacksons-fencing.co.uk/ (Ashford, Kent).
- **Cosa fa**: dal 1947, famiglia alla terza generazione. Produce recinzioni in legno trattato e in acciaio, cancelli, automazioni, barriere acustiche; vende online e attraverso una rete di posatori approvati.
- **Prima schermata**:
  - barra in alto con gli strumenti (Fence calculator, Decking calculator, Gate calculator, Free quote, Quick order, Request a brochure) e "Our other sites: Commercial & High security";
  - testata con il telefono 0800 408 2234 a sinistra, il logo al centro, account, carrello e ricerca; nove voci;
  - foto a tutta larghezza di una recinzione a doghe orizzontali accanto a una piscina, con una donna e un bambino (80%);
  - titolo centrato maiuscolo, Frutiger Light Condensed 68/68; "Premium fencing with a 25 year guarantee." in Lora corsivo;
  - tre bollini (Made in Britain, 25 years, Trustpilot Excellent) e due bottoni;
  - in più, al primo accesso, una finestra che chiede chi sei (casa e giardino, commerciale, alta sicurezza) e porta ai due siti;
  - circa 20 elementi.
- **Struttura**:
  1. apertura;
  2. otto tessere con foto di prodotto;
  3. blog "The Edit" e "Request a Brochure" ("The Good Fencing Guide", gratis per posta);
  4. rimando al sito di sicurezza e alla garanzia di 25 anni;
  5. promozioni di stagione ("Get autumn ready", pannelli antieffrazione certificati LPS 1673);
  6. recensioni;
  7. caroselli di prodotto;
  8. strumenti per progettare (Fence builder, Decking builder, Gate builder);
  9. articoli con i lavori nominati (Martello Tower No 25, Dymchurch; un glamping nel Somerset);
  10. posa e consigli; acquisti; piede.
- **Fotografia**: servizio vero di prodotto montato in giardini veri, luce di giorno inglese; l'apertura è da catalogo. Circa 40 foto.
- **Tipografia**: Frutiger Condensed (Light per il titolo, Bold 26/34 maiuscolo per le sezioni), Lora 18/29 per il testo; a 390 il titolo è 28/28.
- **Colori**: blu notte, bordeaux, verde petrolio, il legno delle foto.
- **Griglia e margini**: contenitore di circa 1000 px centrato.
- **Dettagli da studio**:
  - la garanzia nel sottotitolo;
  - la guida stampata per posta;
  - i calcolatori;
  - le due strade (casa e impresa) con due siti.
  - Difetti: troppe fasce promozionali, popup al primo accesso.
- **Prove**: 25 anni di garanzia, Trustpilot "Excellent", Made in Britain, certificazioni antieffrazione, lavori nominati.
- **Contatto**: numero verde in testata, chat, preventivo gratuito.
- **Si trasferisce**:
  - la garanzia in cifre accanto al titolo (Formentin: solo se l'azienda la dà);
  - il catalogo cartaceo o PDF da chiedere;
  - un "calcolo" semplice (metri, altezza, cancello) che prepara il preventivo (Formentin chiede già foto e misure);
  - i lavori con il nome del luogo.
- **Non si trasferisce**: il negozio online, i popup, le promozioni di stagione.

### Gust. Alberts
- **Indirizzo**: https://www.alberts.de/ (Herscheid; nel piede "© 1852-2026").
- **Cosa fa**: produce recinzioni e cancelli (Zauntechnik), ferramenta, profili e lamiere, sistemi di sbarramento; vende ai rivenditori e ai privati.
- **Prima schermata**:
  - testata bianca con il logo verde, la ricerca "Produkt finden", sette voci e "Händler-Login";
  - quattro foto verticali affiancate, a tutta altezza (visivamente il 100%): quattro persone in camicia a quadri al lavoro, ognuna con un titolo grande maiuscolo condensato ("Alles aus Eisen", "Aus Liebe zum Zaun", "Profis für Profile", "Noch viel mehr");
  - fascia verde "Hier geht's zu unserem Imagefilm";
  - sei elementi.
- **Struttura**:
  1. apertura;
  2. tre prodotti in evidenza con foto, una con l'etichetta "AI" nell'angolo;
  3. "Made in Herscheid" con un saldatore tra le scintille, e la fascia verde "Gemacht, um zu halten.";
  4. magazine (gli apprendisti diplomati);
  5. "7.000+ Produkte" con la ricerca;
  6. piede scuro.
- **Fotografia**: un servizio di campagna, con modelli o dipendenti in posa, luce calda e drammatica, tono uniforme. Una delle foto è segnata come generata con l'intelligenza artificiale.
- **Tipografia**: Veneer Clean Soft (condensato con bordo ruvido) 60/54 maiuscolo per i titoli, Muller 16/26 per il testo; a 390 il titolo è 40/36.
- **Colori**: verde Alberts, antracite, bianco.
- **Griglia e margini**: foto al bordo, testo con margini di circa 110.
- **Dettagli da studio**:
  - le quattro colonne con quattro frasi;
  - "Made in Herscheid";
  - una frase sola come firma.
  - Difetti: le foto da campagna, troppo costruite; l'immagine generata.
- **Prove**: dal 1852, 7.000 prodotti, produzione propria.
- **Contatto**: nel menu e nel piede; "Händler-Login".
- **Si trasferisce**:
  - dire dove si produce ("fatte a Villatora", per le reti ondulate e le colonne che Formentin produce);
  - una frase-firma vera dell'azienda;
  - la foto di chi salda o piega in officina, quando ci sarà il servizio fotografico.
- **Non si trasferisce**: i modelli in posa, le immagini generate (sono illustrazioni al posto delle foto, divieto del committente).

### HANSA-FLEX
- **Indirizzo**: https://www.hansa-flex.de/ (Brema).
- **Cosa fa**: tubi idraulici e raccordi, gestione dei tubi con un codice (X-CODE), servizio fluidi, servizio mobile d'emergenza 24 ore su 24, montaggio, accademia. Di famiglia, "64 Jahre Systempartner".
- **Prima schermata**:
  - barra in alto (paese, lingua, ricerca delle filiali, aiuto e contatti, X-CODE Manager), sei voci, ricerca;
  - carosello a tutta larghezza (75%): un tecnico sorridente con il tablet davanti al furgone rosso; nel secondo slide il disegno al tratto dei raccordi;
  - titolo Outfit 55/72 maiuscolo ("Hansa-Flex steht für Hydraulik", "Hydraulikbedarf online bestellen!") e un bottone rosso;
  - sei elementi.
- **Struttura**:
  1. carosello;
  2. "Unsere Services", sei schede con foto (Schlauchmanagement, Fluidservice, Mobiler Hydraulik-Sofortservice "24/7 an 365 Tagen", Hydraulik Akademie, Referenzen);
  3. "Heute bestellt, morgen geliefert" con un video;
  4. "Ihre Vorteile", quattro punti con la spunta;
  5. notizie (anniversari, nomine, sport);
  6. piede con due numeri: centralino 0421 48 90 70 e servizio d'emergenza +49 800 77 12345.
- **Fotografia**: servizio vero sui tecnici con la divisa e i furgoni rossi; disegni tecnici dei raccordi nel secondo slide.
- **Tipografia**: Outfit maiuscolo per i titoli (55 e 35), Roboto 18/31 peso 300 per il testo.
- **Colori**: rosso HANSA-FLEX, blu scuro per i titoli di sezione, grigio chiaro.
- **Griglia e margini**: margini di circa 80, schede a tre colonne.
- **Dettagli da studio**: il codice per rifare lo stesso tubo, il disegno al tratto dei raccordi, il numero d'emergenza separato.
- **Prove**: 64 anni, servizio 24/7, accademia, consegna il giorno dopo.
- **Contatto**: barra con le filiali, due numeri distinti nel piede, negozio online.
- **Si trasferisce**:
  - "che cosa ti resta dopo": un'etichetta o un numero per rifare lo stesso tubo (Framo: solo se lo fanno);
  - il disegno al tratto dei raccordi come immagine, se Framo ha i disegni dei suoi fornitori;
  - due numeri distinti se esiste un servizio fuori orario.
- **Non si trasferisce**: il carosello, le notizie aziendali, il negozio.

### Pirtek UK
- **Indirizzo**: https://www.pirtek.co.uk/.
- **Cosa fa**: sostituzione dei tubi idraulici sul posto (in genere entro un'ora), manutenzione programmata, gestione dei tubi, banco di vendita, progetti su misura, corsi. Rete di 86 centri.
- **Prima schermata**:
  - testata bianca: logo in un blocco blu notte, quattro voci, due bottoni con icona (centro più vicino, telefono) e il giallo "Book a Callout";
  - foto a tutta larghezza di un tecnico con il casco Pirtek e un tubo sulla spalla (76%), con sopra una griglia di linee sottili come carta millimetrata;
  - riquadro bianco con il titolo in Px Grotesk 50/67 peso 400 ("A nationwide force of hydraulic hose experts"), una riga e un bottone giallo;
  - in basso a sinistra una didascalia: "Location 51° 31' 39.756" N, 0° 16' 2.928" W";
  - sette elementi.
- **Struttura**:
  1. apertura;
  2. "Under the hard hat / In it together", benessere dei tecnici;
  3. "Our services", dodici voci con icona in due colonne;
  4. una testimonianza con nome, luogo e coordinate (Martin Hood, Marwell Zoological Park);
  5. "Why Pirtek?" (86 centri, sul posto entro un'ora);
  6. area clienti;
  7. catalogo, con la foto da vicino della guaina blu e della sua scritta stampata;
  8. notizie;
  9. accreditamenti e piede.
- **Fotografia**: servizio vero di tecnici, sempre con il casco e il giubbotto del marchio, luce di giorno; la foto macro della guaina come immagine di prodotto.
- **Tipografia**: una sola famiglia, Px Grotesk: 50/67 peso 400 in apertura, 34/46 nelle sezioni, 18/30 nel testo; a 390 il titolo è 32/40.
- **Colori**: blu notte, giallo, bianco, la griglia azzurra chiara.
- **Griglia e margini**: margini di circa 80, la griglia di fondo continua in tutta la pagina.
- **Dettagli da studio**:
  - la carta millimetrata come segno del marchio;
  - le coordinate come didascalia (foto vere, con il luogo);
  - la scritta tecnica della guaina usata come immagine;
  - un carattere solo, un peso quasi solo.
- **Prove**: 86 centri, accreditamenti, testimonianze con nome e luogo.
- **Contatto**: "Book a Callout" sempre in testata, centro più vicino, telefono.
- **Si trasferisce**:
  - la foto da vicino della guaina con la sua scritta (Framo la chiede già al cliente: va fatta anche per sé, con il telefono e una buona luce);
  - la didascalia con il luogo o le coordinate sotto le foto vere;
  - un carattere solo con pochi pesi;
  - un segno di fondo legato al mestiere (per Framo, il filetto delle misure in pollici).
- **Non si trasferisce**: la rete di centri, l'area clienti, le dodici icone di servizio.

### Restore Construction
- **Indirizzo**: https://restoreconstruction.com/ (Melrose Park, Illinois).
- **Cosa fa**: ripristino dopo acqua, fuoco, fumo, tempesta e muffa; messa in sicurezza, ricostruzione, gestione della pratica con l'assicurazione. "Still managed by the same family", da oltre 40 anni.
- **Prima schermata**:
  - barra bordeaux in alto: "24/7 Emergency Restoration Services" e il bottone giallo "Call Now: (847) 613-1493";
  - testata bianca con il logo e cinque voci;
  - foto a tutta larghezza della squadra (circa dodici persone con la polo nera del marchio, davanti a un muro di mattoni), scurita (83%);
  - occhiello serif "Water & Fire Damage Restoration in Chicago, IL", titolo in Fraunces 55/60 su tre righe, filetto rosso sotto;
  - un paragrafo, quattro righe con la spunta (24/7 Emergency Response, Proven Chicago Heritage, Guaranteed Results, Insurance Claim Assistance), un bottone giallo;
  - circa 12 elementi.
- **Struttura**:
  1. apertura;
  2. loghi delle certificazioni (IICRC, RIA);
  3. "Tell Us About Your Disaster";
  4. nove servizi con foto;
  5. richiesta di servizio ("processed Mon-Fri 8am-5pm") e "Areas We Serve" con i comuni;
  6. lavori in evidenza (incendio a Oak Park);
  7. quattro promesse con icona;
  8. "Our Story": fondatore nato nella zona, la stessa famiglia, oltre 10.000 clienti, con la foto della squadra davanti al camion;
  9. una recensione con nome e città; piede.
- **Fotografia**: due foto vere della squadra (in apertura e nella storia) e foto di lavori di qualità mista, alcune di repertorio.
- **Tipografia**: Fraunces 600 per i titoli, Poppins 15/25 per il testo; a 390 il titolo è 25/35.
- **Colori**: bordeaux, giallo, nero, bianco.
- **Griglia e margini**: margini di circa 150.
- **Dettagli da studio**: la squadra come prima immagine, il filetto rosso sotto il titolo, gli orari di risposta del modulo. Difetti: spunte generiche, icone.
- **Prove**: 40 anni, la stessa famiglia, 10.000 clienti, certificazioni, comuni serviti.
- **Contatto**: numero in alto e ripetuto in ogni fascia (11 link `tel:`), modulo con gli orari di risposta.
- **Si trasferisce**:
  - la squadra in divisa davanti alla sede o al furgone come foto d'apertura (Oby: otto persone, da fotografare);
  - "gestiamo noi la pratica con l'assicurazione" come promessa principale (Oby lo dice già: "alle pratiche burocratiche pensiamo noi");
  - i comuni serviti in chiaro.
- **Non si trasferisce**: le spunte generiche, il serif da titolo, le foto di repertorio.

### BELFOR Svizzera
- **Indirizzo**: https://www.belfor.com/ch/de/.
- **Cosa fa**: risanamento dopo incendio, acqua e tempesta, per compagnie, amministrazioni, industria e privati. Filiale svizzera di un gruppo internazionale.
- **Prima schermata**:
  - barra sottile in alto (chi siamo, sedi, paese, lingua, ricerca), testata bianca con il logo e cinque voci, il blocco rosso "Kontakt";
  - video a tutta pagina (87%), scuro a sinistra;
  - occhiello rosso "We make it undone", titolo maiuscolo in Libre Franklin 72/79 peso 800 su quattro righe ("Nr. 1 in der Schadensanierung weltweit", con la parola spezzata male);
  - un paragrafo, due bottoni ("Ansprechperson finden" pieno, "Schadenmeldung" a contorno);
  - in basso a destra il blocco rosso fisso "24H/24H Hotline 0800 808 118";
  - otto elementi.
- **Struttura**:
  1. apertura;
  2. "Unser Versprechen: We make it undone." con un carosello per pubblico (Versicherer, Verwaltungen, Industrie, Privat);
  3. "24H/24H für Sie im Einsatz, weltweit", quattro cifre (4.100, 103.000, 168+, 19);
  4. la direzione svizzera, sette ritratti con nome e ruolo;
  5. foto di gruppo con le magliette rosse, "Tausende Kollegen machen uns zur Nr. 1";
  6. notizie;
  7. video con un collaboratore;
  8. chiusura "als wäre der Schaden nie geschehen"; piede.
- **Fotografia**: servizio vero sulla squadra e sui dirigenti (ritratti in studio, foto di gruppo in magazzino), con il rosso del marchio sempre presente.
- **Tipografia**: Libre Franklin, 72/79 peso 800 maiuscolo con spaziatura stretta, sezioni 51/57 peso 800, testo 22/31 peso 500; a 390 il titolo è 28/31.
- **Colori**: rosso BELFOR, nero, bianco.
- **Griglia e margini**: margini di circa 140.
- **Dettagli da studio**:
  - il numero d'emergenza fisso in ogni schermata;
  - il secondo bottone "segnala un danno";
  - le strade per tipo di cliente, con le compagnie per prime;
  - le facce di chi dirige.
  - Difetti: lo slogan in inglese e il "numero 1".
- **Prove**: cifre del gruppo, direzione con il nome, ISO 37001 nelle notizie.
- **Contatto**: numero d'emergenza fisso, "Kontakt" in testata, referente per zona, segnalazione del danno.
- **Si trasferisce**:
  - il numero d'emergenza fisso in basso a destra, anche a 1440 (Oby ha il cellulare in testata, che scorre via a 390 se la testata non è fissa);
  - "Segnala un danno" come seconda azione (Oby ha già "Manda le foto del danno");
  - i titolari e i responsabili con il nome e la faccia.
- **Non si trasferisce**: le cifre di gruppo, lo slogan, il video.

### Dalworth Restoration
- **Indirizzo**: https://www.dalworthrestoration.com/ (Euless, Texas).
- **Cosa fa**: ripristino dopo acqua, fuoco, tempesta e muffa, pulizia, ricostruzione. "Since 1976", nel gruppo Fleet Response.
- **Prima schermata**:
  - colonna di menu verticale a sinistra (150 px, 14 voci);
  - barra blu in alto: "DFW's Trusted Leader in Restoration and Clean-Up, Since 1976", telefono 817-203-2944 e "Request an Estimate";
  - fascia blu vuota (video) con "Water Damage Emergency?" e "Call Now!";
  - riquadro giallo e blu "Over 97,350+ Successful Restoration Projects Completed" con la foto della flotta di deumidificatori;
  - circa 25 elementi.
- **Struttura**: quattro servizi, otto tessere sull'acqua, il processo in sei passi (ispezione, categoria dell'acqua, aspirazione, asciugatura, pulizia, ripristino), fuoco e fumo, tempesta, muffa, servizi in più, "What Sets Us Apart", una bambina alla finestra (repertorio), domande frequenti, "Works Directly with Your Insurance Company" con otto loghi, partner, comuni serviti con la mappa, piede.
- **Fotografia**: mista, una parte vera (flotta, mezzi), una parte di repertorio.
- **Tipografia**: Roboto 700 per tutto, 36 e 30 per i titoli, 16/24 per il testo.
- **Colori**: blu, giallo, bianco.
- **Griglia e margini**: affollata, senza un passo chiaro.
- **Dettagli da studio**: nessuno. È un sito fatto per il motore di ricerca.
- **Prove**: dal 1976, 97.350 lavori, 4,9 su 200 recensioni, loghi delle compagnie.
- **Contatto**: telefono ovunque (8 link `tel:`).
- **Si trasferisce**: i nomi dei passi del processo (Oby ha già "In cantiere, nove passaggi"); l'elenco delle compagnie con cui si lavora direttamente, se i nomi si possono dire.
- **Non si trasferisce**: tutto il resto: repertorio, affollamento, menu laterale.

---

## 3. Le costanti del gruppo

Come si presenta un'azienda di alto livello di questo tipo, guardando i migliori (Pirtek, Eberhard, Auto Bayertz, Habegger, Emch, Schmitt + Sohn, BELFOR, Restore):

**Prima schermata**
- Una sola immagine grande, a tutta larghezza, dal 75 al 100% della prima schermata. Mostra la squadra o il tecnico con il marchio addosso (Pirtek, Habegger, Restore, HANSA-FLEX, Schmitt), il reparto vuoto (Geser), il mezzo al lavoro (Eberhard, Cleveland). Il titolo sta sopra la foto, in basso a sinistra o in un riquadro.
- Nessuno dei migliori apre con titolo a sinistra, foto a destra e due bottoni. Lo fa solo Willenbrock, il portale. Le nostre home lo fanno in otto casi su dieci.
- Il titolo dice il mestiere e il luogo ("Gabelstaplerservice in Celle und Umgebung", "Water & Fire Damage Restoration in Chicago, IL") oppure una promessa breve ("Pionierleistungen in Bau und Umwelt").
- Un'azione principale, al massimo due. Il numero d'emergenza sta fuori dalla foto: in una barra in alto (Schmitt, Restore), in testata (Eberhard) o fisso in basso (BELFOR).
- Da 4 a 8 elementi nei migliori; 15-25 negli affollati (Dalworth, Jacksons, Alpine, Willenbrock).

**Foto**
- Un servizio vero con le stesse persone, la stessa luce e la divisa con il marchio (Pirtek, BELFOR, Eberhard, HANSA-FLEX, Auto Bayertz).
- Le persone hanno un nome: Auto Bayertz (tre ritratti), Alpine (cinque), BELFOR (sette), Hesse (il titolare nel piede).
- La galleria del reparto è una serie sola, nello stesso formato (Auto Bayertz, 12 quadrate; Cleveland, 4:3).
- Il dettaglio tecnico fotografato da vicino diventa immagine di marca: la scritta della guaina (Pirtek), il disegno dei raccordi (HANSA-FLEX), lo schizzo a matita (Emch).
- Chi usa il repertorio o il 3D (Dalworth, Willenbrock, Jeremias, KÖGEL in apertura, la foto "AI" di Alberts) sembra subito un portale o un catalogo.

**Tipografia**
- Spesso una famiglia sola (Pirtek, Eberhard, Habegger, BELFOR, Hesse).
- Per i mestieri d'urgenza (carrozzeria, risanamento, verniciatura): grottesco condensato o nero, maiuscolo, pesi 700-900 (Auto Bayertz 72/900, BELFOR 72/800, Cleveland 56/700).
- Per la tecnica d'edificio (ascensori): leggero e grande (Emch 42/300, Schmitt 44/300). Funziona sulle foto d'architettura, meno sul testo.
- Testo da 18 a 23 px nei migliori (Eberhard 23/33, BELFOR 22/31, Auto Bayertz 20/32). Il difetto comune è il testo piccolo (Alpine 14, KÖGEL 15, Jeremias 15).

**Colori**
- Il colore del marchio è pieno e solo: giallo Eberhard, rosso BELFOR, rosso HANSA-FLEX, verde Alberts, giallo Pirtek. Accanto c'è il bianco, a volte un nero o un blu notte.

**Prove**
- L'anno con il nome del fondatore o la generazione: "1945, gegründet von Willy Bayertz"; "seit 1880"; "seit 6 Generationen"; "seit 1918".
- La garanzia in anni: 6 anni (Auto Bayertz), 25 anni (Jacksons).
- Le misure con l'unità: la cabina 65' x 35' x 30' (Cleveland), la corsa fino a 30 m e la portata da 180 a 1600 kg (Emch), 3.000 m² (Auto Bayertz).
- I lavori con il nome e il luogo (Eberhard, Habegger, Brandenburg, Alpine, Jacksons).
- I certificati come loghi o con la sigla (IICRC, NACE, OSHA VPP, ISO 9001 e 14001, LPS 1673).

**Contatto**
- Il numero d'emergenza è separato da quello d'ufficio e si vede sempre: Schmitt "Service24", BELFOR "24H/24H Hotline", HANSA-FLEX "Sofortservice", Eberhard "Notfalldienste".
- Il contatto si divide per chi scrive: privato o impresa (KÖGEL, Jacksons), compagnie, amministratori, industria, privati (BELFOR), tipo di edificio (Schmitt).
- La richiesta è guidata e chiede quello che serve al tecnico (Hesse: la marca, il modello e la foto della targhetta; Alpine: le foto del lavoro).
- La persona che risponde ha un nome (Alpine: il preventivista con l'interno; Hesse: il titolare).

**Lingua**
- Frasi brevi che tornano: "Reparieren statt Ersetzen", "Markenunabhängig. Persönlich. Vor Ort.", "Gemacht, um zu halten", "Nichts ist zu kompliziert".
- Le parole d'ordine ci sono anche qui ("Cultivating WOW", "enkelfähig", "Innovation", "Nr. 1 weltweit") e sono la parte peggiore di ogni sito.

---

## 4. Le 8 mosse che si trasferiscono alle nostre home di questo gruppo

### 1. Una foto vera sola, larga, con il titolo sopra
- **Cosa**: smettere di aprire con titolo a sinistra, foto a destra, due bottoni e la fila di ingressi sotto. Si prende la foto migliore dell'azienda e la si mette a tutta larghezza (dal 70 al 100% della prima schermata). Il titolo del mestiere va sopra, in basso a sinistra, con un velo scuro solo sotto le righe. Un bottone e il telefono in testata.
- **Esempi**:
  - Geser (la cabina vuota), Eberhard (il mezzo), Pirtek, Restore (la squadra).
  - Da noi: Serenissima (una delle 9 cabine o il carro attrezzi blu "Soccorso stradale"), Belletti (il furgone sotto la facciata di vetro al crepuscolo, che è già quasi così), La Termica (il furgone con la scritta), Fratelli Zuin (il camion con il braccio dell'escavatore), Nord Service (la pala imballata in cabina).
- **Cosa serve**:
  - una foto dell'azienda di almeno 1600 px di lato lungo, con un fondo calmo (cielo, muro, pavimento) dove stare il titolo;
  - dove la foto è più piccola (Unicar, Oby, Formentin, Framo), non la si ingrandisce. La si mette a misura vera, al centro, larga quanto la colonna, con il titolo sopra e non accanto, come Cleveland. Oppure si apre col solo testo, grande, e la foto subito sotto, finché non c'è il servizio fotografico.

### 2. Le persone con il nome, e dove si può con la faccia
- **Cosa**: chi guida l'azienda e chi risponde hanno un nome, un ruolo e, quando c'è, un ritratto. Tutti i ritratti vanno fatti con la stessa luce e lo stesso fondo.
- **Esempi**:
  - Auto Bayertz (tre ritratti in bianco e nero), Alpine (il preventivista con l'interno), BELFOR (sette dirigenti), Hesse (il titolare nel piede).
  - Da noi: Nord Service (Stefano e Leonardo Barbieri), Belletti (Gaetano e Irma Belletti, l'ing. Andrea Viel), La Termica (Mario Camporese e i figli), Fratelli Zuin (la terza generazione), Serenissima (i soci, se l'azienda vuole).
- **Cosa serve**:
  - i nomi e i ruoli confermati dall'azienda;
  - i ritratti, con il servizio fotografico;
  - intanto, i nomi nel testo e nella firma del blocco contatti ("Vi risponde Leonardo Barbieri"), senza fotografie inventate o sagome.

### 3. I lavori con il nome, il luogo, l'anno e una foto
- **Cosa**: al posto delle categorie generiche, tre-sei lavori veri, ognuno con la foto, il nome del luogo o del committente, l'anno e due dati.
- **Esempi**:
  - Eberhard ("Rathausbrücke, Zürich"), Habegger (i clienti), Brandenburg (il lavoro come titolo d'apertura), Alpine (il caso con il cliente), Jacksons ("Martello Tower No 25").
  - Da noi: Belletti lo fa già (Galleria Cavour, Ca' Michiel, Ca' della Nave, con portata, persone, fermate). Va esteso a Fratelli Zuin (ex Foro Boario 1968-69, Prato della Valle), La Termica (il condominio, il camino autoportante), Eurotecnica (le sale), Nord Service (il CAT D8R), Formentin (i lavori di recinzione).
- **Cosa serve**:
  - il permesso del committente per i nomi (per Nord Service, Tabarelli non va scritto);
  - le foto dei lavori, dalle gallerie che le aziende hanno già (La Termica circa 320, Nord 33);
  - l'anno di ogni lavoro, da chiedere.

### 4. Il dettaglio tecnico fotografato da vicino, con una didascalia di luogo
- **Cosa**: è la mossa per chi non ha un servizio fotografico. Una foto da vicino di un dettaglio del mestiere diventa l'immagine di marca, tagliata grande e con una didascalia precisa (che cosa è, dove, quando). Ripetuta in tutte le sezioni, diventa il segno della pagina.
- **Esempi**:
  - Pirtek (la scritta stampata sulla guaina e le coordinate sotto le foto), HANSA-FLEX (il disegno al tratto dei raccordi), Emch (lo schizzo a matita).
  - Da noi: Framo (la scritta della guaina e il raccordo pressato), La Termica (la giunzione del tubo inox, il rame sul coppo), Formentin (la maglia della rete ondulata fatta da loro), Nord Service (la superficie sabbiata a metà, il garnet), Unicar (la targhetta del carrello), Eurotecnica (il microfono da tavolo del sistema conferenze).
- **Cosa serve**:
  - un telefono recente, luce di finestra laterale, il fondo pulito, la foto a fuoco su un punto;
  - una didascalia vera per ogni foto ("Tubo 1/2", due trecce, raccordi pressati in officina, via Liguria 32");
  - niente illustrazioni o disegni rifatti al posto delle foto: vanno bene solo i disegni dell'azienda o dei suoi fornitori.

### 5. Le prove con l'unità di misura e con la garanzia
- **Cosa**: ogni cifra con la sua unità e con il periodo, e la garanzia in anni accanto al titolo se l'azienda la dà. Le misure dell'impianto valgono più delle parole: la cabina, la portata, il diametro, i metri quadri.
- **Esempi**:
  - Cleveland (la cabina 65' x 35' x 30' e che cosa ci entra), Emch (corsa fino a 30 m, portata da 180 a 1600 kg), Auto Bayertz (6 anni di garanzia), Jacksons (25 anni).
  - Da noi: Framo (da 3/16" a 3", lo fa già bene), Serenissima (9 cabine, 3000 mq), Nord Service (le misure della cabina, da chiedere), Belletti (da 12 kg a 100 persone), La Termica (oltre 500 mq di magazzino).
- **Cosa serve**:
  - le misure confermate dall'azienda, con l'anno della verifica;
  - la garanzia scritta, se esiste: mai inventarla.

### 6. Le strade per tipo di cliente o di edificio, subito
- **Cosa**: la prima scelta della pagina è "chi sei", non "che prodotto vuoi": privato o impresa, compagnia o amministratore, condominio o casa.
- **Esempi**:
  - KÖGEL (Privatkunden, Geschäftskunden), BELFOR (Versicherer, Verwaltungen, Industrie, Privat), Schmitt + Sohn (tipo di edificio), Jacksons (casa e giardino, commerciale e sicurezza).
  - Da noi: Oby e Formentin lo fanno già. Va fatto per La Termica (casa, condominio, impresa e installatore), Belletti (condominio, casa, negozio e ufficio, sanità e industria, accanto ai prodotti), Eurotecnica (evento, sala fissa, noleggio), Unicar (carrello fermo, manutenzione, ricambi).
- **Cosa serve**: solo riordinare i contenuti che le home hanno già. Le strade devono essere due-quattro, con parole del cliente e non del catalogo.

### 7. L'emergenza separata e sempre in vista
- **Cosa**: il numero dei guasti o del soccorso è un elemento a sé, con la sua etichetta ("Guasti 24 ore", "Soccorso stradale"), diverso dal numero d'ufficio. Resta visibile a ogni scorrimento: in una barra sottile in alto o in un blocco fisso in basso a destra.
- **Esempi**:
  - Schmitt + Sohn ("Service24" nella barra in alto), BELFOR (la "Hotline" fissa in basso a destra), Eberhard ("Notfalldienste" come prima voce), HANSA-FLEX (due numeri nel piede).
  - Da noi: Belletti (ce l'ha già, "Guasti 24 ore"), Serenissima (soccorso stradale 335 5639355), Oby (il cellulare), Unicar ("Carrello fermo?"), Fratelli Zuin (lo spurgo, se fanno il pronto intervento).
- **Cosa serve**:
  - il numero d'emergenza vero e gli orari in cui risponde, confermati;
  - dove non c'è un servizio d'emergenza, questa mossa non si fa (Framo, Formentin, Eurotecnica).

### 8. Una frase vera che torna, e niente parole d'ordine
- **Cosa**: una frase breve dell'azienda, già sua, che si ripete due o tre volte (apertura, metà pagina, chiusura) e fa da firma. Accanto, si tolgono "qualità", "innovazione", "eccellenza" e simili.
- **Esempi**:
  - Hesse ("Reparieren statt Ersetzen"), Alberts ("Gemacht, um zu halten"), KÖGEL ("Nichts ist zu kompliziert"), BELFOR ("We make it undone").
  - Da noi: Serenissima ("Botta? Risposta!", che è nel logo da anni), Framo ("Porta il tubo vecchio: te lo rifacciamo identico"), Nord Service ("Sappiamo far tornare nuove le macchine con cui lavori ogni giorno"), Unicar ("Consulenti, più che riparatori").
- **Cosa serve**:
  - una frase che l'azienda usa già (sito vecchio, furgoni, brochure, logo), non scritta da noi;
  - un posto fisso dove torna, sempre con lo stesso trattamento (stessa misura, stesso filetto).

### I tre siti migliori del gruppo
1. **Pirtek UK** (https://www.pirtek.co.uk/): il sistema più coerente. Ha un carattere solo, la carta millimetrata come segno, le didascalie con le coordinate, un servizio vero sui tecnici e la scritta della guaina usata come immagine. Insegna come si fa "studio" con poco.
2. **Eberhard** (https://eberhard.ch/): impresa di famiglia dello stesso mestiere di Fratelli Zuin. Ha l'emergenza in testata, le referenze con l'indirizzo e le persone vere con la livrea. Il testo è grande e si legge.
3. **Auto Bayertz** (https://www.auto-bayertz.de/): la struttura più utile per un'officina di servizio. Ha i quattro passi, il "gratis" solo dove è vero, la storia con il nome del fondatore, la galleria in una serie sola e i ritratti con nome e ruolo. Da prendere senza le etichette a pillola e le schede con icona.
