# Berto Guerrino: proposta di nuova home

Proposta non richiesta, solo la home. Nessun contatto con l'azienda, niente pubblicato.

- Pagina: `sito/index.html` con `sito/img/` (solo le immagini usate, JPEG alla loro misura) e `sito/fonts/` (Anybody, con `OFL.txt`). Versione "livello professionale" del 3/11/2026, con il ritocco finale dopo il controllore e le prove dei clienti tipo (che cosa è cambiato: `screenshot/home/NOTA.md`, "Ritocco finale"; la pagina prima del ritocco è in `_prova/index-prima-del-ritocco-finale.html`); la home precedente ("Il pezzo giallo, in scala") è in `_prova/versione-1-originale/`.
- Screenshot: `screenshot/home/` (`home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` da "Orari e contatti" al piede, prime schermate a 320, 768, 1024, 1920), tutti all'ora simulata martedì 3/11/2026 alle 10. Scelte, regole e controlli in `screenshot/home/NOTA.md`, sezione "Livello professionale".
- Rifare tutto: `bash _prova/script/build_finale.sh` (immagini, screenshot, controlli delle 15 regole, prove d'uso; i file temporanei vanno in `_prova/tmp-finale/` e si cancellano alla fine). Un'altra ora: `sito/index.html?ora=2026-11-08T10:00`.
- Aperta come file://, la console può mostrare un avviso CORS sulla `preload` del carattere: è atteso, il carattere si carica comunque.
- Analisi con le fonti: `01-analisi.md`; scheda d'uso e d'identità: `_prova/uso/SCHEDA.md`.

## Il modulo va collegato

Il modulo "Richiesta di prezzo o informazioni" oggi **non invia nulla**: compone un'e-mail (mailto) a bertopd@libero.it con oggetto "tipo: macchina, nome" e tutti i campi, e la apre nel programma di posta di chi lo usa. Dopo il clic mostra anche il testo pronto da copiare, con l'indirizzo e il telefono, per chi usa la webmail e non ha un programma di posta: è un ripiego, non un invio. Prima di pubblicare va collegato a un servizio (per esempio il modulo del gestionale del sito, Formspree o un piccolo script sul server), con:
- l'indirizzo che riceve le richieste (vedi sotto, quale e-mail);
- la casella del consenso privacy e il testo dell'informativa;
- la possibilità di allegare foto della targhetta o del pezzo e disegni: al collegamento si aggiunge `<input type="file" name="allegati" accept="image/*,.pdf" multiple>` al posto del riquadro "allegatele all'e-mail che si apre" (oggi un mailto non può portare allegati; è la riserva della regola 14);
- una risposta automatica con i tempi ("vi richiamiamo entro..."), se Berto la vuole dare.

## Da chiedere o confermare con Berto

In pagina ci sono solo fatti di `01-analisi.md` e di `_prova/uso/SCHEDA.md`. Restano da confermare:

- **Forma giuridica**: in pagina "S.a.s." (testata del sito di oggi), ma il dominio e coobiz dicono ancora "snc".
- **P.IVA 02570660288**: in pagina (piede), ma presa da coobiz e registroaziende, non dal loro sito. REA, PEC e capitale sociale non trovati: non in pagina.
- **E-mail**: in pagina solo bertopd@libero.it (anche nel modulo). Da scegliere tra libero.it, tin.it e gmail.com; meglio un indirizzo sul dominio.
- **Orari**: in pagina lun-ven 8-12 e 14-19, sab 8-12, domenica chiuso (Google e Nextdoor coincidono). Da confermare, con le **chiusure estive**, le ferie di Natale e il **patrono di Saonara** (oggi lo stato conosce solo i festivi nazionali e Pasquetta). Se l'officina ha orari diversi dal negozio, vanno scritti a parte.
- **Fax 049 8791081**: in pagina; dire se si usa ancora.
- **Ingresso accessibile in sedia a rotelle**: in pagina, viene da coobiz.
- **MOD. 80 dello sterrapiante**: in pagina "40/68 HP" (scheda italiana) anche nel paragrafo inglese; le schede inglese, tedesca e francese dicono 40/65.
- **Macchine ancora in produzione**: le otto in pagina più rimorchio, trattorino, bancali e materiale per l'innesto; il numero "12 macchine e attrezzature per vivai nel nostro catalogo" (fascia dei numeri) conta le schede del sito di oggi, compresi bancali e materiale per l'innesto: confermare il numero e quali sono costruite da loro. Il "gruppo irrorazione" e lo "sterrapiante laterale" dei video non hanno una scheda.
- **Scalzapneus**: in pagina SC 1 265 kg e SC 2 455 kg, senza la potenza del trattore (non è nella scheda).
- **Officina e marchi**: chi ha un tosaerba Stihl o una macchina comprata altrove vuole sapere se la riparano. Chiedere la regola vera, con le loro parole ("Stihl: vendita e assistenza"? "riparate anche macchine comprate altrove" o "solo macchine vendute da noi"?) e come si porta la macchina (in negozio negli orari, su appuntamento, ritiro a domicilio). Oggi in pagina c'è solo l'invito "Per una macchina comprata altrove, chiamateci prima."
- **Marchi**: l'elenco degli 11 concessionari è del 2021; Honda li elenca ancora oggi ("Vendita e Assistenza", pagina S39219). Stihl, Goldoni, Grin e gli altri da confermare uno per uno; dire se si possono usare i loghi dei marchi (oggi i nomi sono solo scritti).
- **Vendita diretta in Italia e all'estero**: in pagina (frase di Nextdoor). Chiedere in quali paesi; se lo confermano, i paesi vanno nella sezione Azienda e nel paragrafo inglese.
- **Recensioni**: in pagina il 4,4 su 58 recensioni di Google e tre frasi vere, senza nome. Per la regola delle prove servono nome e comune di chi le ha scritte, con il loro permesso (o il widget ufficiale di Google), e il voto aggiornato al momento della pubblicazione.
- **Numeri dell'azienda**: in pagina quattro (1961, 12, 11, 4,4). Per arrivare a 6-8 numeri veri, come nei riferimenti: addetti, metri quadri di officina e magazzino, macchine costruite in tutto, paesi in cui hanno venduto.
- **Clienti e lavori con il nome** (regole 10 e 11, oggi non superate): chiedere tre vivai che usano le macchine Berto, con il comune, l'anno e la macchina, e il permesso di nominarli; con una foto della macchina al lavoro da loro diventano la sezione "Lavori".
- **Certificazioni, marcatura CE, brevetti**: nessuna nelle fonti, nessuna in pagina. Le "attrezzature brevettate" di Nextdoor: quali e quale brevetto.
- **Traduzioni**: i paragrafi in inglese, tedesco e francese sono una prima stesura della proposta (fatti presi dalla pagina italiana): da far rileggere, o da sostituire con i testi del sito di oggi.
- **Storia**: chi era Guerrino Berto, che cosa è cambiato dal 1961; per la sezione Azienda.

## Foto da fare dal vero

Le foto in pagina sono tutte di Berto, prese dal sito di oggi: le foto in studio (724 px) e i fotogrammi della galleria (500x500; in pagina con una sola correzione del colore comune alle quattro, ma restano morbidi). Nessuna foto di repertorio, nessun disegno. Sono piccole: in pagina non sono mai ingrandite oltre la misura del file. Prima di pubblicare chiedere gli originali dei depliant; poi, in ordine:

1. **La sede col negozio, per prima** (serve al cliente del negozio, che è il visitatore più frequente): la facciata di via Caovilla 27/B con l'insegna e il piazzale con le macchine esposte, di mattina con il sole sulla facciata, orizzontale, almeno 3000 px; il banco del negozio con i ricambi; l'officina con un meccanico al lavoro su un tosaerba o una motosega (persone che guardano il lavoro, non l'obiettivo). Una di queste va nell'apertura al posto della zolla, o accanto.
2. **Fausto e Lorena Berto**, ritratto in negozio o davanti a una macchina gialla, per la sezione Azienda.
3. **Le macchine in campo, una per scheda**: ogni macchina al lavoro in un vivaio di Saonara tra novembre e marzo, luce bassa, stessa altezza di ripresa, quadrata o 4:3, almeno 2000 px; meglio ancora con il nome del vivaio (vedi "Clienti e lavori"). Con queste le schede diventano foto del lavoro e non della macchina.
4. **Le macchine in studio**, se si rifà il catalogo: fondale grigio chiaro freddo continuo, luce morbida dall'alto a sinistra, ombra a terra, vista di tre quarti come oggi, stessa distanza per tutte, 6000 px; lo sterrapiante nelle tre versioni con la stessa inquadratura; tre dettagli (vomere, attacco a tre punti, targhetta BERTO).
5. **La zolla** rifatta: il vomere che solleva la zolla con le radici, quadrata, almeno 2000 px, con lo spazio per il taglio 2:1 del telefono (oggi è un fotogramma 500x500, sul telefono ritagliato a 500x250).

Le foto in campo e quelle in studio devono poi fare una serie sola (regola 5): stesso fotografo, stessa stagione e luce, stessa correzione del colore.

## Licenze

- **Anybody**: Etcetera Type Co., Google Fonts, SIL Open Font License 1.1 (uso commerciale libero), servito dalla pagina; licenza in `sito/fonts/OFL.txt`.
- **Foto e logo di Berto**: dal loro sito; nella proposta solo come prova, per il sito vero serve il loro consenso.
- Nessuna foto di repertorio in pagina; le nove di `assets/esterne/` restano non usate (crediti in `assets/CREDITI.md`).

## Logo

Nessun vettoriale trovato: in pagina i ritagli del cartello giallo di `images/apertura.png` (524 px, mostrati a 120 e 168 px). Le lettere hanno bordo e ombra in rilievo, quindi un SVG ricostruito non sarebbe fedele. Chiedere il file originale a chi ha fatto l'insegna o i depliant.

## Pagine del sito nuovo (link della home)

`macchine/` (indice) e le schede `macchine/sterrapiante.html`, `scalzapneus.html`, `rincalzatrice-porta-innesti.html`, `rincalzatrice-primi-rami.html`, `fresatrice-multipla-alta.html`, `trapiantatrice-tt.html`, `agevolatrice.html`, `trincia-piragna.html`; `giardinaggio.html` (marchi e prodotti), `officina.html`, `azienda.html`, `privacy.html`, `cookie.html`. Le voci del menu portano alle sezioni della home; EN, DE e FR portano ai paragrafi in fondo alla home finché non ci sono le pagine nelle tre lingue. I video sono quelli del canale YouTube @lorenaberto328 (sterrapiante `wZaJq_-mrEM`, sterrapiante laterale `eyAJjiK4kPQ`, scalzapneus `kCI3bBWdKkc`, trapiantatrice `VNqg5tPYEBM`, rincalzatrice porta innesti `NBYQS-FzFFs`, primi rami `_W639llzCX0`, trincia Piragna `5b_3K-YZ2zk`): confermare con Berto che sono quelli giusti per ogni macchina.

## Newsletter

Niente newsletter: la pagina "Novità" è vuota dal 2021 e non ci sono fiere né cataloghi da annunciare. Se confermano che manderebbero le offerte di stagione: campo e-mail, bottone, casella del consenso privacy, collegata a un servizio.
