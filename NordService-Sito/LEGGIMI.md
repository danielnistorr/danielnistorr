# Nord Service: proposta di nuova home (livello professionale)

Proposta non richiesta di nuova homepage per Nord Service SRL (verniciatura e sabbiatura industriale, carrozzeria di macchine da lavoro, Mestrino PD). Solo la home.

- Pagina: `sito/index.html` (statica, si apre con file:///), `sito/img/`, `sito/fonts/` (Archivo, con `OFL.txt`).
- Screenshot e nota di progetto: `screenshot/home/` (`NOTA.md`, sezione "Livello professionale").
- Rifare tutto: `bash _prova/script/build_finale.sh --immagini` (immagini con `pro_img.py`, screenshot all'ora simulata martedì 3 novembre 2026 alle 10, poi i controlli `pro_controlli.mjs`, esito in `_prova/pro_controlli.json`). Prima schermata con le misure: `node _prova/script/pro_prima.mjs <url> <out.png> <larghezza> <altezza> [mobile]`.
- Per provare lo stato aperto/chiuso a un'altra ora: aggiungere all'indirizzo `?ora=2026-11-07T10:00` (ora di Roma).
- Versione precedente ("Tornano nuove", con la pala scontornata): `_prova/versione-1-originale/` (sito e screenshot).
- Analisi con le fonti: `01-analisi.md`; scheda d'uso e identità: `_prova/uso/SCHEDA.md`.

## Il modulo va collegato a un servizio

Il modulo "Chiedi un preventivo" oggi **non invia niente**: controlla nome e telefono e poi apre il programma di posta con una mail già scritta (oggetto "Preventivo: mezzo, modello, nome" e tutti i campi nel testo, compreso "Quanti pezzi o macchine"). Sotto il bottone compare lo stesso testo con "Copia il testo" e l'indirizzo in chiaro, per chi usa una webmail e non vede aprirsi niente. Le foto le allega chi scrive, a mano. Prima di pubblicare va collegato a un servizio di invio vero (per esempio il modulo del CMS, Formspree, o un indirizzo del loro hosting) con **il caricamento delle foto** (3-4 per richiesta, fino a circa 10 MB l'una), una risposta "ricevuto" e la privacy. Anche il bottone "Manda le foto per mail" (con l'indirizzo scritto in chiaro sotto) è un `mailto:` con oggetto e traccia: va bene così, ma se aprono un numero WhatsApp per le foto (vedi sotto) si può aggiungere accanto.

## Da chiedere all'azienda prima di pubblicare

In pagina c'è solo quello che sta in 01-analisi.md e nella scheda, con la loro fonte. Queste cose mancano o sono dubbie e non sono in pagina (o sono in pagina nella forma più prudente):

1. **WhatsApp per le foto**: hanno un numero da rendere pubblico? Per chi è sul piazzale è il modo più comodo di mandare le foto della macchina.
2. **Tempi**: quanto ci vuole di solito (il D8R, dalle date delle foto, circa due settimane). E **in quanto tempo rispondete a una richiesta di preventivo?** Quando lo dicono, va scritto sopra il bottone "Prepara la mail" (come Wilson, "entro 48 ore"). Si può scrivere sotto i bottoni dell'apertura "Tempi e prezzo te li diciamo dopo aver visto le foto"? In pagina oggi nessun tempo.
3. **Ritiro**: vanno a prendere la macchina o la porta il cliente (le foto mostrano 8 macchine sul carrellone)? Si può scrivere "le macchine arrivano anche su carrellone"? In pagina il campo "Dove si trova la macchina" suggerisce "la porto io", niente promesse di ritiro.
4. **Misure**: quante cabine (sabbiatura e verniciatura), quanto grandi, il mezzo più grande che entra. Sarebbero una prova forte (regola 10).
5. **Zona**: da dove arrivano i clienti (Tabarelli è a Mozzecane, 90 km). Non c'è un elenco di comuni in pagina perché le macchine vengono portate in officina e nessuna fonte dice una zona.
6. **Recensioni**: nessuna trovata (YouDriver "There are no reviews yet"; Google, Pagine Gialle e Instagram non leggibili da qui). Se hanno recensioni Google o due o tre clienti disposti a dire una frase con nome e comune, vanno in una fascia dopo i lavori (regola 10).
7. **Clienti con il nome**: Tabarelli (6 foto su 33 sono loro movimentatori) è un cliente fisso? Si può scrivere? Oggi in pagina il nome Tabarelli non è scritto: si vedono solo i loro movimentatori T510 e la torretta 813 nelle foto delle schede.
8. **Certificazioni, associazioni, fornitori di vernici** (per esempio la marca dei prodotti): nessuna nelle fonti. Con i loghi si fa la fascia della regola 10 e si completa il piede.
9. **Lavori**: per tre o quattro lavori il cliente o il luogo e due dati (cosa è stato fatto, giorni). Da confermare per quelli in pagina:
   - che le tre foto del 3, 10 e 16 ottobre 2024 (date dai nomi dei file) siano lo stesso CAT D8R;
   - che la foto dell'apertura (Sony, `DSC07356`, macchina coperta da carta, nastro e nylon) sia stata scattata nella loro cabina di Mestrino, come dice il testo alternativo, e che si possa usare;
   - che la WA320 della scheda Movimento terra (Sony, maggio 2025) sia un lavoro loro (in pagina non c'è scritto "riverniciata");
   - che il mini escavatore (scheda Fondi e vernici), il pannello stuccato (scheda Vetroresina), le due virole e il traliccio giallo ("Altri lavori") siano lavori loro; per virole e traliccio servono cliente o luogo, anno e due dati per farli diventare lavori con un nome (regola 11);
   - la scheda Sabbiatura usa un dettaglio della stessa foto del D8R sabbiato (cingoli e garnet a terra): appena c'è una foto del getto di garnet in cabina va sostituita.
10. **Testi nuovi da approvare**: il titolo "Verniciatura e sabbiatura industriale" è la riga del loro logo; la riga "Carrozzeria e vetri di macchine da lavoro, camion e rimorchi e mezzi agricoli: tutta la macchina o un pezzo solo" è nostra, fatta con le loro parole; anche le righe delle sei schede dei mezzi ("Escavatori, pale gommate, apripista, mini escavatori", "Trattori stradali, scarrabili, semirimorchi e cassoni"...) vengono dalle loro foto e vanno confermate. "Gru e sollevatori" si basa sull'autogru e sul Manitou delle loro foto. Nuove nel ritocco finale, fatte con le loro parole e da far leggere: la garanzia "Un numero solo" (le sei lavorazioni con una sola officina da chiamare), "Dal metallo nudo alla vernice, sulla macchina intera o su un pezzo solo", "Mezzo fermo? Chiama l'officina.", i titoli "Stefano e Leonardo Barbieri" e "Traliccio giallo in cabina".
11. **Orari**: chiusure estive, ponti e patrono di Mestrino. Lo stato "Aperto ora / Chiuso" conta già i festivi nazionali e Pasquetta; il resto va aggiunto nello script quando lo dicono.
12. **Piede**: sede legale a Rubano (Via Pitagora 11/A, da VIES) e officina a Mestrino, scritte così? REA, capitale sociale e PEC non sono pubblici e non sono in pagina. Pagine `privacy/` e `cookie/` da fare.
13. **Social**: l'Instagram è attivo e che cosa ci pubblicano? Se sì, sotto il link va un sottotitolo vero (per esempio "I lavori in officina"); se è fermo, il link va tolto. La pagina Facebook esiste (oggi sul loro sito il link è vuoto)?
14. **Ambiente**: "un occhio di riguardo per l'ambiente" non è in pagina finché non dicono cosa fanno (vernici a base acqua? recupero del garnet?). In pagina restano solo le loro parole sul garnet.
15. **Permessi sulle foto**: chi ha scattato le tre foto Sony e se si possono usare; macchine dei clienti con il marchio in vista (Komatsu, CAT, Tabarelli, Scania): serve il permesso del cliente?
16. **Logo**: serve l'originale vettoriale (SVG o PDF) e una versione ufficiale chiara per i fondi scuri. Nel piede oggi c'è il PNG con le lettere nere rese bianche (stesso disegno, solo il colore cambiato).
17. **Lavori in serie**: fanno lavori ricorrenti o in serie per costruttori, concessionari e noleggiatori (torrette, bracci, cassoni, virole)? Se sì, una riga e una fascia dedicata sotto "Altri lavori"; oggi in pagina solo "Anche un pezzo solo" e il campo "Quanti pezzi o macchine" nel modulo.

## Foto da fare dal vero

Le foto in pagina sono tutte loro, ma in gran parte da telefono e con luci diverse: `pro_img.py` dà a tutte lo stesso trattamento (bilanciamento neutro, colore -10 %, stesso contrasto e stessa curva sulle ombre), ma non può farne una serie vera. Per il sito vero serve una mezza giornata con la stessa fotocamera Sony (APS-C, 35 o 50 mm), luce del mattino o cielo coperto chiaro, sempre la stessa:
- **Stefano e Leonardo** in officina, in tuta, davanti a una macchina appena finita o in cabina: è la foto che manca di più (i riferimenti del mestiere mettono sempre la squadra in apertura o in "Chi siamo").
- **Apertura**: oggi è la cabina con una macchina mascherata (Sony): rifarla in orizzontale e in verticale, con Stefano o Leonardo al lavoro dentro (pistola o mascheratura), la stessa luce dei neon e il logo visibile sulla tuta. In alternativa una macchina finita sul piazzale, di tre quarti, sfondo libero.
- **Una foto per ognuno dei sei mezzi** (movimento terra, movimentatori, gru e sollevatori, camion e rimorchi, mezzi agricoli, pezzi), tutte in orizzontale 4:3, stessa altezza e stessa distanza: sostituiscono le foto da WhatsApp delle schede.
- **Una foto per ognuna delle sei lavorazioni**: getto di garnet in cabina (sostituisce il dettaglio del D8R nella scheda Sabbiatura), pistola a spruzzo sul fondo, stuccatura della vetroresina, saldatura (per la scheda Carpenteria), vetro montato (per la scheda Vetri), ricambio in mano. Oggi tre lavorazioni hanno la scheda con la foto, le altre tre no.
- **Sequenza prima e dopo** dello stesso mezzo dallo stesso punto (segnare il punto a terra col nastro), stessa ottica: sabbiato, fondo, verniciato, finito.
- **Le cabine** vuote e illuminate, con le misure: sono la prova delle capacità.
- **L'insegna e il cancello** di Via Levico 20, per chi arriva col carrellone.

## Pagine che il sito nuovo dovrà avere

Nella proposta i link del menu e del piede puntano alle sezioni della home. Nel sito vero: una pagina per lavorazione (`lavorazioni/sabbiatura-garnet/`, `fondi-e-vernici/`, `vetroresina-e-plastica/`, `carpenteria/`, `vetri/`, `consulenza/`), `lavori/`, `chi-siamo/`, `contatti/`, `privacy/`, `cookie/`. Da togliere dal sito di oggi: l'articolo di prova "Ciao mondo!" e la scheda Consulenza doppia (`-2`).

Niente newsletter: servizio su richiesta, senza notizie, fiere, cataloghi o clienti privati da informare.

## Licenze

- **Carattere**: Archivo (Omnibus-Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero, servito da `sito/fonts/` (licenza in `sito/fonts/OFL.txt`).
- **Foto**: tutte di Nord Service SRL, scaricate da nordservice.net il 24/10/2026 (`assets/CREDITI.md`). Nessuna foto di repertorio, nessuna immagine generata, nessuno scontorno, nessun disegno. I segnaposto Unsplash in `assets/esterne/` non sono usati. Le sei foto di repertorio del sito di oggi (provenienza ignota) sono escluse.
