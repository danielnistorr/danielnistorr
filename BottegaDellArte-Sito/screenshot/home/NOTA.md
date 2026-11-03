# Bottega dell'Arte: home, nota

## Livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP a più larghezze), caratteri in `sito/fonts/`. La home com'era prima di questo passaggio (pagina e screenshot, con la sua nota) è copiata in `_prova/versione-1-originale/`.

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari), sezione B (difetti delle nostre home), sezione C (15 regole); scheda d'uso e d'identità `_prova/uso/SCHEDA.md`. Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14, le pagine intere di Joseph Brot e Union (a pezzi).

Rifare tutto: `sh _prova/script/build_finale.sh --immagini` (immagini con `pro_img.py`, screenshot con `pro_scatti.mjs`, controlli con `pro_controlli.mjs`, posizioni dei compiti con `pro_misura.mjs`). Elementi che escono a destra: `node _prova/script/pro_largo.mjs sito/index.html <larghezza>`.

Screenshot (stessi nomi di prima): `home-1440.jpg` (8545 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (10952 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Dove siamo" al piede). Guardati a pezzi a 390 e 1440 accanto ai riferimenti, e a 320, 768, 1024 e 1920.

### Che cosa è cambiato, in breve

- **Struttura della famiglia B adattata a una falegnameria su chiamata**: testata fissa con "Dove siamo" come prima voce e il telefono della bottega in un bottone pieno; apertura con il mestiere e il luogo (occhiello "Falegnameria a Mestrino, Padova", titolo "Arredi su misura, serramenti e restauro"), la prova (40 anni di esperienza, i restauri al Bo), Chiama la bottega, Mauro e Giuliano con il loro numero, "Manda una foto o un disegno", indirizzo con Indicazioni e "Chiamate prima di passare", e la loro foto vera del sottoscala; "Cosa facciamo" in quattro schede con la foto del lavoro; il restauro con il prima e dopo vero del portone su blocco scuro; "Come lavoriamo" su blocco marrone con quattro numeri, quattro passi e la fascia dei materiali e marchi; tre realizzazioni con il committente o il luogo; "Dove siamo" con la scheda della bottega (foto del capannone, tabella dei recapiti, Chiama e Indicazioni) e il modulo che chiede il tipo di lavoro; piede in quattro colonne.
- **Titolo**: il motto della versione 1 ("L'arte di lavorare il legno come nel passato") non è più il titolo ma la firma accanto alla foto a 1440, come chiede la scheda d'identità (par. 5 e 7: "come firma, non come titolo"; a 390 la frase che diceva cosa fanno era nascosta). Il titolo ora dice il mestiere con le loro parole.
- **Foto, decisione "niente"**: nessuna foto di repertorio e nessuna illustrazione. Solo foto loro, alla misura che reggono: il sottoscala (16:9 a 390, taglio 4:3 a 1440), libreria, portafinestra con gli scuri, loro sui ponteggi al Bo, banco della pasticceria (schede 4:3), portone prima e dopo (3:4), bussola del Bo (mai ingrandita: 667 px), negozio vicino a Bolzano, centro estetico, capannone (4:3). Stesso trattamento per tutte (`pro_img.py`). Tolte rispetto alla versione 1: il portone a tutta altezza con l'interruttore Prima/Dopo in apertura, il maniglione, la porta a bilico, le porte a vetri piombati, le porte scorrevoli del Bo.
- **Colori dal marchio**: niente più calce e pavimento beige. Bianco del loro sito, marrone del logo #6F3219 per tutti i bottoni, le cifre e il blocco "Come lavoriamo", noce scuro #21170F per il testo, il blocco del restauro e il piede, due grigi neutri.
- **Tipografia**: le stesse due famiglie della versione 1, con ruoli fissi: Zodiak 400 per titoli, cifre e firma; Schibsted Grotesk 400 e 700 per testo, etichette e bottoni.
- **Uso**: ogni compito della scheda è nella prima schermata o a uno o due passi (misure sotto).

### Esito regola per regola (controlli di `_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile**: PASSA. A 390, a metà pagina, il bottone "049 900 4916" è a 10 px dall'alto, alto 48 px, toccabile; 12 link `tel:` in pagina; "Dove siamo" è la prima voce del menu.
2. **Prima schermata con mestiere, luogo, prova, azione**: PASSA a 1440x900 e 390x844. Occhiello e titolo dicono il mestiere, "Mestrino" c'è, la prova è "40 anni di esperienza e i restauri al Palazzo del Bo", il bottone "Chiama la bottega 049 900 4916" finisce a 692 px (1440) e a 627 px (390), dove è largo quanto il contenuto (350 su 350).
3. **Immagine vera nell'apertura**: PASSA. Il loro sottoscala a otto ante con la nicchia in ottone, in una casa vera (il prodotto vero, famiglia B): 708x531 a 1440, a tutta larghezza a 390; non scontornato. Persone al lavoro (loro sui ponteggi al Bo) nella scheda Restauro, la sede in "Dove siamo".
4. **Zero repertorio**: PASSA. "indicativ" 0; nessuna immagine da banche, nessuna da `assets/esterne/`.
5. **Foto in serie**: PASSA, con il limite delle foto da telefono. Formati: 4:3 e 3:4 a 1440, 16:9, 4:3 e 3:4 a 390; una sola didascalia (il portone) su 11 foto; stesso trattamento di livelli, bilanciamento, caldo, contrasto e saturazione.
6. **Palette dal marchio**: PASSA. Due colori (marrone del logo #6F3219, noce #21170F) più bianco e tre grigi neutri; nessun `--carta`.
7. **Scala corta e leggibile**: PASSA. 1440: 120, 86, 48, 26, 20, 18, 16, 14 px (8); 390: 56, 40, 30, 22, 17, 16, 14 px (7). Testo corrente 18/17 px; nessun testo sotto i 14 px; titolo 86 px, interlinea 1,0 (a 390 40 px). Il titolo non è in maiuscolo: la scheda d'identità sconsiglia l'aria da insegna di lusso.
8. **Due famiglie**: PASSA. Zodiak e Schibsted Grotesk.
9. **Servizi in schede con la foto**: PASSA. Quattro schede in quattro colonne (due a 768 e 1024, elenco compatto a 390), tutte cliccabili, foto 4:3 per tutte: Per la casa (`arredo/`), Finestre e porte (`serramenti/`), Restauro (`restauri/`), Negozi e locali (`progetti/pasticceria-bolzano/`).
10. **Almeno tre tipi di prove**: PASSA IN PARTE. Quattro numeri (40 anni di esperienza, 2 soci, 22 lavori raccontati, 8 con colorazione al campione, contati sulle loro schede); fascia "Materiali e marchi che usiamo" (porte blindate Dierre, corian, vetrocamera con gas argon, multistrato marino certificato, okumè, vernici all'acqua) al posto dei fornitori con logo; un solo cliente con il nome (Università di Padova, Palazzo del Bo). Recensioni: nessuna nelle fonti, non inventate (LEGGIMI).
11. **Lavori con un nome**: PASSA IN PARTE. Tre lavori con committente o luogo e due dati ciascuno (Palazzo del Bo, Università di Padova; una pasticceria vicino a Bolzano; un centro estetico a Lissaro), foto di 737 px (il Bo 667, la sua misura nativa). Manca l'anno: le schede del sito sono del 2020, ma non è la data del lavoro (LEGGIMI). I nomi della pasticceria e del centro estetico non sono scritti finché il cliente non lo permette.
12. **Ritmo a blocchi**: PASSA. Blocchi pieni oltre al piede: restauro (noce) e come lavoriamo (marrone), più due blocchi grigio chiaro (cosa facciamo, dove siamo); spazio tra le sezioni 128 px a 1440, 64 px a 390; margini 80/20 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno e a filo, raggio 3 px, 48-52 px, testo 16 px; ogni bottone di chiamata ha il numero.
14. **Modulo e "dove e quando"**: PASSA IN PARTE. Modulo con il tipo di lavoro in quattro caselle (arredo per la casa, finestre e porte, restauro, negozio o locale su disegno), comune, due righe; compone un'email con oggetto (da collegare a un servizio, LEGGIMI). La bottega ha la sua scheda con foto, tabella, "Chiama" e "Indicazioni" (percorso su Google Maps); nessun iframe. Gli orari non ci sono: l'unica fonte è una directory non ufficiale; al loro posto "Chiamate prima di passare".
15. **Piede completo**: PASSA, senza certificazioni (non ne hanno). Ragione sociale "Bottega dell'Arte Snc di Nosarini Mauro e Saibene Giuliano", sede legale, P.IVA, indirizzo della bottega con Indicazioni, i tre telefoni, email, "Chiamate prima di passare", privacy e cookie, quattro colonne, testo di almeno 14 px.

### Compiti della scheda (`pro_misura.mjs`)

- **Privato, 390x844**: mestiere e Mestrino a 88-236 px; `tel:+390499004916` alto 48 px a 579 px (e in testata a 10 px); Mauro e Giuliano con il nome a 637 px; "finestre" a 1464, "scuri" a 1510, "armadi" e "cucine" a 1255, ognuno nella sua scheda cliccabile; Indicazioni a 749 px (bersaglio di 47 px) con "Chiamate prima di passare" accanto.
- **Chi ha un pezzo da salvare, 390x844**: "Manda una foto o un disegno" (mailto con oggetto e traccia) a 697 px; le parole del restauro (mobili antichi, porte, portoni, finestre) a 1696; prima e dopo a 2222-2450 px; "Manda una foto del pezzo" con la riga su cosa mandare, indirizzo, "chiamate prima" e telefono nella stessa sezione.
- **Committente, 1440x900**: email in chiaro (mailto con oggetto "Disegno da preventivare") a 699 px e "Manda una foto o un disegno" a 768; "disegni di architetti o semplici schizzi", posa e verniciatura in laboratorio a 1251 px; "Negozi e bar conto terzi" e le foto del negozio e del Bo nelle schede a 1400-1626 px.

### Controlli generali

- Scorrimento orizzontale: nessuno a 320, 360, 390, 768, 1024, 1280, 1440, 1920, 2560. Corretti durante il lavoro: i bottoni dei cellulari a 390 (473 px), ora con il nome sopra il numero; "Chiama la bottega" a 320, che va a capo: sotto i 375 px dice "Chiama 049 900 4916".
- Sovrapposizioni: nessuna negli screenshot a 320, 390, 768, 1024, 1440, 1920 e con il menu aperto a 390. Corretti: la didascalia del portone staccata dalle foto a 1440, lo spazio doppio nel bottone di chiamata.
- Collegamenti: `tel:+390499004916`, `tel:+393477641720`, `tel:+393474109263`; `mailto:info@bottegadellartesnc.it` (con oggetto "Foto o disegno da valutare", "Restauro: foto del pezzo", "Disegno da preventivare" e quello del modulo); Indicazioni `google.com/maps/dir/?api=1&destination=Bottega dell'Arte, Via Levico 18, 35035 Mestrino PD`; nessuna ancora rotta. I link relativi (`arredo/`, `serramenti/`, `restauri/`, `progetti/...`, `azienda/`, `cookie-policy/`) sono gli indirizzi del sito di oggi.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.

### Caratteri e licenze

- Zodiak 400, Indian Type Foundry, da Fontshare, ITF Free Font License (uso commerciale gratuito).
- Schibsted Grotesk (variabile, usati 400 e 700), Google Fonts, SIL Open Font License 1.1 (`sito/fonts/OFL-Schibsted-Grotesk.txt`).
- File serviti dalla pagina in `sito/fonts/`, dettagli in `sito/fonts/LICENZE.txt`.

### Non applicato, apposta

- Apertura a tutto schermo (famiglia B, punto 2): la foto più bella che hanno è 1600x900 da telefono; a tutto schermo a 1440 sarebbe morbida e toglierebbe in prima schermata i tre telefoni e "Manda una foto", che per la scheda vengono prima. È a metà pagina, a filo del bordo destro.
- Novità di stagione e newsletter (punti 6 e 9): il sito è fermo al 2021, non hanno social né novità da raccontare.
- Tabella degli orari: non confermati (LEGGIMI).
- Fascia di loghi dei fornitori: nessun file di logo loro né permesso; la fascia dei materiali è in testo.
- WhatsApp: non confermato che si possa scrivere ai 347 (LEGGIMI).

La nota della versione precedente è in `_prova/versione-1-originale/screenshot/home/NOTA.md`.
