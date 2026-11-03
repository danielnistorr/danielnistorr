# Home di Etichettificio Veneto

Pagina: `sito/index.html`, statica, si apre anche con file:///. Immagini in `sito/img/` (solo la facciata della sede, il logo con la cornice e la favicon), caratteri in `sito/fonts/`. Tutto si rifà con `sh _prova/script/build_finale.sh` (immagini con `pro_img.py`, screenshot, poi i controlli di `pro_controlli.mjs`, esito in `_prova/pro_controlli.json`).

Screenshot (stessi nomi di prima): `home-1440.jpg` (7333 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (12292 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (contatti e piede). La versione 1 com'era prima di questo passaggio (etichetta in lamina oro, settori a schede da cliccare, foto di repertorio) è copiata in `_prova/versione-1-originale/` con la sua nota.

## Livello professionale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente". Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso), sezioni A, B e C. Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14 (in due fogli), le pagine intere di barth e Cly-Del a pezzi. Scheda d'uso: `_prova/uso/SCHEDA.md`.

### Che cosa è cambiato

- **Uso prima di tutto.** La versione 1 non aveva ancora l'uso della scheda: niente orari, niente "Manda il file", niente Stamperia, settori nascosti in schede, preventivo verso una pagina senza allegati. Ora:
  - *buyer a 1440*: nella prima schermata il mestiere e il luogo nel titolo ("Produzione di etichette autoadesive a Saonara (Padova)", la loro frase con il comune), la riga dei fatti (bobina e foglio, neutre o personalizzate, flexo UV, tipografica UV, offset e digitale, fino a 8 colori), la prova nell'occhiello (ISO 9001 dal 2009, FSC-C146871), "Richiedi un preventivo" e "Manda il file", il telefono come bottone in testata, gli orari con lo stato, la facciata vera e, in fondo, la fascia scura con i sei tipi di etichetta come link. Con uno scorrimento ci sono tutte e sei le schede (multipagina, bassa migrazione e RFID visibili insieme); poi la tavola di tecniche, colori e supporti; i certificati con anno e licenza; il modulo con il file;
  - *cliente a 390*: senza scorrere "Chiama 049 879 0566" a tutta larghezza, "Manda file o ordine" (email a info@eveneto.com con oggetto e traccia), "Come arrivare" (percorso in Google Maps) e lo stato "Aperto ora / Chiuso, riapre alle..."; il numero resta nella testata fissa a ogni altezza;
  - *piccolo produttore a 390*: nella seconda schermata i sei tipi di etichetta (con "Dorate e argentate") e la porta della Stamperia di Padova, "Poche etichette, o tante varianti?", con "Chiama 049 640459" e il sito; subito sotto "Etichette dorate e plastificate". A 1440 la stessa porta è anche una riga nell'apertura.
- **Struttura M adattata.** Testata sobria con "Richiedi un preventivo"; apertura con la dichiarazione del mestiere e la sede; settori (sei schede); la Stamperia; tecniche e numeri su blocco scuro; come lavoriamo in quattro passi e l'archivio per le ristampe; qualità con i certificati; preventivo con il modulo del mestiere; contatti con le due "sedi" (Etichettificio Veneto e La Stamperia di Padova), ognuna con telefono ed email; piede in quattro colonne.
- **Foto, decisione "niente".** Tolti l'etichetta in lamina col loro logo (fotomontaggio), i vasetti, i flaconi, la striscia di bar code e il nastro in macchina, e con loro la riga "Le immagini della pagina sono indicative". Resta solo la facciata vera, 1110x720 dal file del loro sito, a 624 px a 1440 (350 px a 390), mai ingrandita. Nessun disegno al posto delle foto.
- **Colori del marchio, niente beige.** Fondo bianco; blu #233588 della scritta del logo per bottoni, link e blocco dei contatti; blu notte #141C47 (lo stesso blu scurito) per la fascia dei settori, le tecniche e il piede; arancio #F28C00 del filo del logo solo sul blu notte (cifre grandi, titoletti) e nei filetti; verde #1F7A45 solo per "Aperto ora". Grigi freddi.
- **Logo vero.** Il logo con la cornice bianca, il filo arancio e l'angolo sollevato, come lo usano loro, in testata e nel piede (nella versione 1 era ritagliato e ricolorato).
- **Dalla versione 1 tengo:** Mona Sans (una famiglia), il blu del logo, il titolo "Etichette autoadesive" dentro la loro frase completa, i testi verbatim dei settori, la frase dello slider "Etichette uniche per i vostri prodotti, studiate per dargli il giusto valore" in chiusura.

### Esito regola per regola

Misure di `node _prova/script/pro_controlli.mjs` più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: PASSA.** Testata fissa di 80 px a 1440 e 64 a 390, bottone "049 879 0566" alto 48 px, più "Richiedi un preventivo" (la voce "Richiesta" della famiglia M) da 701 px in su. A 390, a metà pagina, il bottone si vede e si tocca (`elementFromPoint`). 9 link `tel:`.
2. **Mestiere, luogo, prova e azione nella prima schermata: PASSA.** A 1440x900: H1 con "etichette autoadesive" e "Saonara (Padova)", occhiello "ISO 9001 dal 2009 · FSC-C146871", "Richiedi un preventivo" in testata e nell'apertura. A 390x844: lo stesso, con "Chiama 049 879 0566" largo 350 px (tutta la colonna) a 380 px dall'alto.
3. **Immagine vera nell'apertura: PASSA, con riserva.** La sede vera con la facciata dorata e il logo in rilievo, a 1440 da 346 a 751 px (tutta nella prima schermata), a 390 da 609 a 836 px. È una foto 6 su 10, senza persone né mezzi: va rifatta (LEGGIMI, foto 1).
4. **Zero repertorio: PASSA.** "indicativ" 0 volte; in `sito/img/` solo `sede-facciata`, `logo-etichetta` e `favicon`; nessun riferimento a Unsplash o Pexels.
5. **Foto in serie: PASSA.** Una sola foto, un solo formato (1,54), nessuna didascalia.
6. **Palette dal marchio: PASSA.** Quattro colori (blu, blu notte, arancio, verde solo per "Aperto"), sei neutri; nessun colore scritto fuori da `:root`; nessun token `--carta`.
7. **Scala tipografica corta: PASSA.** 8 misure a 1440 (14, 17, 19, 23, 32, 44, 64, 104) e 8 a 390 (14, 16, 17, 20, 24, 28, 36, 56); testo corrente 19 px a 1440 e 17 a 390; nessun testo sotto i 14 px; H1 64/36 e H2 44/28, nella fascia M.
8. **Al massimo due famiglie: PASSA.** Una sola, Mona Sans, pesi 400 e 650; i titoli in larghezza 112 %, il testo al 100 %; anche modulo e bottoni.
9. **Servizi in schede con la foto: NON PASSA.** Sei schede in tre colonne (due a 768-1100, una sul telefono), tutte cliccabili, con il nome, una riga verbatim e il link; al posto della foto un segno tipografico del settore ("UE 1169/2011", "A coupon", "Bar code e RFID", "3 e 5 pagine", "Sottobusta", "Oro e argento"). Nessuna foto vera di un loro lavoro: per decisione del committente niente repertorio e niente disegni. Le foto da fare sono nel LEGGIMI (foto 2).
10. **Almeno tre tipi di prova: NON PASSA (2 su 4).** Ci sono quattro numeri in cifre da 104 px (8 colori, 4 tecniche, 2009 prima certificazione ISO, 2024 FSC) e la fascia dei certificati con didascalia (ISO 9001:2015 TÜV NORD, FSC-C146871, regolamento UE 1169/2011). Mancano recensioni e clienti con il nome: non sono nelle fonti e non sono stati inventati (LEGGIMI, punti 5, 6 e 7). I quattro numeri sono del mestiere, non aziendali (persone, metri quadri): da chiedere.
11. **Lavori con un nome: NON PASSA.** Nessun lavoro con cliente, anno e dati nelle fonti (LEGGIMI, punto 6). Al loro posto "Come lavoriamo" e l'archivio per le ristampe.
12. **Ritmo a blocchi: PASSA.** Blocchi pieni oltre al piede: la fascia dei settori e le tecniche in blu notte, i contatti in blu; la Stamperia e la qualità in grigio chiaro. Spazi di 120 px a 1440 (96 la Stamperia) e 72/64 a 390; contenitore di 1280 px con margini di 80 a 1440, 20 a 390.
13. **Un solo sistema di bottoni: PASSA.** Pieno e con il bordo, raggio 4 px, 56 px (48 in testata), testo 17 px (16 sul telefono, 15 sotto i 360 px); sul blu le stesse due varianti in bianco. Ogni bottone di chiamata ha il numero.
14. **Modulo e "dove" per il mestiere: PASSA.** Modulo M: nome, azienda (o "privato"), email, telefono, settore, materiale, bobina o foglio, misure, quantità, colori e finiture, avvolgimento e anima, file grafico, note; controllo dei campi obbligatori con avviso e fuoco. "Indicazioni stradali" e "Come arrivare" aprono il percorso in Google Maps; nessun iframe. Le due sedi (etichettificio e Stamperia) hanno telefono ed email ognuna. Il modulo compone un'email (mailto): va collegato a un servizio (LEGGIMI).
15. **Piede completo: PASSA.** Quattro colonne a 1440 (marchio, Etichette, Servizi e azienda, Contatti), testo di almeno 14 px; ragione sociale, P.IVA e C.F., REA, capitale, indirizzo con il percorso, telefono ed email cliccabili, orari, fax, la Stamperia, ISO 9001 e FSC-C146871, Privacy, Cookie e Accessibilità.

### Compiti della scheda d'uso (par. 8), con `pro_controlli.mjs`

- Buyer, 1440x900: cosa e dove nella prima schermata in testo; telefono e "Richiedi un preventivo" senza scorrere, il modulo accetta PDF e AI; multipagina, bassa migrazione e RFID visibili insieme dopo uno scorrimento; tecniche, 8 colori, carta, carta gommata e polipropilene nella stessa tavola; ISO 9001 con la data e FSC con la licenza. Tutto riesce.
- Cliente, 390x844: tel:+390498790566 a un tocco, orari e stato, email con oggetto "Ordine o invio file", indicazioni: tutto nella prima schermata. La testata fissa non copre nulla (la pagina parte sotto di lei e le ancore si fermano sotto la testata). Riesce.
- Piccolo produttore, 390x844: "Poche etichette", "La Stamperia di Padova" e "digitale" nella seconda schermata, tel:+39049640459 a 1459 px e il sito a 1525; "Dorate e argentate" nella fascia e "Etichette dorate e plastificate" nella Stamperia. Riesce.
- Stato degli orari provato a 10 ore e date (`?ora=`): aperto la mattina e il pomeriggio, pausa, prima delle 8, sera, venerdì sera e sabato (riapre lunedì), 8 dicembre, vigilia di Natale sera (salta Natale, Santo Stefano e la domenica), Pasquetta 2027.
- Modulo provato con `?prova=1` (nessuna email aperta, nulla inviato): invio vuoto fermato con il fuoco sul nome; con i dati e un file l'email ha oggetto "Richiesta di preventivo: Prova Srl", il formato, le misure e il nome del file.

### Controlli generali

- Nessuno scorrimento orizzontale e nessuna sovrapposizione in testata e apertura a 320, 360, 390, 768, 1024, 1180, 1280, 1440 e 1920 (misure dello script); screenshot guardati a pezzi a 1440 e 390 interi, e a 320, 768 e 1024. Corretti durante il lavoro: le cifre tabellari di Mona Sans (sembravano di macchina da scrivere, ora proporzionali), il titolo su cinque righe a 390, gli orari spezzati a 320, il campo file con il testo inglese del browser, il menu del telefono (si apre, si chiude al tocco su una voce e con Esc).
- Collegamenti: solo `tel:+390498790566` e `tel:+39049640459`; solo `mailto:info@eveneto.com` (con oggetto) e `mailto:info@lastamperiadipadova.com`; mappe con `google.com/maps/dir/?api=1&destination=Etichettificio Veneto, Via Irpinia 51, 35020 Saonara PD`; nessuna ancora senza destinazione; nessun errore di script.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script nuovi.

### Caratteri e licenze

- **Mona Sans** (GitHub), da Google Fonts, SIL Open Font License 1.1, uso commerciale libero. Servita dalla pagina (`sito/fonts/mona-sans-latin.woff2`, `mona-sans-latin-ext.woff2`, variabile in peso e larghezza), licenza in `sito/fonts/OFL.txt` (le due lineette lunghe della definizione di "Modified Version" sono diventate virgole, per la regola del carattere U+2014; il testo è lo stesso).
- Immagini: solo materiale dell'azienda dal suo sito (facciata `2015-11-sld02.jpg`, logo con la cornice, favicon). Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.
