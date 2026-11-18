# Bazzato, home finale: "Il ponte"

Costruita sulla bozza B, quella scelta dal committente. Restano l'idea, la prima schermata (la foto dell'officina a tutta larghezza con il titolo grande sul pavimento), il trattamento delle foto, il carattere e i colori della bozza; sono cambiati l'esecuzione, i dati, il telefono, i dettagli. Pagina: `sito/index.html`. Si rifà tutto con `bash _prova/script/build_finale.sh`.

Screenshot: `home-1440.jpg` (4677 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (4430 px), `home-390-prima-schermata.jpg` e `chiusura-1440.jpg` (solo la chiusura a 1440, dalla sezione dei contatti alla fine). Sono fatti con l'ora fissata a martedì 20/10/2026 alle 10.30 (`?ora=2026-10-20T10:30`). Senza il parametro la pagina usa l'ora vera di Vigonovo.

## Idea

L'officina com'è, chiara e dritta: un'auto alzata sul ponte, il pavimento a piastrelle, la luce dei neon. Sul pavimento il titolo e, accanto al bottone per chiamare, la cosa che solo questa pagina sa dire: se l'officina di viale Serenissima è aperta adesso e fino a che ora. Il resto della pagina dice che lavori fanno, quanto costano, quanto ci vuole per la revisione e dove sono.

## Le prime due schermate

- **1440, prima schermata.**
  - Testata su fondo chiaro: "Bazzato Autofficina", tre voci di menu e il telefono.
  - Sotto, la foto dell'officina a tutta larghezza fino al fondo dello schermo, con un taglio più stretto di prima: l'auto sul ponte è più grande (circa 260 px su 1440 invece di 230).
  - Sul pavimento, in basso a sinistra, il titolo "Officina multimarca a Tombelle" (General Sans 500, 117 px, spaziatura -0,04em, interlinea 0,93). Sotto, a sinistra, una frase con i lavori, la revisione in sede in circa 45 minuti a € 79 e l'indirizzo.
  - A destra della frase, lo stato dell'officina in grande (29 px, peso 500, punto azzurro): "Aperto, chiude alle 12.00". Sotto, il bottone nero "Chiama 049 9830115" e "Scrivi su WhatsApp". "Foto indicativa" nell'angolo.
- **1440, seconda schermata.** Una frase su chi sono ("L'officina di Andrea e Paolo Bazzato a Tombelle, tra Padova e Venezia, per auto di ogni marca. Prima il preventivo, alla fine il resoconto di ogni operazione fatta.") e due fatti in una riga, col filetto nero sopra e senza icone: Eurorepar Car Service e Auto sostitutiva.
- **390.** Taglio verticale della stessa foto, con l'auto in alto e il titolo su tre righe sul pavimento, sotto il ponte e non sopra. Poi la frase (senza l'indirizzo, che è più giù in "Dove siamo"), lo stato in grande (22 px), il bottone nero e WhatsApp. In testata il nome e il telefono. A 320 tutto sta nella prima schermata e l'auto resta intera.
- **Poi, cinque blocchi in tutto:**
  - "Lavori e prezzi" sul foglio bianco: sette righe, con il prezzo o "a preventivo" dove manca;
  - la revisione in sede: il titolo a sinistra e, accanto, la scheda Prezzo / Pre-revisione / Appuntamenti / Prima revisione / Poi;
  - la chiusura (stile B, "con foto"): la frase "L'officina di Andrea e Paolo Bazzato, per auto di ogni marca." con i recapiti accanto, poi l'unica foto grande dopo l'apertura, l'auto bianca intera alzata sul ponte, a tutta larghezza fino al piede;
  - il piede in una riga sola: ragione sociale, P.IVA, REA e informativa privacy.

## La chiusura: stile B, "con foto" (20/10/2026)

Storia. Le chiusure di tutte le home della campagna erano uguali (titolo di luogo, telefono gigante su fascia scura, colonnine, piede nero a quattro colonne). Sono state rifatte come "un oggetto del mestiere disegnato che porta i recapiti": qui era la scheda di accettazione dell'officina, un foglio bianco rigato con le caselle. Il committente le ha bocciate tutte. Gli sono stati mostrati due campioni su Hambro e su Bazzato (`_prova/chiusure-campioni/`, foglio `confronto.jpg`: A tipografica, B con foto) e ha scelto **B, con foto**. Questa è la chiusura del campione B di Bazzato portata nel sorgente (`_prova/script/finale_pagina.html`) così com'è: stessa frase, stessa foto, stessa impaginazione.

