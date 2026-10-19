# Tre Esse, home finale: "Registro delle opere" (dalla bozza B)

Il committente ha visto le due bozze e ha scelto la B. Questa versione sostituisce del tutto quella costruita prima sulla bozza A ("La tavola"), i cui script sono in `_prova/script/scartata-a/`. Della B restano l'idea, la prima schermata, il trattamento delle foto, il carattere e i colori; sono cambiati i dati, l'esecuzione, il telefono, la sezione Studio e i contatti.

File: `sito/index.html`, `sito/img/` (22 JPEG in più larghezze), `sito/fonts/` (Switzer e licenza). Si rifà tutto con `bash _prova/script/build_finale.sh`; controlli con `node _prova/script/finale_b_controlli.mjs file://.../sito/index.html <cartella>`.

## Idea

Un ufficio tecnico si racconta con quello che ha calcolato. In alto un impalcato in acciaio visto da sotto, in grigi chiari: il cielo e la neve diventano la carta della pagina e le pile a V si posano sul titolo. Sotto c'è il registro delle opere: un elenco tipografico (anno, opera, luogo, tonnellate o metri cubi) e nessuna griglia di miniature. Poche parole e i numeri veri del portfolio.

## Le prime due schermate

- **1440x900**: testata chiara (Tre Esse, Opere, Servizi, Studio, Contatti, telefono). Sotto, la foto a tutta larghezza alta 490 px che sfuma nella carta, senza didascalia. Poi "Ingegneria delle strutture" su una riga a 122 px in Switzer Light. In basso, a sinistra, la frase su cosa fanno e per chi; a destra tre opere con i loro numeri, senza anno (Edificio industriale, Emirati Arabi Uniti 8000 t; Grand Hotel Molino Stucky, Venezia 250.000 m³; Circuito e centro commerciale, Adria 700 t) e il link "Tutte le 34 opere del registro".
- **Seconda schermata a 1440**: il registro. A sinistra il titolo resta fermo durante lo scorrimento, con il contatore in rosso minio (14 ponti e passerelle); a destra i filtri e le righe, con il luogo di ogni ponte preso dal portfolio. Le 8 opere senza anno nelle fonti stanno in fondo sotto "Altre opere", senza colonna dell'anno.
- **390x844**: testata con Opere e telefono, poi la foto tagliata sul vertice della V (362 px). Il titolo va su due righe a 52 px, poi la frase e le prime righe del registro, tutto dentro gli 844 px. A 320 il menu tiene solo il telefono.

## Cosa è cambiato rispetto alla bozza B (giro precedente; l'ultima rifinitura è nel paragrafo seguente)

- Dati: ogni ponte ora ha il suo luogo, preso dal portfolio: Isonzo a Farra d'Isonzo (GO), Versa a Mariano del Friuli (GO), Pegognaga (Mantova), Po di Volano a Migliarino (FE), Tremonti di Sopra (PN), Sambughè (TV), Campocroce sull'A4 (TV), Formentin ad Abano Terme (PD), Komo a Kango (Gabon). Paesi indicati per Nizza, Riyad, Doha e San Pietroburgo. Tesa 105 resta tra le opere in acciaio (80 t). I conteggi dei filtri restano giusti: 14+9+3+4+3 = 33.
- Le due "Foto indicativa" in pagina sono state tolte, insieme a ogni didascalia sulle foto di repertorio: le note di lavorazione stanno nel LEGGIMI.
- Studio: prima accanto alla cupola di Adria c'era una fascia vuota. Ora in alto a sinistra ci sono il titolo e la dotazione dello studio come piccola tabella con filetti (Calcolo, Disegno, Rilievo, Acustica: i software e gli strumenti della pagina Presentazione), al posto del paragrafo in prosa. In basso, allineata al piede della foto, la didascalia con i due numeri del portfolio in grande: diametro 90 m, acciaio 700 t. I software di disegno sono passati dai servizi alla tabella, così non si ripetono. La cupola è al vivo sul bordo destro, larga al massimo 865 px, cioè la sua misura vera, mai ingrandita. È appena più chiara della bozza.
- Fascia dei controventi: il cielo ora coincide esattamente con la carta e i lati sfumano, così non si vede più l'orlo grigio della foto. Non supera mai i 1600 px veri (a 1920 resta di 1600 e il cielo continua nella carta).
- Contatti su carta e non più su fondo nero, con il telefono grande (108 px, cifre tabellari). Il nero resta solo nel piede con i dati societari, come vuole il committente: chiaro, e il nero solo dove serve.
- Telefono: sistemata la crenatura di Switzer a 17 px (con la resa predefinita Chromium a 1x spezzava "stat ici", "costrut tivi"; ora il testo usa `text-rendering: geometricPrecision`). Bottoni dei filtri alti 45 px. Menu ridotto a Opere e telefono.
- Pagina: 5171 px a 1440, prima 5669. A 390 è di 5487 px.
- Tolti il link "Privacy" che puntava a "#" e il PDF del portfolio (22 MB).

