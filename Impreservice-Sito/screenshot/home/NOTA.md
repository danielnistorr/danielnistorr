# Impreservice, home finale: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP in più larghezze), caratteri in `sito/fonts/`. Rigenerazione: `bash _prova/script/build_finale.sh` (foto con `_prova/script/finale_img.py`, apertura con `_prova/script/sezione_img.py`, controlli, screenshot). Prova di gesti, larghezze e collegamenti: `node _prova/script/prova_gesti.mjs file://<cartella>/sito/index.html`.

## L'idea

Il prodotto di Impreservice è un oggetto preciso: due bussole annegate in due conci e un perno che le aggancia a scatto attraverso il giunto. La prima schermata mostra proprio questo, in sezione: due conci di calcestruzzo chiaro tagliati lungo l'asse del connettore, a tutta larghezza sotto il titolo, con Easy Click Smart nero dentro. L'interruttore Aperto / Agganciato chiude il giunto: i due conci scorrono uno verso l'altro, il perno entra nella seconda bussola, resta una linea sottile con i due smussi. Il nome del prodotto diventa il gesto della pagina. Con il nome di un concorrente la pagina non regge: il pezzo, il brevetto, il titolo del loro video e i 42 cantieri sono loro.

## Cosa è cambiato dopo il giudizio cieco (ultimo passaggio)

