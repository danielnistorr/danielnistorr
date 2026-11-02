# Fratelli Ruffatti, home finale: "Una canna"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `_prova/script/build_finale.sh` (immagini con `finale_img.py`, controlli con `finale_prova.mjs`, screenshot con `finale_shot.mjs`). Alta 6407 px a 1440 compreso il piede.

Si parte dal prototipo A scelto dal giudice. La prima schermata è stata ricomposta e non solo ritoccata (K0 era 7,5).

## Idea

Su carta avorio c'è una sola canna ad ancia vera, quella della Fratelli Ruffatti, aperta e messa in piedi. Va dal bordo alto al bordo basso ed è centrata sulle colonne 7 e 8: diventa l'asse della pagina, non un oggetto appoggiato al bordo come in Mario Agnoletto. A sinistra c'è la frase che hanno solo loro, presa dal sito: "Tutte le canne, costruite in casa". A destra le legende, e accanto a quella scelta la frase del mestiere. Con il nome di Mascioni o di Rieger la pagina non regge, perché la canna, il titolo e le frasi sono loro.

## Le prime due schermate

1. **A 1440x900.** In testata: logo corsivo bordeaux, quattro voci (Come costruiamo, Realizzazioni, Storia, Contatti), IT EN RU e telefono.
   - A sinistra il titolo in Gambetta 300 da 90 px su due righe (a 1920 sale fino a 110 px), poi una riga sola: "Organi a canne nuovi e restauri, a Padova dal 1940." Sotto il bottone bordeaux "Scriveteci" (mailto:) e il telefono (tel:).
   - Al centro la canna. A destra tre legende: Noce, Canaletto, Piede. Sotto la legenda attiva ci sono tre righe in Switzer 15 px, inchiostro pieno #1C1A17, con la parte in neretto. Le frasi vengono parola per parola dalla pagina "Canne ad ancia".
   - Sono spariti la scheda "Tav. 1", la didascalia in basso a sinistra e la legenda del risuonatore. Quel testo parlava delle trombe en chamade e non di questa canna.
   - **A 390x844**: titolo su due righe, la riga, bottone e telefono, poi la canna alta 560 px con le legende. Il testo della legenda attiva sta sotto la canna.
2. **"Ogni componente possibile, in laboratorio".**
   - A sinistra il testo breve con il link "Come costruiamo". A destra, fino al bordo, una foto loro: un registro di Tromba sul somiere (`xSfondo-trombe-2`), schiarita verso la carta. La foto Pexels di un altro costruttore è stata tolta.
   - Sotto, tre righe separate da filetti sottili, con la misura dentro il titoletto in Gambetta 28 px e la spiegazione a destra in Switzer 16 px: il 95 % di stagno nelle canne di facciata, il mogano sipo stagionato cinque anni, i pannelli da 48 mm della cassa espressiva. Niente cifre giganti.

Dopo vengono:
- **Opere.** Il titolo è la frase di Michela Ruffatti a Rockit (maggio 2026). Tre opere in 3:4: Davies Symphony Hall (San Francisco, Stati Uniti, cinque tastiere, 1984), Abbazia di Buckfast (testo corretto: cento file di canne, due consolle a quattro tastiere, consegnato tra il 2017 e il 2018) e Boteå (Sollefteå, Svezia, due tastiere, tiranti in fibra di carbonio). Poi la riga "oltre 500 in Italia, oltre 50 negli Stati Uniti" e il link "Tutte le realizzazioni".
- **Storia.** La foto delle maestranze in bicromia, a filo del bordo sinistro, poi La famiglia e Il restauro in tre o quattro righe ciascuna. "Maestri d'Arte e Mestiere 2020" è in inchiostro pieno.
- **Chiusura "b con foto".** La frase loro "La tradizione è forte solo se continua ad evolversi", poi il telefono grande con tel:, l'email con mailto:, l'indirizzo e "Apri la mappa". A destra le trombe en chamade fino al bordo. Il vuoto tra la frase e il telefono ora è di 64 px.
- **Piede.**
  - Logo bordeaux #6A0C10 come nella testata (PNG a 2x e 3x), con la riga "Costruttori e restauratori d'organi a canne a Padova dal 1940".
  - Newsletter con email, bottone e casella del consenso.
  - Quattro colonne: Azienda, Organi, Notizie, e Contatti con Seguici (Facebook, Instagram, YouTube, tutti esistenti).
  - In fondo © 2026 Fratelli Ruffatti, P.IVA 00207160284, Privacy, Cookie, IT EN RU.
  - A 390 le colonne vanno due per riga, in ordine.

## Caratteri e colori

