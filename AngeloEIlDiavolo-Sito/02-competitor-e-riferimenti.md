# 02. Concorrenti e riferimenti di design

Ricerca del 6 ottobre 2026. Ho aperto con Playwright (Chromium, attraverso il proxy; i siti solo http passano da curl) 6 siti di locali della zona e 23 siti di ristoranti di riferimento, a 1440 e a 390 px. Per i nomi dei concorrenti ho usato la ricerca web (guida Michelin, Sluurpy, visitmarostica.eu) e poi ho provato i domini a mano. Gli screenshot grezzi sono in `_prova/ricerca/` (ignorata da git): `<nome>-1440.png` e `<nome>-390.png` a pagina intera (tagliati a 9000 px), `<nome>-<larghezza>-top.png` per la prima schermata, `<nome>.json` con caratteri, colori e larghezza misurati. I pezzi da riprendere sono in `_prova/ricerca/ritagli/`, i fogli di controllo in `_prova/ricerca/pezzi/`, la prova delle accoppiate in `_prova/ricerca/accoppiate/`.

Prima di scegliere i riferimenti ho guardato il materiale che l'osteria ha già (32 foto della galleria, 3 foto grandi, 3 ritratti, 2 disegni): il riferimento giusto nasce da lì, non da un'idea generica di "ristorante elegante". Il foglio è `_prova/ricerca/pezzi/aed-materiale.jpg`.

## 1. Concorrenti

