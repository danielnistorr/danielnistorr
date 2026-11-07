# 02. Riferimenti dal vivo

Ricerca del 18 ottobre 2026. Ho aperto con Playwright (Chromium, attraverso il proxy) 31 siti veri di poliambulatori, gruppi sanitari e medicina del lavoro (26 leggibili), 9 demo di temi medici venduti su ThemeForest ed Envato (8 leggibili), 8 siti di aziende con due pubblici (privati e aziende) fuori dalla sanità, più il sito attuale e l'anteprima Netlify. Ho guardato ogni prima schermata a 1440 e a 390 e le prime tre schermate a 1440 dei siti che uso qui sotto.

Dove sono i file (tutti in `_prova/riferimenti/`):
- `<nome>-1440-schermo.png` e `<nome>-390-schermo.png`: prima schermata (1440x900 e 390x844);
- `<nome>-1440.png` e `<nome>-390.png`: pagina intera;
- `<nome>-foglio.jpg`: le due prime schermate affiancate, per confrontare desktop e telefono;
- `<nome>-tre-schermate.jpg`: le prime tre schermate a 1440 (2700 px, a metà scala); `<nome>-390-tre.jpg`: le prime tre a 390;
- `<nome>-misure.json`: caratteri letti dal codice (h1, paragrafo, font caricati), colori di fondo più usati, bottoni, link `tel:`, larghezza a 390;
- `ritagli/`: 17 ritagli dei gesti citati nelle conclusioni;
- `confronto-390-a.jpg` (sei siti a 390 affiancati) e `confronto-template.jpg` (quattro template e gli ingressi di Benenden).
Gli script sono in `_prova/script/` (`rif.mjs` fa le quattro catture e le misure, `foglio.py`, `tre.py`).

**Attenzione a un artefatto.** Per non far scattare i caroselli, la pagina intera si fotografa allungando la finestra all'altezza della pagina. I siti con l'apertura alta "una schermata" (`100vh`) allora la gonfiano: Pihlajalinna, Medbase, Satispay e l'anteprima Netlify hanno l'apertura enorme nella pagina intera. Per quei siti vale la `-schermo.png`.

**Non usati.** Mayo Clinic (Access Denied di Akamai), Mehiläinen (controllo Vercel: peccato, è il gemello finlandese di Terveystalo), Forward (chiuso), Medigold Health e Poliambulatorio Dyadea (pagina vuota), Too Good To Go e Vitality UK (controllo anti-robot), Clinika (verifica), tia.com (non è Tia Health, è un software doganale: scartato). Le pagine di ricerca di ThemeForest ed Envato Elements e le anteprime `preview.themeforest.net` sono dietro Cloudflare: le classifiche di vendita le ho lette con WebFetch, le demo le ho aperte sui domini degli autori.

## 0. Da dove parte Lavoro & Salute

| | Sito attuale `00-sito-attuale-*` | Anteprima Netlify `00-anteprima-netlify-*` |
|---|---|---|
| Prima schermata | foto stock dall'alto (fonendoscopio, termometro, pillole su azzurro), al centro un blocco appunti con il logo, una frase ("società costituita nel 2006...") e due bottoni pieni, LAVORO arancio e SALUTE blu | schermo diviso a metà: a sinistra un saldatore con scintille (Lavoro), a destra una reception di vetro con orchidee (Salute), parola enorme in serif per metà, una riga, un bottone a filo; logo tondo al centro |
| Caratteri | Open Sans e Roboto | Fraunces (serif display, anche in corsivo: "Da che parte cominciamo?") e Archivo |
| Colori | arancio e blu del logo, azzurro della foto | velo scuro ruggine a sinistra, velo blu notte a destra |
| A 390 | una schermata, i due bottoni ci stanno | le due metà si impilano, 422 px ciascuna, tutte e due nella prima schermata |
| Cosa funziona | i due colori del logo assegnati alle due porte; la scelta subito | la scelta subito, e a telefono le due porte stanno in una schermata |
| Cosa non va | nessuna informazione oltre alla scelta; foto stock da banca immagini | serif corsivo (vietato), velo scuro sulle foto (testo grigio chiaro su grigio), le foto non sono della struttura (la reception non risulta quella di Limena: da verificare in 01), nessuna informazione utile oltre alla parola e al bottone; "Powered by Netlify" sopra il bottone a 390 |

