# San Marco Timbri, home finale: "L'impronta"

Pagina: `sito/index.html` (si apre con file:///, nessuna risorsa esterna). Si rifà tutto con `bash _prova/script/build_finale.sh` (scontorno, immagini, pagina, caratteri, screenshot).

## L'idea

Un timbro con la testa in ottone appena sollevato dalla carta, e accanto la sua impronta d'inchiostro, che scende dalla riga di base del titolo "Personalizziamo timbri e targhe": il mestiere detto con un oggetto e il segno che lascia.
L'impronta torna una volta sola come gesto: chi visita scrive il suo testo e vede il suo timbro stampato, poi lo chiede per email così com'è.
Il resto della pagina è carta chiara e ordinata: i timbri, le dieci lavorazioni in un indice, come si lavora, la chiusura con la foto e il piede.

Rispetto al prototipo A (giudizio del 24/10): niente più ceralacca né monogrammi altrui in apertura, il titolo sta sulla carta e non sopra una foto a tutta larghezza (gesto di Tek.Lam e Bazzato), l'oggetto è scontornato e a filo del bordo destro. Innestati da B: l'indice delle dieci lavorazioni, i tre passi a filetti, le righe dei recapiti a due colonne e la struttura del piede. Non presi da B: selettore dei materiali, Bodoni, blu notte, porta inglese.

## Le prime due schermate

- **1440 x 900.** Testata chiara: logo vero (scritta e leone), quattro voci, telefono in rosso timbro. A sinistra, sulla carta, il titolo a 116 px in Encode Sans largo (125 %, peso 340) su due righe; sotto, tre righe su cosa fanno, il bottone "Prova la tua impronta" e l'email. A destra il timbro scontornato, alto circa 550 px, con la testa d'ottone verso il titolo e il manico che esce dal bordo destro della pagina; tra i due l'impronta tonda "San Marco Timbri, 35129 Padova", che tocca la discendente della "g" di "targhe". Sotto la testa la didascalia "Foto indicativa".
- **Seconda schermata a 1440.** "Timbri in gomma e in metallo" con le tre famiglie in tre righe a filetti (gomma, metallo, ceralacca); accanto, subito, l'impronta interattiva (rettangolare all'inizio, così non ripete quella dell'apertura) e il modulo.
- **390 x 844.** Nell'ordine: il timbro in alto a filo del bordo destro con l'impronta in basso a sinistra, il titolo su due righe a 45 px che appoggia sull'impronta, la frase, il bottone a tutta larghezza, l'email. Testata con logo, telefono e un vero bottone "Menu".
- Altezza: 5531 px a 1440 (piede compreso), 6865 a 390, 5019 a 1024, 7591 a 768, 7078 a 320, 5880 a 1920. Nessuno scorrimento orizzontale a nessuna larghezza.

## Sezioni

1. Apertura (sopra).
2. Timbri in gomma e in metallo, con "Prova la tua impronta".
3. "Dieci lavorazioni, dal timbro all'insegna": titolo e frase (privati, aziende e strutture pubbliche; i timbri in metallo li chiedono soprattutto amministrazioni pubbliche, notai e avvocati, come dice la loro scheda), una foto loro a mezza larghezza fino al bordo (lettere in ottone brunito), poi l'indice 01-10 in due colonne a filetti sottili con le righe vere del loro elenco.
4. "I file li prepariamo noi": fascia bassa (480 px a 1440) con due presse per la stampa a caldo, dichiarata "Foto indicativa"; sotto, la frase sulle macchine e tre passi a filetti (File e loghi; Colori RAL o PANTONE; Prova e campionatura).
5. Chiusura "b con foto": "Per privati, aziende e strutture pubbliche" (frase loro), il telefono 049 776126 grande in rosso con tel:, poi quattro righe etichetta e valore (Cellulare e WhatsApp con wa.me, Email con mailto, Laboratorio con il link alla mappa, Zona); a destra fino al bordo la targa in corten (foto loro, l'unica in opera). Niente orari: non sono pubblicati.
6. Piede (sotto).

## Caratteri e colori

- **Encode Sans** (Impallari Type, Andres Torresi, Jacques Le Bailly; Google Fonts), una sola famiglia, file variabile con assi di peso e di larghezza, servito dalla pagina in `sito/fonts/`. Licenza **SIL Open Font License 1.1** (uso commerciale libero), testo in `sito/fonts/OFL.txt`. Titolo d'apertura largo 125 % peso 340; titoli di sezione 112 % peso 420; voci dell'indice 108 % peso 420 a 32 px; testo 100 % peso 400; cifre tabellari su telefoni, numeri dell'indice e P.IVA.
- Perché: la scritta larga e calma è quella delle targhe incise e dei timbri da ufficio; la larghezza variabile dà al titolo il passo della targa e al testo una lettura normale con una famiglia sola. Il registro chiaro, con un oggetto solo sulla carta, viene da Artisaire (un sigillo solo su un invito chiaro) e da Graf von Faber-Castell (un oggetto grande, testata bianca, poche voci), senza il loro corsivo d'accento. Encode Sans non è nelle liste b della guida e non è usato dalle 13 home amate.
- Colori: carta #F5F2EC, piede #ECE6DB, inchiostro #1B1A17 (15,6:1), grigio dei testi secondari #5B574F (6,4:1 sulla carta, 5,8:1 sul piede), ottone #8A6A2C solo sui numeri dei passi e sul contorno di fuoco (4,5:1), rosso timbro #B8261D solo sui numeri di telefono (5,6:1). Filetti #D6CDBE.

## Interazione

Un solo gesto, "Prova la tua impronta", dentro la sezione dei timbri. Tre righe di testo e la scelta tra timbro rettangolare e tondo: l'impronta si ridisegna subito in SVG con la grana dell'inchiostro e una leggera inclinazione, senza animazioni; i testi lunghi si stringono per stare nel timbro. Il bottone "Chiedi questo timbro" apre un'email a info@sanmarcotimbri.it con forma e testo già scritti (provato: `node _prova/script/fin_gesto.mjs file://.../sito/index.html <uscita.jpg>`). Tastiera: Tab sui campi, frecce sulla forma, fuoco visibile in ottone; dito: campi e bottoni alti 44-48 px. Le uniche transizioni (120 ms) sono il colore dei bottoni toccati. Niente che compare allo scorrimento, niente che segue il cursore.

## Foto, origine e licenza

Trattamento comune con PIL: saturazione al 86-92 %, un filo di contrasto, nitidezza leggera all'uscita; più larghezze con srcset; l'oggetto d'apertura in WebP con trasparenza e un'ombra morbida sulla carta.

| Dove | Foto | Origine | Licenza |
|---|---|---|---|
| Apertura | timbro con testa in ottone e manico in legno, scontornato | Pauline Raw, https://www.pexels.com/photo/a-wooden-stamp-on-a-white-surface-10559993/ (originale 3709x5564; dei quattro sigilli ho tenuto quello in alto, visto di lato) | Pexels License |
| Apertura | impronta tonda | disegnata in SVG nella pagina, stesso motore del gesto | |
| Dieci lavorazioni | lettere ritagliate a rilievo in ottone brunito | sito sanmarcotimbri.it, libreria media | dell'azienda, da confermare |
| Come lavoriamo | due presse per la stampa a caldo sul banco | Dana Sredojevic, https://www.pexels.com/photo/hot-stamping-machines-on-a-table-12884573/ | Pexels License |
| Chiusura | targa direzionale in acciaio corten su pilastro | sito sanmarcotimbri.it, libreria media | dell'azienda, da confermare |
| Testata e piede | logo orizzontale e verticale, bianco reso trasparente | sito sanmarcotimbri.it | dell'azienda |

Nessuna foto generata dall'IA, nessuna già usata in un'altra home della campagna (controllo sui `CREDITI.md`), nessun marchio concorrente in primo piano. La foto della chiusura non compare altrove nella pagina.

## Piede

Logo verticale vero (PNG originale 256x200 reso trasparente, in WebP senza perdite, mostrato a 128 px, quindi 2x; il leone non si ricostruisce in SVG senza l'originale vettoriale), una riga su chi sono e, sotto, la newsletter "Novità e promozioni" (campo a filetto, bottone, consenso privacy). A destra le colonne Lavorazioni (dieci voci su due sottocolonne), Idee regalo, Azienda (Chi siamo, Come lavoriamo, Promozioni e novità, Contatti) e Contatti (telefono e fax, WhatsApp, email, indirizzo con mappa). In fondo: "San Marco Timbri di Tosato Andrea, via G. A. Longhin 91, 35129 Padova, P.IVA 04289090286", Privacy, Cookie. Niente REA né capitale (impresa individuale), niente "Seguici" (nessun profilo verificato). A 390 le colonne si impilano: logo, Lavorazioni, Idee regalo, Azienda, Contatti, newsletter, riga legale.
La newsletter ha senso per la linea regalo (lauree, matrimoni, Natale) e per la pagina "Promozioni & News" che esiste già: il modulo controlla email e consenso ma non invia nulla finché non si collega a un servizio (LEGGIMI).

## Controlli

- Screenshot guardati a pezzi a 1440, 390, 320, 768, 1024 e 1920: nessuna sovrapposizione involontaria (l'impronta tocca il titolo e la testa del timbro copre il bordo dell'impronta per scelta), nessuno scorrimento orizzontale.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI e negli script; nessun punto mediano come separatore; voi ovunque.
- `segnali.sh` (`_prova/tmp-finale` cancellata, risultato riportato qui): famiglia unica Encode Sans, nessun carattere delle liste b, nessuna etichetta sopra i titoli, nessun titolo col punto, 3 misure di H2, 2 fasce di fondo, 26 filetti, 0 frecce, nessun numero grande con etichetta, nessun divieto trovato.
  - "Monospazio 100 %": falso positivo, lo strumento legge "code" dentro il nome "Encode Sans"; in pagina non c'è nessun monospazio.
  - "Area foto 24,6 %" (soglia 35 %): voluto. La pagina segue la ricetta del committente (carta chiara, un oggetto scontornato, aria); le foto ci sono in ogni sezione, ma le loro sono da 1000 px e non reggono di più. Con la giornata di still life (LEGGIMI) si possono allargare.
  - Numerazioni: 01-10 è l'indice delle dieci lavorazioni annunciate dal titolo; 1-3 sono i passi di una procedura vera.
  - Nessun contenuto con data o nome: l'anno di inizio e i lavori con cliente non sono pubblici (LEGGIMI).
- Divieti del committente: nessun gradiente, nessuna emoji, niente Inter, niente card con bordo colorato, niente vetro, niente tre box con icona, niente badge, nessuna icona Lucide, niente dissolvenze allo scorrimento, niente effetti sul cursore, niente bottoni che sbiadiscono, niente serif corsivo.