- **Apertura rifatta dentro la stessa idea (K6, K0, K5, K7)**: via il pezzo in diagonale con le tre legende numerate, che ripeteva il gesto di campagna ed era quasi uguale a DZ Stampi. Ora il connettore sta orizzontale in due conci tagliati, a tutta larghezza; nessuna legenda. Affiancata alla prima schermata di DZ Stampi non ha in comune né il fondo né l'impaginazione né le legende.
- **Il pezzo non è più una cattura CAD ritoccata**: è reso da uno script (`sezione_img.py`) come solido di rivoluzione visto di fianco, con i profili misurati sui disegni dell'azienda (bussola con collo, spalla, corpo e flangia con le alette; perno con corona, gola, coni, collarino, gambo e filetto). Materiale nero satinato come nei loro render 34/35/36, una sola luce morbida dall'alto a sinistra con il riflesso di un pannello, sovracampionato 3 volte: niente spigoli di mesh, niente cuciture, le due bussole hanno la stessa luce (sono lo stesso profilo specchiato).
- **Calore e materia**: i conci sono la superficie di calcestruzzo vero di una foto (Dvoretskyi, Pexels 20818874), con pori e grana, in un grigio caldo; la sede del perno è una parete concava in ombra in alto e in luce in basso. Il nero del pezzo contro il calcestruzzo chiaro dà il contrasto che mancava. Il fondo della pagina resta `#ECEAE5` pieno (tolta la sfumatura radiale).
- **Titolo non più ambiguo (K4)**: sotto "Sistemi di connessione" la riga "per conci di galleria" a 31 px (dal titolo del loro video "Conci attrezzati con tecnologia EasyClick" e dalla pagina Prodotti "adatti alla sezione gallerie"); la frase lunga è salita accanto al titolo, letta subito dopo.
- **Stato agganciato bilanciato**: i due conci si muovono di metà apertura ciascuno, quindi il giunto chiuso resta al centro dello schermo (misurato: livelli a 836 px aperti, 720 px chiusi, a 1440).
- **Pozzo tolto**: era l'immagine più disordinata. La sezione Referenze ora è solo testo (titolo, frase, tre elenchi), e la pagina non ripete più tre volte titolo, paragrafo e foto a tutta larghezza.
- **Foto omogenee**: una sola correzione per tutte (dominante tolta all'80 %, saturazione 0,42, stesso filo caldo, neri non pieni). Il viadotto ora è un taglio 3:2 a filo del bordo sinistro con il testo a destra.
- **Collegamenti**: "Tutti i 42 cantieri" porta a `referenze.html`, "La linea ponti" a `ponti-e-viadotti.html`, "Azienda" nel menu a `azienda.html`; nel piede i prodotti vanno a `easy-click.html` con le ancore, Privacy e Cookie a `privacy.html` e `cookie.html`. Le pagine sono elencate nel LEGGIMI.
- **Chiusura**: il titolo è "Conci attrezzati con tecnologia Easy Click" (titolo del loro video); "Copriamo consegne in tutto il mondo" è sceso in piccolo come "Consegne in tutto il mondo, con tempi secondo quantità". La sezione 2 ha preso un titolo nuovo dal loro comunicato del 2013 ("Entra senza fatica, tiene serrato e allineato").
- **Legende**: tolte anche quella sulla foto della galleria; la didascalia dice già "Le linee sottili sono i giunti".
- Foto più grandi (galleria 2,1:1, viadotto su 8 colonne, scudo su 7) per tenere l'area delle foto sopra il 35 %.

## Le prime due schermate

1. **1440x900**: testata chiara (simbolo vero + nome composto, menu, telefono). "Sistemi di / connessione" a 94 px in alto a sinistra, sotto "per conci di galleria"; a destra la frase "Easy Click unisce e allinea i conci prefabbricati delle gallerie scavate con la fresa...". Sotto, a tutta larghezza (alta 408 px), la sezione dei due conci con il giunto aperto e il perno che sporge dal concio sinistro. Sotto la sezione, a sinistra l'interruttore, a destra la didascalia "Easy Click Smart in sezione tra due conci, ricostruito dai disegni tecnici Impreservice. Brevetto IT 1391815." Tutto dentro i 900 px (interruttore a 815-865). **390x844**: titolo in due righe e la riga "per conci di galleria", frase, sezione alta 191 px con le due bussole intere, interruttore a tutta riga, didascalia.
2. "Entra senza fatica, tiene serrato e allineato" e la galleria a conci a tutta larghezza; poi il testo dal comunicato del 2013 e quattro righe di dati (versioni, Smart HD 480 kN, Hybrid L140 passo 5 mm, brevetto con la data).

Poi: "Dal Brennero a Brisbane" con tre elenchi corti (Italia 24, Europa 8, Mondo 10) e "Tutti i 42 cantieri"; "Giunti per ponti e viadotti" con il viadotto a sinistra; chiusura con telefono, due email, indirizzo e mappa, consegne, e la foto dello scudo a destra fino al bordo; piede.

Altezze: 5.146 px a 1440, 5.767 px a 390, 4.516 px a 1024, 5.767 px a 1920 (piede compreso).

## Caratteri e colori

- **Geologica** (Monokrom, Google Fonts, SIL Open Font License 1.1, uso commerciale libero), una sola famiglia variabile, servita dalla pagina in `sito/fonts/` (latin e latin-ext). Titoli 300, testo 400, etichette e bottoni 500; cifre tabellari per telefono, kN, mm, codici, P.IVA. Motivo: i riferimenti del mestiere usano grotesk neutre e larghe (Univers da Herrenknecht, Akkurat da Knight Architects); Geologica ha la stessa calma con un disegno proprio e non è Inter.
- **Colori**: carta `#ECEAE5` fondo unico, inchiostro `#14171A`, grigio testo `#4F5256` (6,5:1 sul fondo), blu del logo `#075A9E` (5,9:1) nel simbolo, nei passaggi del mouse e nel fuoco da tastiera. Il calcestruzzo dei conci è intorno a `#CBC6BE`, il pezzo nero. Niente fasce colorate.

## Interazione

Interruttore Aperto / Agganciato: due bottoni nativi con `aria-pressed`, stato letto da `aria-live` ("Giunto aperto..." / "Giunto chiuso..."). La pagina si apre col giunto aperto; con "Agganciato" i due conci scorrono in 320 ms uno verso l'altro, con "Aperto" si separano. Con `prefers-reduced-motion` il cambio è immediato (durata 0 s). Provato con Tab, Invio, Spazio e con il tocco a 390 (`prova_gesti.mjs`). È l'unico gesto della pagina; nessuna animazione allo scorrere, nessun effetto sul cursore. Menu a 390 con vero bottone (`aria-expanded`), piede a fisarmonica con veri bottoni.

## Immagini

| In pagina | Origine | Licenza | Lavorazione |
|---|---|---|---|
| Apertura, tre livelli `sez-*` | connettore: profili dai disegni CAD dell'azienda (`12`, `13`, `14`), colore dai loro render; conci: Артем Дворецкий, Pexels 20818874 | dell'azienda; Pexels, gratuita | reso con `sezione_img.py` (solido di rivoluzione, materiale nero satinato, ombre portate, sede conica del perno, smussi sugli spigoli del giunto); WebP con trasparenza a 1x e 2x |
| Galleria di metropolitana a conci | Max Mishin, Pexels 11424325 | Pexels, gratuita | trattamento comune, ombre aperte; 2,1:1 e verticale per il telefono |
| Viadotto | Kewal Nagda, Pexels 27808651 | Pexels, gratuita | trattamento comune; 3:2 |
| Chiusura, scudo della fresa sulla culla | Evangelos Mpikakis, Unsplash CPI7JAIVaDU | Unsplash License | trattamento comune; 4:3 |
| Logo | `logo-impreservice-icona-blu-1000.png` del loro sito | dell'azienda | ritagliato, PNG a 160 e 240 px |

Tutte le foto di repertorio sono in `assets/esterne/` con pagina e licenza in `assets/CREDITI.md`; nessuna compare nei CREDITI.md delle altre home della campagna (controllato per identificativo), nessuna è generata dall'IA. La fresa nella foto di chiusura non ha marchi leggibili in primo piano; i costruttori di frese non sono concorrenti di Impreservice. Le didascalie non citano la fonte.

## Newsletter

Non c'è. Impreservice vende a imprese di scavo e prefabbricatori, ha due notizie in dieci anni (Viatec 2013, WTC 2022), nessun catalogo da scaricare e nessun cliente privato; il blocco newsletter di oggi con ogni probabilità non è collegato a niente. Meglio il contatto diretto e la pagina "Fiere e notizie".

## Controlli (24/10/2026, dopo le correzioni)

- Larghezza del documento uguale alla finestra a 320, 360, 390, 414, 600, 768, 860, 1024, 1180, 1280, 1440, 1680, 1920 e 2560, con il giunto aperto e chiuso. I conci coprono la fascia fino ai bordi anche a 2560.
- Screenshot guardati a pezzi: 1440 intera, 390 intera, prime schermate a 320, 390, 768, 1024, 1440 (aperto e agganciato), 1920; pagina intera a 1024.
- Interruttore: Invio e Spazio da tastiera, tocco a 390, `aria-pressed` e `aria-live` corretti, movimento ridotto a 0 s. Menu e fisarmonica con `aria-expanded`.
- Collegamenti: `tel:+3904441939838`, `mailto:info@impreservicesrl.it`, `mailto:carlo@impreservicesrl.it`, mappa Google con l'indirizzo di via Serenissima 8/b; tutte le ancore interne esistono; i link alle pagine future sono nel LEGGIMI.
- `segnali.sh` del kit a 1440: 0 soglie da correggere su 10, 0 da guardare su 8 (foto 36,3 % della pagina, una famiglia, niente mono, niente etichette sopra i titoli, nessun numero grande con etichetta, 11 filetti larghi).
- Contrasto AA: testo `#4F5256` 6,5:1, blu 5,9:1, bottone attivo 15:1.
- Nessun U+2014 in pagina, nella NOTA, nel LEGGIMI e nei crediti; nessun segnaposto in pagina.
- Divieti del committente: niente gradienti viola-blu, testo in gradiente, emoji, Inter, card con bordo colorato, glassmorphism, tre box con icona, badge sopra il titolo, icone Lucide, dissolvenze allo scorrere, effetti sul cursore, corsivi d'accento, legende numerate.

## Da confermare (dettagli nel LEGGIMI)

La sezione dell'apertura è una ricostruzione (profondità e verso della bussola nel concio, forma della sede del perno, perno avvitato in un concio prima della posa, giunto in cui lavora); "una per concio"; il rivestimento in materiale composito (fonte del 2013); Smart HD e Hybrid ancora in produzione; la linea ponti ancora attiva; materiale e finitura del pezzo nero.
