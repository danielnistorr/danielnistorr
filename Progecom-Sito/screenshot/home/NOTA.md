# Progecom, home finale: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh` (immagini con `finale_img.py` e `pistone_img.py`, pagina da `pagina.html`, screenshot con `shoot_finale.mjs`; prove con `prova_finale.mjs`). Base: prototipo A "Il pezzo", con tutte le indicazioni del giudice e gli innesti da B.

## Idea

Il pezzo che Progecom vende davvero, quotato come su un disegno d'officina: il loro pistone d'iniezione per pressofusione, sdraiato al centro della prima schermata, con tre richiami sulle sue parti vere e la quota del diametro tracciata accanto alla testa.

1. sull'anello posteriore: attacco allo stelo, a filetto o a baionetta;
2. sul corpo: acciaio indurito fino a 420 HB;
3. sull'anello della testa: fascia, CuCo2Be o CuNiSiCr;
4. la quota verticale accanto alla testa: Ø 50-180 mm, scritta in verticale come sulle tavole.

Sono le parole e le misure della pagina Pistoni del loro sito: con il nome di un concorrente la pagina non regge. Il resto della pagina segue il metallo "dal forno al getto", e la chiusura mostra il risultato in fonderia, il getto finito.

## Rifinitura dopo il giudice cieco (ultimo passaggio)

Il giudice cieco aveva dato K0 7, K1 6, K6 6: l'apertura ricalcava Mario Agnoletto (titolo a sinistra, pezzo a destra, richiami a pallino, bottone con "luogo, dal anno") e il protagonista era un carter di repertorio di un pressofusore. Cosa è cambiato:

- **Apertura rifatta, non ritoccata.** Protagonista il pistone di Progecom (`617993_3802f7b2`, foto dal loro sito) isolato con PIL in `_prova/script/pistone_img.py`: sagoma disegnata a mano e ripulita lungo il bordo (niente aloni chiari), dominante azzurra del telefono tolta, la fascia resta appena calda, fondo esattamente #ECEBE6 con un'ombra di contatto morbida ricavata dalla sagoma. Impaginazione nuova: pezzo al centro, quotato, titolo su una riga sotto, frase a sinistra e bottone a destra sull'ultima riga. Niente pallini numerati: un anello sottile sul punto e un filetto. Messa accanto ad Agnoletto e Hambro, la disposizione non combacia.
- **Titolo e pezzo.** Il titolo sta sotto il pezzo: fra i pixel del pistone e il titolo ci sono più di 60 px a 1280, 1366, 1440 e 1920.
- **Da 1000 a 1239 px** la stessa composizione si stringe (pezzo misurato sulla larghezza), senza griglie spezzate; sotto 1000 diventa una colonna: titolo, pistone con la sola quota, frase, bottone.
- **Telefono.** Prima schermata pulita: niente pallini e niente legenda, resta la quota del diametro. Le parti del pistone sono scritte nella tappa Iniezione.
- **Schede.** Sotto 900 px il segno della tappa attiva sta sotto il suo nome (filetto inferiore), con 6 px fra le righe; a 360 px e meno le schede vanno su due colonne. Sopra 900 px i sei pannelli stanno nella stessa cella della griglia: la pagina resta alta 6346 px con qualunque tappa aperta.
- **Degasaggio.** La foto (709 px) occupa sei colonne a filo del bordo, alla sua misura: niente più vuoto di 370 px.
- **Iniezione.** Al posto del pistone da telefono ritagliato ci sono i loro pistoni e la fascia in lega di rame con il pistone in acciaio (`617993_02e7ea19`): carta riportata al colore della pagina, rame lasciato caldo. È l'unico colore caldo della pagina oltre alla bocca di forno e al bottone.
- **Chiusura.** Frase loro nuova, "Ordini evasi in tempi molto brevi, in tutta Italia" (dalla frase sul servizio). Foto: il carter isolato dell'apertura precedente, chiaro e nitido, con la didascalia "Il risultato in fonderia: un carter pressofuso in alluminio (foto indicativa)". Il mucchio scuro di getti di Escalante non c'è più.
- **Testi.** "Dalla fase iniziale al post vendita" resta una volta sola (Assistenza); tolta dall'apertura, dalla chiusura e dal piede.
- **Piede.** La colonna Contatti non ripete la chiusura: telefono, una email e "Come arrivare a Mestrino". La riga su chi sono dice cosa vendono.
- **Area delle foto.** Per tenere la soglia dei segnali (almeno 35 %) i lingotti STEMIN passano a 16:9 e la bocca di forno a 720 px di altezza; lo spazio fra le sezioni scende da 168 a 144 px.

## Prime due schermate

