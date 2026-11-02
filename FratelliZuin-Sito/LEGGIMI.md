# Fratelli Zuin: proposta di nuova homepage

Proposta non richiesta di una nuova home per F.lli Zuin & C. snc (Padova), movimento terra, lavori stradali, demolizioni e aspirazioni con escavatori a risucchio. Solo la home. Nessun contatto con l'azienda, niente di pubblicato.

## Cosa c'è

- `sito/index.html`: la home, una pagina sola, senza librerie esterne.
- `sito/img/`: solo le immagini usate, JPEG o WebP in più larghezze (srcset).
- `sito/fonts/archivo-latin-var.woff2`: Archivo variabile, servito dalla pagina (licenza sotto).
- `screenshot/home/`: home a 1440 e a 390 (intere e prima schermata), chiusura e piede a 1440; `NOTA.md` con idea, scelte, controlli e cosa è cambiato il 2 novembre.
- `_prova/script/build_finale.sh`: rifà immagini, pagina, controlli di testo e screenshot. Usa `finale_img.py` (scontorno e trattamento delle foto), `home-finale.html` (sorgente della pagina) e `finale_shoot.mjs` (screenshot JPEG); `finale_prova.mjs` prova scorrimento orizzontale, tastiera, tocco e collegamenti. La pagina si prova meglio da un server (`python3 -m http.server` dentro `sito/`), anche se si apre pure da file.
- `01-analisi.md`: fatti con le fonti, voti delle foto, direzioni e riferimenti. `_prova/home/a` e `_prova/home/b`: i due prototipi; la home finale parte da A, "Il risucchio".

## Pagine del sito nuovo a cui puntano i link del piede

Oggi esistono solo nella proposta; i nomi dei file sono indicativi.

- `azienda.html` (Chi siamo) e `azienda.html#storia` (La storia dal 1946)
- `servizi.html` con le ancore dei nove lavori: `#risucchio`, `#movimento-terra`, `#lavori-stradali`, `#demolizioni`, `#urbanizzazioni`, `#fognature`, `#esterne`, `#ritiro` (il noleggio ha una pagina sua)
- `noleggio-scarrabili.html` (cassoni da 2 a 25 m³)
- `dove-siamo.html` (istruzioni dal casello di Padova Est, cartina)
- `contatti.html` (Preventivi, modulo con consenso privacy)
- `privacy.html` e `cookie.html` (oggi la cookie policy è dentro la privacy policy: va separata, e il banner deve chiedere un consenso vero, non "se continui a leggere accetti")

La testata e i link della pagina portano alle sezioni della home (Lavori, Storia, Dove siamo).

## Dati da confermare con l'azienda

