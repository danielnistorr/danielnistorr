# Mail di proposta: L'Angelo e il Diavolo

L'Angelo e il Diavolo L'Osteria di Apo Oste in Marostica di Ambrosi Roberto (impresa individuale), Piazza Castello 41/A, 36063 Marostica (VI), P.IVA 02198470243, REA VI-213537.
Mail scritta il 13 ottobre 2026 sul modello di `_metodo/PEC-modello.md`, con le osservazioni riverificate lo stesso giorno sul sito vivo (`_prova/mail-verifica/`). La invia il committente da copiare: da qui non è stato mandato nulla e l'osteria non è stata contattata in nessun modo.
Per L'Angelo e il Diavolo non c'è ancora un sito demo online: la mail allega l'anteprima della pagina iniziale (computer e telefono) e propone di completare il sito. Non va scritto né detto che il sito completo è pronto.

## Destinatario

**Consigliato: robertoapoambrosi@gmail.com**

È l'unico indirizzo che il sito pubblica. Ricontrollato il 13/10/2026 su tutte e cinque le pagine (index, l-angelo-e-il-diavolo, ristorante, contatti, Bando_pr_veneto), con curl e con Chromium: compare solo in `contatti.htm`, sotto "Seguici e prenota il tuo tavolo:", come testo visibile ("Email: robertoapoambrosi@gmail.com") e come link mailto. Nelle altre pagine nessun indirizzo, in nessuna pagina una PEC. Prove: `_prova/mail-verifica/sito/` (codice e `testo-visibile.json`), `contatti-oggi.png`, riepilogo in `_prova/mail-verifica/destinatario.json`.

Dal nome è la casella personale del titolare: per questo la mail si rivolge a una persona sola, **"Gentile Signor Ambrosi,"** con il Lei (non "Gentili Signori" con il Voi). Cortese, mai confidenziale: niente "Apo" nel saluto, anche se è il nome con cui lo conoscono tutti.

Alternative:

- **PEC: langeloeildiavolo@pec.it.** Letta il 13/10/2026 su visurissima.it, pagina dell'impresa con P.IVA 02198470243 ("Sede e Contatti Indirizzo completo PIAZZA CASTELLO 41/A, 36063 MAROSTICA (VI) PEC langeloeildiavolo@pec.it", "Camera Commercio VI · REA: 213537"). Una sola fonte leggibile: reportaziende.it ha risposto 429, ufficiocamerale.it 403 con verifica anti-robot, INI-PEC chiede un captcha (nessun blocco aggirato). Non è sul sito. È il domicilio digitale per le comunicazioni legali, **non un canale per una proposta commerciale**: non usarla per questa mail. Prove: `_prova/mail-verifica/registri/`.
- Telefono 0424 72312, solo per l'eventuale chiamata dopo l'invio (non durante il servizio).

Da non usare:

- **lorenzo.a7788@gmail.com**, pubblicato ancora oggi nella scheda di VisitMarostica ("Tel. 0424 72312, Email: lorenzo.a7788@gmail.com"): non lo pubblica l'osteria e sembra la casella personale di un'altra persona. Prova: `_prova/mail-verifica/visitmarostica/scheda.html`.
- Facebook, Instagram, Tripadvisor: niente proposte via messaggio sui social.

## Oggetto

Nuovo sito per L'Angelo e il Diavolo: anteprima della pagina iniziale in allegato

## Testo

Gentile Signor Ambrosi,

mi chiamo [Nome Cognome] e con [Agenzia] facciamo siti internet. Chi cerca dove mangiare stasera a Marostica vuole sapere se l'osteria è aperta, cosa si mangia e a che numero chiamare. Sul Suo sito si trova a fatica:

- martedì 13 ottobre a mezzogiorno il sito dava aperto dalle 10 alle 15 tranne il lunedì, Google "Chiuso · Apre alle ore 18" e il sito del Comune "chiuso lunedì e martedì a pranzo": a chi credere?
- dal telefono la pagina del computer appare rimpicciolita: per leggere il numero di prenotazione bisogna allargare con le dita;
- non c'è la carta di oggi, e nella galleria c'è ancora l'ingresso di una volta, non la facciata di oggi.

Abbiamo preparato, di nostra iniziativa, la nuova pagina iniziale, partendo dai Suoi testi, rima del lunedì compresa, e dalle foto già pubblicate. Le allego l'anteprima da computer e da telefono, come appare martedì 13 ottobre nel pomeriggio. Non è pubblicata. Se La convince, completeremmo il sito con:

- gli orari giusti e, subito, se oggi l'osteria è aperta;
- la carta, da aggiornare quando cambia;
- il numero da chiamare con un tocco;
- la pagina del contributo regionale, che resta;
- i vecchi collegamenti di Google che funzionano ancora.

Gli orari dell'anteprima sono quelli di Google, non del Suo sito: mi dica quelli giusti. Mi piacerebbe sapere chi c'è oggi in cucina e al banco; poi Le chiederei pizza, piatti, vini, profilo Instagram e il permesso per foto e disegno di Don Backy.

Se Le interessa, passo in Piazza Castello lontano dal servizio e Le mostro tutto in venti minuti, oppure ci sentiamo al telefono quando preferisce. Se invece non Le interessa, basta rispondere a questo messaggio: cancelliamo l'anteprima e non Le scriveremo più.

Cordiali saluti,

[Nome Cognome]
[Agenzia]
[telefono] · [email]

## Allegati

| File | Misure | Peso | Da dove |
|---|---|---|---|
| `AngeloEIlDiavolo-Sito/allegati-mail/angelo-home-computer.jpg` | 1440 x 4056 px, JPEG progressivo, qualità 80, colore 4:4:4 | 830.793 byte (0,79 MB) | stessa cattura di `screenshot/home/home-1440.jpg` (cattura del 13/10 alle 05.32, con l'orologio della pagina messo a martedì 13 ottobre ore 16.30 con `?giorno=2&ora=16:30`: "Stasera aperti dalle 18 a mezzanotte"), codificata dal PNG senza perdita `_prova/home-finale/lavoro/finali/home-1440.png` |
| `AngeloEIlDiavolo-Sito/allegati-mail/angelo-home-telefono.jpg` | 390 x 5372 px, JPEG progressivo, qualità 80, colore 4:4:4 | 418.628 byte (0,40 MB) | stessa cattura di `screenshot/home/home-390.jpg`, dal PNG `_prova/home-finale/lavoro/finali/home-390.png` |

Totale 1.249.421 byte (1,19 MB), tutti e due sotto 1,5 MB senza alzare la compressione e senza ridurre la larghezza. Controllati il 13/10/2026: si aprono (PIL verify e load, `file`), differenza media rispetto ai JPG della home 1,8 e 2,9 su 255 sui tre canali (solo compressione; ricalcolata il 13/10 con PIL: 1,84 e 2,88), e una nuova cattura di `proto.html` con lo stesso script (`_prova/script/pz2_shot.mjs`, `?giorno=2&ora=16:30`) è identica byte per byte ai due PNG finali (stesso sha256). File di lavoro in `_prova/mail-verifica/allegati-controllo/`.

Si allegano solo i due JPG: non `proto.html` (pagine interne citate ma non fatte: L'osteria, Il progetto, Privacy, Cookie), non l'analisi, non gli screenshot del sito attuale. Sono pagine lunghe: il programma di posta le mostra rimpicciolite, aprendole si leggono alla misura vera. Nelle immagini resta scritto "MARTEDÌ 13 OTTOBRE": il testo della mail lo dice già ("come appare martedì 13 ottobre nel pomeriggio"; anche il primo punto nomina martedì 13 ottobre), quindi va bene anche se la mail parte un altro giorno. **Se si correggono le voci qui sotto, i due JPG vanno rigenerati.**

## Variante quando la demo completa è online

Si sostituisce solo il paragrafo che comincia con "Abbiamo preparato" (fino a "completeremmo il sito con:"); il resto resta uguale. In questo caso i due allegati si possono togliere, e la frase "Gli orari dell'anteprima sono quelli di Google, non del Suo sito" va adattata a quello che mostra la demo.

> Abbiamo preparato, di nostra iniziativa, il nuovo sito, partendo dai Suoi testi e dalle foto già pubblicate del locale. Può vederlo qui:
>
> [link]
> Password di accesso: [password]
>
> È un'anteprima privata, protetta da password e non indicizzata sui motori di ricerca. Il sito comprende:

Con la demo online l'elenco va riscritto con quello che c'è davvero (per esempio quante pagine, se la carta è completa, quanti dei vecchi indirizzi sono collegati). Si può aggiungere "Se decide di acquistarlo, può andare online sul Suo dominio in pochi giorni" solo se è vero. Il corpo attuale ha 298 parole (contate con `wc -w` dal saluto alla firma, trattini degli elenchi compresi); con la variante scende a 294, sotto 320.

## Prima dell'invio (non va nella mail)

### Da correggere nell'anteprima prima di mandarla

Cose che l'oste vedrebbe subito come errori, in ordine di quanto saltano all'occhio, con la correzione più piccola. Si correggono in `proto.html`, poi si rifanno `home-1440.png` e `home-390.png` con `_prova/script/hf_finali.sh` e si rigenerano i due JPG in `allegati-mail/` con la stessa riga di PIL (qualità 80, 4:4:4). Se una voce non si corregge, deve restare coperta da una frase della mail (le voci 2, 3, 5, 11 e 12 lo sono già). Dopo aver rigenerato i JPG, ricontrollare misure e peso (sotto 1,5 MB ciascuno).

1. **"Gli altri giorni anche a pranzo, 10.00-14.30"** e la colonna "pranzo" con 10.00-14.30 nella tabella: alle 10 nessuno pranza, 10.00 è l'apertura del bar presa da Google. Correzione: "Gli altri giorni aperti anche di giorno, 10.00-14.30" e l'intestazione "pranzo" diventa "giorno". Meglio ancora: chiedere l'orario della cucina a pranzo.
2. **Orari presi da Google, diversi da quelli del suo sito** (sito: 10.00-15.00 e 18.00-24.00, chiuso il lunedì tranne d'estate; pagina: 14.30, martedì a pranzo chiuso, domenica sera fino alle 23). Quelli del sito li ha scritti lui. Coperto dalla frase della mail "Gli orari dell'anteprima sono quelli di Google, non del Suo sito: mi dica quelli giusti". Non toglierla.
3. **"Bruna ai fornelli" e la frase "Bruna, deportata da APO a Marostica..."** con foto del 2012, mentre le recensioni Google recenti parlano di "Luca e i ragazzi in cucina". Se Bruna non cucina più è la cosa più delicata della pagina. Correzione minima: la didascalia diventa "La cucina romana"; la frase resta perché è sua, parola per parola. Nella mail è coperto da "Mi piacerebbe sapere chi c'è oggi in cucina e al banco", chiesto a parte e non in un elenco. Lo stesso vale per "Apo al banco": foto di quasi 14 anni fa (EXIF 10/11/2012).
4. **A 1440 il riquadro degli orari copre metà della facciata**: l'insegna verticale illuminata "RISTORANTE PIZZERIA", l'ingresso, il 41/A sul muro e l'espositore "I Ristoranti dell'Oca" (il neon "Enoteca Bar Caffè da Apo" resta visibile). A 390 il riquadro sta sotto la foto. Correzione: anche a 1440 il riquadro va sotto la foto (una regola CSS su `.aed-porta` e `.aed-tessera`). La scritta "l'Angelo e il Diavolo" tagliata in alto è già tagliata nella foto: si sistema solo con una foto nuova.
5. **La pizza non c'è**, con l'insegna "PIZZERIA" sulla porta e i clienti su Google che ne parlano. Correzione minima: una voce "Pizza" sotto "Dal forno a legna", se la fanno ancora. Nella mail è coperto da "pizza" tra le cose che "Le chiederei". Attenzione: nei testi la pizza non è mai nominata, ma si vede in tre foto della galleria (ristorante foto14, 15 e 16) e nella tovaglietta del 2012 con "Le nostre pizze" (locale foto5, sfondo cartone-pizza.jpg); per questo la mail non dice che sul sito manca. Se si aggiunge la voce "Pizza", la mail può dire al massimo "nei testi la pizza non è mai nominata, si vede solo in tre foto della galleria".
6. **"I bianchi, della carta dei vini" è un segnaposto** accanto al vero "Il Rosso di Apo". Correzione: "Il bianco: chiedete all'oste", oppure una o due etichette vere quando le dà lui.
7. **"Di stagione" elenca insieme tartufo, radicchio e asparagi**: gli asparagi di Bassano sono di aprile e maggio, in una pagina datata 13 ottobre sembrano in carta oggi; e la lista viene dal Comune. Correzione: il titolo diventa "Durante l'anno".
8. **"Prenota al 0424 72312"** nel bottone, mentre altrove c'è "allo 0424". Correzione: "Prenota allo 0424 72312".
9. **"Lunedì si riposa."** subito sopra la rima "Si riposa il lunedì...": detto due volte in tre righe. Correzione: togliere "Lunedì si riposa." dalla riga piccola.
10. **Lunedì d'estate**: lo script apre il lunedì a giugno, luglio e agosto, ma tabella e frase dicono sempre "turno di chiusura". Oggi non si vede. Correzione, solo se lui conferma: "turno di chiusura (d'estate aperti)".
11. **Data fissa "MARTEDÌ 13 OTTOBRE"** nelle immagini: coperta dalla mail ("come appare martedì 13 ottobre nel pomeriggio").
12. **Link "Instagram" nel piede** (`https://www.instagram.com/l_angelo_eil_diavolo/`): il profilo viene solo dal QR della tovaglietta del 2012 e il 13/10 Instagram rimandava al login, quindi non è verificato. Coperto dalla mail ("profilo Instagram" tra le cose che "Le chiederei"). Correzione più sicura: togliere il link dal piede di `proto.html` finché lui non lo conferma.
13. **"Stasera aperti dalle 18 a mezzanotte"** in grande: fa pensare che la cucina sia aperta fino a mezzanotte. Correzione, se lo script lo permette: "Stasera aperti dalle 18", e l'orario di chiusura solo nella tabella; meglio ancora chiedergli l'ultima comanda.

### Ricontrollare il giorno dell'invio

Le tre osservazioni sono state verificate il 13/10/2026 (martedì), solo lettura di pagine pubbliche. Script e dati in `_prova/mail-verifica/`: `telefono.cjs` e `telefono.json`, `gmaps-orari.cjs` e `google.json`, `parole.py` e `parole.json`, `exif.py`, `xmp_date.py`, `exif-sfondi.json`, `xmp-date.json`, `orari.txt`, `link.txt`, screenshot in `shots/`. Le cinque pagine del sito sono identiche byte per byte a quelle del 6/10.

1. **Orari** (`orari.txt`, `google.json`, `shots/google-scheda-1.png`). Sito, pagina Contatti: "orari di apertura: 10.00-15.00 18.00-24.00", "Turno di chiusura il lunedì tranne i mesi estivi"; piede: "Si riposa il lunedì perché il fegato respiri...". Google alle 12:15 di martedì 13/10: martedì 18-00, mercoledì-sabato 10-14:30 e 18-00, domenica 10-14:30 e 18-23, lunedì chiuso, stato "Chiuso · Apre alle ore 18". VisitMarostica: "orario 10.00-15.00/18.00-24.00", "Giorno chiusura Chiuso lunedì e martedì a pranzo". La frase della mail cita un momento preciso (martedì 13 a mezzogiorno) e resta vera anche se Google cambia dopo; ma se la scheda Google o il sito cambiano prima dell'invio, la frase va riletta. Quali orari siano veri resta da chiedere all'oste.
2. **Telefono** (`telefono.json`, `shots/01-home-390-schermata.png`, ingrandimenti 4x del numero e del menu). Chromium 390x844 come iPhone; le richieste http sono passate da curl (`ctx.route`) perché Chromium col proxy riceve solo l'errore del relay: valgono le misure del secondo giro. Nessun meta viewport nelle 5 pagine; larghezza 988 px (Home), 980 (L'Angelo e il Diavolo e Contatti), 1002 (Ristorante), 1085 (FESR); scala 0,395 / 0,398 / 0,390 / 0,360. "Prenota ora il tuo tavolo : 0424.72312" e menu: 14 px di CSS, circa 5,5 px a schermo (5,0 sulla FESR). **La mail parla solo di leggibilità**: nel codice non c'è un link `tel:`, ma Safari su iPhone a volte riconosce da solo i numeri nel testo, quindi non va scritto né detto che non si può chiamare con un tocco.
3. **Menu, pizza, foto** (`parole.json`, `exif-sfondi.json`, `xmp-date.json`, `shots/facciata-sito2012-vs-google-oggi.jpg`). Nelle 4 pagine: "menu" 0, "menù" 1 (solo "Il menù è sempre abbinato..."), "€" 0, "euro" 0, "prezz" 0, "pizz" 0; circa 310 parole di contenuto. Foto: 3 sfondi su 4 con EXIF del 10/11/2012 (Pentax K-5, FOTO_BITTANTE); le 32 foto della gallery sono state preparate il 23-24/02/2013 (XMP di Photoshop, data di lavorazione e non di scatto): "le foto sono del 2012" vale per il servizio fotografico. Facciata: `images/locale/foto7.jpg` (legno scuro, neon rosa; senza EXIF; XMP: salvata il 24/02/2013, creator www.petuccodesign.it: anno di scatto non noto, per questo la mail non le dà una data) contro la foto del proprietario su Google (pannelli chiari, stemma dorato, "L'osteria di APO"). **Attenzione**: l'insegna "PIZZERIA" non è sparita (oggi c'è una verticale "RISTORANTE PIZZERIA"); è cambiata la facciata, e un'insegna al neon ("Enoteca Bar Caffè da Apo") c'è ancora oggi. La mail dice solo "nella galleria c'è ancora l'ingresso di una volta, non la facciata di oggi": non nomina insegne, neon, colori né anni. Sulla carta: `ristorante.htm` elenca cinque paste e il porcetto e la tovaglietta-menu del 2012 è fotografata, per questo la mail scrive "non c'è la carta di oggi" e non "non c'è il menu".

