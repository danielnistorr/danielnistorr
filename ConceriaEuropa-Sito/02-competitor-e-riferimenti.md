# 02. Concorrenti e riferimenti di design

Ricerca del 6 ottobre 2026. Ogni sito è stato aperto dal vivo con Playwright (Chromium, attraverso il proxy) a 1440 e a 390 px e fotografato a pagina intera; i siti con scorrimento animato sono stati fotografati a finestre successive e poi cuciti. Visitati 6 concorrenti e 15 siti di riferimento (più 8 pagine interne); tenuti 5 riferimenti premium e 2 funzionali.

File: screenshot in `_prova/ricerca/` (`c*` concorrenti, `r-*` home dei riferimenti, `p-*` pagine interne), pezzi già tagliati in `_prova/ricerca/pezzi/`, ritagli dei gesti in `_prova/ricerca/ritagli/`, campione delle tre accoppiate in `_prova/ricerca/campioni/accoppiate-1440.jpg`. Script: `_prova/script/foto.mjs`, `ruota.mjs`, `cuci.py`, `ritagli.py`.

**Chi è Conceria Europa, per scegliere i riferimenti** (solo dal sito attuale): conceria di Montebello Vicentino fondata nel 1969 dai fratelli Faggiana; "pelli per arredamento e carrozzeria auto"; "una delle poche realtà del comprensorio che possono vantare ancora un ciclo di lavorazione completo (dalla pelle grezza al prodotto finito)"; laboratorio interno per prove fisiche; ISO 9001 dal 1999. Sul sottosito products.conceriaeuropa.it: pelli per arredo (semianilina, pieno fiore, smerigliata e stampata), automotive (volanti, selleria, kit di pelli tagliate) e pelli speciali, cioè ignifughe e "Avion" per aeromobili, che "meets the specifications of F.A.R.-B, F.A.R.-A, + category 1 IM + Crib 5". I riferimenti quindi sono concerie per auto, aerei e imbottiti, non case di moda.

## 1. Concorrenti

