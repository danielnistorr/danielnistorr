# evap.it: com'è fatto il sito (rilievo dell'11/11/2026)

Fonti: HTML e CSS scaricati da https://evap.it (home, /servizi/, /chi-siamo/, /life-struvite/, /contattaci/), misure prese con Playwright sulle pagine vere a 1440 e a 390 px, libreria media via `/wp-json/wp/v2/media`. Schermate intere in `riferimenti/` (`<pagina>-1440.jpg`, `<pagina>-390.jpg`).

## 1. Tecnologia

| Cosa | Valore | Da dove |
|---|---|---|
| WordPress | 7.1.4 | `<meta name="generator">` della home |
| Tema | Hello Elementor 3.4.4 | `/wp-content/themes/hello-elementor/style.css` |
| Elementor | 3.31.5 (file JS 3.31.0) | generator della home: `Elementor 3.31.5; features: e_font_icon_svg, additional_custom_breakpoints, e_element_cache; settings: css_print_method-external, google_font-enabled, font_display-swap` |
| **Elementor Pro** | **sì, 3.28.0** | script `elementor-pro-frontend`, widget Pro `theme-site-logo` nel piede, banner di `/wp-content/plugins/elementor-pro/assets/js/frontend.min.js` |
| Testata e piede | modelli di **Sina Extension for Elementor** (`sina-ext-template` 95 = testata, 108 = piede) | `data-elementor-post-type` |
| Widget aggiuntivi | **Jeg Elementor Kit** (JKit): menu, bottoni, riquadri con icona, numeri, testimonianze, squadra | `data-widget_type="jkit_*"` |
| Modulo contatti | **MetForm**, modulo id 135 sulla pagina Contattaci | `data-form-id="135"` |
| Altro | LiteSpeed Cache (unisce CSS e JS), Pressidium Cookie Consent | nomi dei file e classi del `<body>` |
| Modello di pagina | **Elementor a tutta larghezza** (`elementor_header_footer`) su tutte e cinque le pagine | classe `page-template-elementor_header_footer` |
| Kit attivo | `elementor-kit-11` | classe del `<body>`, CSS `/wp-content/uploads/elementor/css/post-11.css` |
| Impostazioni Elementor | colori e caratteri predefiniti **disattivati** (nessuna regola "predefinita" per i widget nel CSS delle pagine) | assenza di `.elementor-widget-heading .elementor-heading-title{...primary...}` nei `post-*.css` |
| Punti di rottura | tablet fino a 1024 px, telefono fino a 767 px (quelli standard) | `@media` del kit |

### Problema trovato: il carattere del sito non si carica

Il kit usa **Plus Jakarta Sans** per tutto, e Elementor lo ospita in locale (`elementor-gf-local-plusjakartasans`). Però:
- il file unito da LiteSpeed per quel foglio (`/wp-content/litespeed/css/0bd5025686e8410ac6e866115ae61a14.css`) è **vuoto** (0 byte);
- il foglio originale (`/wp-content/uploads/elementor/google-fonts/css/plusjakartasans.css`) punta ai file del carattere sul **vecchio dominio di prova** `heuristic-keldysh.195-20-235-104.plesk.page`, che ha un certificato non valido.

Risultato: oggi **tutto il sito si vede nel carattere di riserva del sistema** (Arial su Windows, Helvetica su Mac): lo si nota nelle schermate in `riferimenti/`. I file giusti esistono già su evap.it (`/wp-content/uploads/elementor/google-fonts/fonts/plusjakartasans-*.woff2`). Rimedio, da fare sul sito e non nella pagina: Elementor > Strumenti > "Rigenera file e dati" (e, se resta, ricaricare il carattere in Elementor > Impostazioni > Avanzate "Carica Google Fonts in locale"), poi LiteSpeed Cache > "Svuota tutto". La pagina MVR CARE usa le variabili del kit, quindi segue il sito in entrambi i casi. L'anteprima mostra il carattere del kit; con `anteprima/index.html?carattere=sito` mostra come appare oggi (schermata `screenshot/anteprima-1440-come-oggi-senza-carattere.jpg`).

