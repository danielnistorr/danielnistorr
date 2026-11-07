# Unicar, home: nota di progetto

## Metodo ibrido (novembre 2026)

Prima schermata secondo la sezione D di `_metodo/professionale/ALTO-LIVELLO.md`; sotto, i contenuti e le funzioni della versione professionale, rimessi su una griglia sola. La versione professionale com'era (sito intero e screenshot) è in `_prova/versione-pro/`. Direzione scritta prima dell'HTML: `_prova/alto/DIREZIONE.md`. Provini delle foto: `_prova/alto/provini.jpg`. Confronti: `_prova/alto/confronto-1440.jpg` (professionale, ibrida, Eberhard, Auto Bayertz) e `_prova/alto/confronto-390.jpg`.

### Secondo giro (3/11/2026): clienti tipo e finitura sotto la piega

Vale sopra il ritocco qui sotto e sopra il resto della sezione. Partenza: giudice da agenzia 6,5 dopo il primo ritocco; clienti tipo scesi (cliente 1 da 8,5 a 7,5, cliente 2 da 7,5 a 7). La home del primo ritocco è copiata in `_prova/alto/prima-del-ritocco-2/` (pagina e screenshot); schermate e prove di lavoro in `_prova/alto/ritocco2/`, misure in `_prova/alto/ritocco2/misure/` (lunedì 10.00, 20.00 e sabato 11.00: 40 controlli su 40 a tutte e tre le ore).

**Per i clienti tipo**
- Testata fissa: lo stato aperto o chiuso è sempre in vista, con il pallino verde o rosso e la frase ("Aperto ora fino alle 12.30", "Chiuso ora riapre lunedì alle 8"), su due righe sul telefono. Dal tablet in su anche il numero 049 8792361 è sempre in vista e non si sposta più: il menu non salta (prima saltava di 146 px). Per questo il bottone dell'apertura dal tablet in su dice "Chiamate l'officina"; sul telefono resta "Chiama 049 8792361".
- Telefono: barra in basso con "Chiama 049 8792361 r.a.", rossa, a tutta larghezza, che compare (senza dissolvenza) quando il bottone dell'apertura esce dallo schermo; senza JavaScript è sempre in vista. Il menu del telefono si apre con "Chiamate l'officina 049 8792361" e "Carrello fermo e zona".
- Prima schermata a 390: bottone di chiamata salito da 486 a 376 px (prima del testo), poi gli orari per esteso con "sabato e domenica chiuso" (solo sul telefono) e "Fuori orario? Mandateci la foto della targhetta" su una riga di tocco alta 48 px, con l'email del carrello fermo già scritta. A 1440 la stessa frase prende il posto degli orari (il giudice li voleva fuori dall'apertura): è anche il primo segno della targhetta in apertura.
- Ricambi: accanto alla richiesta c'è di nuovo la riga "L'officina è in via Canada 12, Padova (link alla mappa): lunedì-venerdì 8-12.30 e 14-18.30, telefono 049 8792361" (senza "magazzino" e senza "ritiro al banco", da confermare), e sotto i comandi la riga fissa a 14 px "Posta nel browser? Copiate il testo e mandatelo a unicar@protec.it". Dopo il clic su Ricambi titolo, cosa mandarci, indirizzo, orari, telefono e bottoni stanno nella stessa schermata (bottoni a 601-657 px). Le tracce delle email dividono "Referente" e "Telefono per richiamarvi".
- Zona: torna "Fuori provincia? Chiamateci." come link `tel:` (un invito, non una promessa). I 20 comuni restano fuori, da confermare.
- Modulo: per manutenzione e controlli chiede "Quanti carrelli" al posto di "Dove si trova il carrello"; i campi stanno tre per riga (una riga in meno).

