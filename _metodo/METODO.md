# Metodo: rifare il sito di un'azienda e proporglielo (dal caso Benvegnù)

Questo documento descrive come è stato fatto `BenvegnuSrl-Sito/` e come rifarlo, uguale, per un'altra azienda.
Chi lo legge deve consegnare una cartella `<NomeAzienda>-Sito/` con la stessa struttura e la stessa qualità.

Il riferimento da aprire sempre accanto a questo file è `BenvegnuSrl-Sito/`: i documenti, il generatore,
gli screenshot finali. Quando un punto qui è ambiguo, si guarda come è stato fatto lì.

## 1. Cosa si consegna

```
<NomeAzienda>-Sito/
  01-analisi-sito-attuale.md     pagine, testi reali verbatim, immagini usate, problemi tecnici misurati, dati aziendali
  02-competitor-e-riferimenti.md concorrenti reali + riferimenti premium reali, con cosa si riprende da ognuno
  03-mappa-pagine.md             pagine, sezioni per pagina, navigazione
  LEGGIMI.md                     cosa c'è, come importare, plugin, collaudo fatto, cosa confermare col cliente, foto da fare
  PROPOSTA.md                    osservazioni verificate sul sito attuale + bozza della PEC (non si invia: la manda l'utente)
  _sorgente/                     motore.py, build.py, contenuti.py, prepara_immagini.py (+ estrattori se servono)
  assets/originali/              immagini scaricate dal sito attuale, alla massima risoluzione disponibile
  assets/web/                    immagini ottimizzate per il nuovo sito (generate da prepara_immagini.py)
  elementor-json/                template Elementor (Formato A), generati da build.py
  html-fallback/                 HTML per sezione (Formato B), generati da build.py
  anteprima/                     pagine complete apribili con un doppio clic, generate da build.py
  plugin/                        testo del modulo Contact Form 7, redirect-301.csv se il sito ha URL vecchi da conservare
  screenshot/elementor/          NN-pagina-desktop|tablet|mobile.jpg presi dal WordPress di prova
  screenshot/fallback/           gli stessi presi dall'anteprima HTML
```

`_prova/` (build di prova e screenshot grezzi) è ignorata da git. Anche `assets/originali/` e le immagini di `assets/esterne/`
restano fuori dal repository (pesano decine di MB per azienda): si riscaricano dalle fonti elencate in `manifest.json`
e in 01. In git vanno `assets/web/` e tutto il resto, quindi `build.py` funziona anche da un clone pulito.

## 2. Le fasi

