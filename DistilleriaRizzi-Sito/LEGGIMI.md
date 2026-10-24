# Distilleria Rizzi: proposta di nuova home

Proposta non richiesta, preparata il 24/10/2026, che riguarda solo la home. L'azienda non è stata contattata e non è stato inviato nulla.

## Dove sono le cose

- `sito/index.html`: la home finale, "L'etichetta in piano". È statica e si apre con file:///.
- `sito/img/`: solo le immagini usate, in WebP con alfa per le bottiglie e in JPEG per le foto, in più larghezze.
- `sito/fonts/`: Zodiak e Switzer in woff2 dai pacchetti completi Fontshare, con il testo della licenza ITF FFL.
- `screenshot/home/`: home-1440.jpg, home-1440-prima-schermata.jpg, home-390.jpg, home-390-prima-schermata.jpg, chiusura-1440.jpg e NOTA.md, che descrive idea, caratteri, colori, interazione, foto e controlli.
- `_prova/script/build_finale.sh`: rifà tutto (immagini con `finale_img.py`, caratteri, pagina da `finale_pagina.html`, screenshot con `shot_finale.mjs`).
- `_prova/home/a` e `_prova/home/b`: i due prototipi. Il giudice ha scelto A.
- `01-analisi.md`: i fatti con le fonti. `assets/CREDITI.md`: origine e licenza di ogni immagine.

## Dati da confermare con l'azienda

