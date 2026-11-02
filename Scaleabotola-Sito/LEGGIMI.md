# Scaleabotola (Scalarredo S.r.l.): proposta di nuova home

Proposta non richiesta, solo la home. Non pubblicata, azienda non contattata.

- Pagina: `sito/index.html` con `sito/img/` e `sito/fonts/` (statica, si apre con file:///).
- Screenshot: `screenshot/home/` (home-1440, home-1440-prima-schermata, home-390, home-390-prima-schermata, chiusura-1440). Nota di progetto: `screenshot/home/NOTA.md`.
- Rigenerare tutto: `sh _prova/script/build_finale.sh` (con `controlli` anche 320, 768, 1024, 1920, il menu aperto a 390 e `controlli.mjs`).
- Sorgenti: `_prova/script/home_finale.src.html`, `marchio.part` (marchio SVG), `quote.part` (quota della foto d'apertura), `disegno.py` (disegno in sezione di "Dove va il foro?"), `finale_img.py` (tutte le immagini).
- Analisi e fonti: `01-analisi.md`; prototipi e giudizio: `_prova/home/a`, `_prova/home/b`, `_prova/giudizio.json`.

## Dati da confermare con l'azienda

In pagina ci sono solo dati presi dai loro siti; questi vanno comunque verificati prima di pubblicare:
- **Foto d'apertura**: `PLUS-pantografo.jpg` è sul loro sito (scalarredo.it, 2026) ma ha l'aria di una foto di catalogo del produttore: chiedere se si può usare. La quota "10 cm" è disegnata sui due spigoli del primo gradino in metallo (profondità dichiarata "10 cm" nella pagina PLUS a pantografo); la scritta "pannello 18 mm" sta sulla superficie bianca sotto la scala, che leggo come il pannello della botola aperto: da confermare con loro.
- **Chiusura**: la Montreal bianca (`scale-giorno-Montreal-1.jpg`, foto loro da telefono) è ritoccata (nastri decorativi tolti dal muro, correnti ricostruiti, una vite tolta): il ritocco va accettato dal cliente della foto, e va confermato che sia una Montreal con fascia da 8 mm. Confermare anche `montreal-012` (Montreal antracite) e `banner-bg2` (PLUS in frassino).
- "Progettate, prodotte e posate da noi" e "posa in opera della nostra squadra" per le scale da interno; se le retrattili sono prodotte o rivendute ("fornitura vendita e installazione").
- Misure delle retrattili prese dalle tavole "MISURE STANDARD DISPONIBILI" di scaleabotola.com (probabile fornitore): fori 45 x 70-80 x 100 (soffitto), 50 x 80-80 x 100 (parete), 60 x 80-80 x 100 (terrazzo), 70 x 100 (soppalco), altezza 300 cm, 140 cm a terra e 170 per aprirla, gradini 10 x 35 cm. Il disegno in sezione è ridisegnato in scala (1 cm = 1,25 unità, pendenza di circa 65 gradi, 12 alzate) ma resta schematico: da rivedere con loro, in particolare la parete (portina incernierata in basso) e il soppalco.
- Prezzi del negozio letti il 24/10/2026 (da 238 euro più IVA a soffitto, da 425 euro più IVA a parete): cambiano, vanno letti dal negozio al momento della pubblicazione o tolti.
- Consegna "di solito in 5 giorni" dal magazzino e "2-6 settimane" fuori misura (dalle condizioni di vendita), portata 150 kg e collaudo a 260 kg: sono nel cartiglio della prima schermata, vanno confermati. La norma UNI EN 14975 (citata con anni diversi nei due siti, e "EN 131" nella pagina PLUS) non è in pagina finché non confermano quale norma e quale anno.
- Email da mettere in pagina: oggi scalarredo@scalarredo.it (dalle condizioni di vendita); in alternativa info@scaleabotola.com.
- Indirizzo: il CAP 35035 di Mestrino non è scritto sul loro sito, quindi in pagina non c'è; da aggiungere se lo confermano.
- Orario esatto del sabato (oggi "solo al mattino"); provincia del REA 295631 (presumibilmente Padova).
- "Da due generazioni": anno di inizio della famiglia (srl dal 1997, "più di 40 anni" e "trentennale" nei testi), nomi delle due generazioni, un lavoro con città e anno da mettere in pagina come prova.
- Il secondo numero 049 900 48 34: fax o telefono? Oggi non è in pagina.
- Canale YouTube: l'indirizzo è col nome personale (@giorgiotiziana4735); meglio un indirizzo col nome dell'azienda.

## Foto da rifare dal vero

Una giornata di foto nello showroom di Mestrino e da due o tre clienti basta per sostituire tutto:
1. **Apertura**: una PLUS montata nello showroom, aperta, ripresa dall'alto dentro il foro come oggi (cavalletto sopra la botola, ottica 35 mm in asse con la scala), parquet chiaro sotto, niente cavi né arredi del piano di sotto, luce morbida dall'alto; almeno 4000 px sul lato lungo, così si serve a 2x anche a 960 px. Stessa inquadratura per non spostare la quota del gradino. Meglio ancora con i gradini in frassino.
2. **Retrattili**: macro del gradino in frassino spazzolato con luce radente per la venatura, la cerniera e il bordo del pannello da 18 mm. Sostituisce `banner-bg2`, vecchia e morbida.
3. **Scale da interno**: la Montreal antracite (o una New York) posata, inquadrata solo sulla rampa, casa svuotata di oggetti, pavimento chiaro, luce naturale; almeno 3000 px, così il taglio verticale si serve a 2x (oggi è a 1,35x perché allargando entra uno sgabello).
4. **Chiusura**: la Montreal bianca rifotografata con la reflex dalla stessa posizione, muro sgombro, oppure una foto vera dello showroom sulla statale 11 (interno con le scale esposte, luce del pomeriggio, nessuna persona riconoscibile senza liberatoria).

Formato: RAW o JPEG alla massima qualità, bilanciamento del bianco neutro sul muro.

## Licenze

- Carattere: Archivo (Google Fonts), SIL Open Font License 1.1, uso commerciale libero; servito dalla pagina in `sito/fonts/archivo-latin.woff2`.
- Foto di repertorio: nessuna in pagina. L'elicoidale di Gayatri Dhea (Pexels) usata nella chiusura del giro precedente è stata tolta; resta scaricata in `assets/esterne/` con la licenza in `assets/CREDITI.md`.
- Foto dell'azienda e del fornitore: diritti da confermare (vedi sopra e `assets/CREDITI.md`).

## Logo

- In testata e nel piede: marchio a triangolo in SVG tracciato dai contorni del PNG vero (fedele) più la scritta "Scalarredo scale" estratta dal PNG e ricolorata in blu #1F4FA8. Nel piede è più grande (marchio 50 px, scritta alta 30 px); il quadrato giallo del logo originale non c'è più perché nel piede era il blocco più saturo della pagina e la riga "Le scale a Padova" veniva di 8 px.
- Da chiedere: un vettoriale del logo e il nome del carattere della scritta (oggi simile a un Times); se il favicon "SC" giallo su blu è voluto.

## Pagine che il sito nuovo deve avere (link del piede)

I link del piede puntano a sezioni della home o a queste pagine, che oggi non esistono nella proposta:
- `scale-da-interno/a-giorno-e-a-rampa/`, `scale-da-interno/elicoidali/`, `scale-da-interno/a-chiocciola/`, `scale-da-interno/a-pedata-alternata/`, `scale-da-interno/ringhiere-e-parapetti/`
- `scale-retrattili/a-soffitto/`, `scale-retrattili/a-parete/`, `scale-retrattili/per-terrazzo/`, `scale-retrattili/per-soppalco/`, `scale-retrattili/motorizzate/` (le misure del foro portano a `#foro` della home)
- `negozio/` (negozio online), `catalogo-scale-retrattili.pdf` (oggi `Cat-Retrattili-1.pdf`), `condizioni-di-vendita/`, `privacy/`, `cookie/`
- Lo showroom di Mestrino porta alla chiusura della home (`#showroom`).

## Newsletter

Non c'è e non serve: non pubblicano novità, fiere o collezioni e una scala si compra una volta. Al suo posto, nel piede, il catalogo PDF delle retrattili.

## Dominio

scaleabotola.com va reindirizzato alle pagine delle retrattili del sito nuovo (scalarredo.it), da decidere con loro.
