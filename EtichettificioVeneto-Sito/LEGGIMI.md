# Etichettificio Veneto: proposta di nuova homepage

È una proposta non richiesta: c'è solo la home. Non è pubblicata, l'azienda non è stata contattata e non è stato inviato nessun modulo.

## Dove sono le cose

- `sito/index.html`: la home finale, statica (si apre anche con doppio clic). Accanto ci sono `sito/img/` (solo le immagini usate, in WebP a più larghezze, più i loghi in PNG) e `sito/fonts/` (Mona Sans con la sua licenza).
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` e la `NOTA.md`, cioè le scelte, le foto, cosa è cambiato dopo il giudizio cieco e i controlli.
- `_prova/script/build_finale.sh`: rifà caratteri, immagini e screenshot. Usa `font_finale.sh`, `etichetta_oro.py` (l'etichetta oro dell'apertura), `immagini_finale.py` (le altre foto) e `screenshot_jpeg.py`. `controlli_finale.mjs` prova le schede, il menu, il piede, le larghezze da 320 a 2560 e i link. `bobina_neutra.py` era la vecchia apertura e non è più usato.
- `01-analisi.md`: i fatti con le fonti. `assets/CREDITI.md`: le licenze delle foto. `_prova/home/a` e `_prova/home/b`: i due prototipi. `_prova/cieco.json`: il giudizio cieco a cui risponde l'ultimo passaggio.

## Dati da confermare con l'azienda (in pagina non c'è niente di inventato)

- **La facciata e l'etichetta dell'apertura.** La lettura "la facciata si arriccia come un'etichetta che si stacca" è mia, e tutta la pagina ci si appoggia: va chiesto se l'idea dell'architetto era quella e se l'azienda è d'accordo a usare il proprio logo stampato su un'etichetta in lamina come immagine di apertura.
- **Email.** In pagina c'è solo info@eveneto.com, l'unica indicata nell'informativa privacy. Il dominio eveneto.com però mostra "SITO IN COSTRUZIONE". Va confermato che la casella funziona, o se usare etveneto@tin.it, che sul sito di oggi è indicata accanto all'altra.
- **Fax.** Il 049 644547 è ancora attivo? Se non lo è, va tolto dalla chiusura e dal piede.
- **Orari dell'ufficio, PEC, un referente.** Non sono pubblicati e in pagina non ci sono.
- **Cold foil.** La riga "Lamina" e la scheda Cosmesi dicono, come il sito di oggi, che stampano particolari in oro e argento a cold foil. Va chiesto se lo fanno in casa e su quali macchine.
- **"Fino a 8 colori" e le quattro tecniche.** Vanno legati al parco macchine vero: quante flexo, quante digitali, che larghezza.
- **Certificati.** In pagina ci sono la norma, l'ente, la data della prima certificazione ISO (30 luglio 2009) e la licenza FSC-C146871, che è già sul loro sito. Il numero del certificato ISO (44 100 091062) e le scadenze (29/07/2027 per l'ISO, 03/03/2029 per l'FSC) restano fuori finché il cliente non dà il via libera. Per usare il marchio FSC sul sito servono le regole d'uso del marchio.
- **Vino.** Il sito non ne parla mai, e in pagina non c'è. Se lo fanno, si può aggiungere.
- **"Clienti in tutto il Nord Italia" e "consegna rapida con mezzi propri".** Sono due frasi del loro sito (la pagina servizi). Va confermato che si possono tenere.
- **Dati di companyreports.it** (costituzione 1985, dipendenti, fatturato). Non sono in pagina. Prima di scrivere "dal 1985" serve la visura.
- **Etichette non adesive, scatole e cartellini** (dal certificato FSC). In pagina ci sono solo come "etichette non adesive" nel piede e nella scheda Alimentare (sottobusta).
- **Pagina dei cookie.** Il sito di oggi la tiene come ancora `termini-duso-e-informative/#cookie`; la privacy ha una pagina sua. Nel sito nuovo conviene dare anche ai cookie una pagina propria.

## Foto da rifare dal vero (oggi sono segnaposto; in pagina c'è una sola riga "Le immagini della pagina sono indicative")

