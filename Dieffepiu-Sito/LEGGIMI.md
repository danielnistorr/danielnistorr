# Dieffepiu S.r.l.: proposta di nuova homepage

Proposta non richiesta di una nuova home per dieffepiu.it (solo la home). Non è pubblicata, l'azienda non è stata contattata, nessun modulo è stato inviato.

## Cosa c'è

- `sito/index.html`: la home finale, statica (si apre con file:///). `sito/img/`: solo le immagini usate, WebP in più larghezze. `sito/fonts/`: Pathway Extreme con la licenza.
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` e `NOTA.md` (idea, schermate, caratteri, colori, interazione, foto, controlli).
- `_prova/script/build_finale.sh`: rifà immagini, controllo U+2014 e screenshot. `finale_img.py` lavora le foto (serve OpenCV, già installato in `/root/.local`), `shot_finale.mjs` fa gli screenshot, `prova_gesto.mjs` prova selettore e fisarmonica, `prova_giro3.mjs` prova scorrimento da 320 a 2560, menu con le lingue, newsletter, collegamenti e bersagli di tocco, `largo.mjs` cerca ciò che esce dalla finestra.
- `01-analisi.md`: fatti con le fonti. `_prova/home/a` e `b`: i due prototipi da cui viene la home (base A, innesti di B).

## Dati da confermare con l'azienda

In pagina ci sono solo dati presi da `01-analisi.md`; questi vanno confermati prima della messa in linea.
- **Storia e anni**: "dal 1987" (data di costituzione della società, che era la Di Franco); data della scissione e del cambio di nome in Dieffepiu; come raccontare il rapporto con Di Franco Holding.
- **"Oltre 2.000 impianti"** (catalogo 2023) contro "oltre 1.800" del vecchio sito: il numero di oggi.
- **"Progettiamo e produciamo"** (testo del sito) contro il codice ATECO di commercio all'ingrosso: cosa producono in casa e cosa fanno fare a terzi.
- **Linee e macchine**: "quattordici linee" e "dodici macchine" vengono dal catalogo 2023; quali sono ancora in produzione; i nomi esatti ROLLY STYLE 1, ROLLY STYLE WOOD e ROLLY STYLE 3 (il catalogo scrive "ROLLY STYLE 1, WOOD e 3").
- **Cingolo d'apertura**: le legende dicono "TK101 Cingolo" e "Occhielli di attacco", la riga sotto "TANK REVOLUTION® laterale, fino a 3.000 × 1.900 mm, ingombro minimo 50 mm" (catalogo p. 93). Il codice TK101 è quello che la tavola esplosa di p. 93 dà al cingolo con l'attacco a occhiello, uguale a quello della foto; ma la foto è del kit TANK del sito e non si sa se il pezzo è del TANK 2.0 o del TANK REVOLUTION®: va confermato che sia il TK101, e che "cingolo" e "occhielli di attacco" siano i nomi che usano (sul sito la famiglia si chiama "Sistema carrarmato").
- **Profili TANK** (scheda nella sezione Sistemi, catalogo p. 91): DFTK005 guida superiore 640 g/m, DFTK006 riscontro a muro 269 g/m, DFTK007 cassonetto 977 g/m, DFTK008 barra maniglia 864 g/m, EN-AW 6060 T5: ancora validi.
- **Macchine**: dati del catalogo 2023 di ATT001-B (piano 3.000 mm, barra saldante 1.560 mm, 150 kg, fettuccia 10 e 50 mm, saldatura termica a impulsi), ATT007 (4.000 mm, 400 kg), ATT030 (8.200 mm, 1.200 kg, 4 kW, 40 pezzi l'ora a misura e 30 in kit, taglio della rete a ± 1,5 mm, sotto 70 dB(A)); codice del banco e saldatrice automatica per tubi rete da 6 m (catalogo p. 236: in pagina il codice non c'è, il selettore lo lascia vuoto) e stato del suo "brevetto depositato"; "Taglia e salda la rete sullo stesso banco" per ATT007 è dedotto dal nome "banco elettronico di taglio e saldatura".
- **Brevetti**: "gran parte dei sistemi e delle macchine è coperta da brevetti e modelli di utilità" (catalogo p. 4): ancora vero; TANK 2.0 Bi-Convex "brevettato" o "patent pending" (non citato in pagina).
- **Norma e freno**: EN UNI 13561 e freno-rallentatore FX135 (catalogo pp. 6-7) tolti dalla pagina finché non si verifica che la norma citata sia quella giusta e aggiornata.
- **Colori**: accessori neri di serie, a colori da 1.000 pezzi per tipo con il 20 % sul listino (bronzo, grigio, RAL 1013, 9010, 8017): ancora valido.
- **Fiere**: in pagina "cinque fiere dal 2021 a oggi, l'ultima a Parigi tra settembre e ottobre 2026". Se saranno a MADE expo 2027 (data, padiglione, stand), la riga va cambiata in "la prossima".
- **Recapiti**: orari (piede del sito di oggi contro "h 8-19" delle traduzioni); civico 33 o 33a; email attive (info@dieffepiu.it del sito o le @difranco.it del catalogo); PEC (presa da aziende.it); capitale sociale 300.000 euro interamente versato o no; il fax +39 049 8790918 non è in pagina, se lo vogliono va nella chiusura.
- **Motto** "I valori di sempre, lo sguardo al futuro" (catalogo p. 2): se lo usano ancora.
- **Social**: nel piede solo YouTube (5 video) e Facebook. Instagram (https://www.instagram.com/dieffepiu_srl/, risponde 429, non verificato) è tolto finché non confermano che il profilo è attivo.
- **Lingue**: IT, EN e DE in testata (da 961 px in su) e in fondo al menu del telefono puntano a `/`, `/en/` e `/de/`, pagine che il sito nuovo deve avere (oggi il sito traduce con le bandiere sulla stessa pagina).

## Foto da rifare dal vero

Tutte le foto in pagina sono dell'azienda, ma nessuna è all'altezza di un sito di fascia alta: servono una giornata di still life e mezza giornata nel capannone prima della messa in linea. Dopo il giro 3 in pagina restano tre foto (cingolo, testate, rotoli): l'area coperta da foto è il 30 % a 1440, sotto il 35 % della guida. Non è un difetto da nascondere con foto di repertorio: è la prima cosa da chiedere all'azienda.
- **Still life (una giornata)**, fondo carta chiaro e caldo, luce morbida da sinistra in alto con un pannello di schiarita a destra, ombra di contatto corta, almeno 6000 px sul lato lungo, file grezzi:
  - il cingolo TANK da solo, arrotolato, con gli occhielli verso sinistra (così non serve specchiare la foto), ripreso dall'alto a circa 35 gradi, senza guide o altri pezzi che lo tocchino;
  - il kit TANK disposto con aria tra i pezzi;
  - testate e supporti in tre gruppi piccoli invece che in un mucchio;
  - lo spazzolino in due giri (oggi la foto è del vecchio sito, 1900 px);
  - il freno FX135, una testata con la molla, la sezione di un cassonetto, un rotolo di rete, se servono le schede.
- **Capannone di via Lombardia (mezza giornata, necessaria)**, luce naturale, nessun flash: il banco ATT030 per intero di tre quarti; l'operatore di spalle che carica il rotolo; la saldatura della fettuccia in macro; ATT001-B e ATT007 interi (così il selettore può cambiare anche la foto); i rotoli di fettuccia in magazzino a 4000 px o più. Il fotogramma dell'ATT030 tratto dal video YouTube è stato tolto (morbido, compresso): quando ci saranno le foto vere, il selettore delle macchine può cambiare anche la foto. La sede del sito di oggi è un rendering.
- **Diritti**: chi ha scattato le foto su bianco, quelle di difranco.it e i video, e con quali diritti.

## Licenze

- **Carattere**: Pathway Extreme, Google Fonts, SIL Open Font License 1.1 (uso commerciale libero), file e licenza in `sito/fonts/`.
- **Foto**: in pagina solo foto dell'azienda (sito dieffepiu.it, vecchio sito difranco.it con la stessa P.IVA, anteprima del loro video YouTube). Nessuna foto di repertorio, nessuna immagine generata. Le foto Unsplash e Pexels in `assets/esterne/` non sono usate nella home finale (licenze in `assets/CREDITI.md`).

## Logo

- Usato `assets/originali/logo-dieffepiu-1396x857.png` (PNG trasparente del sito), tagliato sopra la riga piccola "SISTEMI PER ZANZARIERE" (a quelle misure sarebbe alta 4-7 px; la frase del piede lo dice già) ed esportato in WebP senza perdita a 2x: `logo-100.webp` in testata (mostrato a 50 px), `logo-208.webp` nel piede (mostrato a 104 px). Icona: `logo-favicon-apple-icon-180x180.png`.
- Nessun vettoriale trovato (il sito non ha SVG, il catalogo è rasterizzato). Non l'ho ricostruito in SVG: il segno DF+ si potrebbe, le scritte "DIEFFE+" e "SISTEMI PER ZANZARIERE" non si rifanno fedeli. Da chiedere: il file vettoriale originale e chi l'ha disegnato.

## Pagine che il piede presuppone

I link del piede vanno alle pagine del sito nuovo (oggi non esistono) o alle sezioni della home:
- Sistemi: `/sistemi/tank`, `/sistemi/plixi`, `/sistemi/flexal-kit`, `/sistemi/kit-transformer`, `/sistemi/rolly-style`, `/componenti`, `/sistemi` (tutte le linee).
- Macchine: `/macchine/banchi`, `/macchine/saldatrici`, `/macchine/tubi-rete`, `/macchine/bottonatrice`, `/macchine/presse`, `/macchine/kit-banco`.
- Azienda: `/azienda`, `/news` (fiere e novità), catalogo PDF (`https://dieffepiu.it/catalogo.pdf`, 76 MB: per il sito nuovo meglio un PDF leggero o schede per linea), `/login` (area riservata), `#contatti`.
- Lingue: `/` (italiano), `/en/`, `/de/`.
- Recapiti nel piede, uguali in ogni pagina: tel:+390498791175, mailto:info@dieffepiu.it, via Lombardia 33 con il link alla mappa.
- Seguici: YouTube e Facebook (indirizzi in `01-analisi.md`, sezione 8). Privacy e Cookie restano su iubenda.

## Newsletter

Ha senso: una fiera quasi ogni anno (MADE expo e BATIMAT), un catalogo che si aggiorna e clienti professionali già registrati nell'area riservata. Il modulo "Fiere e aggiornamenti del catalogo" nel piede ha campo email, bottone e casella del consenso, ma **non invia nulla finché non si collega a un servizio** (per esempio Brevo o Mailchimp, con doppia conferma); all'invio valido (email e consenso) la pagina scrive "Grazie. L'iscrizione non è ancora attiva: il modulo va collegato al servizio di invio.", un messaggio provvisorio da sostituire con quello vero. Serve anche chi la scrive e un testo del consenso approvato nell'informativa.