Altre cose notate, fuori dal compito: le pagine non hanno un `<h1>` (il titolo del banner è un `<h2>`; LIFE Struvite ne ha uno dentro il widget HTML), la lingua del documento è `en-US`, la pagina LIFE Struvite ha un secondo `<title>` dentro il widget HTML. Nessun plugin SEO: il titolo delle pagine è quello di WordPress ("Servizi – EVAP") e non c'è meta description.

## 2. Colori globali (kit 11)

| Id globale | Valore | Uso sul sito |
|---|---|---|
| `primary` | `#1D365C` | blu scuro: titoli, fasce scure, velatura dei banner, passaggio dei bottoni |
| `secondary` | `#3798E2` | azzurro: bottoni, filetti evidenziati, quadratini |
| `text` | `#4F5D72` | testo, piede |
| `accent` | `#FFFFFF` | bianco: testi su fondo scuro, cornici |
| `386aba7` | `#DBDBDB` | testo chiaro su blu, briciole di pane |
| `f59e185` | `#1D365C4D` | blu al 30% |
| `ce755b7` | `#FFFFFF1A` | bianco al 10% |
| `50cd0e7` | `#FFFFFF36` | bianco al 21%: filetti su fondo blu |
| `0012040` | `#1D365C40` | blu al 25%: bordi delle schede, campi dei moduli |
| `9f5d5c9` | `#F5F6F8` | grigio chiarissimo: schede alternate |
| `c871ce0` | `#224C8B` | blu medio: schede dentro le fasce scure |
| `1a118d4` | `#1D365CB8` | blu al 72% |

Contrasti (WCAG): bianco su `#3798E2` 3,1:1 (sotto il 4,5 richiesto per testo normale: è la scelta di tutti i bottoni del sito, la pagina nuova la mantiene per coerenza e la segnalo); blu `#1D365C` su `#3798E2` 3,9:1; testo `#4F5D72` su bianco 6,7:1; bianco su `#1D365C` 12,1:1; `#DBDBDB` su `#1D365C` 8,7:1.

## 3. Caratteri globali (tutti Plus Jakarta Sans)

| Id | Desktop / tablet / telefono | Peso | Interlinea | Maiuscole | Dove si vede |
|---|---|---|---|---|---|
| `primary` | 80 / 60 / 40 px | 600 | 1 / 1,1 / 1,2 em, spaziatura -1 px | capitalize | (titolo grande; la home usa 70 px personalizzato) |
| `secondary` | 47 / 40 / 34 | 600 | 1,2 | capitalize | H1 del kit, titoli di sezione delle pagine di servizio |
| `text` | 16 | 400 | 1,5 | no | testo, H6 |
| `accent` | 25 / 23 / 22 | 500 | 1,2 | capitalize | H4, numero di telefono nella colonna laterale |
| `58b3754` | 18 | 500 | 1,5, spazio tra parole 1 px | no | testi introduttivi, etichette sopra i titoli |
| `0b4304e` | 17 | 500 | 1,2 | capitalize | H5, bottone della testata |
| `264998f` | 16 | 500 | 1,2 | capitalize | **bottoni del kit** e voci di menu |
| `c959aeb` | 21 | 500 | 1,2 | no | titoli delle schede, titoli del piede |
| `ffbed2e` | 25 / 23 / 22 | 500 | 1,4 | no | H3 |
| `eac7479` | 25 / 23 / 22 | 400 | 1,5 | no | testo grande |
| `d438253` | 16 | 600 | 1,2 | no | etichette in grassetto |
| `9de02ed` | 54 / 45 / 34 | 600 | 1,2 | no | titolo dei banner delle pagine interne |
| `6cd74bd` | 38 / 35 / 30 | 600 | 1,2 | capitalize | H2 del kit, sottotitoli di sezione ("Benefici Dei Nostri Servizi") |
| `e6a7963` | 150 / 100 / 70 | 600 | 1 | capitalize | numeri giganti |

Titoli del kit: H1 = `secondary`, H2 = `6cd74bd`, H3 = `ffbed2e`, H4 = `accent`, H5 = `0b4304e`, H6 = `text`, tutti in `primary`. Link in `primary`. Molti titoli della home sono impostati a mano con le stesse misure ma **senza maiuscole iniziali** (per esempio "Scopri perché EVAP" 47/40/34 px, 600, `text-transform: none`): la pagina nuova fa lo stesso per gli H2, perché "Un Evaporatore Efficiente È Il Cuore..." in italiano non si scrive.

