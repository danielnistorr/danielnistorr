# Home di Molon Giovanni

## Metodo ibrido (novembre 2026)

Rifatta il 3/11/2026 con il metodo ibrido scelto dal committente: prima schermata secondo la sezione D di `_metodo/professionale/ALTO-LIVELLO.md` (cap. 4), sotto i contenuti e le funzioni della versione professionale, rimessi su una griglia sola. Direzione scritta prima dell'HTML in `_prova/alto/DIREZIONE.md`; riga nel registro dei caratteri (`_metodo/professionale/alto/REGISTRO-CARATTERI.md`). La versione professionale di partenza è copiata com'era (sito e screenshot) in `_prova/versione-pro/`.

### Che cosa è cambiato
- **Idea e modello (D1, D4)**: modello F, come nel capitolo 5. La foto vera del frontale rosso nel fieno in collina (`2017_10_11.08_10ritoc.jpg`, 3264 x 2448) a tutta pagina; il titolo scuro scritto nel cielo, a destra dei due alberi sul crinale; un solo bottone rosso, "Va sul vostro mezzo?". Sul telefono la foto in 4:5 sul ranghinatore e il titolo sotto. Riferimenti guardati accanto: Rapid (`riferimenti/rapid-1440-prima-schermata.jpg`) e Reform.
- **Testi (D7)**: `h1` "Anche sul terreno più irregolare.", accorciato dalla loro pagina dei ranghinatori ("perfetto adattamento a qualsiasi tipo di terreno, anche a quello più irregolare"); torna nel piede con lo stesso trattamento. Sotto: "Ranghinatori a cinghie per portattrezzi, trattori e motofalciatrici, da Arlesega di Mestrino (PD)." Manifesto della culmine: "Rivoltare l'erba. Mettere in andana. Allargare l'andana." (loro).
- **Registro (D5)**: Anek Latin (Ek Type, SIL OFL 1.1), una famiglia variabile: larghezza 75 e peso 700 per titoli e nomi, 300 per la riga e il manifesto, larghezza 100 e peso 400 per il testo (18 px a 1440, 17 a 390), tabelle in larghezza 87 con cifre tabellari. Al posto di Encode Sans Condensed del capitolo 5, che è già in 3 home; Fira Sans era appena stata presa da Fratelli Zuin, Roboto Condensed è il carattere di Rapid e Reform. Sofia Sans esce.
- **Testata fissa**: tre voci (Ranghinatori, Ricambi, Rivenditori), DE, telefono 049 900 0103 sempre in vista (a 320 px "Chiama"). Il logo non è un link, per stare nel tetto dei cliccabili. Sul telefono il menu nomina quello che si cerca: Frontali per portattrezzi e trattori, Posteriori a 3 punti, Per motofalciatrici, Ricambi, Rivenditori, Chi siamo, Indirizzo e contatti, English, Français.
- **Sotto la piega, sei sezioni su una griglia a 12 colonne** (margini 80 px a 1440, 40 fino a 1099, 16 sul telefono; bordo destro di ogni blocco a 1360 px a 1440):
  1. *Le macchine*: sei schede con la foto, il nome e la misura in una riga (frontali, posteriori, motofalciatrici, gEnio, girelli, scopatrici), poi le tre famiglie con i fatti (presa di forza 540 o 1000 giri/minuto, PRO, gEnio, optional, attacco a 3 punti, cinghie e ruote, MINI, MIKY, MAJOR) e le tre tabelle (frontali aperta; posteriori e motofalciatrici a un tocco, aperte senza JavaScript), con i link a video e schede tedesca e inglese. Accanto alle tabelle "Va sul vostro mezzo?" con Chiama e Scrivete (traccia: marca e modello, presa di forza, ranghinatore, zona, nome e telefono): colonna ferma a sinistra da 720 px in su, barra ferma in basso sul telefono finché si guardano le tabelle.
  2. *Culmine*: il MAJOR 180.3 dietro una motofalciatrice su un prato di montagna (`2025_03_dok-tc-07-molon-br-scaled.jpg`) a tutta larghezza in 16:9, la didascalia a due voci, il manifesto e il testo dei pettini su cinghie con il video di presentazione.
  3. *Ricambi*, l'unico blocco rosso: le tre cose da dire, "Chiama per il ricambio", "Manda la foto per email" (traccia come prima), "Se non rispondiamo, mandate la foto con il vostro telefono."
  4. *Dove si comprano*: i quattro rivenditori per zona con città e sito; la strada per rivenditori e officine (listino, ordini e configurazioni, email con la traccia).
  5. *Chi siamo*: Enio e Bruno Molon, i 3.000 m² in una frase, le cinque date, l'archivio in bianco e nero e la squadra, con le didascalie.
  6. Il *piede* come biglietto da visita: firma, telefono, fax, email, indirizzo, "Indicazioni stradali", macchine, lingue, ragione sociale, P.IVA, Privacy, Cookie.
