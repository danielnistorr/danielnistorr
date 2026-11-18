# Progecom, home: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh` (immagini `pro_img.py`, sorgente `pagina-pro.html`, screenshot e prove di larghezza `pro_shoot.mjs`, controlli delle regole e dei compiti d'uso `pro_controlli.mjs`, esito in `_prova/pro_controlli.json`).
La versione precedente (pistone quotato, sei tappe "Dal forno al getto"), con la sua nota, è in `_prova/versione-1-originale/`.

## Livello professionale, ritocco finale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente". Regole: `_metodo/professionale/REGOLE.md`, famiglia M, più la scheda d'uso `_prova/uso/SCHEDA.md`. Ritocco fatto sui difetti del controllore (voto 6) e dei due clienti tipo (8,5 e 7,5).
Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14 (due fogli); le pagine intere di barth e Cly-Del, a pezzi. Da Cly-Del la fascia dei numeri a colore pieno e il piede scuro a quattro colonne; da barth i numeri grandi e la pagina fatta di tipografia; da Holzrausch la frase come manifesto.

### Cosa cambia in questo ritocco e perché

- **Apertura con un gesto.** La foto del loro magazzino esce dalla cornice: va a filo del bordo destro della finestra e occupa tutta l'altezza dell'apertura (595 x 566 px a 1440, mai ingrandita: la sorgente è 960 x 720). Niente più fascia bianca vuota sotto. Didascalia tolta: il fatto ("Magazzino crogioli a Mestrino") è nella riga dei servizi accanto, in tre colonne con il filetto oro. Al telefono resta la fascia 16:9 bassa (219 px su 844).
- **Prodotti senza foto.** Tolte le quattro foto dei gruppi (quattro luci diverse, due con diritti incerti, miniature a 390). Ogni gruppo ha una testata tipografica antracite cliccabile con il nome a 32 px e tre sigle vere in oro (Long-Life ISO, Rotore Ø 250 x 80, CuCo2Be, EN AB 46000...). Sono testo, non illustrazioni. Il titolo "Sedici famiglie di prodotto" sta su una riga e si vede nella prima schermata a 1440 (771 px).
- **Le voci senza dati ora ne hanno.** Dalle loro pagine rilette il 3/11 (sez. 10 di `01-analisi.md`): forni a crogiolo, a bacino, fusione rapida, doppia camera; materassini 64-128 kg/m³ classe 1200 °C; miscelazione acqua-distaccante per 6-8 presse; canaline e tazze; AlMn, AlCu, AlTiB, AlSr; lingotti di zinco da 6-8 kg; bilancia e microscopio USB; le quattro maglie scritte una per una (Cerca trova "1,5x1,5"). Solo i bruciatori restano senza dato: la loro pagina non ha testo.
- **Fascia oro dei numeri.** "Servizio" è un blocco pieno `--oro-scuro` con il testo bianco (5,0:1): 1990, 16 e 3 (metalli) a 160 px a 1440 e 96 a 390. "Week-end" e "Italia" non sono più composti come cifre: stanno nel titolo della sezione e nella sezione Forni.
- **Chi siamo come manifesto.** La loro frase "Perché Progecom? Offriamo nuove soluzioni tecniche..." a 48 px su tutta la larghezza, poi il testo, la riga sui clienti con le loro parole («richiesti dai clienti, di importanti aziende leader») e STEMIN.
- **Ritmo.** Bianco, grigio (prodotti con le testate antracite), antracite (forni), oro (servizio), grigio (usato), bianco (chi), grigio (contatti con il modulo su un riquadro bianco), piede antracite. Mai due fondi uguali a contatto.
- **Tocco al telefono.** "Manutenzione forni anche nel week-end" in apertura è una riga alta 44 px; "Manda la foto del pezzo da sostituire" è un bottone di 56 px; "Chiedi di questo" nell'usato ha 49 px di area; tra PROGECOM e il bottone del telefono ci sono 14 px (erano 6).
- **Menu.** "Richiesta" diventa "Contatti" (la sezione si chiama "Richiesta d'offerta e contatti").
- **Piede.** Antracite, quattro colonne, "il cellulare di Mauro Poggese" sotto il numero.

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa (85 px a 1440, 73 a 390) con il bottone bordato "348 604 6875" alto 48 px; a metà pagina, a 1440 e a 390, si vede e si tocca (`elementFromPoint`). Voce "Contatti". 6 link `tel:`, tutti `tel:+393486046875`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** 1440 x 900: H1 "Metalli non ferrosi" con "fonderie di alluminio, zinco e rame", "Mestrino (PD), dal 1990", Chiama a 394 px, Scrivi, l'email in chiaro, la foto a filo e il titolo dei prodotti a 771 px. 390 x 844: lo stesso, Chiama largo quanto la colonna (350 px) a 296 px.
3. **Immagine vera nell'apertura: passa, con riserva.** È il loro magazzino crogioli, ma è un fotogramma di video, morbido, e mostra scatoloni: la foto vera da fare è nel LEGGIMI. Nessuna illustrazione, per scelta del committente.
4. **Zero repertorio: passa.** `indicativ` compare 0 volte; in `sito/img/` solo il magazzino e il logo. Tolte anche le due foto con diritti incerti.
5. **Foto in serie: passa.** Una sola foto in pagina, due formati (1,05 a 1440, 16:9 a 390 e sul tablet), nessuna didascalia.
6. **Palette dal marchio: passa.** `--oro` #AF8642 (fascia del logo) con le sue due tonalità `--oro-scuro` e `--oro-buio`, `--antracite` #2F2E2E (tema del loro sito); il resto sono bianco e grigi neutri, nessun beige.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 19, 23, 32, 48, 72, 160) e 7 a 390 (14, 17, 20, 26, 30, 40, 96); testo corrente 19 e 17 px; niente sotto i 14 px; H1 72 e 40. Il 160 è il gesto di scala dei numeri.
8. **Due famiglie al massimo: passa.** Archivo per titoli, testo e interfaccia (400 e 700); Tinos 700 solo per la scritta PROGECOM.
9. **Servizi in schede con la foto: non passa (per scelta).** Quattro colonne a 1440, ogni gruppo con una testata cliccabile dello stesso formato, il nome e le voci cliccabili. Le foto non ci sono: quelle che c'erano non reggevano e il committente ha detto "niente". Le foto da fare sono nel LEGGIMI.
10. **Almeno tre tipi di prova: non passa (2 su 4).** Fascia di tre cifre vere (1990, 16, 3) e la rappresentanza STEMIN con la didascalia. Recensioni, clienti con il nome e certificazioni non sono nelle fonti: da chiedere (LEGGIMI).
11. **Lavori con un nome: non passa.** Nessun lavoro con cliente, luogo e anno nelle fonti (LEGGIMI).
12. **Ritmo a blocchi: passa.** Due blocchi pieni (antracite Forni, oro Servizio) oltre al piede antracite, alternati a bianco e grigio. Sezioni a 120 px a 1440 e 72 a 390; margini 80 e 20.
13. **Un solo sistema di bottoni: passa.** Pieno oro scuro e bordato, raggio 3 px, 56 px (48 in testata), testo 17 px; 10 bottoni a 1440, tutti quelli di chiamata con il numero.
14. **Modulo e "dove" per il mestiere: passa.** Modulo M (nome, azienda, email, telefono, tipo di richiesta, prodotto o norma, misura lega e quantità, messaggio, istruzione per allegare PDF, DXF, STEP). Vuoto si ferma con l'avviso e il fuoco sul nome; compilato compone l'email con l'oggetto "Ricambio per forno: resistenza SiC (Fonderia di prova)" (intercettata, non inviata). "Vai alla mappa", nessun iframe.
15. **Piede completo: non passa.** Quattro colonne su antracite, testo di almeno 14 px, ragione sociale, P.IVA, indirizzo con la mappa, telefono e due email, Privacy e Cookie. Mancano orari e certificazioni: non sono nelle fonti (LEGGIMI).

