# Nord Service, home: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh --immagini`. La versione precedente ("Tornano nuove", pala scontornata su carta) è copiata com'era in `_prova/versione-1-originale/` (sito e screenshot, con la sua nota).

Screenshot in questa cartella, fatti all'ora simulata martedì 3 novembre 2026 alle 10 (stato "Aperto ora"): `home-1440.jpg` (7165 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (10558 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (contatti e piede).

## Livello professionale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; "non è tarato bene per loro"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia S (servizi tecnici e imprese). Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14; le pagine intere di Wilson ed Eggentaler (in colonne) e di Kline (a pezzi con `slice.py`). Scheda d'uso: `_prova/uso/SCHEDA.md`.

Per Nord Service non c'era una "versione 1 con l'uso": la home di prima era la "Tornano nuove". Questa passata fa insieme l'uso della scheda e il livello professionale.

### Cosa è cambiato e perché

- **Titolo**: via lo slogan "Tornano nuove" (la scheda lo indica come falso per loro); al suo posto la riga del loro logo, "Verniciatura e sabbiatura industriale", in H1 a 72 px (36 sul telefono), Archivo 700 stretto al 78 %: richiama le lettere condensate del logo.
- **Apertura come i riferimenti S** (Kline, Wilson): occhiello "Carrozzeria industriale a Mestrino (PD)", titolo, riga con i link ai mezzi ("Carrozzeria e vetri di macchine da lavoro, camion e rimorchi e mezzi agricoli: tutta la macchina o un pezzo solo"), la prova "Da oltre 40 anni nel settore: Stefano Barbieri e il figlio Leonardo", i bottoni "Chiama 049 900 5162" (pieno arancio) e "Manda le foto della macchina" (bordato, mail con oggetto e traccia), orari con lo stato e officina con "Indicazioni". A destra la WA320 vera sul loro piazzale, 1:1, 519 px (sorgente 4000 px), non scontornata. A 1440 sotto, ancora nella prima schermata, la fila "Su che mezzi lavoriamo" con i sei link.
- **Testata fissa** con il bottone del telefono (48 px) e cinque voci con le loro parole (Mezzi, Lavorazioni, Lavori, Chi siamo, Contatti e orari); sotto 1100 px "Menu" a tendina.
- **Mezzi in schede con le loro foto** (blocco nero): Movimento terra (CAT 330C), Movimentatori (due T510), Gru e sollevatori (autogru), Camion e rimorchi (Scania), Mezzi agricoli (rimorchio agricolo), Pezzi e componenti (torretta 813). Tutte 4:3, tutta la scheda cliccabile: porta al modulo con il mezzo già scelto.
- **Lavorazioni**: tre garanzie brevi con le loro parole (intera o un pezzo solo; interventi localizzati sul danno; garnet, poca polvere e meno rischi per la salute) e le sei lavorazioni numerate con la loro frase e un link al modulo con la lavorazione già scelta; sui vetri anche "Mezzo fermo? Chiama".
- **Lavori** (grigio chiaro): il D8R in tre quadrati affiancati, sempre visibili (via le linguette "scegli il giorno"), poi tre lavori 4:3 (mini escavatore in carta e nastro, due virole, T916).
- **Chi siamo** sul grigio del logo: la loro frase sulla famiglia, tre cifre (40+, 2, 6), ragione sociale, P.IVA, officina e sede legale.
- **Contatti** su arancio pieno: il telefono come titolo grande (96 px, 48 sul telefono, il gesto di scala della pagina), stato, tabella degli orari, mail, indirizzo, "Indicazioni per l'officina", "Cosa scriverci"; a destra il modulo per il mestiere.
- **Piede** nero in quattro colonne: logo con le lettere bianche, Lavorazioni, Mezzi, Officina; riga legale con Nord Service SRL, P.IVA, sede legale, Privacy e Cookie.
- **Tolto**: la pala scontornata e ritoccata, la carta beige, le linguette, la fascia 2:1, il dettaglio dei cingoli, le didascalie con le date come decorazione.

