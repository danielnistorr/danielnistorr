# Nardi, home: livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh`. La versione precedente ("Una scatola sola", con il selettore delle sei famiglie e la foto Unsplash delle mani) è copiata intatta in `_prova/versione-1-originale/`.

Screenshot: `home-1440.jpg` (circa 8.000 px, piede compreso), `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (contatti, modulo e piede). Guardati a pezzi a 1440 e a 390; prime schermate e pagine intere anche a 320, 768, 1024 e 1920; stati della ricerca ("fughe" a 390, "gesso murario" a 1440), elenco dei codici aperto con il filtro Artelinea, menu aperto a 390.

## Livello professionale, ritocco finale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia M, adattata a un produttore che vende ai negozi. Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14 (fogli di contatto), le pagine intere di Cly-Del e barth a pezzi. Il controllore aveva dato 5 su 10 ("sembra il portale di un e-commerce"): questo giro applica i suoi difetti e quelli delle due prove d'uso (negoziante e privato).

### Che cosa è cambiato

1. **Apertura come i riferimenti M**: una dichiarazione e un gesto. A sinistra occhiello, H1 "Stucchi, gessi e malte" su una riga (68 px), la frase della scheda d'uso, il blocco ordini con lo stato, "Ordini 049 879 0626" pieno a 58 px e "Diventa rivenditore" bordato; a destra il **magazzino di Nardi a vivo** fino al bordo dello schermo (720x514 a 1440, metà pagina), con i bancali Briko Line. Lo scaffale del negozio è passato in "Dove si comprano", dove dice il vero.
2. **Ricerca e sei lavori in una fascia grigia a tutta larghezza** in fondo alla prima schermata (label, campo e Cerca su una riga, sei tessere in una riga). A 390 l'ordine resta quello di prima: ricerca e lavori senza scorrere, poi il telefono.
3. **Gesto di scala: la fascia dei numeri** su verde scuro subito dopo l'apertura, quattro cifre vere (1985, 96 prodotti, 89 schede tecniche in PDF, 2011 fotovoltaico) a 120 px (64 a 390), etichette a 17 px, filetti verticali. Tolte le due cifre di riempimento (4 linee e 12 pezzi restano nel testo di Prodotti e Per i negozi).
4. **Rendering rifatti** (`_prova/script/pro_rendering.py`): fondo grigio sfumato sostituito da bianco pieno, riflesso e ombra sotto la confezione tolti (taglio sul bordo basso inclinato, colonna per colonna), confezione centrata e alta il 75% del riquadro in tutte. Le tre foto da studio non da rendering (`Q48A8102`, `Q48A8140`) sono sostituite dai rendering Artelinea dello stesso prodotto; il cemento grigio Artelinea (`Q48A8038`) resta senza miniatura. "Altri prodotti" ora mostra il mastice per vetri, "Artelinea" il sacco da 25 kg dell'E180, "Gli speciali" lo stucco per grossi spessori.
5. **Foto in serie** (`pro_img.py`): un solo trattamento per magazzino, scaffale e sede (bianco neutro, arancio delle scaffalature desaturato del 30%, stessa curva, stessa desaturazione), tutte in 4:3; la sede è tagliata stretta su ingresso, fasce lilla e pilastro NARDI e mostrata al massimo a 533 px (sorgente 747).
6. **Tessere dei lavori** alte 72 px, miniatura 64 px su bianco, nome a 17 px in larghezza normale, bordo 1 px e raggio 4 come i bottoni (freccia sotto i 1024 px).
7. **"Riconosci la scatola"** (dalla prova del privato): dodici scatole Briko Line da 1 kg con il nome sotto, in Prodotti; ogni scatola apre la sua scheda nei risultati.
8. **Professionisti**: la dichiarazione di prestazione è un riquadro a sé con il sacco, "Dichiarazione di prestazione n. 1 - E180 - 2017", prodotto, norma UNI EN 13279-1, reazione al fuoco classe A1 e "Scarica il PDF"; le righe-link sono diventate bottoni del sistema.
9. **Logo** 180x41 a 1440 e 128x29 a 390.
10. **Catalogo codici in PDF vero** (`sito/catalogo-codici-nardi.pdf`, 5 pagine A4, 184 KB, fatto da `pro_catalogo.mjs` con la stessa tabella): intestazione con logo, ragione sociale, indirizzo, ordini, orari, email e "aggiornato al 3 novembre 2026", piede con il numero di pagina, senza filtri, bottoni né colonna schede. Si scarica dalla sezione codici, dai passi del negoziante e dal piede.
11. **Confezioni scritte in un modo solo** ("1 kg x 12 pz, bancale 720 kg", "750 g x 12 pz, bancale 768 pz", "1 l x 12 pz"); gli ossidi hanno "500 g x 6 pz" (da `01-analisi.md`), mordenti e due righe della polvere ceramica "confezione: chiedere al 049 879 0626".
12. **Ricerca**: ogni lavoro mette prima il prodotto che gli dà il nome e la scatola Briko Line (Fughe: prima lo stucco per fughe); parole dei lavori (calco, crepa, scatola elettrica, caminetto, stufa...) che valgono più del testo libero; radice solo da 6 lettere; una lettera sbagliata tollerata (stuko, alabastrno). Le righe d'uso sono sempre le stesse quattro (acqua, tempi, spessore, uso), con "vedi scheda tecnica" dove la scheda non dà il dato; "30%" diventa anche "circa 300 g d'acqua per 1 kg".
13. **Modulo**: oggetto senza parentesi annidate ("Diventare rivenditore: Ferramenta Rossi, Este (PD)"); dopo "Prepara l'email" resta sempre un riquadro con il testo pronto, "Copia il testo", l'indirizzo e il telefono, per chi non ha un programma di posta. "Richiesta" in testata sceglie "Ordine".
14. **Varie**: "Scritto sulle confezioni Briko Line" (non più "su ogni"); passo 3 dei negozi con il link alle schede di sicurezza e la voce "Schede di sicurezza" nel piede; sezioni a colori che si fermano esattamente sotto la testata (niente striscia bianca); script dello stato pronto per le chiusure aziendali (elenco vuoto finché Nardi non le dà).

### Struttura

Testata fissa · apertura (bianco, magazzino a vivo) e fascia della ricerca (grigio) · numeri (verde scuro) · Per i negozi (bianco: tre passi) · Prodotti (grigio: quattro linee, scatole, elenco codici e catalogo PDF) · Professionisti (bianco, riquadro E180 grigio) · Dove si comprano (grigio, scaffale e cinque negozi) · Azienda (lilla, sede) · Contatti e modulo (grigio) · piede (verde scuro).

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** Testata `sticky` di 89 px a 1440 e 73 a 390; bottone "Ordini 049 879 0626" alto 48 px (a 390 solo il numero); a metà pagina a 390 si vede e si tocca (`elementFromPoint`). 10 link `tel:`, tutti `tel:+390498790626`. "Richiesta" bordato accanto.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** 1440 x 900: H1, "Produttori dal 1985, Tombelle di Saonara (PD)", il telefono ordini pieno, "Diventa rivenditore", lo stato, la ricerca e i sei lavori. 390 x 844: H1 a 40 px, ricerca entro 404 px, lavori entro 654, telefono pieno a tutta larghezza (350 px) da 788. La prova resta l'anno: le altre non ci sono nelle fonti.
3. **Immagine vera nell'apertura: passa a 1440.** Il magazzino di Nardi (`IMG_4232`) a vivo sulla metà destra, 720x514. A 390 la foto viene dopo il telefono (1034 px), per lasciare ricerca e lavori nella prima schermata come chiede la scheda d'uso. Mancano ancora persone e produzione: è la prima foto da fare (LEGGIMI).
4. **Zero repertorio: passa.** `indicativ` 0 volte, nessun file Unsplash o Pexels, nessun disegno.
5. **Foto in serie: passa.** Due formati (4:3 per le tre foto, 1:1 per i rendering su bianco pieno), una didascalia su 26 immagini, un trattamento solo per le tre foto. La luce dei tre scatti resta diversa: la serie vera richiede il servizio fotografico.
6. **Palette dal marchio: passa.** `--verde` #276E59 (dal logo #46A589), `--verde-scuro` #173F33, `--lilla` #9396C8 della facciata, `--lilla-chiaro`; neutri freddi; nessun colore fuori da `:root` (anche il foglio di stampa usa i token). Fondo bianco.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 19, 23, 32, 48, 68, 120) e 8 a 390 (14, 16, 17, 19, 24, 30, 40, 64); testo corrente 19 a 1440 e 17 a 390; niente sotto i 14 px; H1 68/40 (fascia M), H2 48/30.
8. **Due famiglie al massimo: passa.** Una sola, Encode Sans: stretta (75 %) a 700 per titoli, numeri e telefono; normale a 400 e 700 per testo e interfaccia (tessere comprese).
9. **Servizi in schede con foto: passa.** Quattro linee in 4 colonne (2 a 390), passo 28 px, confezione quadrata su bianco per tutte, nome a 23 px, riga e "Codici e schede"; tutta la scheda è un link. In più dodici scatole in 6 colonne.
10. **Almeno tre tipi di prova: passa, con riserva (3 su 4).** Quattro numeri aziendali in fascia; la dichiarazione di prestazione E180 in un riquadro con il PDF; cinque negozi con nome e comune (da confermare, LEGGIMI punto 3). Recensioni: nessuna nelle fonti, non inventate.
11. **Lavori con un nome: non passa.** Nessun lavoro con cliente, luogo e anno nelle fonti; nessun segnaposto in pagina (LEGGIMI punto 5).
12. **Ritmo a blocchi: passa.** Blocchi pieni oltre al piede: numeri in verde scuro e Azienda in lilla; fascia della ricerca, Prodotti, Dove e Contatti in grigio, alternati al bianco. Sezioni a 120 px a 1440 e 72 a 390; margine 80 a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno e bordato, raggio 4 px; altezze 48 (testata, filtri), 56 e 58 (telefono e "Diventa rivenditore" in apertura); testo 17 px (16 a 390, 32 e 24 nel telefono grande); i bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: passa, con riserva.** Tipo di richiesta, nome, negozio, città, partita IVA, telefono, email, prodotti e codici, messaggio; il mailto non porta allegati, quindi la pagina chiede di allegare l'ordine all'email e il LEGGIMI chiede il campo nel servizio. Nessun iframe; sede con "Sede nel navigatore" e "Apri la sede nel navigatore".
15. **Piede completo: passa.** Quattro colonne (marchio e indirizzo; Prodotti con schede di sicurezza e catalogo PDF; Azienda con la dichiarazione E180; Contatti con telefono, fax, due email, orari e stato) e riga legale; niente sotto i 14 px.

### Compiti della scheda d'uso (`_prova/uso/SCHEDA.md`, par. 8)

`node _prova/script/pro_shots.mjs`: 51 prove su 51 riuscite.
- *Negoziante, 1440*: telefono ordini, orari e stato senza scorrere (martedì 10.00 "Aperto ora, fino alle 12"); "Codici, confezioni e catalogo in PDF" apre l'elenco dei 96 prodotti (179 link PDF), filtro Artelinea; il catalogo in PDF vero si scarica in due clic; "Diventa rivenditore" sceglie il tipo nel modulo, vuoto si ferma, pieno compone l'email e lascia il testo da copiare; "gesso murario" dà la scheda di sicurezza in un clic; il codice 4302010 trova il gesso murario.
- *Privato, 390*: ricerca e "Chiama" senza scorrere; "Fughe e piastrelle" apre per primo lo stucco per fughe Briko Line; "fughe", "calco", "crepa", "scatola elettrica", "caminetto", "stuko" e "alabastrno" danno per primo il prodotto giusto; la scatola della malta refrattaria apre la sua scheda; "Dove lo compro?" nella prima schermata; dal menu "Dove si comprano" si ferma sotto la testata.
- *Professionista*: "Schede tecniche Artelinea" apre l'elenco filtrato; la sede si apre nel navigatore in un tocco.
- *Orari*: 13.10, 19.30, sabato, 8 dicembre, Pasquetta e 15.00 danno il messaggio giusto.

### Caratteri e licenze

- **Encode Sans** (The Encode Project Authors), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; file variabili serviti dalla pagina in `sito/fonts/`, licenza in `sito/fonts/OFL.txt`. Pesi 400 e 700, larghezze 100 % e 75 %.
- **Foto**: solo materiale di Nardi dalla libreria media di narditalia.com (magazzino, scaffale, sede, rendering delle confezioni, logo). Nessuna foto di repertorio, nessuna immagine generata, nessun disegno (`assets/CREDITI.md`).

### Controlli fatti (3/11/2026)

- Screenshot guardati a pezzi a 1440 e a 390, prime schermate a 320, 768 e 1024, risultati della ricerca a 1440, prime due pagine del catalogo PDF.
- Nessuno scorrimento orizzontale e nessun testo che esce dal suo riquadro a 320, 390, 768, 1024, 1440 e 1920 (controllo anche sui singoli nodi di testo); nessun errore di script.
- `tel:+390498790626` ovunque; `mailto:` con oggetto; mappe con `google.com/maps/dir`; nessun U+2014 in pagina, nei .md e negli script (controllo nel `build_finale.sh`).
- Dati: ogni fatto in pagina viene da `01-analisi.md`, dalla scheda d'uso o dalle schede prodotto del loro sito; quello che è dubbio sta nel LEGGIMI.
