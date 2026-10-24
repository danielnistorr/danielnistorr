# Progecom, home finale: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh` (immagini con `finale_img.py`, pagina da `pagina.html`, screenshot con `shoot_finale.mjs`). Base: prototipo A "Il pezzo", con tutte le indicazioni del giudice e gli innesti da B.

## Idea

Un solo getto di alluminio pressofuso, da solo sul fondo della pagina, con quattro richiami a filo sottile che legano una fornitura di Progecom a una zona vera del pezzo:

1. sulla parete piena: la lega, Al-Si in lingotti da 6-8 kg;
2. sulla parete sottile della canna: pareti senza porosità, degasaggio con rotore Ø 250 mm fino a 2000 cicli;
3. su una nervatura sottile: niente inclusioni, rete con maglia da 1,0 a 2,5 mm;
4. sulla flangia spessa: pressione d'iniezione, pistoni Ø 50-180 mm fino a 420 HB.

Il messaggio è che Progecom non fa il getto, ma porta in fonderia tutto quello che serve per farlo bene. Il resto della pagina segue il metallo "dal forno al getto". Con il nome di un concorrente la pagina non regge, perché le misure e le sigle sono le loro.

## Prime due schermate

**Apertura, 1440x900.** Il K0 del prototipo era 7, quindi l'apertura è stata ripensata, non ritoccata.
- La foto a tutta pagina con il muro e il piano è sparita. Il carter è stato isolato con PIL: il fondo della foto è stato portato al colore esatto della pagina (#ECEBE6) dividendo per un modello liscio del fondo; la staffa dietro e il terzo pezzo sono stati cancellati; restano l'ombra di contatto e i riflessi veri.
- Il pezzo è circa il 10 % più grande che nel prototipo, ancorato in basso a destra a 64 px dal piede della schermata, e non è più tagliato dal bordo.
- A sinistra: titolo "Metalli non ferrosi" (la testata del loro sito) in Archivo largo a 112 px, la frase su cosa fanno, un solo bottone "Chiama +39 348 604 6875" e "Mestrino (PD), dal 1990".
- I quattro richiami sono attaccati al pezzo con filetti da 1 px, come in Mario Agnoletto. La legenda lontana in alto a destra, il secondo carter fantasma e "Tav. 1" sono stati tolti. In basso c'è la didascalia "Carter pressofuso in alluminio (foto indicativa)".
- Il layout regge da 1240 a 1920 px perché il pezzo è un'immagine a sé, dimensionata sulla larghezza e sull'altezza della finestra.
- Tra 901 e 1239 px l'apertura passa a due colonne: testo a sinistra, pezzo con i pallini numerati e la legenda a destra.

**Apertura, 390x844.** Dall'alto: titolo, frase, il pezzo a tutta larghezza con quattro pallini numerati, la legenda breve in due colonne sotto il pezzo, il bottone telefono a tutta larghezza e "Mestrino, Padova. Dal 1990". Tutto sta nei 844 px.

**Seconda schermata: "Dal forno al getto".**
- Apre con la frase di B: "Dal 1990 Progecom porta in fonderia quello che il metallo liquido tocca: il crogiolo, il rotore, la rete, la siviera, il pistone."
- Seguono sei tappe (Fusione, Degasaggio, Filtrazione, Trasporto, Iniezione, Controllo) che ordinano le 16 famiglie del menu, con link alle pagine.
- Le foto delle tappe sono tutte in 4:3, a filo del bordo sinistro, con lo stesso trattamento quasi bianco e nero caldo dell'apertura.
- Nella tappa Iniezione c'è il pistone di Progecom in piedi su fondo carta. La foto del degasaggio non supera i 520 px.
- Nel pannello Fusione, accanto alle leghe di alluminio: "Al-Si per ruote, volanti, forcelle moto e altri particolari di sicurezza".

**Il resto della pagina, in ordine:**
- **Assistenza.** Bocca di forno a filo del bordo sinistro, larga il 56 % e alta al massimo 600 px, un po' desaturata. A destra "Anche nel week-end" con i tre paragrafi. La fascia rossa a tutta larghezza non c'è più.
- **Rappresentanza STEMIN.** Foto dei lingotti a tutta larghezza (12:5, al massimo 680 px di altezza) e una frase sotto.
- **Usato.** Tre prezzi pubblicati in tabella.
- **Chiusura.** Frase loro, telefono grande, due email, indirizzo e "Apri la mappa", foto dei getti grezzi a filo del bordo destro.
- **Piede.**

Altezza a 1440: 6222 px, piede compreso. A 390: 6806 px.

## Caratteri e colori

**Carattere: Archivo**, Google Fonts, SIL Open Font License 1.1 (Omnibus-Type).
- È servito dalla pagina: `sito/fonts/archivo-var-latin.woff2`, file variabile con peso 100-900 e larghezza 62-125 %.
- Titoli in 400 a larghezza 110-118 % con spaziatura da -0,025 a -0,035 em. Testo in 400 a 100 %. Cifre tabellari per misure, prezzi e telefono.
- Un solo carattere, niente monospazio e niente serif.
- Il grottesco largo ricorda le targhe delle macchine e dei forni. È vicino alla calma di Bühler (un getto in alluminio protagonista) e ai grigi di Speira e Hydro, ma è meno anonimo. Nessun'altra home della campagna usa Archivo.

**Colori**

| Uso | Colore | Contrasto |
|---|---|---|
| Fondo alluminio caldo | #ECEBE6 | |
| Piede | #E2E0D9 | |
| Inchiostro | #15171A | 15,0:1 sul fondo |
| Grigio del testo | #55595D | 5,9:1 sul fondo, 5,4:1 sul piede |
| Bronzo, solo su bottone, numero della tappa attiva e anello di fuoco | #7A5424 | 5,6:1 sul fondo; testo chiaro sul bottone 6,2:1 |

L'unico colore forte della pagina è il rosso della bocca di forno, desaturato al 38 %.

## Interazione

Un solo gesto: le sei tappe sono schede vere (tablist, tab, tabpanel).
- Si usano con il clic o il dito; da tastiera con le frecce, Home e Fine (provato con `_prova/script/prova_tastiera.mjs`).
- Il cambio del pannello è netto. L'unica transizione, di 150 ms, è sul filetto e sul colore della tappa toccata.
- Senza JavaScript tutti e sei i pannelli restano visibili.

I richiami dell'apertura sono statici. Non c'è nessuna animazione allo scorrere e nessun effetto che segue il cursore. Il menu del telefono è un vero bottone con aria-expanded e contiene anche "English".

## Foto, origine e licenza

| In pagina | File di partenza | Origine e licenza |
|---|---|---|
| Apertura, carter (desktop e telefono) | `assets/esterne/unsplash-diecastingmould-D60xwIqu-jA.jpg` | Diecasting Mould, Unsplash, Unsplash License. Segnaposto |
| Fusione, forno a crogiolo | `assets/originali/617993_63c4b918289a42529969a3c5ba29ea21.jpg` | sito Progecom, pagina usato |
| Degasaggio | `assets/originali/617993_22fb7a2c5ee746ef9a898a8e4df1e6f5.jpg` (709 px) | sito Progecom |
| Filtrazione, rete | `assets/originali/617993_3b181aec7c864a23b6b424c14cc92736.jpg` | sito Progecom (forse del produttore) |
| Trasporto, siviera e lingottiere | `assets/esterne/unsplash-grieveson-hJqaSkr796w.jpg` | Joseph Grieveson, Unsplash License |
| Iniezione, pistone | `assets/originali/617993_dc2abcaa9fa04adba3876134f985d72d.jpg` | sito Progecom (ritaglio in piedi come nel prototipo B) |
| Controllo, valigetta | `assets/originali/4a6a7c_da1722afe4b04452a44cc09864bc39e1.jpg` | sito Progecom |
| Assistenza, bocca di forno | `assets/originali/4a6a7c_804c276fec54406abe77f3f84fdfb915.jpg` | sito Progecom, pagina usato |
| Rappresentanza, lingotti | `assets/originali/4a6a7c_dc8cdae251a3400dac3b94beb0c3dc7e.jpg` | sito Progecom, pagina Rappresentanze; foto di STEMIN S.p.A. |
| Chiusura, getti grezzi | `assets/esterne/unsplash-escalante-oFe9f0VHEEc.jpg` | Salvador Escalante, Unsplash License |
| Logo | `assets/originali/logo-simbolo-738.png` | sito Progecom, ricolorato nell'inchiostro, WebP 80, 120 e 180 px |

Come sono state scelte e trattate:
- Non è stata scaricata nessuna foto nuova e nessuna immagine è generata.
- Nessuna foto di repertorio compare in altre home della campagna (CREDITI controllati: Diecasting Mould è solo tra le scartate di Marin Assemblaggi).
- La foto di chiusura è diversa da quella subito sopra.
- Tutte le foto hanno lo stesso trattamento (quasi bianco e nero con un filo di caldo) e sono esportate in due o tre larghezze con srcset.
- Le didascalie descrivono il pezzo; la fonte sta qui e in `assets/CREDITI.md`.

## Piede

- **Marchio e presentazione.** Simbolo del sito (PNG ricolorato, WebP a 2x e 3x) con la scritta PROGECOM in Archivo largo, e una riga su chi sono.
- **Colonne.** Azienda, Prodotti (sette famiglie vere e "Tutti i prodotti"), Contatti con telefono, due email, indirizzo e "Apri la mappa".
- **Riga legale.** Ragione sociale, indirizzo, P.IVA 05018460286, Privacy, Cookie, English. Il REA non c'è finché non è verificato.
- **Seguici: no.** Non ci sono social aziendali; l'unico canale è lo YouTube personale di Mauro Poggese.
- **Newsletter: no.** News è "coming soon", non ci sono cataloghi propri né fiere e i clienti sono solo fonderie. L'unico contenuto che cambia è l'usato, servito meglio dalla pagina Usato e dal telefono.
- **Comportamento.** A 390 le colonne si impilano in ordine; tra 601 e 900 px vanno su tre colonne.
- **Link.** Nessun href="#": i link vanno alle sezioni della home o ai percorsi del sito nuovo, elencati nel LEGGIMI.

## Controlli

**Screenshot.** In questa cartella:
- `home-1440.jpg` (6222 px) e `home-1440-prima-schermata.jpg`;
- `home-390.jpg` (6806 px) e `home-390-prima-schermata.jpg`;
- `chiusura-1440.jpg`.

Guardati a pezzi, insieme a 320, 768, 1024, 1280 e 1920 e alle tappe 2 e 5 aperte.

**Esito delle prove.**
- Nessuno scorrimento orizzontale a nessuna larghezza.
- Nessuna sovrapposizione fra testi, verificata dallo script.
- A 320 il telefono della testata è nascosto, perché si sovrapponeva al marchio; resta il bottone grande dell'apertura.

**Segnali da IA** (`segnali.sh` a 1440): 0 soglie bloccanti su 10.
- Foto 35,7 %, Archivo 100 %, mono 0 %, 22 filetti, 0 frecce, 0 etichette maiuscole.
- Una sola riga "da guardare": le tappe numerate 01-06. Si tengono perché sono l'ordine reale del metallo in fonderia.

**Testo e codice.**
- Nessun U+2014 nella pagina, negli script e nei .md.
- Nessun gradiente, ombra di riquadro, icona Lucide, badge o dissolvenza.
- Gli hover cambiano colore o spessore della sottolineatura, mai l'opacità.