### Esito regola per regola

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: PASSA.** Testata fissa 88 px a 1440 e 72 a 390, bottone arancio 48 px ("Chiama 049 900 5162", sotto 520 px solo il numero). A metà pagina, a 390 e a 1440, il bottone si vede e si tocca (`elementFromPoint`). 5 link `tel:`, tutti `tel:+390499005162`.
2. **Mestiere, luogo, prova e azione nella prima schermata: PASSA.** 1440x900: H1 con "sabbiatura", occhiello con Mestrino, "Da oltre 40 anni nel settore", Chiama a 474-530 px, mail, Indicazioni, foto, la fila dei mezzi. 390x844: lo stesso; il Chiama è largo quanto la colonna (350 px, 56 di altezza) a 348-404 px, la mail delle foto a 414-470, orario e stato a 517, Indicazioni a 544-594.
3. **Immagine vera nell'apertura: PASSA, con riserva.** La WA320 sul loro piazzale (Sony), non scontornata, col suolo vero. Non mostra persone né la sede: la foto di Stefano e Leonardo è la prima del LEGGIMI. A 390 la foto comincia a 619 px e se ne vedono 225 su 292 senza scorrere.
4. **Zero repertorio: PASSA.** `indicativ` 0 volte; 13 foto in pagina, tutte loro; nessuna da banche d'immagini; nessuna illustrazione.
5. **Foto in serie: PASSA, con riserva.** Tre formati (1:1 apertura e D8R, 6:5 apertura sul telefono, 4:3 schede e lavori); nessuna didascalia sotto le foto (i nomi sono titoli di scheda); trattamento comune leggero (colore 0,92, contrasto 1,04, verde del pavimento del D8R smorzato). Le luci restano diverse perché sono foto da telefono: la serie vera è nel LEGGIMI.
6. **Palette dal marchio: PASSA.** Arancio #EF7821 del logo (con #A9500F per il testo arancio su bianco, 5,5:1), nero #161616, grigio #4C4C4B del logo, bianco e grigio chiaro freddo #F1F1F1. Nessun colore scritto fuori da `:root`. Niente beige. Contrasti: nero su arancio 6,4:1, bianco su grigio 8,6:1, arancio su grigio 3,0:1 solo per le cifre grandi.
7. **Scala tipografica corta: PASSA.** 7 misure a 1440 (14, 17, 19, 23, 48, 72, 96) e 6 a 390 (14, 17, 20, 30, 36, 48); testo corrente 19 px a 1440 e 17 a 390; niente sotto i 14 px; H1 72/36, H2 48/30.
8. **Due famiglie al massimo: PASSA.** Una sola, Archivo, pesi 400 e 700; titoli e cifre in larghezza 78 %.
9. **Servizi in schede con la foto: PASSA.** Sei schede in tre colonne a 1440 (due a 768, una sul telefono con la foto a sinistra), tutte 4:3 con la loro foto, nome, riga e link, tutta la scheda cliccabile. Le sei lavorazioni restano un indice numerato senza foto: non ci sono foto vere di ognuna (LEGGIMI).
10. **Almeno tre tipi di prova: NON PASSA (1 su 4).** Ci sono tre cifre vere (40+ anni di Stefano, 2 generazioni, 6 lavorazioni), meno delle 4 chieste. Recensioni, certificazioni o fornitori e clienti con il nome non sono nelle fonti e non sono stati inventati (LEGGIMI, punti 4, 6, 7, 8).
11. **Lavori con un nome: NON PASSA.** Quattro lavori con macchina e mese (D8R ottobre 2024 con tre date, mini escavatore dicembre 2024, virole maggio 2025, T916 febbraio 2025), il D8R in tre foto larghe insieme quasi tutta la pagina; mancano il cliente o il luogo e i dati del lavoro (LEGGIMI, punto 9).
12. **Ritmo a blocchi: PASSA.** Blocchi pieni oltre al piede: mezzi nero, chi siamo grigio del logo, contatti arancio; lavori grigio chiaro. Sezioni a 120/120 px a 1440 (apertura 96 sotto) e 72/72 a 390; margini 80 px a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: PASSA.** Pieno arancio e bordato nero, raggio 4 px, 56 px (48 in testata), testo 17 px; i bottoni di chiamata contengono il numero.
14. **Modulo e "dove e quando" per il mestiere: PASSA, senza i comuni.** Modulo con nome, azienda, telefono, email, mezzo (tendina), marca e modello, lavorazione (tendina), cosa c'è da fare, dove si trova la macchina, urgenza (macchina ferma, entro il mese, senza fretta) e la nota sulle foto da allegare; la loro frase "Più sei specifico...". Controlla nome e telefono (avviso e fuoco sul campo); compone la mail con oggetto e campi (da collegare a un servizio, LEGGIMI). Nessun iframe. L'elenco dei comuni non c'è: le macchine arrivano in officina sul carrellone e nessuna fonte dice una zona (LEGGIMI, punto 5); al suo posto officina, orari e "Indicazioni".
15. **Piede completo: PASSA, senza certificazioni.** Quattro colonne a 1440, testo di 14-17 px; Nord Service SRL, P.IVA 04717810289, officina, sede legale, telefono ed email cliccabili, orari, lavorazioni e mezzi, Instagram con il nome dell'account, Privacy e Cookie. Certificazioni: nessuna nelle fonti.

