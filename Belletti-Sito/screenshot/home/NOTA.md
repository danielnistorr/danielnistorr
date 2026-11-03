# Home Belletti

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh`: immagini con `pro_img.py`, controllo dei testi e delle immagini citate, screenshot con `shot_finale.mjs`, poi `pro_controlli.mjs` (le 15 regole, esito anche in `_prova/pro_controlli.json`) e `pro_prova.mjs` (menu, ancore, modulo).

La home di prima ("Il carattere dell'edificio", con la sua NOTA e i suoi screenshot) è copiata com'era in `_prova/versione-1-originale/`.

Screenshot, stessi nomi di prima: `home-1440.jpg` (10354 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (14175 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (contatti e piede). Guardati a pezzi a 1440 e 390 accanto ai riferimenti (prime schermate di tutti e 14, pagine intere di Kline e Wilson); prime schermate e pagine intere anche a 320, 768, 1024 e 1920 (PNG cancellati dopo la lettura).

## Livello professionale (3/11/2026)

Richieste del committente: "secondo me non rappresentano bene l'identità e l'utilizzo corretto di quello che dovrebbe essere il sito" e "ancora troppo poco professionale e di design, e design funzionale all'attività"; per le foto "niente" (nessun repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia S (servizi tecnici e imprese), sezioni A, B e C. Scheda d'uso: `_prova/uso/SCHEDA.md`.

### Che cosa è cambiato rispetto alla home di prima

- **Il numero giusto in alto.** Prima in testata e nel bottone verde c'era lo 049 508 2430 degli uffici, e il numero dei guasti era una riga grigia fuori dalla prima schermata (SCHEDA, par. 7). Ora la testata è fissa e il bottone pieno verde è "Guasti 24 ore 049 900 5131"; gli uffici sono il bottone bordato accanto (da 1101 px in su e a 1024; sul telefono solo il numero dei guasti, più il Menu).
- **La prima schermata dice il mestiere.** Il titolo "L'ascensore rispecchia il carattere dell'edificio" è una loro frase ma è un titolo-manifesto: la SCHEDA (par. 5 e 7) chiede che in apertura si legga cosa fanno. È passato a titolo della sezione degli impianti nuovi, dove dice proprio quello. Ora l'H1 è "Ascensori, piattaforme e servoscala" e, nello stesso H1, "Installazione, manutenzione, ammodernamento e assistenza su impianti di qualsiasi marca, nelle province del Veneto e in parte del Friuli." Sopra c'è l'occhiello "Ascensoristi a Mestrino (Padova), dal 1908".
- **La foto d'apertura è la sede con il furgone dell'assistenza** (depliant 2008, `d-027`, targa sfocata): mezzo con il marchio e sede, come chiedono le regole per la famiglia S. A 1440 è un 4:5 di 519 px (nativa 869) a destra del testo, a 390 una striscia che chiude la prima schermata (nativa 869 px per 390).
- **L'assistenza viene subito dopo**: tre garanzie su antracite, poi "La marcia in più di Belletti" con i tre casi della chiamata (persone bloccate, guasto in orario, guasto fuori orario), i servizi, le province e "Fuori zona? Chiamate gli uffici". Sul telefono l'assistenza viene prima delle garanzie, così il caso "fuori orario" si legge in uno scorrimento.
- **Ammodernamento, piattaforme e servoscala** hanno una sezione, con le frasi dell'ing. Viel (La Piazza Web, 2024) e "Chiedete un sopralluogo". Prima la parola ammodernamento non c'era.
- **Lavori**: niente più selettore a schede. I tre lavori si vedono tutti, ognuno con la foto a 740 px (51 % della pagina), il luogo, i cinque dati tecnici verbatim e i progettisti; sotto, Legnago e Cannaregio con il link ai video.
- **Impianti nuovi in sei schede con la foto vera** (prima: sei righe di testo), tutte cliccabili, che aprono il modulo con il tipo già scelto. Sotto, il riquadro "Per i progettisti" con l'email all'ufficio tecnico già scritta (oggetto e cosa allegare).
- **Chi siamo**: "Ascensoristi da quattro generazioni" (non più "tre generazioni"), il racconto della famiglia, quattro numeri, e la fascia "Qualità e norme" con le date di prima emissione e il link per chiedere le copie aggiornate dei certificati.
- **Contatti su verde pieno**: il numero dei guasti a 96 px come titolo, gli uffici, l'email, l'indirizzo con "Indicazioni stradali" e "Apri la mappa", e il modulo per sopralluogo e preventivo.
- **Piede in quattro colonne**, con la Pallavolo Padova (la SCHEDA chiede di non toglierla).
- **Fuori**: il fondo calce e il grigio caldo (beige di comodo), il selettore dei lavori, la foto di Ca' della Nave come apertura, le didascalie da 14 px sotto ogni foto, il peso 300 dei titoli.

### Uso: i compiti della SCHEDA (par. 8)

- **Visitatore 1, telefono 390x844.** Senza scorrere: testata con il bottone 049 900 5131 (48 px, tel:+390499005131); "Guasto o persona bloccata in cabina? L'assistenza risponde 24 ore su 24, 365 giorni all'anno."; bottone a tutta larghezza "Assistenza 24 ore 049 900 5131" (350x56 px, a 493 px); sotto, il bottone bordato degli uffici e i link "Dopo la chiamata", "Sopralluogo", "Lavori"; la striscia della sede chiude lo schermo (691-879 px). "Qualsiasi marca" è nell'H1 (289 px). Il caso fuori orario è a 1564 px, cioè dentro il primo scorrimento (fino a 1688). A metà pagina il bottone della testata si vede e si tocca (misurato con `elementFromPoint`).
- **Visitatore 2, computer 1440x900.** Nella prima schermata: manutenzione e ammodernamento nell'H1, i due numeri, "Chiedete un sopralluogo". Zona per esteso nelle garanzie (da 883 px) e l'elenco delle province da 1744 px. Piattaforme e servoscala sono nell'H1 e nella loro sezione (da 2315 px). Sopralluogo in un passo: tel: uffici, mailto: con oggetto e traccia, oppure il modulo. Orari degli uffici: non pubblicati, quindi non in pagina.
- **Visitatore 3, progettista.** "Progettisti: i lavori" nella prima schermata porta alla sezione con un clic; a 1440 la prima scheda tecnica completa (Galleria Cavour) è a 437-989 px dopo il clic. L'email all'ufficio tecnico è scritta per intero, con cosa allegare. Certificati: niente link a copie scadute, c'è la richiesta delle copie aggiornate.
- Provato con `pro_prova.mjs`: menu aperto e chiuso al tocco; ancore sotto la testata (72 px sul telefono, 88 a 1440); "Chiedete un sopralluogo" e la scheda Montauto scelgono il tipo nel modulo; invio vuoto fermato con l'avviso e il fuoco sul nome; email composta con oggetto "Richiesta: Impianto nuovo: montauto, Selvazzano Dentro" e corpo completo, letta e non inviata; nessun errore di script.

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs`, più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa di 88 px a 1440 e 72 a 390. Bottone pieno "Guasti 24 ore 049 900 5131" di 48 px; a metà pagina si vede e si tocca a 1440 e a 390. 14 link `tel:` (sette per numero), solo `+390499005131` e `+390495082430`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** A 1440x900 e 390x844: il mestiere nell'H1, Mestrino e "dal 1908" nell'occhiello, il bottone di chiamata dei guasti (a 390 largo quanto la colonna, 350 px; a 320, 280 px). Nessuna sovrapposizione tra i blocchi dell'apertura.
3. **Immagine vera nell'apertura: passa.** La sede Belletti con il furgone bianco e verde e il logo sulla fiancata. È del 2008 e non mostra la squadra: la foto da rifare è nel LEGGIMI.
4. **Zero repertorio: passa.** `indicativ` 0 volte; nessuna immagine da banche o da `assets/esterne/`.
5. **Foto in serie: passa, con riserva.** Tre formati (4:5, 4:3, la striscia del telefono), una sola didascalia (l'apertura) su 12 foto. Stesso trattamento per tutte (autocontrasto leggero, saturazione 0,9, contrasto 1,03). La riserva: le foto vengono da tre servizi diversi (depliant 2008, redazionale DiBaio di Ca' della Nave, quattro foto delle gallerie del sito nelle schede), quindi luce e grana non sono identiche.
6. **Palette dal marchio: passa.** Verde #007A43 (il verde del logo #009A54 scurito per il contrasto, bottoni e blocco dei contatti), verde del logo solo sul fondo scuro, una sua variante per il passaggio del mouse, antracite #1C1E20, il grigio del logo #646567 per il testo secondario, neutri freddi. Nessun colore scritto fuori da `:root`. Niente beige.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 19, 24, 32, 48, 72, 96) e 7 a 390 (14, 17, 20, 24, 30, 40, 48). Testo corrente 19 px a 1440 e 17 a 390. Niente sotto i 14 px. H1 72 px (390: 40), H2 48 px (390: 30).
8. **Due famiglie al massimo: passa.** Una sola, Radio Canada, pesi 400 e 700; i titoli e le cifre in larghezza 88 %, come le lettere strette del logo.
9. **Servizi in schede con la foto: passa.** Sei schede in tre colonne a 1440 (due a 1024 e sul telefono), tutte 4:3, con foto vera, nome, una riga e "Sopralluogo e preventivo"; tutta la scheda è un link. Mostrate al massimo a 411 px su originali di 500-822 px. Il servizio di ogni giorno (assistenza e ammodernamento) ha le sue due sezioni, non una scheda.
10. **Almeno tre tipi di prova: passa (3 su 4).** Quattro numeri (4 generazioni, 35 dipendenti, oltre 20 tecnici, 1997); la fascia "Qualità e norme" con didascalia (ISO 9001 DNV, Allegato XI Eurofins, EN 81-28); clienti e progettisti con il nome nei lavori (Comune di Padova, gli architetti Zambusi, Danzi, Rigo). Mancano le recensioni: non ce ne sono nelle fonti (SCHEDA, "Recensioni") e non sono state inventate.
11. **Lavori con un nome: non passa del tutto.** Tre lavori con luogo, cinque dati e foto larga il 51 % della pagina, più Legnago e Cannaregio. L'anno c'è solo per la Galleria Cavour (ottobre 2007): per Ca' Michiel e Ca' della Nave le fonti non lo danno (LEGGIMI).
12. **Ritmo a blocchi: passa.** Blocchi pieni oltre al piede: garanzie e lavori su antracite, contatti su verde; assistenza e impianti su grigio chiaro, il resto bianco. Sezioni a 120 px sopra e sotto a 1440, 72 a 390. Margini di 80 px a 1440 (contenitore 1280) e di 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno verde e bordato, raggio 4 px ovunque, 56 px (48 in testata), testo a 17 px; i bottoni di chiamata contengono il numero (a 24 px).
14. **Modulo e "dove" per il mestiere: passa.** Modulo con nome, telefono, comune e indirizzo dell'impianto, tipo di richiesta (10 voci), urgenza (Appena possibile, Entro un mese, Senza fretta), note facoltative per la marca, e l'istruzione per le foto della targa o del vano (un mailto non porta allegati). I campi da scrivere obbligatori sono tre. Zona: le sette province del Veneto e parte del Friuli, scritte una per una. Nessun iframe di mappa: "Indicazioni stradali" e "Apri la mappa" aprono Google Maps.
15. **Piede completo: passa.** Quattro colonne, testo di almeno 14 px: ragione sociale, P.IVA e C.F., REA, indirizzo con le indicazioni, i due telefoni e l'email cliccabili, l'orario che c'è (assistenza 24 ore su 24; gli orari degli uffici non sono pubblicati), le province, le certificazioni, YouTube con il sottotitolo, Privacy e Cookie, lo sponsor.