## Ultima rifinitura (dopo il giudizio cieco: 55 su 80)

Il committente ha scelto questa bozza: idea, prima schermata, trattamento delle foto, carattere e colori restano quelli. Cambiano esecuzione, dati e nitidezza.

- **Prima schermata**: la foto resta il segnaposto di Helsinki e il titolo resta "Ingegneria delle strutture". Il giudice chiedeva un'opera di Tre Esse (la tavola del Sarpi o una foto del Sarpi): la tavola è la bozza A, scartata dal committente, e le foto del Sarpi che esistono sono di notte e larghe 922 px, non reggono a tutta larghezza. La foto vera da scattare è descritta nel LEGGIMI, con la legenda da aggiungere.
- **Estratto senza anni**: le tre righe della prima schermata non mostrano più 2011, 2008 e 2006, che nel 2026 dicevano "studio fermo". Al posto del Sarpi, che non ha un numero, c'è il Molino Stucky con i suoi 250.000 m³: tutte e tre le righe hanno una misura. A 1920 l'estratto è largo al massimo 560 px, allineato al margine destro; sotto gli 860 px è largo quanto il paragrafo.
- **Crenatura dei filtri**: "Pont i", "Cement o", "Restaur o" venivano dal foglio di stile del browser, che sui bottoni rimette `text-rendering: auto`. Ora i bottoni ereditano la resa del testo (`text-rendering: inherit`) e le cifre tabellari. La resa `geometricPrecision` del corpo resta: senza, i paragrafi a 17 px del telefono si spezzano ("stat ici", "costrut tivi"), provato a 1x.
- **Registro**: 34 opere. Rochdale (2012) e Birley Fields (2013) sono due righe, come nel portfolio: niente più "2012" con il trattino. Centro direzionale Giotto con 2007 e Padova (portfolio), Centro commerciale Alimarket con Padova (sito). Le 8 opere senza anno sono in un blocco finale "Altre opere" senza colonna dell'anno; il titoletto si nasconde quando il filtro non mostra righe con l'anno (Project management). Conteggi: 14, 10, 3, 4, 3, 34.
- **Cupola di Adria**: intera (1155x865) e non più ritagliata a quadrato, larga al massimo 800 px: i 1155 px reali coprono 1,44 volte su schermo 2x (prima 1 volta). Una sfocatura minima toglie i blocchi JPEG e un contrasto locale ampio separa travi e lamiera; il cielo resta il colore della carta. La didascalia (nome, 90 m, 700 t) è un `figcaption` sotto la foto, allineato al suo bordo: nella colonna di sinistra non c'è più il buco tra tabella e didascalia.
- **Fascia dei controventi**: stessa foto Unsplash, scaricata a 3200 px (prima 1600). Ora è a tutta larghezza e alta 960 px a 1440, nitida anche su schermo 2x (fattore 0,9). Il cielo è riportato esattamente al colore della carta dopo la riduzione, così sui lati non si vede l'orlo.
- **Tablet**: tra 561 e 860 px l'apertura usa il taglio del telefono centrato sul vertice della V (anche a 1344 px), così a 768 le due pile restano simmetriche.
- Spaziatura tra le sezioni appena ridotta (da 124 a 110 px a 1440) e righe del registro di 2 px più basse.

## Caratteri e colori

- **Switzer** (Jérémie Hornus, Indian Type Foundry), da Fontshare. Pesi 300 (titoli, numeri grandi), 400 (testo), 500 (marchio, menu, h3, filtro attivo). I file woff2 sono quelli serviti da Fontshare, non modificati e serviti dalla pagina in `sito/fonts/`. Licenza: **ITF Free Font License 2.0** (`sito/fonts/FFL.txt`), che ammette l'uso commerciale e il self-hosting sul proprio sito e vieta di modificare o convertire i file (per questo non sono stati ridotti). L'attribuzione non è obbligatoria. Le cifre sono tabellari (`tabular-nums`), quindi anni, tonnellate e telefono si allineano senza monospazio. Una sola famiglia.
- Riferimenti: sbp (titolo grottesco sottilissimo e grande, "Wir sind Ingenieure") e Dissing+Weitling (foto da bordo a bordo e una riga sotto). Il registro come tabella tipografica viene dai cataloghi delle opere degli studi di ingegneria, non dalla moda.
- Colori: cemento chiaro #ECEBE7 (fondo e bianco delle foto), inchiostro #1A1C1E, acciaio #5F6870 per il testo secondario (4,8:1). Il rosso minio #C0502A è il colore dell'antiruggine: compare solo nel filo del filtro attivo, e il contatore usa #A8431F (5,05:1). Il piede ha fondo inchiostro con testo #C9CCCF.