**Apertura, 1440x900.**
- In alto la testata. Sopra il pezzo due richiami (corpo, fascia), a sinistra il terzo (attacco), a destra la quota verticale del diametro.
- Il pistone è largo 710 px e alto 492, centrato; il riquadro si calcola su larghezza e altezza della finestra, così titolo, frase e bottone restano dentro la prima schermata da 1280x800 a 1920x1080 e a 1366x768.
- Sotto: "Metalli non ferrosi" (la testata del loro sito) su una riga in Archivo largo, poi la frase "Impianti e prodotti per fonderie di alluminio, zinco e rame, dal crogiolo al pistone d'iniezione. A Mestrino, dal 1990." e a destra il solo bottone "Chiama +39 348 604 6875".

**Apertura, 390x844.** Titolo su due righe, il pistone a tutta colonna con la quota, la frase, il bottone a tutta larghezza. Tutto sta nei 844 px.

**Seconda schermata: "Dal forno al getto".**
- Apre con la frase "Dal 1990 Progecom porta in fonderia quello che il metallo liquido tocca: il crogiolo, il rotore, la rete, la siviera, il pistone."
- Seguono sei tappe (Fusione, Degasaggio, Filtrazione, Trasporto, Iniezione, Controllo) che ordinano le 16 famiglie del menu, con link alle pagine.

**Il resto della pagina, in ordine:**
- **Assistenza.** Bocca di forno a filo del bordo sinistro, larga il 56 % e alta al massimo 720 px, un po' desaturata. A destra "Anche nel week-end" con i tre paragrafi.
- **Rappresentanza STEMIN.** Foto dei lingotti a tutta larghezza (16:9, al massimo 800 px) e una frase sotto.
- **Usato.** Tre prezzi pubblicati in tabella.
- **Chiusura.** Frase loro, telefono grande, due email, indirizzo e "Apri la mappa", il carter a destra fino al bordo.
- **Piede.**

Altezza a 1440: 6346 px, piede compreso. A 390: 6438 px.

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

I colori forti della pagina sono due e vengono dalle foto: il rosso della bocca di forno, desaturato al 38 %, e il rame dei pistoni nella tappa Iniezione. Nel pistone dell'apertura la fascia resta appena calda e richiama il bronzo del bottone.

## Interazione

Un solo gesto: le sei tappe sono schede vere (tablist, tab, tabpanel).
- Si usano con il clic o il dito; da tastiera con le frecce, Home e Fine, e Tab porta al pannello (provato con `_prova/script/prova_finale.mjs`, anche con il tocco a 390 e 768).
- Il cambio del pannello è netto. L'unica transizione, di 150 ms, è sul filetto e sul colore della tappa toccata.
- Senza JavaScript tutti e sei i pannelli restano visibili, uno sotto l'altro.
- Sopra 900 px l'altezza della pagina non cambia da una tappa all'altra; sotto 900 i pannelli tornano uno sotto l'altro e la pagina cambia altezza (fino a 400 px a 390), perché una cella comune lascerebbe un buco di 400 px sotto le tappe corte. Sopra le schede non si sposta nulla.

I richiami e la quota dell'apertura sono statici. Non c'è nessuna animazione allo scorrere e nessun effetto che segue il cursore. Il menu del telefono è un vero bottone con aria-expanded e contiene anche "English".

## Foto, origine e licenza

| In pagina | File di partenza | Origine e licenza |
|---|---|---|
| Apertura, pistone d'iniezione | `assets/originali/617993_3802f7b2a7844e47b99550c37a67ed5f.jpg` | sito Progecom, pagina Pistoni; isolato con `pistone_img.py`. Foto da telefono, da rifare |
| Fusione, forno a crogiolo | `assets/originali/617993_63c4b918289a42529969a3c5ba29ea21.jpg` | sito Progecom, pagina usato |
| Degasaggio | `assets/originali/617993_22fb7a2c5ee746ef9a898a8e4df1e6f5.jpg` (709 px) | sito Progecom |
| Filtrazione, rete | `assets/originali/617993_3b181aec7c864a23b6b424c14cc92736.jpg` | sito Progecom (forse del produttore) |
| Trasporto, siviera e lingottiere | `assets/esterne/unsplash-grieveson-hJqaSkr796w.jpg` | Joseph Grieveson, Unsplash License |
| Iniezione, pistoni e fascia in rame, pistone in acciaio | `assets/originali/617993_02e7ea19ab62426cac9487da06fa965d.jpg` | sito Progecom, pagina Pistoni |
| Controllo, valigetta | `assets/originali/4a6a7c_da1722afe4b04452a44cc09864bc39e1.jpg` | sito Progecom |
| Assistenza, bocca di forno | `assets/originali/4a6a7c_804c276fec54406abe77f3f84fdfb915.jpg` | sito Progecom, pagina usato |
| Rappresentanza, lingotti | `assets/originali/4a6a7c_dc8cdae251a3400dac3b94beb0c3dc7e.jpg` | sito Progecom, pagina Rappresentanze; foto di STEMIN S.p.A. |
| Chiusura, carter pressofuso | `assets/esterne/unsplash-diecastingmould-D60xwIqu-jA.jpg` | Diecasting Mould, Unsplash, Unsplash License. Segnaposto con "foto indicativa" |
| Logo | `assets/originali/logo-simbolo-738.png` | sito Progecom, ricolorato nell'inchiostro, WebP 80, 120 e 180 px |

