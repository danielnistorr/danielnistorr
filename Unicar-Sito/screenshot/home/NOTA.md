# Unicar, home: nota di progetto

File: `sito/index.html` (statico, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`, con `privacy.html` e `cookie.html`. Tutto si rifà con `sh _prova/script/build_finale.sh` (immagini con `pro_img.py`, controlli con `pro_controlli.mjs`, `pro_prova.mjs` e `pro_orari.mjs`, screenshot con `pro_shoot.py`). Screenshot in questa cartella: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`. Pagina alta 7379 px a 1440 e 10685 px a 390.

Versioni precedenti, copiate com'erano: la home "livello professionale" prima di questo ritocco in `_prova/versione-pro-prima-del-ritocco/index.html` (si apre mettendola al posto di `sito/index.html`); la versione 1 con l'uso (carrello Unsplash sulla corsia gialla, fondo cemento) in `_prova/versione-1-uso/` con i suoi screenshot e la sua nota.

## Livello professionale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia S (servizi tecnici e imprese). Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14, le pagine intere di Kline e Wilson (primo giro) e di Eggentaler e Klindworth (ritocco).

Dalla versione 1 con l'uso: via il repertorio (carrello Toyota di Reding, officina di Yurtman), via il beige e il giallo; restano il titolo "Consulenti, più che riparatori", Archivo, il rosso del logo, lo stato "Aperto ora / Chiuso ora", tutte le email con oggetto e traccia, le mappe, il link a Cami2. In pagina solo le due foto loro (sede e squadra, strisce 939 x 249 del vecchio sito), mai ingrandite.

## Ritocco finale (3/11/2026), dopo il controllore del livello e i tre clienti tipo

Il controllore dava 6 su 10: "pulita e seria, ma un titolare non direbbe 'la voglio così'". Cambiato senza nessuna foto nuova e senza dati nuovi:

- **Apertura.** Il titolo resta, e dentro lo stesso H1 c'è ora la riga del mestiere a 32 px (20 sul telefono): "Assistenza, riparazione e ricambi per carrelli elevatori a Padova". Tolto l'occhiello rosso maiuscolo (andava su due righe al telefono e faceva concorrenza ai bottoni). A destra, al posto del paragrafo grigio e del riquadro rosso, una tavola di quattro fatti con i filetti: **Intervento** "24 ore" in cifre da 48 px, **Orari** con lo stato, **Zona** (Padova e provincia, con il furgone, carrello sostitutivo, "Fuori provincia? Chiamateci"), **Marche e ricambi** con il link "Cercate un ricambio? Cosa mandarci". Il bottone di chiamata ha il numero a 23 px (20 sul telefono) e "r.a." come scrivono loro; finché è in vista, il bottone della testata è bordato, poi torna rosso pieno (un solo rosso pieno alla volta).
- **La sede su antracite pieno.** Tolto il fondo mezzo bianco e mezzo scuro: la foto sta in 8 colonne (845 px, sotto la misura d'origine) dentro il blocco antracite, con accanto "Officina e magazzino ricambi, Via Canada 12, 35127 Padova", "Apri la mappa" e "Indicazioni stradali". A 1440 la foto è tutta nella prima schermata (637-861 px). Nello stesso blocco scuro seguono le tre garanzie (la terza ora è "Ricambi di ogni marca", perché le marche hanno la loro fascia subito sotto) e **la fascia delle marche**, spostata da y≈5300 a subito dopo le garanzie: Toyota, BT, Cesab, Altre in Archivo largo 125 % bianco, didascalie a 17 px.
- **Servizi come indice tipografico.** Via le otto scatole bianche alte 300 px: due colonne di quattro righe, numero rosso a 48 px, nome a 23, riga loro a 17, freccia, filetti. Ogni riga è un link a una sezione (02, 03, 04) o al modulo con il tipo di intervento già scelto (01, 05, 06, 07, 08): nessun programma di posta o di chiamata si apre più per sbaglio cliccando una scheda per leggerla. Sul telefono resta numero, nome e freccia: la sezione passa da 2250 px a circa 900.
- **Ricambi.** Titolo e testo a sinistra (niente più bianco vuoto sotto il titolo), a destra "Cosa mandarci" in tre righe, i due bottoni e un riquadro grigio "Magazzino ricambi" con l'indirizzo che apre la mappa, gli orari con "sabato e domenica chiuso", il telefono e l'email con la stessa traccia completa del bottone.
- **Manutenzione e controlli.** Tolti il promemoria dei mesi, il righello e il file .ics (la scheda d'uso, par. 5 e 7, li indica come cosa "da grafico" e date di legge non rilette). Al loro posto la fascia dei numeri: 3 mesi, 1 anno, 3 anni in cifre da 48 px con l'etichetta accanto, nelle colonne 8-12.
- **Chi siamo.** La squadra in 8 colonne e, accanto, i tre passi (esame tecnico, piano d'intervento, metodo concordato) in colonna: niente più 341 px vuoti a destra.
- **Chiusura.** Nel blocco "Scriveteci" c'è il bottone bordato "Carrello fermo? Scriveteci" con la traccia completa. Il modulo controlla nome, azienda e telefono prima di comporre l'email (avviso a 17 px e fuoco sul primo campo vuoto); con "Ricambio" compare "Pezzo o codice, e quantità" e sparisce "Dove si trova il carrello"; l'urgenza parte da "Subito" solo per carrello fermo e riparazione, altrimenti "In settimana", finché chi compila non la sceglie.
- **Orari.** Lo stato tiene conto dei festivi nazionali e di Pasquetta ("Chiuso oggi, festivo, riapre domani alle 8"); il patrono e le chiusure estive restano da confermare (LEGGIMI).
- **Minori.** Le ancore si fermano esattamente sotto la testata; il link "Scriveteci" fuori orario e "Chiamateci" hanno un'area di tocco di 48 px; tutti i colori sono token (`--rosso-scuro` per il passaggio del mouse, `--linea-scura` per i filetti sul nero; il bordo dei campi usa `--testo-2`); commento nel codice sopra l'elenco dei comuni; nel piede, sotto "Orari e zona", cinque comuni e il link all'elenco.

### Le 15 regole, una per una (dopo il ritocco)

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa 88 px a 1440 e 72 a 390, bottone "049 8792361" alto 48 px. A 390 e a 1440, a metà pagina, il bottone si vede e si tocca (`elementFromPoint`). 10 link `tel:`, tutti `tel:+390498792361`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** A 1440 x 900: H1 con "Assistenza, riparazione e ricambi per carrelli elevatori a Padova", "24 ore" in cifre, bottone di chiamata a 431 px. A 390 x 844: lo stesso, bottone largo quanto la colonna (350 px) a 272 px, poi 24 ore, orari con lo stato, zona con carrello sostitutivo e "Fuori provincia? Chiamateci", marche e il link ai ricambi, tutto senza scorrere.
3. **Immagine vera nell'apertura: passa, con riserva.** La sede vera (insegne Unicar, BT Cesab e Cami2, furgoni, due Cesab), ora incorniciata dal blocco antracite e tutta dentro la prima schermata a 1440. Resta una striscia 939 x 249, senza persone in primo piano: serve la ripresa del LEGGIMI. Nessuna illustrazione, per scelta del committente.
4. **Zero repertorio: passa.** `indicativ` compare 0 volte; in `sito/img/` solo sede, squadra e logo.
5. **Foto in serie: passa.** Due foto, stessa ripresa e stesso trattamento; un formato a 1440 (3,77:1), due tagli sul telefono; nessuna didascalia; nessuna ingrandita.
6. **Palette dal marchio: passa.** `--rosso` #C8141C (C del logo) con `--rosso-scuro` per il passaggio del mouse, `--antracite` #17191B (lettere UNI e AR), neutri freddi. Nessun colore scritto a mano fuori da `:root`. Fondo bianco, nessun beige.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 19, 23, 32, 48, 72, 128) e 8 a 390 (14, 16, 17, 20, 26, 30, 40, 48); testo corrente 19 px a 1440 e 17 a 390; nessun testo sotto i 14 px; le didascalie delle marche ora a 17 px; H1 72/40, H2 48/30. Spariti i 12 radio dei mesi.
8. **Due famiglie al massimo: passa.** Una sola, Archivo, pesi 400 e 700.
9. **Servizi in schede con la foto: non passa.** È un indice tipografico in due colonne, righe tutte cliccabili con numero, nome, riga e freccia, ma senza foto: niente repertorio e niente icone disegnate, per scelta del committente. Le foto da fare per ogni servizio sono nel LEGGIMI.
10. **Almeno tre tipi di prova: non passa (1 su 4).** C'è la fascia delle marche con le didascalie, ora subito dopo le garanzie. Mancano recensioni, numeri aziendali di Unicar, clienti con il nome e certificazioni di Unicar: non sono nelle fonti e non sono stati inventati (LEGGIMI, punti 3, 4, 6, 7). Le cifre 3 mesi, 1 anno, 3 anni sono scadenze di legge, non numeri dell'azienda.
11. **Lavori con un nome: non passa.** Nessun lavoro con cliente, luogo e anno nelle fonti (LEGGIMI, punto 5).
12. **Ritmo a blocchi: passa.** Blocchi pieni oltre al piede: sede, garanzie e marche in antracite, controlli in antracite, chiusura rossa; servizi e zone in grigio. Sezioni a 120/120 px a 1440 e 72/72 a 390 (garanzie 72 sopra, perché continuano la fascia della sede); contenitore 1280 px con margini 80 a 1440, 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno rosso e bordato, raggio 4 px, 56 px (48 in testata), testo 17 px (16 sul telefono); i bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: passa.** Tipo di intervento (10 voci), marca, modello e matricola, pezzo e quantità per i ricambi, indirizzo del carrello, descrizione, urgenza, istruzione per le foto (un mailto non porta allegati); controllo dei campi obbligatori. 20 comuni più "e gli altri comuni della provincia". Nessun iframe di mappa.
15. **Piede completo: non passa.** Quattro colonne, testo di almeno 14 px, telefono ed email cliccabili, orari, zona con cinque comuni e il link all'elenco, sede, Privacy e Cookie. Mancano la ragione sociale completa, la partita IVA (la 01014160285 non è valida nel VIES) e le certificazioni (nessuna di Unicar): non si scrivono finché l'azienda non li dà (LEGGIMI, punti 1 e 7). Lo script delle misure lo segna "sì" perché non controlla la P.IVA: l'esito vero è questo.

### Compiti della scheda d'uso (par. 8) e dei clienti tipo

- *Telefono, carrello fermo (390)*: bottone rosso a tutta larghezza a 272 px (a 320: 340 px, "Chiamate 049 8792361 r.a."), numero a 20 px con "r.a."; sotto "Carrello fermo? Scriveteci" con la traccia; poi 24 ore, orari con lo stato, Padova e provincia con carrello sostitutivo e "Fuori provincia? Chiamateci", marche: tutto nella prima schermata, come nella versione 1 con l'uso. Il numero resta nella testata fissa.
- *Ricambi (1440)*: link in prima schermata "Cercate un ricambio? Cosa mandarci" e voce di menu; "anche prodotto all'estero o uscito di produzione", le tre cose da mandare, "Chiedete un ricambio" (email compilata), magazzino con indirizzo che apre la mappa, orari, telefono ed email con la stessa traccia. Il modulo con "Ricambio" chiede pezzo e quantità e non l'indirizzo.
- *Nuovo cliente (1440)*: marche e zona in prima schermata e nella fascia delle marche sotto la sede; manutenzione e controlli in tre righe con "Chiedete un preventivo"; "Vendita e noleggio" in testata; la riga su Unicar e Cami2 in Chi siamo.
- *Identità*: la sede vera nella prima schermata a 1440 e nella seconda a 390.
- Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1280, 1440 e 1920; nessuna sovrapposizione nell'apertura.

### Caratteri e licenze

- **Archivo** (Omnibus-Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; licenza in `sito/fonts/OFL.txt`. Servito dalla pagina (`sito/fonts/archivo-latin.woff2`, `archivo-latin-ext.woff2`), pesi 400 e 700, larghezze 100 %, 110 % e 125 % (nomi delle marche).
- Foto: solo materiale del loro sito (sede e squadra, `assets/originali/testata/007.jpg` e `008.jpg`) e il logo PNG, da usare con il loro permesso. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Controlli fatti (3/11/2026, dopo il ritocco)

- `pro_controlli.mjs`: regole 1-8 e 12-14 superate nelle misure; 9, 10, 11 e 15 no (vedi sopra). Nessuna ancora senza destinazione.
- `pro_prova.mjs`: menu a 390 aperto e chiuso dopo il clic; ancora "Ricambi" sotto la testata; testata bordata in cima e rossa piena dopo lo scorrimento; riga "Batterie" che porta al modulo con il tipo scelto; invio vuoto fermato con l'avviso e il fuoco sul nome; con "Ricambio" compaiono pezzo e quantità e sparisce l'indirizzo; email composta e letta senza inviarla; nessun errore di script.
- `pro_orari.mjs`: martedì 10.00 aperto; 13.10 "riapre alle 14"; 19.30 "riapre domani alle 8"; sabato "riapre lunedì"; 8 dicembre e Pasquetta "Chiuso oggi, festivo"; vigilia di Natale sera "riapre lunedì" (salta Natale, Santo Stefano e la domenica).
- Screenshot guardati a pezzi a 1440 e a 390, prime schermate e pagine intere a 320, 768 e 1024. Nessun U+2014 in pagina, nei .md e negli script.