### Compiti della scheda d'uso (par. 8)

- *Visitatore 1, telefono 390x844*: "Verniciatura", "sabbiatura" e "macchine da lavoro" sopra i 844 px; Chiama 56 px a 348 px e telefono in testata; "Lun-ven 7:00-17:30" con lo stato calcolato sull'ora di Roma a 517 px; mail con oggetto "Foto della macchina da valutare" e traccia (marca e modello, cosa c'è da fare, dove si trova, nome e telefono, quali foto) a 414 px; la fila dei mezzi comincia a 1007 px (scheda Movimento terra a circa 1230, Movimentatori subito dopo). RIESCE.
- *Visitatore 2, computer 1440x900*: foto vera, telefono, mail e indirizzo sopra 900 px; le tre foto del D8R visibili insieme senza clic; le virole e la torretta 813 come componenti con il nome; Stefano e Leonardo Barbieri, Nord Service SRL, P.IVA e sede legale in "Chi siamo" e nel piede. RIESCE.
- *Visitatore 3, telefono*: "vetri", "camion e rimorchi" e "mezzi agricoli" già nella riga della prima schermata (link alle schede e alla lavorazione), le schede "Camion e rimorchi" a 1708 px e "Mezzi agricoli" a 1849; "Indicazioni" con "Via Levico 20 35035 Mestrino PD" nella prima schermata; il telefono resta nella testata fissa. RIESCE.
- *Per tutte*: nessuno scorrimento orizzontale; nessuna foto di repertorio; logo vero e arancio #EF7821 nella prima schermata; niente prezzi, tempi o zone.

### Controlli fatti

- `pro_controlli.mjs`: regole 1-9 e 12-15 superate nelle misure; 10 e 11 no (sopra). Nessuno scorrimento orizzontale e nessuna sovrapposizione nell'apertura a 320, 360, 390, 768, 1024, 1280, 1440 e 1920; nessuna ancora senza destinazione; nessun errore di script; menu del telefono aperto e chiuso dopo la scelta, ancora sotto la testata (88 px); clic su "Scrivici" dei vetri: lavorazione "Sostituzione vetri" e urgenza "Macchina ferma" già scelte; invio vuoto fermato con l'avviso e il fuoco sul nome; mail composta e letta senza inviarla.
- Stato a ore diverse: martedì 6:30 "Chiuso, apre oggi alle 7:00"; 10:00 "Aperto ora"; 17:45 "riapre domani"; venerdì sera e sabato "riapre lunedì"; 8 dicembre e Pasquetta 2027 "Chiuso oggi, festivo, riapre domani"; vigilia di Natale sera "riapre lunedì". Senza JavaScript resta l'orario scritto.
- Screenshot guardati: prime schermate a 320, 390 e 1440; pagine intere a 1440 (a pezzi), 390, 768 e 1024 (in colonne). Corretti durante il lavoro: lo stato su due righe sul telefono (ora righe orario/stato e indirizzo/Indicazioni), il titolo dei lavori che andava a capo sull'anno, la scritta "REDMI NOTE 8 PRO" in due foto (tagliata), lo spazio nel bottone "Chiama".
- Collegamenti: `tel:+390499005162` (5); `mailto:info@nordservice.net` (3, con oggetto; quello delle foto con la traccia); Google Maps con "Nord Service Via Levico 20 35035 Mestrino PD" (percorso in apertura e nei contatti, ricerca nel piede); Instagram.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script nuovi.

### Caratteri e licenze

- **Archivo** (Omnibus-Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; servito dalla pagina (`sito/fonts/archivo-latin.woff2`, `archivo-latin-ext.woff2`, variabile con asse di larghezza), licenza in `sito/fonts/OFL.txt`.
- Foto: solo di Nord Service SRL (`assets/CREDITI.md`), da usare con il loro permesso. Nessuna foto di repertorio, nessuna immagine generata, nessuno scontorno, nessun disegno.