**Sotto la piega**
- Una griglia sola con quattro linee di partenza (colonne 1, 4, 7, 10) usate da tutte le sezioni; il titolo di sezione sta sempre in cima, sopra il contenuto: sparito lo schema "titolo a sinistra e buco sotto". Il controllo della griglia passa (0 blocchi fuori dalle linee; motto e ritorno hanno il rientro ottico voluto).
- Carrello fermo: la sede alla misura vera, il titolo, poi quattro fatti in quattro colonne senza filetti (Carrello fermo con il bottone, Padova e provincia, Carrelli sostitutivi, Toyota, BT, Cesab).
- Servizi: titolo "Che cosa facciamo" (prima "Su tutte le marche e modelli", sgrammaticato e ripetuto). È, con gli orari, l'unico elenco con i filetti.
- Ricambi e controlli: tolto l'`h2` burocratico; due titoli di sezione a 40 px ("Ricambi, anche fuori produzione" e "Catene ogni tre mesi, tagliando ogni anno"), due colonne con la stessa struttura ("Cosa mandarci" e il nuovo "Per il preventivo", dalle voci dell'email del preventivo), i due bottoni sulla stessa linea.
- Culmine (Chi siamo, 993 px): il motto torna una volta, in rosso, a 64 px con spaziatura -0,03 em (le lettere non si toccano più); sotto la squadra **intera** a 939 x 249, alla misura vera (`squadra-939.webp`, taglio 2:1 `squadra-tel-498.webp` sul telefono): guardata a 4x è una foto sola, le fasce bianche sono i muri dell'ingresso, non giunte. Didascalia vera a sinistra ("La squadra all'ingresso dell'officina / Via Canada 12, tra due carrelli Cesab"), poi la loro frase dei tre passi intera, in un paragrafo solo, e Cami2. Tolta la nota d'archivio "Foto sul sito Unicar dal 2012" e il ritaglio di 284 px.
- Orari e contatti: strade per bisogno (Carrello fermo, Ricambi, Manutenzione e controlli) più La sede con "Indicazioni stradali"; il fax va nel piede. Piede su 12 colonne: ragione sociale e Cami2; telefono, fax, email; voci e Privacy, Cookie.
- Finiture: motto con `margin-left:-.04em` (la C cade sul bordo di 90 px); "la foto della targhetta" e "lunedì-venerdì" non si spezzano; istruzioni a 14 px (`.istr`, soglia di `misura-d.mjs` portata a 14).

**Misure finali** (1440x900 e 390x844): foto in prima schermata 0,4%; cliccabili 8 / 3 (soglie 8 e 4); 1 bottone; 143 caratteri fuori dalla testata (160); gesto a 390 83,5%; bottone di chiamata a 390 con il fondo a 376 px, alto 56; 703 parole (750); 5 sezioni tra apertura e piede; 5.694 px a 1440 (7.761 a 390); culmine 993 px; 5 bottoni; 199 KB; una famiglia; 1 numero sopra i 30 px; "Indicazioni" 1; 0 U+2014 e 0 errori. In `misura-d.mjs` i `tel:` e il numero si contano fuori da testata, barra e piede (per S la D12 non mette tetto: 4 `tel:` in pagina, il numero scritto 2 volte). Controlli a 320, 390, 768, 1024, 1440 e 1920 (`script/controlli.mjs`): nessuno scorrimento orizzontale, nessuna sovrapposizione, nessun errore, menu a 7 voci sotto i 1200 px, modulo che segue il tipo e compone l'email, numero o barra visibili dopo lo scorrimento.

**Resta aperto**: la macro della targhetta (il gesto è ancora una frase, non una foto); gli orari e lo stato restano calcolati su orari da confermare, con la nota in Orari e contatti; il comune non si cerca per nome; le prove con tre persone (D1) e il nuovo voto del giudice e dei clienti tipo sono da rifare.

### Alto livello: ritocco dopo il giudice da agenzia (3/11/2026)

Il giudice ha dato 6,5 (prima 5,5): non passavano D1 (il mestiere non si legge nella miniatura), D8 (6.252 px con i tetti veri) e D12 ("Aperto ora" in tre posti). Questo ritocco vale sopra il resto della sezione: dove le righe più sotto dicono altro (sette sezioni, i 20 comuni, la formazione, lo stato in apertura), vale questo. La home di prima è copiata in `_prova/alto/prima-del-ritocco/index.html` (la striscia `squadra-939.webp` si rifà con la versione precedente di `immagini.py`). Schermate di lavoro in `_prova/alto/ritocco/`, miniatura D1 in `_prova/alto/ritocco/d1-300.jpg`.

**Apertura (D1, D3, D12)**
- Il mestiere esce dalla fascia in basso e va subito sotto il motto: "Assistenza e ricambi per carrelli elevatori, Padova" a 40 px peso 600, su 8 colonne, 32 px sotto il motto, "carrelli elevatori," mai spezzato (32 px sotto i 1200, 28 sotto i 900, 23 sul telefono). Nella miniatura a 300 px la riga è alta 8 px e si legge.
- Il blocco motto e mestiere scende in basso (`align-content:end`): il vuoto sta sopra, come cielo; 64 px tra il fondo del mestiere e il filetto a 1440x900 e a 1920x1080. Il motto passa da 176 a 162 px a 1440x900 (`min(12.2vw, 18vh)`), perché le due righe del mestiere ci stiano; a 1920 resta 188.
- Nella fascia in basso restano solo gli orari a 17 px e il bottone: "Lunedì-venerdì 8-12.30 e 14-18.30. Fuori orario, scriveteci" (email con la traccia del carrello fermo, testo fisso). "Aperto ora" non è più in apertura né in testata.
- Testata in apertura: il telefono esce con `display:none` invece di `visibility:hidden`, così il menu finisce a 1350 px (1590 a 1920), sul bordo destro della griglia e del bottone.

