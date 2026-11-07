# Home Eurotecnica Salmaso, livello professionale (3 novembre 2026)

Pagina: `sito/index.html` (statica, si apre anche da file), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, pagina da `_prova/script/index.src.html`, screenshot, controlli `pro_controlli.mjs`; prova degli orari con `pro_orari.mjs`). La versione di prima ("Il giorno dell’evento", 2 novembre) è copiata com’era in `_prova/versione-1-originale/` (sito, screenshot, nota e script).

File in questa cartella: `home-1440.jpg` e `home-390.jpg` (pagine intere), `home-1440-prima-schermata.jpg` (1440 x 900), `home-390-prima-schermata.jpg` (390 x 844), `chiusura-1440.jpg` (telefono grande, modulo e piede).

Altezza: 9156 px a 1440, 13179 a 390.

## Ritocco finale (3 novembre 2026, pomeriggio)

Dal controllo del livello professionale (voto 6: "ordinata e chiara", non ancora "la voglio così") e dalle due prove dei clienti tipo (segreteria di un convegno, geometra di un Comune). Riferimenti riguardati: le prime schermate di tutti e 14 (`riferimenti.jpg`) e quelle a 390 della famiglia S (`_prova/pro-controllo/confronto-famiglia-S.jpg`), le pagine intere di Wilson e Kline a pezzi.