- **Anno**: il sito scrive "nasce nel 1946", il registro delle imprese "Fondazione 1977" (la snc di oggi). In pagina "dal 1946" e "tre generazioni", come scrive l'azienda.
- **Mezzo dell'apertura**: "MAN TGA 35.410" è letto sulla cabina nella foto; i quattro assi sono contati nella foto. Confermare modello e che sia ancora in uso.
- **Titolo**: è la scritta dipinta sulla fiancata ("Escavazioni ed aspirazioni a risucchio controllato"), con "risucchio" in grande. Va bene come prima frase del sito? In alternativa si tiene la stessa impaginazione con un'altra parola loro.
- **Colori**: il giallo del fondo (#ECD675) è il giallo della cabina MAN schiarito, il bordeaux del piede (#5A2830) è la fascia con la scritta, il rosso (#B42620) è il cassone: misurati sulle foto, da confrontare con i codici RAL della carrozzeria se il carrozziere li ha.
- **Foto loro o no**: gallery1 (autocarri sul piazzale), gallery4 (risucchio da dietro), pagina-iniziale-2 (pala CAT sulle macerie, usata per il ritiro del materiale) e pagina-iniziale-1 (Hitachi e DAF, chiusura): sono loro mezzi e loro cantieri?
- **Frasi brevi dei lavori** da far approvare: per urbanizzazioni ("Opere di urbanizzazione per committenti pubblici e privati"), fognature, ritiro del materiale e sistemazioni esterne il sito ha solo il nome della voce; le frasi in pagina sono scritte da noi a partire dai loro testi.
- **Frase della chiusura**: "Scarrabili della larghezza di un'automobile, in grado di intervenire in qualsiasi situazione e spazio" è la loro frase della pagina Azienda; confermare che gli scarrabili piccoli ci siano ancora.
- **SOA**: categorie, classifiche e scadenza. In pagina solo "attestazione di qualificazione SOA", come sul sito.
- **Nome nel piede**: "F.lli Zuin & C. snc" (sito) oppure "FRATELLI ZUIN SNC DI ZUIN ANTONIO, LUIGI, ANDREA & C." (registro).
- **PEC** (non trovata), **orari** di ufficio e del piazzale (non indicati: in pagina non ci sono), un eventuale cellulare per le urgenze, **fax** 049 6458813 ancora attivo.
- Un paio di **lavori recenti veri** (committente, luogo, anno) e le **foto d'archivio** di famiglia (autocarro DOGE, Foro Boario 1968-69) con il permesso di pubblicarle: darebbero alla storia le immagini che oggi mancano.

## Foto

Trattamento unico (PIL): colori un po' spenti e caldi, neri sollevati; lo scontorno non ha maschera di nitidezza (sarebbe andata sopra gli artefatti JPEG), il bordo è ripulito dal bianco del cielo. Nessuna immagine generata dall'IA, nessuna foto ingrandita oltre l'originale.

Loro (dal sito di oggi, `assets/originali/`):
- `gallery3.jpg`, escavatore a risucchio scontornato con il muso intero (contorno destro della cabina disegnato a mano) e ombra disegnata: apertura, 884 px a 1440.
- `gallery4.jpg` (retro col braccio ad arco), `gallery1.jpg` (autocarri), `pagina-iniziale-2.jpg` (pala CAT sulle macerie): tre dei nove lavori.
- `pagina-iniziale-1.jpg`, Hitachi che carica il DAF: chiusura, taglio 2,2:1.
- Logo: `logo-zuin-nero-765x463.png` ricolorato in inchiostro #1B1B19 (testata) e in giallo #ECD675 (piede), PNG a 300 px (2x).

Segnaposto Unsplash (licenza Unsplash verificata sulla pagina di ogni foto, autori e pagine in `assets/CREDITI.md`; in pagina con "Foto indicativa"), tutti ripresi da terra come le foto loro: Marek Studzinski (demolizioni), Anna Kharkivska (urbanizzazioni), John Kakuk (fognature), Wolfgang Weiser (lavori stradali, ritaglio stretto), Troy Mortier VOgZMixWOHo (movimento terra), Annie Spratt (sistemazioni esterne). Nessuna è usata in un'altra home della campagna (controllato sui CREDITI.md delle altre cartelle il 02/11/2026).

### Da rifare dal vero

1. **Il risucchio, per l'apertura** (la più importante): mezzo intero di tre quarti dal lato del braccio, con almeno due metri di spazio davanti al muso (oggi il muso arriva a 4 px dal bordo della foto e il contorno destro della cabina è disegnato a mano; la foto è di 1365 px, per questo in pagina il mezzo non supera i 884 px). Fondo neutro: in pagina il giallo lo mette il sito. Piazzale pulito, cielo coperto chiaro o mattino presto, nessuna ombra dura; macchina ferma su treppiede, obiettivo 50-85 mm da 15-20 m per non deformare, altezza della camera a metà cassone; almeno 4000 px sul lato lungo. Uno scatto anche col braccio aperto.
2. **Il braccio ad arco e il tubo** in dettaglio, stessa luce.
3. **Un cassone scarrabile piccolo**, "della larghezza di un'automobile", in una via stretta.
4. **Un lavoro stradale finito** (rotatoria, pista ciclabile) dall'alto con drone, mezzogiorno coperto; e uno scavo con il risucchio in un luogo confinato.
5. **Movimento terra e demolizioni** con i loro escavatori, per sostituire i segnaposto Unsplash.
6. **La squadra** davanti ai mezzi, in divisa, luce naturale.
7. **Archivio di famiglia**: DOGE, Foro Boario, Prato della Valle, digitalizzati a 600 dpi.

## Licenze

- **Archivo** (Omnibus-Type), Google Fonts, SIL Open Font License 1.1: uso commerciale libero, file servito da `sito/fonts`.
- **Foto Unsplash**: Unsplash License (uso commerciale, attribuzione non obbligatoria; vietato rivenderle senza modifiche). Restano segnaposto da sostituire.
- **Foto e logo dell'azienda**: dal loro sito, usati solo per la proposta.

## Logo

Esiste solo come PNG da scansione di un timbro ovale (765x463, bordi frastagliati): nessun SVG nel sito. In pagina è il PNG ricolorato in inchiostro a 2x, nitido alle misure usate (96 e 150 px). Un SVG va ridisegnato a mano dal file originale (tipografia o carrozziere che dipinge i mezzi) e approvato dall'azienda; il rosso del timbro (#FF0000) resta da usare solo dove lo vogliono loro.

## Newsletter e social

- **Newsletter: no.** L'azienda non ha novità, fiere, cataloghi o collezioni da comunicare; enti, imprese e privati chiamano per un preventivo.
- **Seguici: no.** Nessun profilo social esiste (né nel codice del sito né in rete).
