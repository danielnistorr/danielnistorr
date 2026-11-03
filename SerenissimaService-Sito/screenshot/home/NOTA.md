# Serenissima Service, home: nota

## Alto livello, prova della sezione D (3/11/2026)

Pagina rifatta da capo secondo `_prova/alto/DIREZIONE.md` e la sezione D di `_metodo/professionale/ALTO-LIVELLO.md` (D vince su A e C). La home di prima, con le sue immagini, i caratteri e gli screenshot, è copiata com'era in `_prova/versione-pro/`.

**Come si rifà**
- Foto: `python3 -I _prova/alto/img.py .` (una serie sola, un solo trattamento: bianco neutro sui grigi, curva morbida con neri a 12 e alte luci a 248, saturazione 0,88, nitidezza dopo la riduzione; WebP 1x e 2x, mai oltre la misura naturale; mail personale sulla portiera del carro coperta, targhe della sede sfocate).
- Pagina: `sito/index.html`, scritta a mano, statica, si apre da file://. Caratteri in `sito/fonts/` (Barlow 400, 500, 600 e Barlow Condensed 600, 700, 800, sottoinsieme latin, con `OFL.txt`).
- Misure D: `node _prova/alto/misura-d.mjs` (esito in `_prova/alto/misura-d.json` e `misura-d-soglie.json`). Contrasto del testo sulla foto: `node _prova/alto/contrasto.mjs`. Menu, modulo, stato e mailto: `node _prova/alto/funzioni.mjs`. Targhetta fissa contro il piede: `node _prova/alto/fondo.mjs`. Screenshot: `node _prova/alto/screenshot.mjs`.
- `bash _prova/script/build_finale.sh` rifà la versione di prima e sovrascrive questa: non va più lanciato.

### Ritocco dopo il giudizio da agenzia (3/11/2026, voto 7)

Il giudice ha dato 7 (prima 5,5): la prima schermata regge, sotto la piega la pagina tornava un modello ben eseguito. I clienti tipo trovavano l'auto sostitutiva solo dopo 4 scorrimenti, i noleggi con 3 tocchi e uno scorrimento, le Indicazioni con 3 tocchi e uno scorrimento senza indirizzo in vista all'arrivo. La pagina di prima del ritocco è in `_prova/alto/ritocco/index-prima-del-ritocco.html`. La sezione D non torna indietro: prima schermata identica (7 cliccabili, 1 bottone, 148 caratteri, foto al 91,7%).