- **Apertura nuova, non più "titolo a sinistra e foto a destra" (B1).** Il titolo è il gesto di scala: H1 a 72 px in General Sans 700 su otto colonne, a destra la riga dei servizi; sotto Chiama, la mail dell'offerta con la traccia, orari e sede. Poi la loro panoramica della regia **intera, a tutta larghezza e nel suo formato** (1440 x 554 da 1600 x 616, nessun riquadro e nessun ingrandimento), e sotto le tre porte. Nella prima schermata a 900 px la foto parte a 586 px e se ne vedono 314.
- **A 390 c'è un'immagine nella prima schermata**: una striscia 390 x 130 (3:1) della stessa regia dal lato della sala (lanterne, pubblico, mixer), senza il monitor. La nota dell'offerta è nascosta a 390 (la traccia è nella mail e nel riquadro del Service). Stato e orari a 495, Chiama a 584-640, Indicazioni a 650-706, Offerta a 716-772, indirizzo fino a 832: tutto entro 844.
- **Occhiello con la prova più forte per la PA**: "Padova, dal 1967 · Abilitati MePA, anche OS 30".
- **Persone e testi di terzi**: riprese ritagliata sul solo schermo con la ripresa e il microfono (niente tavolo dei relatori e cartellini, il cartellino sullo schermo sfocato); video tagliata a sinistra del titolo proiettato; il monitor della regia nella panoramica sfocato. Permessi delle persone riconoscibili nel LEGGIMI.
- **Foto più serie**: in `pro_img.py` il bianco va quasi al neutro per tutte (0,75 invece di 0,45), stessa curva e stessa saturazione; la panoramica senza maschera di nitidezza. Le foto del 2016 sono mostrate piccole: sala consiliare a 405 px (4 colonne), facciata e showroom a 360 px accanto all'indirizzo, come aiuto a riconoscere la sede.
- **Impianti meno fitti**: due riquadri (MePA e Assistenza, con l'indirizzo info@ scritto per intero sotto il bottone "Scrivi una email"), poi a 96 px foto della sala consiliare con l'unità di voto e del teatro a sinistra, i sette tipi di sala a destra e sotto "Impianto nuovo: sopralluogo e consulenza tecnica" con il bottone bordato. Le marche principali sono già nel paragrafo d'apertura della sezione.
- **Fascia dei marchi a sé**, su grigio, quattro colonne, nome a 23 px e didascalia a 17 (non più 14), dopo Azienda.
- **Azienda senza foto**: titolo e storia con le loro parole, poi i quattro numeri.
- **Schede del Service**: a 390 tutte quadrate (1:1, stesso taglio); "Chiedi l'offerta" apre la mail a service@ con il servizio già scritto ("Cosa serve: Traduzione simultanea"), invece di saltare al modulo 4000 px più giù.
- **Noleggi con le loro parole**: "Il giorno antecedente", "I noleggi si ritirano il giorno antecedente all'utilizzo; un tecnico qualificato è a disposizione per spiegazioni e domande"; "Lo usate" diventa "Si paga solo l'utilizzo".
- **Arrivo dal menu**: il titolo della sezione si ferma 32 px sotto la testata (prima c'erano 130-200 px vuoti).
- **Modulo**: il titolo cambia con la richiesta (offerta, noleggio, sopralluogo, assistenza, emporio); la data esce gg/mm/aaaa.
- **Orari**: fra 14.00 e 14.30 e fra 18.00 e 18.30, dove 2GIS e il vecchio sito non concordano, la pagina non dice né aperto né chiuso e mostra solo l'orario scritto.
- **Titoli più pesanti**: General Sans 700 per H1, H2, la regola del noleggio, il telefono grande e le cifre; 600 per i titoletti; Host Grotesk 400 per il testo.

## Livello professionale (prima stesura, 3 novembre mattina)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Criterio: prima l'uso, poi l'identità, poi l'esecuzione. Regole: `_metodo/professionale/REGOLE.md`, famiglia S (servizi tecnici e imprese).

### Che cosa è cambiato rispetto alla versione 1

- **Via il titolo slogan e il microfono di repertorio.** "Il giorno dell'evento", spezzato da un radiomicrofono Unsplash scontornato, non diceva chi sono. Il titolo ora è il titolo del loro sito: "Impianti audio e video, service per eventi e noleggi a Padova".
- **Via tutte le foto di repertorio** (DESIGNECOLOGIST, Karisch, Emale, Dang): in pagina restano solo foto loro, dalla libreria del loro sito.
- **Via la linea "Ritiro mer 4 / Evento gio 5 / Reso ven 6" e il calcolo dei giorni feriali**: usava regole inventate da noi. Al loro posto la loro regola scritta in grande ("Quotiamo solo il/i giorno/i di effettivo utilizzo e non quello di consegna e di reso") e i quattro passi con le loro frasi.
- **Restano**: i due caratteri (General Sans per i titoli, Host Grotesk per il testo), il petrolio del logo #257B82 e il petrolio scuro del loro piede di sempre #123E42, la bozza vettoriale del logo, MePA e la storia dei sistemi per conferenze fatti a Padova.
- **Fondo**: bianco e un grigio freddo #EEF2F2, niente beige né il verde acqua chiaro di prima.

### Struttura (famiglia S, adattata)

1. Testata fissa: logo, cinque voci con le loro parole (Service ed eventi, Noleggi, Impianti, Azienda, Dove siamo), stato degli orari e il bottone "049 760348". A 390: logo, bottone del numero, Menu.
2. Apertura: occhiello con le prove (dal 1967, MePA e OS 30), titolo con mestiere e città a 72 px, la riga dei servizi, "Chiama 049 760348" e "Chiedi un'offerta per un evento" (email a service@ con oggetto e traccia), "Offerta personalizzata senza impegno", orari e sede con "Indicazioni"; poi la panoramica della regia in sala storica a tutta larghezza (2024-05-1). A 390: striscia della regia, titolo, servizi, stato e orari, Chiama, "Indicazioni per la sede" (cid), "Chiedi un'offerta", indirizzo con l'angolo.
3. Tre porte su petrolio scuro: Service ed eventi, Noleggi (con la regola dei giorni), Impianti per le sale.
4. Impianti (seconda schermata a 1440): le marche principali nel paragrafo, due riquadri "Abilitati MePA dal 2022, anche per OS 30" e "Un impianto già installato che non va?" (Chiama, email con la traccia, info@ per intero); sala consiliare con l'unità di voto e teatro, i sette tipi di sala con le loro frasi, "Impianto nuovo: sopralluogo e consulenza tecnica".
5. Service su grigio: quattro schede con la foto del lavoro, due schede di testo per traduzione simultanea e streaming, il riquadro "Per l'offerta diteci data, luogo, persone, lingue e se serve la diretta". Ogni scheda apre la mail a service@ con il servizio scritto.
6. Noleggi su petrolio: la regola in 48 px, ritiro il giorno antecedente con il tecnico, si paga solo l'utilizzo, reso a fine evento o il giorno dopo, oppure consegna e montaggio; il materiale; "Chiedi un noleggio" e Chiama.
7. Azienda: dal 1967, i sistemi per conferenze fatti a Padova, quattro numeri veri (1967, 1986, 5 abilitazioni MePA, monitor fino a 86").
8. Marchi su grigio: sette voci con che cosa fanno.
9. Dove siamo: indirizzo con l'angolo, stato, tabella degli orari con il giorno di oggi, Indicazioni e Chiama, "Cercate un pezzo? Chiamate prima di passare"; facciata con l'insegna "emporio dell'audio" e showroom piccole a destra (a 390 la facciata sopra).
10. Chiusura su petrolio scuro: "049 760348" in 88 px, la loro frase sulla consulenza, le due email, il modulo.
11. Piede in quattro colonne.

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`, rifatto dopo il ritocco), più gli screenshot guardati a pezzi a 1440 e 390 e le catture a 320, 768, 1024.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa alta 89 px a 1440 e 73 a 390, bottone "049 760348" alto 48 px. A metà pagina il bottone si vede e si tocca (`elementFromPoint`) a 1440 e a 390. 9 link `tel:`, tutti `tel:+39049760348`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** A 1440 x 900: H1 con il mestiere e "Padova", occhiello "Padova, dal 1967 · Abilitati MePA, anche OS 30", "Chiama 049 760348" (249 x 56) e l'offerta, orari, sede, l'inizio della panoramica. A 390 x 844: striscia, stesso titolo e occhiello, stato e orari, Chiama largo 350 px, Indicazioni, Offerta, indirizzo.
3. **Immagine vera nell'apertura: passa.** La loro regia di un convegno in sala storica (mixer Yamaha, ricevitori, pubblico, soffitto dorato), intera nel suo formato a 1440 e in striscia 3:1 a 390. Riserva: senza persone dell'azienda e senza marchio; la ripresa vera è nel LEGGIMI.
4. **Zero repertorio: passa.** `indicativ` 0 volte, nessun file da Unsplash o Pexels: in `sito/img/` solo tagli di `assets/originali/` e il logo.
5. **Foto in serie: passa, con riserva.** Nove foto a 1440, due formati (2,6:1 la panoramica, 3:2 le altre); a 390 tre (3:1 la striscia, 1:1 le schede, 3:2 le altre); nessuna didascalia; nessuna ingrandita oltre la misura d'origine; stesso bianco quasi neutro, stessa curva e saturazione. Riserva: restano scatti da telefono con luci diverse (tungsteno, sera, giorno del 2016): la serie vera la dà solo una giornata con un fotografo (LEGGIMI).
6. **Palette dal marchio: passa.** `--petrolio` #257B82 (logo) e `--petrolio-scuro` #123E42 (piede del loro sito), più neutri; nessun colore a mano fuori da `:root`; nessun beige.
7. **Scala tipografica corta: passa.** 7 misure a 1440 (14, 17, 19, 23, 48, 72, 88) e 7 a 390 (14, 16, 17, 20, 28, 32, 44); testo corrente 19 px a 1440 e 17 a 390 (schede 17 e 16); nessun testo sotto i 14 px; H1 72 px a 1440 (fascia 56-79) e 32 a 390.
8. **Due famiglie al massimo: passa.** General Sans 700 (H1, H2, cifre) e 600 (titoletti); Host Grotesk 400 (testo) e 600 (etichette, bottoni).
9. **Servizi in schede con la foto: passa, con riserva.** Quattro colonne, quattro schede con la foto del lavoro, 3:2 a 1440 e tutte 1:1 a 390, tutta la scheda cliccabile. Traduzione simultanea e streaming restano schede di testo: non c'è una loro foto che regga (LEGGIMI).
10. **Almeno tre tipi di prova: non passa (2 su 4).** Numeri aziendali (1967, 1986, 5 abilitazioni MePA, 86") e fascia di certificazioni e fornitori (MePA con le abilitazioni; marchi con quello che fanno). Mancano recensioni e clienti con il nome: non sono nelle fonti o vanno citati solo con permesso (LEGGIMI 2 e 3). Nessuno inventato.
11. **Lavori con un nome: non passa.** Le foto del 2024 non hanno luogo, cliente e anno confermati; nessuna didascalia inventata (LEGGIMI 3).
12. **Ritmo a blocchi: passa.** Tre blocchi pieni oltre al piede (porte e chiusura petrolio scuro, noleggi petrolio), due grigi (service, marchi), il resto bianco; piede antracite. Spazio fra le sezioni 120 px a 1440 e 72 a 390; margini 80 e 20.
13. **Un solo sistema di bottoni: passa.** Pieno e bordato, raggio 4 px, altezza 56 (48 in testata), testo 17 px (16 a 390); i bottoni di chiamata contengono il numero; niente più etichette tronche ("Scrivi una email" con l'indirizzo scritto accanto).
14. **Modulo e "dove" per il mestiere: non passa del tutto.** Modulo in home con tipo di intervento (sei voci), luogo e sala o indirizzo dell'impianto, urgenza ("Entro quando": subito, entro la settimana, senza fretta), istruzione per allegare planimetrie e foto (un mailto non porta file), titolo che cambia con la richiesta, data gg/mm/aaaa; nessun iframe, "Indicazioni" apre il cid. Manca l'elenco dei comuni serviti: non è nelle fonti (LEGGIMI 4).
15. **Piede completo: passa, con riserva.** Quattro colonne a 1440, testo di almeno 14 px: ragione sociale, P.IVA, C.F., MePA e OS 30; indirizzo con il link, orari; tel:, info@ e service@; LinkedIn con il sottotitolo; sezioni; Privacy e Cookie. Mancano le zone servite (come la 14) e il credito dello studio (da aggiungere alla consegna).

### Compiti della scheda d'uso (par. 8), dopo il ritocco

- *Evento, 1440*: "traduzione simultanea" e "radiomicrofoni" nella prima schermata; "Chiedi un'offerta per un evento" apre la mail a service@ con oggetto e traccia, con accanto il testo guida; ogni scheda del Service apre la stessa mail con il servizio scritto. La regola dei giorni e "il giorno antecedente" sono nella sezione Noleggi, con le loro parole; nessun calcolatore.
- *Evento, 390*: `tel:+39049760348` a tutta larghezza a 584 px, senza scorrere.
- *Sala, 1440*: Impianti subito dopo le porte (seconda schermata), con cinque marche nel paragrafo, MePA e OS 30, l'assistenza con telefono e info@ per intero, i sette tipi di sala; la fascia dei marchi completa più giù; P.IVA e C.F. selezionabili nel piede.
- *Sede, 390*: stato e orari a 495 px, "Indicazioni per la sede" (cid) a 650, indirizzo con l'angolo entro 832; la sezione Dove siamo con la facciata e "emporio dell'audio"; il bottone del numero resta in testata.
- *Identità*: nessuna foto di sala altrui, nessun prezzo, numero o cliente inventato; titolo e frasi dal loro sito; nessun U+2014.

### Caratteri e licenze

- **General Sans 700 e 600** (Indian Type Foundry), da Fontshare, ITF Free Font License (uso commerciale ammesso, anche sul web); `sito/fonts/general-sans-700.woff2` e `general-sans-600.woff2`.
- **Host Grotesk** (Element Type), da Google Fonts, SIL Open Font License 1.1, file variabile usato nei pesi 400 e 600; `sito/fonts/host-grotesk-variabile.woff2`, licenza in `sito/fonts/OFL-host-grotesk.txt`, note in `sito/fonts/LICENZE.md`.
- Foto: solo materiale del loro sito (libreria media di WordPress, `assets/originali/`), da usare con il loro permesso; i diritti delle sei foto del 2024 vanno chiariti (EXIF, vedi LEGGIMI). Nessuna immagine generata, nessun disegno.

### Controlli fatti (3/11/2026, dopo il ritocco)

- `pro_controlli.mjs`: regole 1-9, 12, 13 e 15 superate nelle misure; 10 e 11 no (mancano dati, non inventati), 14 senza l'elenco dei comuni. Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1440, 1920; nessuna sovrapposizione nell'apertura; nessun errore di script; tutte le ancore hanno la destinazione; tutti i `tel:` sono `+39049760348`, tutti i mailto hanno l'oggetto, la sola mappa è il cid 13052135561717271527.
- Menu a 390: si apre, si chiude dopo il clic, il titolo di Noleggi si ferma 32 px sotto la testata. Modulo: invio vuoto fermato con l'avviso e il fuoco sul nome; scheda "Traduzione simultanea" con la mail a service@ e "Cosa serve: Traduzione simultanea"; mail composta a service@ con "Data dell'evento: 20/11/2026"; con "Assistenza" titolo "Richiesta di assistenza", sei campi da evento nascosti e mail a info@. Lette senza inviarle.
- `pro_orari.mjs`: 10.00 aperto fino alle 12.30; 13.10 riapre alle 14.30; 14.10 e 18.10 solo l'orario scritto; 15.00 aperto fino alle 18.30; 19.00 riapre domani; venerdì sera e sabato riapre lunedì; 8 dicembre e Pasquetta "Chiuso oggi, festivo".
- Screenshot guardati a pezzi a 1440 e 390, pagine intere a 320, 768 e 1024. Nessun U+2014 in pagina, nei .md e negli script.
