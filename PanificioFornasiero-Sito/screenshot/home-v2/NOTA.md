# Home versione 2 (scheda d'uso), Panificio Galileo Fornasiero, 2 novembre 2026

Pagina: `sito-v2/index.html` (statica, si apre con file:///), immagini in `sito-v2/img/` (WebP con srcset), caratteri in `sito-v2/fonts/`. Costruita sulla scheda `_prova/uso/SCHEDA.md`, non sulla home precedente (`sito/`, che resta com'è). Tutto si rifà con `bash _prova/uso/script/build_v2.sh` (immagini, screenshot, prove d'uso).

Screenshot (ora simulata lunedì 2 novembre 2026 alle 10.00, ora di Roma): `home-1440.jpg` (6361 px compreso il piede), `home-1440-prima-schermata.jpg`, `home-390.jpg` (7279 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, più `home-320.jpg`, `home-768.jpg`, `home-1024.jpg`. La pagina legge l'ora di Roma; per le prove si forza con `index.html?ora=2026-11-15T10:00`.

## Cosa è cambiato dopo le prove (2 novembre, sera)

Tre clienti tipo l'hanno provata (prima la home attuale, poi questa: voti 4, 3 e 3,5 prima, 8, 8 e 8 dopo) e il giudice d'identità ha dato 57 su 80, con la prima schermata a 1440 da rifare e la struttura d'uso da tenere. In più il committente ha chiesto più accoppiate di caratteri, più misure e impaginazioni mescolate. Cambiato:

**Uso**
- **Festivi e ferie.** Lo script conosce 1/1, 6/1, Pasqua e Pasquetta (calcolate), 25/4, 1/5, 2/6, 13/6 (Sant'Antonio, patrono di Padova), 15/8, 1/11, 8/12, 25/12, 26/12 e un elenco `FERIE` da riempire con il panificio, in cima allo script. In quei giorni non dice mai "aperto": "Oggi è festa: chiamate prima di passare." in bordeaux, i due negozi "Oggi è festa: chiedete l'orario al telefono" con il pallino grigio. Il giorno di riapertura salta domeniche, festivi e ferie (il 7/12 sera dice "Mercoledì apriamo alle 8.30", il 31/12 sera "Sabato apriamo alle 8.30 in via Alsazia 3"). Dal 20 al 31 dicembre sotto lo stato c'è "Sotto Natale gli orari possono cambiare: chiedete al telefono."
- **Ultimi 30 minuti.** "Aperti ora tutti e due i negozi: chiudiamo tra 5 minuti, alle 13.45." e "chiude alle 20.00, tra 15 minuti".
- **Mercoledì pomeriggio e sabato sempre in vista.** Sotto la riga "oggi" di ogni negozio c'è una riga fissa: via Vigonovese "Mercoledì pomeriggio chiuso. Sabato: chiamate."; via Alsazia "Sabato 8.30-13.30. Cellulare 338 660 06 64", con il cellulare come tel: alto 48 px. Il link "Tutti gli orari e il cellulare" non serve più ed è tolto. A 1440 l'orario non è più scritto tre volte: via la settimana in 15 px grigio, resta l'eccezione in 17 px color inchiostro.
- **"Negozi e orari" arriva sugli orari.** La chiusura non ha più la foto dei pani tondi né la citazione: il tocco porta su "Vieni a trovarci" e, nella stessa schermata a 390, su via Vigonovese con l'orario della settimana e via Alsazia con i suoi due numeri (provato: 2 negozi e 3 tel: visibili all'arrivo, a 390 e a 1440).
- **Chiama in testata.** Sotto i 1100 px la testata fissa ha "Chiama" (44 px) accanto a "Menu": porta all'apertura sui due negozi, con i due numeri, così nessuno chiama il negozio chiuso. Da 1100 px c'è il tel: 049 870 26 58 a destra del menu.
- **Fascia delle Feste con il numero.** A 390 la fascia bordeaux ha il bottone bianco "Chiama 049 870 26 58" (48 px) e "Come si prenota"; finisce a 796 px su 844. Il testo non promette più "adesso": "Panettone e focaccia di Natale: si prenotano in negozio o al telefono." Dal 15 dicembre: "chiamate per sapere se c'è ancora posto."; il 23 dicembre alle 13 la fascia si spegne. A Pasqua lo stesso (dai 7 giorni prima "chiamate per sapere", si spegne il sabato alle 13). Le date stanno in tre variabili in cima allo script (`NATALE_DA`, `FINE_PRENOTAZIONI`, `SPEGNI`). Con JavaScript spento la fascia c'è comunque, con una frase vera tutto l'anno: "Natale e Pasqua: panettone, colomba e focacce si prenotano in negozio o al telefono."
- **Feste.** "Pezzature, prezzi e ultimo giorno utile: chiedete al banco o al telefono. Al telefono vi diciamo anche dove ritirare." (dove si ritira non è pubblico, quindi non lo scrivo). Il link "Via Alsazia: 049 870 51 07" è alto 48 px; la foto del panettone a 390 è 4:3, e arrivando dalla fascia i due tel: stanno interi nella schermata (673-725 e 735-783 px).
- **Didascalia sulla vetrina.** A 390 sotto la striscia: "Via Vigonovese 116, vicino al semaforo"; da 600 px "La nostra vetrina in via Vigonovese 116, vicino al semaforo. Galileo e Fidalma sulla porta." Nella chiusura via Vigonovese è "Laboratorio e negozio, con l'insegna di legno, vicino al semaforo". I due forni vicini non li nomino.
- **Mappa di via Alsazia** con il nome: `query=Panificio Fornasiero Via Alsazia 3 Camin 35127 Padova`. Google Maps nel browser di prova risponde 429: che la scheda del negozio esista va controllato (se non c'è, Google mostra comunque l'indirizzo).
- **Testo di riserva dello stato** (JavaScript spento): "Aperti dal lunedì al venerdì, mattina e pomeriggio (via Vigonovese chiusa il mercoledì pomeriggio). Il sabato mattina in via Alsazia 3."
- **Forniture.** Voce di menu "Forniture e consegne". La sezione è solo testo: la loro frase sulla fornitura, poi "Per decenni abbiamo dato il pane a tante aziende della zona, agli operai delle Officine Meccaniche Stanga e della Snia Viscosa." in prima persona, senza la testata del giornale; sopra i bottoni, in corpo normale, "Chiamate per sapere se arriviamo fino a voi, in che giorni e a che ora."; "Chiama il laboratorio" e "Vedi i pani che facciamo"; l'indirizzo email scritto in chiaro e cliccabile, con oggetto "Fornitura pane" e la traccia; a parte "Anche per le famiglie: offriamo consegne a domicilio in zona Camin e dintorni".
- **Pane.** "più di 30 tipi di pane [...] Tra questi:" prima dell'elenco e "E altri pani secondo la giornata: chiedete in negozio o al laboratorio." dopo; i 15 pani in tre colonne da 5 a 1440: dopo il clic su "Il pane" i 20 nomi stanno tutti in 900 px.
- **Niente pagine vuote.** I link a `storia.html`, `fornitura.html`, `bacheca-di-romina.html`, `privacy-policy.html`, `cookie-policy.html` sono tolti: Bacheca, Privacy e Cookie puntano alle pagine del sito di oggi, "Chi siamo" e "Forniture e consegne" alle ancore.
- **Niente modulo degli avvisi.** "Gli avvisi di Romina" era un servizio che non esiste e prometteva una cosa che non fa. Al suo posto: "Le prenotazioni di Natale e di Pasqua si fanno al telefono: 049 870 26 58. Per sapere quando si aprono, seguiteci su Instagram." Newsletter quindi no: i loro clienti telefonano e le loro notizie (le prenotazioni) passano dal banco e da Instagram; si può aggiungere solo se lo chiedono e con un servizio collegato.

**Identità**
- **Prima schermata a 1440 rifatta** (era testo a sinistra e foto a destra, da modello). Ora è la vetrina di via Vigonovese, 640x319 a misura nativa, centrata su un passe-partout del grigio caldo del sacchetto in ombra (#F3EFE8), con sopra "Panificio Fornasiero, a Camin dal 1963" e sotto la didascalia; sotto ancora, centrata, la frase di stato in 34 px, poi i due negozi in due colonne (Chiama e Mappa ciascuno), poi la fascia bordeaux, che finisce a 890 px su 900. Da 680 px in su vale la stessa impaginazione, così la foto non viene mai ingrandita (prima a 768 era stirata a tutta larghezza). Le tartarughe restano solo nella sezione del pane.
- **Citazioni dal giornale: da sei a due**, firmate solo con il nome: Fidalma sulle focacce nelle Feste e Galileo "Siamo Fornasiero, fornai anche nel nome" in Chi siamo. Via la frase a 50 px della chiusura ("Non abbandonerei mai Camin"), via la testata e la data del Mattino sotto ogni frase (le fonti restano in `01-analisi.md` e nella scheda). Nei panini imbottiti le loro parole del sito: "Con vasta scelta di affettati misti."
- **Chiusura con le loro parole**: "Vieni a trovarci" è il titolo della sezione orari del loro sito.
- **Didascalie**: tolte quelle che ripetevano la foto ("Pane a fette nel cesto del banco...", "il pane con la crosta a squame", "Plumcake negli stampi"); restano "Tartarughe" e "La focaccia, sul sacco dei cinquant'anni: 1963-2013".
- **"I nostri pani padovani"** al posto di "I pani con il nome di casa".
- **Testata**: solo "FORNASIERO", come sull'insegna; la data la porta il titolo.
- **Bacheca**: una sola foto, il pan di Spagna, a 240 px (112 a 390) accanto al testo di Romina; via tortino e plumcake.

**Alta gamma, e la richiesta di mescolare caratteri, misure e impaginazioni** (ripresa la sera del 2 novembre, sezione per sezione; la prima schermata a 390 e a 1440 non è stata toccata)
- **Tre voci con un compito fisso ciascuna.** Josefin Sans è la voce dell'insegna: il nome in testata in corsivo spaziato (messo accanto alla foto, ricalca le lettere dipinte sopra la vetrina), le etichette maiuscole e le date grandi di Chi siamo. Erode per titoli, nomi dei negozi e dei pani, citazioni; Fira Sans per testo, stato, orari, telefoni e bottoni. Mai due caratteri nello stesso paragrafo. Perché queste: vedi "Caratteri e colori".
- **Misure mescolate, con contrasti voluti dentro la stessa sezione**: nel pane il titolo scende a 44 px e i cinque pani padovani salgono a 80 px (erano 50), sopra un elenco a 17 px; in Chi siamo il titolo è a 34 px, la frase di Galileo a 58 px (era 40) e le quattro date a 96 px (erano 64) con le righe sotto a 16 px; "Vieni a trovarci" a 96 px accanto ai telefoni a 28 px. Il titolo d'apertura resta a 46 px, perché il dato più forte della prima schermata è lo stato a 34 px.
- **Un'impaginazione diversa per ogni sezione, mai due uguali di fila** (prima il pane e Chi siamo ripetevano la griglia 5 e 7 delle Feste, con la foto ancora a sinistra):
  1. apertura: centrata e simmetrica, la vetrina a misura nativa sul passe-partout (invariata);
  2. fascia delle Feste: una riga a tutta larghezza (invariata);
  3. Feste: titolo su una riga intera, sotto la foto del panettone a filo del bordo sinistro (7 parti) e il testo a destra (5);
  4. pane, nuovo: tipografica, come la lavagna del banco. Titolo piccolo e frase, poi i cinque nomi su tutta la larghezza a 80 px; sotto, metà e metà: l'elenco in tre colonne e il forno in due a sinistra, le tartarughe a destra a filo del bordo destro. A 768-1099 i cinque nomi uno sotto l'altro a sinistra e la foto a destra; a 390 i nomi uno per riga a 36 px, senza virgole;
  5. Chi siamo, nuovo: una frase grande da sola, tutto centrato sul grigio caldo (titolo piccolo, frase di Galileo, firma, le quattro date in fila); a 390 resta a sinistra, con la frase a 26 px e le date a 48;
  6. forniture: titolo su una riga intera e due colonne disuguali sotto, solo testo (invariata);
  7. Bacheca: una nota piccola e centrata, 1000 px, con una foto da anteprima (invariata);
  8. chiusura: titolo enorme a sinistra, i due negozi a destra (invariata).
- **Pagina**: 6361 px a 1440 (era 5695; resta tra 4500 e 7000) e 7279 a 390 (era 7129). Dopo il clic su "Il pane" a 1440 i 20 nomi stanno ancora tutti nei 900 px.

## Per ogni visitatore della scheda: cosa trova e dove

**1. Il cliente di Camin (telefono, spesso anziano, di fretta).** Nei primi 844 px a 390, senza scorrere: la vetrina con l'insegna e la didascalia; "Panificio Fornasiero, a Camin dal 1963"; lo stato in corpo 21 (finisce a 355 px); i due negozi con "oggi", l'eccezione della settimana, "Chiama" con il numero di quel negozio (52 px) e "Mappa" (52 px), il cellulare di via Alsazia (48 px); la fascia delle Feste in stagione (fino a 796 px). In testata "Chiama" e "Menu".

**2. Chi prenota le Feste (telefono, novembre e dicembre).** La fascia in prima schermata con il bottone per chiamare. Un tocco su "Come si prenota" porta alla foto del panettone tagliato sul sacco di juta, "Non è Natale senza i panettoni e le focacce" (le parole della Bacheca), la ricetta di Galileo, come si prenota, pezzature e prezzi da chiedere, "Chiamaci e ordina: 049 870 26 58" e via Alsazia, la frase di Fidalma e la focaccia sul sacco dei cinquant'anni. Fuori stagione la fascia sparisce e la sezione, "Natale e Pasqua", scende dopo il pane.

**3. Il gestore di bar, ristorante o albergo (computer).** "Forniture e consegne" in testata, un clic; la sezione con la frase loro, la Stanga e la Snia, la domanda da fare al telefono, "Chiama il laboratorio", l'elenco dei pani a un clic, la mail scritta in chiaro con l'oggetto, le consegne alle famiglie.

## Caratteri e colori

Scala a 1440 (dieci livelli, ognuno con un compito): 14-15 px didascalie, etichette e riga legale; 16-17 px piede, elenchi, orari; 19 px testo delle sezioni; 24-28 px nomi dei negozi, telefoni della chiusura, fascia; 34 px stato e titolo di Chi siamo; 44-46 px titolo d'apertura e del pane; 52-60 px titoli di Forniture e Feste; 58 px la frase di Galileo; 80 px i pani padovani; 96 px le date e "Vieni a trovarci". A 390: 14, 16-17, 21 (stato), 26-27 (titolo, frase di Galileo), 32 (titoli), 36 (pani padovani), 40 (chiusura), 48 (date).

- Josefin Sans (Santiago Orozco, Typemade; Google Fonts, SIL Open Font License 1.1), file variabile latin, dritto e corsivo: la voce dell'insegna (nome in testata, etichette, date).
- Erode 400 e 500 (Indian Type Foundry, Fontshare, ITF Free Font License, uso commerciale gratuito): titoli, nomi dei negozi e dei pani, citazioni; mai in corsivo.
- Fira Sans 400, 500 e 600 (Carrois Apostrophe per Mozilla, Google Fonts, SIL Open Font License 1.1): testo, stato, orari, bottoni, piede; cifre tabellari, zero senza barra.
- Perché questa accoppiata, per un panificio di quartiere: le loro tre scritture sono l'insegna di legno (maiuscole bastone spaziate, in corsivo: Josefin Sans ha la stessa geometria anni Trenta), il sacchetto e il logo a cesto (un serif caldo da stampa di bottega: Erode, con le grazie morbide e il contrasto basso, regge i nomi dei pani grandi senza diventare da galleria) e le cose da leggere in fretta, cioè orari e numeri, per clienti spesso anziani al telefono (Fira Sans: occhio grande, cifre chiare e tabellari, molto leggibile a 16-21 px). Niente corsivo serif, niente Inter, nessun carattere delle liste da evitare.
- I file sono serviti dalla pagina in `sito-v2/fonts/` (copie scaricate in `_prova/crawl/fonts-josefin/`). Nessun carattere delle liste da evitare della guida.
- Colori (contrasti WCAG): carta del sacchetto #FBFAF7 con inchiostro bruno #2A1E17 (15,5:1) e testo secondario #5C4A3E (8,0:1); passe-partout e Chi siamo #F3EFE8 (il sacchetto in ombra); legno dell'insegna #4A2E1F per testata, bottoni e piede (bianco sul legno 12,3:1; #D8C6B3 e #E7DACB sul legno oltre 7:1); bordeaux della scritta "Fornasiero dal 1963" #733129 per la fascia delle Feste, le date e lo stato "chiuso" (bianco sul bordeaux 9,5:1); verde #2C6A3C solo per "aperto" (6,2:1). Il fondo non è un beige di comodo: è il bianco del loro sacchetto e il legno della loro insegna.

## Interazione

Un solo gesto, quello che serve: la pagina sa che ora e che giorno è a Camin e lo dice, festivi compresi. Dove l'orario non è scritto (sabato di via Vigonovese, domenica, festivi, Natale) la pagina non dice "chiuso" né "aperto" ma "chiedete l'orario al telefono". Il menu del telefono è un vero bottone con aria-expanded e si chiude toccando una voce. Transizioni solo di colore; niente comparse allo scorrere, niente effetti al cursore.

## Foto, origine e licenza

Tutte del Panificio Galileo Fornasiero, prese dal loro sito (`assets/originali/`, voti in `_prova/inventario-immagini.json`). Nessuna foto di repertorio, nessuna immagine generata. Trattamento in `_prova/uso/script/v2_img.py`.
- Apertura: la vetrina con Galileo e Fidalma (`617993_02eb45f6...`), 640x319, a misura nativa da 680 px; a 390 la striscia 640x262 dello stesso file.
- Feste: il panettone tagliato (`b56ebf_5b27b00f...`, Nikon D3300, dicembre 2020) e la focaccia sul sacco del cinquantesimo (`b56ebf_fabcdffb...`).
- Pane: le tartarughe nel cesto davanti al sacchetto "Fornasiero srl Camin-Padova" (`617993_28aa18bc...`).
- Bacheca: il pan di Spagna con le albicocche (`b56ebf_c01687dd...`), da telefono, solo piccolo.
- Logo nel piede: il logo a cesto del sito a una tinta crema, PNG a 2x e 3x; non ricostruito in SVG perché il disegno ha ombre e sfumature.
- Tolte dopo le prove: pane a fette (`617993_f35f170e...`), panini (`617993_f2c61f63...`), pani tondi della chiusura (`617993_f78248a8...`), tortino e plumcake della Bacheca.
Per usarle nel sito nuovo serve il loro consenso (va chiesto insieme a quello per la foto con Galileo e Fidalma).

## Piede

Logo e una riga su chi sono; la riga sulle prenotazioni al telefono e Instagram (al posto della newsletter, vedi sopra); quattro colonne: Il panificio (Chi siamo, Forniture e consegne, La Bacheca di Romina sul sito di oggi), Prodotti (ancore della home), I negozi (i due telefoni, gli orari, la mail), Seguici (solo Instagram, l'unico social collegato dal loro sito); riga legale con ragione sociale, indirizzo, P.IVA, Privacy e Cookie (pagine del sito di oggi). A 390 Il panificio e Prodotti stanno affiancati, poi I negozi a tutta larghezza e Seguici: l'ordine resta quello. Nella testa della pagina c'è il dato strutturato con i due negozi, CAP 35127 e orari.

## Controlli (2 novembre 2026, dopo le prove)

- Screenshot guardati a pezzi: 1440 intera e prima schermata, 390 intera e prima schermata, 320, 640, 690, 768, 1024; dopo il nuovo impianto del pane e di Chi siamo di nuovo 1440, 390, 320, 768 e 1024 (nessuna sovrapposizione, nessuno scorrimento orizzontale, prima schermata a 390 con le stesse misure: stato a 355 px, quattro tel: e due mappe, fascia a 796).
- Prove d'uso (`_prova/uso/script/v2_prova.mjs`): stato a 26 ore e giorni diversi, tra cui lunedì 13.40 e 14.15, mercoledì 14.30 e 17.00, venerdì 20.30, sabato 7.30, 10.00 e 14.00, domenica, 8/12, 24/12, 25/12, 31/12 sera, 1/1, 6/1, Pasquetta 2027, 25/4, 13/6, 15/8: nei festivi nessun pallino verde e nessun "aperto". A 390x844 il 15 novembre: quattro tel: (52, 48, 52 e 48 px) e due mappe (52 px) nei primi 844 px, le due eccezioni della settimana visibili, la fascia finisce a 796. Feste il 14/12, il 16/12, il 23/12 alle 12 e alle 14, il 15/6, il 20/3 e il 25/3/2027; con JavaScript spento. Arrivo da "Negozi e orari", "Il pane", "Forniture e consegne", "Chiama" a 390 e a 1440.
- Nessuno scorrimento orizzontale a 320, 360, 390, 430, 599, 600, 768, 1024, 1099, 1100, 1280, 1440, 1920, 2560 (a 600 c'era: i due negozi affiancati non ci stavano, ora si affiancano da 720); nessuna ancora rotta; nessun link a pagine locali che non esistono.
- Segnali da IA (`_metodo/kit/segnali.sh` a 1440): 1 soglia da correggere su 10, l'area delle foto, al 16,8 % (era 35,1 % prima delle prove; la foto delle tartarughe ora è a metà pagina invece che a 5 parti su 12, ma la pagina è più lunga) perché ho tolto le tre foto con la stessa inquadratura del cesto, come chiesto dal giudice d'identità. Non la rialzo con altre foto uguali o di repertorio: la rialzano le riprese elencate nel LEGGIMI. Titolo a sinistra e paragrafo a destra: 1 sezione (la chiusura; il pane non lo è più). Da guardare: 5 fasce di fondo (passe-partout, fascia delle Feste, Chi siamo, piede, e la carta), le quattro date grandi (sono il contenuto), tre famiglie di caratteri (ognuna con un compito fisso, per la richiesta del committente).
- Divieti del committente: nessun gradiente, nessuna icona, nessuna card con ombra, niente vetro, niente corsivo serif, niente badge, niente dissolvenze, niente legende numerate, nessun oggetto scontornato.
- Nessun carattere U+2014 in pagina, negli script e in questa nota.

## Cosa resta da confermare

- Il sabato di via Vigonovese e le domeniche dei due negozi (la pagina dice "chiamate"), le ferie (da scrivere in `FERIE`), gli orari dei festivi e di Natale; se il 13 giugno chiudono davvero (Sant'Antonio è festa solo a Padova).
- Se via Alsazia 3 è ancora aperta, chi risponde al 338 660 06 64, e se su Google Maps c'è la scheda del negozio di via Alsazia.
- Le date delle prenotazioni di Natale e Pasqua (inizio, 15 dicembre e 23 dicembre alle 13 sono scelte mie), se si possono dire pezzature e prezzi, e dove si ritira (in tutti e due i negozi?).
- Il consenso a usare le loro foto, la foto della vetrina con Galileo e Fidalma e i loro nomi, e le due frasi dette al Mattino di Padova; come vogliono essere nominati.
- Se la ricetta di Galileo vale anche per colomba e focaccia di Pasqua (in pagina è scritta solo per il Natale).
- "Più di 30 tipi di pane" (il sito ne elenca 20) e quali si fanno ogni giorno.
- Fornitura e consegne: zona, giorni, quantità minime, se le consegne alle famiglie e il pane con il Mattino ai clienti anziani esistono ancora.
- Il marchio da usare (logo a cesto, insegna, scritta del sacchetto) e un file vettoriale; REA (companyreports dice PD 235130, serve una visura), PEC e capitale sociale per la riga legale.
- Instagram è ancora attivo? La pagina Facebook trovata in ricerca è loro? Vogliono un servizio di avvisi per email?
