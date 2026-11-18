# Bottega dell'Arte: home, nota

## Livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP a più larghezze), caratteri in `sito/fonts/`. La home com'era prima di questo passaggio (pagina e screenshot, con la sua nota) è copiata in `_prova/versione-1-originale/`.

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari), sezione B (difetti delle nostre home), sezione C (15 regole); scheda d'uso e d'identità `_prova/uso/SCHEDA.md`. Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14, le pagine intere di Joseph Brot e Union (a pezzi).

Rifare tutto: `sh _prova/script/build_finale.sh --immagini` (immagini con `pro_img.py`, screenshot con `pro_scatti.mjs`, controlli con `pro_controlli.mjs`, posizioni dei compiti con `pro_misura.mjs`). Elementi che escono a destra: `node _prova/script/pro_largo.mjs sito/index.html <larghezza>`.

Screenshot (stessi nomi di prima): `home-1440.jpg` (8791 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (10998 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Dove siamo" al piede). Guardati a pezzi a 390 e 1440 accanto ai riferimenti, e a 320, 768, 1024 e 1920.

### Ritocco finale (3 novembre 2026, dopo il controllo del livello e la prova con i clienti tipo)

- **Apertura a 1440**: la foto del sottoscala è ora verticale 3:4 (taglio 675x900 dall'originale 1600x900, mostrata a 599x799, mai ingrandita), dal bordo della testata al fondo della prima schermata, a filo del bordo destro. A sinistra, su sette colonne: occhiello, titolo su tre righe, la prova, i quattro bottoni su due righe (Chiama la bottega e Manda una foto o un disegno; Mauro e Giuliano), indirizzo con Indicazioni, "Chiamate prima di passare" e l'email in chiaro (mailto "Disegno da preventivare"), i tre mestieri come link e il motto come firma in chiusura. Da 1920 la foto resta a 675 px.
- **Apertura a 390**: taglio 16:9 più stretto (1150x647 dall'originale), senza il lampadario e la pianta del cliente.
- **Realizzazioni**: tre dati veri per ogni lavoro, presi da `_prova/crawl/progetti.txt` e da `/restauri/` (Bo: firma Gio Ponti, i pezzi, i complimenti dei responsabili dell'Università; pasticceria: su disegno del committente, frassino massiccio e ferro nero, la realizzazione del negozio; centro estetico: dal mobilio ai lettini, incassi per i led, arredo completo su misura). Tutte e tre le foto a 737 px a 1440, più di metà pagina. La pasticceria ora è il banco vetrina (`Bolzano-4`, 4:3) invece del panorama con il pavimento curvo e l'insegna; il centro estetico è il mobile con il lavabo in una cabina (`2020-05_819`) invece della reception con i flaconi di altri marchi e il logo del cliente. La bussola del Bo è l'unica immagine ingrandita, del 10 per cento (667 -> 740 px, Lanczos), per stare a metà pagina: va rifatta (LEGGIMI).
- **Scheda "Negozi e locali"**: gli sgabelli in frassino e ferro nero sotto il bancone (`Bolzano-14`, taglio senza l'insegna).
- **Numeri**: "2 soci, Mauro e Giuliano, che curano la posa di persona, senza personale esterno"; "22 lavori documentati, dalle cucine al Palazzo del Bo"; "8 lavori con il colore fatto al campione". Restano quattro cifre, tutte dalle fonti.
- **Tipografia**: elenchi delle schede, testi dei numeri e dati dei lavori a 18 px a 1440 (prima 16); i titoli dei quattro passi in Zodiak come gli altri titoli (prima sans 700), senza il contatore. A 390 gli elenchi delle schede restano in riga a 16 px, con le parole chiave in grassetto (Cucine, Armadi a muro, Finestre, Balconi, scuri, Portoncini, blindate Dierre...).
- **Restauro**: la didascalia del portone occupa tutta la riga del dittico (il selettore era sbagliato), 16 px, bianco al 78 per cento. Sotto "Manda una foto del pezzo" la riga "Si apre la tua posta: allega le foto dalla galleria e invia."; sotto "Puoi anche portarlo in bottega" due bottoni da 48 px, Chiama 049 900 4916 e Indicazioni (prima erano link nel testo alti 21 px).
- **Dove siamo**: a 390 la tabella scrive solo "Mauro" e "Giuliano" e non va a capo nei nomi; i numeri della tabella sono bersagli di 44 px; l'email va a capo a 320 invece di allargare la pagina.
- **Testata e menu**: a 390 la testata è alta 72 px; il menu aperto ha fondo pieno, separatori, ombra, i bottoni Mauro e Giuliano in fondo, e il bottone dice "Chiudi".
- **Link**: le pagine interne puntano agli indirizzi del sito di oggi in forma assoluta (`https://www.bottegadellartesnc.it/arredo/`, `serramenti/`, `restauri/`, `azienda/`, `progetti/`, `progetti/universita-di-padova/`, `progetti/pasticceria-bolzano/`, `progetti/centri-eststici/`, `cookie-policy/`: tutti rispondono 200 il 3/11/2026), così anche nella proposta statica portano a una pagina vera.
- Lo script delle sostituzioni è `_prova/script/ritocco_finale.py` (già applicato, non va rilanciato).

### Che cosa era cambiato nel passaggio precedente, in breve

- **Struttura della famiglia B adattata a una falegnameria su chiamata**: testata fissa con "Dove siamo" come prima voce e il telefono della bottega in un bottone pieno; apertura con il mestiere e il luogo, la prova, i tre telefoni con il nome, "Manda una foto o un disegno", indirizzo con Indicazioni e "Chiamate prima di passare", e la loro foto vera del sottoscala; "Cosa facciamo" in quattro schede con la foto del lavoro; il restauro con il prima e dopo vero del portone su blocco scuro; "Come lavoriamo" su blocco marrone con quattro numeri, quattro passi e la fascia dei materiali e marchi; tre realizzazioni con il committente o il luogo; "Dove siamo" con la scheda della bottega e il modulo che chiede il tipo di lavoro; piede in quattro colonne.
- **Titolo**: il motto della versione 1 ("L'arte di lavorare il legno come nel passato") è la firma a 1440, non il titolo (scheda d'identità, par. 5 e 7). Il titolo dice il mestiere con le loro parole.
- **Foto, decisione "niente"**: nessuna foto di repertorio e nessuna illustrazione. Solo foto loro, alla misura che reggono, con lo stesso trattamento (`pro_img.py`).
- **Colori dal marchio**: bianco del loro sito, marrone del logo #6F3219 per tutti i bottoni, le cifre e il blocco "Come lavoriamo", noce scuro #21170F per il testo, il blocco del restauro e il piede, due grigi neutri.
- **Tipografia**: le stesse due famiglie della versione 1, con ruoli fissi: Zodiak 400 per titoli, cifre e firma; Schibsted Grotesk 400 e 700 per testo, etichette e bottoni.

### Esito regola per regola (`_prova/script/pro_controlli.mjs` e screenshot, dopo il ritocco)

1. **Telefono in testata fissa, sempre visibile**: PASSA. A 390, a metà pagina, il bottone "049 900 4916" è a 12 px dall'alto, alto 48 px, toccabile; testata alta 80 px a 1440 e 72 a 390; 14 link `tel:` in pagina (con Mauro e Giuliano nel menu aperto); "Dove siamo" è la prima voce del menu.
2. **Prima schermata con mestiere, luogo, prova, azione**: PASSA a 1440x900 e 390x844. Occhiello e titolo dicono il mestiere, "Mestrino" c'è, la prova è "40 anni di esperienza e i restauri al Palazzo del Bo", "Chiama la bottega 049 900 4916" finisce a 578 px (1440) e a 631 px (390), dove è largo quanto il contenuto (350 su 350).
3. **Immagine vera nell'apertura**: PASSA. Il loro sottoscala a otto ante con la nicchia in ottone, in una casa vera: a 1440 verticale dal bordo della testata a 879 px (599x799), a 390 a tutta larghezza in 16:9. Non scontornato. Persone al lavoro (loro sui ponteggi al Bo) nella scheda Restauro, la sede in "Dove siamo".
4. **Zero repertorio**: PASSA. "indicativ" 0, "unsplash" e "pexels" 0; tutte le immagini vengono da `assets/originali` (`pro_img.py`). Una sola è ingrandita, la bussola del Bo, del 10 per cento.
5. **Foto in serie**: NON PASSA DEL TUTTO. Formati: 3:4 e 4:3 a 1440; 16:9, 4:3 e 3:4 a 390; una sola didascalia (il portone) su 11 foto; stesso trattamento di livelli, bilanciamento, caldo, contrasto e saturazione. Tolti il panorama distorto della pasticceria e i flaconi di altri marchi. Restano foto di telefono con luci diverse (il flash sulla bussola del Bo, il sole a picco sul capannone, il portone "prima" sul cemento del laboratorio): serve un servizio fotografico (LEGGIMI, "Foto da rifare dal vero").
6. **Palette dal marchio**: PASSA. Due colori (marrone del logo #6F3219, noce #21170F) più bianco e tre grigi neutri; nessun `--carta`.
7. **Scala corta e leggibile**: PASSA. 1440: 120, 86, 48, 26, 20, 18, 16, 14 px (8); 390: 56, 40, 30, 22, 17, 16, 14 px (7). Testo corrente 18/17 px (a 1440 anche elenchi, numeri e dati dei lavori); nessun testo sotto i 14 px; titolo 86 px, interlinea 1,0 (a 390 40 px). Il titolo non è in maiuscolo: la scheda d'identità sconsiglia l'aria da insegna di lusso.
8. **Due famiglie**: PASSA. Zodiak per tutti i titoli (anche i passi) e le cifre, Schibsted Grotesk per testo, etichette e bottoni.
9. **Servizi in schede con la foto**: PASSA. Quattro schede in quattro colonne (due a 768 e 1024, elenco compatto a 390), tutte cliccabili, foto 4:3 per tutte.
10. **Almeno tre tipi di prove**: NON PASSA. Ci sono quattro numeri (40, 2, 22, 8, tutti dalle fonti) e la fascia "Materiali e marchi che usiamo" in testo, senza loghi; un solo cliente con il nome (Università di Padova, Palazzo del Bo). Recensioni: nessuna nelle fonti. Non è stato inventato niente: il LEGGIMI chiede recensioni, nomi dei clienti e loghi dei fornitori.
11. **Lavori con un nome**: PASSA IN PARTE. Tre lavori con committente o luogo, tre dati veri ciascuno e la foto a 737 px su 1440, più di metà pagina. Manca l'anno: le schede del sito sono del 2020, ma non è la data del lavoro (LEGGIMI). I nomi della pasticceria e del centro estetico non sono scritti finché il cliente non lo permette.
12. **Ritmo a blocchi**: PASSA. Blocchi pieni oltre al piede: restauro (noce) e come lavoriamo (marrone), più due blocchi grigio chiaro; spazio tra le sezioni 128 px a 1440, 64 px a 390; margini 80/20 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno e a filo, raggio 3 px, 48-52 px, testo 16 px; ogni bottone di chiamata ha il numero.
14. **Modulo e "dove e quando"**: PASSA CON RISERVA. Modulo con il tipo di lavoro in quattro caselle, comune, due righe; compone un'email con oggetto (da collegare a un servizio, LEGGIMI). La bottega ha la sua scheda con foto, tabella, "Chiama" e "Indicazioni"; nessun iframe. Gli orari non ci sono (fonte non ufficiale): al loro posto "Chiamate prima di passare".
15. **Piede completo**: PASSA, senza certificazioni (non ce ne sono nelle fonti). Ragione sociale, sede legale, P.IVA, indirizzo con Indicazioni, i tre telefoni, email, "Chiamate prima di passare", privacy e cookie, quattro colonne, testo di almeno 14 px.

### Respinto o rimandato nel ritocco, con il motivo

- Foto del Bo da un file 700x525: l'originale è 700x500, un 700x525 sarebbe comunque un ingrandimento; usato l'ingrandimento del 10 per cento con Lanczos, dichiarato.
- Firma "sotto l'H1": messa in chiusura del blocco di testo, sotto i mestieri; sotto il titolo spingeva i bottoni di chiamata in basso e la riga dei mestieri fuori dalla prima schermata.
- Una voce per riga negli elenchi delle schede a 390: spingeva il prima e dopo del restauro a 2707 px, oltre i 2500 del compito "chi ha un pezzo da salvare"; al suo posto le parole chiave in grassetto.
- Titolo e frase del restauro prima del dittico a 390: per la stessa ragione (le foto finirebbero oltre i 2500 px); il dittico resta subito sotto l'occhiello "Restauro".
- Più coppie prima e dopo (portoncino, balconi) e foto da ingrandire al tocco: non in questo ritocco. Il portoncino `Portoncino-prima-e-dopo1` è già un'unica immagine montata da loro, in un altro formato; le prossime coppie vanno fotografate come quella del portone (LEGGIMI).
- Orari, recensioni, anni dei lavori, nomi dei clienti, loghi dei fornitori, WhatsApp: non nelle fonti, chiesti nel LEGGIMI.
- Accorciare la pagina: 8791 px a 1440 e 10998 a 390; ogni sezione serve a un compito della scheda.

### Compiti della scheda (`pro_misura.mjs`, dopo il ritocco)

- **Privato, 390x844**: mestiere e Mestrino a 92-240 px; `tel:+390499004916` alto 48 px a 583 px (e in testata a 12 px, fisso); Mauro e Giuliano con il nome a 641 px; "cucine" a 1259, "armadi" a 1282, "finestre" a 1468, "scuri" a 1514, ognuno nella sua scheda cliccabile (link al sito di oggi, che risponde); Indicazioni a 753 px (bersaglio di 47 px) con "Chiamate prima di passare" sotto. Come prima o meglio: in più le parole chiave in grassetto e il menu con i due cellulari.
- **Chi ha un pezzo da salvare, 390x844**: "Manda una foto o un disegno" (mailto con oggetto e traccia) a 701 px; le parole del restauro (mobili antichi, porte, portoni, finestre) a 1700; prima e dopo a 2249-2477 px (entro i 2500); "Manda una foto del pezzo" con la riga su cosa mandare e su come allegare; indirizzo, "chiamate prima", Chiama e Indicazioni come bottoni da 48 px nella stessa sezione. Come prima o meglio.
- **Committente, 1440x900**: email in chiaro (mailto "Disegno da preventivare") a 685-734 px, "Manda una foto o un disegno" a 526 px, i mestieri e "Realizzazioni" come link a 757 px, il motto a 822; "disegni di architetti o semplici schizzi", posa e verniciatura in laboratorio a 1253 px; "Negozi e bar conto terzi" e le foto del negozio e del Bo nelle schede a 1402-1628 px. Come prima o meglio.

### Controlli generali (dopo il ritocco)

- Scorrimento orizzontale: nessuno a 320, 360, 390, 768, 1024, 1280, 1440, 1920, 2560 (corretto a 320 la tabella di "Dove siamo", che arrivava a 347 px per l'email e i nomi senza a capo).
- Sovrapposizioni: nessuna negli screenshot guardati a pezzi a 390 e 1440, e nelle prime schermate a 320, 768, 1024, 1920 e con il menu aperto a 390 (corretti i bottoni di Mauro e Giuliano nel menu, che uscivano dalla colonna: ora uno per riga).
- Collegamenti: `tel:+390499004916`, `tel:+393477641720`, `tel:+393474109263`; `mailto:info@bottegadellartesnc.it` (con oggetto "Foto o disegno da valutare", "Restauro: foto del pezzo", "Disegno da preventivare" e quello del modulo); Indicazioni `google.com/maps/dir/?api=1&destination=Bottega dell'Arte, Via Levico 18, 35035 Mestrino PD`; nessuna ancora rotta. Le pagine interne sono indirizzi assoluti del sito di oggi, tutti con risposta 200 il 3/11/2026.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script; "indicativ", "unsplash", "pexels" 0 nella pagina.

### Caratteri e licenze

- Zodiak 400, Indian Type Foundry, da Fontshare, ITF Free Font License (uso commerciale gratuito).
- Schibsted Grotesk (variabile, usati 400 e 700), Google Fonts, SIL Open Font License 1.1 (`sito/fonts/OFL-Schibsted-Grotesk.txt`).
- File serviti dalla pagina in `sito/fonts/`, dettagli in `sito/fonts/LICENZE.txt`.

### Non applicato, apposta

- Apertura a tutto schermo (famiglia B, punto 2): la foto più bella che hanno è 1600x900 da telefono; a tutto schermo a 1440 sarebbe morbida e toglierebbe in prima schermata i tre telefoni e "Manda una foto", che per la scheda vengono prima. Dopo il ritocco è a tutta altezza della prima schermata, sulle ultime cinque colonne e a filo del bordo destro.
- Novità di stagione e newsletter (punti 6 e 9): il sito è fermo al 2021, non hanno social né novità da raccontare.
- Tabella degli orari: non confermati (LEGGIMI).
- Fascia di loghi dei fornitori: nessun file di logo loro né permesso; la fascia dei materiali è in testo.
- WhatsApp: non confermato che si possa scrivere ai 347 (LEGGIMI).

La nota della versione precedente è in `_prova/versione-1-originale/screenshot/home/NOTA.md`.