Se una osservazione non è più vera, va tolta o sostituita. Ricambi già verificati il 13/10: "nelle quattro pagine ci sono circa 300 parole in tutto"; "nella galleria si vede ancora l'ingresso di una volta, chi arriva in piazza cercando quella foto non vi riconosce". Non scrivere che il sito è "fermo dal 2013": Home e pagina FESR risultano modificate il 03/07/2026 (aggiunta dei loghi), quindi qualcuno il sito lo tocca ancora. Si può dire che foto e testi sono del 2012-2013.

### Da dire solo a voce, mai per iscritto

- **Lucchetto**: il sito non risponde in https (`https.txt`, 13/10: SSL_ERROR_SYSCALL su www e senza www; http risponde 200 senza reindirizzamento). "Il sito non ha il lucchetto: quando lo aprite, il browser lo segna come non sicuro. Nel sito nuovo lo mettiamo." Il dato "nessun certificato registrato" (crt.sh) è del 6/10: il 13/10 crt.sh rispondeva 502.
- **Dominio**: angeloeildiavolo.com scade il **1° dicembre 2026** (RDAP Verisign letto il 13/10, `rdap.json`; registrar PublicDomainRegistry, DNS Seflow). "Chiunque lo gestisca oggi, conviene controllare che il rinnovo sia fatto, così il passaggio al sito nuovo non ha sorprese." Mai per iscritto: una mail su un dominio in scadenza sembra una truffa.
- **Pagina del contributo FESR**: c'è e funziona, ma si raggiunge solo da una fila di quattro loghi piccoli senza scritte in fondo alla Home (150x31 px, circa 59x12 sul telefono, senza testo alternativo); dalle altre pagine e dal menu non si arriva (`link.txt`). "Nel sito nuovo la teniamo e la mettiamo dove si trova." Tocca un obbligo legato a un contributo pubblico: non presentarlo come difetto.
- **Privacy e cookie**: nessuna informativa e nessun banner; la mappa Google nella pagina Contatti si carica subito (circa 35 richieste a Google prima di qualsiasi consenso) e Google Fonts è chiamato da ogni pagina (dal 01, 6/10). Il nuovo sito li sistema.
- **Instagram**: la mail lo chiede già ("profilo Instagram"). Se non risponde per iscritto, a voce: "Ha un profilo Instagram? Sul sito non c'è nessun collegamento: se c'è, lo mettiamo in evidenza." Il profilo @l_angelo_eil_diavolo è noto solo dal QR della tovaglietta del 2012; il 13/10 Instagram rimandava al login, quindi non è riverificato.
- **Galleria e Google** (solo se chiede di Google): le 32 foto si aprono solo con il clic su "Guarda la gallery" e non sono scritte nella pagina, quindi Google non le vede. Per un cliente con un telefono normale la galleria funziona.
- **Refuso** (facoltativo): nella pagina Ristorante "un'apia carta dei vini" invece di "ampia". In una prima mail suonerebbe pignolo.
- **Facebook**: il vecchio link del sito porta ancora alla pagina del locale (13/10, `facebook.json`): non è un difetto, non dirlo. Unico dettaglio: in Contatti si invita a prenotare da Facebook ("Seguici e prenota il tuo tavolo"); chiedere se rispondono davvero lì.
- Velocità: il sito attuale non è lento (0,6-1,7 s); se chiede, dirlo con onestà.

