# 247LAB, home finale: "We don't fear the dark"

Pagina: `sito/index.html`. Si rifà tutto (immagini, pagina, screenshot) con `bash _prova/script/build_finale.sh`.

## Idea

Una lampada accesa pende sopra la parola "dark". Il motto vero dell'azienda, "We don't fear the dark", è scritto in tondo su una riga sola, e la sospensione BOATY S in ottone scende dall'alto proprio sopra l'ultima parola: la luce cade sul buio. È un'immagine che sa fare solo chi produce luce, e con il nome di un concorrente non regge, perché il motto e la lampada sono loro.

La pagina è chiara. Il nero caldo #12100D sta solo dove una lampada è accesa: l'apertura, alta 900 px a 1440. Da lì in giù il fondo è la carta #F4F1EA. Restano scure solo due foto, perché è la foto a chiederlo: MINA sul muro nero dello shop e Roberto al banco.

Altezza a 1440: 6094 px, piede compreso.

## Cosa è cambiato nella rifinitura (20/10/2026)

Dal giudizio cieco (60/80, K0 7 e K1 7):
1. **Carta subito dopo l'apertura.** Collezioni, MINA, progetti, su misura, chiusura e piede stanno sulla carta. A 1440 il fondo #12100D finisce a 900 px (prima a circa 3000).
2. **La luce sfiora "dark".** La lampada è scesa di 0,37em (bottom da `calc(100% - .78em)` a `calc(100% - 1.15em)`), circa 50 px a 1440: il bordo acceso del paralume sta a circa 15 px sopra le ascendenti di "d" e "k", senza toccarle. Il legame resta in em, quindi vale a ogni larghezza. A 768 il padding sopra il titolo è ridotto nella stessa misura, così il fusto esce ancora dal bordo alto (la lampada parte da -28 px).
3. **Tre collezioni senza le tre schede.** Una sola foto grande, F346 (due fari in ottone su un'asta, Casa P, Verona 2022) dall'originale 4573x3049, in 4:5 a filo del bordo sinistro. Accanto c'è l'indice delle tre collezioni con i filetti: RB, Twentyfour7 e G-label, ognuna con due righe di testo, il link e il catalogo 2026 in PDF. Il render G-6, la foto torbida di 1111 e BOWLY sono tolti. Niente più didascalia tra foto e titolo.
4. **MINA sulla carta, e le tre finiture si distinguono.** Le tre foto dello shop non erano scattate dallo stesso punto. Ho misurato su ognuna il bordo alto del paralume e il bordo basso della base, le ho riportate alla stessa altezza della lampada (1324 px) e allo stesso riquadro 4:5 attorno all'asse. Il riquadro resta 597x746 px in tutte e tre (provato). Le ombre sono aperte con una curva (gamma 0,62): il muro diventa antracite e il cemento grigio chiaro, e ottone, brunito marrone (bronzo) e brunito antracite (acciaio bluastro) si leggono.
5. **Newsletter onesta.** Senza servizio collegato risponde "L'iscrizione apre a breve: intanto scrivici a info@247lab.it", con il mailto.
6. **Collegamenti veri.**
   - Cataloghi (testata, apertura, piede) va alla pagina Cataloghi di oggi.
   - Le collezioni vanno alle loro pagine di oggi, G-label al suo PDF; i tre PDF sono in `sito/cataloghi/`.
   - Chi siamo, Progetti e Shop vanno alle pagine vere.
   - Privacy, Cookie ed EN vanno a `/privacy`, `/cookie` e `/en` (pagine del sito nuovo, elencate nel LEGGIMI).
   - Niente più ancore rotte né doppioni nel piede.
7. **Su misura a 1024.** La frase dell'offerta non sparisce più tra 901 e 1180: titolo a 40 px, testo a `min(520px, 52%)`.
8. **Progetti senza vuoto.** La foto di Casa G (5:4, a filo del bordo sinistro) sta accanto all'indice dei 13 committenti con città e anno, uno per riga tra filetti. Foto e indice sono alti uguali, circa 655 px.
9. **Menu del telefono a tutto schermo.** Pannello fisso sul nero da sotto la testata al fondo dello schermo, testata nera e pagina ferma sotto. Nessun pezzo del titolo o del fusto si vede (screenshot a 390 e 768).
10. **Menu completo fino a 901 px.** Tra 901 e 1180 le sette voci stanno su una riga (gap 18 px, 15 px), senza il telefono in testata; sotto i 900 c'è il bottone Menu.
11. **CIUCCIO**: in didascalia ci sono i dati del catalogo RB 2026 (IP44, 3000K). La scheda del sito dice IP54: è nel LEGGIMI.
12. **Foto più nitide.**
    - WebP a qualità 85 (prima 82).
    - BOATY S e F018 sono rifatte dagli originali Wix (4000x6000 e 4608x3072), con le nuove larghezze apertura-boaty-1780 e persone-f018-2880.
    - MINA arriva fino a 1300 px. Il precaricamento delle altre finiture usa la misura che la pagina mostra davvero.
13. **768 più corta.** Persone e chiusura hanno un taglio orizzontale tra 601 e 900 px (3:2 con il viso a destra, 5:4 senza la fascia di legno). La pagina a 768 passa da 8636 a 7227 px.

## Prime due schermate

**1440x900** (`home-1440-prima-schermata.jpg`)
- Testata trasparente: logo SVG vero, sette voci (Collezioni, Progetti, Su misura, Cataloghi, Shop, Chi siamo, Contatti), telefono, EN.
- Il titolo "We don't fear the dark" è in Jost 300 a 136 px, su una riga, con spaziatura -0,035em.
- BOATY S è appesa con il centro sopra "dark" in ogni larghezza: il fusto esce dal bordo alto, il paralume acceso sfiora le ascendenti della parola.
- Sotto il titolo:
  - "La bellezza della luce nella sua forma più pura" e una riga su chi sono;
  - il solo bottone ottone "Le tre collezioni" e accanto il link "Cataloghi 2026";
  - in basso a destra la didascalia con i dati veri: 1xGU10 LED 8 W, IP20.

**390x844** (`home-390-prima-schermata.jpg`)
- La testata ha il logo a 108 px e il bottone Menu con tre lineette, senza riquadro.
- La sospensione è centrata e il fusto esce dal bordo alto dietro la testata.
- Sotto vengono il titolo su due righe, il sottotitolo, la riga su chi sono, il bottone e il link Cataloghi. Il bottone finisce a 689 px, dentro gli 844; sotto si vede già l'inizio della carta con la foto F346.

## Il resto della pagina (a 1440)

1. **Tre collezioni** (carta, 1147 px): F346 a sinistra fino al bordo, 708x885; a destra il titolo, la riga su TWENTYFOUR7 e l'indice RB, Twentyfour7, G-label.
2. **MINA** (carta, 914 px): a sinistra titolo, testo, il selettore, prezzo e codice, il bottone dello shop; a destra la foto fino al bordo.
3. **Progetti** (carta, 1064 px): "41 progetti dal 2006 al 2025", gli studi, Casa G a sinistra fino al bordo e l'indice dei committenti a destra.
4. **Su misura** (720 px): la foto F018 a tutta larghezza, il titolo "...ma siamo sempre aperti a nuove idee" sul muro nero.
5. **Chiusura** (carta, 700 px): a sinistra "Sempre a tua disposizione, 24/7", il telefono 049 644600 a 48 px con tel:, email con mailto:, WhatsApp, indirizzo con il link alla mappa, la didascalia di CIUCCIO; a destra la foto fino al bordo. Niente orari, perché non sono pubblicati.
6. **Piede** (carta, filetto ottone sopra, 649 px):
   - logo SVG e una riga su chi sono;
   - newsletter con campo, bottone e consenso;
   - quattro colonne: Collezioni, Azienda, Contatti, Seguici (Instagram, Facebook, LinkedIn, Pinterest, Archiproducts, come parole);
   - la riga "© 2026 247LAB di Marco Bertelli, ditta individuale", P.IVA, Privacy, Cookie, English.

   A 390 le colonne vanno due per riga, in ordine.

Sul telefono le foto a filo del bordo diventano a tutta larghezza: F346 e la foto di MINA vengono prima del testo, Casa G prima dell'indice.

## Caratteri e colori

- **Jost** 300 e 400 per titoli, menu, bottoni, prezzo e telefono.
- **Hanken Grotesk** 400 e 500 per testo, didascalie e piede.
- Cifre tabellari su misure, prezzi, codici e anni.
- Perché Jost: è un geometrico su base Futura, come il logo 247LAB, che è un geometrico sottile. Regge perché il titolo è davvero grande e leggero, come Tek.Lam "Scintilla e spessore". Per la carta chiara con un oggetto in ottone il riferimento è Atelier Areti; per l'apertura nera con un solo quadro, Apparatus.
- **Licenze**: tutte e due sono SIL Open Font License 1.1, da Google Fonts. I file woff2 sono serviti dalla pagina in `sito/fonts/`.
- **Colori**, con il contrasto calcolato:
  - su carta #F4F1EA: inchiostro #171614 16,0:1, seppia #5E574D 6,3:1, ottone scuro #6E5119 6,5:1 per passaggio del mouse e fuoco; bottone ottone #C9A35A con testo #12100D 8,0:1;
  - su nero #12100D (apertura, menu, testo su F018): luce #EDE7DC 15,4:1, cenere #A39B8E 6,9:1, ottone #C9A35A 8,0:1;
  - #B8924A solo per il filetto sopra il piede.

  Tutte le coppie passano AA. Niente gradienti, ombre, vetro o icone.

## Interazione

Un solo gesto: il selettore di finitura di MINA.
- Tre radio veri: Ottone, Brunito marrone, Brunito antracite.
- La scelta cambia la foto (stesso riquadro, al pixel), il prezzo (135 o 155 €, letto con aria-live), il codice (247M.001, .002, .003) e il link alla scheda dello shop.
- Funziona con clic, dito e frecce, con il fuoco visibile in ottone scuro.

Il menu del telefono è un vero bottone con aria-expanded: apre un pannello a tutto schermo, si chiude con Esc e il fuoco torna sul bottone. Le uniche transizioni sono cambi di colore di 150 ms su ciò che si tocca. Niente comparse allo scorrere, niente effetti legati al cursore, nessuna dissolvenza.

## Foto: origine e licenza

Sono tutte foto dell'azienda, dal loro sito Wix. L'elenco con i file di origine è in `assets/CREDITI.md`, sezione "Home finale":
- BOATY S (F024);
- Casa P (F346, foto Alessandro Cusano);
- MINA nelle tre finiture (F044-F046);
- Roberto al banco (F018);
- Casa G (F288, foto Alessandro Cusano);
- CIUCCIO (F066).

Non ci sono foto di repertorio né immagini generate, e nessuna è usata in un'altra home della campagna. Le immagini sono lavorate con `finale_img.py`:
- un solo tono caldo leggero sulle foto chiare;
- neri di BOATY S e del muro di F018 portati a #12100D; su F018 una maschera morbida tiene aperte le ombre del viso;
- MINA riportata a scala e riquadro comuni, con le ombre aperte;
- export WebP qualità 85 con srcset (1,97 MB in tutto per 41 file).

La licenza va chiarita: servono il permesso e il credito di Cusano per F288 e F346, e l'autore delle foto di prodotto e del ritratto (vedi LEGGIMI).

## Controlli (20/10/2026, dopo la rifinitura)

- **Segnali da IA** (`segnali.sh`): 0 soglie bloccanti su 10 e 0 da guardare su 8.
  - Foto al 41,9 %.
  - 4 fasce a tutta larghezza: apertura nera, carta, la foto F018, carta.
  - 26 filetti e 0 frecce.
  - 5 misure di H2.
  - Hanken 79,1 % e Jost 20,9 %.
  - Nessuna numerazione 01, 02, 03 e nessuna etichetta sopra i titoli.
- **Scorrimento orizzontale**: scrollWidth uguale a innerWidth a 320, 360, 390, 414, 600, 601, 768, 900, 901, 1024, 1100, 1180, 1181, 1280, 1440, 1600, 1920 e 2560 (`finale_controlli.mjs`).
- **Testata**: tra 901 e 1180 le sette voci stanno su una riga.
- **Su misura tra 901 e 1180**: la frase dell'offerta si vede; il testo finisce a 299 px dall'alto della foto, che è alta da 451 a 590 px.
- **Gesto MINA**:
  - con il solo Tab il fuoco arriva al gruppo di radio (19 tasti) e il contorno si vede;
  - le frecce passano Ottone, Brunito marrone, Brunito antracite, Ottone, con prezzo, codice, foto e link giusti;
  - il tocco a 390 su Brunito marrone dà 155 €, 247M.002 e la foto giusta;
  - il riquadro della foto è 597x746 px per tutte e tre.
- **Menu del telefono** a 390 e 768: aperto, è un pannello fisso a tutto schermo e la pagina sotto non scorre; Esc lo chiude e il fuoco torna sul bottone.
- **Collegamenti**:
  - nessuna ancora rotta;
  - tel:+39049644600 in testata, menu, chiusura e piede;
  - mailto:info@247lab.it;
  - 2 link alla mappa;
  - i link esterni sono le pagine vere di 247lab.it, WhatsApp e i social;
  - i soli href="#" sono i due loghi, che riportano in cima.
- **Newsletter**: con email e consenso risponde "L'iscrizione apre a breve", con il mailto.
- **Screenshot guardati a pezzi**: 1440, 390, 320, 768, 1024 e 1920, più il menu aperto a 390 e 768 e MINA in antracite.
- **U+2014**: 0 nella pagina, negli script, in NOTA, LEGGIMI e CREDITI.
- **Lunghezze delle pagine**: 6094 px a 1440, 5582 a 1024, 7227 a 768, 8213 a 390, 6787 a 1920.
