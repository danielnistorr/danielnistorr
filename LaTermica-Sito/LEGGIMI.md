# La Termica, proposta di nuova home

Proposta non richiesta di una nuova homepage per La Termica snc di Camporese Mario (Mestrino, PD). Nessun contatto con l'azienda, niente pubblicato, nessun modulo inviato.

## Dove sono le cose

- `sito/index.html`: la home finale, statica. Accanto ci sono `sito/img/` (solo le immagini usate, WebP in più larghezze, logo PNG a 2x) e `sito/fonts/` (Brygada 1918 e Host Grotesk, woff2).
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` e `NOTA.md` (idea, schermate, caratteri, colori, interazione, foto, controlli).
- `_prova/script/build_finale.sh`: rifà immagini, pagina, controlli, screenshot e segnali. Gli script sono `build_img.py` (immagini), `larghezze.mjs`, `sezioni.mjs`, `controlli.mjs` e `screenshot_finali.mjs`.
- `01-analisi.md`: fatti con le fonti. `_prova/giudizio.json`: il giudizio sui prototipi. `_prova/home/a` e `_prova/home/b`: i prototipi.
- `assets/CREDITI.md`: origine e licenza di ogni immagine.

## Dati da confermare con l'azienda

- **Forma societaria**: il sito e l'informativa del 10/2023 dicono snc, atoka.io dice srl con la stessa P.IVA. In pagina c'è "La Termica snc di Camporese Mario". Se è srl servono ragione sociale esatta, REA, capitale sociale e PEC, da aggiungere alla riga legale del piede.
- **1978**: in pagina c'è "La ditta nasce nel 1978 nelle coibentazioni termiche di tubazioni", come sul loro sito. Da sapere:
  - se il 1978 va bene come data da mostrare;
  - da quando fanno canne fumarie, perché "da oltre vent'anni" è un testo del 2014 ed è stato tolto;
  - se la ditta era già a Mestrino.
- **I due figli**: in pagina c'è "Mario Camporese, con i suoi due figli". Va bene così? I nomi e i ruoli vanno aggiunti?
- **Fax 049 9007617**: è ancora attivo? Oggi non è in pagina.
- **Email**: info@latermicacamini.com resta quella giusta anche con il dominio latermica.it?
- **Orari** del magazzino e dello showroom: non sono sul sito e non sono in pagina. Se ci sono, vanno nella chiusura.
- **Marchi**: CLAM, Eva Calor e Calux per stufe e caminetti sono ancora quelli trattati?
- **Pronto Lamiera e abbattitori di fuliggine**: sono servizi ancora attivi? Il "98%" del loro sito non è usato.
- **Abilitazioni**: oltre a "autorizzati dalla camera di commercio", quali hanno di preciso? Si possono citare con il numero?
- **Legenda della foto d'apertura**: oggi dice solo "Terminale in rame". Il titolare può confermare una seconda legenda sul gomito, "Curva a 90°, saldata su misura"?
- **Righe dei materiali**: le righe 316L, 304, Rame e Ovali sono riscritte dai loro testi. Vanno controllate con il titolare, in particolare "Rame: tubi 7/10 mm e serie a doppia parete".
- **Luoghi e permessi**: dove sono i cantieri delle foto (il centro storico del rame è Padova?) e se le foto si possono pubblicare con le case riconoscibili.
- **Promemoria pulizia** nel piede: lo vogliono? È una mail all'anno, prima dell'inverno. Se non lo vogliono gestire, si toglie il blocco e il piede resta con logo, quattro colonne e riga legale.
- Dipendenti (4) e ricavi (749.000 €) vengono da atoka.io: non sono in pagina e non vanno messi senza conferma.

## Il promemoria (newsletter minima)

Il modulo nel piede (campo email, bottone "Iscrivimi", casella del consenso con il link all'informativa) oggi non invia niente: `action="#"` e `onsubmit="return false"`. Prima di andare in linea va collegato a un servizio di invio (per esempio Brevo o MailerLite, con server in UE) con doppia conferma dell'iscrizione. Va anche aggiornata l'informativa privacy, che oggi non parla di newsletter. Il link "informativa privacy" punta a `/privacy/`.

## Pagine che il sito nuovo dovrà avere (link del piede e del menu)

- Servizi:
  - `/servizi/canne-fumarie/`
  - `/servizi/video-ispezioni/`
  - `/servizi/spazzacamino/`
  - `/servizi/messa-a-norma/`
  - `/servizi/intubamento-e-risanamento/`
  - `/servizi/stufe-e-caminetti/`
  - `/servizi/abbattitori/`
- Prodotti:
  - `/prodotti/inox-doppia-parete/`
  - `/prodotti/inox-monoparete/`
  - `/prodotti/rame/`
  - `/prodotti/pellet-e-legna/`
  - `/prodotti/comignoli-e-accessori/`
- Su misura:
  - `/su-misura/armadi-copri-caldaia/`
  - `/su-misura/armadi-e-portine-gas/`
  - `/su-misura/cassette-crash/`
  - `/su-misura/lavorazioni-su-disegno/`
  - `/su-misura/pronto-lamiera/`
- Azienda:
  - `/chi-siamo/`
  - `/lavori/`
  - `/showroom-e-magazzino/`
  - "Contatti e dove siamo", che oggi porta alla chiusura della home (`#contatti`)
