# Finiture, home: "Impianti di verniciatura su misura"

Pagina: `sito/index.html` (si apre con file:///, nessuna risorsa esterna). Immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, screenshot con `pro_shoot.mjs`, controlli con `pro_controlli.mjs`, esito in `_prova/pro_controlli.json`).
La versione 1 (24/10/2026, "Cosa vuoi verniciare?" con le quattro schede e il grafico delle barre) è copiata com'era, pagina, immagini, screenshot e nota, in `_prova/versione-1-originale/`.

## Livello professionale (3/11/2026), con il ritocco finale

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso), struttura A1 adattata a un costruttore di impianti B2B che vende all'estero. Riferimenti guardati: le prime schermate dei 14 (`riferimenti.jpg`) e le pagine intere di Cly-Del e barth, a pezzi.

### Il ritocco finale, dopo il controllore (voto 6) e le prove dei due clienti tipo

- **Apertura con un gesto di scala.** L'H1 "Impianti di verniciatura su misura" passa da 64 a 96 px e prende tutta la griglia: la prima riga corre sopra la foto, la seconda ("su misura") le sta accanto. La foto parte dalla seconda riga del titolo e va fino al bordo destro (817 x 545 px a 1440).
- **Foto d'apertura con persone e marchio.** Al posto della porta verde (un primo piano del prodotto, letto come dittico) c'è il tecnico Finiture al quadro della cella robot, con il logo Finiture sul quadro e il robot RAS dietro (`easygalleryimages_1_1092_assistenza.jpg`, 2400 x 1600). La porta verde resta, nella scheda Porte. A 390 la foto apre la pagina subito sotto la testata.
- **Testata meno "portale".** La prima riga ha solo le lingue e lo stato dell'assistenza, che è un link al blocco Assistenza ("Assistenza aperta ora, fino alle 12:00 · orari e lingue"); via orari ed email da quella riga. A 390 la riga ha IT EN DE FR e lo stato corto ("Aperta, fino alle 12:00"), a 320 "Aperta ora": lo stato ora resta sempre visibile, perché la testata è fissa. Orari, lingue e "Scrivi all'assistenza" (con oggetto e traccia) stanno in una fascia antracite sotto la foto, nella prima schermata; il link ha un'area di tocco di 44 px. L'etichetta "Assistenza" del bottone di testata a 390 è a 16 px.
- **Lead con le misure e i paesi**, come chiedeva il serramentista: "per pezzi fino a 6000 × 3500 mm. Lavorano in Germania, Svizzera e Francia, e fino in Canada, India e Australia". Il 90% non è più nel lead: resta nella riga delle prove e nei numeri.
- **Tre lavori completi.** Distner, Setz Fensterbau e Malenfer hanno ognuno foto larga 737 px (51% a 1440), luogo, anno e 3-5 dati, alternati foto a sinistra e a destra. Le foto Setz e Malenfer sono quelle delle loro notizie sul sito. Millet, Bruppacher e Arlt restano in tabella, con la colonna "Quando" (notizia o anno dell'impianto, mai inventato).
- **Testimonianze.** La frase di Wagner in grande (44 px) con il filetto rosso, le altre quattro in elenco a destra, e sotto la fonte: "Dalla home di finiture.it, tradotte in italiano".
- **Azienda.** La foto della squadra è a tutta larghezza (1280 px, dall'originale di 1167: 1,1 volte), i due paragrafi sotto, i numeri ridotti a cinque con etichette di 2-4 parole (70+, 90%, 40, 51, 4; tolto "2000", già nell'occhiello). I due riconoscimenti sono una fascia con titolo grande.
- **Area test** in 7 colonne più 5, centrate. **Assistenza** sul rosso con la foto del tecnico che spiega il Supervisor ai clienti (`easygalleryimages_1_1092_dsc06151.jpg`).
- **Una serie di foto.** In `pro_img.py` tutte le foto hanno lo stesso trattamento: bianco portato a neutro sui grigi della scena, stessi punti di nero e di bianco, curva a S leggera, saturazione -12%. Via la dominante verde-gialla dell'area test e dell'assistenza e il freddo della foto Distner.
- **Modulo onesto sugli allegati.** "Il programma di posta non li allega da solo: li elenchiamo nell'email e tu li aggiungi prima di inviare"; accanto al bottone, info@finiture.it per chi non ha un programma di posta.
- **Atterraggio dalle ancore.** Dal menu si arriva all'etichetta della sezione, 40 px sotto la testata, senza la fascia vuota di 120 px.
- **Piede** con i riconoscimenti. **Script** con l'elenco `CHIUSURE` per le ferie aziendali (vuoto, da chiedere).
- **Dati verificati.** I dati tecnici che il controllore non trovava nelle fonti (Distner dal 1964, Superjet e Superjet Plus, LDP, chiarificatore, cambio colore automatico, 100 barre da 3500 mm, Villers-Farlay, 6 assi, 4 colori, DRY-A, Pro Dry, aspirazione a flusso orizzontale e verticale) sono stati riletti sul sito e citati con URL e data in `01-analisi.md`, sez. 2.

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (`_prova/pro_controlli.json`), più gli screenshot guardati a pezzi a 1440 e 390 e le pagine intere a 320, 768 e 1024.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa di 99 px a 1440 e 93 a 390. "Assistenza +39 049 879 2458" è un bottone di 48 px; a 390, scorsa metà pagina, si vede e si tocca (`elementFromPoint`). C'è anche "Richiedi un progetto". 4 link `tel:`, tutti `tel:+390498792458`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** A 1440x900: H1 a 96 px, "Villatora di Saonara (PD) · dal 2000", "pezzi fino a 6000 × 3500 mm" e i paesi, i quattro settori, i due bottoni, la foto intera e la prima riga di "Ultima linea inaugurata: Distner". A 390x844: foto, fascia dell'assistenza, occhiello, H1 a 38 px, lead e "Richiedi un progetto" largo 350 px su 350.
3. **Immagine vera nell'apertura: passa.** Persona di Finiture, marchio sul quadro, la loro cella robot: è "chi costruisce e segue l'impianto", non il prodotto del cliente. A 390 è la prima cosa sotto la testata.
4. **Zero repertorio: passa.** `indicativ` 0 volte; in `sito/img/` solo foto, render e logo di Finiture. Le nove foto di `assets/esterne/` non sono usate.
5. **Foto in serie: passa, con riserva.** Tre formati: 3:2 (apertura, tre lavori, area test, assistenza), 4:3 (settori e render), la striscia della squadra (2,94:1, unica misura esistente). Nessuna didascalia. Stesso trattamento colore per tutte; resta che sono scatti di epoche diverse (servizio `*_R01` del 2016, foto da telefono dei cantieri): la serie vera chiede il servizio fotografico del LEGGIMI.
6. **Palette dal marchio: passa.** `--rosso` #A51329 (ellisse del logo, robot e Power&Free) con le sue due declinazioni, `--verde-aperto` solo per il punto "aperta ora", poi antracite, bianco e grigi neutri. Nessun beige.
7. **Scala tipografica corta: passa.** 7 misure a 1440 (14, 16, 18, 22, 30, 44, 96) e 8 a 390 (14, 16, 17, 20, 24, 30, 38, 56); testo corrente 18 e 17 px; nulla sotto i 14 px; H1 96 a 1440 (il gesto di scala, come il logotipo di barth) e 38 a 390.
8. **Due famiglie al massimo: passa.** Una sola, Archivo, pesi 400 e 700; titoli e numeri a larghezza 112%.
9. **Servizi in schede con la foto: passa.** Quattro schede dei settori in 4 colonne, foto 4:3, nome, una riga di dati, link, tutta la scheda cliccabile. Le otto macchine nella stessa griglia, render su fondo grigio uniforme.
10. **Almeno tre tipi di prova: passa con riserva (3 su 4, con un tipo a metà).** 5 numeri aziendali; 6 clienti con il nome; 5 testimonianze con il nome dell'azienda e la fonte, senza comune (non è nelle fonti: chiesto nel LEGGIMI). Certificazioni: nessuna nelle fonti; al loro posto la fascia dei due riconoscimenti, senza marchi finché non c'è il permesso.
11. **Lavori con un nome: passa.** Tre lavori con cliente e luogo, anno (2026 per tutti e tre: inaugurazione Distner, notizie Setz e Malenfer), 3-5 dati e foto di 737 px (51%). Altri tre in tabella con "Quando".
12. **Ritmo a blocchi: passa.** Azienda su antracite, assistenza sul rosso, impianti e area test su grigio, piede antracite. Sezioni 120/120 px a 1440 e 72/72 a 390; margini 80 e 20 px.
13. **Un solo sistema di bottoni: passa.** Pieno e bordato, raggio 2 px, 52 px (48 in testata), testo 16 px a 700, anche "Assistenza" nel bottone di testata a 390. I bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: passa.** Campi M di A6 con l'allegato del disegno (PDF, DWG, DXF, STEP, JPG, PNG), più prodotto, misure, vernici e lingua; compone un'email (mailto), da collegare a un servizio (LEGGIMI). Indirizzo con "Apri in Google Maps" in area test, contatti e piede. Nessun iframe.
15. **Piede completo: passa.** Quattro colonne, testo di almeno 14 px: ragione sociale, indirizzo con Maps, telefono con gli orari, email, P.IVA, REA, capitale, Privacy, Cookie, lingue, LinkedIn e YouTube con il sottotitolo, e ora i riconoscimenti. Certificazioni: nessuna da mettere.

### Compiti dei clienti tipo (scheda d'uso, par. 8): nessuno peggiora

- *Serramentista estero, 1440*: "Impianti di verniciatura su misura" più grande, "Finestre" e le misure nella prima schermata; tre casi con foto, paese, barre, robot e misure (prima uno solo), in un clic su "Lavori"; "Richiedi un progetto" porta al modulo con l'allegato, e ora il testo dice il vero su come partono i file; area test con bottone, indirizzo e Maps. Resta il blocco delle lingue: le pagine `en/`, `de/`, `fr/` non esistono (LEGGIMI, prima della messa in linea).
- *Cliente con un impianto, 390*: "Assistenza +39 049 879 2458" in testata fissa, 165 x 48 px; lo stato aperto/chiuso ora è nella testata e resta visibile scorrendo; orari, quattro lingue e "Scrivi all'assistenza" con oggetto e traccia nella prima schermata, con area di tocco di 44 px (prima 15 px); lingua cambiabile dalla testata senza aprire il menu.
- *Usato e singole macchine*: invariato ("Usato" nel menu, riquadro accanto ai settori, "Vuoi solo parte di un impianto? Nessun problema!" con sei macchine).

### Controlli fatti

- `pro_controlli.mjs`: nessuno scorrimento orizzontale a 320, 360, 390, 768, 1024, 1280, 1440 e 1920; testo e foto dell'apertura non si sovrappongono; nessun errore di script; nessuna ancora senza destinazione; menu a 390 aperto e richiuso dopo il tocco.
- Modulo: invio vuoto fermato con l'avviso e il fuoco su "Cosa vuoi verniciare"; "Chiedi una prova in area test" sceglie "Prova in area test"; con un PDF scelto l'email composta ha l'oggetto giusto e l'elenco "Allegati da aggiungere"; letta senza aprirla.
- Orari: martedì 10:15 "Aperta ora, fino alle 12:00"; 13:10 "riapre alle 14:00"; 19:30 "riapre domani alle 8:30"; sabato "riapre lunedì"; 8 dicembre e Pasquetta "Chiusa oggi, festivo"; nelle tre lunghezze della testata.
- Screenshot in questa cartella (stato fissato a martedì 3/11/2026 alle 10:15): `home-1440-prima-schermata.jpg`, `home-1440.jpg`, `chiusura-1440.jpg`, `home-390-prima-schermata.jpg`, `home-390.jpg`; guardati a pezzi insieme alle pagine intere a 320, 768 e 1024 (cancellate dopo). Nessun U+2014 in pagina, nei .md e negli script.

### Caratteri e licenze

- **Archivo** (Omnibus-Type), da Google Fonts, SIL Open Font License 1.1, uso commerciale libero; servito dalla pagina (`sito/fonts/archivo-latin.woff2`, `archivo-latin-ext.woff2`), licenza in `sito/fonts/OFL-Archivo.txt`.
- Foto e render: tutti di Finiture (finiture.it), uso da confermare con l'azienda. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

| Uso | File di partenza | Pixel d'origine per pixel di schermo a 1440 |
|---|---|---|
| Apertura | `easygalleryimages_1_1092_assistenza.jpg` | 2,9 (817 px a schermo) |
| Settori | `EasyGalleryImages_1_16_Finestre_12_R01.jpg`, `EasyGalleryImages_1_17_Porte_3-taglio-dx_R01.jpg`, `easygalleryimages_1_18_clt_1_taglio-dx-e-no-acqua_r01.jpg`, `easygalleryimages_1_19_sedie_1_r01.jpg` | oltre 3 (302 px) |
| Distner | `EasyDNNNews_2160_IMG-20261013-WA0003.jpg` (notizia di ottobre 2026) | 2,2 (737 px) |
| Setz Fensterbau | `EasyDNNNews_2134_IMG20230905164125.jpg` (notizia dell'8/2/2026) | 3,3 (737 px) |
| Malenfer | `EasyDNNNews_2133_IMG20231118172507.jpg` (notizia del 17/5/2026) | 2,2 (737 px) |
| Area test | `easygalleryimages_1_1092_cabina-robot.jpg` | 3,2 (737 px) |
| Assistenza | `easygalleryimages_1_1092_dsc06151.jpg` | 3,8 (630 px) |
| Squadra | `Images_home-fotogallery-5.jpg` (1167x397, l'unica misura online) | 0,9 (1280 px) |
| Macchine | render `EasyDNNnews_19/20/24/27/30/35/36/40_*`, fondo portato a #F2F2F2 | mai ingranditi |
| Logo | `logo-finiture-da-youtube-ritagliato.png` | PNG a 2x; nel piede le lettere schiarite, il rosso com'è |
