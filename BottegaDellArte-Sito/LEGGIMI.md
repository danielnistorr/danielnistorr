# Bottega dell'Arte: proposta di nuova home

Proposta non richiesta di una nuova homepage per Bottega dell'Arte (falegnameria di Mauro Nosarini e Giuliano Saibene, laboratorio in Via Levico 18 a Mestrino). Solo la home. Niente è stato inviato all'azienda né pubblicato.

## Dove sono le cose

- `sito/index.html`: la home finale, statica (si apre con file:///). `sito/img/` solo le immagini usate, `sito/fonts/` i caratteri con le licenze.
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, e `NOTA.md` (idea, schermate, caratteri, colori, interazione, foto, controlli).
- `_prova/script/build_finale.sh`: rifà immagini, caratteri, screenshot e controllo dei segnali. Usa `finale_img.py` e `scatti_finale.cjs`.
- `01-analisi.md`: fatti con fonti, voti delle foto, direzioni e riferimenti. `_prova/home/a` e `b`: i due prototipi.

## Dati da confermare (fuori dalla pagina o da verificare prima di pubblicare)

- **Forma giuridica.** "Snc" su VIES, nel dominio e su reteimprese; "S.R.L." su companyreports. In pagina è scritto "Snc" come da VIES: va controllato in visura.
- **Sede legale** Via Vangadizza 28, 35030 Rubano (VIES la scrive "Vagandizza"); confermare che il laboratorio resta in Via Levico 18 a Mestrino.
- **REA** "PD 344749" (companyreports): non messo nella riga legale finché non c'è la visura. Capitale sociale e PEC non pubblici. Orari del laboratorio non pubblicati, quindi assenti dalla chiusura: se ci sono, vanno aggiunti sotto l'indirizzo.
- **Anno di fondazione 2004** e **"40 anni di esperienza"**: non messi in pagina. Se confermati, una data in home aiuta (per esempio nella frase dei soci).
- **Il portone prima e dopo.** Che `Port.4` e `Port-3` siano lo stesso portone (lo dicono la stessa scheda e le stesse specchiature) e che il cliente lo permetta.
- **Palazzo del Bo.** Se si possono nominare in home l'Università di Padova, il Palazzo del Bo e Gio Ponti; anno e lavori esatti; che la foto delle porte scorrevoli sia davvero del Bo (viene dalla scheda `progetti/universita-di-padova/`) e che si possa pubblicare. La didascalia "Porte scorrevoli, Palazzo del Bo, Università di Padova" va confermata.
- **Finiture.** Se foglia d'oro e patinatura veneziana si fanno ancora (sono nella riga delle finiture perché le cita la pagina Arredo).
- **Persone.** In pagina ci sono solo i due soci; il registro dice "da 2 a 5" dipendenti. La frase "disegnano, costruiscono e verniciano" non dice "da soli" per questo.
- **Macchine** a controllo numerico: quali, se vogliono citarle (oggi non sono in pagina). Porte blindate Dierre: se sono ancora rivenditori o installatori (oggi non in home).
- Il nome della "nota falegnameria artigiana di Padova" dove hanno iniziato, se vogliono dirlo.
- Privacy: il link va alla policy iubenda di oggi (`iubenda.com/privacy-policy/16689485`); la Cookie Policy resta alla pagina di oggi.

## Pagine a cui puntano i link (il sito nuovo deve averle)

Stessi indirizzi del sito di oggi, così non servono redirect: `arredo/`, `serramenti/`, `restauri/`, `azienda/`, `contatti/`, `progetti/` (Realizzazioni, archivio delle 22 schede, da creare), `progetti/universita-di-padova/`, `cookie-policy/`. Nella proposta statica i link relativi non portano a nulla. La pagina `/testimonials/` di oggi, con testo finto in latino, va tolta subito.

## Scelte del piede

- Nessuna colonna Seguici: non hanno social.
- Niente newsletter: il sito è fermo al 2021, non hanno novità, fiere, cataloghi o collezioni, e il cliente privato torna dopo anni. Se in futuro vorranno raccontare i lavori finiti, si può aggiungere (campo email, bottone, consenso privacy, collegata a un servizio).

## Foto da rifare dal vero

Oggi sono tutte foto di telefono fatte al montaggio. Per la versione pubblicata servono, con luce di finestra laterale morbida, cavalletto, obiettivo normale (35-50 mm equivalenti), file a piena risoluzione:
1. **Il portone prima e dopo**, la foto chiave: stesso punto di ripresa, frontale e a metà altezza della porta (niente dall'alto), stessa luce, su un fondo neutro chiaro (un telo o un muro bianco in laboratorio), la porta intera con un po' d'aria intorno. Una per stato, poi si scontornano come ora. Se possibile anche per i prossimi restauri: diventa una serie.
2. **Il maniglione da vicino**, per la chiusura: luce radente da sinistra che fa uscire la venatura, senza le finestre del capannone nel riflesso, inquadratura verticale o quasi quadrata.
3. **Il sottoscala con la nicchia in ottone**: frontale, senza lampadario e pianta del cliente, nicchia accesa e luce del giorno bilanciate.
4. **La porta a bilico**: intera, aperta a metà, in una stanza finita, senza letto e cantiere sul fondo.
5. **Le porte a vetri piombati** a piena risoluzione (oggi 678 px), frontali, senza prese in vista.
6. **Il Palazzo del Bo**, se l'Università lo permette: le porte scorrevoli, la boiserie e i banchi, a luce naturale e a piena risoluzione (oggi 700 x 500 px; in pagina c'è una copia ingrandita per gli schermi densi, morbida).
7. Utili per le pagine interne: mani al lavoro con la gommalacca a tampone, un pezzo con foglia d'oro se la fanno ancora, il laboratorio con le macchine.

## Licenze

- **Foto:** tutte dell'azienda, dal suo sito (`assets/originali/`, elenco in `assets/CREDITI.md`), usate solo per la proposta. Nessuna foto di repertorio, nessun segnaposto esterno nella home finale, nessuna immagine generata. Le foto Unsplash in `assets/esterne/` restano scaricate ma non sono usate.
- **Caratteri:** Zodiak (Indian Type Foundry, Fontshare, ITF Free Font License, uso commerciale gratuito) e Schibsted Grotesk (Google Fonts, SIL Open Font License 1.1), serviti dalla pagina in `sito/fonts/`; dettagli in `sito/fonts/LICENZE.txt`.

## Logo

Usato il PNG originale `assets/originali/logo-bottega-arte-1014.png` (firma calligrafica marrone #6F3219), esportato a 400, 520 e 800 px per la testata e il piede a 2x; icona dal monogramma `logo-monogramma-B-512.png`. Non l'ho ricostruito in SVG: il tratto irregolare non verrebbe fedele. Va chiesto all'azienda il file vettoriale originale (AI, PDF o SVG).

## Segnali da IA

`segnali.sh` a 1440: tutte le soglie a posto tranne l'area foto (22 % contro 35 %): la prima schermata è un pezzo scontornato su fondo chiaro, come vuole il committente, e le foto dei lavori sono piccole. Sale con le foto rifatte. Nessuna data in pagina finché anno e anni di esperienza non sono confermati.