## 4. Contenitori, spaziature, bottoni, raggi, ombre

- **Larghezza del kit**: 1140 px (1024 tablet, 767 telefono), spazio tra widget 20 px. Le pagine però usano quasi sempre **1290 px di contenuto** (contenitore "boxed" a 1290), centrato: a 1440 il testo parte da x = 75.
- **Margine laterale sul telefono**: 20 px.
- **Distanza tra le sezioni**: 100 px nelle pagine di servizio (margine sopra e sotto del contenitore principale); la home usa 150 px sopra la fascia blu e circa 100 tra le altre.
- **Colonne**: 60 px tra le colonne (Servizi: 34% + 66%); 30-40 px tra le schede.
- **Cornice bianca**: le fasce a tutta pagina (banner con foto, fascia blu della home) hanno un **bordo bianco di 20 px** (10 px sul telefono): la foto non tocca mai i bordi della finestra. È il segno più riconoscibile del sito.
- **Bottoni**: azzurro `#3798E2`, testo bianco, 16 px peso 500 con maiuscole iniziali (`264998f`), 15/30 px di margine interno, **spigoli vivi**, nessun bordo, nessuna ombra. Quello della testata è 17 px. Al passaggio (JKit) diventano bianchi con testo blu e si rimpiccioliscono al 90%; quelli nativi del kit diventano blu scuro con testo bianco. I bottoni nativi della colonna laterale di Servizi sono 16 px peso 600.
- **Raggi**: 0 ovunque (bottoni, schede, campi). Fa eccezione solo il widget HTML di LIFE Struvite (4 px).
- **Ombre**: nessuna, tranne il modulo MetForm (ombra larga e chiara intorno al modulo e alone azzurro sul bottone "Invia messaggio").
- **Bordi delle schede**: 1 px `#1D365C40`; le schede "evidenziate" alternate hanno fondo `#F5F6F8` e **filetto azzurro di 3 px sotto**.
- **Movimento**: la home ha sfondi a scorrimento con effetto Ken Burns e passaggio in dissolvenza; il bottone JKit si rimpicciolisce al passaggio; la colonna laterale di Servizi resta ferma scorrendo (JKit sticky, solo desktop). Nessuna animazione d'ingresso delle sezioni.
- **Etichette sopra i titoli**: il sito le usa ("Cosa facciamo", "Perché scegliere EVAP", "Come lavoriamo", "Chi siamo noi di EVAP", "I nostri valori", "Il nostro team", "Contattaci"), in 18 px `58b3754`. La pagina nuova **non** le usa: è un vincolo del committente.

## 5. Testata

- Contenitore a tutta larghezza, fondo bianco, margine interno 10/50 px (30 tablet, 20/30 telefono), alto 80 px (100 sul telefono).
- **Si sovrappone alla prima sezione** della pagina: margine sotto di -115 px (-78 tablet, -65 telefono). Così il banner con la cornice bianca parte sotto la testata.
- Sinistra: logo rotondo (stella grigia e "evap" blu) alto 60 px, collegato a evap.it.
- Centro: menu JKit "Homepage, Servizi, Progetti ▾ (Life Struvite), Chi siamo, Contattaci", 16 px peso 500, nero, 15 px di margine; sottomenu 14 px, largo almeno 220 px.
- Destra: bottone "Contattaci" (JKit) azzurro, 17 px.
- Telefono: logo largo 145 px e bottone quadrato azzurro con le tre righe bianche; il menu esce da sinistra su fondo `#f7f7f7`.

## 6. Piede

- Filetto superiore di 2 px `#4F5D72`, fondo bianco, tre colonne uguali separate da filetti verticali di 2 px `#4F5D72`.
- Colonna 1: logo 120 px, "EVAPporating wastewater into pure water", icone Instagram e Facebook (28 px, colore testo).
- Colonna 2 "Contatti": Via Bernarde, 15 - 36047 Montegaldella (VI) Italy; Via Mantegna, 6 - 36040 Grisignano di Zocco (VI) Italy; Tel. +39 0444 1276355; Email: tecnico2@evap.it.
- Colonna 3 "Support": Privacy Policy, Cookie Policy, Legal, Sitemap.
- Titoli 21 px peso 500 colore testo; sul telefono le colonne vanno in fila con filetti orizzontali.

## 7. Come sono impaginate le pagine