| # | Concorrente | Zona | Cosa fa meglio dell'Angelo e il Diavolo | Punto debole misurato |
|---|---|---|---|---|
| 1 | [Osteria Madonnetta](https://www.osteriamadonnetta.it/) | via Vajenti 21, Marostica, a due passi dalla piazza | si legge da telefono; "Sfoglia il nostro menù" subito sotto la foto d'apertura; "dal 1904", "Chiocciola Slow Food", logo Michelin nel piede; telefono fisso, cellulare, WhatsApp ed email; orari nel piede (gli stessi dell'Angelo e il Diavolo: 10.00-15.00 e 18.00-24.00, giovedì chiuso); sito in italiano, inglese e tedesco; nel piede "Progetto finanziato con il PR Veneto FESR 2021-2027" | a 390 la pagina è larga 900 px: i tre numeri di telefono escono a destra e si legge solo "+39" (`ritagli/concorrente-madonnetta-390-telefoni-tagliati.jpg`); testo in Open Sans 300 grigio #666 su bianco (5,7:1, tratto sottile); impianto da tema WordPress (Divi: lo tradisce la scritta "Seleziona una pagina" del menu), Playfair Display per i titoli |
| 2 | [La Rosina](https://larosina.it/) | via Marchetti 4, Marostica | albergo e ristorante "dal 1917", "Bib Gourmand MICHELIN" dichiarato in home, riconoscimenti in fila (Michelin, Tripadvisor); serate musicali "Note d'Estate" i giovedì di luglio; buono regalo "Degustazione"; badge POR FESR 2014-2020 nel piede | a 390 il titolo d'apertura "Design Restaurant e Luxury Hotel" esce dallo schermo ai due lati (`ritagli/concorrente-larosina-390-titolo-tagliato.jpg`); frasi in inglese da modello d'albergo ("Difference is passion since 1917", "What we can give to our guests"); refuso in home "GUSTA I SAPORTI DEL TERRITORIO"; il ristorante è una voce tra camere e sale |
| 3 | [inOsteria](https://inosteria.it/) | Crosara di Marostica, 7° tornante | i due titolari in foto (in sala e in cucina, con il cane); i prodotti del territorio con il paese d'origine (asparago di Bassano, ciliegie di Marostica, bisi di Borso, fagiolo di Lamon); "3 sale e una terrazza estiva" con foto delle sale | testo bianco su riquadri arancio semitrasparenti posati sulle foto (bianco su arancio pieno 2,1:1, sulla foto ancora meno; misurato `rgba(255,153,0,0.6)`); Amatic SC e Comfortaa; avviso "APERTURA 2026! inOsteria torna ad essere aperta dal giorno venerdi 5 Giugno" ancora in testa a ottobre |
| 4 | [Osteria Terraglio](https://www.osteriaterraglio.it/) | piazza Terraglio 28, Bassano del Grappa | tre ingressi chiari: Cucina, Cantina, Prenota; "Gift card" nel menu; foto di piatti curate | home quasi vuota (carosello e tre pittogrammi); da telefono il menu è una tendina di sistema "Menu" (`ritagli/concorrente-terraglio-390-menu-select.jpg`); nessun orario in home; WordPress 5.6 |
| 5 | [Trattoria Dadoro](https://dadoro.it/) | Solagna, valle del Brenta | tabella orari giorno per giorno con filetti; foto in bianco e nero della famiglia sulla porta; due pulsanti "Scopri il Menù" e "Carta dei vini"; video | il logo non si carica: in testata si legge il testo alternativo "logo trattoria Dadoro" (a 1440 e a 390); il testo d'apertura nelle nostre catture è quasi invisibile (1,5:1 misurato sui pixel, `ritagli/concorrente-dadoro-390-testo-chiaro.jpg`) e da telefono restano grandi blocchi vuoti: contenuti che compaiono allo scorrimento; Fraunces |

Visti e lasciati fuori: [Hotel Due Mori](https://www.duemori.it/) (corso Mazzini, è un albergo, il ristorante non compare nel sito); Osteria Dalla Zita, Ristorante al Castello Superiore, Ristorante Cuori, Trattoria da Toi: nessun sito trovato ai domini provati (castellosuperiore.it è in vendita), compaiono solo su guide e social. Contano lo stesso: chi cerca un posto in centro li confronta su Google e TripAdvisor (il sito attuale rimanda a TripAdvisor), e da lì apre i siti dal telefono.

**Cosa fanno i migliori (Madonnetta prima di tutti):** menu raggiungibile con un tocco; telefono, WhatsApp e orari in ogni pagina; riconoscimenti esterni (Slow Food, Michelin) al posto degli aggettivi; foto vere dei piatti; https. Due concorrenti su cinque espongono nel sito un contributo regionale FESR (Madonnetta "Progetto finanziato con il PR Veneto FESR 2021-2027", La Rosina il POR FESR 2014-2020), lo stesso tipo di contributo appena incassato dall'Angelo e il Diavolo.

**Cosa non fa nessuno (spazio per l'Angelo e il Diavolo):**
1. un'identità disegnata. L'osteria ha già un disegno suo: un angelo azzurro con la lira e la scritta "APO", un diavolo rosso col forcone, al tavolo sotto lo striscione "Osteria L'Angelo & il Diavolo", con la battuta "Vorrà dire che il bianco lo chiameremo l'Angelo... e il rosso il Diavolo!!!" (`locale_foto1.jpg` della galleria). C'è anche un secondo disegno ("GOAL!", diavoli contro angelo), stampato sul menu di carta dei tavoli accanto a "Le nostre pizze" (`cartone-pizza.jpg`). I concorrenti usano modelli generici, con Playfair Display, Open Sans, Fjalla One, Comfortaa, Fraunces;
2. una voce. Le frasi dell'oste sono in rima ("Si riposa il lunedì perché il fegato respiri, aperto tutti gli altri dì tra brindisi e sospiri"); i concorrenti scrivono "sapori e profumi unici del territorio" e "un viaggio alla scoperta di antichi sapori";
3. la cucina romana a Marostica e il porcetto al forno a legna la domenica. La Madonnetta è veneta, La Rosina è gourmet, inOsteria è vegetariana: nessuno vicino propone cacio e pepe, gricia, carbonara;
4. la piazza. L'Angelo e il Diavolo è in piazza Castello 41/A, sotto il portico, con l'insegna al neon (`locale_foto7.jpg`); la Madonnetta è in via Vajenti, "a pochi passi" dalla piazza secondo la guida Michelin. Si può far vedere con una mappa disegnata della piazza;
5. la musica: la frase di Apo è "Un'oste di passaggio, una vita di emozioni, sogni e canzoni tra santi, bugiardi e cialtroni" e la home rimanda al progetto musicale "Voci dal cuore" per l'associazione "30 Nodi per il fegato" [DA CONFERMARE che cosa è e se va tenuto]. La Rosina fa le "Note d'Estate", ma come evento d'albergo.

**Posizionamento proposto (solo frasi del sito attuale, da confermare in 03):** l'osteria di Apo in piazza Castello a Marostica; specialità romane di Bruna (cacio e pepe, matriciana, gricia, aglio & olio, carbonara); porcetto cotto su forno a legna, tutte le domeniche o su prenotazione; si riposa il lunedì. Contro la Madonnetta (storica, veneta, premiata, sito già fatto bene) non si compete su storia e premi ma su carattere: un altro tipo di serata, nella stessa piazza.

**Copy evitato** (visto nei concorrenti): le parole della lista `PAROLE_VIETATE` di `build.py` (La Rosina, inOsteria e Armando al Pantheon ne usano in home), "sapori e profumi unici", "un viaggio alla scoperta di", "luxury", "esperienza", frasi in inglese da albergo, contatori d'anni che invecchiano.

## 2. Riferimenti premium

### 2.1 Perché questi

L'Angelo e il Diavolo è un'osteria piena di gente e di oggetti, con un oste che parla in rima, una cuoca romana, il forno a legna, le pareti coperte di quadri e un disegno come insegna. I riferimenti giusti non sono i ristoranti stellati con fondo crema e titoli sottili, né gli alberghi di design: sono osterie, trattorie e bar a vino con un carattere forte, che hanno un sito di livello alto senza diventare eleganti per forza. Ho tenuto otto siti che fanno ognuno una cosa precisa meglio di tutti, e che si possono collegare a un pezzo vero del materiale dell'osteria.

| Riferimento | Che cos'è | Gesto preciso | Dove nel sito dell'Angelo e il Diavolo |
|---|---|---|---|
| [Bocca di Lupo](https://www.boccadilupo.com/) | trattoria di cucina regionale italiana, Soho, Londra | il rosso vino come campo intero, non come riquadro; orari in due colonne con l'ultima prenotazione; mappa disegnata a tratto chiaro sul fondo vino | fasce "Ristorante" e "Orari", mappa nei Contatti |
| [Via Carota](https://www.viacarota.com/) | osteria del West Village, New York | menu e carta vini composti come fogli stampati; griglia a incastro di foto piccole prese dall'alto; Josefin Sans maiuscolo spaziato (lo stesso carattere del sito attuale dell'Angelo e il Diavolo) | menu nella pagina Ristorante, galleria |
| [Noble Rot](https://noblerot.co.uk/) | tre ristoranti e bar a vino a Londra, e una rivista | un disegno come protagonista (in copertina un angioletto che abbraccia una bottiglia); sulla foto della sala piena: indirizzo, telefono e una fila di pulsanti concreti | apertura della Home, blocco "Prenota" |
| [Roscioli](https://www.roscioli.com/) | salumeria con cucina, forno e caffè, Roma | titoli grandissimi e corti in maiuscolo bastoni; mappa disegnata del quartiere con il locale in un blocco di colore | "Dove siamo": piazza Castello disegnata con la scacchiera |
| [Septime](https://www.septime-charonne.fr/) | bistrot, Parigi | tutto il sito battuto a macchina; menu con il prezzo allineato a destra; orari in quattro righe; i vignaioli in un blocco di nomi | menu, orari, carta dei vini |
| [Asador Etxebarri](https://www.asadoretxebarri.com/) | asador (cucina alla brace), Axpe (Bizkaia) | "Come funziona" in righe brevi con titolo (prezzo, commensali, cucina, orario); domande frequenti a filetti; nel piede la frase sul finanziamento europeo, composta in piccolo | "Come prenotare", piede con l'obbligo FESR |
| [The Quality Chop House](https://thequalitychophouse.com/) | trattoria storica, Farringdon, Londra (dal 1869) | l'insegna dipinta del locale è l'apertura del sito; orari di cucina giorno per giorno nel piede scuro | insegna al neon sotto il portico, piede |
| [Brat](https://bratrestaurant.co.uk/) | cucina sul fuoco a legna, Shoreditch e Hackney, Londra | pagina d'ingresso divisa in due metà piene, una per sede; dentro: un campo di colore pieno con due foto sfalsate e una piccola tabella orari in alto a destra | fascia "il bianco e il rosso", pagina Ristorante (porcetto) |

### 2.2 Riferimento per riferimento

**Bocca di Lupo** (Londra). Fondo vino misurato #642A2F su tutta la pagina, testo #E8E6DF (8,8:1), titoli in un bastoni geometrico art déco maiuscolo spaziato (Mostra Nuova), testo in Century Gothic. Il blocco "Menu" è una foto verticale di un piatto su tovaglia bianca, a sinistra, e a destra tre paragrafi e quattro link maiuscoli sottolineati (À la carte, menu del pranzo, vini, cocktail). Gli orari sono due colonne (lunedì-sabato, domenica) con pranzo e cena, apertura e chiusura della cucina e ultima prenotazione. La mappa è un disegno a tratto color gesso sul fondo vino.
- *Si riprende:* oggi il bordeaux #800920 dell'Angelo e il Diavolo è un riquadro dietro la poesia; diventa il fondo di fasce intere, con il testo chiaro sopra. Gli orari in due colonne, scritti per intero con le parole del sito ("orari di apertura: 10.00-15.00 18.00-24.00", "Turno di chiusura il lunedì tranne i mesi estivi"). Il blocco foto verticale + testo + link sottolineati per la pagina Ristorante.
- *Si evita:* tutta la pagina in vino (stanca: si alterna col bianco); la fila di recensioni di giornali (non abbiamo citazioni verificate); la barra di annunci sopra la testata.
- *Ritagli:* `bocca-di-lupo-menu.jpg`, `bocca-di-lupo-orari.jpg`, `bocca-di-lupo-mappa-contatti.jpg`, `bocca-di-lupo-390-testata.jpg`.

**Via Carota** (New York). Testata marrone #523523 con logo a raggiera; Josefin Sans maiuscolo spaziato per titoli e menu, Libre Baskerville 12 px per il testo, inchiostro #513624 su bianco. Il menu è un foglio composto come una stampa (mesi illustrati nel margine, sezioni Spuntini, Verdure, Pesce, Carne, prezzi tra due punti) e la carta vini è un secondo foglio, con il link a una versione in solo testo. Le foto dei piatti sono in tre colonne a incastro, piccole, prese dall'alto su legno e metallo. Nel testo: aperto da presto fino a tardi, "senza pause, come in una vera osteria".
- *Si riprende:* l'osteria ha già un menu di carta illustrato (il disegno "GOAL!" accanto alle pizze, `cartone-pizza.jpg`): il gesto di Via Carota le appartiene già. Poi la griglia a incastro per le 32 foto della galleria, che sono larghe 800 px: in tre colonne su 1440 ogni foto sta sotto i 440 px, quindi resta nitida anche su schermi retina; il menu come pagina composta, ma in HTML (leggibile da telefono e da Google); Josefin Sans solo per titoli brevi in maiuscolo, che è l'unico uso in cui funziona (il sito attuale lo usa anche per i paragrafi, a 20 px, e affatica).
- *Si evita:* il menu solo come immagine; il logo a raggiera; il marrone come unico colore.
- *Ritagli:* `via-carota-menu-stampato.jpg`, `via-carota-carta-vini.jpg`, `via-carota-griglia-foto.jpg`, `via-carota-testata.jpg`.

**Noble Rot** (Londra). Apertura: riquadro chiaro con cornice nera spessa, logo scritto a mano, una frase, tre pulsanti a cornice, e accanto la copertina della rivista: un angioletto disegnato che abbraccia una bottiglia, "Rosé heaven beyond the angel". Sotto, la foto della sala piena di sera con il nome della sede, indirizzo, telefono, email e una fila di pulsanti: Prenota (l'unico pieno, rosa), Menu, Carta dei vini, Eventi, Buoni regalo. Futura PT nero, articoli con illustrazioni tonde.
- *Si riprende:* un disegno come protagonista accanto alle foto, con la stessa ironia. L'Angelo e il Diavolo ha già il suo (angelo e diavolo al tavolo, "il bianco... il rosso"): va in apertura, a dimensione nativa (800 x 544 px: si mostra al massimo a 544 px di larghezza su retina, quindi in mezza colonna, non a tutta pagina) [DA CONFERMARE autore e diritti del disegno: firma poco leggibile, anno "'98"?]. La fila di azioni sulla foto della sala: Prenota (telefono), Menu, Dove siamo. Un solo pulsante pieno.
- *Si evita:* il rosa acceso, i cerchi, la rivista.
- *Ritagli:* `noble-rot-copertina-angelo.jpg`, `noble-rot-sede-pulsanti.jpg`, `noble-rot-illustrazioni.jpg`.

**Roscioli** (Roma). Fondo #F7F3E7, titoli DIN bold maiuscolo fino a 128 px ("LA FAMIGLIA", "DOVE TROVARCI"), testo nero in grassetto; mappa disegnata del quartiere con i quattro locali come blocchi di colore e le vie scritte lungo il tracciato; in fondo, una scheda per ogni attività con "DAL 1972", "DAL 1992" sopra il nome.
- *Si riprende:* la mappa disegnata, in SVG, di piazza Castello con la scacchiera, i due castelli e l'osteria al 41/A, al posto della mappa Google rimpicciolita di oggi (la mappa Google resta come link "Apri in Maps"); i titoli corti e grandi.
- *Si evita:* le schede che si impilano scorrendo (è un effetto allo scorrimento); un colore diverso per ogni blocco; il fondo crema.
- *Ritagli:* `roscioli-mappa-disegnata.jpg`, `roscioli-titolo-famiglia.jpg`, `roscioli-390-titoli.jpg`, `roscioli-schede-dal.jpg` (nello screenshot le schede risultano sovrapposte proprio per l'effetto di scorrimento).

**Septime** (Parigi). Un solo carattere da macchina da scrivere (Prestige), una croce sottile come separatore, il menu in due righe con il prezzo allineato a destra, gli orari in quattro righe ("lundi - vendredi", "Fermeture samedi - dimanche"), i nomi dei vignaioli in un blocco centrato.
- *Si riprende:* il menu come foglio battuto: piatto a sinistra, prezzo a destra, solo se i prezzi vengono confermati dal cliente [DA CONFERMARE prezzi]; gli orari corti; l'elenco delle cantine se arriva la carta dei vini ("un'ampia carta dei vini", dice il sito, ma non la elenca) [DA CONFERMARE]. In sala l'osteria ha incorniciata la "Legge fondamentale del capo", battuta a macchina (`locale_foto3.jpg`): il carattere da macchina da scrivere viene anche da lì.
- *Si evita:* la pagina quasi vuota, il menu nascosto dietro l'hamburger anche a desktop.
- *Ritagli:* `septime-menu-prezzi.jpg`, `septime-orari-vignaioli.jpg`, `septime-logo.jpg`.

**Asador Etxebarri** (Axpe). Foto della finestra in pietra con il paesaggio, logo e menu in bianco a sinistra; blocco "Come funziona" con quattro voci (prezzo, carne e pesce, commensali, mezzogiorno) di due-quattro righe ciascuna; domande frequenti in righe separate da filetti con una freccia; piede nero con la frase sul finanziamento europeo (NextGenerationEU) in testo piccolo.
- *Si riprende:* "Come prenotare" in righe brevi, con le frasi del sito: porcetto "tutte le domeniche o su prenotazione"; "Turno di chiusura il lunedì tranne i mesi estivi"; prenotazione al telefono 0424 72312. L'obbligo di pubblicità del contributo FESR (oggi pagina `Bando_pr_veneto.htm` e banner in home) va nel piede, composto con i loghi richiesti e una riga di testo, più la pagina dedicata [DA CONFERMARE le regole grafiche del bando su dimensione e posizione dei loghi].
- *Si evita:* il serif sottilissimo (Canela 100) su fondo crema: è il "lusso" generico bocciato con Benvegnù.
- *Ritagli:* `etxebarri-come-funziona.jpg`, `etxebarri-faq.jpg`, `etxebarri-piede-fondi-ue.jpg`, `etxebarri-apertura.jpg`.

**The Quality Chop House** (Londra). L'apertura è la foto dell'insegna storica dipinta in oro sulla facciata ("Dining and Tea Rooms"), con il nome e gli anni "1869-2026" sopra. Il piede scuro elenca gli orari di cucina giorno per giorno.
- *Si riprende:* l'insegna vera come immagine d'identità. L'Angelo e il Diavolo ha la foto dell'insegna al neon sotto il portico (`locale_foto7.jpg`, 800 x 530 px): troppo piccola per la larghezza intera, si usa a mezza colonna nei Contatti; per un'apertura a tutta pagina serve una foto nuova (brief nel LEGGIMI).
- *Si evita:* il titolo sovrapposto alla scritta dipinta (due scritte che si leggono male insieme). Da telefono la nostra cattura è uscita senza fogli di stile (pagina larga 1608 px): non la uso come prova.
- *Ritagli:* `quality-chop-insegna.jpg`, `quality-chop-orari-piede.jpg`.

**Brat** (Londra). L'ingresso è diviso in due metà piene: arancio con il logo della sede di Redchurch Street, rosa con il disegno della sede di Climpson's Arch. Dentro, un campo di colore pieno con due foto in bianco e nero sfalsate (una in alto a sinistra, una più in basso a destra) e gli orari di cucina in una piccola tabella in alto a destra; "Expect wood fired cooking".
- *Si riprende:* una sola fascia divisa a metà, il bianco e il rosso, come nella battuta del disegno ("il bianco lo chiameremo l'Angelo, il rosso il Diavolo"); per il porcetto, due foto sfalsate su un campo pieno (le foto del forno sono 800 x 600: a mezza colonna restano nitide).
- *Si evita:* un ingresso a tutta pagina senza contenuti, che aggiunge un tocco prima del menu.
- *Ritagli:* `brat-due-meta.jpg`, `brat-foto-sfalsate-orari.jpg`, `brat-arch-orari-testo.jpg`.

### 2.3 Visti e lasciati fuori (o presi solo per un dettaglio)

| Sito | Perché no | Dettaglio utile |
|---|---|---|
| [St. JOHN](https://stjohnrestaurant.com/), Londra | sito povero, foto piccola | il maiale inciso come logo: idea per il porcetto, se mai servisse un'icona |
| [Felice a Testaccio](https://feliceatestaccio.com/), Roma | modello generico, maiuscolo sottile | cucina romana: piatto con il nome del locale stampato sul bordo |
| [Da Enzo al 29](https://www.daenzoal29.com/), Roma | titoli in corsivo calligrafico, pulsanti arrotondati | menu in testo, diviso in Antipasti, Primi, Secondi, Dolci; "Non si accettano prenotazioni" detto chiaro |
| [Armando al Pantheon](https://armandoalpantheon.it/), Roma | modello generico | schede delle persone di famiglia con il loro ruolo; regole di prenotazione nel piede |
| [Trattoria Al Pompiere](https://alpompiere.com/), Verona | crema, foto ovali e ad arco, display sottile: è il modello da non fare | anche qui "Progetto finanziato con il PR Veneto FESR 2021-2027" nel piede; regole di prenotazione scritte bene |
| [Antiche Carampane](https://www.antichecarampane.com/), Venezia | pannelli foto a tutta pagina, carattere piccolo | una frase con voce: "Non si arriva per caso" |
| [Rules](https://rules.co.uk/), Londra | EB Garamond corsivo ovunque, ovali | sala vera, velluto rosso e quadri: foto della sala come apertura |
| [Osteria Mozza](https://www.osteriamozza.com/), Los Angeles | blocchi foto e testo alternati, ordinari | barra con indirizzo e telefono sopra la testata |
| [Trippa](https://www.trippamilano.it/), Milano | locale celebre, sito datato | indirizzo e orari, prenotazioni, contatti, menu in quattro colonne |
| [The Sportsman](https://www.thesportsmanseasalter.co.uk/), Seasalter | solo testo | regole di prenotazione scritte per intero |
| [Trattoria Pennestri](https://trattoriapennestri.it/), Roma | modello generico | foto della squadra al banco |
| [Piatto Romano](https://www.piattoromano.com/), Roma | crema e corsivo | tutto in una schermata: tre foto, prenota, chiusura estiva, indirizzo, giorno di chiusura |
| [Lilia](https://www.lilianewyork.com/), [Chez Panisse](https://www.chezpanisse.com/), [Trullo](https://www.trullorestaurant.com/) | corsivi calligrafici, caroselli | nessuno |

Non aperti: osteriadelsole.it e ristorantealcovo.com (la pagina non si costruisce nel browser automatico), cantinadospade.com (controllo anti-robot); santopalato.com, cesareacasaletto.it, trattoriasostanza.it e altri non passano dal proxy.

## 3. Cosa si riprende

### 3.1 Il materiale di partenza

Le foto dell'osteria sono calde, scattate di sera con luce a incandescenza, piene di persone e di oggetti; i piatti sono su tovaglie a righe bianche e blu, il porcetto è dentro il forno con la fiamma. Le risoluzioni decidono l'impianto:

| Immagine | Pixel | Uso massimo |
|---|---|---|
| `apo-locale.jpg` (Apo al banco), `ristorante.jpg` (spaghetti), `cartone-pizza.jpg` (sala piena) | 2000 x 1325 | larghezza intera fino a 1440 su schermo normale; su retina al massimo 1000 px CSS |
| galleria `locale/foto1-9`, `ristorante/foto1-23` | 800 x 530-634 | mezza colonna o griglia a tre colonne |
| ritratti Apo, Bruna, Lorenzo | 448-591 x 523-689 | colonna stretta, 300 px |
| disegno dell'Angelo e del Diavolo, disegno "GOAL!" | 800 x 544, 800 x 634 | mezza colonna, mai a tutta pagina |
| `porceddu.jpg`, `pasta.jpg` | 215 x 200 | non usabili (sono miniature: si usano le versioni 800 della galleria) |

Dal materiale emergono anche cose che il testo del sito non dice: le foto di pizze e di palline d'impasto, l'insegna al neon "Pizzeria" sotto il portico, il menu di carta con "Le nostre pizze" e la scritta "cucina tipica Romana e Sarda" (prezzi leggibili ma di data ignota). [DA CONFERMARE se la pizza è ancora in carta: va in 01 e nel LEGGIMI.]

### 3.2 Sezione per sezione

| Sezione | Gesto | Da chi |
|---|---|---|
| Testata | telefono 0424 72312 sempre visibile e leggibile (oggi da telefono è a 5-6 px), una sola azione piena "Chiama per prenotare" | Noble Rot, Bocca di Lupo |
| Apertura Home | la foto vera della sala o di Apo al banco con nome, indirizzo, telefono e una fila di tre azioni (Prenota, Menu, Dove siamo) | Noble Rot (blocco sede) |
| Il nome | fascia divisa a metà: bianco e rosso, con il disegno e la sua battuta | Brat (due metà), disegno della casa |
| Specialità romane, porcetto | campo vino pieno, foto verticale e testo con link sottolineati; il porcetto con due foto sfalsate del forno | Bocca di Lupo, Brat |
| Menu | foglio composto in HTML: nome del piatto, descrizione, prezzo a destra se confermato | Via Carota, Septime |
| Galleria | griglia a incastro in tre colonne, foto alla loro dimensione, nessun carosello | Via Carota |
| L'Angelo e il Diavolo (le persone) | Apo, Bruna e Lorenzo con la loro frase del sito, ritratti piccoli | Armando al Pantheon, Pennestri |
| Dove siamo | mappa disegnata di piazza Castello con l'osteria al 41/A; foto dell'insegna al neon a mezza colonna | Roscioli, Bocca di Lupo, Quality Chop House |
| Orari e prenotazione | orari scritti per intero in due colonne; "Come prenotare" in righe brevi | Bocca di Lupo, Etxebarri, Septime |
| Piede | ragione sociale, P.IVA, indirizzo, orari; obbligo FESR composto con calma | Etxebarri, Quality Chop House |
| Voce | una frase con carattere invece di uno slogan: le rime dell'oste, verbatim | Antiche Carampane, Noble Rot |

**Scartato:** carosello automatico (Madonnetta, Terraglio, Mozza), comparse allo scorrimento (Dadoro), schede impilate allo scorrimento (Roscioli), foto ovali e ad arco (Al Pompiere, Rules), corsivi calligrafici (Da Enzo, Chez Panisse, Lilia, Piatto Romano), testo su riquadri semitrasparenti (inOsteria), menu solo in PDF o immagine, stelle e recensioni (non verificabili da noi), loghi di premi che l'osteria non ha.

## 4. Accoppiate

Tre accoppiate, tutte su Google Fonts, tutte con i colori presi dal materiale dell'osteria e non da una tavolozza di moda. Nessuna usa il fondo crema come base né il corsivo per le parole d'accento. La prova impaginata, con testi veri del sito, è in `_prova/ricerca/accoppiate/accoppiate.html` (screenshot `prova-1440.png`, `prova-390.png`). I colori di partenza: bordeaux #800920 e rosso #CD1719 del CSS attuale; azzurro #AAD5E3 e magenta #B61763 misurati sul disegno dell'Angelo e del Diavolo; rosso #B60103 delle piastrelle della cucina (`ristorante/foto9.jpg`). Contrasti calcolati con la formula WCAG 2.

### A. Vino e gesso: Josefin Sans + Source Serif 4

- **Caratteri:** Josefin Sans 700, maiuscolo, spaziatura 0,08 em, per titoli brevi, menu di navigazione, telefono e numeri; Source Serif 4 400 e 600 (tondo, mai corsivo) per paragrafi, descrizioni dei piatti, rime dell'oste.
- **Perché:** Josefin Sans è il carattere del sito attuale (continuità per chi già conosce l'osteria) ed è lo stesso che Via Carota usa in maiuscolo spaziato per i titoli; Bocca di Lupo usa un maiuscolo geometrico art déco della stessa epoca. Il serif per il testo viene dai menu stampati delle osterie (Via Carota con Libre Baskerville, Osteria Mozza con Kepler, St. JOHN con Georgia): è il carattere del foglio del menu, non un vezzo. Source Serif 4 ha le dimensioni ottiche e regge i 16-19 px da telefono. Nessun concorrente li usa nei titoli o nel testo (La Rosina carica Josefin Sans nel codice; i titoli dei concorrenti sono Playfair, Fjalla One, Comfortaa, Fraunces).
- **Palette:**

| Colore | Hex | Da dove | Uso |
|---|---|---|---|
| vino | #800920 | CSS del sito attuale | fondo delle fasce Ristorante e Orari, colore dei titoli su bianco |
| gesso | #F3EEE6 | testo chiaro di Bocca di Lupo (#E8E6DF), schiarito | solo testo su vino; non è un fondo |
| inchiostro | #1F1A1A | | testo su bianco, piede |
| azzurro angelo | #AAD5E3 | disegno | etichette e titoletti su vino |
| bianco | #FFFFFF | | fondo delle sezioni chiare |

| Testo | Fondo | Contrasto |
|---|---|---|
| bianco #FFFFFF | vino #800920 | 10,62:1 |
| gesso #F3EEE6 | vino #800920 | 9,19:1 |
| azzurro #AAD5E3 | vino #800920 | 6,74:1 (solo titoletti, almeno 16 px in grassetto) |
| vino #800920 | bianco #FFFFFF | 10,62:1 |
| inchiostro #1F1A1A | bianco #FFFFFF | 17,20:1 |
| gesso #F3EEE6 | inchiostro #1F1A1A | 14,89:1 |

- **Rischio:** è la più vicina al "ristorante caldo e classico"; serve il disegno e la voce per non diventare generica.

### B. Il bianco e il rosso: Archivo stretto + Archivo

- **Caratteri:** Archivo 800 a larghezza 62% (asse `wdth`), maiuscolo, interlinea 0,9, per i titoli grandi, il nome, il telefono, i giorni; Archivo 400 a larghezza 100% per il testo e il menu. Una famiglia, due larghezze, nessun corsivo.
- **Perché:** viene dal disegno della casa, che dice da sé la palette: "il bianco lo chiameremo l'Angelo, il rosso il Diavolo". Il bastoni stretto e nero è quello dei cartelloni e delle insegne, e dei siti di osteria con più carattere: Roscioli (DIN bold maiuscolo fino a 128 px), Noble Rot (Futura bold nero, cornici nere), Brat (logo nero pieno su campo di colore). Regge i titoli brevi e le rime dell'oste scritte grandi, come un manifesto di serata. È la più lontana da tutti i concorrenti.
- **Palette:**

| Colore | Hex | Da dove | Uso |
|---|---|---|---|
| bianco | #FFFFFF | "il bianco... l'Angelo" | fondo principale |
| inchiostro | #151313 | | titoli e testo |
| rosso diavolo | #B8141C | il rosso #CD1719 del CSS attuale, scurito perché il bianco sopra superi 6,5:1 | metà rossa della fascia, pulsante Chiama, parole del titolo |
| azzurro angelo | #AAD5E3 | disegno | blocchi informativi (indirizzo, orari) |

| Testo | Fondo | Contrasto |
|---|---|---|
| inchiostro #151313 | bianco #FFFFFF | 18,51:1 |
| bianco #FFFFFF | rosso #B8141C | 6,66:1 |
| rosso #B8141C | bianco #FFFFFF | 6,66:1 |
| inchiostro #151313 | azzurro #AAD5E3 | 11,76:1 |
| azzurro #AAD5E3 | inchiostro #151313 | 11,76:1 |
| rosso #CD1719 (attuale) | inchiostro #151313 | 3,29:1: non si usa |

- **Rischio:** se il rosso diventa un blocco a tutta larghezza in ogni sezione il sito urla (la critica "troppo piatto" su Benvegnù veniva proprio dai blocchi rossi pieni). Il rosso resta su una fascia, un pulsante e qualche parola.

### C. Menu battuto: Josefin Sans + Courier Prime

- **Caratteri:** Courier Prime 400 e 700 per menu, orari, prezzi e le rime dell'oste; Josefin Sans 700 maiuscolo per i titoli.
- **Perché:** Septime scrive tutto con una macchina da scrivere e il menu diventa un foglio di sala; St. JOHN fa lo stesso con un solo serif da sistema (Georgia). L'osteria ha appesa una "Legge fondamentale del capo" battuta a macchina, e le rime dell'oste hanno il passo delle strofe: il foglio battuto è credibile. Courier Prime è la versione disegnata per lo schermo del Courier.
- **Palette:**

| Colore | Hex | Uso |
|---|---|---|
| carta | #FFFFFF | fondo |
| inchiostro | #1A1A1A | testo |
| matita | #57524E | note, orari secondari |
| rosso prezzi | #A3150F | prezzi, giorno di riposo |

| Testo | Fondo | Contrasto |
|---|---|---|
| inchiostro #1A1A1A | carta #FFFFFF | 17,40:1 |
| matita #57524E | carta #FFFFFF | 7,71:1 |
| rosso #A3150F | carta #FFFFFF | 7,86:1 |

- **Rischio:** senza prezzi confermati il menu battuto perde metà del senso; per paragrafi lunghi il monospazio stanca. Va usata come innesto (menu e orari), non come sistema intero.

### Raccomandazione per la fase 2.3

Base B ("il bianco e il rosso"): è l'unica che nasce da una frase dell'osteria stessa, è lontana da tutti i concorrenti e regge il disegno, le rime e le foto calde senza fondo crema. Da A si innesta il vino #800920 come fondo di una sola fascia (Ristorante o Orari), col testo bianco (10,62:1), per tenere il legame col sito attuale. Da C si innesta Courier Prime solo nel menu, se il cliente fornisce i prezzi. In tutte e tre: Josefin Sans mai per paragrafi, nessun corsivo, foto mai oltre la loro dimensione nativa.
