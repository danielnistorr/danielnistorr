# Zeta S.r.l., proposta di nuova homepage: LEGGIMI

Proposta non richiesta di una nuova home per https://www.zetaitaly.com (solo la home). Nessun contatto con l'azienda, niente pubblicato.

## Cosa c'è

- `sito/index.html`: la home, statica (si apre con file:///). `sito/img/`: solo le immagini usate, WebP in due o tre larghezze. `sito/fonts/`: i tre caratteri serviti dalla pagina (General Sans 700, Switzer 400 e 700).
- `screenshot/home/`: screenshot a 1440 e 390 (intera e prima schermata), `chiusura-1440.jpg` (dal preventivo al piede) e `NOTA.md` (livello professionale: cosa è cambiato, esito delle 15 regole, prove d'uso, controlli, caratteri).
- `01-analisi.md`: fatti con le fonti; `_prova/uso/SCHEDA.md`: chi apre il sito e che cosa ci viene a fare; `assets/CREDITI.md`: origine e licenza di ogni immagine.
- `_prova/script/build_finale.sh`: rifà immagini (`pro_img.py`), caratteri, screenshot (`pro_shot.mjs`) e controlli (`pro_controlli.mjs`). La pagina è scritta a mano.
- `_prova/versione-1-originale/`: la home di prima (busta ricostruita, "Trasparente come il vetro"), con i suoi screenshot e la sua nota.

## Come funziona la home

- Le schede dei prodotti, la riga "Anche", il piede e i link della sostenibilità portano alle pagine vere di oggi (`https://www.zetaitaly.com/categoria-prodotto/...`, `/prodotto/...`, `/prodotti/`, `/chi-siamo/`, `/storia/`, `/ecosostenibilita/`, `/pvc-bio-origine-100-vegetale/`, `/contatti/`, `/privacy/`, `/cookies/`; controllati sulla sitemap il 3/11/2026). Nel sito nuovo vanno tenuti gli stessi indirizzi, così non servono redirect. Gli indirizzi sono scritti per intero per la prova; nel sito vero diventano relativi.
- La categoria `/categoria-prodotto/bioplastica/` oggi contiene solo le visiere COVID: non è collegata dalla home. Va riempita o tolta.
- Lo stato "Aperti ora / Chiusi ora" è calcolato nella pagina sull'ora di Padova, con gli orari lunedì-venerdì 8.30-12.30 e 14.00-18.00, i festivi nazionali, Pasquetta e il 13 giugno (Sant'Antonio, patrono di Padova), e si ricalcola ogni minuto e quando si torna sulla pagina. Un pallino verde o ambra lo fa vedere a colpo d'occhio. Le chiusure estive, di Natale e i ponti non sono noti: vanno chiesti e scritti **ogni anno** nell'elenco `CHIUSURE` dello script in fondo alla pagina, come coppie di date comprese (es. `['2026-08-10','2026-08-21']`); in quei giorni la pagina dice "Chiusi per ferie, riapriamo lunedì 24 agosto alle 8.30". Finché l'elenco è vuoto, il sito può dire "Aperti ora" in un giorno di ferie. Per le prove si apre la pagina con `?ora=2026-11-02T10:00`.
- **Il modulo del preventivo va collegato a un servizio.** Oggi non invia nulla: con "Prepara l'email della richiesta" apre il programma di posta con l'email già scritta a info@zetaitaly.com, con l'oggetto "Richiesta di preventivo: articolo, azienda" e tutti i campi. Il disegno o la foto scelti nel campo "Disegno o foto" non partono, e la pagina lo dice sotto il campo: nell'email c'è la riga "Allegato da aggiungere: nome del file", e l'allegato va aggiunto a mano. Dopo il clic compare nella pagina il riquadro "La richiesta è pronta" con lo stesso testo e i bottoni "Copia il testo" e "Copia l'indirizzo", per chi non ha un programma di posta (webmail, PC aziendale). Quando il modulo sarà collegato, il riquadro va sostituito da una pagina o da un messaggio di conferma con il tempo di risposta. Nel sito vero il modulo va collegato al Contact Form 7 che hanno già in `/contatti/`, con il campo file (PDF, DXF, DWG, AI, EPS, JPG, PNG), la casella della privacy e il reCAPTCHA; oppure a un servizio di moduli con allegati. Il collegamento va provato con un invio vero prima di pubblicare.
- "Scriveteci" (a 390, nella prima schermata) apre un'email a info@zetaitaly.com con oggetto "Ordine o file di stampa" e le righe Azienda, Riferimento ordine o articolo, Quantità; sotto c'è l'indirizzo con "Copia l'indirizzo". Il bottone "Copia" usa gli appunti del browser e, se non sono disponibili, un ripiego.
- Newsletter: no. Zeta lavora su commessa per aziende, non ha notizie da mandare; LinkedIn basta.

## Da chiedere all'azienda

In pagina c'è solo quello che ha una fonte in `01-analisi.md` o nella SCHEDA. Mancano, e servono per il livello che il committente vuole (regole 10 e 11):

1. **Clienti con il nome**: tre-sei clienti che si possono citare (legatorie, editori, catene, banche, aziende pet food), con il permesso scritto. Oggi in home ci sono solo i settori.
2. **Tre lavori con un nome**: per ognuno il cliente o il settore, l'anno, l'articolo e due-tre dati (quantità, formato, materiale, stampa), con una foto larga del pezzo finito.
3. **Certificazioni dell'azienda**: la descrizione del sito di oggi dice "Qualità certificata", ma non ci sono certificati dell'azienda. Se esistono (ISO 9001 o altro), i PDF; altrimenti la frase va tolta dal sito vero. OK Compost e ISCC PLUS sono dei materiali (ISCC PLUS del fornitore): in home sono scritti solo come materiali.
4. **Recensioni o parole di clienti**: su Google non ce ne sono raggiungibili. Se qualche cliente accetta, due-tre frasi con nome, azienda e città.
5. **Numeri dell'azienda**: addetti (LinkedIn dice 2-10, un risultato di ricerca 7), metri quadrati, saldatrici ad alta frequenza, pezzi l'anno, paesi in cui vendono. In home oggi ci sono quattro cifre prese dalle fonti (1969; 3 generazioni; 5 materiali; 8 siti nazionali, cioè .com, .co.uk, .fr, .de, .at, .ch, .be, .es) e le date: con i numeri veri due di queste vanno sostituite (per esempio addetti e paesi).
6. **Tempi di risposta al preventivo** e **quantità minime** per famiglia (in pagina non c'è nessuna promessa sui tempi). Chi confronta tre fornitori con una scadenza sceglie anche da questo: appena Zeta li dà, vanno nel passo 3 "Vi ricontattiamo" ("rispondiamo entro N giorni lavorativi") e accanto al modulo. Anche: come mandare i file pesanti (WeTransfer, Drive, un limite in MB), da scrivere sotto "Scriveteci".
7. **Chiusure estive, di Natale e ponti** (da scrivere nell'elenco `CHIUSURE`, vedi sopra) e se a mezzogiorno qualcuno risponde comunque al telefono.
8. **Ingresso e consegne**: da dove si entra in Viale della Navigazione Interna 55, dove scaricano i corrieri, orari di ricevimento merci se diversi da quelli d'ufficio.

### Dati da confermare

1. **Le persone nelle foto del 2023**: chi è l'uomo al tavolo (apertura) e se è Gavriel Sacerdoti; chi è l'operatore alla linea (Azienda). Il permesso di mostrarli. In pagina non c'è nessun nome sotto le foto.
2. **Le foto dei prodotti**: che le otto foto della serie 2019 siano delle famiglie in cui sono messe. Da confermare soprattutto i due salva taschino per camice (`2019_12_portapenne-salva-camice-medico.jpg`, messi in "Articoli medicali": la farfalla grigia stampata è un disegno generico o il marchio di un cliente? se è un marchio serve il permesso o un'altra foto), la vaschetta termoformata (in "Custodie e accessori", come cartella per campionari), la copertina trasparente aperta (in "Copertine e sovraccoperte") e le custodie azzurre "Ambulatorio veterinario" (in "Pet food e veterinari"). Le scritte piccole su raccoglitore blu e portadocumenti non si leggono; confermare che non sono di clienti.
3. **Date e storia**: la Zeta esisteva prima del 1969 (LinkedIn dice 1967); il brevetto del 1994 (numero, se è ancora valido); se la linea automatica delle cartelle con molla del 1986 è ancora in uso.
4. **Macchine e produzione**: i robot che sigillano nelle buste i cartoncini delle tipografie (in home, dal loro testo di Chi siamo), le valve termoformate per i blister.
5. **Materiali sostenibili**: l'anno del PVC di origine vegetale; OK Compost dal 2019 (in home nella fascia "Materiali certificati", con ISCC PLUS scritto come certificato del fornitore, numero ISCC-PLUS-Cert-ES226-20230004: confermare che è ancora valido); i pannelli fotovoltaici del 2022 ("sui tetti dei propri stabilimenti": in home "sui nostri tetti"; quanti stabilimenti sono).
6. **Settori**: se pet food e medicale restano in home; se le visiere COVID escono dal catalogo.
7. **Dati societari**: REA e PEC non trovati (il piede mostra ragione sociale, P.IVA e C.F., Registro Imprese, capitale sociale); il codice ATECO dei database (20.10.00) non corrisponde al mestiere; se il fax 049 8070219 è ancora attivo (in home non c'è); correggere l'email sbagliata "info@www.zetaitaly.com" nella pagina Chi siamo di oggi.
8. **Lingue** del sito nuovo (in home: italiano e i domini .co.uk, .fr, .de, .es; .at, .ch, .be da decidere) e l'errore di oggi (schede in francese nella home italiana).

## Foto da fare dal vero

In home ci sono solo foto loro: la serie dei prodotti del 2019 (fondo grigio scuro, tagliate 3:2) e due foto del servizio 2023, ognuna nel suo formato (il tavolo intero a 2,4:1, la linea a 3:2 larga al massimo 560 px). Reggono alla misura a cui sono messe, non di più. Per il sito vero:

- **Gli originali del servizio 2023**: chi l'ha fatto, i diritti e i file in alta risoluzione. In rete ci sono solo il tavolo a 1200x500 e la linea a 1024x683, più miniature da 200 px di saldatrici, bobine e controllo. Con gli originali l'apertura può crescere (anche a tutta larghezza) e si fa una serie "reparto" di 4-6 scatti: saldatrice ad alta frequenza con le mani, controllo al tavolo, bobine, robot che sigilla i cartoncini.
- **Custodia per vinile**: la scheda "Custodie e accessori" mostra ancora la vaschetta termoformata, perché l'unica foto loro di una custodia per LP è su fondo bianco con la copertina riconoscibile di un disco. Serve una custodia per vinile sullo stesso fondo grigio scuro, con un disco senza etichetta o una copertina neutra: è una ricerca frequente e potrebbe avere una scheda sua.
- **Prodotti, stessa serie per tutte le famiglie**: mezza giornata di still life. Stesso fondo (il grigio scuro del 2019 va bene e si accorda con il blocco scuro della pagina), stessa luce morbida da un lato, stessa inquadratura dall'alto a tre quarti, formato 4:3, almeno 2000 px. Un pezzo per famiglia, senza marchi di clienti: raccoglitore, busta a perforazione universale, cartellina con molla, copertina per dizionario, portadocumenti auto, custodia per vinile (senza copertina di un disco riconoscibile), porta libretto veterinario, articolo medicale, album o albumino, portaprezzi.
- **Saldatura in macro**: il bordo saldato di una busta cristal, luce radente, ottica macro.
- **La sede**: l'ingresso di Viale della Navigazione Interna 55 visto dalla strada, utile a chi porta il campione.
- **Lavori con nome** (se il cliente dà il permesso): il pezzo finito con la stampa del cliente, in ambiente.
- Togliere sempre i marchi dei clienti dalle foto, o avere il permesso.

## Licenze

- **Foto**: tutte di Zeta S.r.l. (dal loro sito), usate come materiale loro per la proposta. Nessuna foto di repertorio e nessuna immagine generata dall'IA in pagina. Le dieci foto in `assets/esterne/` (Unsplash e Pexels, licenze in `assets/CREDITI.md`) non sono usate.
- **Caratteri**: General Sans 700 (titoli e cifre), Switzer 400 (testo) e 700 (etichette, bottoni, modulo), Indian Type Foundry, da Fontshare, ITF Free Font License (uso commerciale gratuito, anche web). Per il sito vero vanno scaricati da fontshare.com per il dominio di Zeta.

## Loghi

- In pagina il logo è il PNG con trasparenza del loro sito (`assets/originali/logo-zeta-2268x1098.png`, verde #0A6B42), in WebP a 300 e 600 px. Nel piede, su fondo scuro, lo stesso file è reso bianco dal CSS (`filter`).
- Non esiste un SVG vero: `favicon.svg` contiene solo un PNG, e il vettoriale estratto dalla scheda PDF del 2024 è un ridisegno con angoli arrotondati: non va usato. Da chiedere il file vettoriale originale (AI, EPS o PDF), anche per avere la versione bianca ufficiale.
