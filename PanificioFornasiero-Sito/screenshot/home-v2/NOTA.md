# Home versione 2 (scheda d'uso), Panificio Galileo Fornasiero, 2 novembre 2026

Pagina: `sito-v2/index.html` (statica, si apre con file:///), immagini in `sito-v2/img/` (WebP con srcset), caratteri in `sito-v2/fonts/`. Costruita sulla scheda `_prova/uso/SCHEDA.md`, non sulla home precedente (`sito/`, che resta com'è). Tutto si rifà con `bash _prova/uso/script/build_v2.sh` (immagini, screenshot, prove d'uso).

Screenshot (ora simulata lunedì 2 novembre 2026 alle 10.00, ora di Roma): `home-1440.jpg` (5695 px compreso il piede), `home-1440-prima-schermata.jpg`, `home-390.jpg` (7129 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, più `home-320.jpg`, `home-768.jpg`, `home-1024.jpg`. La pagina legge l'ora di Roma; per le prove si forza con `index.html?ora=2026-11-15T10:00`.

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

**Alta gamma, e la richiesta di mescolare caratteri, misure e impaginazioni**
- **Tre voci con un compito fisso ciascuna.** Aggiunta Josefin Sans come voce dell'insegna: il nome in testata in corsivo spaziato (messo accanto alla foto, ricalca le lettere dipinte sopra la vetrina), le etichette maiuscole e le date grandi di Chi siamo. Erode resta per titoli, nomi dei negozi e dei pani, citazioni; Fira Sans per testo, stato, orari, telefoni e bottoni. Mai due caratteri nello stesso paragrafo.
- **Misure mescolate**: a 1440 "Vieni a trovarci" a 96 px, i pani padovani a 50 px in una riga sola con le virgole, la citazione di Galileo a 40 px, le date in Josefin a 64 px, le etichette a 14-15 px; il titolo d'apertura sta volutamente a 46 px, perché il dato più grande e più forte della prima schermata è lo stato.
- **Un'impaginazione diversa per ogni sezione**: apertura centrata e simmetrica sul passe-partout; Feste asimmetriche con la foto a filo del bordo (7 e 5); pane con la foto a sinistra e l'elenco come una lavagna a tre misure; Chi siamo solo parole su fondo grigio caldo, con la citazione grande e le quattro date in fila; forniture con il titolo su una riga intera e due colonne disuguali sotto; Bacheca come una nota piccola e centrata; chiusura con il titolo enorme a sinistra e i due negozi a destra.
- **Pagina più corta**: 5695 px a 1440 (era 6987) e 7129 a 390 (era 9139). Le foto con la stessa inquadratura (cesto, pangrattato, sacchetto) sono passate da quattro a una.

## Per ogni visitatore della scheda: cosa trova e dove

**1. Il cliente di Camin (telefono, spesso anziano, di fretta).** Nei primi 844 px a 390, senza scorrere: la vetrina con l'insegna e la didascalia; "Panificio Fornasiero, a Camin dal 1963"; lo stato in corpo 21 (finisce a 355 px); i due negozi con "oggi", l'eccezione della settimana, "Chiama" con il numero di quel negozio (52 px) e "Mappa" (52 px), il cellulare di via Alsazia (48 px); la fascia delle Feste in stagione (fino a 796 px). In testata "Chiama" e "Menu".

**2. Chi prenota le Feste (telefono, novembre e dicembre).** La fascia in prima schermata con il bottone per chiamare. Un tocco su "Come si prenota" porta alla foto del panettone tagliato sul sacco di juta, "Non è Natale senza i panettoni e le focacce" (le parole della Bacheca), la ricetta di Galileo, come si prenota, pezzature e prezzi da chiedere, "Chiamaci e ordina: 049 870 26 58" e via Alsazia, la frase di Fidalma e la focaccia sul sacco dei cinquant'anni. Fuori stagione la fascia sparisce e la sezione, "Natale e Pasqua", scende dopo il pane.

**3. Il gestore di bar, ristorante o albergo (computer).** "Forniture e consegne" in testata, un clic; la sezione con la frase loro, la Stanga e la Snia, la domanda da fare al telefono, "Chiama il laboratorio", l'elenco dei pani a un clic, la mail scritta in chiaro con l'oggetto, le consegne alle famiglie.

## Caratteri e colori

- Josefin Sans (Santiago Orozco, Typemade; Google Fonts, SIL Open Font License 1.1), file variabile latin, dritto e corsivo: la voce dell'insegna (nome in testata, etichette, date).
- Erode 400 e 500 (Indian Type Foundry, Fontshare, ITF Free Font License, uso commerciale gratuito): titoli, nomi dei negozi e dei pani, citazioni; mai in corsivo.
- Fira Sans 400, 500 e 600 (Carrois Apostrophe per Mozilla, Google Fonts, SIL Open Font License 1.1): testo, stato, orari, bottoni, piede; cifre tabellari, zero senza barra.
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

- Screenshot guardati a pezzi: 1440 intera e prima schermata, 390 intera e prima schermata, 320, 640, 690, 768, 1024.
- Prove d'uso (`_prova/uso/script/v2_prova.mjs`): stato a 26 ore e giorni diversi, tra cui lunedì 13.40 e 14.15, mercoledì 14.30 e 17.00, venerdì 20.30, sabato 7.30, 10.00 e 14.00, domenica, 8/12, 24/12, 25/12, 31/12 sera, 1/1, 6/1, Pasquetta 2027, 25/4, 13/6, 15/8: nei festivi nessun pallino verde e nessun "aperto". A 390x844 il 15 novembre: quattro tel: (52, 48, 52 e 48 px) e due mappe (52 px) nei primi 844 px, le due eccezioni della settimana visibili, la fascia finisce a 796. Feste il 14/12, il 16/12, il 23/12 alle 12 e alle 14, il 15/6, il 20/3 e il 25/3/2027; con JavaScript spento. Arrivo da "Negozi e orari", "Il pane", "Forniture e consegne", "Chiama" a 390 e a 1440.
- Nessuno scorrimento orizzontale a 320, 360, 390, 430, 599, 600, 768, 1024, 1099, 1100, 1280, 1440, 1920, 2560 (a 600 c'era: i due negozi affiancati non ci stavano, ora si affiancano da 720); nessuna ancora rotta; nessun link a pagine locali che non esistono.
- Segnali da IA (`_metodo/kit/segnali.sh` a 1440): 1 soglia da correggere su 10, l'area delle foto, scesa al 16,9 % (era 35,1 %) perché ho tolto le tre foto con la stessa inquadratura del cesto, come chiesto dal giudice d'identità. Non la rialzo con altre foto uguali o di repertorio: la rialzano le riprese elencate nel LEGGIMI. Da guardare: 5 fasce di fondo (passe-partout, fascia delle Feste, Chi siamo, piede, e la carta), le quattro date grandi (sono il contenuto), tre famiglie di caratteri (ognuna con un compito fisso, per la richiesta del committente).
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