- Note legali:
  - `/privacy/` (l'informativa PDF del 10/2023 esiste già)
  - `/cookie/`
- Il menu in testata porta alle sezioni della home: Servizi, Lavori, Prodotti e su misura, Chi siamo, Dove siamo.

## Foto da rifare dal vero

Le foto in pagina sono tutte loro, ma vengono da telefoni e compatte del 2011-2014. Basta mezza giornata di scatti su due o tre cantieri recenti, con una reflex o una mirrorless e il cavalletto, in giornata di cielo coperto chiaro (luce morbida, nessuna ombra dura, cielo uniforme facile da portare al colore carta).

1. **Priorità uno: l'apertura.** Tre canne in rame su un tetto in coppi, con i terminali in fila.
   - Teleobiettivo (70-200 mm) da un tetto vicino o da un cestello, all'altezza dei terminali, così le verticali restano dritte.
   - Cielo coperto, inquadratura orizzontale larga e piena risoluzione.
   - Dietro le canne solo cielo, il meno possibile di case e comignoli.
   - Lo stesso cantiere anche in verticale, per il telefono.
2. **Un terminale inox** contro il cielo, sempre con il teleobiettivo, per la parte "inox" del titolo.
3. **Il camino autoportante** (traliccio con tre canne), visto dal basso e di fianco, con le verticali corrette.
4. **Un armadio inox su misura** su fondo chiaro, in laboratorio. Luce diffusa da un lato e un pannello bianco dall'altro, per avere riflessi lunghi e puliti sull'acciaio; di fronte e di tre quarti.
5. **La video ispezione**: un fotogramma nitido della telecamera dentro una canna inox nuova, senza scritte a schermo.
6. **Il magazzino e lo showroom** ordinati, con luce naturale o lampade calde, per la pagina "Showroom e magazzino".
7. **Mario Camporese e i figli** al lavoro su un tetto, se vogliono comparire, con i dispositivi di sicurezza in vista.

## Licenze

- **Caratteri**: Brygada 1918 e Host Grotesk da Google Fonts, licenza SIL Open Font License 1.1 (uso commerciale libero, anche serviti dal proprio sito). I file sono in `sito/fonts/`.
- **Foto**: tutte di La Termica, dal loro sito. Le foto di repertorio in `assets/esterne/` (Unsplash e Pexels, licenze in `assets/CREDITI.md`) non sono usate nella home finale.

## Logo

Il logo in pagina è un PNG trasparente a 400 e 600 px, ricavato dal JPEG a 3000x938 del loro sito (`assets/originali/logo-completo-3000x938.jpg`). Il sito non ha un SVG e non è stato ridisegnato: ricostruire le forme e la scritta condensata in modo fedele richiede il file originale. Al grafico o all'azienda va chiesto il logo vettoriale (AI, EPS, PDF o SVG).