- **La frase**: "L'officina di Andrea e Paolo Bazzato, per auto di ogni marca." (General Sans 500, 72 px a 1440, 36 px sul telefono, spaziatura -0,036em), a sinistra su 7 colonne di 12. È la loro presentazione, presa dalla frase della seconda schermata: chiude la pagina con i nomi dei titolari invece che con un titolo di luogo.
- **I recapiti**, a destra della frase e allineati al suo piede, a corpo di testo e senza etichette: il telefono a 34 px sottolineato (`tel:`), "Scrivi su WhatsApp o info@bazzato.it", l'indirizzo "Viale Serenissima 3, 30030 Vigonovo (VE)" che apre Google Maps, "Dal lunedì al venerdì, 08.00-12.00 e 14.00-18.00" e "Sabato chiuso" in grigio. Le fasce orarie non si spezzano mai a metà.
- **La foto**: sotto, a tutta larghezza fino al piede, l'auto bianca intera alzata sul ponte nell'officina luminosa (alta 835 px a 1440, 58 % della larghezza; 5:4 sul telefono), con "Foto indicativa" in basso a destra (#3F3E3A sul pavimento chiaro, almeno 6,9). È la foto che prima stava a metà pagina fra il listino e la revisione: ora c'è una sola volta, in fondo, e la pagina non ha una foto in più.
- **Il piede**: invariato, una riga sola sul cemento in grigio (6,4): Bazzato snc di Bazzato Andrea e Paolo & C., P.IVA e C.F. 03599300278, REA VE 322146, Informativa privacy. La PEC non c'è perché non è stata trovata (LEGGIMI, punto 11).
- **Sotto 1100 px** la frase prende tutta la riga e i recapiti vanno sotto, a sinistra; a 390 e a 320 tutto in colonna, la foto 5:4.
- **Cosa è stato tolto**: la scheda di accettazione (foglio rigato, caselle, croce disegnata, bottone "Prenota la revisione"). Restano veri e in pagina tutti i dati: la revisione, il prezzo, la pre-revisione gratis e gli orari degli appuntamenti sono nella sezione "Revisione" con "Per prenotare: 049 9830115"; gli orari degli uffici nel pannello dello stato in apertura.
- **Difetti corretti rispetto al campione**: fra la revisione e la frase restavano 288 px di cemento vuoto (prima li separava la foto); ora la chiusura comincia 40 px sotto la fine della revisione (24 px sul telefono), con lo stesso respiro fra le altre sezioni. Tolte le regole CSS della vecchia banda foto e della scheda, che non servivano più; le due regole sotto 1100 px sono nel blocco delle altre.
- **Altezza**: la chiusura è alta 1277 px a 1440 (`chiusura-1440.jpg`); la pagina passa da 5121 a 4677 px.

## Caratteri e colori

- **General Sans** di Indian Type Foundry (Fontshare), nei pesi 400, 500 e 600: una sola famiglia.
  - I file woff2 vengono dal pacchetto ufficiale (`_prova/crawl/fontshare/zip/GeneralSans_Complete/`), non sono modificati e la pagina li serve da `sito/fonts/`.
  - Licenza: ITF Free Font License 2.0 (`sito/fonts/FFL.txt`). L'uso commerciale è gratuito, anche con i file ospitati sul proprio server (sezione 01). I file però non si modificano e non si cedono a terzi (sezione 02): chi pubblica il sito per Bazzato scarica la sua copia da fontshare.com.
- **Perché General Sans**: è un grottesco sobrio, né tecnico né di moda. Il titolo corto, grande e chiaro, in basso sulla foto luminosa, viene da Lunaz (un oggetto vero in luce morbida, un titolo corto in basso a sinistra) e da Polestar (testo diretto in italiano, carattere sobrio).
- **Scala**: titolo 117 px; titoli di sezione 80 e 56 px; frase d'apertura 41 px; stato dell'officina 29 px; testo 18-19 px; didascalie 13-14 px. Spaziatura negativa sui titoli.
- **Cifre**: General Sans non ha le cifre tabellari, quindi nella colonna dei prezzi le cifre sono messe a larghezza uguale da poche righe di script, senza toccare il file del carattere. Fra "€" e la cifra c'è uno spazio che non va a capo.
- **Colori**:
  - cemento chiaro #F0EEEA per la pagina (prima #E9E8E4: stesso colore della bozza, più luminoso), il foglio bianco #FFFFFF solo sotto il listino (l'unica variazione di fondo);
  - nero #111111 per il testo, grigio #56554F per il testo secondario (contrasto 6,4 sul cemento e 7,5 sul bianco), filetti #C9C7C1;
  - l'azzurro del loro logo, #00C3EF, solo nel punto dello stato "aperto";
  - il bottone è nero e al passaggio diventa petrolio pieno #00667E (6,6 con il bianco), subito, senza dissolvenza.

## Interazione

Il gesto è uno solo: lo stato dell'officina, calcolato con l'ora di Roma, ora dentro l'apertura accanto al bottone per chiamare.
- **Cosa dice**: "Aperto, chiude alle 12.00", "Pausa, riapre alle 14.00", "Chiuso, riapre lunedì alle 08.00", "Chiuso per ferie, riapre il 24 agosto".
- **Chiusure**: legge un elenco modificabile in cima allo script, con le ferie (oggi c'è quella del 6-21 agosto 2026 presa dal sito), i festivi nazionali e Pasquetta, che si calcola da sola. Così ad agosto non dice "Aperto". Se una chiusura inizia entro 45 giorni, il pannello degli orari la annuncia.
- **Il pannello**: lo stato è un bottone che apre, sopra di sé, il pannello degli orari di officina e uffici, con il numero. Si apre con clic, dito, Invio o Spazio; si chiude con Esc (il fuoco torna al bottone) o toccando fuori.
- **Niente movimento**: nessuna transizione, nessuna animazione allo scorrimento, nessun effetto che segue il cursore.
- **Prove** (`_prova/script/prova_stato.mjs`): 13 orari e giorni diversi (prima delle 8, pausa, venerdì sera, sabato, Ognissanti di domenica, vigilia di Natale, Pasquetta 2027, ferie), tutti giusti; tastiera (Invio apre, Esc chiude e il fuoco torna al bottone); dito a 390 (apre, tocco fuori chiude) e a 320 (il pannello sta tutto nella finestra, da 64 a 518 px).

## Foto: origine e licenza

Nessuna foto dell'azienda regge (voti da 1 a 5 su 10 in `_prova/inventario-immagini.json`). Le due foto sono segnaposto con licenza libera, verificata sulla pagina di ogni foto, e nessuna è usata in un'altra home della campagna. In pagina portano l'etichetta "Foto indicativa".

| In pagina | Origine | Licenza | Lavoro fatto |
|---|---|---|---|
| Apertura, officina con l'auto sul ponte vista dal fondo | Renee Razumov, Pexels 33814736 (https://www.pexels.com/photo/modern-car-repair-shop-interior-with-vehicle-33814736/) | Pexels License | tolti SKODA, SUPERB, WURTH e MIRKA; tolto il parafango in primo piano ricostruendo il pavimento in prospettiva; schiarite le piastrelle grigio scuro a sinistra; tolte la scala e le pistole appoggiate al muro; ripulito il vano targa; gialli smorzati; velatura chiara sul pavimento; taglio largo (2040 px) e verticale |
| Chiusura, sotto la frase e i recapiti: auto bianca intera, di fianco, sul ponte | Artem Podrez, Pexels 8985667 (https://www.pexels.com/photo/car-on-lift-at-auto-the-repair-shop-8985667/) | Pexels License (gratuita anche per uso commerciale, senza obbligo di citazione; letta sulla pagina il 19/10/2026) | tolta l'insegna appesa con il marchio e la scritta, tolta la scritta del modello sulla portiera; bianco riportato al neutro (la foto era calda e verdina); saturazione ridotta; taglio 3:2 e 5:4 per il telefono, con il meccanico fuori dal quadro |

Trattamento comune: luce neutra appena fredda, saturazione ridotta, neri non chiusi. JPEG progressivi in più larghezze con `srcset` (`_prova/script/finale_img.py`). Dettagli in `assets/CREDITI.md`.

Resta un limite che nessun ritocco toglie: l'auto dell'apertura è senza paraurti posteriore e la porta a vetri a destra è quella di una cabina di verniciatura. Va bene come segnaposto della luce e dell'inquadratura, non come foto da pubblicare: la foto vera, con una loro auto intera sul ponte, è la prima cosa da fare (LEGGIMI, "Foto da rifare dal vero").

## Le ispirazioni del committente

- **Pelletteria Graziella: non usata.** Nero pieno, serif enorme con il corsivo d'accento: è il registro di una pelletteria che lavora per le maison, ed è sbagliato per un'officina di paese.
- **Studio N19: un solo tratto.** Il titolo grande e sicuro in grottesco su un fondo chiaro, con tanta aria. Niente sfocature né parole in movimento.
- **Perché così poco**: Bazzato non è moda né lusso, è un servizio di fiducia. Qui l'alta gamma è la luce, l'ordine e i prezzi detti chiari.

## Cosa è cambiato nella rifinitura (dopo il giudizio cieco)

- **Stato dell'officina nella prima schermata**: dalla riga di 16 px in testata a un elemento della composizione, 29 px con il punto azzurro, sopra il bottone "Chiama". Il pannello degli orari si apre da lì. In testata resta il telefono.
- **Frase d'apertura**: dice la promessa concreta, "Revisione in sede in circa 45 minuti, € 79", al posto dell'elenco con "revisione in sede".
- **Apertura**: taglio più stretto, l'auto è più grande; schiarite le piastrelle grigio scuro nel pavimento a sinistra. A 390 e a 320 il taglio verticale è più basso: il titolo sta sul pavimento sotto il ponte e l'auto resta intera.
- **Seconda foto**: al posto del SUV tagliato a metà, col fumo e il tubo dei gas di scarico in primo piano, la stessa auto dello stesso servizio fotografico vista intera di fianco sul ponte, con aria ai lati, senza fumo, con la luce riportata a quella dell'apertura.
- **Testi**:
  - tolte dai fatti "Revisione in sede" e "GPL Landi", che erano ripetute più sotto: restano Eurorepar e auto sostitutiva in una riga;
  - il listino si chiama "Lavori e prezzi" (come la voce del menu) invece di "Prezzi chiari, sconti chiari", perché in pagina non c'è nessuno sconto.
- **Colore di fondo**: il cemento passa da #E9E8E4 a #F0EEEA, più luminoso; la velatura del pavimento nella foto usa lo stesso colore.
- **Listino fra 701 e 1100 px**: il prezzo va a capo nella sua colonna ("prezzo anche / al telefono") invece di uscire nel margine; prima a 701 la pagina scorreva di lato di 3 px.
- **320**: bottone e spaziature più stretti, WhatsApp finisce a 296 px con il margine a 300.
- **Dove siamo a 390**: "Tombelle di Vigonovo" non si spezza più su due righe.

## Cosa non è cambiato, e perché

- **La foto a tutta larghezza con il titolo sopra**: è la prima schermata della bozza scelta dal committente e resta. Il giudice proponeva di togliere la foto a tutta pagina e mettere un oggetto scontornato accanto al titolo, cioè un'altra bozza.
- **La foto dell'apertura**: ho cercato su Pexels e Unsplash un'officina chiara vista in asse, con un'auto intera sul ponte e il pavimento libero davanti per il titolo. Ho trovato solo auto di fianco, con il ponte e i banchi proprio dove andrebbe il titolo, oppure foto scure o con marchi in primo piano. Una di quelle è diventata la seconda foto. Per l'apertura la soluzione vera è la foto fatta da loro (LEGGIMI).
- **Il titolo "Officina multimarca a Tombelle"**: è quello della bozza. Ciò che un concorrente non può firmare ora sta subito sotto, ed è più grande: lo stato vero dell'officina e la revisione in sede a € 79 in circa 45 minuti.

## Controlli

- **Larghezze**: 1440, 390, 320, 768, 1024 e 1920, guardate a pezzi. Nessuno scorrimento orizzontale, nessun testo fuori dalla finestra, nessuna sovrapposizione fra testata, titolo, testo e bottoni, né fra la frase, i recapiti, la didascalia della foto e il piede nella chiusura (`finale_scatti.mjs`, che salva anche la chiusura a 1440). La chiusura è stata guardata a pezzi a 1440, 1024, 768, 390 e 320.
- **Da 320 a 2560** (`verifica_larghezze.mjs`, ogni pixel fino a 900 e poi ogni 8): scrollWidth sempre uguale alla larghezza della finestra; i prezzi del listino e i bottoni non escono mai dalla colonna. A 701, 768, 800 e 840 i prezzi finiscono esattamente sul margine (670, 734, 764, 803).
- **Collegamenti**: `tel:+390499830115`, `https://wa.me/390499830115`, `mailto:info@bazzato.it`, Google Maps con "Viale Serenissima 3 Vigonovo VE", informativa privacy sul sito di oggi, ancore interne.
- **Altezza a 1440**: 4677 px.
- **Segnali da IA** (`kit/segnali.sh`, 1440, dopo la chiusura nuova): 0 soglie bloccanti su 10. Foto sul 36,3 % della pagina, General Sans al 100 %, nessun monospazio, nessuna etichetta maiuscola, un titolo col punto su 4 (la frase della chiusura, ammesso), 4 fasce di fondo, 16 filetti. Resta da guardare solo "misure degli H2: 2 (80 e 72 px)": la frase della chiusura è appena più piccola dei titoli di sezione.
- **Contrasto della chiusura**: frase e recapiti neri sul cemento; "Sabato chiuso" e il piede in grigio #56554F (6,4); "Foto indicativa" #3F3E3A sul pavimento chiaro della foto (almeno 6,9).
- **Divieti del committente**: nessun gradiente, nessuna emoji, niente Inter, nessuna card col bordo colorato, nessun vetro sfocato, nessuna icona, nessun badge, nessuna animazione allo scorrimento, nessun effetto sul cursore, nessun bottone che sbiadisce, nessun corsivo d'accento.
- **Caratteri vietati**: nessuna lineetta lunga U+2014 né media U+2013 nella pagina, negli script, in questa nota e nel LEGGIMI.
- **Note di lavorazione**: nessuna in pagina; la build controlla le parole "provvisori", "da rifare", "proposta", "segnaposto".
