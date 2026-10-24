# Home finale, "Un'etichetta sul bianco"

Pagina: `sito/index.html`, statica, si apre anche con file:///. Immagini in `sito/img/` (32 file WebP e PNG), caratteri in `sito/fonts/`. Tutto si rifà con `_prova/script/build_finale.sh`, che lancia `font_finale.sh`, `etichetta_oro.py`, `immagini_finale.py` e gli screenshot. I controlli del gesto, del menu, del piede e delle larghezze stanno in `controlli_finale.mjs`. Alta 4978 px a 1440 con il piede, 4966 a 390.

## L'idea

La loro identità c'è già: la facciata di Saonara è una lastra dorata che si arriccia come un'etichetta che si stacca, e il logo è una scritta a mano dentro un'etichetta con l'angolo sollevato. La prima schermata la porta in piccolo, come oggetto del mestiere: un'etichetta autoadesiva in lamina oro con il loro logo stampato in blu e l'angolo in basso a sinistra che si solleva dalla carta, come nel logo. Coprendo il nome, la pagina non si sposta su un altro etichettificio, perché l'oggetto è la loro facciata in formato etichetta. La chiusura la riprende con la facciata vera.

L'etichetta è un fotomontaggio fatto con `etichetta_oro.py` da una foto vera di lamina oro (Katie Harp, Unsplash) e dal logo dell'azienda: il ricciolo si avvolge su un cilindro con la geometria esatta e le ombre sono calcolate dall'altezza del lembo. Non è un'immagine generata dall'IA. Va sostituita dallo scatto vero, descritto nel LEGGIMI come foto n. 1.

## Le prime schermate

