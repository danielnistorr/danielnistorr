# Bottega dell'Arte: proposta di nuova home

Proposta non richiesta di una nuova homepage per Bottega dell'Arte (falegnameria di Mauro Nosarini e Giuliano Saibene, laboratorio in Via Levico 18 a Mestrino). Solo la home. Niente è stato inviato all'azienda né pubblicato.

## Dove sono le cose

- `sito/index.html`: la home finale "livello professionale" (3 novembre 2026), statica (si apre con file:///). `sito/img/` solo le immagini usate, `sito/fonts/` i caratteri con le licenze.
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, e `NOTA.md` (sezione "Livello professionale": esito delle 15 regole, compiti della scheda, controlli, licenze).
- `_prova/script/build_finale.sh [--immagini]`: rifà immagini (`pro_img.py`), screenshot (`pro_scatti.mjs`), controlli delle 15 regole (`pro_controlli.mjs`) e posizioni dei compiti della scheda (`pro_misura.mjs`). `_prova/script/ritocco_finale.py`: le sostituzioni del ritocco finale del 3/11/2026, già applicate alla pagina (non va rilanciato).
- `_prova/versione-1-originale/`: la home precedente (portone a tutta altezza con Prima/Dopo), pagina e screenshot. `_prova/uso/SCHEDA.md`: chi apre il sito e cosa ci viene a fare. `_prova/crawl/progetti.txt`: i testi delle 22 schede del sito di oggi (wp-json, 3/11/2026).
- `01-analisi.md`: fatti con fonti, voti delle foto, direzioni e riferimenti. `_prova/home/a` e `b`: i due prototipi.

## Il modulo da collegare

Il modulo "Cosa possiamo fare per te?" in fondo alla home oggi **non invia nulla**: compone un'email (mailto a info@bottegadellartesnc.it con oggetto "Richiesta dal sito: tipo di lavoro, nome" e i campi nel testo) che il visitatore spedisce dal suo programma di posta, allegando lui le foto. Prima di pubblicare va collegato a un servizio di invio (per esempio il Contact Form 7 che hanno già su WordPress, o un servizio di moduli), con: campo allegato per foto e disegni (JPG, PDF, fino a qualche MB), consenso privacy con il link a iubenda, protezione dallo spam, risposta automatica. Lo stesso vale per i tre bottoni "Manda una foto o un disegno", "Manda una foto del pezzo" e l'email "Disegno da preventivare", che oggi aprono un'email con l'oggetto già scritto.

## Da chiedere all'azienda (per il livello professionale)

- **Orari della bottega**: l'unica fonte è oraridiapertura24 (lun-ven 8:00-19:30, sabato e domenica chiuso), non ufficiale. In pagina c'è solo "Chiamate prima di passare". Se li confermano, vanno in tabella nella scheda "Dove siamo" (giorni a sinistra, orari a destra), nella prima schermata sotto l'indirizzo e nel piede. Se ricevono solo su appuntamento, scriverlo.
- **WhatsApp**: se si possono mandare le foto ai 347 di Mauro o Giuliano su WhatsApp (le foto del sito arrivano da WhatsApp). Se sì, il bottone "Manda una foto" può aprire WhatsApp.
- **Recensioni**: nessuna trovata (la scheda Google "Falegnameria Bottega Dell`Arte" ha un captcha, prontoimprese e reteimprese a zero). Chiedere il link della scheda Google e il permesso di riportare 2-3 recensioni vere con nome e comune; oppure 2-3 frasi di clienti con il loro consenso. Non ne è stata inventata nessuna.
- **Nomi dei clienti**: se si possono scrivere Pasticceria Cadario e il nome del centro estetico di Lissaro (il marchio è sul banco della reception); oggi in pagina sono "una pasticceria vicino a Bolzano" e "un centro estetico a Lissaro", e le foto scelte non mostrano né l'insegna né il marchio (banco vetrina, sgabelli, mobile con il lavabo). Con il permesso si possono usare anche le foto con l'insegna. Serve poi l'**anno di ogni lavoro** (le schede del sito sono del 2020, che non è la data del lavoro): la regola 11 lo chiede e oggi manca in tutti e tre. Utili due o tre dati in più (metri, pezzi, tempi di consegna).
- **I quattro numeri**: "40 anni di esperienza" è scritto sul loro sito (2018-2020): va riconfermato o aggiornato. "2 soci" con la posa curata da loro viene da `/serramenti/` ("senza l'utilizzo di personale esterno ed occasionale"). "22 lavori documentati" e "8 con il colore fatto al campione" sono contati sulle loro schede. I due numeri da aggiungere, se confermati in visura, sono l'**anno di fondazione** (2004 secondo companyreports) e le **persone in bottega** (il registro dice da 2 a 5); utili anche i lavori all'anno e i comuni dove lavorano di più.
- **Zone servite**: non dichiarate; chiedere i comuni dove posano di solito (Mestrino, Rubano, Selvazzano, Padova...) e se vanno fuori provincia.
- **Fornitori e marchi**: se sono ancora rivenditori o installatori Dierre, quali marchi di vetrocamera, ferramenta e vernici usano, e i **loghi in versione monocromatica** (Dierre e gli altri fornitori) con il permesso di mostrarli: servono per trasformare la fascia "Materiali e marchi che usiamo", oggi in solo testo, in una fascia di loghi con la didascalia di che cosa sono (come Wilson: "Fittings and fixtures from Reece"). Con le recensioni, è quello che manca per la regola 10 (almeno tre tipi di prove). Anche le certificazioni dei serramenti (la scheda delle finestre parla di "certificazione energetica", quella dei portoncini di "portoncini certificati").
- **Macchine** a controllo numerico: quali, se vogliono nominarle.

## Dati da confermare (fuori dalla pagina o da verificare prima di pubblicare)

- **Forma giuridica.** "Snc" su VIES, nel dominio, su reteimprese, Pagine Bianche e Pagine Gialle ("Bottega dell'Arte S.n.c. di Nosarini Mauro e Saibene Giuliano", come ora nel piede); "S.R.L." su companyreports. Va controllato in visura.
- **Sede legale** Via Vangadizza 28, 35030 Rubano (VIES la scrive "Vagandizza"); confermare che il laboratorio resta in Via Levico 18 a Mestrino.
- **REA** "PD 344749" (companyreports): non messo nella riga legale finché non c'è la visura. Capitale sociale e PEC non pubblici. Orari del laboratorio non pubblicati, quindi assenti dalla chiusura: se ci sono, vanno aggiunti sotto l'indirizzo.
- **Anno di fondazione 2004**: non in pagina. **"40 anni di esperienza"**: ora in pagina (apertura e numeri) perché è una frase del loro sito; va riconfermata.
- **Il portone prima e dopo.** Che `Port.4` e `Port-3` siano lo stesso portone (lo dicono la stessa scheda e le stesse specchiature) e che il cliente lo permetta.
- **Le porte a vetri piombati** (`porte_restaurate.jpg`): non sono più in home.
- **Palazzo del Bo.** Se si possono nominare in home l'Università di Padova, il Palazzo del Bo e Gio Ponti; anno e lavori esatti; che le foto della bussola d'ingresso (`universita02`) e dei ponteggi (`universita01`, con loro due al lavoro) siano del Bo, come dice la scheda `progetti/universita-di-padova/`, e che si possano pubblicare.
- **Finiture.** In pagina ci sono solo vernice all'acqua, laccatura e gommalacca. Foglia d'oro e patinatura veneziana le cita la pagina Arredo, ma senza foto né lavori: vanno aggiunte solo se le fanno ancora.
- **Persone.** In pagina ci sono solo i due soci; il registro dice "da 2 a 5" dipendenti. La frase "disegnano, costruiscono e verniciano" non dice "da soli" per questo.
- **Macchine** a controllo numerico: citate in "Come lavoriamo" senza modello. Porte blindate Dierre: in pagina nella scheda "Finestre e porte" e nella fascia dei materiali; confermare che le montino ancora.
- Il nome della "nota falegnameria artigiana di Padova" dove hanno iniziato, se vogliono dirlo.
- Privacy: il link va alla policy iubenda di oggi (`iubenda.com/privacy-policy/16689485`); la Cookie Policy resta alla pagina di oggi.

## Pagine a cui puntano i link (il sito nuovo deve averle)

Stessi indirizzi del sito di oggi, così non servono redirect: `arredo/`, `serramenti/`, `restauri/`, `azienda/`, `progetti/` (Realizzazioni), `progetti/universita-di-padova/`, `progetti/pasticceria-bolzano/`, `progetti/centri-eststici/` (indirizzo di oggi, con il refuso), `cookie-policy/`. Nella proposta statica sono scritti in forma assoluta (`https://www.bottegadellartesnc.it/...`): il 3/11/2026 rispondono tutti 200, così chi prova la home con file:/// arriva a una pagina vera. Nel sito nuovo, sullo stesso dominio, possono tornare relativi. Le voci della testata portano alle sezioni della home (`#dove`, `#lavorazioni`, `#restauro`, `#lavori`, `#richiesta`); la pagina `contatti/` di oggi può restare, ma la home non la richiama più. La pagina `/testimonials/` di oggi, con testo finto in latino, va tolta subito.

## Scelte del piede

- Nessuna colonna Seguici: non hanno social.
- Niente newsletter: il sito è fermo al 2021, non hanno novità, fiere, cataloghi o collezioni, e il cliente privato torna dopo anni. Se in futuro vorranno raccontare i lavori finiti, si può aggiungere (campo email, bottone, consenso privacy, collegata a un servizio).

## Foto da rifare dal vero

Oggi sono tutte foto di telefono fatte al montaggio, con luci diverse (il flash sulla bussola del Bo, il sole a picco sul capannone, il cemento del laboratorio sotto il portone "prima"); in pagina hanno lo stesso trattamento colore ma restano una serie debole, ed è il motivo principale per cui la regola 5 non passa del tutto. Per la versione pubblicata serve un solo fotografo e una sola luce (luce di finestra laterale morbida, cavalletto, obiettivo normale 35-50 mm equivalenti, file a piena risoluzione, almeno 2400 px sul lato lungo), nei tre formati della pagina (16:9 e 4:3 orizzontali, 3:4 verticale):
1. **Mauro e Giuliano in bottega**, al banco o alla macchina, che guardano il lavoro (non l'obiettivo), e un ritratto dei due davanti al capannone con il furgone: è la foto che manca di più (la regola chiede persone o laboratorio in apertura).
2. **Il laboratorio** con le macchine e un pezzo in lavorazione; le mani con la gommalacca a tampone; un campione di colore accanto al pezzo (la colorazione al campione è in 8 schede su 22).
3. **Il sottoscala con la nicchia in ottone** (apertura): frontale, senza lampadario e pianta del cliente, nicchia accesa e luce del giorno bilanciate, in 3:4 verticale (apertura a 1440, oggi un taglio di 675x900 px) e in 16:9 e 4:3.
4. **Il portone prima e dopo** (sezione restauro): stesso punto di ripresa, frontale a metà altezza, porta intera e dritta, fondo neutro (oggi c'è il capannone con la bicicletta). Lo stesso per i prossimi restauri: diventa una serie.
5. **Una finestra vecchia restaurata e i suoi scuri**, a casa del cliente, prima e dopo (oggi c'è solo la portafinestra con gli scuri, 777 px di larghezza).
6. **Una cucina e un armadio a muro** finiti, in luce di giorno, per la scheda "Per la casa" (oggi c'è la libreria).
7. **Il Palazzo del Bo**, se l'Università lo permette: la bussola, le porte scorrevoli, la boiserie, a piena risoluzione e con luce ambiente, senza flash (oggi 700 x 500 px; la bussola nelle Realizzazioni è l'unica immagine ingrandita della pagina, del 10 per cento, per stare a metà pagina).
9. **I lavori per negozi e locali** (pasticceria, centro estetico), finiti e in luce di giorno, con il permesso del cliente: oggi la pasticceria è il banco vetrina e gli sgabelli, il centro estetico un mobile con il lavabo, scelti perché non mostrano insegne, marchi e prodotti di altri.
8. **La facciata della bottega** di giorno, con l'insegna leggibile e il portone aperto (oggi 1140 x 758).

## Licenze

- **Foto:** tutte dell'azienda, dal suo sito (`assets/originali/`, elenco in `assets/CREDITI.md`), usate solo per la proposta. Nessuna foto di repertorio, nessun segnaposto esterno, nessuna illustrazione, nessuna immagine generata (decisione del committente: dove non ci sono foto vere che reggono, nessuna immagine). Le foto Unsplash in `assets/esterne/` restano scaricate ma non sono usate. Da chiedere: il permesso di mostrare i lavori della pasticceria, del centro estetico e del Bo.
- **Caratteri:** Zodiak (Indian Type Foundry, Fontshare, ITF Free Font License, uso commerciale gratuito) e Schibsted Grotesk (Google Fonts, SIL Open Font License 1.1), serviti dalla pagina in `sito/fonts/`; dettagli in `sito/fonts/LICENZE.txt`.

## Logo

Usato il PNG originale `assets/originali/logo-bottega-arte-1014.png` (firma calligrafica marrone #6F3219), esportato a 400, 520 e 800 px per la testata e il piede a 2x; icona dal monogramma `logo-monogramma-B-512.png`. Non l'ho ricostruito in SVG: il tratto irregolare non verrebbe fedele. Va chiesto all'azienda il file vettoriale originale (AI, PDF o SVG).

## Segnali da IA

Nella versione professionale in pagina c'è "40 anni di esperienza" (frase del loro sito, `/azienda/`), da riconfermare; nessun anno di fondazione. Controlli in `screenshot/home/NOTA.md`, sezione "Livello professionale".