### Dati del prototipo da confermare con lui

Nella mail sono riassunti in tre frasi (orari; chi c'è in cucina e al banco; pizza, piatti, vini, Instagram, foto e disegno). C = da confermare.

**Orari e giorni**
- "Lunedì si riposa" e "turno di chiusura": sito, Google, Comune. C per il lunedì d'estate (vedi voce 10 sopra).
- "Martedì solo la sera, 18.00-24.00": scheda Google del 6/10; il Comune dice "chiuso lunedì e martedì a pranzo", il sito no. C
- Mercoledì-sabato 10.00-14.30 e 18.00-24.00: Google. Il sito e il Comune dicono 10.00-15.00. C
- Domenica 10.00-14.30 e 18.00-23.00: solo Google. C
- Ultima comanda e orario della cucina: la pagina non li dice, "a mezzanotte" fa pensare che si mangi fino alle 24. C
- Stato di oggi in grande ("Stasera aperti dalle 18 a mezzanotte") e data: calcolati dallo script sugli orari di Google.

**Rima**: "Si riposa il lunedì perché il fegato respiri, aperto tutti gli altri dì tra brindisi e sospiri." Piede del sito attuale: è sua, OK.

**Piatti e vini**
- Cacio e pepe, matriciana, gricia, aglio & olio, carbonara, "e tante altre specialità": ristorante.htm, 2012-2013. C se sono ancora in carta.
- "Bruna, deportata da APO a Marostica, ha deciso di portare un po' di cultura culinaria romana nel Veneto.": ristorante.htm, parola per parola. C se Bruna cucina ancora.
- "Carne alla griglia": descrizione del proprietario su Google. OK, C solo come unico secondo.
- "Porcetto, tutte le domeniche o su prenotazione", "Dal forno a legna": ristorante.htm. C se è ancora ogni domenica.
- Tartufo di Norcia e delle Langhe, radicchio di Treviso, asparagi di Bassano, piatti a base di oca: scheda VisitMarostica, non scritta dall'osteria. C. L'adesione a "I Ristoranti dell'Oca" si vede solo dall'espositore nella foto della facciata. C
- Pizza: assente dalla pagina, presente sull'insegna e nelle recensioni recenti. C
- "Il Rosso di Apo, il vino della casa": etichetta in una foto del 2012. C se esiste ancora.
- "I bianchi, della carta dei vini": segnaposto. C, servono etichette vere.
- Prezzi: nessuno nella pagina (gli unici trovati sono del 2012). Bene così.

**Persone**
- Bruna: frase di "In tavola" e foto "Bruna ai fornelli" (2012). C: le recensioni recenti citano "Luca e i ragazzi in cucina".
- Apo: foto "Apo al banco", 2012. OK come persona, ma la foto ha quasi 14 anni.
- Musica, canzoni, serate, la gente che viene per Apo e non solo per mangiare: la pagina non ne parla (lettura da oste del 13/10). Da chiedere a voce, se vuole metterlo.
- Lorenzo Ambrosi: non è nella pagina; il sito lo presenta come "il nuovo che arriva". Da chiedere solo se lo si vuole mettere.

**Nomi, indirizzo, numeri**
- "L'Angelo e il Diavolo, l'osteria di APO" e logo: logo attuale pubblicato dall'azienda (file VisitMarostica). OK; serve il vettoriale.
- Piazza Castello 41/A, 36063 Marostica (VI), "sotto il portico": sito, Google, Comune. OK
- Punto sulla mappa: nodo OpenStreetMap 7810315441, "Piazza Castello 41a". La mappa è ruotata e senza nord: farla guardare all'oste, deve riconoscere il suo angolo della piazza.
- Telefono 0424 72312: sito, Google, Comune. OK
- Email robertoapoambrosi@gmail.com: contatti.htm, 13/10. OK
- Facebook `/p/Langelo-e-il-diavolo-100063717151643/` e "si prenota... oppure su Facebook": C se rispondono davvero su Facebook.
- Instagram @l_angelo_eil_diavolo: dal QR della tovaglietta del 2012, non aperto, ma linkato nel piede del prototipo (voce 12). C
- Tripadvisor d2626610: sito. OK
- Ragione sociale, P.IVA 02198470243, REA VI-213537: piede del sito, aziende.it, visurissima. OK
- Sede legale Corso G. Mazzini 21, 36063 Marostica: VIES (che aggiunge "interno 2"). OK, C l'interno.
- FESR: "PR Veneto FESR 2021-2027, con il Distretto del Commercio di Marostica. Contributo deliberato alla nostra impresa € 19.989,96": Bando_pr_veneto.htm. OK, loghi dalla stessa pagina.

**PEC nel piede**: nel prototipo non c'è (cercata, nessun "pec" nella pagina). L'unica trovata, langeloeildiavolo@pec.it, ha una sola fonte leggibile. Per un'impresa individuale sul sito basta la P.IVA: lasciarla fuori; se il titolare la vuole, C.

**Diritti delle immagini** (tutti C)
- Porcetto, rigatoni, Bruna, Apo al banco: foto di Paolo Bittante del 2012 (FOTO_BITTANTE). Servono licenza per il nuovo sito e, se possibile, gli originali.
- La sala: foto del portale VisitMarostica (iPhone 12, 18/10/2023), con i colori portati verso le foto del 2012.
- La facciata: foto caricata dal proprietario sulla scheda Google, probabilmente sua, ma va chiesto.
- Disegno firmato "Don Backy 98", con la battuta e la didascalia "Don Backy, 1998": scansione della galleria del sito. Serve il permesso dell'autore o di chi ne ha i diritti.
- Mappa: dati © OpenStreetMap, citati nella pagina. OK
- Loghi FESR: dalla pagina del bando. OK

**Pagine interne citate ma non fatte**: L'osteria, Il progetto, Privacy, Cookie. Negli screenshot non si nota; se un giorno si manda il link della pagina, sì.

### Controlli

- Correggere l'anteprima (sezione in cima) o, per le voci non corrette, verificare che la mail le copra; poi rigenerare e riaprire i due JPG.
- Riverificare le tre osservazioni il giorno dell'invio con gli script di `_prova/mail-verifica/` (soprattutto gli orari su Google e sul sito).
- Compilare [Nome Cognome], [Agenzia], [telefono] e [email]. La mail parte dalla casella dell'agenzia, non da qui.
- Destinatario solo robertoapoambrosi@gmail.com. Non usare la PEC né lorenzo.a7788@gmail.com, e non mettere la PEC nel piede.
- Saluto "Gentile Signor Ambrosi," e il Lei in tutta la mail (Sue, La, Le, preferisce): se si ritocca il testo, non tornare al Voi dei modelli.
- Orario di invio: mattino di un giorno feriale, non il lunedì (giorno di riposo, legge la posta più tardi) e non a ridosso del servizio. La visita in Piazza Castello va proposta lontano da pranzo e cena, e prima si telefona.
- Allegare solo i due JPG e aprirli dal telefono prima di inviarli: sono pagine lunghe (4056 e 5372 px). Nessun link nella mail.
- Non scrivere né dire che il sito completo è pronto: esiste solo la pagina iniziale. Decidere tempi e prezzo prima dell'eventuale incontro.
- Quando la demo sarà online: password, nessuna indicizzazione, e attenzione al link "chiama" e a eventuali mailto o moduli, che non devono scrivere o telefonare davvero all'osteria durante le prove.
- Nel corpo: niente sicurezza, dominio, privacy, cookie; niente parole da agenzia (lista del metodo, anche quando sono dentro parole più lunghe); niente lineetta lunga.

## Correzioni del controllo avversario (13 ottobre 2026)

Due controlli indipendenti sulla bozza: controllo dei fatti (sola lettura delle 5 pagine vive, VisitMarostica, scheda Google riletta alle 12.21, allegati; file in `_prova/mail-verifica/controllo-fatti/`) e lettura da oste. Testo prima delle correzioni: `_prova/mail-verifica/finale/MAIL-PROPOSTA-prima.md`; corpo finale e variante contati in `_prova/mail-verifica/finale/`.

Nel corpo:

- **Terzo punto riscritto**: era "non c'è il menu, la parola "pizza" non compare mai e le foto del 2012 mostrano ancora il vecchio ingresso in legno scuro e neon rosa". Ora "non c'è la carta di oggi, e nella galleria c'è ancora l'ingresso di una volta, non la facciata di oggi". La pizza si vede in tre foto della galleria e nella tovaglietta del 2012, e manca anche nella nostra anteprima; `ristorante.htm` elenca cinque paste e il porcetto; la foto della facciata (`foto7.jpg`) non ha una data del 2012 provata (XMP 24/02/2013, petuccodesign.it) e un neon c'è ancora oggi. Per l'oste "la parola non compare mai" sembrava un programma e "legno scuro e neon rosa" una presa in giro della sua storia. La pizza resta solo tra le domande.
- **"come si vedeva martedì pomeriggio"** diventato "come appare martedì 13 ottobre nel pomeriggio": la cattura è delle 05.32 con l'ora della pagina simulata (`?giorno=2&ora=16:30`), quindi quel pomeriggio non era ancora arrivato.
- **"partendo dalle Sue foto e dai Suoi testi"** diventato "partendo dai Suoi testi, rima del lunedì compresa, e dalle foto già pubblicate": le foto dell'anteprima sono del Comune, di Google, di Paolo Bittante e di Don Backy. Stessa correzione nella variante. La rima fa capire all'oste che il sito l'abbiamo letto.
- **Primo punto**: "Chiuso · Apre alle ore 18" citato alla lettera; "il sito dava aperto dalle 10 alle 15 tranne il lunedì", perché il sito dà un orario generale e non quello del giorno; "il sito del Comune" al posto di "il portale del Comune" (stessa fonte, parole più semplici); aggiunto "a chi credere?", la conseguenza per il cliente che l'oste riconosce subito.
- **Instagram tra le domande** ("profilo Instagram"): il link è nel piede dell'anteprima ma il profilo non è verificato.
- **Domande su persone e piatti divise**: "Mi piacerebbe sapere chi c'è oggi in cucina e al banco; poi Le chiederei pizza, piatti, vini, profilo Instagram e il permesso per foto e disegno di Don Backy". Prima "Da verificare anche chi è in cucina oggi" sembrava una voce da spuntare su una cosa di casa sua; "il permesso" al posto di "l'uso delle foto", che suonava da notaio.
- **"non del Suo sito"** aggiunto a "Gli orari dell'anteprima sono quelli di Google": anticipa la sua obiezione principale (10.00-14.30 contro il suo 10-15).
- **Tono**: "realizziamo siti per aziende" diventato "facciamo siti internet" (un'osteria non si sente un'azienda); "Su www.angeloeildiavolo.com oggi non è facile trovarlo" diventato "Sul Suo sito si trova a fatica"; "riservata a questa proposta" sostituito da "Non è pubblicata." (vero: non c'è una demo online), anche nella variante ("protetta da password"); "i vecchi indirizzi collegati ai nuovi" diventato "i vecchi collegamenti di Google che funzionano ancora"; "posso passare in un'ora lontana dal servizio per mostrargliela" diventato "passo in Piazza Castello lontano dal servizio e Le mostro tutto".
- **"siete aperti"** diventato "l'osteria è aperta" (due volte), per non sembrare un ritorno al Voi.
- **Conteggio**: corpo da 297 a 298 parole con `wc -w` (dal saluto alla firma); la variante 294 e non "circa 306". Tagliati per stare sotto 300 "oggi", "quindi", "del locale", "da nessuna parte".

Nel resto del file:

- Destinatario: "la legge lui" era una deduzione dal nome dell'indirizzo, ora "Dal nome è la casella personale del titolare"; citazione di visurissima resa letterale.
- Allegati: ora della cattura detta com'è (05.32, orologio della pagina simulato); differenze medie ricalcolate (1,84 e 2,88 su 255 sui tre canali, non 1,7 e 2,5); la nuova cattura è identica byte per byte ai PNG finali, più forte di "nessun pixel oltre 40".
- Anteprima: nuove voci 12 (link Instagram non verificato) e 13 ("Stasera aperti dalle 18 a mezzanotte" fa pensare alla cucina fino alle 24); voce 5 con le prove della pizza in galleria; voce 3 e Persone "quasi 14 anni" (EXIF 10/11/2012); dopo la rigenerazione dei JPG ricontrollare misure e peso.
- Ricontrollare: larghezze con le pagine a cui corrispondono (Contatti 980 mancava); foto della facciata senza data di scatto; nota su insegna al neon e carta.
- Dati da confermare: aggiunta la musica e la gente che viene per Apo, che l'oste non trova nella pagina.
- Controlli: tolto l'esempio di parola lunga che contiene una parola vietata, perché era il file stesso a far scattare il controllo automatico.

Non applicate: nessuna correzione è stata scartata. Le osservazioni dell'oste sull'anteprima (orari, "pranzo", Bruna, bianchi, "Di stagione", "allo 0424", "Lunedì si riposa" doppio, riquadro sulla facciata, pizza, data) erano già nelle voci 1-11 di "Da correggere nell'anteprima" o sono state aggiunte (12, 13); i due JPG allegati non sono stati rigenerati.
