# Belletti S.r.l.: proposta di nuova homepage

Proposta non richiesta, solo la home. Azienda: Belletti S.r.l., ascensori, Via della Tecnica 29, Mestrino (PD). Non è stata contattata e non è stato pubblicato niente.

## Dove sta cosa

- `sito/index.html`: la home, statica, che si apre con file:///. `sito/img/` contiene solo le immagini usate (WebP alla misura giusta e il logo SVG), `sito/fonts/` il carattere Radio Canada con la licenza `OFL.txt`.
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` e `NOTA.md` (che cosa è cambiato, i compiti della scheda d'uso, l'esito delle 15 regole del livello professionale, foto, caratteri, controlli).
- `_prova/script/build_finale.sh`: rifà immagini (`pro_img.py`), controlli dei testi, screenshot (`shot_finale.mjs`), regole (`pro_controlli.mjs`, esito in `_prova/pro_controlli.json`) e prova d'uso (`pro_prova.mjs`: menu, ancore, modulo).
- `_prova/versione-1-originale/`: la home di prima ("Il carattere dell'edificio"), con i suoi screenshot e la sua NOTA.
- `_prova/uso/SCHEDA.md`: chi apre il sito e per fare che cosa. `01-analisi.md`: fatti e fonti. `assets/CREDITI.md`: origine delle foto.

## Il modulo di contatto va collegato

Il modulo "Chiedete un sopralluogo o un preventivo" oggi non spedisce niente da solo. Ha cinque campi in vista (nome, telefono, comune e indirizzo dell'impianto, che cosa serve, quando) e le note a scomparsa ("Aggiungete la marca o una nota"). Controlla nome, telefono e comune, poi apre il programma di posta di chi lo compila con un'email già scritta a info@bellettiascensori.it (oggetto "Richiesta: tipo, comune"; nel corpo nome, telefono, indirizzo dell'impianto, tipo di richiesta, urgenza e note). Sopra il bottone un riquadro ricorda di allegare all'email le foto della targa o del vano, perché un mailto non porta allegati. Dopo il clic compare anche il testo pronto con il tasto "Copia il testo" e il numero degli uffici, per chi usa la posta via web e non vede aprirsi niente.
Nel sito vero va collegato a un servizio di invio (il modulo del CMS, oppure un servizio come Formspree o Netlify Forms) con:
- un campo per allegare foto, pianta o sezione: `<input type="file" name="allegati" accept="image/*,.pdf,.dwg" multiple>`, al posto del riquadro "Foto della targa in cabina o del vano";
- una pagina o un messaggio di conferma ("Richiesta ricevuta, vi richiamiamo"), al posto del testo da copiare;
- l'invio a info@ o all'indirizzo dell'ufficio tecnico, se c'è (vedi sotto);
- una risposta automatica con i tempi di risposta, quando Belletti li dà;
- l'informativa privacy e la casella del consenso.

## Da chiedere a Belletti prima di pubblicare

In pagina c'è solo ciò che è nelle fonti; questi punti vanno confermati, o mancano e vanno chiesti.

**Assistenza**
1. Che cosa succede oggi fuori orario per un guasto senza persone dentro. Il depliant del 2008 dice che il call center "prende nota" e la chiamata "verrà evasa alla ripresa del normale orario lavorativo"; in pagina è scritto più piano: "Il call center prende nota e il tecnico interviene alla ripresa del normale orario di lavoro". Vale ancora? Il tecnico arriva il primo giorno lavorativo? Se il guasto è pericoloso (porta di piano aperta, impianto in un ospedale) cosa si fa? E "di norma i guasti si risolvono entro la stessa giornata" è ancora vero?
2. Gli orari degli uffici (049 508 2430): non sono pubblicati, quindi in pagina non ci sono e la colonna del piede si chiama solo "Contatti". Quando arrivano, vanno nei contatti e nel piede come tabella giorni/ore, e la colonna torna "Contatti e orari".
3. La zona: in pagina ci sono le sette province del Veneto (Padova, Venezia, Treviso, Vicenza, Verona, Rovigo, Belluno) e "parte del Friuli", dalla frase del sito "nelle province del Veneto e in parte del Friuli". Servono le province o i comuni del Friuli, e la conferma che tutte e sette le province venete sono coperte. Il Safety Lift Group per il resto d'Italia esiste ancora? Oggi non è in pagina.
4. Se l'ammodernamento si fa anche su impianti installati da altre ditte (in pagina "qualsiasi marca" è detto solo per la manutenzione, come sul sito).
5. Se i tecnici sono ancora "patentati, con abilitazione prefettizia" e "oltre venti" (in pagina "20+").
6. La frequenza della manutenzione preventiva: il sito dice "ogni anno", il depliant "con frequenza variabile". In pagina non c'è.
6a. Come si cambia manutentore: subentro nel contratto, che documenti servono (libretto, verbali delle verifiche), primo sopralluogo, tempi. In pagina c'è solo "Volete cambiare manutentore? Seguiamo impianti di qualsiasi marca: chiedete un preventivo di manutenzione". Con le risposte si fa un blocco di tre righe nella sezione assistenza.
6b. Che cosa si rifà in un ammodernamento (quadro di manovra, porte, cabina, pulsantiere, adeguamento alle norme) e un ammodernamento vero da mostrare, con il luogo e l'anno. Oggi la sezione ha solo la frase e le parole dell'ing. Viel.

**Fiducia**
7. Certificati validi oggi: le copie online di ISO 9001 (DNV, scaduta il 24/10/2021) ed Eurofins Allegato XI (scaduta il 22/12/2024). In pagina ci sono solo le date di prima emissione (1997 e 1999), "qualità certificata dal 1997" e un link per chiedere le copie aggiornate. Con i PDF validi: link per scaricarli e, se lo vogliono, il logo DNV in un colore.
8. "35 dipendenti, molti giovani" viene dall'ing. Viel (La Piazza Web, 2024); il sito dice "trenta addetti". Qual è il numero di oggi?
9. "Quattro generazioni" (La Piazza Web, 2024): chi è la quarta? Il 1908 come anno d'inizio di Rodolfo Belletti (depliant e pagine TOP; il sito dice "nel Novecento").
10. Recensioni: non ne abbiamo trovate (Google Maps non leggibile dal nostro client, Pagine Gialle senza recensioni). Se hanno una scheda Google con recensioni, o lettere di amministratori ed enti da citare con nome e comune, servono per la fascia delle recensioni che i siti di riferimento hanno e questa home no.
11. Clienti da nominare: amministratori di condominio, enti, imprese che accettano di comparire con il nome (oggi in pagina c'è solo il Comune di Padova, dalla Galleria Cavour).
12. La squadra: nomi, ruoli e anni di mestiere di chi risponde al telefono, dei capi tecnici e della famiglia, per la sezione con le persone.
13. La Pallavolo Padova: lo sponsor è ancora attivo? In pagina c'è una riga nel piede, perché ne vanno fieri (la SCHEDA chiede di tenerla); se non è più attivo si toglie.

**Lavori e progettisti**
14. L'anno di fine lavori di Ca' Michiel e di Ca' della Nave (per la Galleria Cavour c'è: ottobre 2007; il redazionale di Ca' Michiel è del 2008, il concorso di Ca' della Nave del 2006, ma nessuno dei due dà la fine lavori), e che tutti e tre si possano nominare con i committenti e i progettisti (Zambusi, Ziffer, Danzi, Rigo, dai redazionali DiBaio). Se l'"ing. A. Viel" dei redazionali è l'AD Andrea Viel: in pagina, tra i progettisti, è scritto "ing. A. Viel" come nei redazionali. Quando arrivano gli anni vanno nella riga del luogo, come per Cavour ("Venezia, 20xx"). I dati dei tre lavori con le pagine dei PDF sono in `01-analisi.md`, sez. 2.
15. Dati tecnici di Legnago (ponte Principe Umberto) e di Cannaregio, con una foto, per farne due schede come le altre.
16. Un indirizzo email per l'ufficio tecnico (oggi i progetti vanno a info@, con l'oggetto "Progetto per l'Ufficio Tecnico").
17. "Assembliamo ascensori e piattaforme di alta qualità con i migliori componenti disponibili sul mercato internazionale" viene dall'articolo del 2024: va bene così? Producono ancora cabine e porte (depliant 2008)?

**Dati societari e social**
18. PEC, capitale sociale versato (167.000 €), se il fax 049 9003778 serve ancora (non è in pagina).
19. La pagina Facebook è attiva? Oggi in pagina c'è solo YouTube.
20. Il file ufficiale del marchio (al logo vettoriale del depliant manca la "®").

## Foto da rifare dal vero, o da chiedere in originale

Tutte le foto in pagina sono di Belletti: depliant del 2008, gallerie del sito, redazionale DiBaio di Ca' della Nave. Nessuna foto di repertorio, nessuna illustrazione. Il fotografo non è indicato: prima di tutto vanno chiesti gli originali e i diritti d'uso (anche all'editore DiBaio). Le foto sono di 347-948 px e in pagina nessuna è mostrata oltre la sua misura, quindi a densità 1x sono nitide e sugli schermi 2x restano morbide.

Se gli originali mancano, servono due giorni di fotografia, un solo fotografo e una sola luce, almeno 4000 px di lato, in RAW:
1. **Apertura, la squadra davanti alla sede**: tre o quattro tecnici in divisa con il logo, davanti a due furgoni bianchi e verdi, sotto la pensilina di Via della Tecnica 29, al crepuscolo come la foto del 2008. Un verticale 4:5 per il computer e un orizzontale largo per il telefono. Targhe coperte.
2. **Assistenza**: un tecnico al quadro di manovra in un locale macchine e uno sul tetto di cabina, le mani al lavoro, il marchio sulla divisa; il furgone parcheggiato davanti a un condominio.
3. **Chi risponde al telefono**: il call center o l'ufficio assistenza, con la persona che risponde (ritratto, guarda in camera). Oggi in "Chi siamo" c'è l'ufficio tecnico del depliant 2008 (`d-043`, 633x318, mostrato a 424 px): va rifatto o chiesto in originale, con i nomi.
4. **Ammodernamento**: un prima e dopo vero di un ascensore degli anni '60-'70 in un condominio padovano (pulsantiera, cabina, porte di piano).
5. **Piattaforme e servoscala**: una piattaforma installata in una casa, con una persona anziana che la usa (con il suo consenso).
6. **Lavori**: Galleria Cavour di giorno e di sera dalla piazza; Ca' Michiel dal cortile con le verticali dritte; Ca' della Nave dalla corte di mattina, senza le panchine; Legnago dal fiume.
7. **Impianti nuovi**: una cabina finita in officina e le sei famiglie (ascensore, panoramico, montacarichi, montauto, piattaforma, scale mobili) con lo stesso taglio 4:3 e la stessa luce, per le schede. Oggi tre schede vengono dal depliant 2008 (ascensori `d-026`, panoramici `d-002`, montauto `d-030`) e tre dalle gallerie del sito a 335-500 px (montacarichi `fn000053`, piattaforma `fn000257`, scala mobile `fn000171`), tagliate strette e con il bianco corretto in `pro_img.py`: sono le più deboli e vanno rifatte per prime.
8. **La famiglia**: ritratti di Gaetano e Irma Belletti e dell'ing. Viel; i ritratti seppia (`assets/originali/sito/storia1-4.jpg`) in originale, con i nomi.

## Licenze

- **Carattere**: Radio Canada, Google Fonts, SIL Open Font License 1.1, uso commerciale libero; servito dalla pagina in `sito/fonts/`, licenza in `sito/fonts/OFL.txt`.
- **Foto**: di Belletti, con i diritti da confermare (sopra). Le foto di repertorio scaricate per i prototipi in `assets/esterne/` (licenze in `assets/CREDITI.md`) non sono nella home.
- **Logo**: vettoriale vero, estratto dai tracciati della pagina 28 del depliant del 2008 (`assets/originali/logo-belletti-depliant.svg`, script `_prova/script/logo_svg.py`).

## Link della pagina

- Menu e piede portano alle sezioni della home (`#assistenza`, `#ammodernamento`, `#impianti`, `#lavori`, `#storia`, `#contatti`, `#qualita`); le schede degli impianti e i bottoni "sopralluogo" e "preventivo" aprono il modulo (`#richiesta`) con il tipo già scelto.
- Privacy e Cookie puntano a `privacy/` e `cookie/` del sito nuovo (oggi c'è il PDF `Privacy.pdf`). Aperti da file:// non portano a niente: le due pagine vanno create nel sito vero prima di pubblicare.
- Fuori dal sito: Google Maps (indicazioni e mappa per Via della Tecnica 29, Mestrino), YouTube https://www.youtube.com/@BellettiAscensori.

## Newsletter

Non c'è, e non avrebbe senso: la pagina News è vuota da anni, non ci sono fiere né cataloghi nuovi e i clienti cercano un numero di telefono, non aggiornamenti.
