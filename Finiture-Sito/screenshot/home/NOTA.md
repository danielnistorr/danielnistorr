# Finiture, home: "Impianti di verniciatura su misura"

Pagina: `sito/index.html` (si apre con file:///, nessuna risorsa esterna). Immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, screenshot con `pro_shoot.mjs`, controlli con `pro_controlli.mjs`, esito in `_prova/pro_controlli.json`).
La versione 1 (24/10/2026, "Cosa vuoi verniciare?" con le quattro schede e il grafico delle barre) è copiata com'era, pagina, immagini, screenshot e nota, in `_prova/versione-1-originale/`.

## Livello professionale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Ordine dei criteri: uso, identità, alta gamma. Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso), struttura A1 adattata a un costruttore di impianti B2B che vende all'estero. Riferimenti guardati: le prime schermate dei 14 (`riferimenti.jpg`) e le pagine intere di Cly-Del e barth, a pezzi; il foglio della prova su Unicar, Oby e Fornasiero (`_invio/zona/home/livello-professionale.jpg`) e la nota di Unicar.

### Che cosa è cambiato rispetto alla versione 1

- **Titolo.** La versione 1 apriva con la domanda "Cosa vuoi verniciare?" e lasciava il mestiere in corpo 17. Ora l'H1 è la loro frase "Impianti di verniciatura su misura" (carosello del sito di oggi, "Tailor made finishing plants" su LinkedIn) e la domanda resta subito sotto, con le quattro risposte come link: è la scheda d'uso, par. 4 e 7.
- **Testata.** Due righe fisse: sopra, le lingue scritte per esteso (Italiano, English, Deutsch, Français, anche a 390; a 320 IT, EN, DE, FR) e lo stato dell'assistenza in ora italiana ("Assistenza aperta ora, fino alle 12:00", orari, quattro lingue, info@finiture.it con oggetto e traccia); sotto, logo, sei voci (Impianti, Lavori, Macchine, Usato, Assistenza, Azienda), il bottone bordato "Assistenza +39 049 879 2458" e il bottone pieno "Richiedi un progetto". A 390 il bottone Assistenza ha il numero su due righe, alto 48 px, e la riga degli orari sta subito sotto la testata.
- **Via il beige e il grafico delle barre.** Fondo bianco, grigio neutro #F2F2F2, antracite #1D1E20, il rosso Finiture #A51329. Il grafico "barra per barra" (scheda, par. 7: "idea del grafico, non loro") è sostituito dal caso Distner con foto e dati e da una tabella delle linee consegnate.
- **Sezioni nuove**, nell'ordine della scheda (par. 6) e della famiglia M: apertura con riga di prove; impianti per settore in quattro schede con foto e, accanto, "Vuoi solo parte di un impianto? Nessun problema!" e l'usato; impianti consegnati (Distner, poi Setz, Millet, Bruppacher, Malenfer, Arlt) e le cinque testimonianze firmate; azienda e numeri su antracite con la foto della squadra; le otto macchine della linea più Handling & Assembling; area test; assistenza sul rosso; "Richiedi un progetto" con il modulo; piede in quattro colonne.
- **Modulo** "Richiedi un progetto" con i campi del mestiere: tipo di richiesta (impianto completo, ampliamento o singola macchina, prova in area test, usato), prodotto, materiale, misure massime, pezzi al giorno, vernici, lingua della risposta, dati di contatto, disegni o foto (PDF, DWG, DXF, STEP, JPG, PNG) e messaggio. Controlla i campi obbligatori e compone un'email a info@finiture.it con oggetto e campi; i file scelti sono elencati nel testo, perché un mailto non porta allegati. Va collegato a un servizio (LEGGIMI).
- **Tolto**: la newsletter del piede (un modulo che non invia nulla; torna quando c'è il servizio), le didascalie descrittive sotto le foto, il robot coperto dal telo come foto più grande (ora l'area test è in 6 colonne su 12).

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (`_prova/pro_controlli.json`), più gli screenshot guardati a pezzi a 1440 e 390 e le pagine intere a 320, 768 e 1024.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa 99 px a 1440 e 93 a 390 (la scheda chiede lingue e orari in testata, quindi una riga in più dei 72-88 dei riferimenti). "Assistenza +39 049 879 2458" è un bottone di 48 px; a 390, scorsa metà pagina, si vede e si tocca (`elementFromPoint`). Per la famiglia M c'è anche "Richiedi un progetto". 4 link `tel:`, tutti `tel:+390498792458`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** 1440x900: H1 "Impianti di verniciatura su misura" a 64 px, "Villatora di Saonara (PD) · dal 2000", "Oltre il 90% del nostro mercato è all'estero", i quattro settori, "Richiedi un progetto" e "Prova i tuoi pezzi in area test", la foto intera, e la riga "Ultima linea inaugurata: Distner, Wiesau (Germania), 10 e 11 ottobre 2026". 390x844: lo stesso senza la foto (che apre la seconda schermata), bottone principale largo 350 px su 350.
3. **Immagine vera nell'apertura: passa, con riserva.** La porta verde laccata appesa ai ganci del loro Power&Free (7/8, foto loro): mostra la loro macchina e il lavoro, non persone. Le foto con persone (squadra, tecnico al quadro) sono più piccole o più deboli e stanno più sotto. Nel LEGGIMI la ripresa che serve.
4. **Zero repertorio: passa.** `indicativ` 0 volte; in `sito/img/` solo foto, render e logo di Finiture. Le nove foto di `assets/esterne/` non sono usate (CREDITI).
5. **Foto in serie: passa, con riserva.** Tre formati: 3:2 (apertura, Distner, area test, assistenza), 4:3 (settori e render), la striscia della squadra (2,94:1, unica misura esistente). Nessuna didascalia. Stesso trattamento leggero (contrasto 1,03) e nessuna foto ingrandita oltre la misura d'origine; ma la luce non è una sola: il servizio `*_R01` del 2016 accanto a foto di cantiere (Distner da WhatsApp 1600x1200).
6. **Palette dal marchio: passa.** `--rosso` #A51329 (ellisse del logo, robot e Power&Free), con `--rosso-scuro` per il passaggio e `--linea-rosso` per i filetti sul rosso; `--verde-aperto` solo per il punto "aperta ora"; poi antracite, bianco e grigi neutri. Nessun colore scritto fuori da `:root`. Nessun beige.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 16, 18, 22, 30, 44, 64, 96) e 8 a 390 (14, 16, 17, 20, 24, 30, 38, 56); testo corrente 18 e 17 px; nulla sotto i 14 px; H1 64/38 e H2 44/30, nella fascia M.
8. **Due famiglie al massimo: passa.** Una sola, Archivo, pesi 400 e 700; titoli e numeri a larghezza 112 %, che richiama l'espanso del loro marchio.
9. **Servizi in schede con la foto: passa.** Quattro schede dei settori in 4 colonne, foto 4:3 dei loro impianti, nome, una riga di dati, link, tutta la scheda cliccabile. Le otto macchine hanno la stessa griglia con i render CAD su fondo grigio uniforme.
10. **Almeno tre tipi di prova: passa (3 su 4).** Testimonianze firmate (5, con il nome dell'azienda: senza comune e senza stelle, perché recensioni pubbliche non ce ne sono); 6 numeri aziendali (70+, 90%, 40, 4, 51, 2000); 6 clienti con il nome. Certificazioni: nessuna nelle fonti; al loro posto due riconoscimenti con la didascalia (Exporter of the Year 2024, finalisti; partner LegnoLegno per Finestra+).
11. **Lavori con un nome: passa, con riserva.** Sei linee con cliente, luogo e 2-3 dati; Distner ha la foto larga 737 px (51 % della pagina) e la data (10 e 11 ottobre 2026). Per gli altri cinque non ci sono foto della linea attribuibili né anni nelle fonti: sono in tabella, senza anno (LEGGIMI).
12. **Ritmo a blocchi: passa.** Blocchi pieni: azienda e numeri su antracite, assistenza sul rosso, più impianti e area test su grigio e il piede antracite. Sezioni 120/120 px a 1440 e 72/72 a 390; margini 80 px a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno e bordato, raggio 2 px, 52 px (48 in testata), testo 16 px a 700; sul rosso le stesse due varianti in bianco. I bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: passa.** I campi M di A6 (azienda, email, telefono, materiale, quantità, disegno allegato, messaggio) più prodotto, misure, vernici e lingua. Indirizzo con "Apri in Google Maps" (area test, contatti, piede). Nessun iframe.
15. **Piede completo: passa.** Quattro colonne, testo di almeno 14 px: Finiture S.r.l., indirizzo con Maps, impianti e macchine, azienda (con Lavora con noi), telefono con gli orari, email, LinkedIn e YouTube con il sottotitolo, P.IVA, REA, capitale, Privacy, Cookie, lingue. Certificazioni: nessuna da mettere.

### Compiti della scheda d'uso (par. 8)

- *Serramentista estero, 1440*: lingue per esteso nella prima riga della testata (le pagine en/, de/, fr/ sono da fare); "impianti di verniciatura su misura" in H1 e "Finestre" nella prima schermata; Distner, Setz, Millet, Bruppacher e Malenfer in home con paese, barre, robot e misure in testo (un clic su "Lavori" o su "Finestre"); "Richiedi un progetto" porta al modulo con l'allegato e dice cosa mandare; area test con bottone, indirizzo e link a Maps.
- *Cliente con un impianto, 390*: "Assistenza +39 049 879 2458" in testata fissa, `tel:+390498792458`, 165 x 48 px; orari, quattro lingue e `mailto:` con oggetto "Assistenza impianto" e traccia (azienda, impianto, matricola, cosa succede) subito sotto, nella prima schermata; stato "aperta ora / chiusa, riapre..." in ora italiana, festivi nazionali e Pasquetta compresi; lingua cambiabile dalla testata senza aprire il menu.
- *Usato e singole macchine*: "Usato" nel menu e riquadro accanto ai settori (Finiture 5 e 6, "Prezzo: rivolgersi a Finiture", annunci ed email con oggetto); "Vuoi solo parte di un impianto? Nessun problema!" con sei macchine nominate e link; telefono e Maps nella sezione Contatti.

### Controlli fatti

- `pro_controlli.mjs`: nessuno scorrimento orizzontale a 320, 360, 390, 768, 1024, 1280, 1440 e 1920; testo e foto dell'apertura non si sovrappongono; nessun errore di script; nessuna ancora senza destinazione; menu a 390 aperto e richiuso dopo il tocco, "Usato" sotto la testata.
- Modulo: invio vuoto fermato con l'avviso e il fuoco su "Cosa vuoi verniciare"; "Chiedi una prova in area test" sceglie "Prova in area test"; con un PDF scelto l'email composta ha oggetto "Prova in area test: Finestre, ..." e l'elenco "Allegati da aggiungere"; letta senza aprirla.
- Orari: martedì 10:15 "Aperta ora, fino alle 12:00"; 13:10 "riapre alle 14:00"; 19:30 "riapre domani alle 8:30"; sabato "riapre lunedì"; 8 dicembre e Pasquetta "Chiusa oggi, festivo"; 24 dicembre sera "riapre lunedì".
- Collegamenti: solo `tel:+390498792458`, `mailto:info@finiture.it` (con oggetti diversi per assistenza, usato e progetto), `https://goo.gl/maps/h7pm1kBKtmKQNUDn8`.
- Screenshot in questa cartella (stato fissato a martedì 3/11/2026 alle 10:15): `home-1440-prima-schermata.jpg`, `home-1440.jpg`, `chiusura-1440.jpg` (da Contatti in giù), `home-390-prima-schermata.jpg`, `home-390.jpg`; guardati a pezzi insieme alle pagine intere a 320, 768 e 1024 (cancellate dopo). Nessun U+2014 in pagina, nei .md e negli script.

### Caratteri e licenze

- **Archivo** (Omnibus-Type), da Google Fonts, SIL Open Font License 1.1, uso commerciale libero; servito dalla pagina (`sito/fonts/archivo-latin.woff2`, `archivo-latin-ext.woff2`), licenza in `sito/fonts/OFL-Archivo.txt`.
- Foto e render: tutti di Finiture (finiture.it), uso da confermare con l'azienda. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

| Uso | File di partenza | Pixel d'origine per pixel di schermo a 1440 |
|---|---|---|
| Apertura | `EasyGalleryImages_1_17_Porte_3-taglio-dx_R01.jpg` (7/8) | 2,3 (817 px a schermo) |
| Settori | `EasyGalleryImages_1_16_Finestre_12_R01.jpg`, `easygalleryimages_1_17_porte_4_r01.jpg`, `easygalleryimages_1_18_clt_1_taglio-dx-e-no-acqua_r01.jpg`, `easygalleryimages_1_19_sedie_1_r01.jpg` | oltre 3 (302 px) |
| Distner | `EasyDNNNews_2160_IMG-20261013-WA0003.jpg` (notizia di ottobre 2026) | 2,2 (737 px) |
| Area test | `easygalleryimages_1_1092_cabina-robot.jpg` | 3,8 (630 px) |
| Assistenza | `easygalleryimages_1_1092_assistenza.jpg` | 3,8 (630 px) |
| Squadra | `Images_home-fotogallery-5.jpg` (1167x397, l'unica misura online) | 1,9 (610 px) |
| Macchine | render `EasyDNNnews_19/20/24/27/30/35/36/40_*`, fondo portato a #F2F2F2 | mai ingranditi |
| Logo | `logo-finiture-da-youtube-ritagliato.png` | PNG a 2x; nel piede le lettere schiarite, il rosso com'è |
