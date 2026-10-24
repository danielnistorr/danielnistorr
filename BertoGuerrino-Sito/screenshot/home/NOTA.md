# Berto Guerrino, home finale: "Il pezzo giallo, in scala"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, screenshot e prove del gesto con `finale_shot.mjs`, JPEG con `finale_jpg.py`, misura dei segnali con `_metodo/kit/segnali.sh`). Parte dal prototipo A, poi rifinita dopo il giudice cieco (`_prova/cieco.json`).

## Idea

Lo sterrapiante Berto, giallo con il vomere blu, posato sulla linea di terra dentro l'ingombro delle sue tre versioni: tre riquadri MOD. 80, MOD. 85 e MOD. 100 con le quote vere di altezza e lunghezza, come in una tavola d'officina. È la cosa che solo Berto ha (lo stesso pezzo costruito in tre taglie per tre classi di trattore) e sta nella prima schermata, sotto il titolo, con i bottoni e le cifre accanto. Con il nome di un altro costruttore la pagina non regge: macchina, versioni, misure e frasi sono di Berto.

## Prima schermata

- **1440 (apertura fino a 964 px)**: testata con il logo vero (cartello giallo), quattro voci e il telefono. "Macchine speciali per vivai" in Anybody stretto a 136 px su una riga a tutta larghezza. Sotto, su otto colonne, il disegno in scala: linea di terra, i tre riquadri, la foto dello sterrapiante e le quote (160 cm, 230 cm con MOD. 85 attivo). Sulle quattro colonne di destra due righe di testo, i bottoni MOD. 80 / 85 / 100, trattore, larghezza e peso in cifre grandi, "Attacco a tre punti, PTO 540 giri", i link alla scheda e al video, il bottone "Chiama 049 640282". Tutto dentro i 900 px.
- **390**: titolo a 64 px su tre righe, il disegno a tutta larghezza, i tre bottoni larghi un terzo e le prime cifre dentro gli 844 px; testo e telefono subito sotto.
- **768 e 1024**: a 1024 disegno e comandi restano affiancati (sette e cinque colonne, menu a bottone); sotto i 900 il titolo va su due righe, il disegno a tutta larghezza, i bottoni sotto e le cifre accanto al testo.

Sezioni, in ordine: apertura con il gesto; la zolla (una foto alla sua misura di 500 px con il titolo "Il vomere passa sotto la fila, solleva la zolla e la apre" sotto, non accanto); le altre macchine (quattro pezzi su due colonne sulla stessa linea di terra, poi una riga con le altre sette); officina e negozio (una colonna sola, i marchi a 40 px); chiusura con foto; piede. Pagina di 5206 px a 1440 e 5067 a 390, piede compreso.

## Caratteri e colori

- **Anybody** (Etcetera Type Co., Google Fonts, SIL Open Font License 1.1, uso commerciale libero), una sola famiglia variabile con gli assi di larghezza e peso, servita dalla pagina (`sito/fonts/anybody-latin.woff2`, sottoinsieme latin). Titoli a larghezza 72 % e peso 580; cifre grandi e marchi a larghezza 62 %; testo a larghezza 100 % peso 400, 18-19 px su 1,6. Cifre tabellari per misure, pesi, telefono e P.IVA. Il motivo: le lettere strette e piene del cartello BERTO, senza copiarle. Riferimenti del mestiere (sez. 7 di `01-analisi.md`): Sneeboer (officina di famiglia, titolo enorme, un solo colore del marchio) e Väderstad (una sola immagine forte, il giallo del marchio come unico colore).
- **Colori**: carta #F4F1E9, carta scura #EAE5D8 (solo il piede), inchiostro #1B1A17 (15,4:1 sulla carta, 13,8:1 sul piede), grigio #58544B per i testi secondari (6,7:1 sulla carta, 6,0:1 sul piede), grigio delle etichette dei riquadri spenti #6B665B (5,1:1), blu vomere #23324A per i link (11,4:1). Il giallo arriva solo dalle foto, il rosso solo dal logo. Nessun gradiente, nessuna ombra disegnata, nessuna icona.

## Interazione

Un gesto solo, in apertura: i bottoni MOD. 80, MOD. 85, MOD. 100 (`aria-pressed`, frecce sinistra e destra da tastiera, bersagli alti 56 px). Al clic o al tocco cambiano trattore (40/68, 60/100, 100/150 HP), larghezza (90, 110, 120 cm), peso (350, 500, 680 kg) e le quote (140 x 210, 160 x 230, 170 x 280 cm); il riquadro scelto diventa pieno e la foto si scala in modo uniforme dentro di lui (0,18 s, niente con "riduci movimento"). Provato da `finale_shot.mjs`: clic su MOD. 100, due frecce a sinistra fino a MOD. 80 (il fuoco segue, 350 kg), tocco su MOD. 100 a 390 (100/150 HP). Nient'altro si muove; menu a bottone sotto i 1024 px; colonne del piede a fisarmonica con bottoni veri sotto i 600 px (provata col tocco).

## Foto: origine e licenza