**Sotto la piega (D8, D10, D12)**
- Ricambi e Controlli sono una sezione sola, grigia, "Ricambi e normative di sicurezza" (la voce "Normative di sicurezza" è del loro sito), con due colonne uguali: a sinistra il titolo loro dei ricambi a 24 px, il testo, "Cosa mandarci", "Chiedete un ricambio" e "Copia il testo"; a destra "Catene ogni tre mesi, tagliando ogni anno" a 24 px, l'articolo 71 e "Chiedete un preventivo". I link del menu `#ricambi` e `#controlli` portano alle due colonne. Un `h2` in meno; sezioni tra apertura e piede da 6 a 5.
- Servizi: titolo "Su tutte le marche e modelli" (dal loro "tutte le marche e modelli"), per non ripetere "Ricambi". La riga 08 "Formazione carrellisti" è tolta (da confermare), con la sua voce nel modulo; al suo posto "Vendita e noleggio" con la consociata Cami2 (link a cami2.it, freccia esterna). Il link a cami2.it in Chi siamo è tolto, perché c'è già lì e in testata.
- Chi siamo, il culmine (914 px): la squadra è solo il pannello centrale del vecchio banner (`testata/008.jpg`, x 309-593), 284 x 249 alla misura vera, senza le due fasce bianche, nelle colonne 1-3, uguale a tutte le larghezze (a 320 si stringe a 280, mai ingrandita). Accanto, colonne 5-12, la loro frase dei tre passi intera, a 28/38, divisa sulle tre azioni (01 esame tecnico approfondito, 02 piano d'intervento, 03 metodo concordato con il cliente), poi Cami2. Il motto a 56 px resta sopra.
- Orari e contatti (prima "Orari e zona", anche nel menu): l'unico posto dello stato aperto/chiuso, con la riga a 15 px "Orari della sede di via Canada, da confermare con l'officina". Sotto, tre strade: In officina (indirizzo, "negli orari qui sopra", Indicazioni stradali), Per email (unicar@protec.it, per carrello fermo fuori orario, ricambi e preventivi), Per fax.
- Dati da confermare tolti: l'elenco dei 20 comuni (resta "Padova e provincia", testo loro), "Fuori provincia? Chiamateci", la formazione carrellisti, "il magazzino è in via Canada 12, con l'officina" (anche la didascalia della sede ora dice "Officina e furgoni dell'assistenza"). I carrelli sostitutivi restano con la frase del loro sito (pagina servizi/assistenza, fonte nel commento del codice).
- Finiture: "r.a." resta sulla riga del numero anche sul telefono (36 px sotto i 360); nel piede ragione sociale, Privacy e Cookie sulla stessa linea di base; sul telefono i due bottoni di Ricambi e Controlli sono larghi come la colonna.

**Misure dopo il ritocco** (`_prova/alto/misura-d.mjs`, ora con i tetti veri della D8: 450-750 parole, al massimo 6 sezioni tra apertura e piede, 4.000-6.000 px): 40 controlli su 40 passano a lunedì 10.00 e a 20.00 (`_prova/alto/ritocco/misure-10.txt` e `misure-20.txt`).

| Controllo | Prima del ritocco | Dopo |
|---|---|---|
| Cliccabili a 1440 / a 390 | 6 (7 fuori orario) / 2 | 7 / 3, a tutte le ore (soglie 8 e 4) |
| Caratteri a 1440 fuori dalla testata | 140 (151) | 152 (soglia 160) |
| Bottoni in apertura / in pagina | 1 / 5 | 1 / 5 |
| Bottone di chiamata a 390 | fondo a 479 | fondo a 486, alto 56 |
| Motto a 1440x900 | 176 px | 162 px (188 a 1920) |
| Mestiere | 24 px, in fondo | 40 px sotto il motto, 64 px dal filetto |
| Bordo destro del menu in apertura a 1440 | 1205 | 1350 (griglia 1350) |
| Parole | 621 | 596 |
| Sezioni tra apertura e piede | 6 | 5 |
| Altezza a 1440 / a 390 | 6.252 / 7.451 | 5.938 / 7.438 |
| Culmine (Chi siamo) | 931 | 914 |
| "Aperto ora" in pagina | 3 posti | 1 (Orari e contatti) |
| Formati di foto | 3,77 e 2 | 3,77 e 1,14 a 1440 (più 2 per la sede sul telefono) |
| Peso | 193 KB | 153 KB |

Controlli a 320, 390, 768, 1024, 1440 e 1920 (`_prova/alto/script/controlli.mjs`): nessuno scorrimento orizzontale, nessuna sovrapposizione, nessun errore di script; un solo `tel:` e un solo indirizzo email; menu a 5 voci sotto i 1200 px; la riga Batterie porta al modulo con il tipo scelto; il modulo vuoto dice cosa manca e quello pieno compone l'email; dopo lo scorrimento il telefono della testata si vede. Screenshot rifatti con `_prova/alto/script/screenshot.mjs`.

**Cosa resta aperto**
- Il comune non si cerca più per nome ("il comune si trova nell'elenco dei 20 comuni"): l'elenco torna quando l'azienda conferma la zona.
- Le due parti dell'apertura che fanno capire il mestiere sono parole, non immagini: la macro della targhetta resta la prima foto da fare (al posto del rosso pieno).
- Il modulo "titolo a sinistra, contenuto a destra" torna ancora in tre sezioni (carrello fermo, orari, modulo); il contatto non ha ancora le persone con il nome (D12), perché non le conosciamo.

### Cosa è cambiato

- **Idea e gesto (D1)**: "Consulenti, più che riparatori." (dal loro testo: "affiancare il cliente come consulenti più che di riparatori") come un'insegna, in Libre Franklin 800 a 176 px, bianco sul rosso della C del logo, a tutta prima schermata. È l'unico blocco di colore del marchio della pagina e l'unico elemento sopra i 100 px. La frase torna una volta, con lo stesso carattere a 56 px, in testa a Chi siamo.
- **Modello (D4)**: M (la macro della targhetta, dalla riga del capitolo 5) in attesa della foto; oggi apertura di tipografia, perché D2 non lascia altre strade: le uniche foto vere sono due strisce di 939 x 249, che alla misura vera prendono il 18% della prima schermata (fascia vietata) e non si possono ingrandire. La sede va subito sotto, alla misura vera; a 390 compare già in fondo alla prima schermata.
- **Registro (D5)**: una sola famiglia, Libre Franklin (SIL OFL 1.1), pesi 400, 600 e 800; testo 19 px a 1440 e 17 a 390; nessuna monospaziata, cifre tabellari. Archivo esce.
- **Prima schermata**: motto, una riga di mestiere e luogo, orari con lo stato, un bottone "Chiama 049 8792361". Fuori orario lo stato diventa "Chiuso ora · Scriveteci", con l'email già scritta. In testata il telefono si nasconde finché si vede il bottone dell'apertura (uno solo alla volta), poi resta sempre: a 1440 il numero e lo stato, sul telefono "Chiama".
- **Sotto la piega, sette sezioni su una griglia di 12 colonne** (1260 px a 1440, colonne da 83 px e 24 di spazio: 9 colonne sono 939 px, la misura vera delle foto; tutti i blocchi cadono sulle linee delle colonne, bordi destri allineati a 1350 px):
  1. apertura;
  2. la sede alla misura vera, poi "In azienda con il furgone, anche nei casi più ostici": carrello fermo con "Mandateci marca, modello e matricola, con la foto della targhetta" e il bottone "Carrello fermo? Scriveteci" (email con traccia), Padova e provincia con "Fuori provincia? Chiamateci", carrello sostitutivo, ogni marca (Toyota, BT, Cesab);
  3. gli 8 servizi in un indice a due colonne (le righe portano a Ricambi, a Controlli o al modulo con il tipo già scelto);
  4. Ricambi, con la loro frase "anche prodotto all'estero o uscito di produzione", "Cosa mandarci" in tre righe, "Chiedete un ricambio" (email con traccia) e "Copia il testo" per la posta nel browser (nuovo, lo chiedeva la scheda);
  5. Manutenzione e controlli, con le tre scadenze dell'articolo 71 in una frase (non più in cifre grandi) e "Chiedete un preventivo";
  6. Chi siamo, il culmine (931 px): il motto, la squadra alla misura vera con la didascalia "La squadra all'ingresso di via Canada 12, Padova / Foto sul sito Unicar dal 2012", i tre passi nella loro frase per esteso, il rapporto con Cami2 e il link a cami2.it;
  7. Orari e zona: il numero a 56 px (l'unico numero sopra i 30 px), lo stato per esteso, la tabella degli orari, sede con "Indicazioni stradali" (una volta sola), email e fax, i 20 comuni, il modulo. Il piede è un biglietto da visita sullo stesso fondo.
- **Tolto**: la tavola dei quattro fatti in apertura con "24 ore" a 48 px (dato da confermare, ora fuori dalla pagina), il secondo bottone, la fascia scura delle tre garanzie e delle quattro marche, le cifre grandi delle scadenze, tutti gli occhielli maiuscoli, la chiusura rossa (il rosso è in apertura), il piede a quattro colonne che ripeteva servizi, orari e telefono, "Apri la mappa" (resta "Indicazioni stradali"), la frase dei tre passi detta due volte, il campo Email del modulo (l'email la manda chi scrive), il testo d'interfaccia sul modulo in vista (ora 15 px accanto al comando).
- **Foto**: ricaricate in `assets/originali/` dal loro sito (la cartella era sparita con il riavvio; file sul server dal 30/1/2012). Un solo trattamento (`_prova/alto/script/immagini.py`: mezzo bilanciamento verso il neutro, stessa curva, saturazione 0,88, nitidezza leggera), WebP, due formati (3,77:1 e 2:1 per il telefono), mai ingrandite né scurite. Scartata `pagina-DSC_0050.jpg` (magazzino con retrattili BT, non è il lavoro di Unicar).
- **Fondi**: rosso (solo apertura), bianco, grigio chiaro; spazi tra le sezioni di 96 e 160 px (72 e 64 sul telefono).

### Misure (`_prova/alto/misura-d.mjs`, risultati in `_prova/alto/misure/`; ora fissata lunedì 10.00 e 20.00)

| Controllo | Aperto (10.00) | Chiuso (20.00) | Soglia |
|---|---|---|---|
| Foto nella prima schermata a 1440 | 0,4% (è il logo) | uguale | 60% o più, oppure sotto il 12% |
| Cliccabili a 1440, testata compresa | 6 | 7 | 8 per S |
| Bottoni a 1440 / a 390 | 1 / 1 | 1 / 1 | 1 |
| Caratteri a 1440 fuori dalla testata | 140 (195 con la testata) | 151 | 160 |
| Fila di ingressi, cifre di 30 px fuori dal gesto | 0, 0 | 0, 0 | 0 |
| Cliccabili a 390 | 2 | 3 | 4 |
| Gesto o foto a 390 | 78,5% dello schermo | uguale | 50% |
| Bottone di chiamata a 390 | fondo a 479 px, alto 56 | uguale | entro 600, 48 |
| Occhielli sopra h1 e h2 | 0 | | al massimo 1 |
| h1 | 4 parole, 1 virgola | | 9 e 1 |
| Parole in pagina | 621 | | 900 |
| Sezioni | 7 | | 7 |
| Altezza a 1440 | 6252 px (7451 a 390) | | 7500 |
| Peso | 193 KB | | 3 MB |
| Griglia | un solo contenitore 90-1350 px, 0 blocchi fuori dalle linee | | |
| Foto ingrandite / formati | 0 / 1 a 1440 (2 con il telefono) | | 0 / 3 |
| Fondi / blocchi del colore del marchio | 3 / 1 | | 3 / 1 |
| Numeri di 30 px o più in pagina | 1 (il telefono nella chiusura) | | 1 |
| Link tel: fuori dalla testata / numero scritto | 2 / 2 | | 2 |
| "Indicazioni" / "Carrello fermo? Scriveteci" | 1 / 1 | 1 / 2 | 1 / 2 |
| Frasi ripetute, didascalie ripetute | 0, 0 | | 0 |
| Famiglie, elementi sopra i 100 px, testo minimo | 1, 1, 19 px | | 2, 1, 17 |
| Lista nera, istruzioni sopra i 15 px | 0, 0 | | 0 |
| Bottoni in pagina | 5 | | 5 |
| "indicativ", U+2014, errori di script | 0, 0, 0 | | 0 |

Controlli a 320, 390, 768, 1024, 1440 e 1920 (`_prova/alto/script/controlli.mjs`): nessuno scorrimento orizzontale, nessuna sovrapposizione, nessun errore; un solo `tel:+390498792361` e un solo indirizzo `mailto:unicar@protec.it`; menu a 5 voci sotto i 1200 px; la riga "Batterie e caricabatterie" porta al modulo con il tipo scelto; il modulo vuoto dice cosa manca e quello pieno compone l'email; dopo lo scorrimento il telefono della testata è visibile.

### I compiti della scheda e dove stanno ora (y dalla cima, a 390)

- Chiamare: bottone "Chiama 049 8792361" nella prima schermata (fondo a 479 px, 451 a 320, alto 56, largo quanto la colonna); scorrendo, "Chiama" in testata.
- Aperto o chiuso: stato e "Lunedì-venerdì 8-12.30 e 14-18.30" nella prima schermata (357-407 px); per esteso con "riapre..." nella sezione Orari e zona.
- Fuori orario: "Scriveteci" accanto allo stato nella prima schermata; il bottone "Carrello fermo? Scriveteci" a 992-1048 px (entro la schermata e mezza, 1266).
- Zona e carrello sostitutivo: "Padova e provincia", furgone e "Fuori provincia? Chiamateci" a 1106 px, carrello sostitutivo a 1243 px (entro due schermate, 1688); i 20 comuni da "Orari e zona" nel menu.
- Ricambi (computer): "Ricambi" nel menu; in un blocco solo la loro frase con Toyota, BT e Cesab, le tre cose da mandare, "Chiedete un ricambio" e "Copia il testo"; il numero e lo stato restano in testata.
- Controlli: "Controlli" nel menu, le tre scadenze con l'articolo 71 in una frase, "Chiedete un preventivo".
- Chi c'è dietro: "Chi siamo" nel menu, Cami2, i tre passi, la squadra; "Vendita e noleggio" in testata.
- Mestiere, luogo, marche e foto della sede in 5 secondi (computer): mestiere e Padova nella prima schermata; marche e sede alla seconda schermata (la sede comincia a 1060 px a 1440). È il compito che la sezione D sposta di più.

### Problemi aperti

- **Manca la macro della targhetta.** Il modello M è sospeso: con la foto (al telefono, luce di finestra, a fuoco sulla matricola, almeno 2400 px) il rosso pieno diventa la foto a tutta prima schermata con il motto sopra. Senza, l'apertura è solo tipografia: la riconoscibilità sta tutta nel colore e nella frase.
- **Le foto restano due strisce di 939 px del 2012**, cucite e morbide: alla misura vera sono piccole a 1440 e a 1920. Con il servizio fotografico (LEGGIMI) la pagina sale di livello senza cambiare struttura.
- Fuori orario la prima schermata a 1440 sale a 151 caratteri e 7 cliccabili: dentro le soglie, ma è il caso più pieno.
- A 1440 le marche e la foto della sede non sono nella prima schermata (compito 1 del visitatore 3 della scheda): stanno alla seconda.
- Orari da confermare (vengono dalla scheda di Cami2); formazione carrellisti e testo sull'articolo 71 da far rileggere; "24 ore" fuori dalla pagina finché non lo confermano; il modulo non invia nulla.
- Il controllo D1 (tre persone e la miniatura a 300 px) e quello D4 sull'ondata della zona si fanno a mano, fuori da questo lavoro.

---

## Nota della versione professionale (3/11/2026, resta com'era)

File: `sito/index.html` (statico, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`, con `privacy.html` e `cookie.html`. Tutto si rifà con `sh _prova/script/build_finale.sh` (immagini con `pro_img.py`, controlli con `pro_controlli.mjs`, `pro_prova.mjs` e `pro_orari.mjs`, screenshot con `pro_shoot.py`). Screenshot in questa cartella: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`. Pagina alta 7379 px a 1440 e 10685 px a 390.

Versioni precedenti, copiate com'erano: la home "livello professionale" prima di questo ritocco in `_prova/versione-pro-prima-del-ritocco/index.html` (si apre mettendola al posto di `sito/index.html`); la versione 1 con l'uso (carrello Unsplash sulla corsia gialla, fondo cemento) in `_prova/versione-1-uso/` con i suoi screenshot e la sua nota.

## Livello professionale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia S (servizi tecnici e imprese). Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14, le pagine intere di Kline e Wilson (primo giro) e di Eggentaler e Klindworth (ritocco).

Dalla versione 1 con l'uso: via il repertorio (carrello Toyota di Reding, officina di Yurtman), via il beige e il giallo; restano il titolo "Consulenti, più che riparatori", Archivo, il rosso del logo, lo stato "Aperto ora / Chiuso ora", tutte le email con oggetto e traccia, le mappe, il link a Cami2. In pagina solo le due foto loro (sede e squadra, strisce 939 x 249 del vecchio sito), mai ingrandite.

## Ritocco finale (3/11/2026), dopo il controllore del livello e i tre clienti tipo

Il controllore dava 6 su 10: "pulita e seria, ma un titolare non direbbe 'la voglio così'". Cambiato senza nessuna foto nuova e senza dati nuovi:

- **Apertura.** Il titolo resta, e dentro lo stesso H1 c'è ora la riga del mestiere a 32 px (20 sul telefono): "Assistenza, riparazione e ricambi per carrelli elevatori a Padova". Tolto l'occhiello rosso maiuscolo (andava su due righe al telefono e faceva concorrenza ai bottoni). A destra, al posto del paragrafo grigio e del riquadro rosso, una tavola di quattro fatti con i filetti: **Intervento** "24 ore" in cifre da 48 px, **Orari** con lo stato, **Zona** (Padova e provincia, con il furgone, carrello sostitutivo, "Fuori provincia? Chiamateci"), **Marche e ricambi** con il link "Cercate un ricambio? Cosa mandarci". Il bottone di chiamata ha il numero a 23 px (20 sul telefono) e "r.a." come scrivono loro; finché è in vista, il bottone della testata è bordato, poi torna rosso pieno (un solo rosso pieno alla volta).
- **La sede su antracite pieno.** Tolto il fondo mezzo bianco e mezzo scuro: la foto sta in 8 colonne (845 px, sotto la misura d'origine) dentro il blocco antracite, con accanto "Officina e magazzino ricambi, Via Canada 12, 35127 Padova", "Apri la mappa" e "Indicazioni stradali". A 1440 la foto è tutta nella prima schermata (637-861 px). Nello stesso blocco scuro seguono le tre garanzie (la terza ora è "Ricambi di ogni marca", perché le marche hanno la loro fascia subito sotto) e **la fascia delle marche**, spostata da y≈5300 a subito dopo le garanzie: Toyota, BT, Cesab, Altre in Archivo largo 125 % bianco, didascalie a 17 px.
- **Servizi come indice tipografico.** Via le otto scatole bianche alte 300 px: due colonne di quattro righe, numero rosso a 48 px, nome a 23, riga loro a 17, freccia, filetti. Ogni riga è un link a una sezione (02, 03, 04) o al modulo con il tipo di intervento già scelto (01, 05, 06, 07, 08): nessun programma di posta o di chiamata si apre più per sbaglio cliccando una scheda per leggerla. Sul telefono resta numero, nome e freccia: la sezione passa da 2250 px a circa 900.
- **Ricambi.** Titolo e testo a sinistra (niente più bianco vuoto sotto il titolo), a destra "Cosa mandarci" in tre righe, i due bottoni e un riquadro grigio "Magazzino ricambi" con l'indirizzo che apre la mappa, gli orari con "sabato e domenica chiuso", il telefono e l'email con la stessa traccia completa del bottone.
- **Manutenzione e controlli.** Tolti il promemoria dei mesi, il righello e il file .ics (la scheda d'uso, par. 5 e 7, li indica come cosa "da grafico" e date di legge non rilette). Al loro posto la fascia dei numeri: 3 mesi, 1 anno, 3 anni in cifre da 48 px con l'etichetta accanto, nelle colonne 8-12.
- **Chi siamo.** La squadra in 8 colonne e, accanto, i tre passi (esame tecnico, piano d'intervento, metodo concordato) in colonna: niente più 341 px vuoti a destra.
- **Chiusura.** Nel blocco "Scriveteci" c'è il bottone bordato "Carrello fermo? Scriveteci" con la traccia completa. Il modulo controlla nome, azienda e telefono prima di comporre l'email (avviso a 17 px e fuoco sul primo campo vuoto); con "Ricambio" compare "Pezzo o codice, e quantità" e sparisce "Dove si trova il carrello"; l'urgenza parte da "Subito" solo per carrello fermo e riparazione, altrimenti "In settimana", finché chi compila non la sceglie.
- **Orari.** Lo stato tiene conto dei festivi nazionali e di Pasquetta ("Chiuso oggi, festivo, riapre domani alle 8"); il patrono e le chiusure estive restano da confermare (LEGGIMI).
- **Minori.** Le ancore si fermano esattamente sotto la testata; il link "Scriveteci" fuori orario e "Chiamateci" hanno un'area di tocco di 48 px; tutti i colori sono token (`--rosso-scuro` per il passaggio del mouse, `--linea-scura` per i filetti sul nero; il bordo dei campi usa `--testo-2`); commento nel codice sopra l'elenco dei comuni; nel piede, sotto "Orari e zona", cinque comuni e il link all'elenco.

### Le 15 regole, una per una (dopo il ritocco)

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa 88 px a 1440 e 72 a 390, bottone "049 8792361" alto 48 px. A 390 e a 1440, a metà pagina, il bottone si vede e si tocca (`elementFromPoint`). 10 link `tel:`, tutti `tel:+390498792361`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** A 1440 x 900: H1 con "Assistenza, riparazione e ricambi per carrelli elevatori a Padova", "24 ore" in cifre, bottone di chiamata a 431 px. A 390 x 844: lo stesso, bottone largo quanto la colonna (350 px) a 272 px, poi 24 ore, orari con lo stato, zona con carrello sostitutivo e "Fuori provincia? Chiamateci", marche e il link ai ricambi, tutto senza scorrere.
3. **Immagine vera nell'apertura: passa, con riserva.** La sede vera (insegne Unicar, BT Cesab e Cami2, furgoni, due Cesab), ora incorniciata dal blocco antracite e tutta dentro la prima schermata a 1440. Resta una striscia 939 x 249, senza persone in primo piano: serve la ripresa del LEGGIMI. Nessuna illustrazione, per scelta del committente.
4. **Zero repertorio: passa.** `indicativ` compare 0 volte; in `sito/img/` solo sede, squadra e logo.
5. **Foto in serie: passa.** Due foto, stessa ripresa e stesso trattamento; un formato a 1440 (3,77:1), due tagli sul telefono; nessuna didascalia; nessuna ingrandita.
6. **Palette dal marchio: passa.** `--rosso` #C8141C (C del logo) con `--rosso-scuro` per il passaggio del mouse, `--antracite` #17191B (lettere UNI e AR), neutri freddi. Nessun colore scritto a mano fuori da `:root`. Fondo bianco, nessun beige.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 19, 23, 32, 48, 72, 128) e 8 a 390 (14, 16, 17, 20, 26, 30, 40, 48); testo corrente 19 px a 1440 e 17 a 390; nessun testo sotto i 14 px; le didascalie delle marche ora a 17 px; H1 72/40, H2 48/30. Spariti i 12 radio dei mesi.
8. **Due famiglie al massimo: passa.** Una sola, Archivo, pesi 400 e 700.
9. **Servizi in schede con la foto: non passa.** È un indice tipografico in due colonne, righe tutte cliccabili con numero, nome, riga e freccia, ma senza foto: niente repertorio e niente icone disegnate, per scelta del committente. Le foto da fare per ogni servizio sono nel LEGGIMI.
10. **Almeno tre tipi di prova: non passa (1 su 4).** C'è la fascia delle marche con le didascalie, ora subito dopo le garanzie. Mancano recensioni, numeri aziendali di Unicar, clienti con il nome e certificazioni di Unicar: non sono nelle fonti e non sono stati inventati (LEGGIMI, punti 3, 4, 6, 7). Le cifre 3 mesi, 1 anno, 3 anni sono scadenze di legge, non numeri dell'azienda.
11. **Lavori con un nome: non passa.** Nessun lavoro con cliente, luogo e anno nelle fonti (LEGGIMI, punto 5).
12. **Ritmo a blocchi: passa.** Blocchi pieni oltre al piede: sede, garanzie e marche in antracite, controlli in antracite, chiusura rossa; servizi e zone in grigio. Sezioni a 120/120 px a 1440 e 72/72 a 390 (garanzie 72 sopra, perché continuano la fascia della sede); contenitore 1280 px con margini 80 a 1440, 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno rosso e bordato, raggio 4 px, 56 px (48 in testata), testo 17 px (16 sul telefono); i bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: passa.** Tipo di intervento (10 voci), marca, modello e matricola, pezzo e quantità per i ricambi, indirizzo del carrello, descrizione, urgenza, istruzione per le foto (un mailto non porta allegati); controllo dei campi obbligatori. 20 comuni più "e gli altri comuni della provincia". Nessun iframe di mappa.
15. **Piede completo: non passa.** Quattro colonne, testo di almeno 14 px, telefono ed email cliccabili, orari, zona con cinque comuni e il link all'elenco, sede, Privacy e Cookie. Mancano la ragione sociale completa, la partita IVA (la 01014160285 non è valida nel VIES) e le certificazioni (nessuna di Unicar): non si scrivono finché l'azienda non li dà (LEGGIMI, punti 1 e 7). Lo script delle misure lo segna "sì" perché non controlla la P.IVA: l'esito vero è questo.

### Compiti della scheda d'uso (par. 8) e dei clienti tipo

- *Telefono, carrello fermo (390)*: bottone rosso a tutta larghezza a 272 px (a 320: 340 px, "Chiamate 049 8792361 r.a."), numero a 20 px con "r.a."; sotto "Carrello fermo? Scriveteci" con la traccia; poi 24 ore, orari con lo stato, Padova e provincia con carrello sostitutivo e "Fuori provincia? Chiamateci", marche: tutto nella prima schermata, come nella versione 1 con l'uso. Il numero resta nella testata fissa.
- *Ricambi (1440)*: link in prima schermata "Cercate un ricambio? Cosa mandarci" e voce di menu; "anche prodotto all'estero o uscito di produzione", le tre cose da mandare, "Chiedete un ricambio" (email compilata), magazzino con indirizzo che apre la mappa, orari, telefono ed email con la stessa traccia. Il modulo con "Ricambio" chiede pezzo e quantità e non l'indirizzo.
- *Nuovo cliente (1440)*: marche e zona in prima schermata e nella fascia delle marche sotto la sede; manutenzione e controlli in tre righe con "Chiedete un preventivo"; "Vendita e noleggio" in testata; la riga su Unicar e Cami2 in Chi siamo.
- *Identità*: la sede vera nella prima schermata a 1440 e nella seconda a 390.
- Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1280, 1440 e 1920; nessuna sovrapposizione nell'apertura.

### Caratteri e licenze

- **Archivo** (Omnibus-Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; licenza in `sito/fonts/OFL.txt`. Servito dalla pagina (`sito/fonts/archivo-latin.woff2`, `archivo-latin-ext.woff2`), pesi 400 e 700, larghezze 100 %, 110 % e 125 % (nomi delle marche).
- Foto: solo materiale del loro sito (sede e squadra, `assets/originali/testata/007.jpg` e `008.jpg`) e il logo PNG, da usare con il loro permesso. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Controlli fatti (3/11/2026, dopo il ritocco)

- `pro_controlli.mjs`: regole 1-8 e 12-14 superate nelle misure; 9, 10, 11 e 15 no (vedi sopra). Nessuna ancora senza destinazione.
- `pro_prova.mjs`: menu a 390 aperto e chiuso dopo il clic; ancora "Ricambi" sotto la testata; testata bordata in cima e rossa piena dopo lo scorrimento; riga "Batterie" che porta al modulo con il tipo scelto; invio vuoto fermato con l'avviso e il fuoco sul nome; con "Ricambio" compaiono pezzo e quantità e sparisce l'indirizzo; email composta e letta senza inviarla; nessun errore di script.
- `pro_orari.mjs`: martedì 10.00 aperto; 13.10 "riapre alle 14"; 19.30 "riapre domani alle 8"; sabato "riapre lunedì"; 8 dicembre e Pasquetta "Chiuso oggi, festivo"; vigilia di Natale sera "riapre lunedì" (salta Natale, Santo Stefano e la domenica).
- Screenshot guardati a pezzi a 1440 e a 390, prime schermate e pagine intere a 320, 768 e 1024. Nessun U+2014 in pagina, nei .md e negli script.