Tutte e due fanno la stessa cosa: una pagina-bivio vuota. Il committente vuole tenere l'impianto a due porte e renderlo "più moderno". Dai riferimenti viene una risposta precisa: nei siti veri le due porte non sono mai solo due parole su due foto, ma due elenchi di cose da fare (sezione 3).

## 1. Poliambulatori, gruppi sanitari, medicina del lavoro

Li ho scelti perché hanno lo stesso problema di Lavoro & Salute: le persone che prenotano una visita e le aziende che comprano la medicina del lavoro. Terveystalo, Pihlajalinna e Concentra fanno proprio le due cose (in Finlandia la "työterveys", medicina del lavoro per le aziende, è il cuore di questi gruppi).

### 1.1 Terveystalo (Finlandia) - privati e medicina del lavoro
[terveystalo.com/fi](https://www.terveystalo.com/fi) e la sezione [Työterveys](https://www.terveystalo.com/fi/tyoterveys). File: `terveystalo-*`, `terveystalo-tyoterveys-*`, ritagli `terveystalo-due-pubblici-e-scorciatoie.jpg`, `terveystalo-fascia-tyoterveys-meta.jpg`.
- **Prima schermata:** in cima una riga di schede per pubblico: Henkilöasiakkaat (privati), Työterveys yrityksille (medicina del lavoro per le aziende), Julkiset palvelut, Töihin Terveystaloon, Yhtiö. Sotto: menu, campo di ricerca, "Asioi verkossa". Fascia blu notte con titolo "Sujuvasti hoitoon" (alle cure senza intoppi), una riga ("online o in oltre 200 sedi"), un solo bottone bianco "Varaa aika" (prenota) e quattro scorciatoie con piccola icona: vaccino antinfluenzale, pronto soccorso, servizio clienti (telefono), listino prezzi.
- **Seconda e terza:** prestazioni più cercate come pillole a scorrimento (pediatra, ortopedico, ginecologo, laboratorio), due schede notizia con foto vere di ambulatorio, poi l'app, poi **una fascia a metà**: a sinistra titolo blu grande "Työterveyspalvelut yrityksille ja organisaatioille", testo, bottone "Pyydä tarjous" (chiedi un'offerta); a destra la foto di due persone al lavoro davanti a un portatile.
- **Prenotazione e telefono:** un bottone unico in apertura; telefono 0900 30 000 nei link. **Specialità:** pillole. **Medici:** pagina "Asiantuntijat". **Foto:** persone vere in ambulatorio, luce calda, colori naturali. **Caratteri:** TerveystaloSans e TerveystaloSansDisplay (proprietari, grottesco molto nero nei titoli, 600 a 30 px nell'h1 della home, display più grande nelle fasce). **Colori:** blu notte #1A244A, blu marchio #0046AD, bianco, grigio #F6F6F6; forme blu a macchia (dal marchio) come unico decoro. **Densità:** alta ma ordinata.
- **Da non riprendere:** le macchie decorative sono il loro marchio; le schede notizia a carosello con frecce.
- **Da riprendere:** le schede per pubblico in cima e la seconda porta come fascia a metà con titolo e foto di lavoro vera.

### 1.2 Pihlajalinna (Finlandia) - privati e medicina del lavoro
[pihlajalinna.fi](https://www.pihlajalinna.fi/). File: `pihlajalinna-*` (usare la `-schermo`), ritaglio `pihlajalinna-colore-del-marchio-nelle-foto.jpg`.
- **Prima schermata:** riga di pubblici in alto (Henkilöasiakkaat, Työterveys, Julkiset palvelut, Yhtiö, Työpaikat, Sijoittajat), menu con "Varaa aika" pieno arancio. Una griglia asimmetrica: a sinistra grande foto di un medico vero che ride, camice con il puntino arancio del marchio, titolo bianco "Ihmisen kokoista huolenpitoa" (cura a misura di persona) e "Varaa aika"; a destra due riquadri: vaccino antinfluenzale (donna con cerotto, cerchio di puntini arancio del logo dietro) e "24 % kokee työuupumusta" (ricerca sul lavoro 2026).
- **Foto e colore:** le foto sono state fatte apposta per il marchio, con fondi rosati e i puntini arancio-rossi del logo dentro l'immagine o sui camici. È il punto più forte di tutta la ricerca: il colore del marchio non sta in un riquadro accanto alla foto, sta nella foto. **Caratteri:** Satoshi 900 per i titoli, Satoshi 500 per il testo. **Colori:** arancio-rosso del logo, rosa cipria #C29F9E nei fondi foto, bianco. **Telefono:** 010 312 010 nei link.
- **Da non riprendere:** le etichette-badge sopra i titoli nei riquadri ("Varaa aika rokotukseen", "Työelämä 2026 -tutkimus"): è un divieto del committente.
- **Da riprendere:** il colore del logo dentro le foto della struttura.

### 1.3 Concentra (USA) - medicina del lavoro
[concentra.com](https://www.concentra.com/). File: `concentra-*`, ritagli `concentra-apertura-foto-e-partner.jpg`, `concentra-datori-e-pazienti.jpg`.
- **Prima schermata:** menu con EMPLOYERS e PATIENTS come prime due voci. Apertura divisa: a sinistra la foto di un operaio con casco ed occhiali che lavora a un motore, "Workforce Health That Works."; a destra un pannello blu "Partner With Us" con un bottone verde.
- **Seconda schermata:** **due colonne affiancate, Employer Resources e Patient Resources**, ognuna con una foto e un elenco di compiti concreti come link: per i datori "trova un centro, scopri gli ambulatori in azienda, crea un account, scarica i moduli, visite per autisti professionisti, test antidroga"; per i pazienti "trova un centro, telemedicina, scarica i moduli, cosa sapere della visita preassuntiva, paga la fattura".
- **Terza:** sei servizi in cerchi con icona (infortuni sul lavoro, fisioterapia, visite, test, viaggi e vaccini, urgenze), storia "dal 1979".
- **Caratteri:** Source Sans Pro. **Colori:** blu #002855, arancio, verde dei bottoni. **Densità:** alta.
- **Da non riprendere:** l'aspetto da portale del 2012 (banner arancio di notizia sopra l'apertura, cerchi con icona, bottoni a filo arancio), il copy di vanto ("A Tradition of Excellence").
- **Da riprendere:** la struttura. È il riferimento più vicino a Lavoro & Salute: le due porte come due elenchi di compiti, uno per l'azienda e uno per la persona, uno accanto all'altro.

### 1.4 Amazon One Medical (USA) - persone e aziende
[onemedical.com](https://www.onemedical.com/) e [/business](https://www.onemedical.com/business/). File: `onemedical-*`, `onemedical-business-*`, ritaglio `onemedical-riga-per-aziende.jpg`.
- **Prima schermata:** menu con "For You" e "For Business". Titolo serif blu "Comprehensive healthcare just got less painful", prezzo dell'abbonamento, un bottone, poi tre righe piccole: condizioni, "Già iscritto?", "Have a company sponsored membership? Click here." A destra una donna al telefono tagliata da un arco blu.
- **Seconda e terza:** tre schede foto (salute mentale, visita annuale, farmacia), titolo grande centrato, sei vantaggi con illustrazioni piatte.
- **Pagina aziende:** stessa grafica, foto di un'infermiera vera con una paziente, "The primary care benefit employees love", poi cinque vantaggi illustrati e "8.500+ organizzazioni".
- **Caratteri:** GT Super Display (serif) e Ginto. **Colori:** verde bosco #005450, crema #F4F4F4, crema caldo.
- **Da non riprendere:** serif display "editoriale", illustrazioni piatte di persone, titolo-slogan.
- **Da riprendere:** la riga piccola ma visibile per l'altro pubblico subito sotto il bottone principale.

### 1.5 Pall Mall Medical (Regno Unito) - poliambulatorio privato
[pallmallmedical.co.uk](https://www.pallmallmedical.co.uk/). File: `pallmall-*`, ritagli `pallmall-telefono-in-testata.jpg`, `pallmall-medici-con-ruolo.jpg`, `pallmall-sedi-con-foto-vera.jpg`.
- **Prima schermata:** in testata "Call Us On 0161 832 2111" in blu, accanto al bottone "Enquire Now"; menu per aree (diagnostica ed esami del sangue, immagini, specialistica). A sinistra su fondo sabbia "Private Healthcare & Diagnostics", due righe di descrizione, quattro voci con spunta; a destra **una foto vera di tre infermiere della struttura** davanti all'insegna arancio delle loro sale.
- **Seconda e terza:** "How can we help you?" con schede foto per area; "Your team of trusted specialists" con ritratti, nome e ruolo sotto ("Medical Director", anni di pratica); "Find a clinic near you" con la **foto vera della facciata di ogni sede**, nome e indirizzo.
- **A 390:** le aree diventano righe con miniatura e barra gialla, i medici righe con foto piccola e nome (vedi `confronto-390-a.jpg`): la lista a telefono più chiara di tutta la ricerca.
- **Caratteri:** Beatrice (grottesco). **Colori:** giallo #FFB81C, sabbia #F0E8E0, verde del bottone.
- **Da non riprendere:** Trustpilot e "Special Offers" (vietati per la comunicazione sanitaria in Italia), la chirurgia estetica in testa, ritratti dei medici con fondi diversi tra loro.
- **Da riprendere:** telefono per intero in testata; ritratti con nome e ruolo; foto della facciata con indirizzo.

### 1.6 Humanitas (Rozzano) - ospedale e poliambulatori
[humanitas.it](https://www.humanitas.it/). File: `humanitas-*`, ritagli `humanitas-prenota-a-domande.jpg`, `humanitas-informazioni-utili.jpg` (scuriti dal velo del popup 5x1000, che si apre su tutte le catture).
- **Prima schermata:** "Benvenuti in Humanitas", "Oltre 50 specialità cliniche e più di 700 medici", e **la prenotazione come quattro domande numerate**: "1. Dove vuoi fare la visita? 2. Cosa vuoi prenotare? 3. Quale orario preferisci? 4. Hai un'assicurazione?" e "Prenota". Sotto, i numeri del gruppo con icona.
- **Seconda e terza:** banner del piano sanitario, poi "Tutte le principali informazioni": prenotazioni, contatti e orari, indicazioni e parcheggi, norme di preparazione agli esami, esami di laboratorio, referti e cartelle cliniche. Poi i racconti dei pazienti a video.
- **Caratteri:** Euclid per i titoli, Inter per il testo. **Colori:** verde #007953, arancio del bottone "Prenota online", bianco; decoro di "Y" colorate.
- **Da non riprendere:** popup all'apertura, numeri di vanto, racconti di pazienti (testimonianze: vietate), banner pubblicitari in mezzo alla home.
- **Da riprendere:** la prenotazione scritta come domande in ordine; il blocco delle informazioni pratiche (preparazione, referti, parcheggio).

### 1.7 Gruppo San Donato
[grupposandonato.it](https://www.grupposandonato.it/). File: `sandonato-*`, ritaglio `sandonato-scorciatoie-ssn-privata.jpg`.
- **Prima schermata:** illustrazione di una città con persone e medici, "Benvenuti in Gruppo San Donato" in Noe Display, ricerca, quattro pillole: VISITA SSN, VISITA PRIVATA, CONVENZIONI, DOTTORI. Un premio "#1" a sinistra.
- **Seconda e terza:** "58 sedi, 9000 medici, 5,8 mln pazienti", "In evidenza" a schede, le sedi per città con miniatura del monumento, Smart Clinic con foto vera della vetrina.
- **Caratteri:** Noe Display (serif a contrasto alto) e Manrope. **Colori:** rosso del marchio, bianco, grigio #F6F6F6.
- **Da non riprendere:** il premio "#1" e i numeri (superlativi), l'illustrazione generica, la foto stock rosa.
- **Da riprendere:** le pillole sotto il titolo che dicono il canale (SSN, privata, convenzioni): per Lavoro & Salute "privata", "convenzioni" (se ce ne sono, da 01) e "per aziende".

### 1.8 Centro Medico Santagostino
[santagostino.it](https://www.santagostino.it/). File: `santagostino-*`.
- **Prima schermata:** "Da 15 anni i **migliori professionisti** della tua zona", tre spunte (Qualità, Accessibilità, Brevi tempi d'attesa), campo "Come possiamo aiutarti?", a destra foto vera di quattro operatori in divisa colorata.
- **Seconda e terza:** notizie, città, "Cosa possiamo fare per te" su fondo blu con schede icona (visite, laboratorio, odontoiatria, day surgery, check up) e un elenco di link a destra.
- **Caratteri:** Source Sans Pro; titolo a pesi misti (leggero e grassetto nella stessa frase). **Colori:** blu #0579AB, arancio del logo per Accedi e Prenota online.
- **Da non riprendere:** il superlativo "migliori professionisti", le spunte generiche, le schede icona con ombra, l'enorme vuoto bianco sotto la ricerca.
- **Da riprendere:** foto vera del personale nella prima schermata; "Prenota online" in arancio pieno sempre in testata, anche a 390.

### 1.9 Medbase (Svizzera) - poliambulatori e salute in azienda
[medbase.ch](https://www.medbase.ch/). File: `medbase-*` (usare la `-schermo`), ritaglio `medbase-oggetti-su-colore.jpg`.
- **Prima schermata:** una griglia 3x2 di quadrati: termometro su arancio pieno, cerotti incrociati su verde pieno, videovisita, due volti, al centro un quadrato blu con "Prenota online un medico o un terapista". "Betriebliche Gesundheit" (salute in azienda) è una voce del menu. A destra tre icone fisse: sedi, appuntamento, buoni.
- **Caratteri:** Palanquin. **Colori:** blu #0069B4, arancio #EA651E, verde.
- **Da non riprendere:** i volti stock a primo piano e il carosello della griglia.
- **Da riprendere:** gli oggetti veri della visita fotografati su un colore pieno. Per Lavoro & Salute vale solo con oggetti della struttura (l'audiometro, lo spirometro, l'ecografo, se ci sono: da 01).

### 1.10 Kry (Svezia, ex Livi nel Regno Unito)
[kry.se](https://www.kry.se/), [livi.co.uk](https://www.livi.co.uk/). File: `kry-*`, `livi-*`, ritaglio `kry-compiti-del-paziente.jpg` (velato dal banner dei cookie).
- **Prima schermata:** "Vi tar hand om dig om 14 minuter" in un grottesco nerissimo verde scuro, tre spunte, due bottoni, a destra un padre che bacia il neonato in una foto notturna tagliata da una curva; sotto, una barra con 34 centri, 14 milioni di visite, 4,9 nell'App Store.
- **Seconda:** "Få hjälp idag": sei righe di compiti (videovisita, rinnovo ricetta, salute mentale, pelle, prenota in un centro, iscriviti), poi pillole per bisogno (donna, uomo, stress, pressione alta, fisioterapia...).
- **Caratteri:** il loro "family" (black 900 nei titoli). **Colori:** verde scuro #1B4349, menta #ECF3ED.
- **Da non riprendere:** voti e numeri, il tempo d'attesa come promessa ("in 14 minuti").
- **Da riprendere:** l'elenco dei compiti scritti come verbi ("prenota", "rinnova", "trova").

### 1.11 Visti e messi da parte
- **CDI Centro Diagnostico Italiano** (`cdi-*`): "Per le aziende" in menu, ma carosello in apertura, nove icone di specialità in fila, "Passione per il cliente, eccellenza clinica" e Trustpilot.
- **SYNLAB Italia** (`synlab-*`): "Servizi per aziende" come scheda in testata (buono), ma famiglia stock sul prato e quattro schede foto stock.
- **Affidea** (`affidea-*`): la foto "Ottobre Rosa" (due donne e nastro rosa su grigio) ha l'aspetto di un'immagine generata; carosello; "Per le aziende" in menu; a 390 una barra fissa in basso con Prestazioni, Prenota, Referti (buona idea).
- **Medicover Polonia** (`medicover-*`): sconti in percentuale, banner, dieci colonne: esempio di cosa non fare.
- **Hirslanden** (`hirslanden-*`): titolo grigio su foto chiara, contrasto debole.
- **Cleveland Clinic** (`cleveland-*`): video in apertura, titolo con lineetta lunga.
- **Parsley Health, Avi Medical, Crossover, Carbon Health, Feelgood, Auxologico, Nuffield Health, HCA UK (ex Roodlane)**: ritratti da modella, viola acceso (Avi), cerchi decorativi vuoti (Crossover), popup newsletter (Auxologico), offerta palestra (Nuffield). Feelgood (medicina del lavoro svedese) apre con un magazziniere in gilet giallo che ride fra gli scaffali (con ogni probabilità stock): il tono, una persona al lavoro e non un medico in posa, è quello giusto per la porta Lavoro.

## 2. Template medici venduti su ThemeForest ed Envato

Classifica "Health & Beauty" di ThemeForest per vendite, letta il 18/10/2026: MediCenter 12,7K vendite, MP 4,8K, Healthflex 4,6K, Medicate 3,7K, MediClinic 2,7K. Avada (il tema più venduto di sempre su ThemeForest) e BeTheme hanno demo mediche. Medicora (Key-Design) è il più recente fra i "trending" della ricerca "medical clinic". Le pagine dei template kit di Envato Elements sono dietro Cloudflare e le loro anteprime non hanno un dominio pubblico: ho usato le demo dei temi WordPress, che sono le stesse impostazioni.

| Template | File | Prima schermata | Caratteri | Prime tre schermate |
|---|---|---|---|---|
| [Avada Health](https://avada.website/health/) | `tpl-avada-health-*` | foto stock (medico anziana con bambina), "Caring For Life" con "For Life" colorato, riquadro azzurro trasparente con orari e telefono | Open Sans, Montserrat | quattro icone in fila, "Meet our doctors" a tre ritratti stock |
| [MediCenter](https://quanticalabs.com/wp_themes/medicenter/home/) | `tpl-medicenter-*` | donna stock a braccia aperte su cielo, slider, **tre box sovrapposti: emergenza, orari dei medici, orari di apertura** | Open Sans, Source Sans Pro, PT Serif | servizi a icone, medici, notizie |
| [MediClinic](https://mediclinic.qodeinteractive.com/) | `tpl-mediclinic-*` | slider, **tre box colorati: emergenza con telefono, orari dei medici, orari** | Open Sans, Poppins, Heebo | medici stock scontornati, griglia di specialità a icone |
| [Healthflex](https://healthflex.plethorathemes.com/) | `tpl-healthflex-*` | medico stock, riquadro grigio trasparente "QUALITY CARE / Your Health is our priority", **quattro box blu con illustrazione** | Lato, Raleway | testo, reparti in miniatura, servizi a icone con orari |
| [Medicora](https://sites.keydesign.xyz/medical-clinic/) (2025-26) | `tpl-medicora-*` | foto stock di due medici al monitor, etichetta "TRUSTED HEALTHCARE" sopra il titolo, **tre box: emergenza 24/7, sedi, orari** | Inter Tight, Helvetica | foto radiografia, "Experienced medical professionals", sei schede servizi a icone |
| [Medicate](https://medicate.peacefulqode.co.in/) | `tpl-medicate-*` | etichetta "GREAT EXPERIENCE IN BULDING" (con il refuso) sopra "Orthopedic Treatment Accute Pain", testo lorem, foto stock; a 390 la demo dà errore | Quicksand, Montserrat | |
| [BeTheme Clinic](https://themes.muffingroup.com/be/clinic/) e [Medic](https://themes.muffingroup.com/be/medic2/) | `tpl-be-clinic-*`, `tpl-be-medic2-*` | dottoressa stock sorridente su blu con riquadri bianchi e verdi; medico anziano stock con "01" gigante | Roboto, Exo, Quattrocento | |

Cosa hanno in comune (`confronto-template.jpg`):
- **lo stesso schema in sei su sette:** foto stock a tutta larghezza con titolo-slogan a sinistra, e tre box sovrapposti al bordo basso con emergenza, orari e telefono. È "tre box con icona in fila" più "foto a tutta larghezza con titolo sopra": due voci della lista K6;
- titoli-slogan intercambiabili ("Caring For Life", "Quality medical care you deserve", "Dedication And Commitment", "Your Health is our priority"); etichette sopra il titolo (Medicora, Medicate); parola del titolo in colore (Avada); azzurro ospedaliero e bianco;
- icone ovunque (servizi, reparti, vantaggi), medici stock scontornati in camice, slider in apertura;
- **nessuno ha due ingressi o due pubblici.** Ho cercato anche fra i temi "split screen" più venduti (Manon, Moose, Any): sono portfolio, nessuno è medico. La home a due porte non è un'impostazione da template: è una scelta di Lavoro & Salute, e va difesa come tale.
- **L'unica cosa giusta che hanno:** orari e telefono nella prima schermata. Il contenuto va ripreso, la forma (tre box sopra la foto) no.

## 3. Home a due porte fatte bene

| Sito | File | Come mostra i due pubblici |
|---|---|---|
| [Satispay](https://www.satispay.com/it-it/) | `porte-satispay-*`, ritaglio `satispay-interruttore-privati-negozi.jpg` | interruttore a tre posizioni al centro della testata: **Privati / Welfare / Negozi**; la pagina sotto cambia tutta. Arancio pieno #FF3D00, Bricolage Grotesque 800 e Inter. |
| [Monzo](https://monzo.com/) | `porte-monzo-*`, ritaglio `monzo-personale-business.jpg` | accanto al logo due schede con icona: **Personal / Business**; apertura con una foto vera in un riquadro arrotondato. MonzoSans. |
| [Wise](https://wise.com/it/) | `porte-wise-*` | Personale / Business come prime voci del menu; apertura con il calcolatore vero dell'operazione al posto della foto. Wise Sans 900 maiuscolo, verde #9FE870. |
| [Benenden Health](https://www.benenden.co.uk/) | `porte-benenden-*`, ritaglio `benenden-tre-ingressi.jpg` | sotto la foto, tre ingressi della stessa misura: **"Private healthcare for me" / "Healthcare for my business" / "Existing members"**, ognuno con due righe e un bottone. È sanità privata britannica, il caso più vicino per tipo di cliente. |
| [Octopus Energy](https://octopus.energy/) | `porte-octopus-*` | una porta principale (casa, con il campo del CAP) e sotto il bottone una riga: "Looking to switch your business? Get a quote". |
| Terveystalo, Pihlajalinna | sezione 1 | riga di pubblici sopra la testata; la seconda porta torna più in basso come fascia a metà (Terveystalo). |
| Concentra | sezione 1 | EMPLOYERS e PATIENTS prime voci del menu; due colonne di compiti nella seconda schermata. |
| One Medical | sezione 1 | "For You" e "For Business" nel menu, riga "company sponsored membership" sotto il bottone. |

Cosa insegnano:
1. **Nessun sito grande usa lo schermo diviso a tutta altezza** con una parola per metà. Chi ha due pubblici usa tre forme: un interruttore in testata (Satispay, Monzo, Terveystalo, Pihlajalinna), ingressi affiancati della stessa misura subito sotto l'apertura (Benenden, Concentra), oppure una porta principale e una riga per l'altra (Octopus, One Medical).
2. **Ogni porta dice chi sei e cosa puoi fare**, in frasi da persona ("Healthcare for my business", "Patient Resources: find a center, schedule a visit, pay your bill"), non con una parola sola.
3. **L'interruttore resta** quando sei entrato: da Privati passi a Negozi senza tornare indietro.
Per Lavoro & Salute la richiesta del committente (aprire con le due sezioni) è compatibile con tutto questo: le due porte stanno nella prima schermata, ma ognuna è piena di informazioni utili, e dopo l'ingresso l'interruttore Lavoro | Salute resta in testata.

## 4. Conclusioni

### Gesti da riprendere

1. **Le due porte come due elenchi di compiti, non come due parole su due foto.** Porta Lavoro (per le aziende): le cose che un datore di lavoro chiede, scritte come verbi, prese dal sito attuale (medico competente, sorveglianza sanitaria, corsi di formazione, consulenza D.Lgs 81/2008: l'elenco preciso da 01). Porta Salute (per le persone): le specialità e la diagnostica che risultano in 01, e come prenotare. Da `ritagli/concentra-datori-e-pazienti.jpg`, `ritagli/benenden-tre-ingressi.jpg`, `ritagli/kry-compiti-del-paziente.jpg`.
2. **L'interruttore Lavoro | Salute fisso in testata** dopo l'ingresso, con la porta attiva evidenziata e l'altra a un tocco. Da `ritagli/satispay-interruttore-privati-negozi.jpg`, `ritagli/monzo-personale-business.jpg`, `ritagli/terveystalo-due-pubblici-e-scorciatoie.jpg`.
3. **I due colori del logo come colori delle due porte, pieni e dentro le foto.** Il logo di Lavoro & Salute ha già l'arancio-rosso (LAVORO) e il blu (SALUTE) e il sito attuale li assegna ai due bottoni. Come Pihlajalinna mette i puntini del logo sui camici e nei fondi delle foto, il nuovo sito porta l'arancio in tutta la parte Lavoro e il blu in tutta la parte Salute, a campi pieni, senza veli scuri e senza sfumature tra i due. I valori esatti si misurano sul logo in 01. Da `ritagli/pihlajalinna-colore-del-marchio-nelle-foto.jpg` e `00-sito-attuale-1440-schermo.png`.
4. **Telefono scritto per intero e toccabile in testata**, e sotto il bottone di prenotazione ("oppure chiamate lo ..."). Un poliambulatorio su appuntamento si prenota soprattutto per telefono. Da `ritagli/pallmall-telefono-in-testata.jpg` e `avi-1440-schermo.png` ("Lieber telefonisch?" sotto il bottone).
5. **Scorciatoie per i compiti frequenti sotto ogni porta:** per le persone "Prenota una visita", "Orari", "Come arrivare a Limena", "Referti" (se il servizio c'è); per le aziende "Chiedi un preventivo", "Calendario dei corsi" (se c'è in 01). Da `ritagli/terveystalo-due-pubblici-e-scorciatoie.jpg` e `ritagli/sandonato-scorciatoie-ssn-privata.jpg`.
6. **La seconda porta che ritorna più in basso come fascia a metà**, con titolo grande nel suo colore e una foto vera di lavoro accanto: chi è entrato per una visita scopre che Lavoro & Salute fa anche la medicina del lavoro per la sua azienda, e viceversa. Da `ritagli/terveystalo-fascia-tyoterveys-meta.jpg`.
7. **Medici con ritratto, nome, ruolo e specialità**, con lo stesso fondo e la stessa luce, e a 390 come righe con foto piccola. Solo con i nomi che risultano in 01 e con foto vere. Da `ritagli/pallmall-medici-con-ruolo.jpg` e `confronto-390-a.jpg`.
8. **La sede vera e le informazioni pratiche:** foto della facciata di Via S. Felice e Fortunato 26, indirizzo, orari, parcheggio, cosa portare alla visita, preparazione agli esami. Da `ritagli/pallmall-sedi-con-foto-vera.jpg` e `ritagli/humanitas-informazioni-utili.jpg`.

### Errori da evitare

1. **Foto a tutta larghezza con slogan e tre box sovrapposti** (emergenza, orari, telefono): è l'impianto di sei template su sette (`confronto-template.jpg`, `tpl-medicenter-foglio.jpg`, `tpl-medicora-foglio.jpg`). Orari e telefono sì, ma dentro le porte.
2. **Schermo diviso con una parola per metà e un bottone a filo, senza altre informazioni:** è l'anteprima Netlify (`00-anteprima-netlify-1440-schermo.png`) e, in altra forma, il sito attuale. Nessun riferimento vero lo fa; regge con il nome di chiunque (K1 e K3 bassi).
3. **Serif display e corsivo "eleganti":** Fraunces e "Da che parte cominciamo?" nell'anteprima, GT Super Display di One Medical, Teodor di Parsley. È il lusso generico già bocciato (divieto del serif corsivo). I siti di sanità europei migliori (Terveystalo, Pihlajalinna, Kry, Monzo, Satispay come porte) usano un grottesco pieno e nero nei titoli.
4. **Velo scuro sulle foto per leggerci sopra il testo:** anteprima Netlify (ruggine e blu notte), Healthflex, Hirslanden (titolo grigio su foto chiara). Testo grigio su grigio, contrasto basso, foto spente.
5. **Foto stock o generate al posto della struttura:** il saldatore e la reception di vetro dell'anteprima, la famiglia sul prato di Synlab, le modelle di Parsley, il nastro rosa di Affidea che sembra generato, i medici scontornati dei template. La porta Lavoro scalda con una persona vera al lavoro (il tono di Feelgood, `feelgood-1440-schermo.png`, ma con foto vere), meglio se in un'azienda cliente e con il suo consenso; finché mancano, segnaposto dichiarato.
6. **Vanto, numeri e superlativi:** "i migliori professionisti" (Santagostino), premio "#1" e "9000 medici" (San Donato), "eccellenza clinica" e Trustpilot (CDI, Pall Mall), voti dell'App Store e "in 14 minuti" (Kry), offerte e sconti (Pall Mall, Medicover). Nella comunicazione sanitaria italiana non si fanno (vedi 03-norme). Al loro posto: dal 2006, l'indirizzo, cosa si fa, come si prenota.
7. **Popup, banner e caroselli sopra l'apertura:** 5x1000 di Humanitas, newsletter di Auxologico, banner di notizia di Concentra, caroselli di CDI, Affidea, MediClinic, Medbase.
8. **Icone per ogni servizio:** nove icone di CDI, sei cerchi di Concentra, illustrazioni di Healthflex e One Medical, schede icona di Santagostino. Le specialità si scrivono come elenco leggibile, al più con la foto vera della stanza o dello strumento.