### 2.1 Analisi del sito attuale (01)
- Scarica tutte le pagine (sitemap, menu, link interni), i testi, le immagini alla risoluzione più alta trovata
  (guarda `srcset`, l'originale senza `-300x200`, gli sfondi CSS). Salva gli originali in `assets/originali/`.
- Copia i testi **verbatim**, con i refusi. Il nuovo sito usa le frasi dell'azienda, corrette, non frasi inventate.
- Misura i problemi, non giudicarli a occhio: tempo di caricamento, peso pagina, mobile rotto (screenshot a 390),
  HTTPS, cookie banner, privacy policy, dati societari mancanti in fondo pagina (P.IVA obbligatoria),
  link rotti, immagini sgranate, copyright fermo a un anno vecchio. Ogni problema con la prova (URL, screenshot, misura).
- Dati aziendali da fonti pubbliche: ragione sociale, P.IVA, indirizzo, telefono, email, orari, marchi trattati.
- Elenca gli URL vecchi: servono per `plugin/redirect-301.csv`.

### 2.2 Concorrenti e riferimenti premium, dal vivo (02)
- 3-6 **concorrenti reali** (stessa zona o stesso settore): cosa fanno meglio e peggio, con screenshot.
- 4-8 **riferimenti premium reali**: aziende vere del settore, o di settori vicini, con siti di livello alto.
  Apri i siti con Playwright, fai screenshot e ritagli dei pezzi che riprendi (`_prova/ricerca/`).
- Per ogni riferimento scrivi **cosa si riprende** (impianto, ritmo, un gesto preciso) e cosa no. Mai copiare.
- L'utente ha bocciato un tentativo "Atelier" crema + serif corsivo come "AI slop": i riferimenti devono essere
  coerenti col settore dell'azienda e le "accoppiate" (font, colori, foto) devono venire da siti veri del settore.
  Benvegnù (forniture per calzature, Vigonovo): Barlow Condensed + Barlow, nero, bianco, rosso cuoio del sito storico,
  filetti sottili, foto prodotto scontornate. Era giusto perché nasceva da Vibram, Valextra, Edward Green, Mastrotto.

### 2.3 Direzione e specifica
- Prima di scrivere codice: 2-3 proposte di direzione, punteggio su criteri espliciti (più bello e vivo di oggi,
  premium credibile e tracciabile ai riferimenti, uso onesto delle foto e della loro risoluzione, qualità mobile,
  costruibile in Elementor gratuito senza trucchi fragili, rispetto dei divieti). Si sceglie, si innesta il meglio
  delle altre, si scrive una specifica per sezione (misure, testi, comportamento). Esempio: la specifica della home di Benvegnù.
- Ogni sezione ha **un'idea e un gesto** (una striscia, una foto che esce dalla fascia, un titolo grande che morde la foto).
  Variare larghezza, asse, fondo e scala tra sezioni consecutive.

### 2.4 Costruzione
- Copia `BenvegnuSrl-Sito/_sorgente/` nella nuova cartella. **Non toccare la logica di `motore.py` e `build.py`**:
  - in `motore.py` cambia solo il prefisso delle classi: `sed -i 's/bvg-/<px>-/g' motore.py`;
  - in `contenuti.py` definisci `PREFISSO = '<px>'` (3 lettere) e `NOME_SITO = '<Nome>'`: `build.py` li legge;
  - riscrivi `contenuti.py` da zero per la nuova azienda, mantenendo il contratto che `build.py` usa:
    `TEMA`, `BASE_PREDEFINITA`, `BASE`, `imposta_base()`, `header()`, `footer()`, `PAGINE` (lista di dict con
    `slug` `NN-nome`, `titolo`, `sezioni` = funzione che ritorna `[(nome, nodo), ...]`, `titolo_seo`, `descrizione`).
  - `BASE_PREDEFINITA`: `https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/<Cartella>/assets/web/`.
  - adatta `prepara_immagini.py` alle immagini della nuova azienda (ritagli, dimensioni, loghi monocromi).
- `python3 _sorgente/build.py` deve chiudere con `ok:` e nessun problema (controlla trattini lunghi, parole vietate,
  link annidati, alt mancanti, chiavi non valide).

### 2.5 Collaudo in un WordPress locale (kit)
Ogni azienda ha il suo WordPress (Elementor 4.3.3 gratuito, Hello Elementor, Ultimate Addons for Elementor per
header/footer, Contact Form 7) su una porta sua. Il kit è in `scratchpad/kit/` (copia in `_metodo/kit/`).

```
K=<scratchpad>/kit
$K/nuovo-wp.sh <slug> <porta> <cartella>/assets/web        # crea e avvia il WordPress vuoto
SLUG=<slug> PORT=<porta> SRC=<cartella>/_sorgente PREFIX="<NOME_SITO>" MENU="chi-siamo,prodotti,contatti" \
  PAGINE="/:01-home /chi-siamo/:02-chi-siamo" VIEWS="desktop tablet mobile" HTMLTOO=1 $K/ciclo.sh
$K/avvia-wp.sh <slug> <porta>                              # dopo un riavvio del container
$K/wpc.sh <scratchpad>/wp-<slug> <comando wp-cli>          # wp-cli su quell'istanza
$K/wpc.sh <scratchpad>/wp-<slug> eval-file $K/cf7.php "<titolo>" <modulo.txt> <email>   # modulo di contatto
python3 $K/slice.py <png> 1600 1440 <outdir>               # taglia uno screenshot lungo per guardarlo a pezzi
node $K/controlla.mjs <porta> "/:01-home /chi-siamo/:02-chi-siamo"   # sbordamenti, immagini rotte o ingrandite, link, a 4 larghezze
python3 $K/esporta.py <cartella-sito>                      # _prova/shots/*.png -> screenshot/elementor|fallback/*.jpg
```
Una striscia a scorrimento orizzontale va marcata con `data-scorre` (o scroll-snap): `shoot.mjs` allora fotografa
con un viewport alto invece della cattura a pagina intera, che la farebbe scattare.
`ciclo.sh` fa: build di prova, import dei template, pagine, header/footer/menu, screenshot in `_prova/shots/`.
Le pagine si chiamano come lo slug senza numero (`02-chi-siamo` diventa `/chi-siamo/`).

Controlli obbligatori a 390, 768, 1024 e 1440 (Elementor e fallback):
- `document.documentElement.scrollWidth == innerWidth` (nessuno scorrimento orizzontale) su ogni pagina;
- nessuna immagine segnaposto o rotta, nessun testo che va a capo male (numeri di telefono, orari, prezzi);
- header: menu su una riga a desktop, hamburger funzionante a mobile, voce attiva;
- guarda **davvero** ogni screenshot a pezzi (slice.py), non solo i numeri.

### 2.6 Revisione indipendente e correzioni
Una revisione separata, da chi non ha costruito, a lenti: difetti desktop, difetti responsive, fedeltà dei testi
(niente inventato, tutto tracciabile a 01), interazione e robustezza (tastiera, focus, JS spento, riduzione movimento),
divieti. Ogni rilievo con prova (screenshot, selettore, misura). Si correggono i confermati, si rigenera, si rifanno
gli screenshot finali in `screenshot/`.

### 2.7 Proposta (PROPOSTA.md)
- 4-6 osservazioni sul sito attuale, **verificate e misurabili**, scritte con rispetto (niente "il vostro sito è terribile").
- Cosa contiene il nuovo sito, in concreto.
- Bozza di PEC commerciale B2B: breve, firmata dall'utente (Evox Consulting), con la possibilità di vedere la demo
  e la frase per non ricevere altre comunicazioni. Mai inviata da noi.

## 3. Divieti (tutti i siti, sempre)
- gradiente viola-blu; testo hero in gradiente; emoji nei titoli; Inter ovunque;
- card con bordo sinistro colorato; glassmorphism; dark mode a basso contrasto;
- tre box con icona in fila; badge sopra il titolo; icone Lucide ovunque; componenti shadcn non toccati;
- sezioni che compaiono in dissolvenza allo scroll; fascio che segue il cursore; bottoni che sbiadiscono all'hover
  (l'hover cambia colore pieno, mai opacità);
- spaziature incoerenti (una sola scala, `SPAZI` in motore.py); trattini lunghi (U+2014) da nessuna parte;
- copy generico (`PAROLE_VIETATE` in build.py: eccellenza, passione, a 360, leader, know-how, mission...);
- corsivo serif per le parole d'accento.

E inoltre:
- niente referenze, recensioni, numeri, anni, certificazioni o clienti inventati. Se un dato non è pubblico, non c'è,
  oppure è un segnaposto dichiarato nel LEGGIMI tra le cose da confermare;
- niente foto stock spacciate per l'azienda. Se mancano foto buone, si costruisce il design su ciò che c'è
  (prodotti, tipografia, mappa, colore) e nel LEGGIMI si scrive il brief delle foto da fare;
- niente contatti con l'azienda, niente pubblicazione: la demo resta locale (o su un sottodominio privato con noindex
  se l'utente lo chiede).

## 4. Lezioni tecniche (costate tempo su Benvegnù)
- **Risoluzione delle foto**: mai mostrare un'immagine più grande della sua dimensione nativa (controlla a 1440 e su retina).
  Ritaglia per breakpoint invece di ingrandire.
- **Link annidati**: un contenitore-link non può contenere altri link (il browser chiude il primo `<a>` e la griglia
  si rompe). `build.py` lo controlla.
- **Larghezze in Elementor**: `width_mobile` non eredita; imposta sempre le tre larghezze. Griglie: la somma delle
  larghezze + gap deve stare sotto il 100% (Benvegnù: 4 colonne 23.59%, 2 colonne su tablet 48.5% non 49%).
  `flex_wrap` esplicito. Contenitori a larghezza fissa: `_flex_size none`.
- **CSS nel nodo RAW**: è un foglio di stile, non una classe. Classi e CSS di sezione vanno nel nodo `css=`.
- **Sfondi**: le sezioni con immagine di sfondo hanno la classe `e-no-lazyload`, altrimenti a volte restano vuote.
- **Tema Hello**: colora `a` e `button` in rosa (#c36). Ogni selettore personalizzato va dentro la classe della sezione,
  con colori espliciti per riposo, hover, focus e disabilitato.
- **Ultimate Addons**: il menu va a capo e il sottomenu esce dalla pagina: `nowrap` sulle voci e `overflow-x:clip` sulla testata.
- **Testi**: `text-wrap:balance` sui titoli, `pretty` sui paragrafi; spazi indivisibili nei telefoni; word joiner (U+2060)
  negli intervalli orari; margine 0 sull'ultimo paragrafo degli editor di testo.
- **Fallback HTML**: deve essere identico all'Elementor a ogni breakpoint. Controllalo con gli stessi screenshot
  (`HTMLTOO=1`). Bug già visti: margini dei titoli azzerati, specificità delle larghezze, card che si restringono.
- **Elementi dinamici** (striscia scorrevole, ecc.): un solo widget HTML con markup, `<style>` scoped e `<script>`,
  identico nel fallback. Scorrimento nativo con scroll-snap, frecce che si disabilitano agli estremi, tastiera,
  `prefers-reduced-motion`, controlli nascosti senza JS. Niente autoplay, niente librerie.
- **Screenshot**: lo screenshot a pagina intera di Chrome fa scorrere le strisce e svuota gli iframe: `shoot.mjs`
  usa immagini caricate subito e un viewport alto. "Immagini non tutte caricate" su una striscia lazy è un artefatto.
- **Proxy**: la porta del proxy cambia; usa sempre `$HTTPS_PROXY`. Il WordPress di prova prende le immagini da
  `http://127.0.0.1:<porta>/assets/` (link simbolico), quindi non serve la rete per importare.
- **Container**: un riavvio ferma i server PHP. Rilancia `avvia-wp.sh`.