## Interazione

Un solo gesto: i filtri del registro (Ponti e passerelle 14, Acciaio 10, Cemento armato 3, Restauro 4, Project management 3, Tutte 34). Sono bottoni con `aria-pressed` e funzionano con mouse, dito, Tab, Invio e spazio. Accorciano l'elenco senza ricaricare la pagina e aggiornano il contatore (`aria-live`). Il link "Tutte le 34 opere" della prima schermata porta al registro e lo apre su Tutte. Senza JavaScript si vedono tutte le righe. L'unica transizione dura 0,12 s, solo sul colore dei filtri. Niente dissolvenze allo scorrere, niente effetti che seguono il cursore.

## Foto, origine e licenza

Un solo trattamento per tutte (PIL): monocromo, ombre sollevate a grigio acciaio #3A3E42, luci portate al colore della carta. Ogni foto è in 3, 4 o 5 larghezze con srcset, in JPEG.

| In pagina | Origine | Licenza |
|---|---|---|
| Apertura | Jao Kop, unsplash.com/photos/ZovCK9PgffY (Helsinki) | Unsplash License, uso commerciale, attribuzione non richiesta. **Segnaposto**: non è un'opera di Tre Esse |
| Fascia | Jonathan Lim, unsplash.com/photos/0BvlhW4zthY (Vancouver), versione a 3200 px | Unsplash License, ricontrollata il 19/10/2026. **Segnaposto**: non è un'opera di Tre Esse |
| Studio | Cupola del circuito di Adria, ritaglio dal portfolio Tre Esse 2013 (1155x865, intero) | Materiale dell'azienda, uso da confermare |

L'unico file nuovo è la versione più grande della foto di Lim (stessa foto, stessa licenza). Nessuna immagine è generata. Le due foto Unsplash non compaiono in altre home della campagna (controllati tutti i `*-Sito/assets/CREDITI.md` il 19/10/2026). Le foto vere da scattare sono descritte nel LEGGIMI.

## Ispirazioni del committente (Pelletteria Graziella, Studio N19)

Le ho usate pochissimo, come già nella bozza. Tre Esse è un ufficio di ingegneria strutturale che lavora per imprese e carpenterie, non un marchio di moda o di lusso. Il registro giusto viene dagli studi di ingegneria (sbp, Dissing+Weitling), non dalla pelletteria. Di Graziella non ho preso niente: fondo nero, serif con parole in corsivo e foto di prodotto sono il tono sbagliato per chi calcola ponti. Di N19 ho preso solo due tratti: il titolo enorme in grottesco su fondo chiaro e il vuoto attorno.

## Controlli (ultima rifinitura, 19/10/2026)

- Scorrimento orizzontale: nessuno da 320 a 2560 px (passo 10/40).
- Altezza: 5109 px a 1440 (6379 con "Tutte" aperto), 5296 a 390, 5537 a 320, 5235 a 1920, 4393 a 1024, 5723 a 768.
- Prime schermate guardate a 320, 390, 768, 1024, 1440 e 1920; pagine intere a 1440 e 390 guardate a pezzi; registro guardato su Tutte, Restauro e Project management a 1440 e 390. Nessuna sovrapposizione tra blocchi di testo (controllo automatico a tutte le misure).
- Immagini: a 1x nessuna è servita oltre la sua misura vera. A 2x la fascia è a 0,9, l'apertura a 1,2, la cupola a 1,39 (la misura massima che esiste).
- Filtri: dito, mouse, Tab con Invio e spazio, link dalla prima schermata (14, 10, 4, 3 e 34 righe, contatore giusto, bottoni alti 45 px). Crenatura dei filtri guardata a 1x: "Ponti e", "Cemento", "Restauro" regolari.
- Collegamenti: `tel:+390498705564` (testata e contatti), `mailto:info@3essesrl.com`, mappa `google.com/maps/search/?api=1&query=Via+San+Marco+14+30030+Vigonovo+VE`.
- `segnali.sh` (`_prova/segnali-finale/`): 0 soglie bloccanti su 10. Foto al 35,8 %, monospazio 0 %, una famiglia, nessuna etichetta maiuscola, nessun titolo col punto. Da guardare: una sola misura di H2 (58 px), tenuta di proposito.
- Nessun carattere U+2014 né U+2013 nella pagina; nessun U+2014 negli script e nei .md di questa consegna. Nessuna nota di lavorazione a vista.
- Divieti del committente: nessun gradiente, nessuna emoji, niente Inter, card, glassmorphism, tre box con icona, badge, icone, dissolvenze allo scorrere, effetti sul cursore o corsivi d'accento.