### Caratteri e licenze

- **Radio Canada** (The Radio-Canada Project Authors), Google Fonts, SIL Open Font License 1.1, uso commerciale libero. Servita dalla pagina (`sito/fonts/radio-canada-latin.woff2` e `-latin-ext.woff2`), licenza in `sito/fonts/OFL.txt`. È il carattere della home di prima: una famiglia sola.
- **Foto**: solo materiale di Belletti (depliant 2008, gallerie del sito, redazionale DiBaio), con i diritti da chiedere (LEGGIMI). Nessuna foto di repertorio, nessuna immagine generata, nessun disegno. Il logo è il vettoriale vero del depliant.

### Foto in pagina

| File in `sito/img/` | Soggetto | Origine | Mostrata al massimo |
|---|---|---|---|
| `apertura-sede-*` | sede di Mestrino di sera con il furgone | depliant, `d-027` (869x1263), targa sfocata | 519 px su 869 |
| `apertura-sede-striscia-*` | lo stesso, striscia per il telefono | `d-027`, taglio 869x420 | 390-900 px su 869 |
| `assistenza-tecnico-347` | tecnico al quadro | depliant, `d-033` (347x553) | 347 px |
| `ammodernamento-scala-470` | scala del palazzo con la cabina d'epoca | depliant, `d-036` (470x704) | 470 px |
| `lavoro-cavour-*` | Galleria Cavour di sera | depliant, `d-037` (948x1263), 4:3 | 740 px su 948 |
| `lavoro-camichiel-*` | Ca' Michiel, la cabina col mosaico | depliant, `d-020`, 4:3 | 740 px su 790 |
| `lavoro-cadellanave-*` | Ca' della Nave dalla corte | `01_DiBaio_Martellago.pdf` (942x694), senza le panchine, 4:3 | 740 px su 789 |
| `impianto-*` | cabina tonda, torre in vetro, montacarichi, montauto, piattaforma, tappeti mobili | gallerie `fn000008`, `fn000053`, `fn000257`, `fn000165`; depliant `d-002`, `d-030` | 411 px su 500-640 |

