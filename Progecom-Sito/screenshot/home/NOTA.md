# Progecom, home: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh` (immagini `pro_img.py`, sorgente `pagina-pro.html`, screenshot e prove di larghezza `pro_shoot.mjs`, controlli delle regole e dei compiti d'uso `pro_controlli.mjs`, esito in `_prova/pro_controlli.json`).
La versione precedente (pistone quotato, sei tappe "Dal forno al getto"), con la sua nota, è in `_prova/versione-1-originale/`.

## Livello professionale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso), più la scheda d'uso `_prova/uso/SCHEDA.md`.
Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14; le pagine intere di barth e Cly-Del, a pezzi. Da barth la home fatta di tipografia con i numeri in fila; da Cly-Del la dichiarazione del mestiere in alto, i blocchi pieni alternati (chiaro, antracite) e le schede con il filetto.

Progecom non aveva una versione 1 con l'uso: la home precedente era quella del pistone. L'uso viene quindi dalla scheda, compito per compito.

### Cosa cambia e perché

- **Ordine della pagina, preso dalla scheda (par. 6).** Testata fissa, apertura, le 16 famiglie in 4 gruppi, forni e ricambi, servizio, usato, chi siamo con STEMIN, richiesta con il modulo, piede. È la struttura M di A1 (dichiarazione, competenze con immagine, numeri, rappresentanza, contatti) adattata a un agente con un solo telefono.
- **Apertura.** Il titolo resta "Metalli non ferrosi" (la testata del loro sito), e dentro lo stesso H1 c'è il mestiere: "Prodotti, impianti e assistenza per fonderie di alluminio, zinco e rame". Sotto: "Mestrino (PD), dal 1990", il bottone pieno "Chiama +39 348 604 6875", il bottone bordato "Scrivi: manda misura, codice o foto" (email a commerciale@ con oggetto e traccia), la riga "Magazzino a Mestrino · consegne in tutta Italia · manutenzione forni anche nel week-end" (l'ultima voce porta alla sezione Forni). A 1440 l'email è anche in chiaro. A destra il loro magazzino crogioli, dall'anteprima del loro video; al telefono è una fascia 16:9 bassa (219 px su 844, il 26 %).
- **Prodotti: elenco aperto, niente schede da aprire.** Le 16 famiglie, ognuna con il link alla sua pagina e i dati veri delle fonti (Long-Life ISO, resistenze a filo e SiC, rotore Ø 250 x 80 mm fino a 2000 cicli, maglia da 1,0 a 2,5 mm, Ø 50-180 mm, EN AB 46000...). Ricambistica forni è la seconda voce. Ogni gruppo ha una foto loro 4:3. Cerca nella pagina trova crogioli, resistenze, rotore, pistoni, 46000, zinco.
- **Forni e ricambi: blocco antracite suo.** Manutenzione e pulizia "anche nel week-end", la loro frase "Siamo convinti che... dei Vostri forni" con la V maiuscola, l'elenco dei ricambi, Chiama, "Fissa la manutenzione per email" e "Manda la foto del pezzo da sostituire", entrambe email con l'oggetto e i campi già scritti.
- **Servizio.** "Ordini evasi in tempi molto brevi, su tutto il territorio nazionale" (loro), la fila dei quattro fatti (1990, 16, Week-end, Italia) e tre punti con le loro parole (magazzino, dalla fase iniziale al post vendita, certificati e formazione).
- **Usato.** Quattro macchine con capacità, prezzo e costo del nuovo, e per ognuna "Chiedi di questo" (email con la macchina nell'oggetto); "Tutto l'usato"; il riquadro "Hai un forno da vendere?" con Chiama e "Proponi il tuo forno".
- **Identità.** Il loro logo con la fascia oro, non ricolorato; la scritta PROGECOM in un serif bold come quella di oggi (Tinos 700) con "di Poggese Mauro"; oro #AF8642 del logo e antracite #2F2E2E del loro tema; nessuno slogan, frasi loro in "noi". STEMIN è una riga con la didascalia, senza le loro foto.
- **Tolto.** Il pistone isolato su beige (oggetto scontornato su fondo chiaro), il carter di repertorio con "foto indicativa", la siviera di Grieveson, i lingotti STEMIN a tutta larghezza, le sei tappe a schede, il fondo #ECEBE6, la scritta PROGECOM in Archivo largo.

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa (84 px a 1440, 72 a 390) con il bottone bordato "348 604 6875" alto 48 px; a metà pagina, a 1440 e a 390, si vede e si tocca (`elementFromPoint`). C'è anche la voce "Richiesta". 6 link `tel:`, tutti `tel:+393486046875`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** 1440 x 900: H1 con "fonderie di alluminio, zinco e rame", "Mestrino (PD), dal 1990", Chiama a 394 px, Scrivi, l'email in chiaro, la foto del magazzino e già il titolo dei prodotti (757 px). 390 x 844: lo stesso, Chiama largo quanto la colonna (350 px) a 295 px, Scrivi sotto, la riga dei servizi, la fascia della foto.
3. **Immagine vera nell'apertura: passa, con riserva.** È il loro magazzino crogioli (scaffali di crogioli imballati), ma è un fotogramma di video 1280 x 720, un po' morbido: usato a 515 px a 1440 e a 390 px al telefono, mai ingrandito. La foto vera da fare è nel LEGGIMI. Nessuna illustrazione, per scelta del committente.
4. **Zero repertorio: passa.** `indicativ` compare 0 volte; in `sito/img/` solo magazzino, le quattro foto dei gruppi e il logo.
5. **Foto in serie: passa, con riserva.** Stesso trattamento per tutte (bianco neutro, saturazione 88 %, contrasto leggero); due formati (4:3 e, solo al telefono e sul tablet, 16:9 per il magazzino); una didascalia su cinque foto. Restano foto da telefono di giorni diversi: la serie vera è lo still life del LEGGIMI.
6. **Palette dal marchio: passa.** `--oro` #AF8642 (fascia del logo), con `--oro-scuro` #8C6A33 per bottoni e testo (5,0:1 con il bianco) e `--oro-buio` per il passaggio del mouse; `--antracite` #2F2E2E (tema del loro sito); il resto sono bianco e grigi neutri, nessun beige. Nessun colore fuori da `:root`.
7. **Scala tipografica corta: passa.** 7 misure a 1440 (14, 17, 19, 23, 32, 48, 72) e 6 a 390 (14, 17, 20, 26, 30, 40); testo corrente 19 px a 1440 e 17 a 390; nessun testo sotto i 14 px; H1 72 e 40, H2 48 e 30.
8. **Due famiglie al massimo: passa.** Archivo per titoli, testo e interfaccia (pesi 400 e 700); Tinos 700 solo per la scritta PROGECOM nel marchio, come il serif del loro logo di oggi.
9. **Servizi in schede con la foto: passa in parte.** Griglia di 4 colonne, una per gruppo, ognuna con la foto loro 4:3 (stesso taglio), il nome e le voci cliccabili con la freccia. Le 16 voci singole non hanno una foto ciascuna: non ce ne sono di loro che reggano.
10. **Almeno tre tipi di prova: non passa (2 su 4).** Ci sono la fila dei quattro fatti (due sono cifre: 1990 e 16) e la rappresentanza STEMIN con la didascalia. Mancano recensioni (non esistono), clienti con il nome (il sito dice solo "importanti aziende") e certificazioni: non inventati, da chiedere (LEGGIMI).
11. **Lavori con un nome: non passa.** Nessun lavoro con cliente, luogo e anno nelle fonti (LEGGIMI).
12. **Ritmo a blocchi: passa.** Due blocchi antracite (Forni e ricambi, Richiesta) e due grigi (Prodotti, Usato) alternati al bianco, piede grigio. Sezioni a 120 px a 1440 e 72 a 390; contenitore 1280 px con margini 80 a 1440, 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno oro scuro e bordato, raggio 3 px, 56 px (48 in testata), testo 17 px; tutti i bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: passa.** Modulo M: nome, azienda, email, telefono, tipo di richiesta (offerta, ricambio, manutenzione nel week-end, usato da comprare o da vendere, altro), prodotto o norma, misura, lega e quantità, messaggio, e l'istruzione per allegare disegno (PDF, DXF, STEP) o foto all'email. Controllo dei campi obbligatori con l'avviso e il fuoco. Indirizzo con "Vai alla mappa" (Google Maps); nessun iframe.
15. **Piede completo: non passa.** Quattro colonne, testo di almeno 14 px, ragione sociale, P.IVA 05018460286, indirizzo con la mappa, telefono e due email cliccabili, Privacy e Cookie. Mancano gli orari (non pubblicati) e le certificazioni (nessuna nelle fonti): non si scrivono finché l'azienda non li dà (LEGGIMI).

### Compiti della scheda d'uso (par. 8)

- *Cliente abituale, 390 x 844.* Chiama a tutta larghezza a 295 px (`tel:`, alto 56 px); Scrivi con l'oggetto "Richiesta d'offerta dal sito" e la traccia (prodotto, misura, quantità, allego foto) a 361 px; il numero resta nella testata fissa in ogni punto; la manutenzione "anche nel week-end" è a un tocco dalla riga dei servizi e a due dal menu (Menu, Forni e ricambi), con Chiama e "Fissa la manutenzione per email".
- *Fonderia nuova, 1440 x 900.* In prima schermata cosa fa, dove, da quando, per quali metalli, telefono ed email in chiaro; subito sotto le 16 voci aperte, ognuna con almeno un dato o il rimando alla scheda; "Non trovi la voce? Mandaci misura o disegno" accanto all'elenco; STEMIN è una riga, senza foto.
- *Usato.* Voce "Usato" in testata (un tocco; al telefono il menu porta l'usato sotto la testata, provato); quattro macchine con capacità, prezzo e costo del nuovo, "Tutto l'usato", "Hai un forno da vendere?" con telefono ed email.
- *Identità.* Ogni foto è loro, il logo è il loro con la fascia oro, nessun orario e nessun servizio non pubblicato (WhatsApp, 24 ore).

### Caratteri e licenze

- **Archivo** (Omnibus-Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero: `sito/fonts/archivo-var-latin.woff2` (file variabile già usato prima), licenza in `sito/fonts/OFL-Archivo.txt`.
- **Tinos** 700 (Steve Matteson), Google Fonts, Apache License 2.0, uso commerciale libero: `sito/fonts/tinos-700-latin.woff2`, licenza in `sito/fonts/LICENSE-Tinos.txt`. Solo per la scritta PROGECOM.
- Foto: solo materiale loro (il fotogramma del loro video e quattro foto del loro sito), elenco e diritti da confermare in `assets/CREDITI.md`. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Controlli fatti

- `pro_controlli.mjs`: regole 1-9 e 12-14 superate nelle misure (3, 5 e 9 con le riserve scritte sopra); 10, 11 e 15 no. Nessuna ancora senza destinazione, nessun `href="#"`, tutti i 14 `mailto:` con l'oggetto, una sola mappa (Google Maps, Via Udine 24, 35035 Mestrino PD). Il modulo vuoto si ferma con l'avviso e il fuoco sul nome; compilato compone l'email (intercettata, non inviata) con l'oggetto "Ricambio per forno: resistenza SiC (Fonderia di prova)".
- `pro_shoot.mjs`: nessuno scorrimento orizzontale e nessuna sovrapposizione fra testi a 320, 390, 768, 1024, 1280, 1440 e 1920. Altezza 6844 px a 1440 e 11941 a 390.
- Screenshot guardati a pezzi: pagine intere a 1440 e 390, prime schermate a 320, 768 e 1024 (le prove sono state cancellate dopo).
- Nessun U+2014 in pagina, negli script e nei .md.