- **Tolto**: la fila degli ingressi in apertura, il secondo bottone, gli occhielli sopra i titoli, la fascia delle cifre (25 modelli, 5 famiglie, 3.000 m², 5,0 su Google), il telefono a 96 px, il modulo "Richiesta" (al suo posto le tre email con la traccia, una per bisogno), "Va sul vostro mezzo?" ripetuto tre volte, il testo d'interfaccia "si apre un'email già scritta", la foto del lago, i fondi alternati antracite, rosso e grigio, "Vai alla mappa" doppio. Da 11.530 a 6.996 px a 1440.
- **Foto (D2, D10)**: `assets/originali/` mancava dopo il riavvio; l'ho ricostruita riscaricando dalla libreria media di molonmachinery.com le 111 immagini di almeno 1000 px (elenco `_prova/alto/media/elenco.txt`, provini `_prova/alto/provini.jpg`). Un trattamento per apertura, culmine e squadra (bianco a metà verso il neutro, spalla sulle alte luci, saturazione 0,88, contrasto 1,04), l'archivio in bianco e nero neutro con la stessa curva; nessuna scurita in blocco: dietro al titolo c'è solo una sfumatura chiara locale. Script `_prova/alto/script/img_alto.py`; le sei schede sono gli scontornati della versione professionale. 10 foto in pagina, 3 formati a ogni larghezza.

### Le misure
`node _prova/alto/misura-d.mjs` (copia estesa di `alto/diagnosi/misure/misura.mjs`), risultati in `_prova/alto/misure/misure.json`.