| # | Concorrente | Dove | Settori (dal loro sito) | Cosa fa meglio di Conceria Europa oggi | Cosa fa peggio | Screenshot |
|---|---|---|---|---|---|---|
| 1 | [Conceria Montebello](https://www.montebello-tannery.it/) | Via Lungo Chiampo 123, Montebello Vic.: la stessa via (Conceria Europa è al 129) | pelli bovine per moda, arredo, calzatura, pelletteria; dal 1967 | sito responsive; fondo pagina completo (PEC, P.IVA, capitale sociale); bilancio di sostenibilità 2024 e un ebook scaricabili; logo POR FESR in fondo pagina, con discrezione | la home parla solo di moda (album FW, blog di alta moda, "Fast Collection / Seasonal / Icons"): l'arredo non si vede; copyright fermo al 2022; nel nostro scatto a 390 la foto d'apertura non si carica e resta il testo alternativo (da ricontrollare a mano) | `c1-montebello-1440.png`, `-390.png` |
| 2 | [Poletto Leathers](https://www.polettoleathers.com/it/) | Arzignano | in home: abbigliamento, pelletteria, arredamento, calzature; aviazione secondo il profilo Lineapelle [DA VERIFICARE] | sito recente e asciutto (Archivo, grigio #EAEAEA, blocchi neri); voce "Store ready to go" sempre in testata; settori come quattro colonne di foto sfalsate; foto vera dello stabilimento; "pelli chrome free e metal free" spiegate in una riga | apertura video che nel nostro scatto resta un fondo grigio; foto di stretta di mano da archivio per "Parliamone"; iscrizione alla newsletter due volte nella stessa home; l'aviazione non compare | `c2-poletto-*` |
| 3 | [Gruppo Mastrotto](https://www.mastrotto.com/it) | Arzignano | fashion, interior e design, automotive, nautica, aviazione, materiali rigenerati | è il concorrente diretto sugli stessi tre settori; griglia di sei settori con foto, due righe di testo e "Scopri di più"; servizio Express con numeri concreti (più di 1.700 colori, spedizione in 48 ore, piccoli quantitativi); news con data; PEC in fondo | superlativi generici già nel titolo della pagina; la scheda aviazione dice "i più rigidi parametri di sicurezza" senza nominare una norma; il jet e lo yacht non mostrano la pelle | `c4-mastrotto-*`, ritaglio `20` |
| 4 | [Gruppo Dani](https://www.gruppodani.com/en/) | Arzignano | Furniture & Contract, Leather Goods, Clothing, Footwear, Automotive, Transportation, Smart Devices, Saddlery | una prova datata e verificabile (EcoVadis Platinum, marzo 2026); minisito del bilancio di sostenibilità; fondo pagina completo (PEC, REA, capitale sociale) | apertura a carosello con un dipinto; otto settori elencati in una frase sopra una sola foto; nel nostro scatto una lunga fascia bianca sotto i settori (animazione non partita, da ricontrollare) | `c5-dani-*` |
| 5 | [Faeda](https://www.faeda.com/) | Montorso Vicentino | pelletteria, calzatura, arredamento e auto; dal 1956 | foto grandi di pelle vera; servizio FLASH spiegato con numeri (oltre 700 colori, spedizione in 48 ore, nessun minimo d'ordine) | sito Wix con la versione per telefono fissata a 320 px (`<meta name="viewport" content="width=320">`) e poi ingrandita; testi pieni di superlativi; un volto in primo piano senza didascalia; carosello a frecce | `c6-faeda-*` |
| 6 | [G.M. Leather](https://gmleatherspa.com/) | Arzignano | arredamento, pelletteria e moda, automotive aftermarket; quotata su Euronext Growth Milan dal 13 luglio 2022 ([il NordEst](https://www.ilnordest.it/economia/imprese/il-gruppo-vicentino-gm-leather-spa-approda-a-piazza-affari-xwya4p0p)) | linea del tempo con gli anni; numeri in evidenza | al nostro browser risponde prima una verifica Cloudflare ("Non sono un robot"); parole d'accento in corsivo colorato; a 1440 l'anno 1976 va a capo in "197 / 6"; icone in riquadri; foto d'archivio generiche (mani con borsa, divano) | `c3-gmleather-*` |

Dati di dimensione citati solo dove pubblici: Conceria Montebello S.p.A. 35,8 M€ di fatturato 2023, 100-249 dipendenti ([aziende.it](https://www.aziende.it/conceria-montebello-s-p-a)); Conceria Europa 15,6 M€ nel 2024 (da 01).

**Cosa fanno i migliori:**
- i settori sono la prima navigazione, ognuno con una foto (Mastrotto, Poletto);
- un servizio spiegato con numeri invece che con aggettivi (Mastrotto Express, Faeda FLASH, Poletto Store);
- prove con data (Dani: EcoVadis marzo 2026) e documenti scaricabili (Montebello: bilancio 2024);
- dati societari completi in fondo pagina, PEC compresa.

**Cosa non fa nessuno (lo spazio per Conceria Europa):**
1. **mostrare la pelle che passa per le fasi.** Conceria Europa ha già sei foto della "Metamorfosi della pelle" (pelle grezza, rinverdita, wet-blue, crust, tinta, rifinita) e scrive di avere il ciclo completo. Nessun concorrente della valle lo fa vedere;
2. **nominare le norme.** Per l'aviazione Mastrotto scrive "parametri di sicurezza"; Conceria Europa ha già pubblicato le sigle (F.A.R.-A, F.A.R.-B, classe 1 IM, Crib 5);
3. **il laboratorio.** I concorrenti mostrano la sostenibilità, nessuno le prove. Conceria Europa ha un laboratorio interno e foto vere delle prove (trazione, macchina di prova);
4. **un nome a cui scrivere.** Nessuno indica un referente commerciale; Conceria Europa ha un indirizzo commerciale distinto da info@ [nome e ruolo DA CONFERMARE].

**Posizionamento proposto** (solo fatti del sito attuale): "Pelli per arredamento, automotive e aviazione. Dalla pelle grezza al prodotto finito, a Montebello Vicentino, dal 1969." L'aviazione sul sito principale compare solo negli H1 nascosti; sul sottosito ha una pagina sua: va confermata come settore attivo [DA CONFERMARE]. Contro Mastrotto (stessi settori, molto più grande) non si gareggia su ampiezza e servizio di pronta consegna, che Conceria Europa non dichiara e non va inventato, ma su ciclo completo, laboratorio e norme dichiarate. Contro Montebello (stessa via) la differenza è netta: loro parlano alla moda, Conceria Europa all'arredo e al trasporto.

**Copy da evitare** (visto nei concorrenti): i superlativi dell'elenco PAROLE_VIETATE di `build.py`, presenti in Mastrotto, Faeda e G.M. Leather; "punto di riferimento", "partner"; i contatori che invecchiano: il sito attuale scrive "da oltre 40 anni al servizio della pelle", che nel 2026 è già sbagliato per difetto. Si scrive "dal 1969".

**Caratteri dei concorrenti** (da non usare, per distinguersi): Montebello Raleway e Montserrat; Poletto Archivo e DM Sans; Mastrotto Silka; Dani Tiempos Fine e Figtree; Faeda Avenir e Helvetica (Wix); G.M. Leather Arsenal e Montserrat.

## 2. Riferimenti

### 2.1 Riferimenti premium

Tratti comuni ai cinque: fondo neutro (bianco, grigio #E8E8E8 o #F2F2F2), un solo senza grazie con i titoli in peso leggero, testo piccolo e ordinato, il colore lo porta la pelle e non l'interfaccia, dati tecnici scritti per esteso, documenti da scaricare. Il corsivo graziato compare solo in Elmo, come parola d'accento dentro i titoli: è il cliché da non riprendere.

#### Bridge of Weir Leather: [bridgeofweirleather.com](https://www.bridgeofweirleather.com/)
Conceria scozzese per interni auto (Scottish Leather Group). Founders Grotesk 300, titoli a 100 e 54 px; fondo #E8E8E8; un trattino rosso corto sotto i titoli; link testuali rossi con freccia; fondo pagina #182427.
- **Gesto da riprendere:** (1) la pelle fotografata come oggetto su un grigio neutro, il titolo accanto e non sopra la pelle; da telefono il titolo scende sotto la foto e la pelle resta pulita; (2) titolo leggero a sinistra e testo a destra in due colonne, trattino corto sotto il titolo; (3) la prova di laboratorio come foto principale di una sezione ("Superior leather, tested for high performance", provino in trazione).
- **Da evitare:** tre colonne con icona in fila ("Perfection / Driven / Inspired"); nature morte con muschio e provette per la sostenibilità; testo corrente #707070 su #E8E8E8, contrasto 4,0:1, sotto il 4,5:1 necessario.
- **Ritagli:** `01-bridgeofweir-pelle-come-oggetto.jpg`, `02-...-titolo-e-testo-in-due-colonne.jpg`, `03-...-laboratorio-prova.jpg`.

#### Edelman Leather (MillerKnoll): [maharam.com/edelman](https://www.maharam.com/edelman/)
Pelli per imbottiti, contract, aviazione e nautica. Home fatta solo di foto: un dittico e sotto un trittico di pelli in piega, nessuna frase. Scheda prodotto (Arc 700138-003): foto della pelle, foto di tutte le varianti impilate, griglia di quadratini colore, poi la scheda in due colonne: Characteristics, Testing ("BS 5852 Crib 5", "FAR 25.853a"), Environmental, e sotto Documents (Specifications, Maintenance Guidelines, Environmental Data Sheet, MSDS). Color Library: tutte le pelli in una griglia di quadrati, ordinata per colore, con un filtro per tinta.
- **Gesto da riprendere:** il blocco "Prove" che elenca le norme per esteso, una per riga, nella scheda delle pelli speciali e aviazione; le pelli in piega a tutta cella, senza testo sopra.
- **Da evitare:** testo a 9-16 px, carrello campioni, griglia infinita (Conceria Europa ha poche foto: una griglia lunga resterebbe vuota).
- **Ritagli:** `10-edelman-pelli-in-piega.jpg`, `11-edelman-scheda-prove-e-documenti.jpg`, `12-edelman-biblioteca-colori.jpg`. Da telefono le varianti vanno a capo 5 per riga e la scheda diventa una colonna (`p-edelman-arc-390.png`).

#### Sørensen Leather: [sorensenleather.com](https://sorensenleather.com/)
Conceria danese, pelli per arredo e architettura. Messina Sans per testo e menu, AT Realm (graziato dritto) per i titoli; fondo #F2F2F2. Sopra il menu una barra di strumenti: "Image Bank", "3D Download", "Samples". In home otto quadrati piccoli con l'etichetta sotto, senza cornice. Pagina collezione (CLASSIC): testo, poi un elenco con etichette in neretto (Thickness 1.4-1.6 mm, Size 5.0-6.0 m², Origin, Surface, Finish, Tannage, Dye, Certification), poi i link "Download Technical Details", "Order samples", "OEKO-TEX® certificate", poi i colori con nome e codice ("Black - 40433").
- **Gesto da riprendere:** la scheda pelle a etichette in neretto più valore, chiusa da link di download; i colori con il nome sotto; la barra di strumenti come idea per "Certificati" e "Contatti" sempre a portata.
- **Da evitare:** banner cookie che copre l'apertura, finestra newsletter che si apre da sola, titoli graziati (vedi §4).
- **Ritagli:** `07-sorensen-barra-strumenti.jpg`, `08-sorensen-griglia-quadrati.jpg`, `09-sorensen-scheda-tecnica-e-colori.jpg`.

#### Elmo: [elmoleather.com](https://elmoleather.com/)
Conceria svedese: arredo, automotive, aviazione, nautica, ferroviario. Bagoss Standard. Ogni sezione si apre con un'etichetta piccola in neretto sopra un filetto a tutta larghezza ("A Good Choice", "Designed With the Airline in Mind", "Popular Prints Available"). Pagina aviazione: il prodotto con un dato preciso ("Elmolite... weighing just 700 grams/m²"); foto delle installazioni con didascalia che dice dove ("Seats with Elmo leather inside Norwegian Air Shuttle B737NG"), la fiera con anno ("Hamburg Interiors Expo 2023").
- **Gesto da riprendere:** etichetta più filetto come sistema di apertura di tutte le sezioni; didascalie che dicono cosa si vede; un prodotto presentato con un numero vero.
- **Da evitare:** parole in corsivo graziato dentro i titoli ("High-quality *Leather*"); etichette a pillola colorata sopra le foto; una fascia di colore pieno diverso per ogni sezione; foto d'archivio con un bambino al finestrino.
- **Ritagli:** `16-elmo-etichetta-e-filetto.jpg`, `17-elmo-prodotto-con-dato.jpg`, `18-elmo-didascalia-installazione.jpg`, `19-elmo-quattro-settori.jpg`.

#### Kvadrat: [kvadrat.dk](https://www.kvadrat.dk/en)
Tessuti per imbottiti e contract: il settore vicino, stessi clienti (produttori di divani e sedute). Interfaccia bianca e grigia, il colore lo dà il materiale. Scheda prodotto (Ria 2): foto grande del materiale, accanto le varianti in quadratini con il codice sotto; "Product details" a etichetta e valore (Category, Composition, Width, Weight); poi sezioni richiudibili Performance, Care, Downloads; sotto la foto la nota "colours displayed digitally may vary slightly from the actual product. Therefore, we recommend requesting samples before ordering".
- **Gesto da riprendere:** la nota onesta sui colori a schermo con l'invito a chiedere i campioni; la tabella etichetta e valore accanto alla foto.
- **Da evitare:** contenuti sullo stilista famoso, ordini dietro accesso, pulsanti a pillola neri tutti uguali.
- **Ritaglio:** `13-kvadrat-varianti-e-dettagli.jpg`.

### 2.2 Riferimenti funzionali (contenuto giusto, aspetto da non riprendere)

| Riferimento | Cosa fa | Cosa si prende | Cosa no |
|---|---|---|---|
| [Wollsdorf Leder](https://www.wollsdorf.com/) (Austria: auto, arredo, aerei, gli stessi tre settori) | tre settori con una parola sola, "Road / Interior / Air", e una lineetta sotto; pagina aerei con fatti verificabili ("certified since 2007 according to EN 9100", pelle "about 40% lighter"); riquadro "Your contact person" con nome, ruolo e telefono | i tre settori chiamati con una parola: Arredamento, Automotive, Aviazione; il referente commerciale con nome e contatto diretto [DA CONFERMARE] | tre riquadri uguali in fila, aerei disegnati dentro cornici, cascata da archivio, loghi dei clienti (Conceria Europa non ne pubblica), Kievit 100 a 103 px sopra la foto, finestra cookie a tutto schermo. Ritagli `04`, `05`, `06` |
| [Spinneybeck](https://www.spinneybeck.com/) (MillerKnoll, pelli per arredo e architettura) | "Color Book": quadrati di pelle con il codice sotto (SA 0783, AU 0663...) e filtri per colore, articolo, grana, rifinizione; in fondo pagina una colonna "Downloads": About Leather, Environmental, Catalogs, Product Cut Sheets, Maintenance + Cleaning | la colonna "Documenti" nel fondo pagina, con i file che Conceria Europa ha già (certificato qualità, certificato ICEC, Policy aziendale); il ritmo cella più codice per la sequenza delle fasi | impaginazione datata, didascalia grigia sopra la foto d'apertura, carosello a frecce. Ritagli `14`, `15` |

### 2.3 Aperti e scartati

- [Moore & Giles](https://mooreandgiles.com/): oggi è un negozio di borse; finestra "Which Bag is Right for You?" all'apertura.
- [Tärnsjö Garveri](https://tarnsjogarveri.com/): fondo crema, EB Garamond maiuscolo spaziato, negozio al dettaglio: è proprio il cliché bocciato.
- [Garrett Leather](https://garrettleather.com/): pelli per aviazione e arredo, ma titoli IvyPresto, icone in cerchi e pulsanti a pillola; utile solo l'elenco "Resources" (Hide Sizes, Glossary, Leather Care).
- [Foglizzo](https://www.foglizzo.com/): ambienti che sembrano rendering, Playfair Display.
- [Boxmark](https://www.boxmark.com/): blocchi rossi, carosello con logo "Eco".
- [Lantal](https://www.lantal.com/en/): tessuti per aerei; foto ritagliate a cerchio e lunga lista di notizie.
- [Muirhead](https://www.muirhead.co.uk/): pelli per aviazione; contenuti utili ma sezioni che compaiono in dissolvenza e pannello cookie laterale.
- [Pasubio](https://www.pasubio.com/en/): conceria auto di Arzignano con Microgramma esteso; la home blocca lo scorrimento e il video risponde "We couldn't verify the security of your connection": non verificabile, quindi non usato.

## 3. Cosa si riprende

| Gesto | Da | Dove nel sito di Conceria Europa | Con quale materiale vero | Condizione |
|---|---|---|---|---|
| Pelle protagonista su fondo neutro, titolo accanto e non sopra; da telefono il titolo sotto la foto | Bridge of Weir, Edelman | apertura della Home | `images/home/1-4.jpg`, 2200x918: pelli in piega ocra, nero, cuoio, petrolio | mai oltre 2200 px; ritaglio per breakpoint; niente testo sulla pelle |
| Etichetta piccola più filetto a tutta larghezza come apertura di ogni sezione | Elmo | tutte le pagine | testi propri | una sola scala di spazi (`SPAZI`) |
| Titolo leggero a sinistra, testo a destra, trattino corto sotto il titolo | Bridge of Weir | Azienda, introduzione dei settori | "Fondata nel 1969 dai fratelli Faggiana..." (testo attuale, corretto) | |
| Settori chiamati con una parola | Wollsdorf | Home e menu: Arredamento, Automotive, Aviazione | `arredamento.jpg` 419x411, `background_autom_arred/1.jpg` 1096x476, `speciali_1/2.jpg` 615x257 | non tre riquadri uguali in fila: nomi grandi su una riga con filetto e foto di misure diverse; Aviazione [DA CONFERMARE] |
| Sequenza delle fasi, cella più numero | ritmo della mazzetta Spinneybeck; il contenuto è solo di Conceria Europa | "Metamorfosi della pelle", in Home e in Azienda | sei foto `images/metamorfosi/*.jpg`, 1096x476 | le foto hanno la scritta impressa in basso a destra: ritagliarla o chiedere gli originali |
| Blocco "Prove" con le norme una per riga | Edelman (Testing) | Pelli speciali / Aviazione | "F.A.R.-B, F.A.R.-A, + category 1 IM + Crib 5" dal sottosito products | solo le sigle pubblicate; valori ed esiti [DA CONFERMARE] |
| Foto di laboratorio come prova | Bridge of Weir | Controllo qualità | `controllo_qualita/a_1.jpg` 345x476, `b_1.jpg` 369x247 | foto piccole: mostrate alla loro misura con didascalia, mai ingrandite; brief foto nuove nel LEGGIMI |
| Scheda pelle a etichetta e valore, chiusa da link di download | Sørensen, Kvadrat | pagine delle pelli (pieno fiore, semianilina, smerigliata, volanti, selleria, kit tagliati, ignifughe) | descrizioni del sottosito (es. "Full grain leather softened and milled...") | solo i campi noti; spessori, misure, rifinizioni [DA CONFERMARE] |
| Nota sui colori a schermo e invito a chiedere i campioni | Kvadrat | sotto le foto di pelle colorata | frase di servizio, non un dato | |
| Colonna "Documenti" in fondo pagina | Spinneybeck, barra strumenti Sørensen | fondo pagina e pagina Certificati | certificato qualità, `pdf/certificato_icec.pdf`, Policy aziendale, Accessibilità (già sul sito) | solo file esistenti |
| Referente commerciale con nome e contatto | Wollsdorf | Contatti | faggiana.luigi@conceriaeuropa.it | nome e ruolo [DA CONFERMARE] |
| Didascalie che dicono cosa si vede | Elmo | sotto ogni foto | nomi delle fasi, del laboratorio, del reparto | mai clienti o installazioni inventati |

Non importato: loghi dei clienti, carrello campioni, video d'apertura, carosello, corsivo d'accento, pillole colorate, tre icone in fila, sezioni in dissolvenza, testo grigio chiaro su grigio.

## 4. Accoppiate

Campione con testi e foto veri dell'azienda: `_prova/ricerca/campioni/accoppiate-1440.jpg` (sorgente `accoppiate.html`). Nel campione la foto di laboratorio è ingrandita oltre i suoi 345 px: va bene solo per il campione. Contrasti calcolati con la formula WCAG.

### A. "Banco prova": Hanken Grotesk + IBM Plex Mono (consigliata)

- **Caratteri:** Hanken Grotesk 300 per i titoli grandi (48-72 px a desktop), 400 per il testo (17 px), 600 per menu ed etichette in neretto delle schede. IBM Plex Mono 500 maiuscolo, 12-13 px, spaziatura 0,06-0,08 em, solo per etichette brevi: numeri delle fasi 01-06, sigle delle norme (F.A.R.-A, CRIB 5, ISO 9001), anni. Mai per i paragrafi.
- **Palette:** grigio prova #E8E8E6 (fasce; dal #E8E8E8 di Bridge of Weir e dal #EDEDE8 di Edelman), bianco #FFFFFF, inchiostro #121820, grigio testo #4B525C, blu Europa #1E3A5C (dall'insegna illuminata, foto `conceriaeuropa.jpg`: #1F446B, #0D2848), azzurro #C9D6E6 solo su blu. Il blu va su trattini, voce attiva, focus, etichette; nessun blocco blu grande. Il colore forte lo danno le foto delle pelli.

| Testo | Fondo | Contrasto |
|---|---|---|
| inchiostro #121820 | grigio prova #E8E8E6 | 14,5:1 |
| inchiostro #121820 | bianco | 17,8:1 |
| grigio testo #4B525C | grigio prova #E8E8E6 | 6,4:1 |
| grigio testo #4B525C | bianco | 7,9:1 |
| blu Europa #1E3A5C | grigio prova #E8E8E6 | 9,4:1 |
| blu Europa #1E3A5C | bianco | 11,6:1 |
| bianco | blu Europa #1E3A5C | 11,6:1 |
| azzurro #C9D6E6 | blu Europa #1E3A5C | 7,8:1 |

- **Da dove viene:** Bridge of Weir (grottesco leggero in grande, grigio #E8E8E8, trattino corto sotto il titolo, qui blu invece che rosso), Edelman (scheda con le prove in colonna), Elmo (etichetta e filetto), Sørensen (etichette in neretto). Il carattere monospaziato viene dai codici della mazzetta Spinneybeck e dalle sigle normative di Edelman: qui diventa la voce del laboratorio.
- **Perché per Conceria Europa:** i suoi fatti più forti sono tecnici (ciclo completo, laboratorio, ISO dal 1999, norme F.A.R. e Crib 5) e il blu è quello del suo marchio. Nessun concorrente usa questi caratteri.
- **Rischio:** grigio e monospaziato possono diventare freddi. Si bilancia con le foto a colori grandi (ocra, cuoio, petrolio) e tenendo il monospaziato a poche parole per sezione.

### B. "Mazzetta": Albert Sans, una sola famiglia

- **Caratteri:** Albert Sans 300 per i titoli, 400 per il testo, 600 per link ed etichette. Un grottesco geometrico di matrice scandinava, vicino al Neuzeit S di Kvadrat.
- **Palette:** bianco #FFFFFF, grigio fascia #F2F2F2 (lo stesso di Sørensen), nero #191919, grigio #5F5F5B, grigio chiaro #BDBDBA solo su nero. Nessun colore d'accento: il colore lo portano le pelli, come in Edelman, Kvadrat e Spinneybeck; il blu resta solo nel logo.

| Testo | Fondo | Contrasto |
|---|---|---|
| nero #191919 | bianco | 17,6:1 |
| grigio #5F5F5B | bianco | 6,4:1 |
| nero #191919 | grigio fascia #F2F2F2 | 15,7:1 |
| grigio #5F5F5B | grigio fascia #F2F2F2 | 5,7:1 |
| grigio chiaro #BDBDBA | nero #191919 | 9,3:1 |

- **Da dove viene:** Kvadrat (varianti in quadrati, interfaccia che si fa da parte), Sørensen (quadrati con etichetta sotto, #F2F2F2), Edelman (home di sole foto, biblioteca colori), Spinneybeck (codice sotto ogni campione).
- **Perché:** è l'impianto più vicino ai riferimenti per l'arredo, dove il cliente sceglie per colore e mano.
- **Rischio:** vive di molte foto di campioni che oggi non esistono (quattro pelli grandi più poche piccole): con poche celle la mazzetta sembra vuota. Servirebbe un servizio fotografico. Bianco e nero senza accento si avvicina anche all'aspetto di Benvegnù.

### C. "Cabina": Fira Sans + Fira Sans Condensed

- **Caratteri:** Fira Sans 200-300 per titoli molto grandi (72-96 px a desktop), 400 per il testo; Fira Sans Condensed 500 maiuscolo, 13-14 px, spaziatura 0,14 em, per nomi dei settori ed etichette. Fira discende da FF Meta, parente stretto del Kievit di Wollsdorf.
- **Palette:** blu notte #0E1A2B (l'insegna #0D2848 scurita), bianco, azzurro grigio #AFBCCD (testo secondario sul blu), cuoio #D98A4E (solo filetti e numeri grandi sul blu; schiarito dal cuoio di `home/3.jpg`, #B4500D), cuoio scuro #9A4A12 per i link su bianco, grigio #4A5361, fascia #E4E7EB.

| Testo | Fondo | Contrasto |
|---|---|---|
| bianco | blu notte #0E1A2B | 17,5:1 |
| azzurro grigio #AFBCCD | blu notte #0E1A2B | 9,1:1 |
| cuoio #D98A4E | blu notte #0E1A2B | 6,4:1 |
| blu notte #0E1A2B | bianco | 17,5:1 |
| grigio #4A5361 | bianco | 7,8:1 |
| cuoio scuro #9A4A12 | bianco | 6,2:1 |
| blu notte #0E1A2B | fascia #E4E7EB | 14,1:1 |
| grigio #4A5361 | fascia #E4E7EB | 6,3:1 |

- **Da dove viene:** Wollsdorf (grottesco sottilissimo in grande, settori in una parola con lineetta), il fondo pagina #182427 di Bridge of Weir, le aperture nere di Mastrotto e Pasubio; l'interno di una cabina o di un'auto è scuro.
- **Perché:** l'unica immagine a colori del marchio è l'insegna blu; il blu notte fa risaltare le pelli colorate e parla ad automotive e aviazione.
- **Rischio:** più di una o due fasce scure per pagina appesantiscono; Fira ha un'aria da software se usato piccolo; i titoli a 200 vanno tenuti sopra i 40 px.

### Raccomandazione

**A come base**: è l'unica che trasforma in forma i fatti veri dell'azienda (laboratorio, norme, ciclo completo) e che usa il suo blu. Da B si innesta la griglia di campioni solo nelle pagine delle pelli; da C una sola fascia blu notte, per Pelli speciali e Aviazione. La scelta definitiva si fa in 2.3, con il punteggio sui criteri del metodo.

**Perché niente graziato:** nel settore il graziato compare solo nei siti per l'arredo (Sørensen AT Realm nei titoli, Dani Tiempos Fine, Garrett IvyPresto, il logotipo di Edelman). Ma Dani, ad Arzignano, lo usa già; i riferimenti per auto e aerei (Bridge of Weir, Wollsdorf, Elmo, Pasubio) sono tutti senza grazie; e l'utente ha già bocciato il crema con il corsivo graziato. Quindi nessun graziato e nessun fondo crema.