- **Gambetta** (titoli, pesi 300 e 400) e **Switzer** (testo, pesi 400 e 500), tutti e due di Indian Type Foundry su Fontshare.
  - Licenza ITF Free Font License, uso commerciale gratuito. I woff2 sono serviti dalla pagina in `sito/fonts/`, scaricati dal CDN di Fontshare il 24/10/2026.
  - Perché: Rieger, il riferimento più vicino del mestiere, abbina un serif da frontespizio (PP Neue World) a un grottesco sobrio (GT America). Gambetta ha la stessa voce da lapide e sta accanto al corsivo del logo senza imitarlo.
  - Nessun corsivo in pagina. Numeri tabellari su anni, misure e telefoni; apostrofi tipografici.
- **Colori.**
  - Carta #F4F1EA (anche il fondo della foto della canna, portato a questo valore con PIL), piede #ECE7DD.
  - Inchiostro #1C1A17; grigio #5C564E solo per didascalie e note (contrasto 6,4:1 sulla carta, 5,9:1 sul piede).
  - Bordeaux del logo #6A0C10 per logo, bottone e legenda attiva.

## Interazione

Le tre legende sono bottoni veri (`aria-pressed`, `aria-controls`): toccandone una compare la sua frase e le altre si nascondono, con un cambio netto e senza animazione. È l'unico gesto della pagina. Le sole transizioni sono il cambio di colore di fondo del bottone e del tasto "Iscriviti" (0,15 s). Niente comparse allo scorrere, niente effetti al cursore. Il filtro per tastiere del prototipo B va nella pagina Realizzazioni del sito nuovo (vedi LEGGIMI).

## Foto: origine e licenza

Sono tutte della Fratelli Ruffatti, prese dalla libreria media di ruffatti.com: nessuna foto di repertorio, nessuna foto di altri costruttori, nessuna immagine generata dall'IA. I diritti delle foto delle installazioni vanno confermati (LEGGIMI).

| Foto in pagina | File originale | Misura vera | In pagina a 1440 |
|---|---|---|---|
| Canna ad ancia aperta | `2016_04_xtrompette3.jpg` | 800x603 (ruotata 595x800) | circa 670x900, ingrandita 1,1 volte; morbida a 2x |
| Registro di Tromba | `2016_04_xSfondo-trombe-2.jpg`, taglio 800x600 | 800x600 | circa 930x700, ingrandita 1,16 volte |
| Davies Symphony Hall | `2016_03_xDavies-Symphony-e1480329573331.jpg` | 800x1085 | 421 px di larghezza |
| Abbazia di Buckfast | `2018_11_756A0922-3.jpg` | 1028x758 (taglio 568x758) | 421 px; file a 800 ingrandito 1,4 volte |
| Boteå | `2018_11_P1270600-1.jpg` | 3264x2448 | 421 px |
| Maestranze, archivio | `2016_03_storia1-575.jpg` | 900x575 | circa 1040x665, ingrandita 1,16 volte |
| Trombe en chamade | `2016_04_xOrgan064modif.jpg`, taglio 600x600 | 600x600 | circa 710x640, ingrandita 1,18 volte |

Il trattamento è lo stesso per tutte: colore un po' più sobrio (saturazione 0,92) e contrasto appena più deciso. Il registro di Tromba è schiarito verso la carta, l'archivio è in bicromia inchiostro e carta. Ogni foto è esportata in due o tre larghezze con srcset. Nessun file supera 1,5 volte la misura vera; tutto quello che a 2x resta morbido è elencato nel LEGGIMI.

## Controlli fatti

- **Larghezze.** Screenshot guardati a pezzi a 1440 (intera) e 390 (intera), più le prime schermate a 320, 768, 1024, 1280 e 1920.
  - Nessuno scorrimento orizzontale; nessuna legenda fuori schermo o sopra la testata, il titolo o il testo (`finale_prova.mjs`).
  - Sotto i 1200 px il menu si apre con un vero bottone, perché le voci toccherebbero la canna. Sotto i 900 px la canna va sotto il titolo.
- **Gesto.** Provato con Tab e Invio a 1920, 1440, 1280 e 1024, e col dito a 768, 390 e 320: la legenda premuta e la frase visibile cambiano insieme.
- **Segnali da IA.** `_metodo/kit/segnali.sh` dà tutte le 18 soglie OK:
  - foto al 35,3 % della pagina; Switzer 85 % e Gambetta 15 %; nessun monospazio;
  - nessun numero grande con etichetta, nessuna etichetta maiuscola sopra i titoli, nessuna freccia; 6 filetti larghi;
  - due fasce di fondo (pagina e piede).
- **Testo.** Nessun U+2014 nella pagina, nella NOTA e nel LEGGIMI (controllato dallo script). Nessun dato fuori da `01-analisi.md` e dai testi scaricati; nessun segnaposto in pagina.
- **Divieti del committente.** Niente Inter, niente icone Lucide, niente gradienti, niente card, niente badge, niente "Tav.", niente cartellini disegnati.
