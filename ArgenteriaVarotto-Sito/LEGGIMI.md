# Argenteria Varotto Alfredo: proposta di nuova home

Proposta non richiesta, solo la home. Niente è stato inviato all'azienda né pubblicato.

- Pagina: `sito/index.html`, con `sito/img/` e `sito/fonts/`. Si apre anche da file.
- Screenshot e nota di progetto: `screenshot/home/` (`NOTA.md` spiega idea, caratteri, colori, gesto, foto e controlli).
- Rigenerare tutto: `bash _prova/script/build_finale.sh` (immagini `finale_img.py` con lo scontorno ad alfa di `alfa.py`, sorgente della pagina `pagina.html`, tagli `finale_tagli.py`, misure `finale_misura.mjs`, prova del selettore `finale_gesto.mjs`; `prova_alfa.py` mostra in rosso i buchi chiusi da togliere quando si scontorna una foto nuova).
- Ultimo passaggio (2 novembre): fondo dal blu del marchio, prima schermata e chiusura come banco di posa (parete, piano, titolo appoggiato sull'orizzonte), pezzi dello shop scontornati con la loro ombra. Il dettaglio è nella NOTA.
- Analisi con le fonti: `01-analisi.md`. Prototipi scartati e scelti: `_prova/home/a` (base della finale) e `_prova/home/b`.

## Dati da confermare con l'azienda (non sono a vista in pagina, o lo sono nella forma più prudente)

1. "Dal 1974": in pagina c'è "dal 1974" come nella testata di oggi ("Since 1974"); il testo Azienda dice "agli inizi degli anni '70". Quale preferiscono?
2. Chi è Luca Varotto rispetto ad Alfredo, e da quando l'impresa individuale Varotto & Co. di Varotto Luca ha preso il posto della ditta di Alfredo (CRIBIS le dà 11-20 anni).
3. A chi è intestato il punzone 364 PD, e se la produzione in Corso Stati Uniti è dell'impresa (l'attività registrata è "commercio all'ingrosso di metalli non ferrosi").
4. Quali lavorazioni si fanno davvero in casa (martello, tornio, cesello, incisione, argentatura galvanica) e se il laboratorio si può fotografare.
5. Se Sheffield e alpacca portano un loro marchio: oggi il selettore dice che non portano il titolo legale né il punzone 364 PD, e i punzoni compaiono solo su 925 e 800.
6. Royal Queen, Royal England, Sweet Home e TEN sono marchi registrati loro? Chi produce i pezzi Sheffield? I numeri 55, 46, 20, 129 e 4 sono le categorie del sito di oggi: vanno aggiornati se cambiano.
7. Il vassoio dell'apertura, il sottopiatto dei Marchi e l'alzata della chiusura sono foto dello shop: sono loro i diritti? Di quale marchio sono i tre pezzi (Royal Queen o Royal England)? Serve l'originale del vassoio ad almeno 2500 px di larghezza: quello dello shop è 1280 px e a 1160 px CSS sugli schermi 2x l'incisione si ammorbidisce.
8. Orari di apertura (non pubblicati, quindi non in pagina) e se ricevono privati in sede.
9. PEC e REA (non trovati; il capitale sociale non è previsto per un'impresa individuale): se vogliono, vanno nella riga legale.
10. Fiere: la pagina di oggi è vuota, quindi "Fiere" non è nel piede. Partecipano ancora (Homi, Ambiente, Vicenzaoro)? Se sì, una data con città e stand è il contenuto più forte da aggiungere.
11. Social: Facebook (facebook.com/varottostore) e Pinterest (pinterest.it/lucavarotto) sono dello shop Varottostore e nel piede sono scritti così. Vanno tenuti nel sito del marchio? Instagram (instagram.com/varottostore) non è verificato e non è in pagina.
12. SenoCap: citarlo nel sito nuovo o lasciarlo su senocap.com?
13. Paesi dell'export e una frase vera sui clienti (gioiellerie, hotel), se si può dire.
14. Il colore della pagina viene dal blu del loro marchio (#00265a) molto diluito: va bene come colore della casa? Se hanno un blu ufficiale (Pantone o codice del catalogo stampato), si aggiorna in tre righe del CSS.

## Newsletter

È nel piede (email, Italiano o English, consenso privacy) perché esiste già sul sito di oggi e promette nuovi articoli, sconti e promozioni. **Non funziona finché non si collega a un servizio**: Brevo o Mailchimp con doppio consenso (doppio opt-in) e due liste, italiano e inglese. Oggi il modulo non invia nulla: al clic mostra solo un messaggio. Il testo del consenso va allineato alla nuova informativa privacy (quella di oggi cita ancora il D.Lgs. 196/2003).

## Pagine del sito nuovo (destinazioni dei link della home)

| Link | Pagina |
|---|---|
| Storia | `storia/` |
| Il laboratorio, I punzoni | `laboratorio/`, `laboratorio/#punzoni` |
| Varotto Alfredo, Royal Queen, Royal England, Sweet Home, TEN | `collezioni/varotto-alfredo/`, `collezioni/royal-queen/`, `collezioni/royal-england/`, `collezioni/sweet-home/`, `collezioni/ten/` |
| Posate (linee Inglese, Barocco, Cardinale, Impero, Mauriziano, Perles, Regina Anna, San Marco, Floreale) | `posate/` |
| Riparazione e argentatura | `riparazione/` |
| Hotel e ristoranti | `hotel-ristoranti/` |
| Liste nozze e bomboniere | `liste-nozze-bomboniere/` |
| Area clienti (proposte d'ordine dei rivenditori) | `area-clienti/` |
| Privacy, Cookie | `privacy/`, `cookie/` |
| English | `en/` |
| Fiere (solo se confermano) | `fiere/` |
| Shop online | https://www.varottoshop.com/ (esterno) |

Le voci del menu in alto e "Contatti" portano alle sezioni della home.

## Foto da rifare dal vero

Oggi in pagina ci sono tre foto dell'azienda (dallo shop, 1280 px al massimo, scontornate) e cinque segnaposto Unsplash con la didascalia "Foto indicativa". Una giornata di still life e due ore in laboratorio bastano a sostituirle tutte. Il set è quello della pagina: un fondale chiaro per la parete (vicino a #F3F5F8) e un piano appena più scuro e freddo (vicino a #E2E8EF, carta o laminato opaco grigio azzurro), con l'orizzonte netto tra i due; così le foto nuove si scontornano poco o niente e l'argento riflette lo stesso colore della pagina.

1. **Apertura**: un pezzo loro in argento 925 (un vassoio inciso o una brocca martellata) con la stessa inquadratura del vassoio di oggi: visto di tre quarti dall'alto, circa 30 gradi, disteso sul piano grigio azzurro del set, luce morbida da un grande diffusore in alto a sinistra e pannello bianco di schiarita a destra, riflessi puliti senza finestre riconoscibili. File di almeno 3000 px di larghezza, pezzo largo quasi tutto il fotogramma e un po' d'aria sopra.
2. **Macro del punzone 364 PD impresso**, e degli altri due accanto, a luce radente da un lato (una sola lampada bassa), con un obiettivo macro 1:1: è la prova dell'idea e può stare nel selettore o nella pagina Laboratorio.
3. **Selettore dei titoli**: la posata Inglese nei quattro metalli (argento 925, argento 800, Sheffield, alpacca), stessa inquadratura, stessa luce e stessa scala, sul piano del set, formato quadrato. Sostituisce calice, cucchiaio, salsiera e forchette.
4. **Laboratorio** (per la sezione "Lavorato a mano, tutto a Padova", oggi solo testo): una foto a tutta larghezza di mani al lavoro su un pezzo d'argento (martellatura, cesello o lucidatura al tornio), luce di finestra laterale, fondo del laboratorio non troppo scuro, niente orologi o gioielli al polso. Formato 21:9 o 2:1.
5. **Riparazione**: mani che lucidano o riargentano un pezzo d'argento loro (meglio un vassoio o una posata che si riconoscono), verticale 4:5. Sostituisce la foto di Burke (pulitrice, segnaposto).
6. **Chiusura**: un pezzo d'argento in piedi e diverso da quello dell'apertura (una caffettiera, un candelabro o l'alzata di oggi in 925), fotografato davanti all'orizzonte del set con l'orizzonte a metà altezza del pezzo, ripresa quasi frontale. Sostituisce l'alzata dello shop.
7. **Marchi**: il sottopiatto va bene come segnaposto; meglio un pezzo Royal Queen o Royal England fotografato come il punto 1.
8. **Selettore**: il calice di Wales (925), il cucchiaio di Kumpan (800), la salsiera di Cook (Sheffield) e le forchette di Tewari (alpacca) sono segnaposto fino alla foto 3.

## Licenze

- Caratteri: Boska (Fontshare, ITF Free Font License 2.0, uso commerciale gratuito, `sito/fonts/FFL.txt`); Rethink Sans (Google Fonts, SIL Open Font License 1.1, `sito/fonts/OFL-RethinkSans.txt`). Serviti dalla pagina, nessuna richiesta a server esterni.
- Foto Unsplash: Unsplash License, verificata sulla pagina di ogni foto il 24/10/2026 (Wales e Burke riverificate il 02/11/2026); autori e link in `assets/CREDITI.md`. Sono segnaposto per la proposta.
- Foto dello shop e loghi: materiale dell'azienda, diritti da confermare (punto 7).

## Loghi

- In pagina c'è il PNG originale (`assets/originali/logo-varotto-alfredo-130x153.png`, contenuto 75x96 px) portato al colore inchiostro e mostrato a 48 px di altezza, cioè un 2x pieno: regge, ma serve il **vettoriale** (SVG, PDF o AI) per il sito vero e per il favicon, che oggi manca.
- Non l'ho ricostruito in SVG: il segno a onde e le lettere con grazie di "ARGENTERIA" a 130 px non danno abbastanza dettaglio per un ridisegno fedele.
- I tre punzoni sono ridisegnati in SVG dalle GIF del sito (`logo-punzone-364PD.gif`, `logo-punzoni-925-800.gif`, `logo-scritta-varotto-alfredo-168x29.gif`). La forma è fedele, ma il carattere è Rethink Sans: con il punzone vero o un file ad alta definizione si possono rifare identici.