- **Fondazione**: in pagina c'è il 15/12/1926 (LinkedIn e la loro home), con il "1850" spiegato come anno del marchio Genzial acquistato nel 1945. Va confermato, insieme alla festa del centenario del 15/12/2026 con mostra, assaggi e visite.
- **Titolari**: in pagina ci sono solo i nomi, Maddalena e Alessandro, come nella loro home. Va chiesto se vogliono anche i cognomi (Varotto e Belluco, dall'articolo de La Difesa del Popolo).
- **"Distilleria" senza distillazione**: oggi non distillano. La pagina dice "liquori, amari e aromi" e "infusi, alcolati e sciroppi", mai "distilliamo". Il nome resta.
- **Felsina, Fernet e Garofano**: non hanno una scheda. I gradi (21°, 45°, 21°) vengono dalla pagina `coloriesaporidiprimavera2024`, e "tra i più amati per il dopo pasto" e il Garofano nel vin brulè vengono dall'articolo `due-cuori-e-un-distillato`. Il formato non è indicato. Va confermato che i sei prodotti siano tutti in vendita oggi.
- **Alchermes**: la bottiglia fotografata è il liquore ("gradi 30" in etichetta), non l'aroma a 70° della linea pasticceria. Per questo la didascalia non dà il grado. Per il sito vero serve la foto del formato da laboratorio.
- **16.540 bottiglie dal 14 dicembre 2022**: è il numero del contatore della loro home al 24/10/2026. Va aggiornato con un numero vero o tolto.
- **Spaccio**: in pagina c'è "chiamaci per sapere quando passare", come nei loro Contatti. Il blog del 2024 e la pagina della Festa del Papà 2025 danno orari diversi: se lo spaccio ha orari fissi, vanno scritti.
- **Ricettari e strumenti del fondatore in vetrina nello spaccio**: vengono dall'articolo del 2025. Va confermato che siano ancora esposti.
- **Clienti**: nella home non ne ho nominato nessuno. Se vogliono citare le pasticcerie e i distributori, serve il loro permesso.
- **Dati societari**: REA, capitale sociale e anno di costituzione della srl non sono pubblici e non sono in pagina. Il capitale "11.0 K €" viene solo da Atoka: va verificato in visura prima di mostrarlo.
- **Etichette per terzi** (sambuco, Enoteca Manchiero): non sono in home. Va chiesto se è un servizio da offrire.
- **Negozio online**: hanno un WooCommerce vuoto. Se vogliono vendere online, la vendita di alcolici a distanza ha obblighi propri (età, accise, spedizione).

## Avvertenze da aggiungere nel sito vero

- Va aggiunta una riga sul consumo responsabile e sulla vendita ai soli maggiorenni, nel piede o vicino ai prodotti, ed eventualmente un controllo d'età all'ingresso se ci sarà il negozio online.
- Privacy e Cookie oggi non esistono (404): vanno scritte prima di andare online, e serve un banner dei cookie se ci saranno statistiche o mappe incorporate.

## Pagine che il sito nuovo deve avere (linkate dalla home)

- Liquori e amari, `/liquori-e-amari/`: aperitivi, punch, liquori e amari, con una scheda per prodotto.
- Per la pasticceria, `/pasticceria/`: il catalogo dei 40 e oltre aromi e ingredienti, la Vodka 70° e i formati.
- Sciroppi per granite, `/sciroppi-per-granite/`.
- La storia 1926-2026, `/storia/`: il centenario, la mostra, i ricettari.
- Spaccio e orari, `/spaccio/`.
- Notizie, `/notizie/`: oggi è il blog con 5 articoli.
- Contatti: per ora è l'ancora `#contatti` della home. Se serve si fa una pagina propria.
- Privacy, `/privacy/`, e Cookie, `/cookie/`.
- Social del piede: Instagram, Facebook e LinkedIn (indirizzi verificati in 01-analisi.md, sez. 8). Non esiste un canale YouTube.

## Newsletter

Il modulo "Lettere dalla distilleria" nel piede (email, bottone e casella del consenso) **non invia nulla** finché non viene collegato a un servizio come Brevo o Mailchimp, con il doppio consenso: email di conferma e registro dei consensi. Il link "Ricevi l'invito per email" del centenario porta a questo modulo. Ha senso perché ci sono il centenario, i cofanetti delle feste, le fiere e i clienti privati dello spaccio. L'informativa privacy deve citare la newsletter.

## Foto da rifare dal vero

Il materiale di oggi vale circa 4 su 10. Le bottiglie scontornate del 2024 reggono la proposta, ma sono foto da telefono con nitidezza spinta e luce piatta.

1. **Le sei etichette di casa, più l'Alchermes**: mezza giornata di still life in studio. Ogni bottiglia piena va fotografata da sola, dritta e frontale, su un fondale di carta color avorio (vicino a #F3EEE6). La luce è una sola, morbida, grande, da sinistra (bank o finestra con diffusore), con un pannello bianco a destra. Serve un polarizzatore per togliere i riflessi sul vetro e sull'etichetta. Obiettivo da 90-100 mm a f/11, file a 6000 px o più. Si tiene la stessa distanza per tutte, così le altezze restano in scala vera (il Pinalpe da 75 cl più basso). Le foto sostituiscono `assets/originali/2024-02-*.png` e `2023-02-bott-alchermes.png`, e le ombre si rifanno in ripresa invece che con PIL.
2. **Spezie del Garofano**: chiodi di garofano, cannella, scorze d'agrumi e mele vere, sul piano del loro laboratorio o su carta, dall'alto e con la stessa luce morbida. Sostituisce la foto Pexels di Kunuk. Taglio orizzontale largo (18:7).
3. **Chiusura**: un bicchierino del loro Felsina o Garofano nel sole radente della finestra dello spaccio, oppure la vetrina con i ricettari del fondatore. Sostituisce la foto Pexels di Reding. Formato orizzontale 4:3 o 3:2.
4. **Facoltative per le altre pagine**: le mani di Maddalena e Alessandro su alcolati e infusi in laboratorio, i ricettari aperti, la sede in via Negri di giorno (al posto della schermata di Street View).

## Licenze

- **Caratteri**: Zodiak e Switzer sono di Indian Type Foundry, distribuiti da Fontshare con la ITF Free Font License 2.0, che consente l'uso commerciale gratuito anche in self-hosting. Il testo è in `sito/fonts/LICENZA-ITF-FFL.txt`. I file sono quelli del pacchetto completo, non modificati.
- **Foto Pexels** (licenza Pexels: uso gratuito anche commerciale, attribuzione non obbligatoria): Sedanur Kunuk, spezie (30004632), e Mathias Reding, bottiglia e bicchierini nel raggio di sole (11560692). Sono segnaposto d'atmosfera: nessuna mostra un prodotto Rizzi o marchi di terzi.
- **Foto e grafiche dell'azienda**: bottiglie e logo vengono dalla libreria media del loro sito. Per il sito vero vanno chiesti gli originali e confermati i diritti.

## Loghi

- Non esiste un logo vettoriale pubblico. In pagina ci sono due PNG ricolorati in inchiostro #1C1815: la scritta a pennello nella testata (da `logo-distilleria-rizzi-scritta-1286x168.png`) e il logo completo con calice e scritta nel piede (da `logo-distilleria-rizzi-nero-1500x300.png`, a 720 px, mostrato a 300 px).
- La scritta è un tratto a pennello irregolare e non si ricostruisce a mano in SVG in modo fedele. Va chiesto il file originale a chi ha disegnato il logo, oppure si vettorializza con un tracciamento automatico (potrace) e lo si fa approvare a loro.
- Il vecchio marchio col leone ("casa fondata nel 1850") esiste solo a 392 px e non è usato.