**Che cosa ho cambiato**
- **Il culmine ha una foto che domina.** Il carro attrezzi prende 8 colonne su 12 (864 x 576, file 1641 px). Accanto, sulle 4 colonne restanti, sta in alto la sua riga ("Il carro attrezzi") e in basso, sul fondo della foto, la frase dell'auto sostitutiva in Barlow Condensed 600 a 28/34, come unico titolo della tessera (niente più h3 a 26 sopra una frase a 32). Sotto, una fila da tre alla pari: la pratica in sola tipografia con il modulo CID, il carrozziere e le cabine gialle a 416 x 277, tutte 3:2. L'area del carro è 4,3 volte quella delle altre; il culmine è alto 1455 px.
- **Il banco accettazione esce dalla home** (vuoto, senza persone): la pratica è una tessera di testo finché non c'è lo scatto di chi risponde (LEGGIMI 20).
- **Il taglio del carro** in `img.py` parte da y 170, sotto le lettere dell'insegna: nessuna lettera troncata sul bordo alto, 26 px d'aria sopra il lampeggiante, il carro intero. L'insegna intera non si può avere perché l'originale è già tagliato su "SERENISSIMA". Resta tagliato in alto il disco del marchio FIAT.
- **Una sola numerazione.** Il culmine è senza numeri; i reparti sono un indice 01-05 su tutta la larghezza (numero, nome, riga, "Vai alla pagina" a destra), righe tutte alte 72 px con filetti a 1 px. Le tre foto dei reparti stanno in una fila da sole, con lo stesso taglio e una didascalia di una parola (Officina, Cristalli, Levabolli). Il 06 "Soccorso stradale" è tolto: il soccorso compare 3 volte nel testo (riga del mestiere, testata o barra del telefono, chiusura).
- **La targhetta blu fissa non c'è più.** Da 1024 px in su il soccorso sta in testata, a destra di "Chiama", come testo blu del carro in Barlow Condensed 700 ("Soccorso 335 5639355", sotto i 1240 px su due righe), senza riquadro e con `data-ruolo="emergenza"`. Sotto i 1024 px restano la barra fissa in basso (Chiama 60%, Soccorso 40%) e il menu a pannello: il punto di rottura è passato da 900 a 1024 perché la testata con il soccorso entra solo da lì (controllo `_prova/alto/ritocco/testata.mjs`, da 900 a 1920 nessun a capo né sovrapposizione). Coperti dalla parte fissa a 1440: 0 (`ritocco/scorri.mjs`). Il piede torna a 48 px in fondo.
- **Menu del telefono**: in testa lo stato, gli orari e "Per i sinistri scegli l'interno Carrozzeria"; le voci sono Incidente, Compagnie, Denuncia del noleggio (porta dritto all'elenco dei noleggi, `#noleggi`), Servizi, Tagliando, Chi siamo, Dove siamo (porta all'indirizzo, `#indirizzo`). I link dei noleggi e "Indicazioni" sotto i 1024 px sono alti 48 px.
- **Chiusura**: le tre strade hanno la stessa struttura (etichetta, numero o email a 28 px, una riga con l'orario; per il soccorso solo "Con il nostro carro attrezzi", perché l'orario non è confermato). A destra la sede, poi l'indirizzo scritto, lo stato e l'unico "Indicazioni"; sul telefono l'indirizzo, lo stato e "Indicazioni" vengono subito dopo il titolo.
- **Minori**: velo dell'apertura a 0,72 sul 20% più basso e didascalia in Barlow 500 a 16 px (fondo sotto la didascalia, 98° percentile: 14,1:1 a 1440 e 12,9:1 a 390; lo script `giudice/contr.mjs` lasciava visibile la didascalia, che ha un suo colore, e misurava le lettere: corretto in `ritocco/contr-giusto.mjs`); "Tutto nella stessa sede" con il titolo a sinistra e la frase e la storia nella stessa colonna a destra, allo stesso margine; la riga sotto il titolo del culmine su una riga sola; il filetto della frase "Poi pensiamo noi..." a tutta larghezza; cielo della sede desaturato (solo l'azzurro, al 45%).

**Che cosa non ho fatto, e perché**
- **Nomi delle persone e orari del soccorso** (D12, "Le persone hanno un nome"): nessuna fonte li dà, non si inventano. Chiesti nel LEGGIMI (punto 19). D12 resta l'unica misura D che non passa sul contatto per persona.
- **"Christian, levabolli"**: solo dopo la conferma e il permesso (LEGGIMI 19).
- **object-position della cabina al 46%**: non serve più, l'angolo in basso a destra non ha più la targhetta.
- **Servizio fotografico** (cabina a 4000 px, squadra in divisa): resta il tetto indicato dal giudice, fuori da questo ritocco.

**Misure dopo il ritocco** (`node _prova/alto/misura-d.mjs`, tutte le soglie passano): 5917 px a 1440 (9034 a 390, prima 10031), 606 parole, 5 sezioni, 8 foto in 2 formati, 2 bottoni a 1440 e 3 a 390, culmine 1455 px, 565 KB a 1440 e 447 KB a 390, nessuno scorrimento orizzontale, sovrapposizione o errore a 320, 390, 768, 1024, 1440 e 1920. Clienti tipo rifatti con gli stessi script (`_prova/alto/ritocco/prova-1` e `prova-2`): anticipo e auto sostitutiva dopo 1 scorrimento (prima 4), modulo CID dopo 2, compagnie con un tocco dal menu; noleggi con Menu, "Denuncia del noleggio" e il link di Alphabet, 3 tocchi e 0 scorrimenti, link alto 48 px; Indicazioni con 3 tocchi e 0 scorrimenti, con indirizzo e stato in vista all'arrivo.

