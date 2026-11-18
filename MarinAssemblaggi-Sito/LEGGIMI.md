# Marin Assemblaggi: proposta di nuova home

È una proposta non richiesta di nuova homepage (solo la home) per Marin Assemblaggi srl, Saonara (PD). Non è pubblicata: l'azienda non è stata contattata e nessun modulo è stato inviato.

## Dove sono le cose

- `sito/index.html`: la home finale, statica (si apre con file:///). Immagini in `sito/img/` (solo quelle usate, WebP in più larghezze), caratteri in `sito/fonts/` con la licenza.
- `screenshot/home/`:
  - `home-1440.jpg` (intera), `home-1440-prima-schermata.jpg`, `home-390.jpg` (intera), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`;
  - `NOTA.md` con l'idea, le schermate, i caratteri, i colori, l'interazione, le foto e i controlli.
- `_prova/script/build_finale.sh`: rifà immagini, pagina e screenshot. Con l'argomento `controlli` scrive anche 320, 768, 1024, 1920 e lo stato "Montato" in `_prova/controlli/`. I sorgenti sono:
  - `index.sorgente.html` (la pagina);
  - `finale_img.py` (le foto);
  - `scatti_finale.mjs` (gli screenshot);
  - `controlli_finali.mjs` (scorrimento da 320 a 2560, nitidezza delle foto, tastiera, tocco, collegamenti, U+2014);
  - `misura_nome.mjs` (la spaziatura di "ASSEMBLAGGI" sotto "MARIN").
- `01-analisi.md`: fatti con le fonti. `_prova/home/a` e `_prova/home/b` sono i due prototipi; la finale parte da A.

## Prima della messa online (bloccante)

- **La foto d'apertura nuova, a 6000 px.** Oggi `8407` è di 1600x600: in pagina sta a 880 px, 1x, senza ingrandimenti, quindi sugli schermi retina è morbida e l'area foto della home resta al 28,8 % (la soglia della guida è 35 %). Servono due scatti identici a camera ferma dello stesso set, "Sciolto" e "Montato" (dettagli sotto, "Foto da rifare", punto 1). Con quelli l'apertura può crescere oltre i 1000 px e l'interruttore mostrerà due foto vere invece dello schiarimento del gruppo non scelto.

## Dati da confermare con Marin (non sono in pagina, o ci sono solo nella forma sicura)

1. **Logo.** Esiste un logo vettoriale (carta intestata, insegna, furgoni)? Oggi testata e piede usano la ragione sociale composta su due righe in Zalando Sans largo: "MARIN" in 500 e, sotto, "ASSEMBLAGGI" in 400 spaziato alla stessa larghezza. Non è un logo inventato e non ha pittogrammi. Se il logo esiste va messo al suo posto, in SVG se fedele, altrimenti PNG o WebP a 2x.
2. **Anni di attività.** Il sito dice "da oltre venti anni", ma la srl è del 20/12/2016 (companyreports.it).
   - In pagina c'è solo "Dal 2016 la ditta è Marin Assemblaggi srl".
   - Se Marin conferma l'anno di inizio della ditta precedente, la riga diventa "Da oltre venti anni nell'assemblaggio per conto terzi; dal 2016 è Marin Assemblaggi srl", meglio ancora con l'anno vero.
3. **Unità della coppia degli avvitatori**: "da 3 a 60 N" e "da 3 a 15 N". Sono N·m o N·cm? Finché non lo dicono, in pagina c'è solo "con controllo di coppia", senza numeri.
4. **Nomi dei pezzi nelle didascalie e nei testi alternativi**: "Sciolto: corpo, bussola e sfera", "Montato: la sfera è in sede"; negli alt corpo esagonale e bussola in ottone, sfera d'acciaio, raccordo; sotto il banco "Bussole, sfere e raccordi in ottone". Sono letti dalle foto, quindi Marin deve dare i nomi giusti e confermare i materiali.
5. **La frase della chiusura**: "Precisione e puntualità: i nostri committenti ve lo confermeranno". Unisce due periodi del loro "Chi siamo" ("esprime il meglio nella precisione e puntualità" e "I nostri Committenti ve lo confermeranno"); nel testo originale "Committenti" ha la maiuscola, in pagina è minuscolo. Va fatta approvare così.
6. **Pezzi dei clienti.** Le foto mostrano pezzi dei committenti. Dal banco di `8447` è rimasto solo il gruppo di bussole, sfere e raccordi in ottone, senza scritte leggibili: le impugnature "250 bar", "Made in EEC" e il pomello "250" sono fuori. Va confermato comunque che quei pezzi si possano mostrare.
7. **Diritti delle foto** "KeKKo-clicK" (EXIF di 8407, 8447, slide2, slide3) per il sito nuovo.
8. **Sede.** Saonara o "Villatora di Saonara" (la mappa di Google dice Villatora). "Noventa Padovana" nel titolo del sito di oggi va tolto: era una sede precedente?
9. **Fax.** È ancora attivo? È lo stesso numero del telefono; in pagina c'è solo il telefono.
10. **Visura.** REA PD 437367 (da un aggregatore), capitale sociale e PEC: entrano nella riga legale del piede solo dopo la visura.
11. **Settori, clienti tipo, certificazioni, lotti minimi e tempi di consegna.** Sul sito non c'è nessun numero; con un dato vero la home guadagna una prova.
12. **La marcatrice a punti** (quella con il display in `MAC_4`): marca e modello.

## Pagine del sito nuovo (i link del piede)

Esistono solo come destinazione: vanno fatte con il sito completo.

- `lavorazioni/assemblaggio.html`
- `lavorazioni/avvitatura.html` (avvitatura a coppia controllata)
- `lavorazioni/cianfrinatura.html` (cianfrinatura e coniatura)
- `lavorazioni/marcatura.html` (marcatura laser e a punti)
- `lavorazioni/confezionamento.html` (confezionamento ed etichette)
- `lavorazioni/attrezzature.html` (attrezzature di montaggio)
- `chi-siamo.html`, `reparto.html` (il reparto e le macchine)
- `privacy.html`, `cookie.html`

"Dove siamo" porta alla chiusura della home (`#contatti`).

- **Newsletter**: non c'è e non serve. Marin è un terzista B2B senza prodotti propri, cataloghi, fiere o clienti privati.
- **"Seguici"**: non c'è, perché non esistono social attivi (Facebook è un link vuoto, Google+ è chiuso).

## Foto da rifare dal vero (mezza giornata con lo stesso fotografo)

1. **Apertura, due scatti identici a camera ferma.**
   - Il set di `8407` (stessi cinque pezzi, piano a specchio, luce morbida da studio) a 6000 px di lato lungo.
   - Primo scatto, "Sciolto": tutti i pezzi separati. Secondo scatto, "Montato": gli stessi pezzi montati, senza muovere camera, luce e piano.
   - Così l'interruttore scambierà due foto vere: oggi scambia due versioni della stessa foto, con il gruppo non scelto schiarito del 70 %. Va lasciata aria sopra e ai lati: in pagina la foto sta sotto il titolo, a destra.
   - Fondo bianco caldo e uniforme, senza l'alone aggiunto ai lati; il riflesso corto basta.
2. **Tre coppie "sciolto e montato"** su bianco, con la stessa luce: tappi con o-ring, cartucce, raccordi. Servono per le pagine delle lavorazioni.
3. **Il banco**: il gruppo di bussole, sfere e raccordi di `8447` fotografato da solo su bianco, a 6000 px, senza gli altri pezzi attorno (oggi sono tolti con una sagoma a mano e le ombre del piano sono ripulite).
4. **Il reparto, per i passi 1 e 2**: mani all'avvitatore a coppia controllata e alla pressa su tavola rotante, su un fondo pulito.
   - Inquadrature larghe e orizzontali, luce del reparto più una luce morbida di riempimento.
   - Niente cartelli e tende verdi nell'inquadratura.
5. **Marcatura laser al lavoro**: la marcatrice Sisma EASY che incide un pezzo, in luce bassa.
6. **Confezionamento**: un lotto contato, termosaldato ed etichettato sul banco, con l'etichetta leggibile solo se è di Marin.

## Licenze

- **Foto in pagina**: solo foto di Marin dal loro sito (`assets/originali/`, copyright "KeKKo-clicK" nell'EXIF; diritti da confermare, punto 5). Nessuna foto di repertorio e nessuna immagine generata. I segnaposto Unsplash e Pexels di `assets/esterne/` non sono usati nella finale.
- **Carattere**: Zalando Sans di Google Fonts, SIL Open Font License 1.1, nome riservato "Zalando".
  - I file woff2 sono quelli serviti da Google Fonts (latin e latin-ext), copiati in `sito/fonts/` senza modificarli e senza rinominarli, con `OFL.txt`.
  - Se un giorno si fa un sottoinsieme o una modifica, il carattere va rinominato (nome riservato).
- **Loghi**: nessun logo usato, perché Marin non ne ha uno sul sito. La scritta della testata di oggi (Open Sans) è conservata solo come documento in `assets/originali/logo-scritta-testata-2x.png`.
