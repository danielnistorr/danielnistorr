# 02. Riferimenti dal vivo

Ricerca del 18 ottobre 2026. Ho aperto con Playwright (Chromium, attraverso il proxy) 17 siti di produttori e distributori di filtri e ricambi, italiani e stranieri, più il sito attuale di CFV. Dieci sono leggibili e completi e li uso qui sotto, quattro li ho guardati e messi da parte, tre erano bloccati. Ho guardato ogni prima schermata a 1440 e a 390, le prime tre schermate a 1440 e la pagina intera fino al piede.

Dove sono i file (tutti in `_prova/riferimenti/`):
- `<nome>-1440-schermo.png` e `<nome>-390-schermo.png`: prima schermata (1440x900 e 390x844);
- `<nome>-1440.png` e `<nome>-390.png`: pagina intera;
- `<nome>-tre-schermate.jpg`: le prime tre schermate a 1440 (2700 px, a metà scala); `<nome>-390-tre.jpg`: le prime tre a 390;
- `<nome>-misure.json`: caratteri letti dal codice, fondi più usati, bottoni, link `tel:`, larghezza a 390;
- `_foglio-a.jpg` ... `_foglio-d.jpg`: prime schermate 1440 e 390 affiancate; `_confronto-390.jpg`: sei siti a 390 uno accanto all'altro; `_sotto-*.jpg`: la parte bassa delle pagine (dalla terza schermata al piede);
- `ritagli/`: 11 ritagli dei gesti citati nelle conclusioni.
Script in `_prova/script/`: `rif.mjs` (quattro catture e misure), `titoli.mjs` (i tre testi più grandi della prima schermata con il loro carattere, per i siti senza `h1`), `tre.py`, `foglio.py`.

**Artefatti.** La pagina intera si fotografa allungando la finestra, per non far scattare i caroselli: le aperture alte "una schermata" allora si gonfiano (Hengst ha la cornice gialla lunga 2700 px). Per quei siti vale la `-schermo.png`. SF-Filter l'ho rifatto con la cattura a pagina intera normale (`shoot.mjs`), perché la pagina scorre in un contenitore interno. RS Italia ha lo stesso problema e non si lascia fotografare intera: per RS uso solo la prima schermata.

**Non usati.** Hydac (403 openresty), Parker (403), FleetPride (403): bloccano i robot. Busch Vacuum a desktop mostra l'avviso "versione obsoleta del browser" e la pagina senza stile (a 390 si vede: "Il vostro fornitore unico per tutte le vostre esigenze per il vuoto"). Granit Parts a desktop non carica il foglio di stile. MANN-FILTER su `/it/` dà la pagina 404 gialla: ho usato `/it-it.html`. HIFI FILTER non serve una versione italiana (`/it` porta al sito francese).

## 0. Da dove parte CFV (`00-sito-attuale-*`, `ritagli/cfv-muro-dei-marchi.jpg`)

| | Sito attuale |
|---|---|
| Testata | logo su blu notte, menu HOME, AZIENDA, MARCHI, E-COMMERCE, CONTATTI |
| Prima schermata | una foto composita scontornata su bianco: filtri di molti marchi su un ripiano (MANN-FILTER, Hengst, UFI, HIFI, Fleetguard LF3883, Donaldson, WIX, Iveco, Delphi e altri), con il logo CFV al centro. Nessun testo, nessuna ricerca, nessun telefono |
| Seconda e terza | banda blu con "Centro Filtri Veneto S.r.l. ha specialisti che lavorano dal 1985 nel settore della filtrazione e ricambi."; nastro giallo e nero da cantiere; blocco giallo con testo accanto a un primo piano di carta filtrante; "APPLICAZIONI PER PRODOTTI DI FILTRAZIONE" in cinque colonne di miniature (mezzi movimento terra e agricoltura, idraulici, separatori e pompe vuoto, trattamento aria e fumi, chimica e accessori) con testi giustificati |
| Caratteri e colori | Roboto; blu notte, giallo, nero, bianco |
| Cosa vale | la foto del ripiano è l'unica cosa che ha solo CFV: un distributore che mette i filtri di tutti i marchi uno accanto all'altro. È l'idea propria da cui partire (vedi conclusioni) |
| Cosa non va | in prima schermata non si capisce cosa fare: non si cerca un codice, non si chiama, non si sceglie tra ricambista e privato; settori e marchi stanno sotto la piega e in miniature piccole |

