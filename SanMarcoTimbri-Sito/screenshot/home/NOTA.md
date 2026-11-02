# San Marco Timbri, home finale: "L'impronta" (giro del 2 novembre)

Pagina: `sito/index.html` (si apre con file:///, nessuna risorsa esterna). Si rifà tutto con `bash _prova/script/build_finale.sh` (scontorno del leone, immagini, pagina, caratteri, screenshot).

## L'idea

La prima schermata è composta come un timbro tondo: una riga di testo sopra, il segno al centro, una riga sotto, tutto su un asse solo. Sopra c'è "Personalizziamo", al centro il loro leone traforato in ottone cromato, sotto "timbri e targhe". Il fondo è il blu dell'inchiostro da timbri, il colore che il loro lavoro lascia sulla carta; il resto della pagina è carta bianca da ufficio con il testo nello stesso blu.
L'impronta torna come gesto: chi visita scrive il suo testo, lo vede stampato in blu sulla carta e lo chiede per email così com'è.
Il piede torna sul blu, così la pagina si apre e si chiude come un foglio timbrato.

## Cosa è cambiato rispetto alla versione giudicata

Rispetto al giudizio cieco (`_prova/cieco.json`, 53/80) e alla richiesta del committente del 2 novembre ("più alta gamma, meno uguali tra loro"):
- **Apertura rifatta nell'impianto, non solo nell'oggetto.** Prima: carta beige, titolo a sinistra, timbro di repertorio scontornato a destra, impronta disegnata, "Foto indicativa" (lo schema di Hambro e Agnoletto). Ora: fondo blu inchiostro a tutta larghezza, asse centrale, titolo spezzato sopra e sotto il leone come la scritta di un timbro tondo, nessuna legenda e nessun "Foto indicativa". Confrontata con le prime schermate di Hambro, Agnoletto e della zona di Grisignano (`_invio/zona/home/copertine-est-grisignano.jpg`): nessuna ha un fondo di colore pieno con un oggetto centrato e il titolo diviso sopra e sotto.
- **L'oggetto è loro**: il leone traforato in ottone cromato della libreria media del sito (il leone lega nome, marchio e mestiere), scontornato dal cartone con `fin_leone.py` (maschera ristretta dentro il bordo, sfumatura di 1 px, il giallo del cartone tolto dal contorno), cromo reso neutro, ombra corta sul blu. Provato a deviceScaleFactor 2: nessun alone chiaro lungo il contorno.
- **Nessuna foto di repertorio in pagina**: via il sigillo di Pauline Raw e le presse di Dana Sredojevic. Tutte e tre le foto sono loro.
- **Colore di fondo dal mestiere**: blu inchiostro #26389C (apertura, piede, impronta) e carta bianca #FAFAF7 al posto del beige #F5F2EC.
- **Testata**: la sola scritta "sanmarcotimbri" in bianco, al centro sull'asse, a 30 px (il leone a tratto, illeggibile a quella misura, resta nel piede). Sotto i 1100 px il menu passa a un bottone vero.
- **Timbri e impronta**: le tre famiglie in tre colonne senza filetti, sopra; sotto due colonne, anteprima larga sette colonne su dodici (circa 690 px a 1440, 480 a 1024) e modulo a destra. Tolto `maxlength`: le righe lunghe si stringono nell'impronta e nell'email arriva il testo intero (provato con "Studio Notarile Bianchi Rossi & Associati S.r.l.").
- **Dieci lavorazioni**: indice senza numeri 01-10, nome e riga vera sulla stessa linea, accanto una sola foto loro alta quanto l'indice, a filo del bordo destro. È l'unico blocco a filetti della pagina (erano 26 filetti, ora 17 compresi quelli del piede).
- **Come lavoriamo**: niente più fascia di repertorio né passi numerati 1-3; titolo e due frasi loro (macchine, file, RAL o PANTONE, campionatura).
- **Chiusura**: frase loro "Su qualsiasi materiale, a fresa o a laser" (dalla riga "INCISIONI su qualsiasi materiale sia a fresa che laser", che ora compare solo qui; nell'indice Incisioni dice "A fresa e a laser"). Niente più tabella etichetta e valore: telefono grande, poi WhatsApp, email, indirizzo con la mappa e la zona in righe di testo semplici. La targa in corten è mostrata al massimo alla sua misura vera (624 px, prima 660 px ingranditi a 708), taglio senza il cielo bianco ai lati, foto a filo del bordo sinistro e testo a destra.
- **Piede**: newsletter in una fascia orizzontale sotto le colonne; Lavorazioni in due sottocolonne sotto un solo titolo; scarto tra le basi delle colonne sotto gli 80 px.
- Tolto il `<link rel=preload>` del carattere (errori CORS aperto da file://; `font-display:swap` basta).

## Le prime due schermate

- **1440 x 900.** Fondo blu fino a 890 px. Testata: quattro voci a sinistra, la scritta al centro, il telefono a destra, tutto in bianco. "Personalizziamo" a 103 px (Encode Sans largo 118 %, peso 330), il leone largo circa 610 px, "timbri e targhe" sotto; una riga ("Timbri in gomma e in metallo, targhe, insegne e segnaletica. Un laboratorio artigiano a Padova."), il bottone bianco "Prova la tua impronta" e l'email. In basso a destra, sul margine, la didascalia sobria "Leone traforato in ottone cromato".
- **Seconda schermata a 1440.** "Timbri in gomma e in metallo", le tre famiglie, l'impronta interattiva in blu e il modulo.
- **390 x 844.** Stesso asse: testata con scritta, telefono e "Menu"; "Personalizziamo" a 45 px, il leone quasi a tutta larghezza, "timbri e targhe", la frase, il bottone a tutta larghezza, l'email, la didascalia. Tutta l'apertura sta nella prima schermata.
- Altezze: 5024 px a 1440 (piede compreso), 6384 a 390, 6496 a 320, 6699 a 768, 4630 a 1024, 5114 a 1920.

## Sezioni

1. Apertura (sopra).
2. Timbri in gomma e in metallo, con "Prova la tua impronta".
3. "Dieci lavorazioni, dal timbro all'insegna": privati, aziende e strutture pubbliche; i timbri in metallo li chiedono soprattutto amministrazioni pubbliche, notai e avvocati (come dice la loro scheda); l'indice; le lettere in ottone brunito.
4. "I file li prepariamo noi".
5. Chiusura "b con foto" (foto a sinistra a filo del bordo, testo a destra). Niente orari: non sono pubblicati.
6. Piede.

## Caratteri e colori

- **Encode Sans** (Impallari Type, Andres Torresi, Jacques Le Bailly; Google Fonts), una sola famiglia, file variabile con assi di peso e di larghezza, servito dalla pagina in `sito/fonts/`. Licenza **SIL Open Font License 1.1** (uso commerciale libero), testo in `sito/fonts/OFL.txt`. Titolo d'apertura largo 118 % peso 330; titoli di sezione 112 % peso 420; voci dell'indice 110 % a 27 px; testo 100 % peso 400; cifre tabellari su telefoni e P.IVA.
- Perché: la scritta larga e calma è quella delle targhe incise e dei timbri da ufficio; la larghezza variabile dà al titolo il passo della targa e al testo una lettura normale con una famiglia sola. Encode Sans non è nelle liste b della guida.
- Colori: blu inchiostro #26389C (fondo di apertura e piede; bianco sopra 9,9:1, testi secondari #D2D7F0 6,9:1), carta #FAFAF7, testo #1C2A78 (12,2:1), grigio blu dei testi secondari #4F5674 (6,9:1), impronta #3443B0 (7,8:1), filetti #D5D8E3. Nessun rosso, nessun ottone di comodo: un timbro ha due colori, l'inchiostro e la carta.

## Interazione

Un solo gesto, "Prova la tua impronta", dentro la sezione dei timbri. Tre righe di testo e la scelta tra rettangolare e tondo: l'impronta si ridisegna subito in SVG con la grana dell'inchiostro blu e una leggera inclinazione, senza animazioni; i testi lunghi si stringono per stare nel timbro. "Chiedi questo timbro" apre un'email a info@sanmarcotimbri.it con forma e testo intero già scritti.
Provato con `node _prova/script/fin_gesto.mjs <url> <uscita.jpg>`:
- tastiera a 1440: Tab dalla testata ai campi nell'ordine giusto, freccia destra sulla forma passa a "Tondo", fuoco visibile;
- dito a 390: tocco su "Tondo", tocco su "Menu" (si apre, aria-expanded true), Esc lo chiude;
- bersagli alti 44-48 px.
Le uniche transizioni (120 ms) sono il colore dei bottoni toccati. Niente che compare allo scorrimento, niente che segue il cursore.

## Foto, origine e licenza

Trattamento comune con PIL: saturazione al 90-92 % sulle foto, cromo del leone quasi neutro (18 %), un filo di contrasto, nitidezza leggera all'uscita; più larghezze con srcset.

| Dove | Foto | Origine | Licenza |
|---|---|---|---|
| Apertura | leone traforato in ottone cromato, scontornato | sito sanmarcotimbri.it, libreria media (`traforato-in-ottone-cromato.jpg`, 1000x750) | dell'azienda, da confermare |
| Dieci lavorazioni | lettere ritagliate a rilievo in ottone brunito | sito sanmarcotimbri.it, libreria media | dell'azienda, da confermare |
| Chiusura | targa direzionale in acciaio corten su pilastro | sito sanmarcotimbri.it, libreria media | dell'azienda, da confermare |
| Testata e piede | scritta e logo verticale, bianco reso trasparente e ricolorato in bianco | sito sanmarcotimbri.it | dell'azienda |

Nessuna foto generata dall'IA, nessuna di repertorio, nessun marchio concorrente in primo piano. Il leone viene da uno scatto di 1000 px (il leone è largo circa 830 px nell'originale): a 1440 è mostrato largo circa 610 px, quindi a 1x è nitido, mentre su uno schermo 2x è ingrandito di circa 1,5 volte, morbido ma pulito; va rifatto in studio (LEGGIMI).

## Piede

Logo verticale vero (PNG originale 256x200, bianco reso trasparente, in bianco sul blu, mostrato a 120 px, quindi 2x; il leone non si ricostruisce in SVG senza l'originale vettoriale) e una riga su chi sono. Colonne: Lavorazioni (dieci voci in due sottocolonne), Idee regalo, Azienda (Chi siamo, Come lavoriamo, Promozioni e novità, Contatti), Contatti (telefono e fax, WhatsApp, email, indirizzo con mappa). Sotto, la fascia "Novità e promozioni" con campo, bottone e consenso; in fondo "San Marco Timbri di Tosato Andrea, via G. A. Longhin 91, 35129 Padova, P.IVA 04289090286", Privacy, Cookie. Niente REA né capitale (impresa individuale), niente "Seguici" (nessun profilo verificato). A 390 si impila: logo, Lavorazioni, Idee regalo e Azienda affiancate, Contatti, newsletter, riga legale.
La newsletter ha senso per la linea regalo (lauree, matrimoni, Natale) e per la pagina "Promozioni & News" che esiste già: controlla email e consenso ma non invia nulla finché non si collega a un servizio (LEGGIMI).

## Controlli (2 novembre)

- Screenshot guardati a pezzi a 1440, 390, 320, 768, 1024 e 1920; dettaglio del leone a deviceScaleFactor 2.
- scrollWidth uguale a innerWidth a 24 larghezze da 320 a 2560 (`_prova/script/fin_larghezze.mjs`).
- Collegamenti: `tel:+39049776126`, `mailto:info@sanmarcotimbri.it`, `https://wa.me/393761673361`, Google Maps su "Via Giacinto Andrea Longhin 91 35129 Padova"; nessuna ancora interna rotta.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI e negli script; voi ovunque.
- `segnali.sh` (cartella di uscita cancellata dopo la lettura):
  - OK: nessun carattere delle liste b, 0 etichette sopra i titoli, 0 titoli col punto, 3 fasce di fondo, 1 sola sezione titolo a sinistra e testo a destra, 17 filetti, 0 frecce, 0 numeri grandi con etichetta, 0 numerazioni, nessuna tabella, nessun divieto trovato, famiglia unica, nessun titolo nero.
  - "Monospazio 100 %": falso positivo, lo strumento legge "code" dentro il nome "Encode Sans"; in pagina non c'è nessun monospazio.
  - "Area foto 18,4 %" (soglia 35 %): voluto. Le foto loro sono da 1000 px e non reggono di più senza ingrandirle; la ricetta del committente chiede un solo oggetto con aria. Con la giornata di still life (LEGGIMI) si allargano.
  - Misure di H2: 60 px nelle sezioni e 13 px nei titoletti del piede.
  - Nessun contenuto con data o nome: anno di inizio e lavori con cliente non sono pubblici (LEGGIMI).
- Divieti del committente: nessun gradiente, nessuna emoji, niente Inter, niente card con bordo colorato, niente vetro, niente tre box con icona, niente badge, nessuna icona Lucide, niente dissolvenze allo scorrimento, niente effetti sul cursore, niente bottoni che sbiadiscono, niente serif corsivo, niente legende numerate sull'oggetto.
