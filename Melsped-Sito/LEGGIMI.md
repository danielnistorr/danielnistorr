# Melsped Srl: proposta di nuova home

Proposta non richiesta di una nuova homepage per Melsped Srl, casa di spedizioni di viale Veneto 9 a Saonara (PD). Solo la home: le pagine interne sono linkate ma non ancora fatte. Nulla è stato pubblicato né inviato all'azienda.

## Dove sono le cose

- `sito/index.html`: la home, statica, si apre anche con file:///. Immagini in `sito/img/` (WebP in più larghezze, logo SVG), caratteri in `sito/fonts/` (Archivo, con la licenza `OFL.txt`).
- Foto di partenza: `assets/esterne/` e, alla risoluzione piena, `assets/esterne-alta/` (apertura, Dogana, chiusura).
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, e `NOTA.md` con idea, scelte e controlli.
- `_prova/script/build_finale.sh` rifà tutto: immagini (`finale_img.py`), caratteri, controlli (`controlla_img.py`, ricerca di U+2014), screenshot (`scatti_finali.mjs`), misure (`misura_finale.mjs`) e segnali da IA. `prova_tastiera.mjs` prova il selettore e il piede con la tastiera; `controlli_finali.mjs` misura lo scorrimento orizzontale da 320 a 2560 px, i bersagli di tocco a 390 e i collegamenti. Controlli a pezzi in `_prova/script/controllo/`.
- Analisi con le fonti: `01-analisi.md`. Crediti delle immagini: `assets/CREDITI.md`. Prototipi da cui nasce: `_prova/home/a` (scelto) e `_prova/home/b`.

## Pagine del sito nuovo linkate dalla home

Vanno create (oggi il sito Joomla del 2013 non le ha con questi indirizzi):

| Indirizzo | Contenuto |
|---|---|
| `/servizi/strada/` | groupage door-to-door in Europa, camion completi e dedicati, espressi |
| `/servizi/est-europa/` | le tratte verso il nord e l'est, Ungheria, Bulgaria, Romania |
| `/servizi/aereo/` | spedizioni aeree |
| `/servizi/mare/` | spedizioni marittime, groupage su container |
| `/servizi/dogana-intrastat/` | operazioni doganali, Moduli Intrastat |
| `/servizi/magazzino/` | logistica e magazzino, ritiro e riconsegna |
| `/azienda/` | chi siamo |
| `/paesi/` | paesi serviti |
| `/contatti/` | contatti con la mappa |
| `/en/` | versione inglese (oggi esiste) |
| `/privacy/`, `/cookie/` | oggi mancano: vanno scritte con il loro consulente |

Nel menu in alto i link portano alle sezioni della home (`#servizi`, `#paesi`, `#azienda`, `#contatti`). Il piede ha tre colonne: Servizi (le sei pagine `/servizi/...`), Azienda (`/azienda/`, `/paesi/`, `/en/`) e Contatti (telefono, email, PEC, mappa, LinkedIn); la pagina `/contatti/` resta nel sito nuovo ma dalla home si arriva ai recapiti della chiusura.

## Dati da confermare con Melsped

In pagina c'è solo ciò che è scritto sul loro sito o nel Registro Imprese (fonti in `01-analisi.md`). Da confermare:

1. **L'anno**: la pagina dice "dal 1975" come il sito di oggi ("Nata nel 1975"), ma la srl risulta iscritta il 02/01/1978. Il 1975 è l'anno di una ditta precedente? Se va scritto 1978, cambia in tre punti (riga sotto il titolo dell'apertura, paragrafo grande di "Chi siamo", riga sotto il logo nel piede).
2. **Il fax** 049 879 2024, in piccolo nella chiusura: è ancora in uso? Se no, si toglie la riga.
3. **Gli orari** d'ufficio e di magazzino: non sono pubblicati, quindi in pagina non ci sono. Se ce li danno vanno nella chiusura, sotto l'indirizzo.
4. **L'email** da mostrare: info@melsped.it (sul sito è nascosta in JavaScript). La PEC melsped@pec.it viene da aziende.it.
5. **I social**: nel piede c'è solo LinkedIn, come ultima voce della colonna Contatti (linkedin.com/company/melsped, che esiste ma ha il settore sbagliato e non ha il logo: va corretta prima di metterla in pagina). La pagina Facebook esiste (foto profilo del 2022) ma non si legge senza login: va aggiunta solo se è attiva. Twitter/X `@Melsped` non verificato; Google+ è chiuso.
6. **I servizi di oggi**, perché i testi sono del 2013: tratte giornaliere, camion completi e dedicati, espresso, aereo, mare, groupage su container, ritiro e riconsegna con mezzi propri. In particolare il rapporto con Ungheria, Bulgaria e Romania ("estremamente enfatizzato" nel 2013): ora è nella prima schermata ("Da Saonara verso Ungheria, Bulgaria e Romania, e in tutta Europa, dal 1975") ed è la cosa da confermare per prima. Se non è più vero, la riga diventa "Da Saonara in tutta Europa, dal 1975".
7. **Il magazzino** "oltre 1.400 metri quadri": è ancora così?
8. **Intrastat**: in pagina c'è "i Moduli Intrastat" (parola del sito) con la definizione delle loro note. Non c'è scritto che li compilano o li presentano: se lo fanno, si può dire.
9. **Le frasi grandi** sono loro: "Abbatti i confini" e "Le esigenze del cliente al primo posto" sono le due metà del titolo del Profilo aziendale; "Ogni maggior svincolo in..." e "in ogni angolo del mondo industrializzato" sono dalle pagine Servizi. "Da Saonara verso Ungheria, Bulgaria e Romania, e in tutta Europa" è una nostra sintesi della pagina dei servizi camionistici e dei "partners e corrispondenti dislocati in tutti paesi europei". "Organizziamo la spedizione e facciamo le pratiche" è una nostra sintesi del mestiere: va bene detta così?
10. **Il tracking** online della pagina Web è scritto al futuro ("sarà in grado"): esiste? Se sì, un link nel menu.
11. **Certificazioni** (AEO, ISO 9001) e numeri (spedizioni l'anno, corrispondenti): non sono pubblici e non ci sono. Se esistono sono la prova più forte da mettere in "Chi siamo". I 7 dipendenti (aziende.it, 2025) sono stati tolti dalla home.
12. **Privacy e cookie**: il sito di oggi ha un pixel di tracciamento `script.whoseesyou.com` e nessun banner. Nel sito nuovo va chiarito con il loro consulente.

## Newsletter

Non c'è, di proposito: Melsped è uno spedizioniere B2B senza fiere, cataloghi, collezioni né clienti privati, e le sole "notizie" del sito sono cronache di pallavolo del 2012. Se un giorno volessero comunicare novità (nuove tratte, orari di chiusura estiva), si aggiunge nel piede un campo email con la casella del consenso, collegato a un servizio (Brevo, Mailchimp o simili): senza collegamento non funziona.

## Foto: tutte da rifare dal vero

Le foto in pagina sono segnaposto Unsplash (licenza Unsplash, uso commerciale libero, verificata sulla pagina di ogni foto; elenco e ritocchi in `assets/CREDITI.md`). In pagina lo dice una riga sola in fondo al piede ("Foto indicative, da sostituire con le foto di Melsped"), da togliere quando arrivano le foto vere. Le foto del sito di oggi (2013, al massimo 660 px) non reggono a questa misura. Serve mezza giornata di un fotografo, con queste priorità:

1. **Apertura, la prima da fare.** Il loro furgone Iveco col logo giallo (meglio di un semirimorchio che non è loro), fermo davanti alle baie di viale Veneto 9; in alternativa il semirimorchio di un partner, solo con il suo permesso scritto. Di tre quarti, con il muso verso sinistra e la coda verso destra, verso le 9 del mattino, con il sole alle spalle del fotografo. Due terzi dell'inquadratura di cielo, perché il titolo "Abbatti i confini" sta su una riga sola, da margine a margine, sopra il mezzo. Orizzonte dritto (a bolla), macchina a circa 1,2 m da terra, 35-50 mm, file da almeno 5000 px di lato lungo. Una seconda versione verticale, con il mezzo nel terzo basso, per il telefono. Piazzale sgombro: niente auto, bidoni o cartelli.
2. **Chiusura.** Un bancale filmato pronto al carico (o una fila di bancali) nel loro magazzino, in luce di giorno dai portoni aperti, ripreso ad altezza d'occhio. Taglio orizzontale 4:3. In alternativa la facciata con l'insegna, frontale.
3. **Strada.** Le baie della sede con un camion accostato, frontali, in luce radente del pomeriggio. Taglio 12:5.
4. **Dogana e magazzino.** Il magazzino da 1.400 m² in luce naturale, da una corsia ordinata, con un solo carrello; in alternativa l'ufficio con il planisfero da parete col logo, ripreso in piano. Il segnaposto di oggi è un capannone vuoto e nuovo.
5. **Aereo e mare.** Melsped non ha aerei né navi: vanno bene foto di banca immagini con licenza commerciale, oppure foto dei loro partner con il permesso scritto. Per il mare meglio una foto da terra (il molo, un container al carico) della nave dall'alto, che è l'immagine più vista del settore. Stesso trattamento delle altre: bianco caldo, ombre aperte, blu bassi, taglio 12:5.
6. Persone ritratte (le due impiegate delle foto del 2013 o chi c'è oggi): solo con il consenso firmato.

## Logo

Il sito non ha un vettoriale. In pagina c'è un mio ricalco in SVG del PNG 457x457 della pagina Facebook (`assets/originali/logo-melsped-ricalco-da-facebook.svg`), fedele fino a circa 450 px; in testata e nel piede è tagliato sopra la riga "SPEDIZIONI INTERNAZIONALI", che a 150 px sarebbe alta 7 px e illeggibile. Da chiedere: il vettoriale originale e il giallo ufficiale (nel PNG è circa #F7CF0A, nel JPEG del sito è più arancio). Il favicon oggi non esiste: la pagina usa lo stesso SVG.

## Licenze

- Foto: Unsplash License (https://unsplash.com/license), segnaposto, nessuna generata dall'IA, nessuna usata in altre home della campagna (elenco e ritocchi in `assets/CREDITI.md`).
- Carattere: Archivo di Omnibus-Type, SIL Open Font License 1.1, servito dalla pagina (`sito/fonts/`), licenza in `sito/fonts/OFL.txt`.
- Testi: dal sito melsped.it e dai dati del Registro Imprese riportati da aziende.it.