- **1440.** In alto il logo blu pulito e il menu (Etichette, Servizi, Certificazioni, Contatti, telefono). A sinistra "Etichette autoadesive" a 152 px, dal loro "Produzione di etichette autoadesive". A destra il paragrafo, il bottone "Preventivo gratuito" e il telefono. Sotto, appoggiata in basso a destra con il suo margine (bordo destro dell'etichetta sul margine di 64 px), l'etichetta oro larga circa 630 px. A sinistra, in basso, i tre dati in una lista a filetti: Stampa, Lamina, Supporto. In fondo una sola riga "Le immagini della pagina sono indicative".
- **390.** Logo, "Menu", titolo su due righe, l'etichetta quasi a tutta larghezza, paragrafo, bottone e telefono: tutto nella prima schermata. Poi i tre dati.
- **961-1200** tiene l'impaginazione del computer con il titolo a 10vw; **sotto 960** l'etichetta scende sotto il titolo, paragrafo e dati vanno su due colonne; **sopra 1808** i margini crescono e il testo resta su 1680 px.

Dopo vengono i quattro settori con le schede, i servizi (2x2 a filetti) e il nastro in macchina a tutta larghezza, la frase dei certificati con le due voci, la chiusura "b con foto" e il piede.

## Cosa è cambiato in questo passaggio (giudizio cieco del 24/10/2026)

1. **Apertura (bloccante K1).** Tolta la bobina di adesivi elettorali di Element5 ritoccata. Al suo posto l'etichetta in lamina oro con l'angolo sollevato, nitida: file a 2002, 1400, 1000 e 700 px con srcset, quindi 2x a 1440. I bordi dell'immagine tornano esattamente al colore della carta, così non si vede il rettangolo. Il titolo resta corto.
2. **Apertura (bloccante K6).** Tolte le legende a pallino e filetto (il gesto di Agnoletto) e l'oggetto che attraversava la pagina (il gesto di FM Sistemi). I tre dati sono una lista di testo a filetti nella colonna di sinistra, senza segni sull'immagine; l'etichetta è appoggiata in un punto preciso. Sparisce anche il difetto dei numeri 1, 2, 3 senza pallini sotto i 1200 px.
3. **Quattro foto dei settori.** Ora sono tutte su un piano chiaro, con il bianco portato alla carta della pagina e la dominante neutralizzata, e nessuna scritta leggibile: Alimentare sono i due vasetti di Maram visti dall'alto, con le etichette ripulite dalle scritte inglesi e senza la macchia rossa sul bordo; Cosmesi e chimico è una bottiglia con quattro flaconcini dall'alto (Leeloo The First, nuova), al posto della foglia d'oro senza prodotto; Sicurezza è la striscia di bar code con il fondo rosa portato al bianco carta; Multipagina è il flaconcino della stessa serie di Leeloo, ripulito da "STRESS KIT". Non esiste un segnaposto libero e decente di un'etichetta a libretto aperta: lo scatto vero è nel LEGGIMI.
4. **Chiusura senza buco.** `justify-content:flex-start` sul testo e foto con il suo rapporto (1110/720) al posto di `min-height:600px`: tra il titolo e il telefono ci sono 56 px a 1440 e 1024, 32 px a 390. La foto non è più ingrandita oltre il file, quindi è più nitida (1,4x a 1440 su schermo 2x). I riflessi arancio bruciati del ricciolo sono virati verso l'oro della lastra e attenuati; il ricciolo resta perché è il soggetto. Una maschera di contrasto leggera sui bordi.
5. **Testata.** Il bottone Menu parte da 900 px: a 768 il logo finisce a 198 px e il bottone è a 677 px.
6. **Menu del telefono.** Si chiude al tocco su una voce (aria-expanded torna false e la scritta torna "Menu") e con Esc; il logo resta sopra il pannello (z-index).
7. **Schede.** Il testo sotto la foto ha l'altezza del più lungo (misurata da uno script al caricamento, al cambio di larghezza e quando i caratteri sono pronti): l'altezza della pagina è identica con tutte e quattro le schede, da 320 a 2560.
8. **Piede.** Tolto "Contatti" dalla colonna Azienda (c'è già la colonna Contatti). Privacy punta a `termini-duso-e-informative/informativa-privacy/`, la pagina vera; Cookie resta su `termini-duso-e-informative/#cookie`, come sul sito di oggi.
9. **Didascalie.** Le quattro "Foto indicativa" sono sparite: resta una sola riga nell'apertura, "Le immagini della pagina sono indicative". L'elenco completo delle foto da rifare è nel LEGGIMI.

Non ho cambiato idea né direzione: carta, un oggetto, titolo grande, schede, chiusura con la facciata, piede blu notte.

## Chiusura e piede

- **Chiusura.** La frase dello slider di oggi, "Etichette uniche per i vostri prodotti, studiate per dargli il giusto valore". Il telefono grande con tel:, info@eveneto.com con mailto:, l'indirizzo con "Apri la mappa" (Google Maps) e una riga piccola con fax e preventivo gratuito. A destra, fino al bordo, la facciata dorata. Non ci sono orari, perché non sono pubblicati.
- **Piede.** Blu notte #121A3D, l'unico fondo scuro. Logo bianco (342 px, servito a 156) con la riga "Etichette autoadesive e non adesive, in bobina e a foglio, neutre o personalizzate. Saonara, Padova." e quattro colonne con titoletti oro chiaro #D9BD7E: Azienda (Chi siamo, Certificazioni, Preventivo), Etichette (i quattro settori), Servizi (i quattro servizi), Contatti (telefono, email, indirizzo con mappa, fax). A 390 è una fisarmonica con `details` e `summary` veri. In fondo ragione sociale, P.IVA e C.F., REA, capitale sociale, Privacy, Cookie, Accessibilità.
- **Niente newsletter e niente "Seguici".** È un fornitore B2B su commessa: non ha novità, fiere, cataloghi o clienti privati da avvisare, e non ha social (nessun link nel codice del sito, nessun risultato in rete). Al posto della newsletter c'è il link Preventivo.

## Caratteri e colori

- **Mona Sans** di GitHub, scaricata da Google Fonts e servita da `sito/fonts/` (woff2 variabile in larghezza e peso, latin e latin-ext). Licenza SIL Open Font License 1.1, uso commerciale consentito; il testo è in `sito/fonts/OFL.txt`. Una famiglia sola: titoli in peso 380 con larghezza 104 % e spaziatura da -0,04 a -0,03em, testo in 400, enfasi in 540-560. Il riferimento è Autajon: un grottesco aperto e leggero in grande, il prodotto protagonista e tanta aria.
- **Cifre** proporzionali in tutte le righe di numeri: le tabellari di Mona Sans hanno un disegno da monospazio e sembravano codice.
- **Colori.** Carta #F3F1EC, inchiostro #17181C, grigio #56575C (6,4:1 sulla carta), schede non attive #6B6C71 (4,6:1). Il blu del logo #233588 sul bottone, sul filetto della scheda attiva, sul logo e sull'etichetta. Nel piede testo #E9E7EF (13,8:1), secondario #B9BED3 (9,2:1), titoletti #D9BD7E (9,3:1). L'oro è solo nell'immagine.

## Il gesto

Le quattro schede dei settori cambiano foto, frase e dettaglio con un cambio netto, senza dissolvenze. Sono `button role="tab"` con `aria-selected`; da tastiera rispondono a frecce, Home e Fine, a 390 sono una griglia 2x2 da toccare. Le uniche transizioni sono il colore delle schede e il fondo del bottone al passaggio (0,15 s), senza opacità; con `prefers-reduced-motion` non ci sono nemmeno quelle.

## Foto: origine e licenza

Tutte sono segnaposto tranne la facciata. Licenze lette sulla pagina di ogni foto il 24/10/2026, dettagli in `assets/CREDITI.md`. Nessuna è generata dall'IA e nessuna è già usata in un'altra home della campagna.

| In pagina | File | Origine | Lavorazione |
|---|---|---|---|
| Apertura, etichetta oro | `apertura-etichetta-*.webp` (2002, 1400, 1000, 700) | fotomontaggio: lamina oro di Katie Harp (Unsplash `Em96eDRJPD8`) e logo dell'azienda | `etichetta_oro.py`: lamina virata verso l'oro della facciata, logo stampato in blu #233588, angolo arrotolato su un cilindro, ombre calcolate, bordi alla carta |
| Alimentare | `settore-alimentare-*.webp` e `-m-` | Maram, Pexels 35389955 | due vasetti dall'alto, scritte a mano tolte, ruotata di 46 gradi, angoli riempiti con il telo riflesso |
| Cosmesi e chimico | `settore-cosmesi-*.webp` | Leeloo The First, Pexels 20140036 | scritte tolte (resta il codice a barre), ruotata di 90 gradi |
| Sicurezza | `settore-sicurezza-*.webp` | Anna Shvets, Pexels 6250876 | fondo rosa portato al bianco carta, ruotata |
| Multipagina | `settore-multipagina-*.webp` | Leeloo The First, Pexels 20140032 | scritte tolte |
| Servizi | `servizi-nastro-*.webp` | Anthony Roberts, Unsplash `zDcJ2DFew9M` | taglio orizzontale sulla mano e sul nastro |
| Chiusura | `chiusura-facciata-*.webp` (1110, 800) | sito di Etichettificio Veneto, `2015-11-sld02.jpg` | cielo desaturato, riflessi arancio attenuati, maschera di contrasto leggera. L'originale è 1920x720: va rifotografata |
| Testata e piede | `logo-blu.png`, `logo-bianco.png` (342x189) | logo bianco del sito, ricolorato | servito a 150 e 156 px, circa 2,2x. Niente SVG: il ricalco della scritta a mano non sarebbe fedele |

Le quattro foto dei settori hanno lo stesso trattamento (saturazione 0,8, contrasto morbido, fondo neutralizzato e moltiplicato per la carta), tagliate a 2,25:1 con un taglio 4:3 per il telefono.

## Controlli

- **Larghezze.** scrollWidth uguale a innerWidth a 320, 390, 768, 900, 961, 1024, 1200, 1280, 1440, 1920 e 2560 (`controlli_finale.mjs` e screenshot). Guardati a pezzi gli screenshot interi a 1440 e 390 e le prime schermate a 320, 768, 961, 1024, 1200 e 1920: nessuna sovrapposizione, il telefono del paragrafo non tocca più l'etichetta tra 961 e 1200.
- **Gesto.** Clic su Sicurezza mostra Sicurezza; freccia destra passa a Multipagina e ci porta il fuoco; freccia sinistra torna a Sicurezza; Home va ad Alimentare, Fine a Multipagina. A 390 un tocco su Multipagina mostra Multipagina. Altezza della pagina uguale con le quattro schede a tutte le larghezze provate.
- **Menu e piede.** A 390 il menu si apre (aria-expanded true), il logo resta sopra il pannello, al tocco su Servizi si chiude (aria-expanded false). Le colonne del piede partono chiuse al telefono e un tocco su Etichette apre solo quella; sul computer restano aperte.
- **Collegamenti.** 34 link, nessuno vuoto o "#". tel:+390498790566, mailto:info@eveneto.com, mappa `https://www.google.com/maps/search/?api=1&query=Via+Irpinia+51+35020+Saonara+PD`.
- **Chiusura.** Tra il titolo e il telefono 56 px a 1440, 1024 e 768, 32 px a 390 (il giudice chiedeva al massimo 80).
- **Carattere.** Mona Sans caricata dalla cartella `fonts`.
- **Segnali da IA** (`_metodo/kit/segnali.sh`, uscita in `_prova/segnali-finale/`): 0 soglie bloccanti e 0 da guardare. Foto al 37,2 % della pagina, Mona Sans al 100 %, monospazio 0 %, 11 filetti, nessuna freccia, nessuna etichetta maiuscola sopra i titoli, H2 in tre misure (60, 44, 50), date 2009 e 2024.
- **Divieti del committente.** Nessuno: niente gradienti, icone, card, badge sopra il titolo, dissolvenze allo scorrere, effetti che seguono il cursore, corsivi d'accento.
- **U+2014.** Nessuna lineetta lunga in pagina, negli script, in questa nota, nel LEGGIMI e in CREDITI.
- **Dati.** Tutti da `01-analisi.md`: telefono, fax, email, indirizzo, P.IVA, REA, capitale, ISO dal 30/07/2009 con TÜV NORD, FSC-C146871, 8 colori, le quattro tecniche, UE 1169/2011, bassa migrazione, sottobusta, 3 e 5 pagine, cold foil. Il resto è nel LEGGIMI tra le cose da confermare.
