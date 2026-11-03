# Home Eurotecnica Salmaso, livello professionale (3 novembre 2026)

Pagina: `sito/index.html` (statica, si apre anche da file), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, pagina da `_prova/script/index.src.html`, screenshot, controlli `pro_controlli.mjs`; prova degli orari con `pro_orari.mjs`). La versione di prima ("Il giorno dell’evento", 2 novembre) è copiata com’era in `_prova/versione-1-originale/` (sito, screenshot, nota e script).

File in questa cartella: `home-1440.jpg` e `home-390.jpg` (pagine intere), `home-1440-prima-schermata.jpg` (1440 x 900), `home-390-prima-schermata.jpg` (390 x 844), `chiusura-1440.jpg` (telefono grande, modulo e piede).

Altezza: 8503 px a 1440, 13210 a 390.

## Livello professionale

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all’attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Nuovo criterio: prima l’uso, poi l’identità, poi l’esecuzione. Regole: `_metodo/professionale/REGOLE.md`, famiglia S (servizi tecnici e imprese). Riferimenti guardati: le prime schermate a 1440 di tutti e 14 (foglio `riferimenti.jpg`) e a 390 dei cinque della famiglia S, le pagine intere di Kline e Wilson a pezzi; la prova su Unicar, Oby e Fornasiero (`_invio/zona/home/livello-professionale.jpg` e la nota di Unicar).

### Che cosa è cambiato rispetto alla versione 1

- **Via il titolo slogan e il microfono di repertorio.** "Il giorno dell’evento", spezzato da un radiomicrofono Unsplash scontornato, non diceva chi sono e la scheda d’uso lo indica come cosa "da grafico". Il titolo ora è il titolo del loro sito: "Impianti audio e video, service per eventi e noleggi a Padova", con l’occhiello "Padova, dal 1967".
- **Via tutte le foto di repertorio** (DESIGNECOLOGIST, Karisch, Emale, Dang): in pagina restano solo foto loro, dalla libreria del loro sito.
- **Via la linea "Ritiro mer 4 / Evento gio 5 / Reso ven 6" e il calcolo dei giorni feriali**: usava regole inventate da noi. Al loro posto la loro regola scritta in grande ("Quotiamo solo il/i giorno/i di effettivo utilizzo e non quello di consegna e di reso") e i quattro passi con le loro frasi.
- **Restano**: i due caratteri (General Sans per i titoli, ora nel peso 600; Host Grotesk per il testo), il petrolio del logo #257B82 e il petrolio scuro del loro piede di sempre #123E42, la bozza vettoriale del logo, MePA e la storia dei sistemi per conferenze fatti a Padova.
- **Fondo**: bianco e un grigio freddo #EEF2F2, niente beige né il verde acqua chiaro di prima; tre blocchi pieni (petrolio scuro, petrolio, petrolio scuro) e il piede antracite.

### Struttura (famiglia S, adattata)

