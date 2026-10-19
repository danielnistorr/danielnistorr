# Tek.Lam, home finale: nota

Pagina: `sito/index.html` (si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, pagina da `home_finale.html`, controlli con `controlla_finale.py`, screenshot). Parte dal prototipo A ("Il foglio", `_prova/home/a/`) con tutte le indicazioni del giudizio applicate; la prima schermata è stata ripensata, non ritoccata.

## L'idea

Il segno del logo Tek.Lam è un raggio laser rosso che scende nella lamiera e gira a 90 gradi: taglio e piega in un tratto solo. In pagina quel raggio esce davvero dal logo. Scende tratteggiato lungo il margine sinistro, accanto al titolo, e in basso gira ad angolo retto. Diventa così la linea di quota sotto la foto, che è incorniciata nelle proporzioni del foglio intero 3000 × 1500 mm, il campo di lavoro del loro laser e della punzonatrice SG6. Il tratto si disegna una volta sola al caricamento (300 ms in giù, poi 320 ms in orizzontale) e poi resta fermo. Sul telefono il foglio si gira (1500 × 3000) e la quota dice 1500. Senza il logo di Tek.Lam l'idea non regge: il tratto parte dal loro segno.

## Prime due schermate

1. A 1440. Fondo acciaio caldo #DEDBD5. A sinistra il titolo "Tagliamo, pieghiamo e saldiamo a Tombelle", in Mona Sans stretta (larghezza 75) peso 500 a 104 px, grafite. A destra, su 8 colonne, la cornice 2:1 con la loro foto: saldatura TIG su un cassone inox col film protettivo blu stampato, una mano al lavoro. Sotto corre il raggio rosso con la quota 3000. Più sotto la frase su chi sono, il bottone rosso "Mandaci il disegno" (a 706-758 px), il telefono e due didascalie: cosa c'è nella foto e perché la cornice ha quelle proporzioni. A 390 vengono prima il titolo su tre righe, poi la cornice verticale alta il 46 % dello schermo con la didascalia di fianco, la quota 1500, la frase, il bottone (750-798 px) e il telefono, tutti dentro gli 844 px.
2. "Le lavorazioni, sotto lo stesso tetto": cinque schede (punzonatura e cesoia, taglio laser, piegatura, saldatura, tubi e profili). Ognuna ha la foto nella stessa cornice 2:1, la quota rossa dove la misura è della macchina in foto (asse X 3000 della SG6, lunghezza utile 3100 delle piegatrici), una frase e tre dati. La scheda aperta all'arrivo è la SG6, la macchina che ha solo Tek.Lam fra le loro: punzona e cesoia insieme.

Poi la fascia a tutta larghezza della piegatura (foto loro), i sei settori, la storia della famiglia Volpato come quota (1978, 2020, oggi), le due persone con l'email, il campo rosso dei contatti (telefono grande come primo recapito, email, indirizzo, sede e mezzi con 50 q e 35 q) e il piede con i dati societari.

## Caratteri

