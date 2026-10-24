# Berto Guerrino: proposta di nuova home

Proposta non richiesta, solo la home. Nessun contatto con l'azienda, niente pubblicato.

- Pagina: `sito/index.html` con `sito/img/` (solo le immagini usate, JPEG in più larghezze) e `sito/fonts/` (Anybody).
- Screenshot: `screenshot/home/` (`home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, più le prime schermate a 320, 768, 1024, 1920 e il gesto su MOD. 100 e MOD. 80 a 1440 e MOD. 100 a 390 con la fisarmonica del piede aperta). Idea, scelte, controlli e cosa è cambiato dopo il giudice cieco in `screenshot/home/NOTA.md`.
- Aperta come file://, la console mostra un avviso CORS sulla `preload` del carattere: è atteso, il carattere si carica comunque; servita in http l'avviso non c'è.
- Rifare tutto: `bash _prova/script/build_finale.sh` (immagini, screenshot, misura dei segnali; i file temporanei vanno in `_prova/tmp-finale/` e si cancellano alla fine).
- Analisi con le fonti: `01-analisi.md`. Prototipi: `_prova/home/a` (scelto) e `_prova/home/b`.

## Dati da confermare con Berto

In pagina ci sono solo fatti di `01-analisi.md`. Restano da confermare:

- **Forma giuridica**: in pagina "S.a.s." (testata del sito), ma il dominio e coobiz dicono ancora "snc".
- **P.IVA 02570660288**: in pagina, ma presa da coobiz e registroaziende, non dal loro sito. REA, PEC e capitale sociale non trovati: non in pagina.
- **Email**: in pagina solo bertopd@libero.it. Da scegliere tra libero.it, tin.it e gmail.com; meglio un indirizzo sul dominio.
- **Orari**: non in pagina. Nextdoor (lun-ven 8-12 e 14-19, sab 8-12) e coobiz non coincidono sul mercoledì.
- **MOD. 80**: in pagina "40/68 HP" come nella scheda italiana; inglese, tedesco e francese dicono 40/65.
- **Foto dello sterrapiante**: quale versione è (si è evitato di scriverlo).
- **"Costruite da noi"** per le quattro macchine della griglia e le sette della riga "E poi" (dal testo "attrezzature vivaistiche da noi prodotte"): confermare macchina per macchina, e che siano ancora tutte in produzione.
- **Marchi**: l'elenco dei concessionari è del 2021.
- **Vendite all'estero**: tolte dalla pagina (vengono solo da Nextdoor); se confermate, si aggiungono alla frase della chiusura con i paesi.
- **Disegno in scala**: i tre riquadri e le quote usano altezza e lunghezza delle schede (140 x 210, 160 x 230, 170 x 280 cm); la foto è una sola, di tre quarti, scalata nei tre riquadri: confermare che le tre versioni hanno la stessa forma. Lo spostamento del vomere "fino ad un metro" è solo nel testo, non disegnato.
- Le "attrezzature brevettate" di Nextdoor: non in pagina finché non si sa quale brevetto.

## Foto da rifare dal vero

Le foto in pagina sono tutte di Berto, prese dal sito e da un'anteprima YouTube: piccole (724 px, 500 px) o fotogrammi SD. Non c'è nessuna foto di repertorio. Prima di pubblicare chiedere gli originali dei depliant; se non ci sono:

1. **Sterrapiante in sala posa o in capannone**: fondale chiaro continuo (grigio caldo chiaro, vicino alla carta #F4F1E9), luce morbida dall'alto a sinistra, ombra a terra tenuta, vista di tre quarti come quella di oggi (vomere a sinistra, attacco a destra), a 6000 px sul lato lungo; meglio ancora le tre versioni MOD. 80, 85 e 100 con la stessa inquadratura e la stessa distanza, così il disegno in scala mostra tre foto vere; più tre dettagli: vomere, attacco a tre punti, presa di forza e pompa. Oggi la foto è a 700 px e su schermi 2x è morbida.
2. **Le quattro macchine della griglia** (e le altre per le schede) con la stessa luce, lo stesso fondale, lo stesso punto di vista e la stessa altezza di macchina: oggi hanno luce e colore diversi e si sono solo avvicinate al computer.
3. **La zolla**: la sterratura in un vivaio di Saonara tra novembre e marzo, luce bassa, il vomere che solleva la zolla con le radici, quadrata, almeno 2000 px.
4. **Chiusura**: oggi è il fotogramma del video della trincia Piragna (1280 px, SD ingrandito, morbido). Da rifare: una macchina Berto al lavoro tra i filari di un vivaio di Saonara, d'inverno, sole basso, orizzontale, almeno 3000 px; oppure il piazzale con le macchine gialle davanti all'officina.
5. **Officina e negozio**, se si vuole una foto nella sezione; un ritratto di Fausto e Lorena per la pagina Azienda.

## Licenze

- **Anybody**: Etcetera Type Co., Google Fonts, SIL Open Font License 1.1 (uso commerciale libero), servito dalla pagina.
- Nessuna foto di repertorio in pagina (Seymour, usata nella versione precedente, è stata tolta; resta in `assets/esterne/` con la licenza in `assets/CREDITI.md`).
- **Foto e logo di Berto**: dal loro sito; nella proposta solo come prova, per il sito vero serve il loro consenso.

## Logo

Nessun vettoriale trovato: in pagina i ritagli del cartello giallo di `images/apertura.png` (524 px, mostrati a 112 e 168 px, quindi oltre il 2x). Le lettere hanno bordo e ombra in rilievo, quindi un SVG ricostruito non sarebbe fedele. Chiedere il file originale a chi ha fatto l'insegna o i depliant.

## Pagine del sito nuovo (link del piede e della home)

`macchine/` (indice) e le schede `macchine/sterrapiante.html`, `scalzapneus.html`, `rincalzatrice-porta-innesti.html`, `rincalzatrice-primi-rami.html`, `trapiantatrice-tt.html`, `trincia-piragna.html`, `fresatrice-multipla-alta.html`, `agevolatrice.html` (più rimorchio, trattorino, bancali e varie dall'indice; in home e nel piede sono linkate sterrapiante, scalzapneus, le due rincalzatrici, trapiantatrice, trincia, agevolatrice e l'indice); `azienda.html`, `giardinaggio.html` (marchi e prodotti), `officina.html`, `video.html`, `privacy.html`, `cookie.html`. Le voci del menu portano alle sezioni della home. Il video "Il video in campo" è https://youtu.be/wZaJq_-mrEM (dalla pagina video del sito).

## Newsletter

Niente newsletter: la pagina "Novità" è vuota dal 2021, il canale YouTube ha 27 iscritti, nessuna fiera né catalogo da annunciare. Se confermano che manderebbero le offerte di stagione: campo email, bottone, casella del consenso privacy, collegata a un servizio (non funziona finché non si collega).

## Segnali da IA: righe da guardare

- **Area foto 19,8 % (soglia 35 %)**: la home è costruita sul pezzo nel disegno in scala (che lo strumento non conta) e Berto non ha foto grandi. Non si maschera ingrandendo foto piccole: sale con le foto vere della chiusura, della zolla e dell'officina (brief qui sopra).
- **Tre numeri grandi**: le cifre del gesto (trattore, larghezza, peso) e il 1961 della chiusura, voluti.
- **Un titolo col punto**: "La nostra ditta nasce nel 1961.", frase loro.