1. Testata fissa: logo, cinque voci con le loro parole (Service ed eventi, Noleggi, Impianti, Azienda, Dove siamo), stato "Aperto ora, fino alle 12.30" e il bottone "049 760348". A 390: logo, bottone del numero, Menu.
2. Apertura: occhiello con la prova (dal 1967), titolo con mestiere e città, la riga dei servizi (amplificazione, radiomicrofoni, traduzione simultanea, video e videowall, riprese e streaming), "Chiama 049 760348" e "Chiedi un’offerta per un evento" (email a service@ con oggetto e traccia: data, luogo e sala, persone, cosa serve, lingue, diretta, ritiro o montaggio), "Offerta personalizzata senza impegno", poi orari con lo stato e sede con "Indicazioni". A destra la loro foto della regia in sala storica (2024-05-1). A 390 l’ordine è quello di chi passa in sede: stato e orari, Chiama, "Indicazioni per la sede" (Google Maps con il cid), "Chiedi un’offerta", indirizzo con l’angolo della via.
3. Tre porte su petrolio scuro, al posto della fascia delle garanzie: Service ed eventi, Noleggi (con la regola dei giorni), Impianti per le sale. Sono le loro tre promesse, con le loro frasi.
4. Impianti (seconda schermata a 1440, per chi gestisce una sala): tre riquadri "Abilitati MePA dal 2022, anche per OS 30" con le cinque abilitazioni, "Un impianto già installato che non va?" (Chiama e email di assistenza a info@ con la traccia) e "Sopralluogo e consulenza tecnica" (email con la traccia e la planimetria); il teatro (2024-05-5), i sette tipi di sala con le loro frasi e la fascia dei marchi con quello che fanno.
5. Service: quattro schede con la foto del lavoro (amplificazione 2024-05-3, radiomicrofoni 2024-05-6, video 2024-05-4, riprese 2024-05-2), due schede di testo per traduzione simultanea e streaming, e il riquadro "Per l’offerta diteci data, luogo, persone, lingue e se serve la diretta". Ogni scheda porta al modulo con la richiesta e la voce già spuntate.
6. Noleggi su petrolio: la regola in 48 px, ritiro il giorno prima con il tecnico, uso, reso a fine evento o il giorno dopo, oppure consegna e montaggio; il materiale in tre colonne; "Chiedi un noleggio" (email con la traccia) e Chiama.
7. Azienda: i banchi con i microfoni e l’unità di voto (sala_vicenza), la storia con le loro parole e quattro numeri veri (1967, 1986, 5 abilitazioni MePA, monitor fino a 86").
8. Dove siamo: facciata con l’insegna "emporio dell’audio" e showroom, indirizzo con l’angolo, stato, tabella degli orari con il giorno di oggi evidenziato, Indicazioni e Chiama, "Cercate un pezzo? Chiamate prima di passare".
9. Chiusura su petrolio scuro: "049 760348" in 88 px, la loro frase "Avete bisogno di un consiglio o di una consulenza tecnica?", le due email con a che cosa servono, e il modulo.
10. Piede in quattro colonne.

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito completo in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi a 1440 e 390 e le catture a 320, 768, 1024.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa alta 89 px a 1440 e 73 a 390, bottone "049 760348" alto 48 px con la cornetta. A metà pagina, a 1440 e a 390, il bottone si vede e si tocca (`elementFromPoint`). 9 link `tel:`, tutti `tel:+39049760348`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** A 1440 x 900: H1 con il mestiere e "Padova", occhiello "Padova, dal 1967", bottone "Chiama 049 760348" e la mail dell’offerta, orari, sede, le tre porte. A 390 x 844: lo stesso titolo, stato e orari, "Chiama 049 760348" largo 350 px, "Indicazioni per la sede", "Chiedi un’offerta", indirizzo e traccia dell’offerta, tutto senza scorrere.
3. **Immagine vera nell’apertura: passa.** La loro regia di un convegno in una sala storica con il soffitto dorato, il mixer Yamaha in primo piano e il pubblico. Riserva: è uno scatto da telefono (1600 x 616), mostrato senza ingrandirlo (a 1440 lo riquadro alto 622 px sui 616 d’origine); senza persone dell’azienda e senza mezzi con il marchio: la ripresa vera è nel LEGGIMI.
4. **Zero repertorio: passa.** `indicativ` compare 0 volte; in `sito/img/` solo tagli delle foto del loro sito e il logo; nessun file da Unsplash o Pexels.
5. **Foto in serie: passa.** Nove foto, tutte dalla loro libreria, con lo stesso trattamento (`pro_img.py`: rumore da telefono smorzato, bianco portato a metà verso il neutro, saturazione 0,9, contrasto leggero); due formati a 1440 (3:2 per tutte, l’apertura riquadrata dalla colonna, circa 1,18:1), nessuna didascalia, nessuna ingrandita oltre la misura d’origine.
6. **Palette dal marchio: passa.** `--petrolio` #257B82 (logo 2025) e `--petrolio-scuro` #123E42 (piede del loro sito), più neutri (inchiostro, testo secondario, grigio freddo, bianco, filetti). Nessun colore scritto a mano fuori da `:root`. Nessun beige. Il rosso della facciata resta nella foto.
7. **Scala tipografica corta: passa.** 7 misure a 1440 (14, 17, 19, 23, 48, 56, 88) e 7 a 390 (14, 16, 17, 20, 28, 32, 44); testo corrente 19 px a 1440 e 17 a 390 (schede 17 e 16); nessun testo sotto i 14 px; H1 56 px a 1440 e 32 a 390.
8. **Due famiglie al massimo: passa.** General Sans 600 per titoli e cifre, Host Grotesk 400 e 600 per testo, etichette, bottoni e modulo, in tutta la pagina.
9. **Servizi in schede con la foto: passa, con riserva.** Quattro colonne, quattro schede con la foto del loro lavoro, tutte 3:2, nome, riga e "Chiedi l’offerta", tutta la scheda cliccabile. Traduzione simultanea e streaming sono due schede di testo a parte, perché non c’è una loro foto che regga (le vecchie `trad` e `streaming` sono 397 px e cataloghi): sono nel LEGGIMI tra le foto da fare.
10. **Almeno tre tipi di prova: non passa (2 su 4).** Ci sono i numeri aziendali (1967, 1986, 5 abilitazioni MePA, monitor fino a 86") e la fascia di certificazioni e fornitori (MePA con le cinque abilitazioni, marchi con quello che fanno). Mancano recensioni (nessuna leggibile, nessuna inventata) e clienti con il nome: Camera di Commercio di Padova e Università di Udine risultano da atti pubblici ma vanno citati solo con il loro permesso (LEGGIMI).
11. **Lavori con un nome: non passa.** Le foto del 2024 sono lavori veri ma senza luogo, cliente e anno confermati; nessuna didascalia inventata. Cosa chiedere è nel LEGGIMI.
12. **Ritmo a blocchi: passa.** Tre blocchi pieni oltre al piede: le porte (petrolio scuro), i noleggi (petrolio), la chiusura (petrolio scuro); service e dove siamo su grigio; piede antracite. Spazio fra le sezioni 120 px a 1440 e 72 a 390; margini 80 px a 1440 e 20 a 390 (16 sotto i 360 px).
13. **Un solo sistema di bottoni: passa.** Pieno e bordato, raggio 4 px, altezza 56 px (48 in testata), testo 17 px (16 sul telefono); i bottoni di chiamata contengono il numero; sui blocchi scuri le stesse due varianti in bianco.
14. **Modulo e "dove" per il mestiere: passa, con riserva.** Modulo in home con: che cosa vi serve (service, noleggio con ritiro, noleggio con montaggio, impianto nuovo o sopralluogo, assistenza, emporio), nome e telefono obbligatori, ente, email, data dell’evento, persone, luogo e sala (indirizzo dell’impianto per impianti e assistenza), cosa serve (sei voci), lingue, diretta, tipo di sala, entro quando (urgenza), descrizione, istruzione per allegare planimetrie e foto (un mailto non porta allegati). Compone l’email a service@ (eventi e noleggi) o a info@ (impianti, assistenza, emporio): niente invio automatico. Nessun iframe di mappa: "Indicazioni" apre la loro scheda Google con il cid. Manca l’elenco dei comuni serviti: non è nelle fonti (LEGGIMI).
15. **Piede completo: passa.** Quattro colonne a 1440, testo di almeno 14 px: Eurotecnica Salmaso S.R.L., P.IVA 01353510280, C.F. 01871990238, "Abilitata MePA dal 2022, anche OS 30"; sede ed emporio con indirizzo cliccabile e orari; telefono, info@, service@, LinkedIn con il sottotitolo; le sezioni; Privacy e Cookie. Le zone servite mancano per la stessa ragione della regola 14.

### Compiti della scheda d’uso (par. 8)

- *Evento, 1440*: "traduzione simultanea" e "radiomicrofoni" nella prima schermata (riga dei servizi, in grassetto). "Chiedi un’offerta per un evento" apre l’email a service@ con oggetto e traccia, con accanto "scriveteci data, luogo, numero di persone, lingue e se serve la diretta". La regola dei giorni è nella porta "Noleggi" a 900-1000 px e in grande nella sezione Noleggi, con "Il giorno prima, ritiro in sede" e il tecnico; nessun calcolatore.
- *Evento, 390*: `tel:+39049760348` a tutta larghezza a 444 px, senza scorrere.
- *Sala, 1440*: sezione Impianti nella seconda schermata, con MePA e OS 30, l’assistenza con telefono e info@, i sette tipi di sala (sale consiliari e chiese comprese) e i marchi come testo; P.IVA e C.F. selezionabili nel piede.
- *Sede, 390*: stato e orari a 360 px, "Indicazioni per la sede" (cid) a 512 px, indirizzo con l’angolo a 650 px; la sezione Dove siamo con la facciata, "emporio dell’audio" e la tabella degli orari; il bottone del numero resta in testata scorrendo.
- *Identità*: nessuna foto di sala altrui, nessun prezzo, numero o cliente inventato; titolo e frasi dal loro sito; nessun U+2014.

### Caratteri e licenze

- **General Sans 600** (Indian Type Foundry), da Fontshare, ITF Free Font License (uso commerciale ammesso, anche sul web); `sito/fonts/general-sans-600.woff2`.
- **Host Grotesk** (Element Type), da Google Fonts, SIL Open Font License 1.1, file variabile usato nei pesi 400 e 600; `sito/fonts/host-grotesk-variabile.woff2`, licenza in `sito/fonts/OFL-host-grotesk.txt`, note in `sito/fonts/LICENZE.md`.
- Foto: solo materiale del loro sito (libreria media di WordPress, `assets/originali/`), da usare con il loro permesso; i diritti delle sei foto del 2024 vanno chiariti (EXIF, vedi LEGGIMI). Nessuna immagine generata, nessun disegno.

### Controlli fatti (3/11/2026)

- `pro_controlli.mjs`: regole 1-9 e 12-15 superate nelle misure; 10 e 11 no. Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1440, 1920; nessuna sovrapposizione nell’apertura; nessun errore di script; tutte le ancore hanno la destinazione; tutti i `tel:` sono `+39049760348`, tutti i mailto hanno l’oggetto, la sola mappa è il cid 13052135561717271527.
- Menu a 390: si apre, si chiude dopo il clic su una voce, l’ancora si ferma sotto la testata. Modulo: invio vuoto fermato con l’avviso e il fuoco sul nome; la scheda "Traduzione simultanea" spunta la voce nel modulo; email composta a service@ per il service e a info@ per l’assistenza (con sei campi da evento nascosti), lette senza inviarle.
- `pro_orari.mjs`: martedì 10.00 aperto fino alle 12.30; 13.10 riapre alle 14.30; 19.00 riapre domani; venerdì sera e sabato riapre lunedì; 8 dicembre e Pasquetta "Chiuso oggi, festivo"; vigilia di Natale sera riapre lunedì.
- Screenshot guardati a pezzi a 1440 e 390, prime schermate e pagine intere a 320, 768 e 1024. Nessun U+2014 in pagina, nei .md e negli script.