Come sono state scelte e trattate:
- Non è stata scaricata nessuna foto nuova e nessuna immagine è generata.
- Nessuna foto di repertorio compare in altre home della campagna (CREDITI controllati: Diecasting Mould è solo tra le scartate di Marin Assemblaggi).
- La foto di chiusura è diversa da quella subito sopra. Le due foto di repertorio rimaste (Grieveson, Diecasting Mould) non compaiono in altre home della campagna; Escalante non è più usata.
- Tutte le foto hanno lo stesso trattamento (quasi bianco e nero con un filo di caldo, il rame lasciato caldo) e sono esportate in due o tre larghezze con srcset. I due pezzi isolati (pistone e carter) hanno il fondo esattamente del colore della pagina.
- Le didascalie descrivono il pezzo; la fonte sta qui e in `assets/CREDITI.md`.

## Piede

- **Marchio e presentazione.** Simbolo del sito (PNG ricolorato, WebP a 2x e 3x) con la scritta PROGECOM in Archivo largo (il logotipo vero è un serif nero: da confermare con il titolare), e una riga su chi sono: "Crogioli, degasaggio, filtrazione, pistoni d'iniezione e strumenti di controllo per fonderie di metalli non ferrosi. Mestrino, Padova, dal 1990."
- **Colonne.** Azienda, Prodotti (sette famiglie vere e "Tutti i prodotti"), Contatti ridotta a telefono, una email e "Come arrivare a Mestrino", per non ripetere la chiusura parola per parola.
- **Riga legale.** Ragione sociale, indirizzo, P.IVA 05018460286, Privacy, Cookie, English. Il REA non c'è finché non è verificato.
- **Seguici: no.** Non ci sono social aziendali; l'unico canale è lo YouTube personale di Mauro Poggese.
- **Newsletter: no.** News è "coming soon", non ci sono cataloghi propri né fiere e i clienti sono solo fonderie. L'unico contenuto che cambia è l'usato, servito meglio dalla pagina Usato e dal telefono.
- **Comportamento.** A 390 le colonne si impilano in ordine; tra 601 e 900 px vanno su tre colonne.
- **Link.** Nessun href="#": i link vanno alle sezioni della home o ai percorsi del sito nuovo, elencati nel LEGGIMI.

## Controlli

**Screenshot.** In questa cartella:
- `home-1440.jpg` (6346 px) e `home-1440-prima-schermata.jpg`;
- `home-390.jpg` (6438 px) e `home-390-prima-schermata.jpg`;
- `chiusura-1440.jpg`.

Guardati a pezzi, insieme a 320, 768, 1024, 1280, 1366x768 e 1920 e alle tappe 2 e 5 aperte (in `_prova/tmp-finale/prove/`), e alla tappa 5 aperta a 390. I PNG grandi sono stati cancellati (screenshot del giudice in `_prova/cieco/`, restano i pezzi JPEG) o convertiti in JPEG (prototipi in `_prova/home/`).

**Esito delle prove** (`prova_finale.mjs` e `shoot_finale.mjs`).
- scrollWidth uguale a innerWidth a 320, 360, 390, 414, 600, 768, 900, 1000, 1024, 1180, 1239, 1240, 1280, 1366, 1440, 1600, 1920 e 2560.
- Nessuna sovrapposizione fra testi, verificata dallo script.
- Schede: frecce, Home, Fine e Tab da tastiera; tocco a 390 e 768; senza JavaScript sei pannelli uno sotto l'altro. A 1440 la pagina è alta 6346 px con ognuna delle sei tappe aperte.
- Collegamenti: 4 `tel:+393486046875`, 3 `mailto:` (info e commerciale), 2 link a Google Maps per Via Udine 24, 35035 Mestrino; nessun `href="#"`.
- A 320 il telefono della testata è nascosto, perché si sovrapponeva al marchio; resta il bottone grande dell'apertura.

**Segnali da IA** (`segnali.sh` a 1440): 0 soglie bloccanti su 10.
- Foto 35,6 %, Archivo 100 %, mono 0 %, 22 filetti, 0 frecce, 0 etichette maiuscole, nessuna parola da brochure (tolta "soluzioni" dalla chiusura).
- Una sola riga "da guardare": le tappe numerate 01-06. Si tengono perché sono l'ordine reale del metallo in fonderia.

**Testo e codice.**
- Nessun U+2014 nella pagina, negli script e nei .md.
- Nessun gradiente, ombra di riquadro, icona Lucide, badge o dissolvenza.
- Gli hover cambiano colore o spessore della sottolineatura, mai l'opacità.

**Respinto, con il motivo.**
- Altezza costante delle schede anche sotto 900 px: la cella comune lascerebbe fino a 400 px vuoti sotto le tappe corte; sopra le schede non si sposta nulla.
- Sostituire la foto del degasaggio con il rotore in grafite: il file del sito è largo 386 px, non regge.