## 1. Produttori di filtri

### 1.1 MANN-FILTER (Germania, sito italiano) `01-mann-filter-*`
- **Prima schermata:** testata gialla con menu Catalogo, Trova Rivenditori, Applicazioni, Prodotti, Assistenza, Scopri di più, Motorsport. Sotto, una barra scura fissa con "Ricerca Smart" (menu a tendina per il tipo di ricerca), campo e "Cerca". Poi un mosaico a fisarmonica di quattro pannelli fotografici veri (Sostenibilità, "Di fiducia." con i volti di meccanici e clienti, Filtro aria per abitacolo, Motorsport).
- **Prime tre:** il titolo di marca; poi l'elenco delle famiglie a sinistra con icona (Filtro aria per l'abitacolo, Filtro aria, Filtro olio, Filtro carburante, Applicazioni speciali) e a destra una famiglia alla volta, con foto della confezione e del filtro scontornati e quattro righe di testo; poi tre numeri (100 % Qualità OE, 85 anni, 1° marchio per affidabilità) e "Dal primo all'ultimo chilometro" con un gruppo di filtri scontornati. Sotto: "Filtrazione pluripremiata", "Perché MANN-FILTER è la scelta vincente" (sei punti), piede con MANN+HUMMEL Italia S.r.l., indirizzo di Torino, telefono, fax, email.
- **Come si cerca:** barra di ricerca in ogni pagina, sotto la testata; a 390 si chiude in una barra "Cerca Prodotto" che si apre al tocco.
- **Famiglie, marchi, mezzi, foto:** famiglie a elenco con scheda accanto (`ritagli/mann-famiglie-a-elenco.jpg`); foto di prodotto scontornate con la confezione giallo-verde, sempre la stessa luce.
- **Tipografia e colori:** Helvetica Neue Heavy Condensed per i titoli (48 px), Helvetica Neue 55 Roman per il testo. Giallo pieno rgb(255,240,0) e verde del marchio: il colore viene dalla scatola, non da una tavolozza.
- **Densità:** alta ma ordinata; il giallo tiene insieme tutto.
- **Da non riprendere:** la fisarmonica a pannelli (si legge un pannello alla volta), la fila di tre numeri, "Perché ... è la scelta vincente", le icone al tratto in elenco.

### 1.2 Donaldson (USA, sito italiano) `02-donaldson-*`
- **Prima schermata:** testata blu con Prodotti, Settori, Risorse, Azienda, lente, lingua e tre bottoni arancio (Assistenza, Acquista, Contatti). Carosello di cinque slide: blocco blu diagonale con titolo e testo a sinistra, foto a destra (una linea di imbottigliamento, una donna con gilet in magazzino).
- **Prime tre:** "Innovazione per ogni settore", carosello di schede (Agricoltura, Conversione elettrica dei veicoli, Edilizia, Elettronica...); "Nuova tecnologia" (ArmorSeal, Downflo, sfiati); "Presenti a livello globale" con 10 / 1,300 / 150; una foto storica in bianco e nero di un uomo su un trattore accanto a "Uno spirito d'avanguardia, fondata nel 1915". Poi notizie ed eventi.
- **Come si cerca:** solo la lente in testata; in home non c'è un campo per il codice.
- **Tipografia e colori:** Univers (300 per i titoli a 50 px, 700 per i numeri a 100 px), Arial nel testo. Blu rgb(0,69,124) e rgb(19,128,197), arancio per le azioni.
- **Da riprendere:** la foto d'archivio accanto all'anno di fondazione.
- **Da non riprendere:** blocco colore con testo e foto accanto (lo schema di Zoccarato), carosello in apertura, fila di numeri, foto di settore da banca immagini (operaio con elmetto, mano con telefono).

