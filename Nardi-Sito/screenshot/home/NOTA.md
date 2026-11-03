# Nardi, home: livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh`. La versione precedente ("Una scatola sola", con il selettore delle sei famiglie e la foto Unsplash delle mani) è copiata intatta in `_prova/versione-1-originale/`.

Screenshot: `home-1440.jpg` (6.900 px circa, piede compreso), `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (contatti, modulo e piede). Guardati a pezzi a 1440 e a 390; prime schermate e pagine intere anche a 320, 768, 1024 e 1920; stati della ricerca ("fughe" a 390, "gesso murario" a 1440), elenco dei codici aperto con il filtro Artelinea, menu aperto a 390.

## Livello professionale (3/11/2026)

Richiesta: "secondo me non rappresentano bene l'identità e l'utilizzo corretto di quello che dovrebbe essere il sito" e "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura), adattata a un produttore che vende ai negozi. Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14, le pagine intere di Cly-Del e barth (più l'apertura di Budri).

### L'idea

Nardi non è un marchio da showroom: è un piccolo produttore di polveri che vende ai negozi e la cui scatola finisce in mano a chi fa la crepa di casa. La home è quindi uno strumento, nel registro delle loro schede ("Inizio presa 5 - 8 min", "Massimo spessore 2-3 mm per mano") e con le loro foto vere: lo scaffale con le scatole in fila, il magazzino con i bancali, la sede dipinta come la scatola. Della versione 1 restano il titolo "Stucchi, gessi e malte" (dice il mestiere), Encode Sans, il verde del logo e il logo vero. Via il fondo beige, la scatola scontornata come scultura, il selettore delle sei famiglie e le mani di Unsplash.

### Struttura (famiglia M adattata)

1. **Testata fissa** con sei voci con le loro parole (Prodotti, Per i negozi, Professionisti, Dove si comprano, Azienda, Contatti), "Richiesta" bordato e "Ordini 049 879 0626" pieno. A 390 restano il logo, il bottone del telefono e "Menu".
2. **Apertura**: occhiello "Produttori dal 1985, Tombelle di Saonara (PD)", H1 "Stucchi, gessi e malte", la frase della scheda d'uso ("Li produciamo a Tombelle di Saonara e li vendiamo ai negozi in tutta Italia"), il campo "Cosa devi fare?" e i sei lavori con la scatola vera; a destra lo scaffale (foto loro) e il blocco "Ordini dei negozi" con lo stato aperto o chiuso, il telefono a 32 px, gli orari, "Codici e confezioni" e "Diventa rivenditore".
3. **Per i negozi** (verde scuro pieno): come si ordina in tre passi, il magazzino, "Diventa rivenditore" e "Chiedi il listino", la fascia dei sei numeri (1985, 96, 4, 12, 89, 2011).
4. **Quattro linee, 96 prodotti**: quattro schede quadrate con la confezione vera (Briko Line, Artelinea, Gli speciali, Altri prodotti), ognuna apre l'elenco filtrato; sotto, l'elenco di codici, confezioni e schede PDF dei 96 prodotti (193 codici), filtrabile e da stampare.
5. **Per i professionisti** (grigio): Artelinea, schede, dichiarazione di prestazione E180 in PDF, telefono per quantità e consegna, sede nel navigatore.
6. **Dove si comprano**: nei negozi, con il nome o il codice della scatola, e cinque negozi che la vendono.
7. **Azienda** (lilla pieno, il colore della facciata): la sede vera, la storia in tre righe, 1985, 2011, Made in Italy.
8. **Contatti e modulo** (grigio): telefono, fax, orari in tabella con lo stato, email, email per le schede di sicurezza, sede con il navigatore; modulo "Richiesta o ordine".
9. **Piede** (verde scuro) in quattro colonne e riga legale.

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** Testata `sticky` di 88 px a 1440 e 72 a 390; bottone "Ordini 049 879 0626" alto 48 px (a 390 solo il numero). A metà pagina a 390 il bottone si vede e si tocca (`elementFromPoint`). 9 link `tel:`, tutti `tel:+390498790626`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** A 1440 x 900: H1 "Stucchi, gessi e malte", Tombelle di Saonara nell'occhiello e nella frase, "dal 1985", il telefono ordini come bottone a tutta colonna, lo stato e i due bottoni del negoziante, la ricerca e i sei lavori. A 390 x 844: il campo di ricerca entro 395 px, i sei lavori entro 623, il bottone del telefono a tutta larghezza (350 px) da 765 px; il telefono resta anche in testata.
3. **Immagine vera nell'apertura: passa, con riserva.** Lo scaffale con le scatole Briko Line (`IMG_2282`, foto del loro sito) a destra del titolo a 1440, nella seconda schermata a 390. Non ci sono persone né la produzione: è la prima foto da fare (LEGGIMI). Nessuna illustrazione, per scelta del committente.
4. **Zero repertorio: passa.** `indicativ` compare 0 volte; nessun file Unsplash o Pexels in pagina (tolte le mani con la spatola).
5. **Foto in serie: passa, con riserva.** Tre foto d'ambiente tutte 16:9 con lo stesso trattamento (bianco neutro, un filo di contrasto, colore più quieto) e miniature 1:1 dei rendering: due formati. Una sola didascalia (la sede, perché aggiunge l'indirizzo). La luce resta diversa tra scaffale, magazzino e facciata: la serie vera richiede il servizio fotografico del LEGGIMI.
6. **Palette dal marchio: passa.** `--verde` #276E59 (verde del logo #46A589 scurito per il contrasto) con `--verde-scuro` #173F33 per i blocchi pieni, `--lilla` #9396C8 della facciata con `--lilla-chiaro`; neutri freddi; nessun colore fuori da `:root`. Fondo bianco, nessun beige.
7. **Scala tipografica corta: passa.** 7 misure a 1440 (14, 17, 19, 23, 32, 48, 72) e 8 a 390 (14, 16, 17, 19, 20, 24, 30, 40); testo corrente 19 px a 1440 e 17 a 390; nessun testo sotto i 14 px; H1 72/40, H2 48/30.
8. **Due famiglie al massimo: passa.** Una sola, Encode Sans: stretta (75 %) a 700 per titoli, lavori, numeri e telefono; normale a 400 e 700 per testo e interfaccia.
9. **Servizi in schede con foto: passa.** Le quattro linee in 4 colonne (2 a 390), confezione vera quadrata per tutte, nome, riga e "Codici e schede"; tutta la scheda è un link. In più i sei lavori in apertura, ognuno con la sua scatola.
10. **Almeno tre tipi di prova: passa, con riserva (3 su 4).** Sei numeri aziendali in fascia; la dichiarazione di prestazione dell'E180 scaricabile (UNI EN 13279-1, classe A1), anche nel piede; cinque negozi con nome e comune. I negozi sono presi dai loro siti e non sappiamo se comprano da Nardi: da confermare (LEGGIMI, punto 3). Recensioni: nessuna nelle fonti, non inventate.
11. **Lavori con un nome: non passa.** Nessun lavoro con cliente, luogo e anno nelle fonti (LEGGIMI, punto 5).
12. **Ritmo a blocchi: passa.** Blocchi pieni oltre al piede: Per i negozi in verde scuro, Azienda in lilla; Professionisti e Contatti in grigio. Sezioni a 120 px a 1440 e 72 a 390 (l'apertura parte a 56 e 28 sotto la testata); contenitore di 1280 px con margini di 80 a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno verde e bordato, raggio 4 px, 56 px (48 in testata, 58 il telefono grande), testo 17 px (16 a 390, 32 e 24 nel telefono grande); i bottoni di chiamata contengono il numero. Sul verde scuro le stesse due varianti in bianco.
14. **Modulo e "dove" per il mestiere: passa, con riserva.** Campi per chi ordina: che cosa ti serve (ordine, diventare rivenditore, listino, schede di sicurezza, quantità per un cantiere, altro), nome, negozio o impresa, città e provincia, partita IVA, telefono, email, prodotti, codici e quantità, messaggio; controllo dei campi obbligatori. L'allegato (ordine in file) non si può mettere in un mailto: la pagina chiede di allegarlo all'email, il LEGGIMI di collegare il modulo a un servizio. Sede con "Apri la mappa" e "Apri la sede nel navigatore"; nessun iframe di mappa.
15. **Piede completo: passa.** Quattro colonne: ragione sociale e indirizzo con indicazioni; Prodotti; Azienda con la dichiarazione di prestazione; Contatti con telefono, fax, due email, orari e stato. Riga legale con ragione sociale, P.IVA e C.F., REA, capitale sociale, Privacy e Cookie. Testo di almeno 14 px.

### Compiti della scheda d'uso (`_prova/uso/SCHEDA.md`, par. 8)

Prove di `node _prova/script/pro_shots.mjs` (41 su 41 riuscite):
- *Negoziante, 1440*: telefono ordini, orari e stato senza scorrere (martedì 10.00 "Aperto ora, fino alle 12"); "Codici e confezioni" apre l'elenco dei 96 prodotti con 179 link PDF, filtro Artelinea; "Diventa rivenditore" porta al modulo con il tipo già scelto, il modulo vuoto si ferma con l'avviso, pieno compone l'email (letta, non inviata); "gesso murario" nella ricerca mostra in un clic la scheda di sicurezza; il codice 4302010 trova il gesso murario. Il catalogo in PDF non esiste: l'elenco si stampa o si salva in PDF dalla pagina.
- *Privato, 390*: ricerca e "Chiama" senza scorrere; "fughe" porta allo stucco per fughe con la scatola; "Caminetti e stufe" in un tocco porta alla malta refrattaria con "Inizio presa 30 minuti" e "Uso interno/esterno"; "Dove lo compro?" nella prima schermata porta alla risposta; dal menu "Dove si comprano" si ferma sotto la testata e il menu si chiude.
- *Professionista*: "Schede per professionisti" nella prima schermata a 390 (a 1440 "Sacchi Artelinea e schede tecniche"); l'elenco filtrato Artelinea ha formati, codici e PDF; la sede si apre nel navigatore in un tocco.
- *Orari*: 13.10 "riapre alle 14"; 19.30 "riapre domani alle 8"; sabato "riapre lunedì alle 8"; 8 dicembre e Pasquetta "Chiuso oggi, festivo"; 15.00 "Aperto ora, fino alle 18".

### Caratteri e licenze

- **Encode Sans** (The Encode Project Authors), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; file variabili (peso 100-900, larghezza 75-125 %) serviti dalla pagina in `sito/fonts/`, licenza in `sito/fonts/OFL.txt`. Pesi usati 400 e 700, larghezze 100 % e 75 %.
- **Foto**: solo materiale di Nardi dalla libreria media di narditalia.com (scaffale, magazzino, sede, rendering delle confezioni, logo), da usare con il loro permesso. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno (`assets/CREDITI.md`).

### Controlli fatti (3/11/2026)

- Nessuno scorrimento orizzontale e nessuna sovrapposizione di testi a 320, 390, 768, 1024, 1440 e 1920; nessun errore di script.
- `tel:+390498790626` ovunque; `mailto:` con oggetto (info@ per ordini e richieste, sicurezza@ per le schede di sicurezza); mappe con `google.com/maps/dir/?api=1&destination=Via Sant'Antonio 24/a, 35020 Tombelle di Saonara PD`; 176 PDF delle schede controllati (tutti rispondono 200) più la dichiarazione di prestazione.
- Nessun U+2014 in pagina, nei .md e negli script (controllo nel `build_finale.sh`).
- Dati: ogni fatto in pagina viene da `01-analisi.md`, dalla scheda d'uso o dalle schede prodotto del loro sito; quello che è dubbio sta nel LEGGIMI.
