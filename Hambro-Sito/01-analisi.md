# Hambro: analisi per la nuova home

Sito: https://www.hambro.it (crawl e screenshot del 19/10/2026: home, 8 pagine di menu, galleria, 20 schede del catalogo). Fonti citate come URL + frase; le pagine del sito sono indicate con il percorso dopo `hambro.it/`.

## 1. In breve

- **Chi**: Hambro srl, via dell'Artigianato 30, Vigonovo (VE). L'idea è di Giorgio Gastaldello, "che opera nel settore della pelletteria dal 1979" (home). Il 1979 riguarda lui, non la srl: l'anno della società non è pubblico (sez. 8).
- **Cosa fa davvero**: è un fornitore di componenti per chi produce borse, cinture, scarpe e capi. Vende minuteria metallica in zama, ferro e ottone (moschettoni, anelli, fibbie, chiusure), cerniere, lacci in pelle e cuoio, nastri per tracolla, fodere, rinforzi per borse e pelli. In laboratorio fa due cose: ricopre fibbie e bottoni con il materiale del cliente e realizza semilavorati in pelle e tessuto (home, fibbie-e-bottoni-da-ricoprire).
- **Per chi**: pelletterie, calzaturifici e laboratori di abbigliamento. Il sito non nomina nessun cliente e nessuna maison. Il modulo "Ordina subito" accetta anche il "Privato".
- **Quanti**: dipendenti, metri quadri e fatturato non sono pubblici. La pagina Facebook ha "185 followers".
- **Il punto**: Hambro fa le parti che non si vedono, cioè l'interno, il rinforzo, la fibbia sotto la pelle. È questo che può reggere una home di alta gamma, non il catalogo da ferramenta di oggi.

## 2. Il sito di oggi

**Pagine**: Home, Accessori abbigliamento, Accessori Pelletterie, Accessori Calzature, Gamma pelli Rappresentanze, Fibbie e Bottoni da ricoprire, Articoli Nuovi, Catalogo prodotti (20 categorie, una scheda ciascuna), Contatti. Nella sitemap c'è anche `galleria`, che è vuota.

**Testi veri essenziali (verbatim)**:
- Home (h1 "Hambro srl"):
  - "Da sempre è specializzata nella creazione e commercializzazione di articoli metallici, rinforzi ed interni per la produzione di borse, cinture, calzature e abbigliamento."
  - "Il personale specializzato offre la possibilità di creare articoli personalizzati su richiesta del cliente."
  - "il nostro laboratorio attrezzato, è in grado di realizzare componenti semilavorati in pelle e tessuto"
  - "accessori in legno e bambù,accessori di plastica e metallo nichel free , accessori con strass"
  - "Gli articoli presenti in questo sito, sono una parte di quello che è disponibile"
- Accessori abbigliamento:
  - "Realizziamo laccio in pelle: tubolare,piatto, cucito, striscie a taglio vivo da mm2 a mm60, su richiesta anche a campione"
  - "Tessuto in alcantara h.1.40 vari colori"
- Accessori Pelletterie: "un vasto assortimento di nastri per tracolla o cinture, in cotone e poliestere da mm20-25-30-40-50".
- Accessori Calzature: "Laccio tubolare: corda cerata, elastico, pelle mm2-3-4". Didascalie: "OCCHIELLI+RIVETTI", "LAMPO PLASTICA+METALLO", "FIBBIE DOPPIE".
- Fibbie e bottoni: "REALIZZIAMO FIBBIE E BOTTONI RICOPERTI, ANCHE CON VOSTRO MATERIALE, SIA TESSUTO CHE PELLE". Misure delle fibbie da ricoprire: mm40, mm50, mm60.
- Gamma pelli Rappresentanze: "Siamo rappresentanti della Satab, con nastri" (organza, nastro vichy).
- Catalogo, testi delle schede:
  - minuteria: "MATERIALE ZAMA", "MATERIALE FERRO-ZAMA", "MATERIALE ZAMA-FERRO-OTTONE", "E' POSSIBILE SU ORDINAZIONE AVERE VARIE FINITURE";
  - pelli: "diversi tipi di pelle (agnello, montone, nappe, vitello) di diverse metrature e in tutti i colori possibili!";
  - rinforzi: "scheletri, pelli, salpe e rinforzi, con cui creare la vostra borsa nei minimi dettagli";
  - lavorazioni particolari: "dal camouflage a temi come il floreale o la stampa cocco";
  - altre categorie: "Occasioni Macchine", "Nostre creazioni" (orecchini in pelle).
