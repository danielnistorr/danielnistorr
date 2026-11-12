# Home finale di Tecnoplastic, "Il cuore della pompa"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `sh _prova/script/build_finale.sh` (immagini con `finale_img.py`, pagina da `index-sorgente.html`, screenshot con `scatti_finale.mjs`). Base: prototipo A, con le correzioni del giudice e gli innesti da B.

Altezze: 5929 px a 1440 (piede compreso), 6975 px a 390.

## Idea

Il Taurus, il loro galleggiante brevettato che "rimane sott'acqua", appeso al suo cavo sotto il pelo dell'acqua. La prima schermata è divisa in due da una sola linea da bordo a bordo: sopra, sulla carta, il titolo, la riga su chi sono e i recapiti; sotto, una fascia d'acqua piatta a tutta larghezza (#E9F0F0, lo stesso colore a sinistra e a destra) dove sta solo il pezzo, con una legenda; il cavo sale e buca la linea. Si capisce in due secondi che è un galleggiante che lavora sotto la superficie, cosa che un galleggiante tradizionale non fa: con il pezzo di un concorrente la pagina non regge. Poi si guarda dentro (il sezionato con le nove parti), le sei versioni, i filtri, il modo di lavorare, la chiusura con la sede.

## Le prime due schermate

1. 1440x900: testata (logo, Galleggianti, Filtri, Azienda, Download, Contatti, IT/EN, telefono). "Il cuore della pompa" su una riga a 112 px (dalla loro frase "il galleggiante sia il cuore di ogni pompa"); sotto il titolo, nella stessa fascia asciutta, la riga su chi sono ("progettati e stampati a Saonara dal 1994"), "Chiama 049 879 0775" e l'email, tutti sopra la linea (y 271-323). La linea dell'acqua a y 368, 1 px in #12303A al 42 %. Sotto la linea, fino al fondo della prima schermata, la fascia d'acqua piatta: il fondo #EFF2F0 dietro il pezzo e un velo azzurro al 6 % sopra il pezzo (insieme #E9F0F0, misurato uguale a x 100 e x 1300), così il corpo sembra davvero sott'acqua e il cavo sopra la linea resta asciutto. Il Taurus a destra: corpo 347x488 px (immagine 388x704, servita da un file nativo 510 px, mai ingrandita), il più grande della pagina. Una sola legenda: "Contrappeso integrato: resta sott'acqua". Nessun testo sotto la linea oltre la legenda.
2. 390x844: titolo su due righe, riga su chi sono, "Chiama 049 879 0775" (y 304-356), email, poi la linea d'acqua e la fascia piatta con il Taurus (224 px di larghezza, corpo 200x282) e la sua legenda a sinistra. A 320 la legenda si toglie e il Taurus va al centro.
3. 1024x768: titolo a 84 px, riga e recapiti sotto il titolo e sopra la linea (y 422), Taurus a destra con la legenda a sinistra; telefono in testata fino a 901 px.

Poi: "Un galleggiante dentro un altro galleggiante": titolo a sinistra e testo a destra in alto, sotto il sezionato (alto 600 px, largo 288) accanto all'elenco delle 9 parti della scheda (la spiegazione solo sulla voce accesa, i dati in una riga sotto), così a 1440x900 foto, numeri e tutte e 9 le voci stanno insieme sullo schermo; "Sei Taurus" (6 colonne a 1440, 3 colonne con immagini da 100 px a 390; ordine Taurus, Drink, EX, Fep, SiHF, PUR, così i due gialli non stanno vicini, e il PUR dice "Liquidi abrasivi, cavo PUR"); "Filtri Dolphin e Whale"; "Dallo stampo al collaudo, nello stesso stabilimento" con le cinque fasi in una riga di parole (Progettazione, Stampi, Stampaggio, Assemblaggio, Collaudo, dalla frase di about-it; elenco verticale a 390), clienti e distributori, le prove sui galleggianti e le certificazioni in una riga piccola; chiusura; piede. Stacchi tra le sezioni tutti uguali: 160 px a 1440, 128 a 1024, 112 a 768, 96 a 390.

## Chiusura e piede

- Chiusura: la loro frase "Sembriamo un laboratorio artigianale, ma abbiamo la capacità produttiva di una grande azienda" in Red Hat Display a 68 px; sotto, "testo a sinistra e foto a destra fino al bordo": i recapiti in colonna (telefono +39 049 879 0775 a 40 px con tel:; sales@ con mailto:, indirizzo e "Apri la mappa"; "Orari di ufficio e magazzino") e a destra la facciata con la fontana e l'insegna fino al bordo della finestra, alta 373 px e mostrata a 1:1 (892x373 a 1440, tagliata ai lati dal riquadro, mai ingrandita fino a 1600 px di riquadro). Fino a 900 px la foto va sotto i recapiti in un taglio 780x373 sull'insegna e la fontana: a 390 è alta 186 px, cioè 2x nativo.
- Piede su #ECEAE4: logo (marchio vettoriale della brochure più "tecnoplastic" in Comfortaa resa in tracciati), riga su chi sono, "Brochure 2024 (PDF)", "Seguici" con YouTube a parte (tra 561 e 1199 px logo e riga a sinistra, brochure e Seguici a destra nella stessa riga, allineati alle colonne sotto); colonne Galleggianti, Filtri, Azienda (con "Distributori: Italia, Cipro, Regno Unito, Stati Uniti" e "Negozio online (Water Fitters)"), Contatti; riga legale con ragione sociale, indirizzo, P.IVA 00046450284, Privacy, Cookie, English. A 390 le colonne sono una fisarmonica con veri bottoni (aria-expanded). Testi secondari #5B605F su #ECEAE4: contrasto 5,4:1 (AA).
- Newsletter: non messa. Non hanno notizie né fiere da comunicare, i clienti sono costruttori e distributori che ricevono la brochure annuale, i privati comprano da Water Fitters che ha già la sua. Al suo posto la brochure scaricabile.

## Caratteri e colori

- Red Hat Display (titoli, 400) e Red Hat Text (testi, 400 e 500), superfamiglia dello stesso disegnatore, cifre tabellari vere per misure, orari e telefono. Google Fonts, SIL Open Font License 1.1: serviti dalla pagina in `sito/fonts/` (file variabili, sottoinsieme latin) con `OFL-redhatdisplay.txt` e `OFL-redhattext.txt`. Motivo: grottesco geometrico con la "o" tonda, parente dell'ITC Avant Garde di VOLA (riferimento 2) e del Comfortaa del loro logo, che rima con la sfera del Taurus; non è nelle liste b della guida; nessuna altra home della campagna lo usa.
- Carta #F6F5F1, carta 2 #ECEAE4 (fascia delle versioni e piede), inchiostro #17191B, pietra #5B605F, filetti #D6D3CB, linea dell'acqua #12303A al 42 %, acqua #E9F0F0 piatta (fondo #EFF2F0 più velo azzurro al 6 % sopra il pezzo, nessun gradiente, nessuna trama), rosso del marchio #D22631 solo nel logo e nel numero acceso del sezionato. Il colore pieno lo danno i galleggianti. Riferimenti: CEA (un solo pezzo nitido su grigio chiaro), VOLA (frase grande e pulita), Fantini (il rosso del marchio come unico accento).

## Interazione

Una sola, sul Taurus sezionato: toccando, passando col mouse o con Tab un numero sulla foto si accende la voce dell'elenco, e viceversa (frecce su e giù nell'elenco). Solo cambio di colore in 0,12 s. A 390 l'elenco mostra le prime 3 parti e un vero bottone "Tutte le 9 parti"; se si tocca sulla foto un numero oltre il 3, l'elenco si apre da solo. Nessuna animazione allo scorrere, nessun effetto sul cursore, nessun hover che sbiadisce. Il resto: menu a 900 px e fisarmonica del piede a 560 px, con bottoni veri.

