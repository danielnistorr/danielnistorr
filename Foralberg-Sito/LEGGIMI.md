# Foralberg: proposta di nuova homepage

Proposta non richiesta, solo la home. Nulla è stato inviato all'azienda né pubblicato.

## Dove sono le cose

- `sito/index.html`: la home finale (livello professionale con il ritocco finale, 3 novembre 2026), statica, si apre con file:///. Immagini in `sito/img/` (furgone e stand della 38a Fiera, archivio Foralberg, in JPEG a quattro larghezze; logo orizzontale e monogramma in SVG), caratteri in `sito/fonts/` (Newsreader per titoli e cifre, `OFL-Newsreader.txt`; Schibsted Grotesk per testo e interfaccia, `OFL.txt`; tutti e due Google Fonts, SIL Open Font License 1.1).
- `screenshot/home/`: home-1440.jpg, home-1440-prima-schermata.jpg, home-390.jpg, home-390-prima-schermata.jpg, chiusura-1440.jpg e `NOTA.md` (sezione "Ritocco finale": cosa è cambiato, esito delle 15 regole, prove d'uso; sotto, il passaggio precedente e la versione 1 originale). Prova del modulo: `node _prova/script/ritocco_modulo.mjs <percorso>/sito/index.html <cartella>`.
- `_prova/script/build_finale.sh`: rifà immagini (`pro_img.py`), pagina (da `index.sorgente.html`), screenshot (`pro_shots.mjs`, ora simulata martedì 3 novembre 2026 alle 10.00) e controlli (`pro_controlli.mjs`, esito in `_prova/pro_controlli.json`). Per vedere la pagina a un'altra ora: `index.html?ora=2026-11-07T10:00`.
- `_prova/versione-1-originale/`: la home "Firmato Foralberg" com'era prima di questo passaggio (sito e screenshot).
- `_prova/uso/SCHEDA.md`: chi apre il sito, che cosa viene a fare, prove per il collaudo.
- `_prova/crawl/catalogo-2026-testo.txt`: testo del Catalogo 2026/2027 (516 pagine), da cui vengono l'indice dei capitoli con le pagine, i criteri del progetto (p. 5) e la personalizzazione dei piatti (p. 103). Il PDF da 56 MB non è conservato.
- `01-analisi.md`: fatti con le fonti, voti delle foto, riferimenti. `assets/CREDITI.md`: provenienza delle immagini.

## Il modulo di richiesta va collegato a un servizio

In home c'è il modulo "Chiedete un preventivo" (tipo di richiesta, settore, area, nome, locale, telefono, email, messaggio, allegato; con "Progetto o impianto" anche spazio, pasti e tipologia di cucina). **Oggi non invia nulla da solo**: compone un'email a servizioclienti@foralberg.it con oggetto ("Richiesta: Preventivo, Albergo, Hotel..., Nome") e tutti i campi, che il visitatore invia dal suo programma di posta. Un'email aperta da un link non può portare allegati: sul telefono che lo permette si apre la condivisione con il file, altrimenti la pagina dice di allegarlo nella posta. Con la webmail o senza un programma di posta non si apre nulla: per questo, dopo il clic, la pagina mostra il testo della richiesta da copiare ("Copia il testo", "Copia l'indirizzo email") e il numero del servizio clienti, e non dice più che l'email è partita. Finché non è collegato a un servizio, chi manda una planimetria deve allegarla a mano: è il primo lavoro da fare.
- Da collegare a un servizio che riceva anche i file (per esempio il modulo del sito nuovo su WordPress con Contact Form 7 o WPForms, oppure Formspree, Basin o simili), con l'invio a servizioclienti@foralberg.it e una conferma a chi scrive.
- Quando il servizio c'è: togliere il testo da copiare e la frase sulla posta, e mostrare la conferma solo dopo la risposta del server ("Ricevuto, vi richiamiamo entro...").
- Va scritto con l'azienda il testo dell'informativa privacy accanto al pulsante (oggi c'è solo la frase su come si apre l'email) e deciso il tempo di risposta da promettere (oggi nessuna promessa in pagina).
- La newsletter della versione 1 è stata tolta: non inviava nulla. Se l'azienda la vuole (la privacy di oggi prevede la mailing list), si rimette nel piede dopo averla collegata a Brevo, Mailchimp o al servizio che già usano.

## Da chiedere o confermare con l'azienda (in pagina non c'è nulla di dubbio)

- **Recensioni**: le recensioni Google non si leggono da qui; su Cylex e Italiarecensioni ci sono recensioni aggregate di La Vetrinetta (4,48 su 52 a Cylex), su Facebook 6 recensioni da snippet. Per la regola delle prove servono 3-4 recensioni vere con nome, comune e fonte, con il permesso di pubblicarle (meglio di alberghi e ristoranti).
- **Clienti e lavori con il nome**: alberghi, ristoranti o enti arredati o forniti, con il permesso; per ogni lavoro luogo, anno e due o tre dati (coperti, metri della cucina, pezzi forniti) e una foto. Oggi in pagina ci sono solo le forniture storiche (Venezia 1959, Costa Smeralda 1960) senza nomi.
- **Marche per area**: in pagina le marche sono assegnate alle aree dove compaiono nel catalogo (Steelite, RAK, Revol e BIT nella porcellana e nella posateria, Rona nel vetro e nel bar, Revol in sala, melamina e gastronorm) o dove le descrive la pagina Marchi trattati (Wüsthof, Berto's). Cambro non ha descrizione sul sito di oggi: in pagina c'è solo il nome, senza area; dire in quale area va (per esempio Gastronorm e trasporto pasti) e con quale descrizione. RAK è descritta solo come "Porcellana" (capitolo del catalogo). Confermare l'elenco e quali marche vogliono in evidenza; il senso di "Rivenditore esclusivo per" Rosenthal, Villeroy & Boch e WMF (piede di La Vetrinetta) prima di scriverlo.
- **Novità da mettere in home**: le linee che spingono su LinkedIn (Rona Tribute, i piatti Asteria & Nyx, Steelite "garanzia a vita contro le sbeccature"): di quale marca è Asteria & Nyx, in quale area va e se vogliono una riga "Nuovo catalogo 2026/2027" come novità di stagione (famiglia B, punto 6).
- **Cifre**: "6 portali e albi della PA" è il conteggio dell'elenco in pagina (MePA, SINTEL, SATER, Bandi Alto Adige, SIT Belluno, Albo di Peschiera del Garda): confermare che l'elenco è completo e aggiornato.
- **Impianti**: "tra i marchi degli impianti, Berto's" (Berto's è sulla pagina Marchi come "Cucine e impianti per la ristorazione"); confermare che i progetti di cucina si fanno con Berto's ed eventuali altri marchi; se esiste un PDF pubblico del catalogo "Impianti e cucine professionali", il link va nella scheda Impianti.
- **Monouso e sanificazione**: in pagina c'è solo "articoli monouso di produzione italiana ed estera" (pagina Company); la linea "Ecoline" e la sanificazione non sono nel catalogo 2026/2027: se sono un'area vera, serve la riga e il catalogo.
- **Orari**: chiusure estive e natalizie, festa del patrono (13 giugno, Sant'Antonio) e se lo showroom riceve su appuntamento anche fuori orario. Oggi lo stato considera chiusi solo i festivi nazionali e Pasquetta.
- **La Vetrinetta**: che "aperto anche il sabato" e la lista nozze (matrimonio.com) siano da dire in home; che lavetrinetta@foralberg.it sia l'indirizzo giusto per la lista nozze; "dal 1976" (matrimonio.com) non è in pagina finché non lo confermano.
- **Numeri**: "11 agenti e commerciali" e "oltre 30 collaboratori" (sito) contro 25 collaboratori e 8 agenti (LinkedIn) e 27 dipendenti (Atoka): in pagina c'è solo 11 agenti e commerciali, da confermare; "più di 6.000 in pronta consegna" e "oltre 30.000 articoli" dal catalogo.
- **Storia**: anno della 36a Fiera (1953 sul sito, 1958 nel catalogo), anno e sede del furgone (timeline 1963, cassone "via Trieste 11", sede in via San Fermo dal 1962), grafia di Guerino o Guerrino Desiderio (in pagina c'è solo "la famiglia Desiderio"), HospitalityRiva 2026 (dalla pagina LinkedIn) come voce della riga del tempo.
- **Diritti delle foto d'archivio** ("Foto Giordani"): permesso d'uso e originali a piena risoluzione; anche foto della sede del 1980 e dello showroom del 2008, se esistono.
- **Indirizzi**: ldesiderio@foralberg.it come contatto pubblico per vendite e showroom (ricostruito dal codice della pagina Contatti); l'Ufficio di Rappresentanza a Venezia (non in pagina: indirizzo e ruolo da chiedere).
- **Social**: LinkedIn (it.linkedin.com/company/foralberg-s-r-l) è nel piede; un profilo Instagram citato nei post e il Facebook facebook.com/foralberg.it non sono verificati: se li confermano si aggiungono con il sottotitolo.
- **Riga legale**: REA, PEC e capitale sociale (520.000 euro solo da Atoka) non messi finché non li confermano. Le Note legali di oggi citano due volte "Selco" (modello copiato): da correggere.
- **Link al catalogo**: `#page=N` apre la pagina N del PDF; le pagine dell'indice di p. 7 coincidono con quelle del PDF (controllato sul testo: a ogni numero si apre il capitolo, con la sua pagina d'apertura o la prima pagina di prodotti). Se il PDF viene sostituito, i numeri vanno ricontrollati. Meglio ancora: un PDF per capitolo o un catalogo sfogliabile, perché 56 MB sul telefono sono troppi.
- **Logo**: file originale vettoriale (la distanza tra monogramma e firma nella versione orizzontale è rimisurata a occhio sul JPEG) e il blu ufficiale (#0082B9 dalla copertina, in pagina scurito a #00699A per il contrasto del testo bianco).

## Foto da fare dal vero

La home oggi ha due sole foto, tutte e due d'archivio. Per decisione del committente non ci sono foto di repertorio né disegni: le schede dei prodotti sono tipografiche finché non ci sono foto vere. Quello che serve, in ordine di importanza:
- **Lo showroom di via Cile**, in largo, ripreso frontale come gli stand degli anni Sessanta (la stessa inquadratura con l'insegna), luce del giorno o luce dello showroom bilanciata: va nella scheda "Per i professionisti" e, se forte, accanto al titolo al posto del furgone (che passa in "Chi siamo").
- **Le persone**: il servizio clienti al telefono, un agente con un cliente al banco, il progettista sul disegno; guardano il lavoro, non l'obiettivo. Più un ritratto della famiglia Desiderio per "Chi siamo".
- **Una foto per area**, stessa serie per tutte (stesso fotografo, stessa luce naturale laterale, stesso fondo bianco neutro, formato 4:3 orizzontale, oggetto centrato con aria intorno): una tavola apparecchiata (porcellana, posate, calici), il banco bar con coppe e shaker, un buffet allestito, il pentolame in cucina, le vaschette gastronorm, una cucina installata. Si passano nello stesso trattamento (`pro_img.py` può fare la versione a colori con luci neutre).
- **Il magazzino** dei 6.000 articoli in pronta consegna e un furgone di oggi con il marchio, se c'è: sono le prove del "pronta consegna in tutta Italia".
- **La facciata di La Vetrinetta** in via Vigonovese 93, per la scheda "Per i privati".
- **Una cucina consegnata**, con il nome del locale e il permesso: è il primo lavoro con il nome.
- L'archivio: scansione di tutte le stampe a 1200 dpi in scala di grigi, senza ritocchi, con il retro (date, timbri) per fissare gli anni.

## Pagine del sito nuovo a cui puntano i link

La home oggi punta solo alle sue sezioni, ai PDF dei cataloghi su foralberg.it, a La Vetrinetta (shop e Facebook), a LinkedIn e alle mappe. Dal piede: `/lavora-con-noi/`, `/privacy/`, `/cookie/`, `/note-legali/` (da creare nel sito nuovo). Pagine proposte: Prodotti per area, Marchi con le schede, Progetti e impianti, Personalizzazione, Acquisti PA, Chi siamo e storia, Showroom e dove siamo, Lavora con noi, Contatti; La Vetrinetta resta il sito esterno per i privati.

## Licenze e loghi

- Foto d'archivio (furgone OM Lupetto 30, stand alla 38a Fiera di Padova, "Foto Giordani"): proprietà Foralberg; diritti da chiedere prima di qualsiasi pubblicazione.
- Nessuna foto di repertorio in pagina: le Pexels della versione 1 sono state tolte (dettagli in `assets/CREDITI.md`).
- Carattere: Schibsted Grotesk, Google Fonts, SIL Open Font License 1.1, servito dalla pagina.
- Logo: tracciati vettoriali estratti dalla copertina del Catalogo 2026/2027 (`_prova/script/logo_svg.py`), ricolorati #1D1D1B; da sostituire con il file originale appena l'azienda lo manda. I marchi dei fornitori dipinti sul furgone (Lagostina, Valsodo, Walküre, Duplex, Miele) fanno parte della foto d'archivio. I nomi dei marchi trattati sono scritti in testo, senza i loro loghi.