- Mona Sans (Degarism Studio per GitHub), da Google Fonts, licenza SIL Open Font License 1.1 (testo in `sito/fonts/OFL-MonaSans.txt`). Viene servita dalla pagina come file woff2 variabile, con gli assi peso 200-900 e larghezza 75-125. È una sola famiglia per tutto. La larghezza 75 fa i titoli (peso 500 per l'apertura e il campo dei contatti, 450 per gli H2, dopo il giudizio che voleva i titoli fra 400 e 500 e non più a 200). La larghezza 100 fa il testo a 17 px e le didascalie a 14 px. Il riferimento è il grottesco tecnico stretto della direzione A dell'analisi, accanto al lettering TEK.LAM del logo. La scala è a forte contrasto: 104 px contro 14 px, come i titoli grandi e leggeri di Zahner e la sobrietà dei testi piccoli di De Castelli.
- Numeri: le cifre proporzionali di Mona Sans. Quelle tabellari hanno lo zero barrato e sembrano codice, e la guida vieta il monospazio, quindi niente monospazio, nonostante l'indicazione del giudizio di usarlo per le misure. Le misure stanno allineate in tabella con gli spazi indivisibili (3000&nbsp;mm, 049&nbsp;980&nbsp;14&nbsp;86).
- Maiuscolo spaziato solo per le tre etichette dei recapiti (Telefonare, Scrivere, Venire).

## Colori

- Fondo acciaio caldo #DEDBD5: il grigio freddo #E2E4E3 del prototipo, scaldato come chiedeva il giudizio.
- Grafite #1D1B18 (il nero del logo, scaldato), testo secondario #57534C.
- Rosso del raggio del logo #E30913, usato per il raggio, le quote, il bottone e la scheda attiva. Per il testo rosso piccolo c'è #B5070F.
- Campo dei contatti #D20A12: è il rosso del logo, appena più fondo perché il testo bianco regga il contrasto. Il "colore deciso che viene dall'azienda" che il committente ha amato nell'osteria. Il verde petrolio del logo non è usato: mai due colori forti nella stessa vista.

## Interazione

- Il raggio: si disegna una volta al caricamento e si ricalcola fermo, senza animazione, quando cambia la finestra. Con "riduci movimento" non c'è nessuna animazione.
- Le schede delle lavorazioni: si aprono con clic, tocco, frecce, Inizio e Fine, e il fuoco resta visibile. Il cambio di foto è secco (la dissolvenza da 140 ms del prototipo è tolta). Le transizioni sono di 180 ms, solo sul colore della scheda e del bottone. Sul telefono le schede sono una riga che scorre in orizzontale, con la scheda attiva sottolineata in rosso.
- Non c'è niente che compare allo scorrere e niente che segue il cursore. Nessun bottone sbiadisce: al passaggio cambia colore pieno.

## Foto, origine e licenza

Tutte le foto passano per la stessa gradazione, in `_prova/script/finale_img.py`: saturazione all'80 % (il film blu resta blu), neri sollevati verso una grafite calda, alte luci appena calde, curva morbida e nitidezza a misura. Vengono esportate in JPEG a 2-4 larghezze con srcset e a 1440 mai ingrandite oltre 1,1 volte, salvo la scheda Saldatura, ritagliata da slide1 e ingrandita 1,3 volte.

| In pagina | File | Origine | Licenza |
|---|---|---|---|
| Apertura (2:1 e 1:2), scheda Saldatura | `assets/originali/2020-08-slide1.jpg` | sito teklam.it, foto loro | da confermare con l'azienda |
| Scheda Punzonatura | `2020-08-slide3.jpg` | sito teklam.it, foto loro | da confermare |
| Scheda Piegatura e fascia | `2020-08-slide4.jpg` | sito teklam.it, foto loro | da confermare |
| Riquadro "La Byspeed nell'officina di Tombelle" | `2020-09-laserbystronic.jpg` (470 px, misura originale) | sito teklam.it, foto loro | da confermare |
| Sede, mezzi | `2020-09-fabbrica.jpg`, `2020-08-automezzi.jpg` (470 px) | sito teklam.it, foto loro | da confermare |
| Scheda Taglio laser, l'unica foto di repertorio | `assets/esterne/unsplash-cardinalli-Z0MTavs8WVg.jpg` | Clayton Cardinalli, https://unsplash.com/photos/Z0MTavs8WVg | Unsplash License (vedi `assets/CREDITI.md`) |
| Logo | `2020-07-logo-TEKLAM.png` | sito teklam.it | marchio dell'azienda |

La foto di repertorio è una sola, con la scritta "Foto indicativa", e il titolo della scheda è "Taglio laser", senza il nome della macchina. Non è nella scheda aperta all'arrivo. Il nome Bystronic Byspeed sta solo nel testo e accanto alla loro foto piccola. Nessuna immagine generata dall'IA e nessuna foto nuova scaricata in questo giro. La scheda Tubi e profili non ha foto: mostra in disegno le due sezioni più grandi che curva la Pedrazzoli (quadro 20 × 20 × 3, tondo Ø 32 × 2,2), ingrandite, con le quote rosse.

## Dati

Tutti da `01-analisi.md`: 4400 W, campo 3000 × 1500, SG6 X 3000 e Y 1500, cesoia Gasparini fino a 3000 mm, piegatrici Finn-Power 8 assi con bombatura Wila e Warcom con bombatura idraulica a 3100 mm, OMES 120 mm e 2000 mm, Pedrazzoli 20×20×3 e Ø32×2,2, Ercolina a controllo numerico, verniciatura e cromatura su impianti esterni collegati, 1978 FDS Volpato S.n.c. e ferro battuto, 2020 Tek.Lam S.r.l., Sandro e Dimitri Volpato, indirizzo, telefono, fax, email, P.IVA, casello A13 Padova Interporto, autocarro centinato 50 q di portata utile, autocarro con gru 35 q complessivi. Le righe sotto i settori (case metallici, cassetti e mobili in lamiera verniciata, telai per banchi frigo, pannelli per cabine, griglie) vengono dalle sei schede di Realizzazioni del loro sito. Tolti rispetto al prototipo: la "zincatura" (Attrezzature dice solo verniciatura e cromatura), le quote "misure della macchina" e il titolo con il nome della macchina sulla foto di repertorio, la didascalia "il nostro laser" sotto una foto non loro, la frase "La pagina ha le sue proporzioni". Gli spessori massimi del laser restano fuori, perché le due pagine del loro sito non concordano.

## Controlli fatti

- `segnali.sh` sulla pagina a 1440: uscita 0, nessuna soglia bloccante. L'area foto è al 35 %, proprio sulla soglia, perché le foto loro più larghe sono di 1330 px. Mona Sans è al 100 % del testo, monospazio 0 %, 18 filetti, 0 frecce, 0 etichette sopra i titoli, date 1978 e 2020. Restano due righe da guardare. Gli H2 hanno due misure (72 e 124 px): è voluto, perché l'elemento grande è uno per vista (il titolo d'apertura, poi "Mandaci il disegno" sul campo rosso). Il "gradiente" segnalato è il tratteggio del raggio (un repeating-linear-gradient rosso e trasparente), non una sfumatura.
- Screenshot a 1440, 390, 320, 768, 1024 e 1920, guardati a pezzi. Nessuno scorrimento orizzontale (larghezza della pagina uguale alla finestra a tutte le misure). Nessuna sovrapposizione: il raggio passa sempre nel canale a sinistra del titolo. Le schede sono state provate con clic, tocco e freccia a destra, e la foto cambia secco.
- Nessun U+2014 nella pagina, in questa nota e nel LEGGIMI (controllato da `controlla_finale.py`). Nessuna lineetta lunga, nessun gradiente viola, nessun testo in gradiente, nessuna emoji, niente Inter, niente bordo sinistro colorato, niente vetro, niente badge, nessuna icona e nessun componente di libreria.
- Divieti del committente: nessuno violato. L'unica animazione è il raggio al caricamento, chiesto dal giudizio.
