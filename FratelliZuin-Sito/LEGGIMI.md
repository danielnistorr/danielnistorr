# Fratelli Zuin: proposta di nuova homepage

Proposta non richiesta di una nuova home per F.lli Zuin & C. snc (Padova Est): scavi e movimento terra, cassoni scarrabili, demolizioni, fognature e spurgo, lavori stradali, escavatori a risucchio. Solo la home. Nessun contatto con l'azienda, niente di pubblicato.

Versione di oggi: "livello professionale" del 3/11/2026, con il ritocco finale dopo il controllo del livello e le prove dei clienti tipo (cosa è cambiato: `screenshot/home/NOTA.md`) (regole in `_metodo/professionale/REGOLE.md`, famiglia S; scheda d'uso in `_prova/uso/SCHEDA.md`). La versione di prima (fondo giallo, "risucchio" a tutta pagina, foto Unsplash) è in `_prova/versione-1-originale/`.

## Cosa c'è

- `sito/index.html`: la home, una pagina sola, senza librerie esterne. Si apre anche da file.
- `sito/img/`: solo foto e logo dal loro sito, JPEG in più larghezze (srcset), nessuna ingrandita.
- `sito/fonts/archivo-latin-var.woff2` e `OFL.txt`: Archivo variabile, servito dalla pagina (licenza sotto).
- `screenshot/home/`: home a 1440 e a 390 (intere e prima schermata), chiusura e piede a 1440; `NOTA.md` con le scelte, l'esito delle 15 regole e i controlli.
- `_prova/script/build_finale.sh`: rifà tutto. Usa `pro_img.py` (immagini), `home-pro.html` (sorgente della pagina), `pro_shoot.py` e `pro_vista.mjs` (screenshot), `pro_controlli.mjs` (15 regole, prove d'uso, larghezze; esito in `_prova/pro_controlli.json`).
- `01-analisi.md`: fatti con le fonti, voti delle foto.

## Il modulo di preventivo va collegato

Il modulo in home (nome, telefono, email, tipo di lavoro, indirizzo del lavoro, descrizione, per quando) oggi **compone un'email** a info@fratellizuin.it con oggetto "Richiesta di preventivo: <tipo>" e i campi compilati nel testo ("Per quando: da concordare" se non si sceglie), e chi scrive aggiunge le foto a mano. Al computer senza programma di posta il mailto non si apre: per questo nella sezione del risucchio l'indirizzo è scritto anche in chiaro. Per la pubblicazione va collegato a un servizio di invio (il modulo del CMS, oppure Formspree, Netlify Forms o simili) con: caricamento delle foto (2-3 immagini, fino a 10 MB), consenso privacy, risposta automatica a chi scrive, protezione dallo spam. Da decidere con l'azienda chi riceve le richieste e in quanto tempo risponde (una promessa come "entro 48 ore" si scrive solo se la danno loro).

## Da chiedere all'azienda prima di pubblicare

1. **Orari** d'ufficio e del piazzale (in pagina non ci sono: la regola 15 li vuole nel piede), e un **cellulare o WhatsApp per le urgenze**, se c'è.
2. **Zone servite**: l'elenco dei comuni (Padova, Vigonza, Noventa, Cadoneghe...?) per la sezione "Dove siamo" e il piede. Oggi non c'è nessun elenco, per non inventarlo.
3. **Misure dei cassoni e degli autocarri**: il sito `.it` dice "da 2 a 25 mc", il `.com` "da 3 MC a 18 MC". In pagina 2-25 m³ (sito principale). Nelle cifre c'è anche "30-250 q", autocarri da 30 a 250 quintali, dal sito `.com` (letto nei risultati di ricerca): da confermare.
4. **Spurgo e canal jet**: lo scrive il sito `.com` ("spurgo e il lavaggio con il sistema canal jet"); confermare che lo fanno ancora, e anche la vendita di materiali e il noleggio mezzi.
5. **SOA**: categorie, classifiche e scadenza, e il PDF dell'attestazione da mettere in "Per enti e imprese" come file scaricabile (come Eggentaler), e il nome dell'organismo SOA. Oggi in pagina ci sono la fascia delle qualifiche (Attestazione SOA, REA PD 82662, ATECO 42.11, senza loghi), la frase del loro sito e il bottone che chiede il documento per email. Con categorie e classifiche la fascia diventa più forte ("OG3 classifica ...").
6. **PEC** (non trovata), **fax** 049 6458813 ancora attivo?, **nome da mostrare** ("F.lli Zuin & C. snc" del sito, nel piede; la ragione sociale del registro "Fratelli Zuin snc di Zuin Antonio, Luigi, Andrea & C." è nei dati per gli enti).
7. **Anno**: il sito scrive "nasce nel 1946", il registro "Fondazione 1977" (la snc di oggi). In pagina "dal 1946" e "tre generazioni", come scrive l'azienda.
8. **Lavori con un nome** (regola 11): tre o quattro lavori recenti con committente o luogo, anno, due o tre numeri (metri di strada, m³ di scavo, giorni) e una foto ciascuno. Per i lavori storici (Foro Boario 1968-69, Azienda del Gas di Via Trieste, Prato della Valle) gli anni mancanti e le foto d'archivio.
9. **Recensioni e clienti** (regola 10): nessuna recensione in rete (Reteimprese e Pagine Gialle: nessuna). Se vogliono, chiedere ai clienti una recensione su Google; e i nomi di enti e imprese per cui lavorano, con il permesso di citarli.
10. **Numeri della Ditta**: quanti mezzi (autocarri, escavatori, escavatori a risucchio), quante persone (Atoka stima circa 16 dipendenti: non è in pagina finché non lo confermano).
11. **Dati e usi del risucchio**: profondità, portata, lunghezza del tubo, che cosa non aspira; e gli usi tipici che fanno davvero (scavi vicino a tubazioni e cavi, pulizia di silos, vasche e capannoni, aspirazione di inerti, fanghi e polveri), da scrivere in un elenco "Si usa per" solo quando li confermano. Oggi la pagina dice di chiederli al telefono.
12. **Foto**: che tutte quelle in pagina siano mezzi e cantieri loro (`pagina-iniziale-1` in apertura, `movimento-terra-1000x800-1`, `gallery2`, `gallery3`, `gallery4`, `pagina-iniziale-2`, `demolizioni-1000x800-1`, `lavori-stradali-1000x800-1`); in particolare l'escavatore Hitachi e il DAF dell'apertura, che l'inventario segna "loro (probabile)". Nell'ultima il cassone ha una scritta sul portellone ("F.LLI CAMION..."?): verificare che non sia un mezzo di un'altra ditta.
13. **Frasi** da far approvare: le righe brevi delle schede sono prese dai loro testi (`.it` e `.com`) e accorciate; "Scavi controllati e aspirazione di qualsiasi materiale" corregge la loro frase ("scavi controllati e ideali per aspirare"); "Cosa scriverci", "Per una richiesta bastano luogo, materiale, quantità approssimativa e data", "Portata, profondità di scavo e lunghezza del tubo: chiedetecele al telefono" e le didascalie delle qualifiche sono scritte da noi.
14. Quale dei due siti (`fratellizuin.it` o `.com`) è quello giusto.

## Foto

In pagina solo foto loro (`assets/originali/`), con un trattamento unico (`_prova/script/pro_img.py`: livelli puliti, blu del cielo spenti del 45%, saturazione -15%, alte luci compresse a 240, bilanciamento appena freddo, tagli con il cielo attorno al 20%), in tre formati per vista: a 1440 4:5 (l'escavatore che carica il cassone, in apertura), 2:1 (il risucchio), 4:3 (le schede); sotto i 900 px la stessa scena dell'apertura in striscia larga e le schede in 3:2. `gallery1` (il parco autocarri) non è più in pagina. Nessuna foto di repertorio: le sei Unsplash della versione di prima sono state tolte dalla pagina (restano in `assets/esterne/`, vedi `assets/CREDITI.md`). Nessuna immagine generata dall'IA, nessun disegno.

### Da rifare dal vero (in ordine di importanza)

1. **Apertura: la squadra davanti ai mezzi**, in divisa, nel piazzale di Via Bassette, con due o tre autocarri con il timbro sulle portiere leggibile e un cassone rosso. Mattino presto o cielo coperto chiaro, niente ombre dure; obiettivo 35-50 mm da 10-15 m, camera ad altezza d'uomo; almeno 4000 px sul lato lungo, orizzontale e una verticale per il telefono. Sostituisce l'apertura di oggi (`pagina-iniziale-1`: mezzi al lavoro ma nessuna persona, luce di mezzogiorno con foschia) e il parco autocarri `gallery1`. Se possibile, tutta la serie nella stessa giornata e con la stessa luce: è quello che oggi il trattamento comune può solo avvicinare.
2. **Il risucchio al lavoro**: il mezzo di tre quarti dal lato del braccio con il tubo aperto su uno scavo vero (vicino a tubi o cavi) e un operaio; poi un dettaglio della bocca del tubo. Stessa luce della serie.
3. **Un cassone scarrabile piccolo** "della larghezza di un'automobile" in una via stretta o un cortile, mentre viene posato.
4. **Le schede, una foto per lavoro, stesso taglio 4:3**: scavo per un allaccio, demolizione con pinza, ritiro macerie, spurgo con l'autobotte, un cortile o passo carraio finito, una strada o rotatoria finita (anche con drone, mezzogiorno coperto). Le schede di strade, cortili e urbanizzazioni oggi non hanno foto.
5. **Ritratti** dei titolari e di chi risponde al telefono (per una futura sezione "squadra", regola A1 punto 6), luce naturale.
6. **Archivio di famiglia**: il DOGE, il Foro Boario, il Prato della Valle, digitalizzati a 600 dpi, con il permesso di pubblicarli.

## Pagine collegate dal piede

Oggi esistono solo come nomi: `privacy.html` e `cookie.html` (la cookie policy di oggi è dentro la privacy policy: va separata, e il banner deve chiedere un consenso vero, non "se continui a leggere accetti"). Tutti gli altri collegamenti della home portano alle sezioni della pagina.

## Logo

Esiste solo come PNG da scansione di un timbro ovale (765x463, bordi frastagliati): in pagina è ricolorato in nero #141414 (testata) e in bianco (piede), PNG a 2x; l'icona del browser è il timbro rosso a 64 px. Un SVG va ridisegnato a mano dal file originale (tipografia o carrozziere che dipinge i mezzi) e approvato dall'azienda.

## Licenze

- **Archivo** (Omnibus-Type), Google Fonts, SIL Open Font License 1.1: uso commerciale libero, file servito da `sito/fonts` con `OFL.txt`.
- **Foto e logo dell'azienda**: dal loro sito, usati solo per la proposta.

## Newsletter e social

- **Newsletter: no.** L'azienda non ha novità, cataloghi o eventi da comunicare; si chiama per un preventivo.
- **Seguici: no.** Nessun profilo social esiste (né nel codice del sito né in rete).