### Che cosa è cambiato

- **Apertura, modello Q.** La cabina vuota in asse (`2015-04-fornoDentro1.jpg`, 1920 x 1276) a tutta larghezza, con sopra il motto del logo come titolo: **BOTTA? RISPOSTA!** in Barlow Condensed 800 maiuscolo, 146 px a 1440 (la direzione diceva 152: a 152 il punto esclamativo toccava il carrello verde della foto). Sotto, la riga del mestiere e la didascalia a due voci "Una nostra cabina / Corso Stati Uniti 19, Padova", senza anno (cartella 2015-04, EXIF 19/03/2016). Il velo nero è solo sul 45% basso (58% sotto i 640 px). A 390 la stessa foto esce tagliata in verticale (720 x 1276, centrata al 48%).
- **Numero fisso.** A 1440 la targhetta blu del carro, "Soccorso stradale 335 5639355", in basso a destra a ogni scorrimento (`data-ruolo="emergenza"`, link `tel:`); sotto i 900 px una barra fissa: Chiama 049 760655 (60%) e Soccorso (40%). Il piede ha 112 px in fondo perché a fine pagina la targhetta non copra nulla (controllato con `fondo.mjs`).
- **Testata**: logo, 4 voci (Incidente, Compagnie e noleggi, Tagliando, Dove siamo) e "Chiama 049 760655". Sul telefono "Menu" apre il pannello con lo stato "Sede aperta ora" e 6 voci; senza JavaScript "Menu" porta al piede.
- **Culmine** "Hai avuto un incidente? Pensiamo a tutto noi" (1805 px): il percorso dell'auto in cinque tempi, quattro foto 3:2 a 624 px (il carro, il banco accettazione, il carrozziere, le cabine gialle con il loro nome) e la tessera di testo dell'auto sostitutiva. Le foto sono passate da 4:3 a 3:2, come l'apertura, per stare sotto i 6000 px senza accorciare il culmine.
- **Compagnie e noleggi** su grigio: le 27 compagnie per nome in due colonne, i sei noleggi in righe d'indice con link di testo (niente più 8 bottoni bordati su blu), la frase su che cosa facciamo dopo la denuncia.
- **Tutto nella stessa sede**: la storia in una frase con tre numeri (1993, 2001, 3000 mq), tre reparti con foto e tre righe di solo testo, numerati 01-06.
- **Prenota il tagliando**: modulo corto (nome, telefono, targa, auto e km, data, note), orari in tabella. Il modulo resta in home perché per S la richiesta è il mestiere (D12).
- **Chiusura verde**, l'unico blocco del colore del marchio: tre strade per bisogno con numero a 28 px e orario, la foto della sede 2:1, lo stato, un solo "Indicazioni".
- **Tolti**: la fascia verde dei quattro percorsi, la fascia delle 5 cifre grandi, la fascia delle prove (ISO 9001 e Polizia di Stato escono finché non sono confermate), la linea del tempo con la Ferrari, le sei schede blu dei noleggi, il telefono a 96 px, l'occhiello, il campo email, "Che cosa ti serve", "Quando" e il ritiro a domicilio dal modulo, Archivo. I bottoni passano da 13-14 a 3, le parole da 1245 a 602, l'altezza da 9959 a 5990 px.

### Le misure D, prima e dopo

Prima: `alto/diagnosi/misure/nostre-*.json` (la home di oggi, misurata dalla diagnosi). Dopo: `_prova/alto/misura-d.json`, finestre 1440 x 900 e 390 x 844, ora di prova martedì alle 10.