### 1.3 Fleetguard (Cummins, ora Atmus, sito italiano) `03-fleetguard-*`
- **Prima schermata:** testata bianca con un campo largo al centro, "Ricerca per parola chiave, Letteratura, Parti n., VIN"; menu Home, Informazioni, Prodotti, Trova un rivenditore, Knowledge center, Supporto. Sotto, una foto vera: una mano con il guanto che monta un filtro LF3370 sul motore, un riquadro rosso che incornicia il filtro, il titolo "Funzionamento più pulito e più duraturo grazie alla scienza della filtrazione" su un velo scuro.
- **Prime tre:** "Prodotti in evidenza" con schede in cui il titolo è il codice (FK11025 Kit filtri carburante, LF17822 Filtro olio cartuccia, HF29230 Cartuccia idraulica sintetica); "Vai oltre. ... Non accontentarti mai." con "Cerca prodotti e soluzioni"; quattro articoli di esperti; foto di persone al lavoro, ognuna con il riquadro rosso. Piede: Cerca codici, Richiedi un preventivo, Trova un rivenditore, Assistenza in garanzia.
- **Come si cerca:** per codice, parola chiave, documentazione o numero di telaio (VIN), dallo stesso campo.
- **Tipografia e colori:** Helvetica Neue; bianco, nero rgb(28,28,28), rosso. Il titolo dell'apertura è disegnato dentro l'immagine (`titoli.mjs` non trova nessun testo grande nella prima schermata e non c'è `h1`).
- **Da riprendere:** il codice come titolo della scheda (`ritagli/fleetguard-codici-in-vista.jpg`); il filtro vero nelle mani di chi lo monta.
- **Da non riprendere:** titolo dentro la foto (a 390 diventa un riquadro di 90 px con il testo che copre il motore), lo slogan "Non accontentarti mai", le schede di articoli tutte uguali.

### 1.4 HIFI FILTER (Francia) `04-hifi-filter-*`
- **Prima schermata:** un render 3D isometrico in grigio (una città fatta di filtri), il titolo "VOTRE PARTENAIRE EN FILTRATION & SÉPARATION" in maiuscolo enorme con "PARTENAIRE" in rosso, un riquadro bianco "RECHERCHE: Vous cherchez un filtre, une application, un accessoire ?" con campo "Référence, nom, marque", accanto un blocco rosso "E-CATALOG".
- **Prime tre:** "Nos activités" e "Nos solutions" con due render isometrici (camion, escavatore, trattore, barca, fabbrica); filtri scontornati che scorrono su una parola gigante; "LE CONCEPT HIFI FILTER" ("depuis plus de 40 ans", filtri compatibili). Sotto: "ONE STOP FILTER SHOP" con una foto vera di un mucchio di filtri di ogni tipo (sacchi, cartucce idrauliche, pannelli, filtri a vite); news con data, fiere (EIMA, SEPEM); piede rosso.
- **Come si cerca:** campo unico per riferimento, nome o marca, più il catalogo elettronico a parte.
- **Tipografia e colori:** Druk Condensed 500 a 160 px, Aeonik nel testo; rosso rgb(228,5,32), grigi, nero.
- **Da riprendere:** la foto vera dell'assortimento mischiato (`ritagli/hifi-foto-assortimento.jpg`); il campo di ricerca che dice cosa si può scrivere.
- **Da non riprendere:** i render isometrici (sembrano generati), la parola gigante dietro i prodotti, "Votre partenaire", una parola del titolo in un altro colore come unico gesto.

### 1.5 Hengst (Germania, sito italiano) `08-hengst-*`
- **Prima schermata:** testata nera con Prodotti, Applicazioni, L'azienda, Carriera, campo, "Contattateci" giallo. Carosello con una spessa cornice gialla intorno a un'immagine (la Terra dallo spazio, "purifying our planet").
- **Sotto:** "Come possiamo aiutarvi?" con campo e **Ricerche frequenti** a pillole (Celle a combustibile, Idraulica, Assistenza sanitaria, Filtro HEPA); "Applicazioni" in dieci icone al tratto; quattro foto (Macchine agricole e da costruzione, Veicoli commerciali, Autovetture, Marina).
- **Tipografia e colori:** Museo 700 (slab) a 56 px, "Robot" 200 nel testo; nero, blu rgb(0,40,128), giallo.
- **Da riprendere:** le ricerche frequenti come scorciatoie sotto il campo (`ritagli/hengst-ricerche-frequenti.jpg`).
- **Da non riprendere:** la Terra dallo spazio, il carosello a tutta altezza, la griglia di icone.

## 2. Distributori e negozi

### 2.1 SF-Filter (Svizzera, distributore multimarca con marchio proprio) `05-sf-filter-*`
È il mestiere più vicino a CFV.
- **Prima schermata:** un solo compito. Giallo pieno, titolo "Find Your Filtration Solutions for Mobile and Industry", un campo bianco largo con selettore "All" e "Enter any reference or machine brand and model...", sotto "Search by OEM reference, SF item, machine brand and model." e "Need help finding the right filter? Call or email us." (`ritagli/sf-ricerca-unica.jpg`). Menu: Mobile, Industry, Cross reference list, SF-Filter Group, Customer Support.
- **Prime tre:** quattro tasselli (Filters for Mobile, Filters for Industries, Fluid Management, Latest products); una fascia con foto di un campo arato e il logo ("over 60 years of industry knowledge"); cinque servizi con icona; news; **Our brands**, un muro di 24 loghi in riquadri uguali (Argo Hytos, Baldwin, Cim-Tek, Coopers Fiamm, Donaldson, Eaton, Fleetguard, Hengst, Hydac, Kleenoil, MANN-FILTER, MP Filtri, Pall, Parker, Rexroth, RT Filter, SMC, UFI, WIX e altri).
- **Mezzi:** nel piede l'elenco per macchina (Agricultural machines, Automobiles, Construction machines, Small motors, Forklifts, Snow machines, Suction excavator vehicles, Trucks and buses) e per industria (Air, Compressed air, Dust removal, Hydraulic, Process filtration, Vacuum pump filters, Ventilation, Water...).
- **Come si cerca:** codice originale (OEM), codice SF, marca e modello della macchina, più la pagina "Cross reference list".
- **Tipografia e colori:** Open Sans 700 a 50 px e 400; giallo rgb(255,242,0), nero rgb(39,39,42), bianco.
- **A 390:** campo e frase di aiuto nella prima schermata, i quattro tasselli diventano righe.
- **Da non riprendere:** le strisce diagonali sfumate nel giallo, la fila di cinque icone dei servizi, la fascia con foto e logo.

### 2.2 Kramp (distributore di ricambi agricoli, sito italiano) `07-kramp-*`
- **Prima schermata:** testata rossa con campo "Cerca per codice articolo, marca o parola chiave"; sotto il menu per **mondo della macchina**: Attrezzature agricole, Trattori & Parti veicolo, Giardinaggio & Forestale, Oleodinamica & Trasmissioni, Macchine movimento terra, Negozio & Officina, e a destra "Ricerca modello" (`ritagli/kramp-menu-per-macchina.jpg`). Banner (Illuminazione a marchio Kramp), poi due tasti gialli larghi: "Trova un rivenditore" e "Diventa Cliente: richiedi un account per poter effettuare ordini".
- **Prime tre:** quattro tessere (EIMA Pad. 18 stand D22, motori rasaerba, 75 anni, Instagram); "I nostri marchi", striscia di loghi con frecce e contatore 13/50 (`ritagli/kramp-striscia-marchi.jpg`); quattro box rossi con icona (Parts Management, Shop, Engineering, Connect); prodotti di stagione; marchi sponsorizzati; "Polo informativo" con articoli datati; testimonianze di clienti con nome e paese (Cominelli, Leno BS; Italtecnica, S. Donà di Piave VE). Piede con tutte le categorie per mondo.
- **Tipografia e colori:** Barlow Condensed 700 maiuscolo a 40 px, Barlow nel testo; rosso rgb(157,26,21), giallo rgb(255,187,51), azzurro.
- **Da riprendere:** il menu per macchina, non per tipo di filtro; le due porte esplicite per chi compra (rivenditore e cliente con account), che per CFV sono RICAMBISTI e PRIVATI.
- **Da non riprendere:** i box rossi con icona, le tessere promozionali che si prendono la prima schermata, la quantità di sezioni. Barlow Condensed + Barlow è anche la coppia di Benvegnù: per CFV non va ripresa (clausola di campagna).

### 2.3 DT Spare Parts (Diesel Technic, ricambi per veicoli industriali, sito italiano) `09-dt-spareparts-*`
- **Prima schermata:** barra blu di servizi con icone (Partner Portal, Helpdesk, Premium Shop, Parts Specialists, Novità, Newsletter) e campo "Termine di ricerca"; logo con "Genuine Quality. Durable Trust."; slider "365 giorni di regali" (programma premi per le officine); "Il Suo marchio per un ottimo lavoro" con quattro tessere grigie (Quasi 50 000 prodotti, 24 mesi di garanzia, Servizi online, Premium Shop).
- **Sotto:** foto di un tecnico in officina con loghi di negozi che fluttuano (montaggio); "Trovi il ricambio in modo semplice e veloce" con i dispositivi finti del Partner Portal; notizie datate (controllo del ricambio dal numero di telaio); "Parts Specialists Video" con tecnici veri accanto al pezzo (PS TIPS: Air dryer, valvole, interruttori); newsletter; nel piede il bollino "TecDoc Premier Data Supplier".
- **Tipografia e colori:** Frutiger 700 e 900; blu rgb(27,72,136), grigio chiaro, bianco.
- **Da riprendere:** il numero concreto dell'assortimento quando è vero; le persone del mestiere davanti al pezzo.
- **Da non riprendere:** slider promozionale, tessere con icona, dispositivi finti, loghi fluttuanti.

### 2.4 FilterFinder (Regno Unito e Irlanda, negozio di filtri industriali del gruppo Micro-Mesh) `11-filterfinder-*`
- **Prima schermata:** barra blu notte con campo "Enter your item, model, SKU or part #", EUR, Contact, Sign in, Cart; sotto "Chat with us", "DHL Express global shipping", "Rated Excellent on Trustpilot". Apertura "Get Started & Find Your Filters" con "1,000,000+ cross references and over €100M of stock" e un secondo campo; un disegno al tratto di un filtro. Tre schede (spedizione DHL, accesso, aiuto in chat).
- **Prime tre:** "Our Key Partners", 16 loghi (MANN-FILTER, Fleetguard, Pall, Hydac, Argo Hytos, Donaldson, MP Filtri, Filtrec, Rexroth, HIFI FILTER, Parker, Stauff, Microfit, Filtration Group, UFI, Hengst) e sotto cinque famiglie con foto di prodotto (Hydraulic, Oil, Compressed Air, Air, Process Filters) (`ritagli/filterfinder-muro-marchi-famiglie.jpg`); settori in carosello; "Innovating Filtration Since 1968" con la foto d'archivio dell'edificio della Micro-Mesh (`ritagli/filterfinder-dal-1968.jpg`); recensioni; piede con indirizzo della sede.
- **Tipografia e colori:** Roboto 700 a 40 px e 400; blu notte rgb(36,47,62), giallo.
- **Da riprendere:** marchi e famiglie nella stessa fascia (chi distribuisce cosa, e di che tipo); l'anno con la sua prova d'archivio.
- **Da non riprendere:** tre schede in fila, carosello di settori con foto di repertorio (un caccia, un aereo), il blu notte con giallo come semplice tavolozza.

### 2.5 RS Italia (distributore industriale) `14-rs-1440-schermo.png`
- Solo la prima schermata. Il campo ha un interruttore **"Codice costruttore"**: acceso, la ricerca legge il codice del produttore invece delle parole (`ritagli/rs-codice-costruttore.jpg`). Noto Sans e Oswald, bordeaux.
- **Da riprendere:** dire in chiaro che si può incollare il codice del costruttore. Per CFV basta la frase sotto il campo, senza interruttore.

## 3. Visti e messi da parte

| Sito | Prima schermata | Perché fuori |
|---|---|---|
| WIX Filters (USA) `06-wix-*` | nero, video vuoto al primo fotogramma, "SEE WHY WIX FILTERS IS THE CHOICE OF CHAMPIONS", h1 "RACING IS IN OUR DNA"; Gotham Black e Book; bottone giallo "FILTER FINDER" fisso in testata | slogan e video; l'unico gesto utile è il bottone di ricerca sempre in testata |
| UFI Filters (Verona) `13-ufi-*` | render di un modulo filtro su blu, "CHOSEN BY THE BEST"; Montserrat 800 e Roboto; poi primo impianto: Light vehicles, Heavy duty | render e slogan, parla da fornitore di primo impianto, non da chi vende al banco |
| MP Filtri (oleodinamica, Pessano con Bornago) `10-mp-filtri-*` | render di un filtro blu enorme con "PASSION TO PERFORM" in sottile; Helvetica Neue LT; pagina intera non catturabile | esempio da manuale di slogan e render come unico gesto |
| Busch Vacuum `12-busch-390*` | a 390: "Il vostro fornitore unico per tutte le vostre esigenze per il vuoto." e illustrazione | desktop non leggibile dal robot |
| Hydac, Parker, FleetPride, Granit Parts | 403 o pagina senza stile | non leggibili |

## 4. Cosa dicono i riferimenti, in breve
- **Il primo gesto è la ricerca.** Nove siti su dieci mettono un campo nella prima schermata o nella testata (tutti tranne Donaldson, che ha solo la lente); i migliori dicono cosa si può scrivere (codice originale, codice concorrente, marca e modello, telaio).
- **Si entra per macchina.** I distributori (Kramp, SF) dividono per mondo della macchina: agricoltura, movimento terra, veicoli industriali, oleodinamica, industria. I produttori dividono per famiglia di filtro (aria, olio, carburante, abitacolo, idraulico).
- **I marchi sono la prova del distributore.** SF e FilterFinder mettono il muro dei loghi alto nella pagina; Kramp una striscia; CFV ha già una foto che fa la stessa cosa con i prodotti veri.
- **Caratteri:** grottesco condensato e pesante per i titoli (Helvetica Neue Heavy Condensed, Druk Condensed, Barlow Condensed, Oswald), grottesco neutro nel testo; nessun serif tranne lo slab di Hengst. Colore pieno che viene dal marchio o dalla confezione (giallo MANN, giallo SF, rosso HIFI e Kramp, blu Donaldson e DT).
- **Densità:** alta, ma con un compito chiaro per schermata. I siti che sembrano "da IA" sono quelli con render, slogan e caroselli (HIFI, UFI, MP, WIX, Hengst); quelli che sembrano veri hanno foto di filtri veri e codici leggibili (Fleetguard, MANN, SF, la foto "One stop filter shop" di HIFI).

## 5. Conclusioni

### Gesti da riprendere per CFV
1. **Una sola ricerca che dice cosa si può scrivere**, con il telefono subito sotto. Campo largo nella prima schermata, sotto una riga sola: codice originale, codice di un altro marchio, oppure marca e modello del mezzo; "Non lo trovi? 049 9801910 o info@centrofiltriveneto.com". Da `ritagli/sf-ricerca-unica.jpg` (SF-Filter), con la frase di `ritagli/rs-codice-costruttore.jpg` (RS) e il campo per riferimento, nome e marca di `04-hifi-filter-1440-schermo.png`. Dove porta la ricerca (e-commerce attuale o richiesta del codice) è [DA CONFERMARE] e va nel LEGGIMI.
2. **Il ripiano di tutti i marchi come idea propria della prima schermata.** È la foto che CFV ha già (`ritagli/cfv-muro-dei-marchi.jpg`): un distributore che mette Fleetguard, Donaldson, MANN-FILTER, HIFI e gli altri uno accanto all'altro. Nessun produttore può mostrarla, perché ognuno mostra solo i suoi. Va tenuta grande, scontornata, accanto alla ricerca, non sotto. Rinforzo: la foto vera e mischiata di `ritagli/hifi-foto-assortimento.jpg` (HIFI, "One stop filter shop"). Controllare la risoluzione originale prima di usarla a tutta larghezza.
3. **Entrare per mezzo e per macchina, non per tipo di filtro.** Una riga di ingressi con i settori di CFV: auto, veicoli industriali, movimento terra, agricoltura, oleodinamica, pompe a vuoto, aria e fumi, depolverazione, chimica e accessori. Da `ritagli/kramp-menu-per-macchina.jpg` (Kramp) e dal piede di `05-sf-filter-1440.png` (SF, per macchina e per industria).
4. **Marchi e famiglie nella stessa fascia.** I nomi dei marchi distribuiti (dal sito attuale) accanto alle famiglie che coprono, scritti come testo; i loghi solo dopo l'autorizzazione o la conferma di distributore (nel LEGGIMI). Da `ritagli/filterfinder-muro-marchi-famiglie.jpg` (FilterFinder) e dal muro "Our brands" di `05-sf-filter-tre-schermate.jpg`.
5. **Due porte esplicite per chi ordina**: RICAMBISTI e PRIVATI, due tasti larghi con una riga ciascuno su cosa ottiene chi entra. Da "Trova un rivenditore" e "Diventa Cliente" di `07-kramp-1440-schermo.png` (Kramp). Cosa offre CFV a ciascuno va preso da 01 o segnato [DA CONFERMARE].
6. **Il codice come titolo** dove si mostra un prodotto: codice grande, famiglia e mezzo sotto, foto scontornata. Da `ritagli/fleetguard-codici-in-vista.jpg` (Fleetguard). Solo codici veri leggibili nelle foto di CFV (per esempio il Fleetguard LF3883 della foto del ripiano), mai codici inventati.
7. **"Dal 1985" con la sua prova**, non come numero in una fila. Da `ritagli/filterfinder-dal-1968.jpg` (FilterFinder, l'edificio d'archivio) e dalla foto del trattore del 1915 in `02-donaldson-tre-schermate.jpg`. Una foto della sede di Vigonovo o del primo magazzino è [DA CONFERMARE]: se non c'è, l'anno resta una riga di testo.
8. **Le richieste frequenti come scorciatoie** sotto il campo (per esempio le famiglie più chieste), in pillole di testo. Da `ritagli/hengst-ricerche-frequenti.jpg` (Hengst). Quali sono le più chieste va confermato con CFV; in prima battuta si usano i settori del sito attuale.

Colore e caratteri: il colore deciso c'è già nel marchio di CFV (giallo, blu, nero, il nastro giallo e nero del sito attuale), come per MANN e SF viene dal marchio. Titoli in un grottesco condensato pesante, come tutto il settore, ma non Barlow Condensed (già Benvegnù e Kramp) e non il giallo pieno di MANN e SF come fondo dell'intera apertura: la scelta va fatta nella fase di direzione.

### Errori da evitare
1. **Titolo-slogan al posto del compito**: "PASSION TO PERFORM" (`10-mp-filtri-1440-schermo.png`), "RACING IS IN OUR DNA" (`06-wix-*`), "CHOSEN BY THE BEST" (`13-ufi-*`), "Votre partenaire" (`04-hifi-filter-*`), "Non accontentarti mai" (`03-fleetguard-tre-schermate.jpg`). Il titolo di CFV dice cosa si trova e per quali mezzi.
2. **Render 3D e illustrazioni isometriche** al posto delle foto: le città di filtri di HIFI, i moduli di UFI e MP Filtri sembrano generati. CFV ha foto vere di prodotti veri: si usano quelle.
3. **Carosello o fisarmonica in apertura**: Donaldson (cinque slide), Hengst, DT, WIX, la fisarmonica di MANN. Il messaggio cambia mentre lo leggi e a 390 resta una sola slide.
4. **Blocco colore con testo e foto accanto, file di box con icona**: l'apertura di Donaldson, "Il Suo marchio per un ottimo lavoro" di DT, i cinque servizi di SF, i quattro box di Kramp. Sono gli schemi che il giudice punisce (K6) e sono quelli del sito attuale di CFV (blocco giallo con foto, cinque miniature in fila).
5. **Fila di numeri**: MANN (100 % / 85 anni / 1°), Donaldson (10 / 1,300 / 150), FilterFinder (1,000,000+). CFV non ha numeri pubblici di codici, magazzino o clienti: non si inventano.
6. **Foto di repertorio dei settori**: la Terra dallo spazio di Hengst, il caccia di FilterFinder, l'operaio con elmetto di Donaldson. Per i settori di CFV meglio il nome del mezzo e il filtro vero che una foto di stock; se serve una foto, va con licenza verificata e segnata da sostituire.
7. **Titolo disegnato dentro la foto**: Fleetguard non ha testo vero nell'apertura e a 390 il titolo copre il motore. Il titolo di CFV è testo, la foto non viene coperta.
8. **Promozioni e servizi che rubano la prima schermata al compito**: "365 giorni di regali" di DT, le tessere fiera e Instagram di Kramp, le tre schede DHL, accesso, chat di FilterFinder. Nella prima schermata di CFV stanno solo ricerca, ripiano dei marchi, settori, le due porte e il telefono.