### Respinti, con il motivo

- **Il titolo di prima in apertura**: è un manifesto senza il mestiere dentro; la SCHEDA (par. 5, 7 e 8) e la regola 2 chiedono cosa fanno nel titolo. La frase resta, come titolo degli impianti nuovi.
- **Recensioni**: non ce ne sono nelle fonti.
- **Squadra con nome, anni e ruolo (A1, punto 6)**: le fonti nominano solo Gaetano e Irma Belletti e l'ing. Viel, senza foto; niente ritratti inventati. Da chiedere.
- **Ritratti seppia della famiglia (`storia1-4`, 227 px, voto 3)**: troppo piccoli e senza nomi; sarebbero stati il quarto formato in pagina. Da chiedere in originale.
- **Elenco dei comuni (A1, punto 8)**: le fonti dicono "le province del Veneto e in parte del Friuli". In pagina ci sono le sette province; i comuni e la parte del Friuli vanno chiesti.
- **Fascia dei loghi delle certificazioni**: il logo DNV accanto a un certificato di cui online c'è solo la copia scaduta sembrerebbe un certificato valido. Ci sono le date di prima emissione e la richiesta delle copie aggiornate.
- **Promessa dei tempi di risposta accanto al modulo (A6)**: non è nelle fonti.
- **Safety Lift Group per il resto d'Italia**: da confermare (il dominio non risponde); al suo posto "Fuori zona? Chiamate gli uffici".
- **Foto della sede di notte `d-051`**: bella, ma il blocco dei contatti regge senza e la sede è già nell'apertura.

### Controlli fatti (3/11/2026)

- `pro_controlli.mjs`: regole 1-10 e 12-15 superate nelle misure, 11 no (l'anno di due lavori). Nessuna ancora senza destinazione; nessun errore in console.
- Scorrimento orizzontale: nessuno a 320, 360, 390, 768, 1024, 1280, 1440 e 1920 (scrollWidth uguale alla finestra).
- Collegamenti: `tel:+390499005131` (assistenza) e `tel:+390495082430` (uffici); `mailto:info@bellettiascensori.it` con oggetto e traccia per sopralluogo, ufficio tecnico, certificati e modulo; Google Maps con Via della Tecnica 29, 35035 Mestrino (ricerca e indicazioni); YouTube @BellettiAscensori.
- Nessun U+2014 nella pagina, negli script, nella NOTA, nel LEGGIMI e nei CREDITI (controllo dentro `build_finale.sh`).