| Soglia | 1440 x 900 | 390 x 844 | Esito |
|---|---|---|---|
| Foto nella prima schermata (D2) | 92,8 % | 57,8 % | passa (60 % o più; a 390 almeno 50 %) |
| Cliccabili (D3) | 6: Ranghinatori, Ricambi, Rivenditori, DE, telefono, bottone | 4: DE, telefono, Menu, bottone | passa (6 e 4) |
| Bottoni pieni o bordati | 1 | 1 | passa |
| Caratteri fuori da testata e menu | 150 | 150 | passa (160) |
| Fila di ingressi, cifre di 30 px o più, occhielli | 0, 0, 0 | 0, 0, 0 | passa |
| `h1` | 5 parole, 0 virgole, 68 px | 42 px | passa (9 parole, 1 virgola) |
| Famiglie di caratteri, elementi sopra 100 px, testo corrente | 1, 0, 18 px | 1, 0, 17 px | passa |
| Parole | 725 | 706 | passa (900) |
| Sezioni tra apertura e piede | 5 (6 con l'apertura) | uguale | passa (7) |
| Altezza | 6.996 px | 9.235 px | passa a 1440 (7.500) |
| Griglia | 12 colonne, passo 24, margini 80-1360, un solo bordo destro (1360) | 12 colonne, passo 16, 16-374 | passa |
| Foto ingrandite (file vero contro larghezza resa, anche con `object-fit: cover`) | 0 | 0 | passa, anche a 320, 768, 1024 e 1920 |
| Formati | 1,7 (apertura), 1,5, 1,8 | 0,8, 1,5, 1,8 | passa (3) |
| Fondi delle sezioni | bianco, grigio sotto la foto d'apertura, rosso (1 sezione) | bianco, rosso | passa (3, rosso una volta) |
| Spazi tra le sezioni | 96 e 160 px (culmine) | 64 e 104 | passa (due valori, 1,67 volte) |
| Link `tel:` | 3 (testata, Va sul vostro mezzo, Ricambi), tutti `tel:+390499000103` | uguale | passa (3 per M) |
| `mailto:` | 4, tutti a info@molonmachinery.com: "Va sul mio mezzo?", "Ricambio Molon", "Rivenditori: listino e ordini", semplice nel piede | uguale | funzioni diverse, ognuna una volta |
| "Indicazioni" | 1 | 1 | passa |
| Numeri ripetuti più di 2 volte fuori dalle tabelle | "120" 3 volte, ma è il nome del modello MINOR MINI 120 e l'inizio della misura dei posteriori | uguale | vedi problemi aperti |
| Il telefono "049 900 0103" scritto | 2 volte (testata e piede) | uguale | passa |
| Lista nera, istruzioni sopra 14 px, "indicativ", repertorio | 0 | 0 | passa |
| Peso caricato | 645 KB (1920: 850 KB) | 436 KB | passa (3 MB) |
| Bottoni in pagina | 6 | 6 | il tetto ibrido non lo fissa; D8 ne chiede 5 (vedi sotto) |

Contrasto del titolo e della riga sul cielo, misurato sulle fasce senza testo della schermata a 1440: sfondo con luminanza da 0,73 in su, quindi almeno 12:1 con l'antracite. Bianco sul rosso 5,6:1, grigio del testo secondario 6,9:1 sul bianco.

### Controlli a 320, 390, 768, 1024, 1440 e 1920
Larghezza del documento uguale alla finestra a tutte e sei; 0 sovrapposizioni tra testi e immagini (escluse le scritte volute sulla foto d'apertura e la barra ferma del telefono, che passa sopra le tabelle); 0 errori di script; la testata con il telefono resta davanti a metà pagina a ogni larghezza. Provato a mano con Playwright: la colonna "Va sul vostro mezzo?" resta ferma a 1440 accanto alle tabelle dei posteriori, la barra in basso a 390 accanto alla tabella dei frontali; i bottoni delle tabelle si aprono e si chiudono con `aria-expanded`. Screenshot rifatti in `screenshot/home/` (stessi nomi, più `home-1920-prima-schermata.jpg` e `home-320-prima-schermata.jpg`) e guardati a pezzi accanto alla versione professionale e alle prime schermate di Rapid e Reform.

### Compiti della scheda d'uso e dove stanno ora
- **Contadino, 390.** (1) Prima schermata: la foto vera al 58 %, il titolo, la riga con il mestiere, i tre mezzi e il luogo. (2) "Va sul vostro mezzo?" porta con un tocco alle tabelle (frontali aperta); dal menu "Frontali", "Posteriori a 3 punti" e "Per motofalciatrici" in due tocchi; le sei schede sono alla seconda schermata. Tabelle a 390 con modello, doppi denti, lavoro, massima e peso, senza scorrimento orizzontale (sotto i 375 px si nasconde "Massima"). (3) La presa di forza è il primo fatto dei frontali; "Va sul vostro mezzo?" con Chiama e Scrivete è una barra ferma in basso finché si guardano le tabelle. Le marche dei mezzi restano fuori. (4) "Rivenditori" in testata e nel menu, zona, nome, città e sito; DE in testata a 44 x 44 px.
- **Proprietario con guasto, 390.** (1) Telefono in testata fissa, sempre. (2) "Ricambi" nel menu e in testata a 1440: il blocco rosso con le tre cose da dire. (3) "Manda la foto per email" con oggetto e traccia. (4) Orari: non pubblicati, la pagina non li inventa.
- **Rivenditore, 1440.** (1) Le sei famiglie con foto, nome e misura alla seconda schermata, tutte link. (2) Tabelle in testo selezionabile con cifre tabellari (posteriori e motofalciatrici a un clic). (3) Schede tedesca e inglese sotto ogni tabella; depliant PDF ancora da avere. (4) "Siete un rivenditore o un'officina?" con l'email del listino; email, telefono e indirizzo copiabili nel piede. Il modulo con la scelta "Listino e ordini per rivenditori" non c'è più: lo sostituisce l'email con la traccia.

### Problemi aperti
- **Didascalia dell'apertura**: il modello F la prevede, ma luogo e anno della foto non si sanno, e i 160 caratteri non bastavano anche per lei: la foto d'apertura non ha didascalia. Quella della culmine dice "MAJOR 180.3 dietro una motofalciatrice / Prato di montagna, foto Molon", senza anno. Vanno chiesti luogo, anno e autore di tutte e due (LEGGIMI).
- **Il portattrezzi dell'apertura** ha un adesivo "G6" e una piccola targhetta gialla: la marca non è leggibile e non è scritta, ma un contadino la riconosce. Se Molon preferisce, si rifà la foto (LEGGIMI, "Foto da fare").
- **Telefono nel piede in testo, non link**: per stare nei 3 `tel:` di D12. La testata fissa lo ha sempre in vista.
- **6 bottoni in pagina** (D8 ne vuole 5): Va sul vostro mezzo, Chiama e Scrivete accanto alle tabelle, i due di Ricambi, il listino. Togliendo "Scrivete per il listino" (diventerebbe un link) si scende a 5.
- **"120" tre volte** fuori dalle tabelle: è il nome di un modello (MINOR MINI 120) e una misura; lo lascio.
- **Colonna sinistra vuota nella schermata intera** accanto alle tabelle: dal vivo c'è "Va sul vostro mezzo?" che resta ferma; nella schermata intera resta in alto.
- **Prove con il nome**: nessun lavoro con cliente, luogo e anno e nessuna recensione con nome nelle fonti (LEGGIMI, punto 7). Le prove in pagina sono le persone (Enio e Bruno Molon), i rivenditori con il nome e l'archivio.
- **Giudizio**: non ho rifatto il giudice da agenzia né le prove dei clienti tipo; le misure dicono che i tetti passano, il voto va dato da chi guarda.
- Nessun carattere U+2014 nella pagina, negli script, in DIREZIONE e in questa nota. Nessun commit.


## Livello professionale (3/11/2026), con il ritocco finale (sostituito dal metodo ibrido; copia in `_prova/versione-pro/`)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso), struttura A1 adattata a un costruttore di macchine da fieno che vende tramite rivenditori. Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14 (fogli in `_prova/pro-controllo/rif/`), le pagine intere di barth e Cly-Del (a pezzi), più Budri e Odermatt nel controllo. Scheda d'uso: `_prova/uso/SCHEDA.md`.

Questa home sostituisce "Il pettine" (versione 1, copiata com'era in `_prova/versione-1-originale/` con sito e screenshot).

Pagina: `sito/index.html` (statica, si apre con file:///), immagini WebP in `sito/img/`, carattere in `sito/fonts/`. Sorgente: `_prova/script/pagina-pro.html`. Si rifà tutto con `bash _prova/script/build_finale.sh` (logo `finale_logo.py`, immagini `pro_img.py`, pagina, screenshot `pro_shot.mjs` a 1440, 390, 320, 768 e 1024, controlli `pro_controlli.mjs` in `_prova/pro_controlli.json`). Altezza: 11.530 px a 1440, 17.930 a 390.

### Ritocco finale: che cosa è cambiato rispetto alla prima passata "livello professionale"
Dal controllo del livello (voto 6) e dalle prove dei due clienti tipo (6,5 e 6,5):
- **Apertura con un gesto**: blocco antracite pieno con l'H1 bianco a 72 px (era 64 su bianco), occhiello bianco con il filetto rosso, la foto vera a filo destro e senza raggio, i tre ingressi in fila sotto, divisi da filetti scuri, solo testo, con la misura su una riga. Taglio della foto spostato sulla macchina e sull'andana (via il 16 % a destra, dove c'è il portattrezzi). Tolto "dal 1967" dalla riga del mestiere: in apertura resta "dal 1936" una volta sola.
- **390, bottone principale a tutta larghezza** (350 px). "Ricambi" diventa la prima riga degli ingressi ("Macchina ferma: come ordinare il pezzo"); i quattro ingressi stanno in righe di 56 px divise da filetti e l'ultimo finisce a y 815 su 844.
- **Nuova sezione "Le macchine"** subito sotto l'apertura, al posto di girelli e scopatrici: sei schede in 3 colonne (2 sotto i 1100 px, 1 sotto i 720), foto 3:2 a tutta larghezza della scheda (409 x 272 a 1440, 348 x 232 a 390), fondo della foto e della scheda dello stesso grigio, nome a 24 px, misure, freccia, tutta la scheda è un link. La sesta è il gEnio, con la sua foto vera (`2025_02_gEnio-230-4-depliant.gif`). Sotto i 1100 px le foto restano.
- **Tabelle**: quella dei frontali resta aperta (il rivenditore ci arriva con un clic); quelle dei posteriori e delle motofalciatrici sono righe "6 modelli posteriori" / "10 modelli per motofalciatrici" con i nomi dei modelli e il bottone "Vedi i 6 modelli" / "Vedi i 10 modelli" (aria-expanded; senza JavaScript restano aperte). Sul telefono la colonna "Massima cm" ora si vede (era nascosta) e si nasconde "Pettini"; sotto i 375 px si nasconde anche "Massima" perché la tabella stia nei 280 px. Nota sotto i frontali: "Il 300 PRO lavora 280 cm; 320 cm è la larghezza massima."
- **"Va sul mio mezzo?"**: al posto del link al modulo in fondo, la domanda "Va sul vostro mezzo? Diteci marca, modello e presa di forza." con due bottoni, "Chiama 049 900 0103" e "Scrivete" (mailto con oggetto "Va sul mio mezzo?" e traccia: marca e modello, presa di forza con giri e verso, zona, nome e telefono).
- **Numeri**: solo dati dell'azienda, a 96 px: 25 modelli di ranghinatori (9 + 6 + 10, dalle tabelle), 5 famiglie di macchine, 3.000 m² coperti, 5,0 su Google con 8 recensioni. Via 1936, 1967 (restano nella cronologia) e "100-280" (misura di prodotto).
- **Ricambi**: colonna di destra allineata in alto con il numero grande in bianco sopra i due bottoni; via il fax; "Se non rispondiamo, mandate la foto con il vostro telefono a info@molonmachinery.com" con il link alto 44 px.
- **Prezzo**: "Per il prezzo rivolgetevi al rivenditore o chiamateci" (prima la pagina dava per certo che il prezzo lo fa il rivenditore).
- **Contatti**: a partire da 1100 px i recapiti restano fermi accanto al modulo mentre si scorre (sticky).
- **Foto in serie**: stesso trattamento per tutte le foto in campo e per la squadra in `pro_img.py` (bianco neutro corretto a metà, spalla morbida sulle alte luci che recupera il cielo dell'apertura, ombre appena aperte, saturazione 0,92, contrasto 1,04); velatura tolta dalla foto del lago.
- **Codice e tocco**: nessuno stile in riga (fax, indirizzo e titolo "Lingue" del piede in classi; colore del link email in classe); il filetto dei numeri è il token `--filetto-chiaro`; link del piede, Privacy, Cookie, informativa del modulo e lingue (44 x 44, distanza 4 px) di almeno 44 px. Il menu del telefono si chiude prima di scorrere alla sezione, così il titolo non finisce più sotto la testata (prima, a 390, Ricambi dal menu arrivava 139 px troppo in alto).
- Occhiello dei frontali "Ranghinatori frontali per portattrezzi e trattori"; testo alternativo del MAJOR allineato alla tabella.

### Le prime schermate
- **1440 x 900**: testata bianca fissa di 81 px (logo, cinque voci, IT DE EN FR, bottone rosso "049 900 0103"). Blocco antracite: a sinistra occhiello "Arlesega di Mestrino (PD) · dal 1936", H1 "Ranghinatori a cinghie" a 72 px, riga "per portattrezzi, trattori e motofalciatrici", frase loro, "Chiama 049 900 0103" pieno e "Ricambi" bordato; a destra la foto vera 4:3 a filo del bordo. Sotto, i tre ingressi per mezzo (712-864 px).
- **390 x 844**: testata fissa di 73 px con logo, telefono e Menu; IT DE EN FR a vista; foto 16:9 a filo; blocco antracite con occhiello, H1 a 40 px, riga del mestiere, "Chiama 049 900 0103" a tutta larghezza, poi Ricambi e i tre ingressi (fino a y 815).
- **1024 x 768**: come a 1440 con il menu nel bottone; gli ingressi entrano interi. **768 x 1024**: foto 16:9 sopra, testo e ingressi in tre colonne sotto. **320 x 640**: come a 390; il telefono in testata perde l'icona.

### Le 15 regole, una per una
Misure di `node _prova/script/pro_controlli.mjs` (`_prova/pro_controlli.json`), più gli screenshot guardati a pezzi a 1440, 390, 320, 768 e 1024.

1. **Telefono come bottone nella testata fissa: passa.** Testata sticky di 81 px a 1440 e 73 a 390; bottone pieno alto 48 px con il numero. Al 50 % della pagina il bottone sta a 16 px dall'alto a 1440 e a 12 a 390 e `elementFromPoint` lo trova. 10 link `tel:`, tutti `tel:+390499000103`. Per M c'è anche la voce Contatti con il modulo.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** H1 con il mestiere, "Arlesega di Mestrino (PD)", "dal 1936", bottone di chiamata in vista; a 390 il bottone è largo 350 px su 350 (a tutta larghezza) e Ricambi resta in vista come prima riga degli ingressi.
3. **Immagine vera nell'apertura: passa.** Il frontale Molon rosso al lavoro sul prato in collina, con l'andana, tagliato sulla macchina. Riserva: il portattrezzi (senza marchi leggibili) occupa ancora la parte destra; la foto da rifare è nel LEGGIMI.
4. **Zero repertorio: passa.** `indicativ` 0, `unsplash|pexels` 0; 13 immagini visibili, tutte foto di Molon in `sito/img/`; nessuna illustrazione (gli SVG sono il logo, il telefono e le frecce).
5. **Foto in serie: passa con riserva.** Tre formati a ogni larghezza (4:3, 3:2, 16:9: a 1440 apertura, lago, MAJOR e archivio 4:3, schede 3:2, squadra 16:9; a 390 apertura e squadra 16:9); 1 didascalia su 13 immagini; stesso trattamento colore per tutte le foto in campo, schede tutte sullo stesso grigio con la stessa linea di terra. Riserva: restano scatti di anni e luci diverse (archivio in bianco e nero, squadra a luce piatta); la serie vera è la giornata di riprese del LEGGIMI.
6. **Palette dal marchio: passa.** `--rosso` #C8231B (la vernice delle macchine) e `--rosso-scuro` solo al passaggio del mouse; `--antracite` #1F2122 dal logo; il resto sono neutri freddi. 0 colori scritti fuori da `:root` (anche il filetto chiaro è un token). Nessun beige.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 20, 24, 32, 48, 72, 96) e 8 a 390 (14, 16, 18, 20, 24, 28, 40, 48); testo corrente 17/16 px; nessun testo sotto i 14 px; H1 72/40, H2 48/28 (fascia M).
8. **Due famiglie al massimo: passa.** Una sola, Sofia Sans, pesi 400 e 700.
9. **Schede con la foto: passa.** Sezione "Le macchine": 6 schede in 3 colonne a 1440 (passo 24 px), ognuna con la foto 3:2 dello stesso taglio (409 x 272), il nome e la freccia; tutte link. Le foto restano a tutte le larghezze (2 colonne sotto i 1100, 1 sotto i 720).
10. **Almeno tre tipi di prova: non passa (2 su 4).** Ci sono 4 numeri aziendali (25 modelli, 5 famiglie, 3.000 m², 5,0 su Google con 8 recensioni) e la fascia dei partner con paese e sito. Mancano recensioni con nome e comune, clienti con il nome e certificazioni: non sono nelle fonti (01-analisi: "Nessuna certificazione, nessun premio, nessun cliente citato") e non sono stati inventati; vanno chiesti (LEGGIMI, punto 7).
11. **Lavori con un nome: non passa.** Nessun lavoro con cliente, luogo e anno nelle fonti (LEGGIMI, punto 7).
12. **Ritmo a blocchi: passa.** Apertura, Ricambi e Chi siamo in antracite, Come lavora in rosso Molon (4 blocchi pieni oltre al piede); Posteriori e Contatti in grigio. Sezioni 120/120 px a 1440 e 72/72 a 390; margini 80 a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: passa.** 17 bottoni visibili a 1440, pieno rosso e bordato, raggio 4 px, 52 px (48 in testata), testo 17/16 px; tutti i bottoni di chiamata contengono "049 900 0103".
14. **Modulo e "dove" per il mestiere: passa.** Modulo con tipo di richiesta, nome, azienda, email, telefono, paese e zona, presa di forza, mezzo, macchina Molon dalla targhetta, messaggio; al posto dell'allegato del disegno la pagina chiede di allegare le foto all'email che si apre (un mailto non porta allegati; il servizio vero è nel LEGGIMI). Sede con "Vai alla mappa" e "Indicazioni stradali"; 0 iframe.
15. **Piede completo: non passa del tutto.** Quattro colonne (4fr 3fr 3fr 3fr), testo di 17 px e di 14 nella riga legale, ragione sociale, indirizzo, P.IVA 00258060284, telefono ed email cliccabili, mappa, rivenditori, lingue, Privacy e Cookie, link alti 44 px. Mancano gli orari (non pubblicati) e le certificazioni (nessuna nota): LEGGIMI punti 1 e 7. La ragione sociale S.r.l. o S.n.c. è da confermare (punto 8).

### Compiti della scheda d'uso (par. 8), dopo il ritocco
- **Contadino, 390 x 844.** In prima schermata la foto vera, il mestiere, il telefono a tutta larghezza, le lingue e i tre ingressi per mezzo: un tocco su "Motofalciatrici e motocoltivatori" porta a MINI, MIKY e MAJOR con larghezze e pesi. **Riesce**, come prima. "Va su un Reform a 540 giri?": i giri sono scritti, le marche no (vanno confermate da Molon, LEGGIMI punto 3); adesso accanto alla domanda ci sono "Chiama" con un tocco e "Scrivete" con la traccia già pronta, invece del modulo a 11.000 px. **Riesce a metà, meglio di prima.** Scelta della larghezza: frontali in tabella aperta; per posteriori e motofalciatrici le misure sono nel titolo, nella riga di presentazione e nelle tre schede MINI, MIKY e MAJOR, e la tabella intera è a un tocco ("Vedi i 6 modelli"); la colonna della larghezza massima ora si vede sul telefono. **Riesce.** Rivenditore: invariato (Gasser con il sito, "chiamateci" per le altre zone). **Riesce a metà.**
- **Proprietario con guasto, 390 x 844.** Telefono a tutta larghezza e "Ricambi" in prima schermata; un tocco chiama, un tocco porta al blocco Ricambi con il numero grande, le tre cose da dire e "Manda la foto per email". **Riesce.** Orari: non pubblicati, quindi il compito 1 resta senza "orari di oggi" (LEGGIMI punto 1). Ricambi dal rivenditore e tempi: non nelle fonti (punto 2).
- **Rivenditore, 1440 x 900.** Le tre famiglie e il telefono in prima schermata; un clic porta alla tabella aperta dei frontali. **Riesce.** Depliant PDF: non esiste (punto 6). Email e telefono in testo copiabile. **Riesce.**
- **Per tutti**: 0 link "#", nessuna foto di repertorio, nessuna immagine riscalata a fingere un altro modello, larghezza del documento uguale alla finestra a 320, 390, 768, 1024 e 1440, 0 sovrapposizioni, nessuna zona toccabile sotto i 44 px a nessuna delle cinque larghezze (escluso il link nascosto "Vai al contenuto").

### Foto, origine e trattamento
Tutte di Molon Giovanni, da molonmachinery.com (`assets/originali/`, voti in `_prova/inventario-immagini.json`, elenco in `assets/CREDITI.md`):
- `apertura-*` (4:3) e `apertura-tel-*` (16:9): `2017_10_11.08_10ritoc.jpg` (3264 x 2448), tolto il 16 % a destra, al massimo 1600 px.
- `frontale-lago-*`: `2017_10_11.08_4-copia.jpg` (2000 x 1500), 4:3, velatura tolta.
- `major-prato-*`: `2025_03_dok-tc-07-molon-br.jpg` (4032 x 3024, orientamento EXIF corretto), 4:3.
- `archivio-*`: `2017_10_foto4.jpg`, 4:3, bianco e nero neutro.
- `squadra-*`: `2017_10_P1090586_mod-1.jpg`, 16:9.
- `s-*`: gli scontornati `2017_10_230_5-scont.jpg`, `2017_10_RANGHINATORE-POST09noEtichette.jpg`, `2018_01_MAJOR160_sf.jpg`, `2025_02_gEnio-230-4-depliant.gif`, `2017_10_girello-380.jpg`, `2017_10_SCOPA-lamiera.jpg`, moltiplicati sul grigio #F0F1F1 a parità di massa, 3:2.
Nessuna foto mostra macchine di altri costruttori con marchi leggibili in primo piano.

### Caratteri e licenze
Sofia Sans (Lettersoup, Google Fonts), file variabile latino servito dalla pagina (`sito/fonts/sofia-sans-latin-var.woff2`), SIL Open Font License 1.1, testo in `sito/fonts/OFL-Sofia-Sans.txt`: uso commerciale libero.

### Fonti dei dati in pagina
`01-analisi.md` (storia, numeri, recapiti, partner, testi loro), `_prova/uso/SCHEDA.md` (portattrezzi, compiti), le tabelle dei modelli lette il 3/11/2026 sulle pagine di molonmachinery.com (`_prova/crawl/`). "25 modelli" è la somma delle tre tabelle (9 + 6 + 10); "5 famiglie" sono frontali, posteriori, per motofalciatrici, girelli e scopatrici (le voci Prodotti del sito di oggi).

### Controlli fatti (3/11/2026, ritocco finale)
- Screenshot rifatti in `screenshot/home/` (1440 e 390 intere e prima schermata, chiusura a 1440, prime schermate a 320, 768 e 1024) e guardati a pezzi, insieme alle pagine intere a 320, 768 e 1024.
- Interazione provata con Playwright: bottoni delle tabelle (si aprono e si chiudono, aria-expanded e testo corretti), menu del telefono (Ricambi, Rivenditori e Contatti arrivano a 80 px dall'alto, sotto la testata), ingresso "Ricambi", link "Chiedete il vostro" che sceglie il tipo nel modulo, avviso del modulo senza nome ed email. Unico messaggio in console: aprendo da file:// il preload del carattere è bloccato dal browser (CORS dei file locali); il carattere si carica comunque, e su un server il messaggio non c'è.
- Nessun carattere U+2014 nella pagina, negli script, in questa nota, nel LEGGIMI e nei CREDITI.


## Versione 1, "Il pettine" (24/10/2026), sostituita

Archiviata con sito e screenshot in `_prova/versione-1-originale/`. La nota di allora segue com'era.


Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, logo con `finale_logo.py`, pagina da `pagina.html`, screenshot con `finale_shot.mjs`). Prove della prima schermata con `prove_apertura.mjs`, controlli finali con `controlli_finali.mjs`. Altezza a 1440: 5517 px, piede compreso; a 390: 6690 px.

### L'idea
Il ranghinatore frontale a cinghie, scontornato e nitido sulla carta color fieno, è l'unico protagonista, e si misura: scegliendo il modello la macchina cambia larghezza in scala sopra una sola linea di terra quotata da 0 a 320 cm, con la barra rossa del lavoro e quella grigia della larghezza massima. È la loro tabella dei frontali (190, 210, 230, 250, 260, 300 PRO) resa visibile sul loro oggetto: con il nome di un altro costruttore la scala e i numeri non tornano più.

### Le prime due schermate
1. A 1440: testata con il logo MOLON in SVG, cinque voci, telefono e lingue. Titolo "Ranghinatori a cinghie" a 112 px su una riga. Sotto, a sinistra, la frase sulle tre operazioni e il bottone rosso "Chiama 049 900 0103"; in basso a sinistra la scelta del modello (sei numeri in cifre tabellari, Versione PRO, gEnio) con la riga "280 cm di lavoro, 320 massima, 16 pettini"; a destra la macchina sulla linea di terra. All'apertura è scelto il 300 PRO, il più largo. Nessuna legenda a filetti, nessuna riga "luogo, dal anno".
2. "Nove frontali per trattore, da 190 a 280 cm di lavoro": i sei dati del modello scelto (si aggiornano con la scelta in alto) e le quattro parti in una riga di testo con filetto sopra (denti doppi, pettini su cinghie trapezoidali, bandella fermafieno, ruote ballon), poi la nota su PRO e gEnio e su come è riportata la foto. Poi la gamma 2x2, la storia con l'archivio a filo, la riga dei rivenditori, la chiusura con la foto in campo, il piede.
A 390: testata con logo, telefono e bottone "Menu"; titolo su due righe, frase, bottone rosso, scelta del modello, la macchina sulla linea di terra: tutto dentro gli 844 px. Da 960 a 1439 la prima schermata scala anche con l'altezza della finestra (a 1366x768 e 1280x720 bottone e linea di terra restano sopra la piega); sotto i 960 si impila.

### Caratteri e colori, con i riferimenti
- Sofia Sans (Lettersoup, Google Fonts), una famiglia sola, file variabile latino servito dalla pagina (`sito/fonts/sofia-sans-latin-var.woff2`). Licenza SIL Open Font License 1.1, testo in `sito/fonts/OFL-Sofia-Sans.txt`: uso commerciale libero. Titoli 380 con spaziatura da -0,025 a -0,035em, testo 400, etichette e titoletti 500; cifre tabellari per modelli, misure e telefono. Motivo: è la scelta della guida per macchine e industria (c1, riferimenti Festool e Metzner), un impianto DIN con più calore, vicino alle scritte delle targhette delle macchine.
- Carta #F3F0E7 (lo stesso fondo su cui sono moltiplicati gli scontornati), piede #E2DDCF con un filetto in cima, inchiostro #1E1D1A, grigio #5D5950 (6,1:1 sulla carta, 5,1:1 sul piede), rosso Molon #C8231B solo per il bottone, il tratto del modello attivo e la barra del lavoro (bianco sul rosso 5,6:1). Riferimenti: Sneeboer (un solo rosso del marchio), Reform (il rosso coerente con le macchine), Pöttinger (la macchina riconoscibile prima di tutto); la pulizia chiara dalle home amate di Mario Agnoletto e Hambro.

### Interazione
Un gesto solo, "Scegli il modello": radio veri (frecce della tastiera, focus visibile, dito), più due caselle. Al cambio la macchina e le due barre cambiano larghezza in 0,18 s (niente con prefers-reduced-motion), si aggiornano la riga sotto i numeri (annunciata con aria-live) e i sei dati della sezione seguente. Versione PRO si spegne dove non esiste (190, 210), è fissa sul 300 PRO e altrove torna com'era stata scelta dal visitatore (variabile separata, provata). gEnio aggiunge 60 kg. Valori della tabella del sito (11-16 pettini, doppi denti 4, 4, 4-5, 5-6 sul PRO, pesi da 210 a 350 kg). Il menu a 390 e il piede a fisarmonica a 390 usano veri bottoni con aria-expanded; sopra i 640 i titoli del piede sono testo semplice, fuori dall'ordine di tabulazione. Nessuna comparsa allo scorrimento, nessun effetto sul cursore, hover a colore pieno.

### Foto, origine e licenza
Tutte dell'azienda, da molonmachinery.com (`assets/originali/`, vedi `assets/CREDITI.md`); nessuna foto di repertorio, nessuna immagine generata, nessuna foto già usata in un'altra home della campagna.
- `macchina-*`: `2017_10_230_5-scont.jpg` (2048x1536, fondo bianco), moltiplicato sulla carta con ombre di contatto; a 1440 è larga al massimo 880 px, quindi la variante da 1780 px basta anche a 2x. Per gli altri modelli la stessa foto è riportata in proporzione alla larghezza massima, e la pagina lo dice nella nota.
- `gamma-*`: `2017_10_RANGHINATORE-POST09noEtichette.jpg`, `2018_01_MAJOR160_sf.jpg` (fondo grigio riportato a bianco), `2017_10_380-2.jpg`, `2017_10_SCOPA-lamiera.jpg`: ritagliate sul loro ingombro (ignorando i puntini isolati), allineate a sinistra come i titoli, stessa linea di terra e stessa ombra; la scala sta a metà tra stessa area e stessa altezza, così il girello piatto e la scopatrice piena pesano uguale.
- `archivio-*`: `2017_10_foto4.jpg`, virata sul tono della carta, tagliata meno di prima.
- `chiusura-*`: `2017_10_11.08_10ritoc.jpg` (3264x2448, la foto migliore dell'inventario, voti 7/7), taglio 4:5 a sinistra: la macchina, l'andana e i due alberi sul crinale. Del portattrezzi restano lo specchio e un pezzo di cabina sul bordo destro, senza marchi leggibili.
- `logo-molon.svg`: ricostruito dal logo piatto grigio, confrontato al 400 % con l'originale.

### Piede
Logo e una riga su chi sono; colonne Prodotti (cinque famiglie e Ricambi), Azienda (Chi siamo, Storia, Rivenditori), Contatti (telefono, fax, email, indirizzo, mappa), Lingua; ultima riga con ragione sociale, indirizzo, P.IVA, Privacy, Cookie, ©. Fondo #E2DDCF con filetto, nessuna ombra, nessuna icona. Nessuna colonna Seguici finché i canali YouTube non sono confermati come ufficiali.
Newsletter: non c'è, perché vendono tramite rivenditori in Italia e all'estero, la pagina News è vuota dal 2017, le fiere non vengono comunicate e il cliente finale compra dal rivenditore; al suo posto la riga dei rivenditori con il telefono.

### Cosa è cambiato nella rifinitura finale (giudizio cieco in `_prova/cieco.json`)
- Prima schermata rifatta dentro la stessa idea: tolte le quattro legende numerate a filetti e la riga "Arlesega di Mestrino (PD), dal 1936" accanto al bottone; il selettore è salito nella prima schermata e la macchina cambia larghezza in scala sopra la linea di terra quotata. Le parti sono scese in una riga di testo sotto la piega.
- Prima schermata scalata anche sull'altezza (`--u` con `100svh`): niente sovrapposizioni tra 1100 e 1366 (provate 960, 1024, 1100, 1200, 1280, 1366, 1440, 1920), bottone sopra la piega a 1366x768 e 1280x720.
- Bug PRO corretto: dal 300 al 260 il PRO si spegne se il visitatore non l'ha scelto; la sua scelta resta passando per 190, 210 e 300.
- "Scegli il modello" al posto di "Scegli la larghezza di lavoro"; la riga sotto i numeri dice i cm veri (300 PRO = 280 cm di lavoro).
- Gamma: scontornati ritagliati e allineati a sinistra, masse pareggiate, righe più vicine; sezione di circa 1100 px a 1440.
- Storia: "2025" diventa "Oggi"; i rivenditori escono dalla colonna e diventano una riga a tutta larghezza con cinque nomi; colonna di testo allineata al fondo della foto.
- Chiusura con la foto 7/7 dell'inventario al posto di quella da telefono.
- Piede: fondo più scuro con filetto; titoli di colonna non più bottoni sul desktop.
- A 390 zone toccabili di almeno 44 px (modelli, caselle, link del piede e dei recapiti, logo), niente riquadro azzurro al tocco.
- Testi: h2 della gamma "Le altre macchine Molon" (non ripete più la frase d'apertura), sottotitolo riscritto; tolti gli indici 01-04 dalle parti.

### Controlli
- Screenshot guardati a pezzi: 1440 intera e prima schermata, 390 intera e prima schermata, chiusura e piede a 1440, più 320x640, 768x1024, 1024x768, 1920x1080 e le prove a 960, 1100, 1200, 1280, 1366 con il 190 e il 300. Larghezza del documento uguale alla finestra a 320, 360, 390, 640, 768, 900, 1024, 1099, 1100, 1280, 1366, 1440, 1920 e 2560.
- Interazione provata con Playwright: frecce e spazio sui radio, spazio sulla casella PRO, sequenze 300-260, 260 PRO-300-260, 190-230; tocco sui modelli a 390; menu con Esc; fisarmonica del piede. Nessun errore in console.
- Link: `tel:+390499000103`, `mailto:info@molonmachinery.com`, Google Maps su "Via Mestrina 10 35035 Arlesega Mestrino PD".
- `segnali.sh` a 1440: 0 soglie da correggere su 10, 0 da guardare su 8; foto al 35,1 %, una famiglia, 14 filetti larghi, 2 fasce di fondo (pagina e piede), H2 in 4 misure. L'unico gradiente sono le tacche della linea di terra.
- Nessun carattere U+2014 nella pagina, negli script, in questa nota e nel LEGGIMI.