| In pagina | File | Origine | Licenza |
|---|---|---|---|
| Sterrapiante (nel disegno in scala) | `img/sterrapiante-700.jpg` | `vivaio/images/STERRAPIANTE.png` del sito (724 px): cornice e didascalia tolte, fondo grigio stimato con una superficie polinomiale e diviso, ombra tenuta, taglio sul punto d'appoggio. Solo alla misura nativa, mostrata fino a circa 690 px CSS: nessun ingrandimento | materiale dell'azienda, solo come prova |
| Quattro macchine | `img/porta-innesti, primi-rami, piragna, agevolatrice -420/640.jpg` | foto in studio delle schede, stesso trattamento, luminosità e croma della vernice avvicinate allo sterrapiante | materiale dell'azienda |
| La zolla | `img/zolla-500.jpg` | `vivaio/gallery/FOTO-3.jpg` (500x500), dominante marrone corretta con i livelli per canale, niente viraggio | materiale dell'azienda |
| Chiusura | `img/campo-640/960/1264.jpg` | anteprima del video YouTube `5b_3K-YZ2zk` del loro canale (trincia Piragna al lavoro tra le file), bande nere tolte, colori naturali, mai oltre la misura del file | materiale dell'azienda |
| Logo | `img/logo-berto.png`, `img/logo-berto-payoff.png` | ritagli di `images/apertura.png` (cartello giallo, 524 px), mostrati a 112 e 168 px | logo dell'azienda |

Nessuna immagine generata dall'IA e nessuna foto di repertorio in pagina.

## Piede

Logo con "Instruments for professionals" e una riga su chi sono; colonne Macchine per vivai (con le due rincalzatrici separate), Azienda, Contatti, Seguici (solo YouTube, l'unico social che esiste); in fondo ragione sociale, P.IVA, Privacy, Cookie. Link alti almeno 24 px. A 390 le quattro colonne si aprono a fisarmonica.

**Niente newsletter**: la pagina "Novità" del sito è vuota dal 2021, il canale YouTube ha 27 iscritti e non ci sono fiere né cataloghi da annunciare. Si aggiunge solo se confermano che manderebbero le offerte di stagione.

## Cosa è cambiato dopo il giudice cieco

- Apertura e versioni fuse: il disegno in scala con i bottoni sta sotto il titolo, nella prima schermata; non è più "titolo a sinistra e pezzo scontornato a destra con le legende", e la foto dello sterrapiante compare una volta sola.
- Tolta la quota "fino a 1 m fuori carreggiata" e le legende: nessuna quota che non corrisponda a un punto della macchina; il dato resta nel testo.
- Sterrapiante solo a 700 px, la misura del file: tolti i file 1160 e 1560 ingranditi (e anche il 400, non più usato).
- Zolla: non più foto da un lato e testo dall'altro; foto a 500 px con il titolo sotto, colore corretto (nessun fotogramma YouTube più nitido della zolla: le anteprime dello sterrapiante hanno riquadri incorniciati).
- Chiusura: al posto della foto di repertorio desaturata (Seymour) il fotogramma YouTube più nitido di una macchina Berto al lavoro, a colori naturali; a 1024 il passo sopra il titolo è 112 px come le altre sezioni.
- Altre macchine: da sei a quattro, su due colonne alla stessa altezza; trapiantatrice e fresatrice nella riga "E poi".
- Officina: titolo e testo in una colonna di 640 px; marchi a 40 px, sotto le macchine per gerarchia; link "Giardinaggio e marchi" su una riga sua.
- Piede: link e Privacy/Cookie alti almeno 24 px; "Rincalzatrice porta innesti" e "Rincalzatrice primi rami" separate.
- In quest'ultimo passaggio: scritte del disegno in scala più grandi dove il disegno si rimpicciolisce (da 901 a 1100 px, sotto i 760 e sotto i 360: a 320 le quote sono a circa 12 px invece di 10), zolla con la dominante corretta, tolto il riquadro azzurro del tocco su bottoni e link.

## Controlli

- scrollWidth uguale a innerWidth a 320, 360, 390, 414, 600, 700, 768, 820, 900, 1024, 1100, 1280, 1366, 1440, 1680, 1920 e 2560; nessuna sovrapposizione tra titolo, disegno, testo, bottoni e cifre; nessun elemento oltre il margine della colonna; nessun link del piede sotto i 24 px (controlli automatici in `finale_shot.mjs`). Screenshot a 1440 e 390 guardati a pezzi, prime schermate a 320, 768, 1024 e 1920 guardate.
- Collegamenti: `tel:+39049640282` (testata, apertura, chiusura, piede), `mailto:bertopd@libero.it`, mappa Google con "Via Caovilla 27/B 35020 Saonara PD".
- Nessun U+2014 nella pagina, negli script, nella NOTA e nel LEGGIMI.
- Segnali da IA (`_metodo/kit/segnali.sh` a 1440): 9 soglie bloccanti su 10 OK. Sotto soglia l'area delle foto, 19,8 % contro 35 %: lo strumento non conta la foto dentro lo SVG, e Berto non ha foto grandi (il meglio è a 724 px e 1280 px da un video SD). Come dice la guida per le aziende senza foto grandi, non si maschera ingrandendo: è la prima cosa da chiedere (brief nel LEGGIMI). Da guardare: tre numeri grandi (le cifre del gesto e il 1961 della chiusura), voluti; un titolo col punto (la frase loro della chiusura).
- Divieti del committente: nessun gradiente, testo in gradiente, emoji, Inter, bordo sinistro colorato, vetro, icone Lucide, badge, tre box, comparse allo scorrimento, effetti sul cursore, bottoni che sbiadiscono, serif corsivo.
- Aperta come file://, la console mostra un avviso CORS sulla `preload` del carattere: il carattere si carica comunque da `@font-face`; servita in http l'avviso sparisce.