1. **Apertura, l'etichetta in lamina oro.** È la foto più importante. Oggi è un fotomontaggio (lamina oro vera di Katie Harp su Unsplash, logo dell'azienda, ricciolo e ombre calcolati con `etichetta_oro.py`). Lo scatto vero: una loro etichetta autoadesiva in lamina oro stampata in cold foil, formato circa 12x8 cm con gli angoli arrotondati, con il logo in blu #233588, appoggiata su un cartoncino opaco color carta (#F3F1EC o il più vicino) con l'angolo in basso a sinistra sollevato di 2-3 cm, come nel logo, così che si veda il retro bianco con l'adesivo. Va stampata apposta: è il biglietto da visita del cold foil. Ripresa dall'alto con un'inclinazione di 10-15 gradi, ottica macro o 90-100 mm, diaframma f/11. Luce: un bank grande da sinistra in alto e un pannello bianco a destra, più una striscia di luce radente che accenda la lamina in diagonale. Formato orizzontale 3:2, almeno 5000 px, con l'etichetta che occupa due terzi della larghezza e carta libera attorno per l'ombra. Si scontorna sul colore della pagina.
2. **Le quattro schede**, tutte dallo stesso piano chiaro color carta, con la stessa luce morbida da sinistra, riprese dall'alto e tagliate orizzontali 2,25:1 (lasciare aria per un taglio 4:3 al telefono):
   - Alimentare: due o tre vasetti o vaschette con una loro etichetta vera (oggi sono due vasetti di marmellata di Maram con le scritte a mano tolte);
   - Cosmesi e chimico: un flacone con l'etichetta a coupon e un dettaglio in lamina a luce radente (oggi bottiglia e flaconcini di Leeloo The First con le scritte tolte);
   - Sicurezza: una striscia di etichette bar code, RFID o antitaccheggio con la numerazione progressiva leggibile (oggi la striscia di Anna Shvets, con il fondo rosa portato al bianco);
   - Multipagina: un'etichetta a libretto aperta a ventaglio su un flaconcino, con le pagine stampate. È la più urgente delle quattro: il segnaposto di oggi (flaconcino di Leeloo The First) ha un'etichetta semplice, e un'etichetta a libretto libera e decente negli archivi non esiste.
3. **Reparto.** Mani sul nastro all'uscita della flexo, i cliché, la prestampa. Luce del posto, nessun flash diretto, colori neutri. Prende il posto della foto di Anthony Roberts nei servizi.
4. **Facciata.** In alta risoluzione (almeno 5000 px), con luce di fine giornata radente sulla lastra dorata e cielo pulito, senza i riflessi arancio di oggi sul ricciolo. Inquadratura orizzontale 3:2 con la curva della lastra e il logo in rilievo a destra. Oggi c'è la foto del sito, 1920x720 con il cielo ritoccato: a 1440 su uno schermo ad alta densità resta morbida.

## Licenze

- **Mona Sans** (GitHub), da Google Fonts, SIL Open Font License 1.1. Uso commerciale libero. Il testo della licenza è in `sito/fonts/OFL.txt` e va lasciato accanto ai file.
- **Foto Unsplash** (Katie Harp, Anthony Roberts): Unsplash License, uso libero anche commerciale e modifiche consentite. Non si possono vendere le foto senza modificarle.
- **Foto Pexels** (Maram, Anna Shvets, Leeloo The First): Pexels License, uso libero, attribuzione non obbligatoria, modifiche consentite.
- **Facciata e loghi**: sono dell'azienda, presi dal suo sito.
- Le foto di repertorio del sito di oggi (supermercato, farmacia, enoteca) non si usano: la licenza era dell'agenzia che ha fatto il sito.

## Loghi

- Non esiste un vettoriale pubblico, e nei PDF non c'è. La scritta a pennarello non si ricalca fedele in automatico, quindi non ho fatto un SVG.
- In pagina ci sono `sito/img/logo-blu.png` (blu #233588, in testata) e `sito/img/logo-bianco.png` (nel piede). Sono tutti e due il logo bianco del sito (350x203) ritagliato e ricolorato, serviti a 150 e 156 px, circa 2,2x. Lo stesso logo è stampato nell'etichetta dell'apertura.
- Il riquadro con l'angolo arricciato e il filo arancio #F28C00 non c'è più: l'angolo sollevato ora è quello dell'etichetta oro.
- Va chiesto il vettoriale originale, e se l'arancio fa parte del marchio.

## Pagine del sito nuovo a cui punta la home

I percorsi sono gli stessi del sito di oggi, quindi non servono redirect:

- `azienda/`, `azienda/certificazioni/`
- `prodotti/etichette-settore-alimentare/`, `prodotti/etichette-per-cosmesi-e-settore-chimico/`, `prodotti/etichette-per-la-sicurezza/`, `prodotti/etichette-multipagina/`
- `servizi/prestampa/`, `servizi/assistenza-tecnica/`, `servizi/archivio-file-e-campioni-prodotti/`, `servizi/consegna-rapida/`
- `preventivo/`
- `termini-duso-e-informative/informativa-privacy/`, `termini-duso-e-informative/#cookie`, `informativa-sullaccessibilita/`
- Ancore della home: `#etichette`, `#servizi`, `#certificazioni`, `#contatti`.
- La pagina `contatti/` del sito di oggi resta, ma la home non la cita più: i contatti sono nella chiusura e nella colonna Contatti del piede.

## Newsletter e social

Non ci sono. È un fornitore B2B su commessa, senza notizie, fiere, cataloghi o clienti privati, e non ha profili social: nessun link nel codice e nessun risultato nelle ricerche del 24/10/2026. Se aprissero un profilo, nel piede va aggiunta una colonna "Seguici" con i soli social che esistono.