### Compiti della scheda d'uso (par. 8), dopo il ritocco

- *Cliente abituale, 390 x 844.* Chiama a 296 px, Scrivi sotto con oggetto e traccia, numero sempre nella testata fissa; la manutenzione nel week-end è a un tocco dalla riga dei servizi (ora alta 44 px) e a due dal menu; nella sezione ci sono Chiama, "Fissa la manutenzione per email" e il bottone "Manda la foto del pezzo da sostituire".
- *Fonderia nuova, 1440 x 900.* In prima schermata cosa fa, dove, da quando, per quali metalli, telefono ed email; il titolo dei prodotti a 771 px; Cerca trova crogioli, resistenze, rotore, pistoni, 46000, zinco, 1,5x1,5; 15 famiglie su 16 hanno un dato tecnico; STEMIN è una riga senza foto; la riga sui clienti con le loro parole.
- *Usato.* Voce in testata; quattro macchine con capacità, prezzo e costo del nuovo; "Tutto l'usato"; "Hai un forno da vendere?".
- *Identità.* L'unica foto è loro, il logo è il loro con la fascia oro, nessun orario e nessun servizio non pubblicato.

### Caratteri e licenze

- **Archivo** (Omnibus-Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero: `sito/fonts/archivo-var-latin.woff2` (file variabile già usato prima), licenza in `sito/fonts/OFL-Archivo.txt`.
- **Tinos** 700 (Steve Matteson), Google Fonts, Apache License 2.0, uso commerciale libero: `sito/fonts/tinos-700-latin.woff2`, licenza in `sito/fonts/LICENSE-Tinos.txt`. Solo per la scritta PROGECOM.
- Foto: solo il fotogramma del loro video del magazzino crogioli (diritti da confermare, `assets/CREDITI.md`). Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Controlli fatti

- `pro_controlli.mjs`: regole 1-8 e 12-14 superate (3 con la riserva scritta sopra); 9, 10, 11 e 15 no. Nessuna ancora senza destinazione, nessun `href="#"`, tutti i 14 `mailto:` con l'oggetto, una sola mappa.
- `pro_shoot.mjs`: nessuno scorrimento orizzontale e nessuna sovrapposizione fra testi a 320, 390, 768, 1024, 1280, 1440 e 1920. Altezza 7356 px a 1440 e 12871 a 390. `misure_extra.mjs`: distanza logo-telefono, aree di tocco, posizione del titolo dei prodotti.
- Screenshot guardati a pezzi: pagine intere a 1440 e 390, prime schermate a 320, 390, 768, 1024 e 1440 (le prove sono state cancellate dopo).
- Nessun U+2014 in pagina, negli script e nei .md.
