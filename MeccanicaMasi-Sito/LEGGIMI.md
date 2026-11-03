# Meccanica Masi: proposta di nuova homepage

Proposta non richiesta, solo la home. Non è pubblicata, l'azienda non è stata contattata.

## Cosa c'è

- `sito/index.html`: la home, livello professionale del 3 novembre 2026 con il ritocco finale (porte a blocchi, numeri e telefono fuori scala, foto in serie, richiesta di intervento); statica, si apre con file:/// o da qualsiasi server. Immagini in `sito/img/` (WebP, solo foto loro), caratteri in `sito/fonts/` (Mona Sans).
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`; `NOTA.md` spiega struttura, scelte ed esito delle 15 regole.
- `_prova/script/build_finale.sh` rifà tutto: logo (`finale_logo.py`), foto (`pro_img.py`), screenshot (`pro_shot.mjs`), controlli (`pro_controlli.mjs`, esito in `_prova/pro_controlli.json`). Le modifiche del ritocco finale sono in `ritocco_css.py`, `ritocco_html.py` e `ritocco_js.py` (già applicate alla pagina, da non rilanciare).
- `_prova/versione-1-originale/`: la home di prima ("Pezzi dal pieno, su disegno"), con sito e screenshot.
- `_prova/uso/SCHEDA.md`: chi apre il sito e per cosa; `01-analisi.md`: i fatti con le fonti.

## Il modulo "Mandateci il disegno" va collegato a un servizio

Oggi il modulo non invia nulla: compone un'email (mailto) a info@meccanicamasi.it con oggetto e campi già scritti, e apre il programma di posta di chi lo compila. Un mailto non porta allegati: il nome del disegno scelto finisce nel testo e la pagina dice di allegarlo a mano. Per chi non ha un programma di posta (posta solo dal browser), dopo "Prepara l'email" la pagina mostra il testo composto con il bottone "Copia il testo". Se si sceglie manutenzione o installazione, titolo e istruzioni della sezione diventano quelli di una richiesta di intervento.

Per il sito vero va collegato a un servizio che riceva i file e li inoltri a info@meccanicamasi.it: per esempio Contact Form 7, che hanno già sul WordPress di oggi, con il campo file aperto a `pdf|dxf|dwg|step|stp|jpg|jpeg|png|heic` (oggi accetta solo immagini, audio e video), un limite di circa 20 MB e una risposta automatica a chi scrive. Stessa cosa per la candidatura di "Lavora con noi" (CV in PDF). Poi, nel codice, al posto di `location.href = url` si invia il modulo al servizio.

## Da chiedere all'azienda

Niente di questo è in pagina come segnaposto.

**Per le prove (regole 10 e 11, oggi non passano)**
- **Recensioni**: la scheda Google esiste (il loro QR porta a `g.page/r/CXwmW46XNK4aEBM/review`, luogo CID 1922531916466824828) ma il testo non si legge in automatico. Chiedere se si possono citare due o tre recensioni con nome e comune; la pagina ha già il link "Le recensioni su Google".
- **Clienti con il nome**: quali tipografie, cartotecniche, sacchettifici o aziende si possono nominare (anche solo il nome e la città), compresa "una delle principali aziende di produzione giornali del Veneto".
- **Anno e luogo dei lavori**: per supporto Man-Roland, pulegge, leva in ghisa, mandrino espansibile, linea giornali, rullo pinza (le schede del vecchio sito hanno "Anno: 2015" e "Wallahia Inc." del tema).
- **Certificazioni o associazioni** vere, se ce ne sono (il NADCAP del vecchio sito è del tema: non citarlo).

**Per chi chiama**
- **Tempi d'intervento**: si può scrivere qualcosa come "in giornata nel padovano"? Oggi la pagina dice "nel minor tempo possibile", come il loro sito, e "Tempi e costi dipendono dalla macchina e dalla distanza: chiedeteli al telefono".
- **Richieste fuori orario**: la pagina, quando sono chiusi, propone "Lasciateci la richiesta per email". Non promette una reperibilità: se ce n'è una (sabato pomeriggio, festivi), dirlo e si aggiunge.
- **Prezzi o diritto di chiamata**: pubblici o no.
- **Orari**: lun-ven 8-18 e sab 8-12 sono dell'officina o solo delle chiamate; se chiudono nei festivi nazionali (la pagina li dà per chiusi, Pasquetta compresa), il 13 giugno (Sant'Antonio, patrono di Padova) e in agosto.
- **WhatsApp sul 348 169 34 51**: se sì, si aggiunge "Mandateci una foto su WhatsApp" accanto a "Mandateci il disegno".
- **Telefono fisso**: c'è solo il cellulare.
- **Fin dove arrivano**: le regioni del sito (Veneto, Friuli, Trentino, Emilia-Romagna) sono tutte servite sul posto? Finché non lo confermano non c'è la cifra "4 regioni" nella fascia dei numeri.

**Per chi manda un pezzo**
- **Misure massime**: diametro e lunghezza al tornio, corsa della fresatrice CNC, spessore della lamiera (oggi la pagina dice "ve le diciamo al telefono, macchina per macchina"); modelli veri dietro i loghi Soraluce, Anselmi, Dahlih, Thomas, Bosch, New Drill (in pagina ci sono solo i nomi dei costruttori).
- **CMM**: la macchina di misura tridimensionale della scheda Man-Roland è loro o di un fornitore (non citata).
- **Gruppi stampa completi e prodotti brevettati** (piede e Lavora con noi del sito di oggi): quali, e se si possono mostrare.

**Su di loro**
- **Anno**: 1977 o "oltre cinquant'anni"? Il sito scrive quattro date diverse; la srl è del 2019. Che legame c'è con "Masi Macchine Grafiche S.R.L." del logo vecchio. Non è in pagina finché non lo confermano.
- **Matteo**: in pagina c'è "Matteo ha raccolto l'eredità del padre" (dal loro Chi siamo); il cognome no. Confermare che va bene.
- **6 persone**: è il dato 2024 di aziende.it; confermare (è la prima cifra della fascia dei numeri).
- **Altri numeri per la fascia** (come barth e Cly-Del): metri quadri dell'officina, interventi o commesse in un anno, anno di fondazione confermato. Oggi le cifre sono quattro: 6 persone, 6 torni, 1 fresatrice CNC a 3 assi, 3 m di lamiera.
- **Dati tecnici dei lavori**: lega del supporto Man-Roland, tipo di cuscinetto, ganasce del mandrino, nastri della linea giornali. Le frasi del vecchio sito che li dicevano ("6082 o 7075", "montato a pressione", "ganasce a settori", "nastri in PVC") non sono nelle fonti salvate e sono state tolte dalla pagina.
- **Cookie**: l'indirizzo della cookie policy iubenda, per il link "Cookie" del piede (oggi c'è solo Privacy).
- **REA**: in pagina PD-450853 (aziende.it, companyreports.it); il sito di oggi scrive "Iscr. Reg. Imp. n. 307590256". Capitale sociale e PEC (aziende.it) non sono in pagina.
- **Cylex** dà anche via delle Gramogne 56, 35127 Padova: forse la sede di prima.
- **Logo**: in pagina la sola scritta vettoriale "meccanica Masi SRL" (nera in testata, bianca nel piede); chiedere quale marchio tengono e un vettoriale del marchio rotondo con l'ingranaggio.
- **Permesso per le foto** della loro libreria e per mostrare i pezzi dei clienti.

## Foto: cosa rifare dal vero e come

La home usa solo foto loro (elenco in `assets/CREDITI.md`), mai ingrandite: le due dell'apertura sono originali di 598 px mostrati a 550. Sono foto da telefono di giorni e luci diverse, rese simili con un trattamento comune deciso (saturazione 0,45, bianco neutro, viraggio freddo) e due soli formati, 2:1 e 4:3. Il servizio che serve, mezza giornata con un solo fotografo e una sola luce:

1. **Apertura, "In azienda da voi"**: un loro tecnico dentro una macchina da stampa di un cliente, mani e attrezzi sul gruppo rulli, la macchina aperta. Orizzontale 2:1, almeno 2400 px. Intanto chiedere l'originale di `IMG20230705092448.jpg` (pulegge e cinghie, 05/07/2023), oggi a 598 px.
2. **Apertura, "In officina da noi"**: il tornio CNC o la Soraluce con un pezzo e una persona al pannello, luce di finestra. Intanto l'originale di `IMG20240312141719.jpg` (tornio sulla puleggia, oggi a 598 px).
3. **Squadra e sede**: le sei persone davanti all'officina di via dell'Artigianato con l'insegna, e il furgone se c'è; serve per "Chi siamo" e per la regola 3 (oggi in pagina non ci sono persone). Le due foto esterne della libreria sembrano Street View: non usate.
4. **Manutenzione**: gli originali senza la scritta "SHOT ON MI" di `IMG_20210409_073157.jpg` (rulli) e `IMG_20210901_112738.jpg` (confezionatrice); meglio rifarle con il tecnico al lavoro.
5. **Lavorazioni**: tornio con il truciolo, fresatrice con il pezzo in tavola, piegatrice con una lamiera lunga, saldatura TIG; tutte 4:3, stessa luce. La foto della lamiera di oggi è un dettaglio poco leggibile.
6. **Un rullo per offset o flexo finito**: manca ed è la loro lavorazione più richiesta.
7. **Lavori**: supporto Man-Roland, pulegge, leva, mandrino e rullo pinza rifatti interi su un solo fondo neutro grigio scuro, stessa luce, orizzontali 4:3 (oggi tappetino verde, carta bianca e banco nero, uniti solo dal trattamento colore; la leva e il mandrino sono tagli di foto verticali).

## Licenze

- **Mona Sans** (GitHub, distribuita da Google Fonts): SIL Open Font License 1.1, uso commerciale libero; woff2 variabili in `sito/fonts/`.
- **Jost** (Google Fonts, SIL OFL 1.1): solo "SRL" del logo, in tracciati; non servito dalla pagina.
- **Foto**: della libreria media pubblica del loro sito; uso da confermare. Nessuna foto di repertorio in pagina (quelle di `assets/esterne/` non sono usate), nessuna immagine generata dall'IA (le cinque Gemini della loro libreria sono escluse), nessuna illustrazione.

## Loghi

- `sito/img/logo-masi-scritta.svg`: la scritta vettoriale del loro `logo-meccanica-masi-srl-modificato.svg`, rosso #ED1C24 e nero #231F20, senza gli ingranaggi raster; "SRL" in tracciati da Jost 800. `logo-masi-scritta-chiaro.svg` è la stessa con il nero portato a bianco, per il piede.

## Collegamenti in pagina

- Tutti i link interni puntano a sezioni della home (Manutenzione, Lavorazioni, Lavori, Mandateci il disegno, Chi siamo, Lavora con noi, Contatti): nessuna pagina da fare per far funzionare la home. Privacy porta alla loro pagina di oggi (`meccanicamasi.it/privacy-policy-2/`); il cookie banner (iubenda) resta da rimettere sul sito vero.
- Mappa: "Apri la mappa" sulla scheda Google con il CID; "Indicazioni stradali" con `google.com/maps/dir`.

## Newsletter

Non c'è: lavorano su commessa per altre aziende, senza fiere, cataloghi, collezioni né clienti privati da tenere informati.