| Regola | Soglia | Prima | Dopo | Esito |
|---|---|---|---|---|
| D2 foto nella prima schermata, 1440 | 60% o più (o sotto il 12%) | 32-33%, foto di 720 px nel riquadro a destra | 90,3% (cabina 1440 x 828 su 900) | passa |
| D2 foto nella prima schermata, 390 | 50% o più | 25% | 85% | passa |
| D2 nessuna foto ingrandita | file vero di almeno la larghezza mostrata, scala con `cover` non oltre 1 | 720 px mostrata a 708 | a 320, 390, 768, 1024, 1440 e 1920 tutte le 9 foto a scala 1 o meno (cabina 1440/1440 e 1920/1920) | passa |
| D3 cliccabili, 1440 | 8 per S | 14 | 7: logo, 4 voci, Chiama, targhetta del soccorso | passa |
| D3 bottoni, 1440 | 1 | 3 | 1 (Chiama); la targhetta è il numero d'emergenza separato | passa |
| D3 caratteri fuori dal menu, 1440 | 160 | 716 | 156 (203 con il menu) | passa |
| D3 fila di ingressi | 0 | 4 percorsi in fascia | 0 | passa |
| D3 cifre di 30 px o più | 0 | 0 nella prima schermata, 5 sotto | 0 | passa |
| D3 a 390 | 4 cliccabili, 1 bottone, foto 50% | 9 cliccabili, 4 bottoni, 25% | 4 (logo, Menu, Chiama, Soccorso), 1 bottone, 85% | passa |
| D5 famiglie calcolate | 2 | 1 (Archivo, in 9 home) | 2 (Barlow, Barlow Condensed); Barlow solo in Framo, altra zona: 2 su 45 | passa |
| D5 elementi sopra 100 px | 1 | 0 (h1 a 38 px) | 1, l'h1 a 146 | passa |
| D5 testo corrente | 17 px a 1440 | 17-19 | 17 minimo, 19 il corpo; a 390 16 per i soli nomi delle compagnie | passa |
| D6 occhielli sopra h1/h2 | 1, con un fatto | 1 ("Botta? Risposta!" sopra l'h1) più 3 maiuscoli spaziati | 0 | passa |
| D7 h1 | 9 parole, 1 virgola | 13 parole, 2 virgole | "Botta? Risposta!", 2 parole, 0 virgole, dal logo del 2016 | passa |
| D7 lista nera, lineetta lunga | 0 | 0 | 0, 0 | passa |
| D7 frase-firma in 2-3 punti | 2-3 | 1 | 2 ("Pensiamo a tutto noi" negli h2 del culmine e della chiusura) | passa |
| D8 parole | 450-750 (S) | 1245 | 602 (596 a 390) | passa |
| D8 sezioni | 6 | 9 | 5 | passa |
| D8 bottoni nella pagina | 5 | 13 (14 a 390) | 3: Chiama, targhetta, Prepara l'email | passa |
| D8 altezza a 1440 | 4000-6000 | 9959 | 5990 | passa, al limite |
| D8 culmine | almeno 900 px | nessuno | 1805 px | passa |
| D9 numeri di 30 px o più | 1 | 5 in fascia più il telefono a 96 | 0 | passa |
| D10 foto in home | 12 | 10 | 9 | passa |
| D10 formati | 3 | 3-4 | 2 (3:2 e 2:1) | passa |
| D10 "indicativ", repertorio | 0 | 0 | 0 | passa |
| D11 fondi oltre al piede | 3 | 4 | 3 (bianco, grigio #F1F2F0, verde) | passa |
| D11 sezioni col colore del marchio | 1 | 2 (percorsi e chiusura) | 1 (chiusura) | passa |
| D11 spazi tra le sezioni | 2 valori, rapporto 1,5 | 0/120, uno solo | 80 e 128 (1,6) | passa |
| D12 "Indicazioni" | 1 | 2 | 1 | passa |
| D12 telefono di 40 px o più e modulo | ammessi solo per S | telefono a 96 e modulo | modulo sì, telefoni a 28 | passa |
| D12 peso della pagina | sotto 3 MB | | 607 KB a 1440, 489 KB a 390 (665 KB a 1920) | passa |
| D12 testo senza JavaScript | tutto | | 602 parole su 602; lo stato mostra gli orari | passa |

**Controlli di finitura** (`misura-d.mjs`, `contrasto.mjs`, `funzioni.mjs`): a 320, 390, 768, 1024, 1440 e 1920 nessuno scorrimento orizzontale, nessuna sovrapposizione tra testi, nessun errore di script (i `preload` dei caratteri davano errore CORS da file:// e sono stati tolti). 7 link `tel:` (sede, soccorso, Sifà 800 037631), 2 `mailto:` con oggetto, quello della chiusura anche con la traccia (nome, telefono, targa, di che cosa hai bisogno); il modulo compone "Prenotazione tagliando, targa AB123CD" con tutti i campi e senza JavaScript manda il modulo per posta con `action="mailto:"`. Contrasto del bianco sulla foto, misurato sui pixel sotto ogni riga: h1 da 5,4 a 9,7:1 in media (il 10% più chiaro dei pixel almeno 3,5:1), riga del mestiere e didascalia almeno 4,5:1 anche sul 10% più chiaro. Focus visibile (contorno di 3 px verde, bianco sul verde e sulla foto), alt descrittivi su tutte le foto, nessun testo dentro le immagini.

**Confronto a vista** (`_prova/alto/lavoro/confronto.jpg` con Geser, BELFOR e Pirtek; `lavoro/lontano.jpg` con la pagina intera di Geser a 300 px): la prima schermata regge accanto a Geser (stessa stanza, ma qui il testo è un titolo solo sul pavimento e non un riquadro velato) e a BELFOR (la targhetta fissa fa il lavoro della loro hotline, senza il secondo bottone). Corretto dopo il confronto: il titolo ridotto da 152 a 146 px e a 10,1vw sotto i 1240 px perché a 1024 copriva il carrello; le foto del culmine e dei reparti in 3:2; la tessera 5 su due righe; "Soccorso" senza "stradale" sotto i 360 px; il piede alzato sopra la targhetta.

### Problemi aperti

- **Altezza al limite**: 5990 px su 6000. Qualsiasi riga in più (per esempio la riga ISO nel piede, dopo la conferma) va compensata, prima accorciando le righe 04-06 dei reparti.
- **La foto d'apertura è di 1920 px** (servizio Nikon, cartella 2015-04): rispetta D2 a 1x, ma sugli schermi 2x è morbida. Resta la richiesta del servizio fotografico (cabina vuota in asse a 4000 px e più), vedi LEGGIMI.
- **Il passo 3 mostra la Ferrari 488 di un cliente** (serie 2018-09): il taglio tiene solo il passaruota, le mani e il carrozziere, niente marchio; il permesso resta da chiedere (LEGGIMI 13).
- **`_prova/script/pro_controlli.mjs`** (compiti dei clienti tipo) cerca gli elementi della pagina di prima e va adattato alla soglia nuova ("entro due schermate o un tocco dal menu") prima di ripetere le prove con i clienti tipo e il giudizio da agenzia.
- **A 390 la pagina è lunga 10031 px** (contro 14606 di prima): D8 conta solo 1440, ma le tre foto dei reparti a tutta larghezza pesano; si possono mettere in due colonne se il telefono va accorciato.
- **Dati da confermare in pagina**, solo con le parole del loro sito: 335 5639355 come soccorso (1), interno Carrozzeria (2), le 27 compagnie (4), link e scadenze dei noleggi, Sifà che rimanda a Unipol Rental (5), 1993, 2001 e 3000 mq nella frase della storia (6), "fino a 35 quintali" e "smart repair da 1 a 4 ore" (12).

---

## Storia: la nota della versione professionale (copiata in `_prova/versione-pro/`)


Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, pagina da `_prova/script/index.html`, screenshot). La versione precedente (apertura "Botta? Risposta!" con la Ferrari 488) è copiata com'era in `_prova/versione-1-originale/` (pagina, immagini e la sua nota).

Altezza: 9959 px a 1440, 14606 px a 390.

### Livello professionale, ritocco finale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessun repertorio, nessun disegno). Regole: `_metodo/professionale/REGOLE.md`, famiglia S (servizi tecnici e imprese). Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14, le pagine intere di Kline e Dulwich Diggers a pezzi (prima anche Kline e Wilson). Scheda d'uso: `_prova/uso/SCHEDA.md`. Il ritocco parte dal giudizio del controllore (voto 6, dieci difetti) e dalle prove dei due clienti tipo (voti 7,5 e 8).

### Che cosa è cambiato in questo ritocco

- **Apertura con un tratto proprio.** La foto della sede con il carro attrezzi arriva fino al bordo destro e copre tutta l'altezza dell'apertura (niente più riquadro arrotondato a destra del titolo). Sotto, i quattro percorsi stanno su una **fascia piena verde del logo**, in bianco: il colore del marchio è nella prima schermata a 1440 e a 390. La fascia delle garanzie, subito sotto, è passata su grigio chiaro per non avere due verdi di fila.
- **Foto d'apertura ritagliata di nuovo** (`pro_img.py`): solo la parte sinistra dell'originale, così il cartello di terzi "egroup / Consorzio Zambelli Revisioni" (servizio non confermato) resta fuori campo; via anche la fascia alta di cielo. Restano l'insegna "SERENISSIMA, officina e carrozzeria" e il carro blu "Soccorso stradale Serenissima Service" con "Il Socio" sulla cabina.
- **Il motto come testo**: "Botta? Risposta!" in verde, della misura di una riga, sopra il titolo (nel logo a 390 non si leggeva). Logo più grande: 76 px di altezza a 1440 (testata di 100 px), 56 px a 390 (testata di 76 px); a 390 il bottone della testata mostra solo il numero, come la pillola di Wilson.
- **Gesto di scala**: il telefono della chiusura è a 96 px a 1440 (80 a 1240, 72 a 900, 56 a 390), su una riga sua sopra le due colonne.
- **Prove in alto**: sotto i numeri, una fascia bianca con didascalia: "Certificazione ISO 9001, sistema di gestione per la qualità"; "Albo fornitori della Polizia di Stato, nel triennio 2023-2025"; "Carrozzeria fiduciaria di 27 compagnie, e punto di riparazione per sei società di noleggio". In "Chi siamo" le stesse prove sono state sostituite dalle loro date (anni Sessanta, 1993, 2001, 2018, 2023-2025), così non si ripetono.
- **Sinistro e compagnie**: "Non anticipi nulla" come titolo della prima garanzia, con la loro frase "Il cliente non dovrà anticipare nulla" nel testo (la lead dell'apertura non la ripete più). Sotto il CID il collegamento "La tua compagnia è convenzionata? Vedi le 27 compagnie"; titolo "Le 27 compagnie fiduciarie"; voce "Compagnie" nel menu ("Chi siamo" resta nel menu del telefono). Grandine, smart repair e parabrezza sono dopo l'elenco delle compagnie, con il titolo "Grandine, piccoli danni e cristalli".
- **Noleggi**: Alphabet e Leasys hanno due bottoni uguali (senza controparte, con controparte) al posto della scheda tutta cliccabile, e Leasys anche il PDF DEN001; l'etichetta "Entro 3 giorni" accanto al nome di Alphabet e Leasys, "Subito, 8-19" per Sifà, con il bottone "Chiama Sifà 800 037631". I quattro passi di Serenissima dopo la denuncia stanno prima delle schede (a 1440 e a 768 in colonne; sul telefono riassunti in una riga del testo d'apertura, così Alphabet resta in vista dopo il salto).
- **Stato**: "Sede aperta ora" / "Sede chiusa ora", così non sembra valere per il soccorso stradale.
- **Prima schermata del telefono**: "Indicazioni: Corso Stati Uniti 19" (si sa dove porta prima di toccare).
- **Chiusura**: un solo bottone "Indicazioni stradali (Google Maps)"; l'indirizzo è testo. Etichette di sezione in minuscolo, in grassetto (niente maiuscolo spaziato nei titoli).
- **Modulo**: se si chiede il ritiro a domicilio, l'indirizzo è obbligatorio (avviso e fuoco sul campo).
- **Minori**: a 390 "3000 mq" a tutta larghezza e le altre quattro cifre in 2x2; la scheda del soccorso dice "Soccorso stradale a disposizione, con il nostro carro attrezzi" (la loro frase, senza la parafrasi di prima); Alphabet punta all'indirizzo nuovo della pagina (`...-e-furti.html`, il vecchio rimanda lì).

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito completo in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi a 1440 e 390 e le pagine intere a 320, 768 e 1024.

1. **Telefono come bottone nella testata fissa: passa.** Testata `sticky` di 100 px a 1440 e 76 a 390; bottone pieno alto 48 px ("Chiama 049 760655" a 1440, "049 760655" a 390), visibile e toccabile a metà pagina (`elementFromPoint`). 12 link `tel:`.
2. **Mestiere, luogo, prova e azione: passa.** H1 "Pensiamo a tutto noi / Carrozzeria, officina e soccorso stradale a Padova, dal 1993"; stato "Sede aperta ora, fino alle 12"; "Chiama 049 760655" a 553 px a 1440 e a 279 px a 390, a tutta larghezza (350 px). I quattro percorsi sono interi nella prima schermata a 1440 (fascia verde fino a 894 px) e a 390 (fino a 839 px).
3. **Immagine vera nell'apertura: passa.** Sede con insegna e carro attrezzi con la livrea, 708 x 600 a 1440 (a tutta altezza, fino al bordo), 390 x 195 a 390; il cartello delle revisioni è fuori campo.
4. **Zero repertorio: passa.** `indicativ` 0 volte; 0 svg, nessun `background-image`; in `sito/img/` solo foto e logo dell'azienda; i segnaposto Pexels di `assets/esterne/` non sono usati.
5. **Foto in serie: passa, con riserva.** Stesso trattamento per tutte (`pro_img.py`); tre formati a vista: apertura circa 8:7 a 1440 (1,15), 4:3 delle sei schede, 2:1 (apertura a 390 e facciata); una didascalia su otto foto; nessuna foto ingrandita. Riserva: scatti del 2015, 2018 e 2019, non un solo servizio (LEGGIMI).
6. **Palette dal marchio: passa.** `--verde` #076633 (logo e insegna), `--verde-scuro` (passaggio del mouse), `--blu` #16306E (il carro), neutri freddi. Fondo bianco, nessun beige.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 19, 23, 32, 48, 64, 96) e 8 a 390 (14, 17, 19, 20, 26, 32, 40, 56); testo corrente 19/17 px; nulla sotto i 14 px; H1 64/32, H2 48/26; il telefono a 96 px è il gesto fuori scala.
8. **Due famiglie al massimo: passa.** Una sola, Archivo, pesi 400 e 700.
9. **Servizi in schede con la foto: passa.** Sei schede in tre colonne, tutte 4:3, nome, riga e link; tutta la scheda è il link; a 390 righe con la miniatura.
10. **Almeno tre tipi di prova: passa (3 su 4).** Cinque numeri della sede; fascia di certificazioni con didascalia (ISO 9001, albo fornitori della Polizia di Stato 2023-2025, fiduciaria di 27 compagnie), senza loghi; compagnie e noleggi per nome. Mancano le recensioni: nessuna fonte verificata (LEGGIMI).
11. **Lavori con un nome: non passa.** Nelle fonti c'è un solo lavoro con anno (la Ferrari 488 del 2018, ora nelle date di "Chi siamo"), senza dati e senza foto. Servono tre lavori con luogo, anno e dati (LEGGIMI).
12. **Ritmo a blocchi: passa.** Blocchi pieni oltre al piede: fascia verde dei percorsi nell'apertura, noleggi su blu, chiusura su verde; garanzie, compagnie e tagliando su grigio chiaro, alternati al bianco. Sezioni a 120 px a 1440 e 72 a 390; margini 80 a 1440 e 20 a 390. Nessuno scorrimento orizzontale da 320 a 1920.
13. **Un solo sistema di bottoni: passa.** Pieno e bordato, raggio 4 px, 56 px (48 in testata e dentro le schede dei noleggi), testo 17 px; i bottoni di chiamata contengono il numero (anche "Chiama Sifà 800 037631").
14. **Modulo e "dove" per il mestiere: passa in parte.** Tipo di cliente, che cosa serve (9 voci), urgenza, ritiro con l'indirizzo (ora obbligatorio se richiesto), note con l'istruzione per allegare le foto; compone l'email a info@ con oggetto. Nessun iframe. Non c'è un campo foto (un `mailto` non porta allegati: va con il servizio vero, LEGGIMI) e manca l'elenco dei comuni serviti, che nessuna fonte dà.
15. **Piede completo: passa.** Quattro colonne a 1440, ragione sociale, P.IVA e C.F., indirizzo, telefoni ed email cliccabili, mappa, orari, servizi, ISO 9001, Privacy e Cookie, Facebook con il sottotitolo; testo di almeno 14 px. Zone servite: solo la sede (vedi 14).

### Compiti della scheda d'uso (par. 8)

- *Botta, telefono*: chiamata e soccorso con un tocco nella prima schermata, interno Carrozzeria scritto sotto il bottone, "Sede aperta/chiusa ora" sull'ora di Roma (prove: lunedì 9, mercoledì 13, venerdì 18.30, sabato 11 e 15, 8 dicembre, Pasquetta, tutte giuste). "Non anticipi nulla" e auto sostitutiva uno scorrimento sotto. Compagnie: 27 nomi, ricercabili, raggiungibili dal menu ("Compagnie") o dal collegamento sotto il CID. CID con un tocco da "Ho avuto un incidente". Grandine e cristalli con i tempi, subito dopo le compagnie.
- *Noleggio, telefono*: "Auto a noleggio: denuncia il danno" nella prima schermata; dopo il tocco Ayvens e Alphabet sono in vista (Alphabet a 627 px con l'etichetta "Entro 3 giorni"); il secondo tocco apre il modulo giusto. Per Leasys due bottoni uguali, con e senza controparte, più il PDF DEN001. Indicazioni con un tocco dalla prima schermata.
- *Tagliando, computer*: "Prenota il tagliando" nella prima schermata; un clic porta al modulo; orari in tabella accanto al modulo e nella chiusura.
- *Identità*: logo più grande e motto scritto sopra il titolo; la loro sede e il loro carro nell'apertura; frasi loro, a tu, senza maiuscolo urlato.

### Caratteri e licenze

- **Archivo** (Omnibus-Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; testo della licenza in `sito/fonts/OFL.txt`. Servito dalla pagina (`sito/fonts/archivo-latin.woff2`, `archivo-latin-ext.woff2`), nessuna chiamata a Google.
- Foto: solo materiale del loro sito (`assets/CREDITI.md`), da usare con il loro permesso. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Controlli fatti (3/11/2026)

- `pro_controlli.mjs`: regole 1-10 e 12-15 superate nelle misure (14 e 15 senza elenco dei comuni), 11 no. Il controllo della regola 10 ora verifica la fascia delle prove; quello della 13 accetta anche il numero di Sifà. Nessuna ancora senza destinazione, nessun errore di script.
- Prove con il browser (390, tocchi veri): salto a "Noleggio" con Alphabet in vista; modulo con il ritiro chiesto e l'indirizzo vuoto fermato con l'avviso e il fuoco su "Indirizzo per il ritiro"; invio vuoto fermato sul nome; email composta e letta senza inviarla; menu del telefono con 7 voci che si chiude dopo il clic.
- Larghezze 320, 360, 390, 768, 1024, 1280, 1440, 1920: nessuno scorrimento orizzontale, nessuna sovrapposizione nell'apertura. Pagine intere a 320, 768 e 1024 guardate a pezzi.
- Collegamenti dei noleggi provati il 3/11/2026: Ayvens (nemo.aldautomotive.it) e Athlon rispondono; Alphabet rimanda all'indirizzo con `.html`, già messo; Sifà rimanda a unipolrental.it; Leasys (leasysdenunciasinistri.com) e Volkswagen Lease non hanno risposto dalla prova (LEGGIMI, punto 5).
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, in CREDITI e negli script.