- Orari: "Lunedì-Giovedì mattina dalle 08:00 alle 12:00 pomeriggio dalle 13:30 alle 17:30", "Venerdì ... pomeriggio CHIUSO".
- Sul sito non ci sono numeri, certificazioni né un elenco di macchine.

**Tecnologia**:
- CMS chiuso "Sito Internet Professionale" di Campadello Design, su PHP 8.2, nginx e Plesk.
- Bootstrap 5.3.3, jQuery 3.7.1, slider slick, lightbox, Font Awesome 6.6.
- Font: Economica per il menu, Poppins per il testo.
- Banner cookie, widget di accessibilità e reCAPTCHA sono di Campadello. Il sito si installa come web app (manifest con `theme_color` #003366).
- Meta description e og:description sono vuote. Il logo è un JPEG di 175x98.

**Problemi a 1440** (`_prova/attuale/home-1440.png`, pezzi in `p1440/`):
- La linguetta blu della voce attiva "HOME" copre metà del logo.
- Il menu ha 8 voci in un condensato grigio piccolo.
- Lo slider è largo 1140 px ma viene stirato a 1440, quindi è morbido. La terza slide è un collage scontornato.
- Al posto di un claim c'è "Hambro srl" in una fascia blu, e il titolo più grande della pagina è "SCARICA LA NOSTRA WEB APP".
- Il testo è giustificato a tutta larghezza.
- Seguono tre foto da telefono (pelli colorate, catene fluo, pelle metallizzata) senza didascalia.
- Il riquadro "nuovissimo e-shop" non porta a nessun e-shop.
- Il banner dei cookie copre metà della prima schermata.
- Scheda prodotto (`cat-1440.png`): foto da 400x300 su un fondo sfumato grigio, poi un modulo d'ordine con il prezzo vuoto ("x = (iva esclusa)").

**Problemi a 390** (`home-390.png`, pezzi in `p390/`):
- Il popup "Installa la nostra WebApp" copre logo e menu, e il banner dei cookie copre il testo.
- Il testo giustificato lascia buchi.
- Le foto arrivano a tutta larghezza una dopo l'altra: la pagina è alta 3336 px.
- Non c'è scorrimento orizzontale.

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Hambro srl | piede di ogni pagina di hambro.it: "Hambro srl" |
| P.IVA | 00967020280 | piede: "P.IVA: 00967020280". La cifra di controllo è valida. Il codice d'ufficio 028 è Padova (è una mia lettura, sez. 8) |
| Indirizzo | via dell'Artigianato, 30, 30030 Vigonovo (Venezia) | `contatti`: "Indirizzo: via dell'Artigianato, 30, 30030 Vigonovo (Venezia)" |
| Telefono | 049 9802326 | `contatti`: "Telefono: 0499802326" |
| Altro numero | 049 9802330 | prontoimprese.it/impresa/vigonovo/pelli-e-pellami-produzione-e-commercio/hambro: "Il telefono di Hambro - S.R.L. è 0499802330". Un estratto di ricerca di paginegialle.it lo dà come fax, ma la pagina non si apre (403) |
| Email | commerciale@hambro.it | `contatti`: "E-mail: commerciale@hambro.it" |
| PEC | non trovata | |
| Anno | 1979, ma riferito al fondatore | home: "Gastaldello Giorgio che opera nel settore della pelletteria dal 1979" |
| Attività dichiarata | ingrosso pelli e produzione di accessori | coobiz.it/azienda/noventa-padovana-commercio-ingrosso/co3513433: "Commercio all'ingrosso di pelli ed affini pellame in genere ; lavorazione e produzione confezioni in genere e di accessori per l'abbigliamento sia per conto proprio che per terzi" |
| Altre sedi | Noventa Padovana | coobiz (stessa pagina): "Via Oltre Brenta 46 35027" e "Noventa Padovana (Padova) – Via Col di Lana, 1/5/9". Forse dati vecchi |
| Rappresentanze | Satab (nastri) | `gamma-pelli-rappresentanze`: "Siamo rappresentanti della Satab, con nastri" |
| Social | Facebook, 185 follower | facebook.com/profile.php?id=100057503796900: "Hambro srl, Vigonovo. 185 followers. Apparel & clothing" |
| Dipendenti, mq, fatturato, clienti | non trovati | reportaziende e informazione-aziende rispondono 429, ufficiocamerale e paginegialle 403 |

## 4. Materiale visivo

Ho scaricato 139 file (16 MB) in `assets/originali/`. L'inventario con misure, pagine, soggetto e voti (qualità / forza come apertura, da 1 a 10) è in `_prova/inventario-immagini.json`; i fogli provino sono in `_prova/fogli/`. Non ci sono video. Il logo esiste solo come JPEG di 175x98 (scritta marrone in cornice).

| Gruppo | Quanti | Misure | Qualità | Apertura | Giudizio |
|---|---|---|---|---|---|
| Slider: rivetti, occhielli e il bottone "MADE IN ITALY" su nero lucido (`20180717b6cd…`) | 1 | 1140x475 | 6 | 6 | la migliore, ma piccola. Sembra una foto di un produttore di minuteria |
| Slider: minuteria dorata su pelle stampa cocco (`20180830650…`) | 1 | 1140x475 | 6 | 5 | luce da studio, composizione rigida da catalogo |
| Fibbie in ottone e brunite in fila su nero (`20180720bcc8…`) | 1 | 524x524 | 6 | 5 | bella idea, risoluzione inservibile per un'apertura |
| Slider: collage scontornato con ombre finte | 1 | 1140x475 | 3 | 1 | da clip-art |
| Scontornati del catalogo su bianco (fibbie, moschettoni, chiusure) | 64 | 400x300 e 345x259 | 4 | 1 | puliti e coerenti ma minuscoli: vanno bene come miniature di griglia, non oltre |
| Foto da telefono grandi: bobine di laccio, cordoncino, juta, nastri | 7 | da 1838 a 1920 px di larghezza | 3-4 | 2-3 | luce al neon, scaffale di metallo sullo sfondo, rumore e nitidezza artificiale da telefono |
| Foto da telefono medie: pelli colorate, pelle metallizzata blu e grigia, catene fluo | 7 | 768-1024 | 3-5 | 1-3 | la pelle metallizzata (5/3) ha una grana vera, le altre sono istantanee |
| Foto piccole: orecchini su tovaglia a pois, macchine usate, fodere, cartelle colori, collage di minuterie | 45 | da 300x134 a 800x400 | 2-3 | 0-1 | da non usare |
| Scansioni del catalogo di terzi "ASTOR" | 10 | 1700x2338 e 291x400 | 2 | 0 | materiale non loro: da escludere |
| Logo | 2 | 175x98 | 2 | 0 | serve il vettoriale |

**Verdetto**: il materiale **non regge** una home di alta gamma. In media vale 3 su 10. Nessuna foto supera 1140 px con una qualità decente, e le tre migliori hanno l'aspetto di foto di catalogo di un fornitore (diritti da chiarire). Per la proposta servono le foto segnaposto della sez. 6. Per il sito vero serve una giornata di still life in macro (fibbie, finiture, bobine, "nuda e ricoperta") più un'ora in magazzino e in laboratorio.

## 5. Il soggetto visivo

**Cosa è bello da vedere, a un livello da rivista**:
- La fibbia e il moschettone in zama o ottone come piccola scultura. Le finiture una accanto all'altra (oro, nichel, brunito, ramato) raccontano la frase "E' POSSIBILE SU ORDINAZIONE AVERE VARIE FINITURE".
- La bobina di laccio piatto "a taglio vivo": la spirale mostra due colori, il fiore scuro e il taglio chiaro del cuoio. Si vede già nella loro foto `2020082819b5…`, ma è scattata male.
- Le misure come ornamento: mm2, mm4, mm20, mm40, mm60. Nastri e lacci in fila per larghezza sono una scala grafica già pronta.
- L'interno della borsa: scheletri, salpe e rinforzi, cioè quello che nessuno vede e che tiene in forma una borsa di lusso.

**Il dettaglio solo loro**: la fibbia da ricoprire, nuda (metallo grezzo) accanto alla stessa fibbia ricoperta con la pelle del cliente ("ANCHE CON VOSTRO MATERIALE"). È il prima e dopo del loro mestiere, e nessun fornitore di minuteria lo mostra.

**Direzione A, "Sotto la pelle" (scura, still life)**
- Idea visiva: una tavola di still life su nero. Un oggetto per schermata, quasi a grandezza reale, con la misura in mm e il materiale accanto come in una didascalia da museo. Il racconto va dal metallo, alla fibbia ricoperta, alla borsa finita.
- Immagini: macro su nero lucido o su grana nera, una sola luce radente, riflesso sul piano. La coppia "nuda e ricoperta" della stessa fibbia. Segnaposto: le foto Rodrigues su specchio, Compagnons, Karimov.
- Tipografia: una serif editoriale ad alto contrasto (es. Cormorant Garamond o Newsreader Display) per i titoli, più una mono (es. IBM Plex Mono) piccola e maiuscola per misure, materiali e codici.
- Colore: nero caldo #0E0D0B, ottone #B08D57, nichel #C9CCCF, carta #EDE8DF per i testi. Niente blu #003366.
- Gesto: un selettore di finitura (Oro, Nichel, Brunito, Ramato) cambia la foto della stessa fibbia al clic o al tocco, con un cambio netto e nessuna transizione.

**Direzione B, "Campionario" (chiara, archivio tecnico)**
- Idea visiva: la home come il cassetto di un campionario. È una griglia rigorosa delle 20 famiglie, ognuna con numero, materiale ("ZAMA", "FERRO-ZAMA-OTTONE") e misure, come un catalogo tecnico svizzero ma caldo.
- Immagini: scontornati rifotografati in scala reale su carta bianca con ombra dura di sole, più strisce di nastri e lacci in fila per larghezza e per colore. Segnaposto: Rodrigues su bianco, Juno Jo, Devon Chan, Tepavac.
- Tipografia: una grotesk neutra (es. Inter Tight o Schibsted Grotesk) con numeri tabellari grandi per le misure. Etichette maiuscole spaziate.
- Colore: carta #F4F1EA, inchiostro #161514, un solo accento cuoio #8A4B2A. Il colore pieno viene solo dai nastri veri.
- Gesto: un righello in millimetri. Toccando una misura (mm2 … mm60), una barra a schermo prende la larghezza reale del laccio o del nastro. In più, filtri per materiale che non ricaricano la pagina.

## 6. Immagini sostitutive

Ci sono 10 foto Unsplash in `assets/esterne/`, tutte a 2400 px. Su ogni pagina ho controllato la licenza ("Free to use under the Unsplash License", nessuna Unsplash+). URL, autori e licenza sono in `assets/CREDITI.md`. Sono segnaposto e il LEGGIMI lo dice; nessuna è generata dall'IA.
- A, apertura: Rodrigues, fibbia dorata su specchio (`FXVC26csSz4`). Altre per A: Rodrigues oro e nichel, Rodrigues nichel, Compagnons grana nera.
- B, apertura: Rodrigues, fibbie con borchie su bianco al sole (`2hWmYcG26E8`). Altre per B: Juno Jo nastri appesi, Devon Chan bobine di nastro.
- Comuni: Karimov cuoio, Cohen Berg mani sul cartamodello (il laboratorio), Tepavac corda avvolta (le bobine).
- Manca un'immagine del "ricoperto": la serve una foto vera di Hambro.

## 7. Riferimenti di alta gamma nel mestiere

Ho aperto i siti dal vivo il 19/10/2026. Le prime schermate sono in `_prova/riferimenti/<nome>-1440.png` e `-390.png`; i font sono letti dal codice e salvati in `<nome>.json`.

1. **Oerlikon Riri** (riri.com, cerniere e bottoni per il lusso).
   - Cosa lo rende di alta gamma: la prima schermata è un flat lay di cerniere e bottoni su carta color terracotta, con il prodotto protagonista e i colori veri. Sotto c'è la macro di un cursore su nero. Usa Work Sans 100/300 e il logo rosso come unico accento.
   - Da non riprendere: lo slider con una ventina di puntini, il testo dentro un riquadro grigio semitrasparente, il menu con i pallini rossi.
2. **Gruppo Mastrotto** (mastrotto.com, concia).
   - Cosa lo rende di alta gamma: nero pieno, un solo titolo enorme "Leather forward" in Silka 600, due righe di testo e un solo link sottolineato. A 390 la grana di pelle bordeaux occupa tutto lo schermo con il testo centrato. Il logo alterna peso light ("GRUPPO") e bold ("MASTROTTO").
   - Da non riprendere: il video di apertura, che a 1440 resta nero finché non carica, e il menu nascosto dietro un'icona a griglia.
3. **Horween Leather** (horween.com, concia dal 1905).
   - Cosa lo rende di alta gamma: una foto vera di lavoro a tutta larghezza (mano, utensile, cuoio, bottale), quasi monocroma. Le voci di menu sono maiuscole spaziate; i testi sono in Calluna (serif), le etichette in DIN Condensed. Sotto c'è "SINCE 1905." in corsivo.
   - Da non riprendere: la barra dei cookie grigia e il testo a 14 px grigio chiaro.
4. **Charles F Stead** (cfstead.com, scamosciati inglesi).
   - Cosa lo rende di alta gamma: una foto documentaria del capannone con le pelli gialle sui cavalletti, che fa vedere la fabbrica vera come lusso. Il titolo in Operetta (serif) da 56-60 px sta in basso a sinistra, i testi sono in sofia-pro; a 390 la composizione regge identica.
   - Da non riprendere: il menu ad hamburger anche su desktop.
5. **Bonaudo** (bonaudo.com, pelli per la moda, Milano 1923).
   - Cosa lo rende di alta gamma: molto bianco, una sola immagine editoriale in bianco e nero al centro, il logo color oro oliva con "MILANO 1923" e il rimando a Lineapelle in piccolo.
   - Da non riprendere: il carosello con le frecce, la foto di moda con modella (Hambro non avrà mai questo materiale) e il pulsante dell'audio.
6. **Galvanica Formelli** (galvanicaformelli.it, finiture per accessori e catene dei brand di moda: è lo stesso mestiere di Hambro).
   - Cosa lo rende di alta gamma: un video scuro di catene dorate a tutta larghezza e il logo in serif.
   - Da non riprendere: il maiuscolo Montserrat UltraLight centrato sul video (si legge male), il pulsante grigio "MORE INFO" e l'impianto da tema TheGem.

Scartati, con gli screenshot in `riferimenti/scartati/`:
- Lampo: immagine di repertorio datata.
- Pasubio: il contenuto è bloccato senza consenso ai cookie.
- Alcantara: il video resta nero.
- Lineapelle: grafica datata.
- Metalbottoni, Eurominuterie, Metal on Demand: impianti datati o vuoti.
- Tärnsjö: il video non è disponibile.
- Tanneries du Puy: è una pagina di e-shop.
- dani.it è in costruzione; ilcea.com è un dominio in vendita.

Questi riferimenti si sommano a Mobbin, non lo sostituiscono.

## 8. Da confermare

- L'anno di costituzione della srl e il legame con il "1979" del fondatore.
- La sede storica a Noventa Padovana (coobiz) e il codice IVA 028 (Padova): la mia lettura è che la società sia nata in provincia di Padova.
- Se il 049 9802330 è il fax.
- PEC, dipendenti, superficie, fatturato: non trovati.
- I clienti: nessuno è citato. Lavorano per maison o per terzisti?
- L'"e-shop" annunciato nel riquadro della web app: non l'ho trovato.
- Chi produce la minuteria e chi fa le finiture: "creazione e commercializzazione" non dice se c'è produzione interna.
- Le macchine del "laboratorio attrezzato", e se si possono fotografare.
- I diritti delle tre foto dello slider e dei 64 scontornati, che sembrano foto di produttore.
- Il rapporto con Astor: le 10 scansioni sono di un catalogo di terzi. È una rappresentanza come Satab?
- Il logo vettoriale.
- "Occasioni Macchine" e "Nostre creazioni" (orecchini): sono ancora attive?
