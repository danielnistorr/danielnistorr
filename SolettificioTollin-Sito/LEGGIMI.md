# Solettificio Tollin: proposta di nuova home

Proposta non richiesta, solo la home. Non è stata inviata né pubblicata; l'azienda non è stata contattata.

- Pagina: `sito/index.html` (statica, si apre con file:///). Immagini in `sito/img/`, carattere in `sito/fonts/`.
- Screenshot: `screenshot/home/` (1440 intera e prima schermata, 390 intera e prima schermata, chiusura e piede a 1440). Spiegazione delle scelte in `screenshot/home/NOTA.md`.
- Si rifà tutto con `bash _prova/script/build_finale.sh` (con `--tieni` restano le prove a 320, 768, 1024 e 1920 in `_prova/tmp-build/`). Prove della rifinitura: `node _prova/script/prova_rifinitura.mjs <cartella>`.
- Analisi con le fonti: `01-analisi.md`. Prototipi e voti del giudice: `_prova/home/a/` e `_prova/home/b/`.

## Dati da confermare con l'azienda

- **Il foglio dell'apertura**: è il cartoncino dei modelli tagliato dal plotter Comelz CN della modelleria (così lo descrive la didascalia)? Va confermato cosa sia il materiale e se il plotter è ancora quello.
- **Il civico**: il sito dice via Irpinia 15, la mappa incorporata punta al 12. In pagina c'è il 15.
- **Il fax**: 049 644643 (sito) o 049 8790773 (coobiz, vecchia ditta). Tolto dalla pagina finché non si conferma che serve.
- **Gli orari**: non pubblicati, non sono in pagina.
- **Le macchine di oggi**: plotter Comelz CN, tranciatrice Comelz CM44S, pressa Comec SPM12, lette nelle foto del 2016 o prima. Sono ancora queste?
- **Il taglio**: il testo italiano parla di laser e di punzone e lama oscillante; in pagina solo punzone e lama oscillante (la frase verbatim).
- **La storia**: chi ha fondato nel 1970 e dove. In pagina c'è solo "Siamo nati nel 1970, come piccola realtà a conduzione familiare" (da `azienda.html`) e nel piede "Dal 1970, oggi in via Irpinia 15": nessun legame tra il 1970 e Villatora. Da confermare anche il passaggio dalla ditta individuale Tollin Gianfranco alla S.r.l. nel 2011 (nella riga legale: "S.r.l. dal 2011") e chi sono oggi "i titolari".
- **I marchi dei fornitori** (Tecno-Sint, Texon, Ocram, Adhegel, Greenlife, Fisca, SATRA): si possono mostrare o nominare? Nella foto della scatola le scritte sono state tolte col ritocco.
- **I clienti** e le fasce di mercato: nessuno è nominato.
- **Il logo ufficiale**: impronte verdi con "SOLETTIFICIO TOLLIN" o riquadro azzurro "Dal 1970"? In pagina ci sono le impronte, senza la riga piccola "Qualità artigianale italiana".
- **Il sito inglese**: resta? Il link "English" punta a `en/`.

## Foto da rifare dal vero

Il materiale di oggi è piccolo (850x600, con la cornice disegnata nel file). Serve mezza giornata di still life e un'ora in reparto.

1. **Apertura**: oggi è il foglio di cartoncino della loro foto `modelleria2.jpg` (850x600), scontornato e pulito; regge a 820 px su schermi normali, è morbido su quelli ad alta densità. Da rifare dal vero: il foglio appena uscito dal plotter, appoggiato su un piano chiaro o tenuto sospeso, ripreso dall'alto e di tre quarti, luce di finestra laterale, almeno 4000 px di lato lungo, con molta aria intorno; meglio se si vede lo spessore del taglio. Come sostituto definitivo, se il foglio non piace: un loro sottopiede cambrato da solo, di profilo e di tre quarti, su fondo chiaro.
2. **I quattro reparti**, stesso taglio orizzontale 3:2 e stessa luce naturale, senza cornici: il foglio di cartoncino che esce dal plotter CN (l'immagine più forte, va rifatta grande); la CM44S con il foglio color cuoio sul nastro; gli stampi della SPM12 con le forme; le mani che sistemano i sottopiedi nella scatola.
3. **La scatola di sottopiedi cambrati**, dall'alto e di tre quarti, con la luce che segue la curva della pila; se i marchi del fornitore non si possono mostrare, con il lato senza stampa in vista. Oggi le scritte sono tolte col ritocco e da vicino si vede.
4. **La chiusura**: il furgone davanti al capannone in una bella giornata, porte aperte e cartoni, a 3000 px almeno (oggi è la foto del sito a 720 px).

## Licenze

- **Carattere**: Commissioner (Kostas Bartsokas), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; file servito dalla pagina.
- **Foto di Tollin**: dal sito tollin.it, diritti dell'azienda; usate solo per questa proposta.
- **Segnaposto**: nessuno nella home finale (tutte le foto sono di Tollin). Quelli scaricati per i prototipi sono elencati in `assets/CREDITI.md`.
- Nessuna immagine generata con l'IA.

## Logo

Nessun vettoriale sul sito. In pagina c'è il ritaglio del JPEG più grande (`assets/originali/logo-tollin-piedi-it.png`, 420x98) senza ingrandimento, fondo reso trasparente, 316x69 px mostrato a 150 px (2,1x); tolta la riga piccola "Qualità artigianale italiana", che a quella misura sarebbe alta 5 px. Una ricostruzione SVG della scritta non sarebbe fedele (la scritta mescola un condensato tipo Impact e un geometrico non identificati): va chiesto il file vettoriale originale.

## Pagine del sito nuovo linkate dalla home

`azienda.html`, `dove-siamo.html`, `en/`, `studio-modelleria.html`, `lavorazione-automatizzata.html`, `cambratura.html`, `supervisione.html`, `sottopiedi.html` (ancore `#uomo`, `#donna`, `#bambino`, `#sandalo`, `#materiali`), `contatti.html` (modulo con consenso privacy, da collegare a un servizio di invio), `privacy.html`, `cookie.html`. Nella proposta non esistono ancora. La testata porta alle sezioni della home (`#reparti`, `#sottopiedi`, `#contatti`) e ad `azienda.html`; nel piede "English" (`en/`) sta nella riga in basso accanto a Privacy e Cookie.

## Niente newsletter, niente social

Tollin vende solo ai calzaturifici e non ha notizie, fiere, cataloghi né clienti privati: una newsletter non avrebbe niente da mandare. Nessun profilo social trovato: nel piede non c'è "Seguici".
