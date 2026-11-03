# Nic Dean: proposta di nuova home

Proposta non richiesta di una nuova homepage per Nic Dean S.r.l., calzaturificio della famiglia Nicoletto a Villatora di Saonara (PD), con lo spaccio di fabbrica in via Lombardia 29. Solo la home.

- **Pagina**: `sito/index.html`, statica (si apre con file:///), con `sito/img/` e `sito/fonts/`. Versione "livello professionale" del 3 novembre 2026, con il ritocco finale dello stesso giorno (apertura a tutta fascia, tessere sullo stesso grigio della fila, foto dello spaccio tolta, testo a 19 px, 1975 e 2013 a 200 px: dettagli in `screenshot/home/NOTA.md`).
- **Screenshot e nota**: `screenshot/home/` (nota in `screenshot/home/NOTA.md`, sezione "Livello professionale", con l'esito di ogni regola).
- **Analisi con le fonti**: `01-analisi.md`. Scheda di identità e d'uso: `_prova/uso/SCHEDA.md`.
- **Versione precedente**: `_prova/versione-1-originale/` (sito e screenshot com'erano prima di questo passaggio).
- **Rifare tutto**: `bash _prova/script/build_finale.sh` (screenshot e controlli); `--immagini` rifà anche le immagini con `pro_img.py`. Controlli delle regole e prove d'uso: `node _prova/script/pro_controlli.mjs <percorso di sito/index.html>`.

## Prima di tutto: verificare che lo spaccio sia aperto

La home presuppone che calzaturificio e spaccio di via Lombardia 29 siano attivi. Per i registri la società oggi ha ATECO 68.20 (affitto di immobili propri), 1 dipendente, 20.918 euro di fatturato nel 2025, sede legale in via Emilia 2 a Padova, e il sito è fermo al 2017. Nessuna recensione pubblica trovata (SCHEDA, "Prima di tutto").

**La home si manda solo dopo un sopralluogo o una visura**, senza contattare l'azienda finché non si decide. Se lo spaccio è chiuso non c'è un cliente per questa home.

## Stato "aperto o chiuso" dello spaccio: ora è acceso

In questa versione lo stato è calcolato (nella prima schermata e in testata da 1280 px): "Aperto ora, fino alle 12", "Chiuso ora, riapre oggi alle 14:30", "Chiuso il sabato e la domenica, riapre lunedì alle 8", "Chiuso per ferie, riapre il 1 settembre alle 8", "Chiuso, oggi è festa, riapre domani alle 8". La riga di oggi nella tabella degli orari è in grassetto.
- **Calcolo**: ora italiana; lunedì-venerdì 8-12 e 14:30-17; chiuso sabato, domenica, tutto agosto e i festivi nazionali (Capodanno, Epifania, Pasquetta, 25 aprile, 1 maggio, 2 giugno, Ferragosto, Ognissanti, 8 dicembre, Natale, Santo Stefano, e il 4 ottobre dal 2026).
- **Senza JavaScript** la riga dice "Aperto lunedì-venerdì, chiuso sabato, domenica e agosto", vero in ogni momento, e sotto restano gli orari scritti.
- **Prova a un'ora data**: `index.html?ora=2026-11-07T10:00` (gli screenshot sono fatti a martedì 3 novembre alle 10).
- **Da aggiungere a mano** dopo la conferma: il patrono locale e le chiusure straordinarie (ferie di Natale, ponti) nell'elenco `CHIUSURE` dello script, date nella forma `'2026-12-28'`; in quei giorni lo stato dice "Chiuso oggi, riapre ...". Senza questo elenco, il 28 dicembre la pagina direbbe "Aperto ora" anche se lo spaccio fosse chiuso. Se gli orari non si confermano, lo stato va tolto (basta non chiamare `aggiorna()` nello script).

## Cose da chiedere all'azienda (oggi in pagina o legate alla pagina)

- **Orari dello spaccio**: il loro sito dice lunedì-venerdì 8-12 e 14:30-17 ma anche "aperti tutta la settimana": la pagina scrive "Sabato e domenica chiuso" (SCHEDA, par. 3). Da confermare, come la chiusura di tutto agosto (la news del loro sito non ha anno) e i festivi.
- **Pagamento** in contanti e carta, **appuntamento** per mail o telefono: dal sito del 2017 ("Se vuoi puoi prendere un appuntamento per mail o telefono"); la pagina non dice più "fuori orario", che non era nelle fonti.
- **Cosa vende oggi lo spaccio**: se solo produzione propria, se ancora per donna, uomo e ragazzo e "di tutti i numeri".
- **Le scarpe in pagina** (otto tessere): sono le foto della galleria del loro Flash (ritoccate nel 2015) e lo stivale del sito del 2017. In pagina non hanno date e il testo dice "Le collezioni cambiano con la stagione: per sapere cosa c'è adesso, chiamaci o passa". Da chiedere: quali modelli ci sono ancora, i nomi che usano loro (oggi i nomi sono descrizioni nostre: "Tronchetto con risvolto, grigio"), i materiali (camoscio, vernice) prima di scriverli.
- **La fila delle décolleté**: modello, nomi dei colori, se il pitone è vero o stampato; se il modello è ancora in vendita (galleria "Estate 2017").
- **Spedizione o ritiro** per chi chiede una scarpa per mail (SCHEDA, visitatore 2): non è scritto da nessuna parte, quindi la pagina non promette nulla. Fa solo chiedere: "Se abiti lontano, scrivi anche la tua città e chiedi se si può spedire", e ogni mail delle scarpe ha la riga "Se abiti lontano, la tua città (per chiedere se si può spedire)". È il punto che decide per chi abita lontano (cliente tipo 2, compito non riuscito): va chiesto all'azienda e, se spediscono, scritto chiaro sotto il titolo delle scarpe con costi e tempi; se non spediscono, scrivere "si ritira in spaccio".
- **Uomo e ragazzo in foto**: la pagina dice "quasi tutti da donna: allo spaccio trovi anche uomo e ragazzo", perché le foto che hanno sono di modelli da donna (da confermare, il mocassino e la francesina potrebbero essere unisex). Servono almeno una scarpa da uomo e una da ragazzo per la griglia.
- **Gamma dei numeri** ("di tutti i numeri"): se la danno, per esempio "donna dal 35 al 41", va nella sezione delle scarpe.
- **Ordini di quantità**: la pagina dice "Si possono fare anche ordini con un numero consistente di calzature per negozi, fiere o eventi ... ti mandiamo gratuitamente un preventivo" e "di livello medio-fine" (parole del loro sito). Va confermato che lo facciano ancora.
- **Mercati**: "Per anni le calzature Nic Dean sono andate soprattutto ai negozi d'Europa e del Nord America" è al passato perché viene dal sito del 2017. Da confermare con loro.
- **Telefono e fax**: 049 640672 e 049 8791084 vengono dal sito; verificare che rispondano. Il fax si toglie se non è attivo.
- **Riga legale**: C.F. e P.IVA 02707240285, REA PD-300932, capitale 51.000 euro i.v. da riscontrare con una visura. Sede legale (via Emilia 2, Padova) e PEC non sono in pagina: da decidere con loro.
- **Facebook "Nic Dean Shop"**: tolto dalla pagina perché non si è potuto verificare che sia viva (si apre solo dopo il login). Il cliente tipo dello spaccio la cerca per ferie, chiusure straordinarie e sconti: se è viva va sotto gli orari ("Chiusure straordinarie e sconti: pagina Facebook Nic Dean Shop") e nel piede con il sottotitolo "la pagina dello spaccio".
- **Chi della famiglia Nicoletto** guida l'azienda e se vuole comparire, con nome e foto.

## Prove che mancano (regola 10): da chiedere, non da inventare

Le regole chiedono almeno tre tipi di prove tra recensioni, numeri, certificazioni o fornitori, clienti con il nome. In pagina ci sono solo le due cifre vere, 1975 e 2013, a 200 px in "Chi siamo" (tolti "3" e "Tutti", che erano riempitivi). Da chiedere:
- **Recensioni**: una scheda Google dello spaccio con recensioni vere (oggi non trovata). Con 3-5 recensioni con nome e comune si aggiunge una fascia tra lo spaccio e "Chi siamo".
- **Negozi clienti** che vendono o hanno venduto le scarpe Nic Dean, con il permesso di nominarli.
- **Fiere**: l'ultima documentata è MICAM Milano e GDS Düsseldorf, marzo 2012; tolta dalla home perché fa sembrare l'azienda ferma. Se ce ne sono di più recenti, vanno nella sezione per i negozi.
- **Numeri di produzione**: paia l'anno, modelli a collezione, anni di attività nello stesso capannone, solo se li danno loro.

## Modulo da collegare

Nella sezione "Per negozi, fiere ed eventi" c'è un modulo con il tipo di richiesta (Ordine per un negozio, Fiera o evento, Una scarpa per me, Altro), nome, telefono, email e "Modelli, numeri e quantità".
- **Oggi non invia nulla da solo**: "Prepara l'email" apre il programma di posta di chi scrive con una mail a info@nicdean.it già compilata (oggetto "tipo, nome" e i campi nel testo). Senza JavaScript il modulo usa `action="mailto:"`.
- **Va collegato a un servizio** (Formspree, Brevo, un endpoint PHP sul loro hosting o simili), con conferma di ricezione e informativa privacy vera. Poi va aggiornata la riga "Privacy" del piede, che oggi dice, ed è vero per questa pagina statica, che non usa cookie e non raccoglie dati.
- **La newsletter della versione 1 è stata tolta**: non inviava nulla. Si rimette solo con un servizio vero e se lo spaccio manda davvero avvisi (ferie, sconti).

## Foto da fare dal vero

La home usa solo foto loro, perché il committente ha deciso "niente" repertorio e niente illustrazioni. Sono deboli: per questo la pagina si regge su tipografia, colori del marchio e fatti. In ordine di importanza:

1. **La fila delle décolleté in studio**, la prima di tutte: è l'immagine della prima schermata. Oggi è una foto da 1024 px di autore ignoto (EXIF "Software: Google"), ripulita con PIL (chiazze del camoscio attenuate, fondo portato a un grigio chiaro neutro). Come: cinque colori dello stesso modello, camoscio nuovo, fondo continuo grigio chiaro, luce morbida da sinistra, ombra corta, macchina all'altezza del plateau, almeno 4000 px di lato. Con la foto nuova si rifanno `fila-760/972/1480.jpg` con `pro_img.py` senza toccare la pagina.
2. **Lo spaccio** in luce naturale, finestre non bruciate: scaffali di scatole, il banco, una scarpa in mano a una cliente, 4:3, almeno 2400 px. La foto di oggi (960x720, compatta, voto 3, finestre bruciate) è stata tolta dalla pagina nel ritocco finale: oggi la sezione è solo tipografia. Con la foto nuova si riaccende il passo 3 di `pro_img.py` (`SPACCIO = True`) e la foto va a sinistra della tabella degli orari.
3. **La facciata con l'insegna NIC DEAN** sul cancello, dal marciapiede: serve a riconoscerli arrivando (la foto di oggi sembra una cattura di Street View e non è usata).
4. **Le scarpe di oggi**, una per modello, tutte con la stessa luce della fila su fondo grigio chiaro continuo (o bianco, che `pro_img.py` porta al grigio #EBEBE9 della pagina), stessa inquadratura di profilo, almeno 2000 px: sostituiscono le otto tessere (Olympus del 2001, 500x375). Con 8 o 12 modelli la griglia resta la stessa.
5. **Macro della firma NicDean sul sottopiede**, stessa luce della fila: può diventare il secondo gesto della pagina, in "Chi siamo".
6. **Le mani al banco a Villatora**, solo se la produzione continua: per la sezione dei negozi, che oggi è solo testo e modulo.

## Caratteri

League Spartan (The League of Moveable Type, Google Fonts), SIL Open Font License 1.1, uso commerciale libero. Una sola famiglia, pesi 400 e 700 (prima 300-500: rifatto il download con `wght@400..700` il 3/11/2026).
- **File serviti dalla pagina**: `sito/fonts/league-spartan-latin.woff2` e `league-spartan-latin-ext.woff2`.
- **Licenza**: `sito/fonts/OFL.txt`.

## Loghi

- **In pagina**: `sito/img/logo-nicdean.png` (390x96, trasparente), rendering 4x del disegno vettoriale dentro il loro Flash `indice_nic.swf`; il blocchetto rosso resta in prospettiva come nel Flash.
- **Da chiedere**: il logo vettoriale originale e la versione piatta ufficiale, all'azienda o a Medialine Group, l'agenzia del Flash.
- **Firma**: la firma "NicDean" in corsivo del sottopiede non esiste in digitale.

## Fuori dalla pagina, apposta

- "Riviera del Brenta": è il loro modo di dire, ma Saonara è ai margini del distretto; il refuso "Riviera del Brente" non va riportato.
- La data "1997 nasce la Nic Dean S.r.l." (dato di registro) e le pagine "Collezioni" per stagione, che non esistono: in una home sola tutti i link portano a un punto della pagina.