**Schema comune delle pagine interne** (Servizi, Chi siamo, Contattaci, LIFE Struvite): banner con foto, velatura `primary` al 50%, cornice bianca di 20 px, margine interno 200 px sopra e 100 sotto (alto 489 px a 1440, 395 sul telefono), titolo centrato bianco 54 px (`9de02ed`) e sotto le briciole "Home → Pagina" in `#DBDBDB` 16 px. Poi il contenuto a 1290 px, 100 px più in basso.

**Servizi** (`riferimenti/servizi-*.jpg`): due colonne, 34% a sinistra e 66% a destra, 60 px tra le due.
- A sinistra, ferma scorrendo: riquadro bordato "Altri servizi" con quattro bottoni azzurri a tutta larghezza (Evaporatori Sottovuoto, Evaporatori Raschiati, Cristallizzatori, Altri Impianti E Service) che cambiano il contenuto a destra (schede nascoste); sotto, riquadro blu `primary` con icona, "Vorresti maggiori informazioni al riguardo?", filetto, telefono 25 px, email, bottone "Contattaci".
- A destra: titolo 47 px, due righe di testo, foto larga 831 px, "Benefici Dei Nostri Servizi" 38 px, testo, quattro riquadri JKit in griglia 2 x 2 (bordo 1 px, icona quadrata 45 px, titolo 21 px, testo 16 px).
- Telefono: la colonna laterale va **in fondo** (ordine invertito).

**LIFE Struvite** (`riferimenti/life-struvite-*.jpg`): banner come le altre; poi un unico **widget HTML** con stili propri, che non usano il kit: carattere Roboto (che a sua volta non viene caricato), colori `#308dde` e `#1b2f52` (vicini ma diversi da quelli del kit), spigoli a 4 px, larghezza 1140, colonna laterale di 300 px con l'indice "In questa pagina" e il riquadro blu dei contatti, titoli 44 e 31 px peso 800, schede con icone, passi numerati in quadratini azzurri, elenco con quadratini, schede dei partner. È la pagina più recente (agosto 2026) e la più "curata", ma è fuori dal sistema del kit: la pagina MVR CARE **non** la prende a modello per i valori, solo per l'idea di indice e di riquadro dei contatti.

**Home** (`riferimenti/home-*.jpg`): apertura a tutta pagina con sfondi a scorrimento, titolo bianco 70 px allineato a sinistra con filetto, testo 18 px, bottone; numeri bianchi sovrapposti al bordo basso; "Scopri perché EVAP" con foto a sinistra e testo a destra; quattro schede in fila alternate (bordate / grigie con filetto azzurro); fascia blu con cornice bianca, titolo a sinistra e schede blu medio a destra; foto larga; "Gli step di produzione" con passi su una linea verticale e quadratini.

**Chi siamo**: banner; titolo 47 px con due foto e due blocchi "La nostra Vision / Mission"; due schede alternate; la squadra.

**Contattaci**: banner; a sinistra titolo, testo e tre riquadri JKit (indirizzi, telefono, email), più i due PDF dell'informativa; a destra il modulo MetForm (Nome, Cognome, Email, Argomento, Domande/commenti, consenso, "Invia messaggio"); sotto le due mappe Google.

## 8. Cosa ne prende la pagina MVR CARE

- Tutti i colori e i caratteri dal kit (con `__globals__` nel modello), bottoni identici a quelli del kit, spigoli vivi, nessuna ombra.
- Contenuto a 1290 px, 100 px tra le sezioni, 60 px tra le colonne, margine di 20 px sul telefono.
- Cornice bianca di 20 px (10 sul telefono) intorno alle due fasce piene: l'apertura con la foto velata di blu (come i banner) e la fascia blu delle attività (come quella della home).
- Foto a sinistra e testo a destra come "Scopri perché EVAP"; quadratini azzurri come gli "step" della home; schede alternate bianco / `#F5F6F8` con il filetto azzurro di 3 px come le schede della home e di Chi siamo; telefono, email e bottone come il riquadro blu della colonna di Servizi.
- Il gradino in più: titolo d'apertura allineato a sinistra e più grande (80 px, `primary`) invece del titolo centrato a 54 px, una tabella di confronto vera al posto di due schede, testi corti tenuti dal ritmo dei filetti invece che da icone.