## Foto, origine e licenza

Tutte di Tecnoplastic, da `assets/originali/` (sito e brochure 2024 dell'azienda): `taurus-2.png` (apertura: a misura nativa, ruotato con la punta in alto con una rotazione sovracampionata che torna a 1x, bande della tavolozza a 256 colori attenuate con un filtro che rispetta i bordi, maschera di contrasto decisa solo sul rilievo col logo, cavo sfumato in alto; file da 510, 400 e 300 px, mai ingrandito), le cinque versioni del Taurus, `taurus-sezionato.png` (numeri azzurri tolti con ritocco locale, poi stessa pulizia a misura nativa, 449 e 320 px), `dolphin-10-triple.png`, `img-2601-2.jpg` (facciata, maschera di contrasto leggera, mai ingrandita: 1600x373 intera e taglio 780x373), `logo-marchio-tp.svg`. Nessuna foto di repertorio, nessuna immagine generata: i segnaposto di `assets/esterne/` restano inutilizzati. WebP con trasparenza e JPEG in 2-3 larghezze con srcset.

## Controlli

- Screenshot guardati a pezzi a 1440 e 390 (interi), più 320, 768, 1024 e 1920 (interi, in `_prova/controlli`, PNG cancellati dopo averli guardati) e gli stati a 390 (elenco aperto, piede aperto, menu).
- `_prova/script/larghezze.mjs`: scrollWidth uguale a innerWidth a 28 larghezze da 320 a 2560; testata senza sbordare a 901-1200 con il telefono visibile; nessun errore in console aperta come file:// (tolti i due preload dei caratteri).
- `_prova/script/prova_gesto.mjs`: a 1440x900, con il sezionato al centro, la figura va da y 150 a 750 e l'elenco da 197 a 602; clic sul 9 della foto accende la voce 9, visibile senza scorrere; mouse, Tab e frecce su e giù funzionano; a 390 con il tocco l'8 apre l'elenco da solo, il bottone "Tutte le 9 parti" si apre e si chiude, la fisarmonica del piede e il menu hanno aria-expanded. Collegamenti: tel:+390498790775, mailto:sales@tecnoplastic.com, Google Maps su via Calabria 3/5 (9 in tutto, tutti corretti).
- Immagini a 1440 1x: Taurus 388x704 da un file di 400 px (corpo nativo 456x642), sezionato 288x599 da 320 px, facciata 892x373 a 1:1. A 390 2x: Taurus e sezionato dal file nativo più grande.
- Nessun U+2014 in pagina, script e note.
- `segnali.sh`: tutto OK tranne l'area foto, 19 % contro 35 % (bloccante) e le fasce di fondo, 6 contro 4 (da guardare: la fascia d'acqua dell'apertura è l'idea della pagina). L'area foto scende dal 21,9 % perché il sezionato e la facciata non sono più ingranditi: senza foto di repertorio non si raggiunge, si risolve con il servizio fotografico del LEGGIMI (still life in alta risoluzione e due ore in reparto). Nessun gradiente in pagina.
- Dati: ogni dato in pagina viene da 01-analisi.md o dalle schede in `_prova/crawl` (0,95-1,05 kg/dm³ e "rimane sott'acqua" dalla scheda Taurus, IP68, 20 m, 20° ±5°, 10(8) A 250 Vac, 1,5 HP, UL, 5 bar, 11 bar, ACS, 50.000 cicli, ICIM dal 2004, Campioni dell'Export 2023, distributori, orari, P.IVA; "cavo PUR" dalla scheda Taurus-PUR, modello cavo "PUR 4G0.75").

## Ultima rifinitura (giudice: 7, 7, 8, 8, 9, 7, 6, 7)

- Apertura: l'acqua è una fascia piatta a tutta larghezza dalla linea al fondo della prima schermata (prima era un gradiente orizzontale che lasciava asciutta la metà sinistra); riga su chi sono, "Chiama" ed email salgono sopra la linea; resta una sola legenda; l'ombra del pezzo non esce più dalla fascia.
- Taurus d'apertura rifatto dal file originale a misura nativa, senza l'ingrandimento 2x: più nitido, rilievo del logo leggibile, corpo da 310x430 a 347x488 a 1440; il sezionato scende da 420x874 a 288x600, quindi il pezzo d'apertura è il più grande della pagina.
- Sezionato: titolo e testo sopra, foto ed elenco affiancati sotto; a 1440x900 si vedono insieme foto, numeri e tutte e 9 le voci.
- Chiusura: recapiti a sinistra e facciata a destra fino al bordo, alta 373 px a 1:1 (prima una striscia 1440x336 ridotta); a 390 un taglio servito a 2x nativo.
- Piede tra 561 e 1199 px: brochure e Seguici nella riga del logo, niente vuoto a destra.
- Testata: telefono visibile fino a 901 px. Refuso: "del Sole 24 Ore e di Statista". Preload dei caratteri tolti (errori CORS su file://). Sei Taurus riordinati, PUR con "cavo PUR".
- Prerequisito per la consegna: lo still life del Taurus a 4000 px (LEGGIMI). La pagina regge con i file di oggi solo perché il pezzo non supera la misura nativa.
