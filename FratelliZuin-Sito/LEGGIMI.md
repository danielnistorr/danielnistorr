# Fratelli Zuin: proposta di nuova homepage

Proposta non richiesta di una nuova home per F.lli Zuin & C. snc (Padova), movimento terra, lavori stradali, demolizioni e aspirazioni con escavatori a risucchio. Solo la home. Nessun contatto con l'azienda, niente di pubblicato.

## Cosa c'è

- `sito/index.html`: la home, una pagina sola, senza librerie esterne.
- `sito/img/`: solo le immagini usate, JPEG o WebP in più larghezze (srcset).
- `sito/fonts/archivo-latin-var.woff2`: Archivo variabile, servito dalla pagina (licenza sotto).
- `screenshot/home/`: home a 1440 e a 390 (intere e prima schermata), chiusura e piede a 1440; `NOTA.md` con idea, scelte e controlli.
- `_prova/script/build_finale.sh`: rifà immagini, pagina, controlli di testo e screenshot. Usa `finale_img.py` (scontorno e trattamento delle foto), `home-finale.html` (sorgente della pagina) e `finale_shoot.mjs` (screenshot JPEG).
- `01-analisi.md`: fatti con le fonti, voti delle foto, direzioni e riferimenti. `_prova/home/a` e `_prova/home/b`: i due prototipi; la home finale parte da A, "Il risucchio".

## Pagine del sito nuovo a cui puntano i link del piede

Oggi esistono solo nella proposta; i nomi dei file sono indicativi.

- `azienda.html` (Chi siamo) e `azienda.html#storia` (La storia dal 1946)
- `servizi.html` con le ancore `#movimento-terra`, `#lavori-stradali`, `#demolizioni`, `#risucchio`, `#fognature`
- `noleggio-scarrabili.html` (cassoni da 2 a 25 m³)
- `dove-siamo.html` (istruzioni dal casello di Padova Est, cartina)
- `contatti.html` (Preventivi, modulo con consenso privacy)
- `privacy.html` e `cookie.html` (oggi la cookie policy è dentro la privacy policy: va separata, e il banner deve chiedere un consenso vero, non "se continui a leggere accetti")

La testata e i link della pagina portano alle sezioni della home (Lavori, Storia, Dove siamo).

## Dati da confermare con l'azienda

- **Anno**: il sito scrive "nasce nel 1946", il registro delle imprese "Fondazione 1977" (la snc di oggi). In pagina "dal 1946" e "tre generazioni", come scrive l'azienda.
- **Mezzo dell'apertura**: "MAN TGA 35.410" è letto sulla cabina nella foto; i quattro assi sono contati nella foto. Confermare modello e che sia ancora in uso.
- **Foto loro o no**: gallery1 (autocarri sul piazzale), lavori-stradali-1000x800 (scavo con tubazioni, usata per le fognature), gallery4 e gallery5 (risucchio): sono loro mezzi e loro cantieri? La foto del movimento terra del prototipo (stessa scena della chiusura) è stata tolta.
- **Frasi brevi dei lavori** da far approvare: per urbanizzazioni, fognature, ritiro del materiale e sistemazioni esterne il sito ha solo il nome della voce; le frasi in pagina sono scritte da noi a partire dai loro testi.
- **SOA**: categorie, classifiche e scadenza. In pagina solo "attestazione di qualificazione SOA", come sul sito.
- **Nome nel piede**: "F.lli Zuin & C. snc" (sito) oppure "FRATELLI ZUIN SNC DI ZUIN ANTONIO, LUIGI, ANDREA & C." (registro).
- **PEC** (non trovata), **orari** di ufficio e del piazzale (non indicati: in pagina non ci sono), un eventuale cellulare per le urgenze, **fax** 049 6458813 ancora attivo.
- Un paio di **lavori recenti veri** (committente, luogo, anno) e le **foto d'archivio** di famiglia (autocarro DOGE, Foro Boario 1968-69) con il permesso di pubblicarle: darebbero alla storia le immagini che oggi mancano.

## Foto

Trattamento unico (PIL): colori un po' spenti e caldi, neri sollevati; lo scontorno ha una sola maschera di nitidezza leggera. Nessuna immagine generata dall'IA, nessuna foto ingrandita oltre l'originale.

Loro (dal sito di oggi, `assets/originali/`):
- `gallery3.jpg`, escavatore a risucchio scontornato con ombra disegnata: apertura.
- `gallery4.jpg` (retro col braccio ad arco), `gallery1.jpg` (autocarri), `lavori-stradali-1000x800-1.jpg` (scavo con tubazioni): tre dei nove lavori.
- `gallery5.jpg`, fiancata con logo e scritta: storia, "Oggi".
- `pagina-iniziale-1.jpg`, Hitachi che carica il DAF: chiusura.
- Logo: `logo-zuin-nero-765x463.png` ricolorato in inchiostro #1B1B19, PNG a 300 px (2x).

Segnaposto Unsplash (licenza Unsplash, verificata il 24/10/2026, autori e pagine in `assets/CREDITI.md`; in pagina con "Foto indicativa"): Bruno BD (demolizioni), Iain CJwHaOQFcwI (urbanizzazioni), Wolfgang Weiser (lavori stradali), Shane McLendon (movimento terra), Brandon Mowinkel (ritiro del materiale), Eduard Delputte (sistemazioni esterne). Nessuna è usata in un'altra home della campagna (controllato sui CREDITI.md delle altre cartelle).

### Da rifare dal vero

1. **Il risucchio, per l'apertura** (la più importante): mezzo intero di tre quarti dal lato del braccio, con almeno due metri di spazio davanti al muso (oggi la foto taglia il muso: per questo il mezzo è a filo del bordo destro). Piazzale pulito, cielo coperto chiaro o mattino presto, nessuna ombra dura; macchina ferma su treppiede, obiettivo 50-85 mm da 15-20 m per non deformare, altezza della camera a metà cassone; almeno 4000 px sul lato lungo. Uno scatto anche col braccio aperto.
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
