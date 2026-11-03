# Fratelli Zuin: proposta di nuova homepage

Proposta non richiesta di una nuova home per F.lli Zuin & C. snc (Padova Est): scavi e movimento terra, cassoni scarrabili, demolizioni, fognature e spurgo, lavori stradali, escavatori a risucchio. Solo la home. Nessun contatto con l'azienda, niente di pubblicato.

Versione di oggi: **metodo ibrido** del 3/11/2026. La prima schermata segue la sezione D di `_metodo/professionale/ALTO-LIVELLO.md`: modello F, la frase loro "In qualsiasi situazione e spazio" nel cielo della foto, un bottone. Sotto ci sono i contenuti della versione professionale su una griglia sola. Direzione in `_prova/alto/DIREZIONE.md`; cambiamenti, misure e problemi aperti in `screenshot/home/NOTA.md`. La versione professionale com'era è in `_prova/versione-pro/` (sito e screenshot). Scheda d'uso: `_prova/uso/SCHEDA.md`.

## Cosa c'è

- `sito/index.html`: la home, una pagina sola, senza librerie esterne. Si apre anche da file.
- `sito/img/`: solo foto e logo dal loro sito, in WebP con più larghezze (srcset); nessuna è mostrata oltre i suoi pixel.
- `sito/fonts/`: Fira Sans Extra Condensed 800 e Fira Sans 400 e 500 (sottoinsieme latino in woff2), con `OFL.txt`.
- `screenshot/home/`: home a 1440 e a 390 (intere e prima schermata), prime schermate a 1024 e 768, `chiusura-1440.jpg`, `NOTA.md`.
- `_prova/alto/`: `DIREZIONE.md`, `provini.jpg`, `script/foto.py` (trattamento e tagli), `script/screenshot.mjs` (screenshot), `misura-d.mjs` (soglie della sezione D, con l'esito in `esito-d.txt`), `concorrenti/` (Eberhard e Brandenburg a 1440).
- `assets/originali/`: riscaricata il 3/11/2026 dal loro sito con l'API `wp-json/wp/v2/media`, perché il riavvio l'aveva svuotata. Ho tolto le pale eoliche del tema e le foto di repertorio e di cronaca (`lavori.jpg`, `demolizioni.jpg`). `assets/esterne/` e le Unsplash di `CREDITI.md` non ci sono più e non servono.
- `01-analisi.md`: i fatti con le fonti e i voti delle foto.

## Il modulo di preventivo va collegato

Il modulo in home (nome, telefono, email, tipo di lavoro, indirizzo del lavoro, descrizione, per quando) oggi **compone un'email** a info@fratellizuin.it con oggetto "Richiesta di preventivo: <tipo>" e i campi compilati nel testo ("Per quando: da concordare" se non si sceglie), e chi scrive aggiunge le foto a mano. Al computer senza programma di posta il mailto non si apre: per questo nella sezione del risucchio l'indirizzo è scritto anche in chiaro. Per la pubblicazione va collegato a un servizio di invio (il modulo del CMS, oppure Formspree, Netlify Forms o simili) con: caricamento delle foto (2-3 immagini, fino a 10 MB), consenso privacy, risposta automatica a chi scrive, protezione dallo spam. Da decidere con l'azienda chi riceve le richieste e in quanto tempo risponde (una promessa come "entro 48 ore" si scrive solo se la danno loro).

## Da chiedere all'azienda prima di pubblicare

1. **Orari** d'ufficio e del piazzale (in pagina non ci sono: la regola 15 li vuole nel piede), e un **cellulare o WhatsApp per le urgenze**, se c'è.
2. **Zone servite**: l'elenco dei comuni (Padova, Vigonza, Noventa, Cadoneghe...?) per la sezione "Dove siamo" e il piede. Oggi non c'è nessun elenco, per non inventarlo.
3. **Misure dei cassoni e degli autocarri**: il sito `.it` dice "da 2 a 25 mc", il `.com` "da 3 MC a 18 MC". In pagina c'è 2-25 m³, dal sito principale. "30-250 q" (autocarri da 30 a 250 quintali, dal sito `.com`) è da confermare e nella home ibrida non c'è più.
4. **Spurgo e canal jet**: lo scrive il sito `.com` ("spurgo e il lavaggio con il sistema canal jet"). Va confermato che lo fanno ancora, e anche la vendita di materiali e il noleggio dei mezzi. Nella home ibrida spurgo e canal jet non ci sono: la riga è "Fognature" e il modulo ha "Fognatura". Se fanno pronto intervento, lo spurgo va in testata come voce a sé.
5. **SOA**: categorie, classifiche e scadenza, e il PDF dell'attestazione da mettere in "Per enti e imprese" come file scaricabile (come Eggentaler), e il nome dell'organismo SOA. Oggi in pagina ci sono la fascia delle qualifiche (Attestazione SOA, REA PD 82662, ATECO 42.11, senza loghi), la frase del loro sito e il bottone che chiede il documento per email. Con categorie e classifiche la fascia diventa più forte ("OG3 classifica ...").
6. **PEC** (non trovata), **fax** 049 6458813 ancora attivo?, **nome da mostrare** ("F.lli Zuin & C. snc" del sito, nel piede; la ragione sociale del registro "Fratelli Zuin snc di Zuin Antonio, Luigi, Andrea & C." è nei dati per gli enti).
7. **Anno**: il sito scrive "nasce nel 1946", il registro "Fondazione 1977" (la snc di oggi). In pagina "dal 1946" e "tre generazioni", come scrive l'azienda.
8. **Lavori con un nome** (regola 11): tre o quattro lavori recenti con committente o luogo, anno, due o tre numeri (metri di strada, m³ di scavo, giorni) e una foto ciascuno. Per i lavori storici (Foro Boario 1968-69, Azienda del Gas di Via Trieste, Prato della Valle) gli anni mancanti e le foto d'archivio.
9. **Recensioni e clienti** (regola 10): nessuna recensione in rete (Reteimprese e Pagine Gialle: nessuna). Se vogliono, chiedere ai clienti una recensione su Google; e i nomi di enti e imprese per cui lavorano, con il permesso di citarli.
10. **Numeri della Ditta**: quanti mezzi (autocarri, escavatori, escavatori a risucchio), quante persone (Atoka stima circa 16 dipendenti: non è in pagina finché non lo confermano).
11. **Dati e usi del risucchio**: profondità, portata, lunghezza del tubo, che cosa non aspira; e gli usi tipici che fanno davvero (scavi vicino a tubazioni e cavi, pulizia di silos, vasche e capannoni, aspirazione di inerti, fanghi e polveri), da scrivere in un elenco "Si usa per" solo quando li confermano. Oggi la pagina dice di chiederli al telefono.
12. **Foto**: va confermato che tutte quelle in pagina siano mezzi e cantieri loro: `pagina-iniziale-1` in apertura, `gallery3` (risucchio), `lavori-stradali-1000x800-1` e `pagina-iniziale-2` (serie). Le didascalie dicono che cosa si vede, non "Mezzi della Ditta". Vale in particolare per l'escavatore Fiat-Hitachi EX215 e il DAF dell'apertura, che l'inventario segnava "loro (probabile)". Servono anche il luogo e l'anno di ogni foto, perché le didascalie oggi non li hanno. Nell'ultima il cassone ha una scritta sul portellone ("F.LLI CAMION..."?): verificare che non sia un mezzo di un'altra ditta.
13. **Frasi** da far approvare. Nella home ibrida: "In qualsiasi situazione e spazio", presa dalla loro pagina Azienda e accorciata, che è la frase d'apertura e torna nel piede; le righe dei lavori, prese dai loro testi; "nella ragione sociale ci sono Antonio, Luigi e Andrea Zuin", dal registro; "Per cassoni, scavi e lavori piccoli si fa prima al telefono" e "Scriveteci il lavoro", scritte da noi. Dalla versione professionale: le righe brevi delle schede sono prese dai loro testi (`.it` e `.com`) e accorciate; "Scavi controllati e aspirazione di qualsiasi materiale" corregge la loro frase ("scavi controllati e ideali per aspirare"); "Cosa scriverci", "Per una richiesta bastano luogo, materiale, quantità approssimativa e data", "Portata, profondità di scavo e lunghezza del tubo: chiedetecele al telefono" e le didascalie delle qualifiche sono scritte da noi.
14. Quale dei due siti (`fratellizuin.it` o `.com`) è quello giusto.

## Foto

In pagina ci sono solo foto loro (`assets/originali/`), con un trattamento unico (`_prova/alto/script/foto.py`): livelli comuni ai tre canali contro la foschia, il 35% della correzione verso il neutro, una curva leggera, alte luci a 244, saturazione 0,88. I formati sono tre. La scena larga dell'apertura è `pagina-iniziale-1` a 2000, 1440 e 1024 px, con un taglio 4:3 sotto i 1024 px e uno verticale di 692 px (camion e braccio) sul telefono. Il risucchio `gallery3` è tagliato con il cielo sopra (1365x760, mostrato al massimo a 1280 px), per comporci il titolo. La serie dei lavori è di due foto in 3:2 (`lavori-stradali`, `pagina-iniziale-2`). Escono, dopo il giudice del 3/11/2026, i due dettagli del risucchio (`gallery4`, `gallery5`), l'autobotte `gallery2` (finché lo spurgo non è confermato) e `demolizioni`. Restano fuori `movimento-terra` (stessa scena dell'apertura), `gallery1` (metà è asfalto vuoto), `gallery6` e `1365-1024` (provenienza da confermare). Nessuna foto di repertorio, nessuna immagine generata, nessun disegno. La frase d'apertura sta nel cielo della foto, in alto a destra: se la foto cambia, va rimessa dove il fondo è libero.

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

- **Fira Sans Extra Condensed** e **Fira Sans** (The Mozilla Foundation e Telefonica S.A.), SIL Open Font License 1.1: uso commerciale libero. Il sottoinsieme latino è fatto con `pyftsubset` dai TTF di google/fonts e servito da `sito/fonts` con `OFL.txt`. Sofia Sans, quella indicata nel capitolo 5, è già in 3 home; Archivo, della versione di prima, è fuori catalogo.
- **Foto e logo dell'azienda**: dal loro sito, usati solo per la proposta.

## Newsletter e social

- **Newsletter: no.** L'azienda non ha novità, cataloghi o eventi da comunicare; si chiama per un preventivo.
- **Seguici: no.** Nessun profilo social esiste (né nel codice del sito né in rete).
