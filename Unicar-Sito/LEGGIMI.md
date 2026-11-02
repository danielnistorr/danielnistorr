# Unicar: proposta di nuova home

Proposta non richiesta di una nuova homepage per Unicar srl (assistenza carrelli elevatori, via Canada 12, Padova). Solo la home.

- Pagina: `sito/index.html` con `sito/img/` e `sito/fonts/`; si apre direttamente nel browser.
- Screenshot: `screenshot/home/` (home-1440, home-1440-prima-schermata, home-390, home-390-prima-schermata, chiusura-1440) e la nota di progetto `screenshot/home/NOTA.md`.
- Analisi con le fonti: `01-analisi.md`. Giudizio sui prototipi: `_prova/giudizio.json`.
- Per rifare tutto: `sh _prova/script/build_finale.sh`.
- Prove: `node _prova/script/finale_prova.mjs` (promemoria con clic, frecce e tocco, menu, piede), `node _prova/script/finale_larghezze.mjs` (scorrimento orizzontale da 320 a 2560, impaginazione dell'apertura, collegamenti), `node _prova/script/finale_viste.mjs` (larghezze di confine e righello, scrive in `_prova/tmp-finale/`, da cancellare).

## Da confermare con Unicar (non messo in pagina, o messo solo nella forma sicura)

- **Prima di tutto**: se Unicar esiste ancora come società a sé. La P.IVA 01014160285 non risulta attiva nel VIES (24/10/2026), Cami2 è in maggioranza del Gruppo Selini dal 5/11/2024 e il furgone del service porta la livrea Toyota e Cami2. Se Unicar è stata fusa in Cami2, la proposta va rivolta a Cami2.
- "Messa in funzione entro 24 ore dalla chiamata": è nel loro testo del 2012. Non è in pagina; se lo confermano, può tornare come titolo ("In funzione entro 24 ore dalla chiamata") e "Consulenti, più che riparatori" passa alla chiusura.
- Zona degli interventi: in pagina "Padova e provincia" (dal loro testo); se arrivano anche a Venezia, va detto.
- Se sono ancora assistenza autorizzata BT e Cesab, cioè Toyota Material Handling; quanti furgoni e tecnici ha oggi Unicar da sola (12 mezzi nel 2012).
- I numeri del gruppo in pagina sono di Cami2 e Unicar insieme (cami2.it/azienda/: 25 tecnici esterni con furgone, circa 3500/4000 carrelli dei clienti tra Padova e Venezia): in pagina sono detti "delle due aziende insieme"; vanno riconfermati.
- La metratura della sede: in pagina "oggi di oltre 4000 mq" (cami2.it/azienda/); la pagina storia di Cami2 dice che nel 2009 la sede è arrivata a 3000 mq. Va confermato il dato di oggi.
- Se fanno ancora la formazione dei carrellisti e con quale ente; le certificazioni di Unicar (quelle trovate sono di Cami2: ISO 9001, Toyota A.S.E.C., OHSAS).
- Anno di costituzione (stima intorno al 1982, non in pagina), orari dell'officina, PEC, un numero per le emergenze: non trovati, non in pagina. Se ci sono gli orari, vanno nella chiusura sotto l'indirizzo.
- Il promemoria riprende la loro "Nota informativa" sull'art. 71 del D.Lgs. 81/2008 (funi e catene ogni tre mesi, tagliando annuale, registro conservato tre anni): il testo e il calcolo vanno fatti rileggere a loro prima della pubblicazione.
- Il link "Vendita e noleggio (cami2.it)": se nel sito nuovo vendita e noleggio restano un rimando a Cami2.

## Foto da rifare dal vero (una mattina in via Canada)

Tutte le foto della home sono segnaposto tranne la sede, che è loro ma piccola (in pagina un taglio di 455 x 249 dalla striscia di 939 x 249, mai ingrandito). L'apertura è un segnaposto a tutti gli effetti: un carrello Toyota qualunque, usato, da Unsplash. È progettata perché ci vada il loro.
1. **Il carrello dell'apertura** (oggi Reding, Unsplash): un carrello appena revisionato in officina Unicar, pulito, fotografato intero (montante, cabina, contrappeso e ruote dentro l'inquadratura, con margine), di tre quarti da dietro come quello della pagina, a 1,2 m da terra, parcheggiato dentro una corsia gialla vera del loro pavimento, su fondo il più possibile neutro (un muro chiaro o il cielo coperto), luce diffusa del mattino, obiettivo 50-85 mm per non deformare, ripresa a 24 MP o più. Serve anche uno scatto con il solo fondo per scontornare. Con i vetri della cabina chiusi e puliti si evita il vetro fumé ricostruito. Se possibile un Toyota o un BT di un cliente, senza adesivi di altri concessionari.
2. **L'officina** (oggi Yurtman, Unsplash, in piccolo): un tecnico Unicar in tuta da lavoro sul montante o sulle catene, mani e attrezzo in primo piano, luce naturale dai lucernari, formato orizzontale 4:3 almeno 3000 px di lato.
3. **La sede** (oggi un taglio della striscia del loro vecchio sito): la palazzina di via Canada con l'insegna UNICAR, i furgoni dell'assistenza allineati sul piazzale, cielo sereno o coperto chiaro, panoramica orizzontale ad almeno 4000 px di lato; per la chiusura serve un taglio 3:2 di almeno 2000 px sulla palazzina con l'insegna UNICAR, che in pagina potrà crescere fino a metà larghezza.
4. Per le altre pagine: il magazzino ricambi, un furgone attrezzato aperto, il pavimento d'officina con la corsia gialla.

## Licenze

- Foto Unsplash (Reding `r4Y_VNKzAbw`, Yurtman `GjmQzjPuF30`): Unsplash License, uso commerciale libero, attribuzione non obbligatoria; dettagli, ritocchi e avvertenze sui marchi in `assets/CREDITI.md`.
- Sede (`assets/originali/testata/007.jpg`) e logo: materiale del loro sito, da usare con il loro permesso.
- Carattere Archivo: SIL Open Font License 1.1 (`sito/fonts/OFL.txt`), servito dalla pagina.

## Logo

C'è solo il PNG 241 x 100 del vecchio sito (`assets/originali/logo-unicar-241x100.png`), usato ritagliato ai bordi e mostrato a 96 px in testata e nel piede (densità 2,5x). Non è ricostruito in SVG perché la versione piatta perderebbe il rilievo grigio delle lettere. Serve il vettoriale originale; manca anche la favicon.

## Pagine che il sito nuovo dovrà avere (i link della home oggi puntano alle sezioni)

- Servizi: Assistenza e riparazione, Manutenzione programmata, Batterie e caricabatterie, Controlli di sicurezza, Formazione carrellisti.
- Ricambi.
- Chi siamo, Dove siamo (con la mappa), Normative e controlli (la nota sull'art. 71 riscritta).
- Privacy (`privacy.html`) e Cookie (`cookie.html`), riscritte per il GDPR (l'informativa di oggi cita ancora il D.Lgs. 196/2003): i due link del piede puntano già a questi file.
- Vendita e noleggio: link esterno a cami2.it.

## Newsletter

Non c'è e non serve: lavorano solo per aziende, non comunicano novità, fiere o cataloghi e non hanno clienti privati. Il gesto utile per i clienti è il promemoria dei controlli, che scarica le date nel calendario.
