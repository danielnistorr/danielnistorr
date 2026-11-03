# Recinzioni Formentin: proposta di nuova homepage

Proposta non richiesta di nuova home per Formentin Srl (insegna Recinzioni Formentin), via Lombardia 17, Villatora di Saonara (PD). Solo la home; nessun contatto con l'azienda, nessun modulo inviato, nessuna pubblicazione.

## Dove sono le cose

- `sito/index.html`: la home ibrida del 3/11/2026 ("Produciamo e montiamo"), statica (si apre con file:///). `sito/img/`: 7 foto loro in WebP (la macro della rete in 8:9, i lavori in 4:3, la rete del culmine in 3:2, da 400 a 800 px) e `marchio.svg`. `sito/fonts/`: Big Shoulders Display e Public Sans con le licenze.
- `_prova/versione-pro/`: la home professionale di prima (pagina, immagini, Geologica, screenshot), com'era. `_prova/alto/`: direzione (`DIREZIONE.md`), provini, script delle immagini e degli screenshot, misure della sezione D (`misura-d.mjs`).
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `home-1024-prima-schermata.jpg`, `home-768-prima-schermata.jpg`, `chiusura-1440.jpg` e `NOTA.md` (in testa il metodo ibrido con le misure; sotto la nota della versione professionale).
- `_prova/script/build_finale.sh`: rifà immagini (`pro_img.py`), pagina (copia `index.sorgente.html` in `sito/`), screenshot (`pro_shots.mjs`, `pro_shots.py`) e controlli (`pro_controlli.mjs`, esito in `_prova/pro_controlli.json`). `pro_misura.mjs`: misure rapide di testata e scorrimento a 12 larghezze. `largo.mjs`: elementi che escono dalla larghezza.
- `_prova/versione-1-originale/`: la home di prima ("La rete ondulata la facciamo noi"), pagina, immagini e screenshot, com'era.
- `_prova/uso/SCHEDA.md`: chi apre il sito e che cosa ci viene a fare. `01-analisi.md`: fatti con le fonti. `assets/CREDITI.md`: origine e licenza di ogni immagine.

## Da chiedere all'azienda prima di pubblicare

In pagina ci sono solo fatti del sito di oggi e di atoka (citati in `01-analisi.md`). Da confermare o da avere:

1. **Orari**: lun-ven 8.00-12.00 e 13.30-17.30, sabato su appuntamento (dal sito); le directory dicono altro (8.00-12.15; 8-12 e 13-17). Valgono per il banco e per l'esposizione? Chiusure estive, ponti e festa del patrono di Saonara: lo stato "Aperto ora" conosce i festivi nazionali e Pasquetta; le altre date vanno nell'elenco `CHIUSURE` dello script in fondo alla pagina (dal primo all'ultimo giorno chiuso), oggi vuoto.
2. **Come funziona il preventivo**: i tre passi in pagina ("Mandateci foto e misure", "Vi richiamiamo" e fissiamo l'appuntamento in sede, "Vedete i modelli, avete il preventivo": in sede vi diamo il preventivo, gratuito) e la riga che compare fuori orario ("Fuori orario: mandateci foto e misure, vi richiamiamo noi.") vanno fatti leggere al titolare: le recensioni negative raccontano proprio questo passaggio. Se accettano foto e misure su WhatsApp al 335 7740278, si aggiunge un bottone. Se l'esposizione si visita senza appuntamento nei giorni feriali, si cambia "su appuntamento".
3. **Zona servita per la posa**: l'elenco dei comuni (regole 14 e 15 dei riferimenti). Oggi in pagina non c'è nessuna zona.
4. **Recensioni**: le frasi trovate ("competenza, disponibilità, consigli anche disinteressati", giugno 2022) vengono da copie delle recensioni Google su altri siti. Vanno rilette su Google Maps e messe in pagina con il nome e il comune solo con il loro consenso; con il voto e il numero di recensioni farebbero la terza prova che manca (regola 10).
5. **Lavori con un nome**: per i tre lavori in pagina (`canc082202`, `canc082201`, `ringh082202`; `ringh082203` è uscito con il ritocco del 3/11) e per il cancello del campo sportivo nella sezione Aziende (`gallery_cancelli_img_1114.jpg`) il comune, l'anno, se la posa è stata loro e due dati (metri, altezza, modello); e il permesso dei clienti a mostrare le case. Con questi la regola 11 passa, e si possono rimettere "recenti" e "posati" nel titolo della sezione (oggi "Alcuni nostri lavori").
6. **Clienti e lavori per aziende**: aziende, condomini, impianti sportivi o comuni per cui hanno lavorato, da nominare se loro e i clienti sono d'accordo.
7. **Betafence**: che siano ancora rivenditori e installatori ufficiali; che Securifor, Nylofor, Decofor e i cancelli in kit EN 13241-1 siano ancora a listino; se ForFence è un loro sistema o di un fornitore (per ora è solo tra i sistemi, non nella fascia "Marchi e norme"). Un logo ufficiale Betafence in un solo colore per la fascia, se il marchio lo consente.
8. **Il banco di attrezzature edili**: che sia ancora attivo e con quali categorie; se carpenteria e grigliati elettrosaldati si fanno ancora.
9. **Dati legali**: P.IVA 00074590282 (da atoka, il sito di oggi non la mostra), REA, PEC, sede legale (via Andorra 11 a Padova su atoka, o già via Lombardia 17). In pagina oggi non c'è nessuno di questi dati: la P.IVA è stata tolta dal piede finché non la confermano (al suo posto c'è un commento HTML).
10. **L'anno**: "primi anni Settanta" (pagina Azienda) contro i "32 anni" di atoka; un anno preciso e il nome del fondatore renderebbero "50+" un fatto datato. Il nome del titolare (un "Andrea" compare nei riassunti delle recensioni: non usato).
11. **Squadra**: chi fa la posa e chi risponde al telefono, con nome e anni di mestiere, se vogliono comparire (sezione "squadra" dei riferimenti, oggi assente).
12. **Social**: nessun profilo trovato; se ci sono, una riga nel piede.
13. **Numeri veri per la fascia dei numeri** (regola 10, ne servono almeno 4): metri quadri dell'esposizione, modelli esposti, recinzioni o metri posati in un anno o in totale, comuni serviti, anno di fondazione preciso. Oggi in pagina c'è solo "50+ anni": i conteggi di prima ("4 materiali", "3 usi", "3,0 m") sono stati tolti perché sembravano riempitivi. La fascia si rimette quando ce ne sono quattro.
14. **Tempi di risposta**: entro quanti giorni richiamano dopo una richiesta (Wilson scrive "entro 48 ore" accanto al modulo). Non è scritto in pagina finché non lo dicono loro.
15. **Cellulare ai privati**: il 335 7740278 è sul sito di oggi; nella home ibrida compare una volta sola, in "Orari e strada". Da togliere se il titolare preferisce che i privati chiamino il fisso.
16. **La rete ondulata e le colonne**: la frase della home, "Produciamo e montiamo", e il culmine dicono che le reti ondulate e le colonne le producono loro (pagine Reti ondulate e Colonne del sito di oggi). Le foto della macchina sono del 2014, prima del trasloco: va confermato che la macchina c'è ancora e dove lavora, e se si possono scrivere "fatte a Villatora". Se la rete non si produce più, frase e culmine vanno cambiati. Da confermare anche le maglie in tabella (10 x 10 filo 2 ... 40 x 40 filo 4).
17. **Esposizione su appuntamento**: il bottone "Chiedi l'appuntamento" prepara un'email con giorni e orari preferiti. Se preferiscono il telefono, diventa un `tel:`.

## Il modulo di contatto

Nella home ibrida il modulo non c'è più: rifaceva con un'email lo stesso lavoro del bottone "Manda foto e misure". Restano tre email già scritte, con oggetto e traccia: "Preventivo recinzione" (apertura e preventivo), "Appuntamento per l'esposizione" e "Richiesta per azienda o impianto sportivo". Quello che segue vale per la versione professionale (`_prova/versione-pro/`).

Il modulo in home ("Richiesta di preventivo") **compone un'email** (`mailto:` a info@recinzioniformentin.it con oggetto "Preventivo: <tipo di lavoro>" e nel testo nome, telefono, email, tipo, indirizzo, metri, altezza, cancelli, urgenza, giorni preferiti per l'appuntamento, descrizione e se le foto sono allegate) e la apre nel programma di posta di chi scrive; le foto si allegano lì. Nel sito vero va **collegato a un servizio di invio** (per esempio il modulo del CMS con allegati, o un servizio come Formspree o Netlify Forms) con: allegati per le foto e i disegni (JPEG, PDF, DWG), una casella del consenso privacy, un filtro anti-spam e la risposta automatica con i tempi che l'azienda può promettere. Anche i bottoni "Manda foto e misure" e "Manda il disegno" sono `mailto:` con la traccia: possono restare.

## Foto da fare dal vero

Le foto in pagina sono loro ma piccole (800 px), fatte col telefono in giorni e luci diverse, e quelle del negozio sono del 2014-2015, cioè probabilmente della sede di prima del trasloco (via Andorra): per questo non sono nella sezione "Dove siamo". Una giornata di scatti, mirrorless o reflex da 24 MP in su, luce del mattino o cielo coperto chiaro, niente HDR, stessa luce e stesso taglio per tutta la serie (4:3 orizzontale, più qualche verticale per il telefono):

1. **Apertura**: il titolare o la squadra davanti a una recinzione appena posata o al furgone con il logo, in via Lombardia; in alternativa un cancello scorrevole antracite frontale, come un prospetto, alla luce del mattino, in orizzontale largo (16:10, almeno 2000 px). Con le persone la regola 3 passa senza riserva. Oggi l'apertura è `canc082204` ritagliata in 16:10 per togliere il piazzale: regge, ma resta uno scatto da telefono.
2. **La sede di via Lombardia 17**: la facciata con l'insegna da strada (aiuta chi arriva) e l'ingresso del negozio.
3. **L'esposizione**: i modelli in fila, vuota e ordinata, luce laterale.
4. **Il banco**: il bancone con una persona dietro, gli scaffali di chiodi, casseri, rete e pali.
5. **La posa**: le mani del loro personale che fissano un pannello alla piantana o montano un cancello.
6. **Lavori**: quattro-sei lavori recenti a piena risoluzione (almeno 1600 px di lato), con comune e anno, per privati e almeno uno per un'azienda o un impianto sportivo, tutti con la stessa luce: oggi due sono al crepuscolo e due di giorno, e la serie non è ancora una serie (regola 5).

## Pagine a cui puntano i link

I link della testata e delle schede portano alle sezioni della home o al modulo. Nel sito vero servono anche, con redirect 301 dagli indirizzi di oggi (che hanno `/index.php/` dentro, elenco in `01-analisi.md` sez. 8): le pagine prodotto (recinzioni in alluminio, cancelli, ringhiere e inferriate, rete metallica e pali, Betafence, grigliati, tettoie), Attrezzature edili, Contatti (oggi 404), `/privacy/` e `/cookie/` (oggi mancano: i link del piede puntano lì).

## Licenze

- **Caratteri**: Big Shoulders Display 700 (The Big Shoulders Project Authors) e Public Sans 400 e 600 (The Public Sans Project Authors), tutte e due SIL Open Font License 1.1 (uso commerciale libero), file di `@fontsource` 5.1.0 serviti da `sito/fonts/` con le licenze `OFL-big-shoulders-display.txt` e `OFL-public-sans.txt`. Geologica è uscita (resta in `_prova/versione-pro/`).
- **Foto**: solo foto del loro sito (elenco in `assets/CREDITI.md` e nella NOTA); l'uso va confermato con l'azienda e, per le case riconoscibili, con i clienti. Nessuna foto di repertorio in pagina: le foto Unsplash e Pexels di `assets/esterne/` non sono più usate.

## Logo

Non esiste un vettoriale pubblico: la versione migliore è `logoOmbra.gif` 740x744 (`assets/originali/logo-ombra-740x744.gif`). In pagina c'è un ridisegno in SVG fedele a forma e colori (rete a rombo azzurra #5A94F7, F verde #08B508), senza l'ombra e con il numero di maglie stimato; accanto, il nome "Recinzioni Formentin" composto in Public Sans 600, senza ridisegnare il logotipo di oggi. Va chiesto il vettoriale originale con i colori ufficiali.
