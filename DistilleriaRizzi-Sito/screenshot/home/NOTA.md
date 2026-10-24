# Distilleria Rizzi, nuova home: "L'etichetta in piano" (versione finale)

Pagina: `sito/index.html`, statica, si apre con file:///. Immagini in `sito/img/` (solo quelle usate, WebP e JPEG in più larghezze), caratteri in `sito/fonts/`. Tutto si rifà con `sh _prova/script/build_finale.sh` (immagini, caratteri, pagina, screenshot). Alta 5039 px a 1440 (piede compreso), 6026 px a 390.

## Idea

Su un fondo color carta c'è una sola bottiglia vera di Rizzi, ritta su un filo sottile che attraversa la pagina come il piano di un tavolo d'archivio. Le legende leggono l'etichetta storica: lo scudo RIZZI, le medaglie, "Industria liquori F.lli Rizzi, Padova". Il patrimonio di Rizzi sono le sei etichette di casa, non un alambicco che oggi non c'è più. Con il nome di un concorrente la pagina non regge, perché le etichette sono solo loro.

## Prime due schermate

1. **Apertura.** In alto la testata chiara con il logo a pennello, quattro voci e il telefono. A sinistra c'è il titolo "Liquori e amari dal 1926" (Zodiak 300, 124 px, tre righe) con due righe sul mestiere. Sotto, dopo circa 150 px d'aria, vengono i sei nomi in griglia 3x2 a 27 px, con il grado accanto. Sotto ancora c'è la riga con grado, uso e formato presi dalle schede, appoggiata al filo del piano. A destra la Felsina è alta 755 px e ha la base esattamente sul filo, con ombra portata e ombra di contatto. Accanto ha tre legende sottili, con il numero in Zodiak e il testo nell'inchiostro a 15 px. Il "Tav. 1 di 6" del prototipo è stato tolto.
   A 390 la schermata è stata rifatta. Il titolo sta a tutta larghezza (54 px, tre righe). Sotto ci sono due colonne: a sinistra i sei nomi in colonna a 22 px, ognuno con un'area di tocco di 44 px, a destra la bottiglia alta circa 400 px. Seguono il filo con la riga del grado a tutta larghezza e poi il paragrafo, anche lui a tutta larghezza. Nella prima schermata si vedono il titolo, la bottiglia intera e tutti e sei i nomi, senza colonne strette né metà vuote.
2. **Pasticceria.** Il titolo "Oltre 40 aromi e ingredienti per la pasticceria" non ha più l'etichetta sopra. L'Alchermes con la dama è alto 620 px, con l'arancio riportato al naturale e la stessa luce e la stessa ombra della Felsina. Seguono tre righe a filetto (sciroppi di zucchero, aromi alcolici a 70°, creme e vini). La Vodka 70° è una nota piccola con tutti i formati. Chiudono la sezione due link.

Poi vengono le spezie del Garofano in una fascia di 1440x560, su fondo riportato verso la carta, con "Facciamo tutto noi, dall'inizio alla fine", i ricettari del fondatore in vetrina e le 16.540 bottiglie. Segue il centenario su campo rosso: le due date grandi, il testo e la cronologia a 17 px, filetti al 30 % della carta e il link all'iscrizione nel piede. Dopo c'è la chiusura e in fondo il piede.

## Chiusura e piede

- Chiusura "b con foto": il testo sta a sinistra (5/12) e la foto a destra arriva al bordo (7/12), alta quanto il blocco di testo. La frase è la loro: "Dal nostro laboratorio al tuo bicchiere, senza tappe inutili" (pagina `spritz`). Il telefono è in Zodiak a 48 px con tel:, poi vengono l'email con mailto:, l'indirizzo con "Apri la mappa" e gli orari dell'ufficio dalla pagina Contatti, con la riga sullo spaccio. La foto mostra due bicchierini e una bottiglia nel raggio di sole e illustra "al tuo bicchiere". Non è la stessa foto della sezione sopra e non è usata in nessun'altra home della campagna.
- Piede: logo completo con calice e scritta, ricolorato in inchiostro (PNG a 720 px, mostrato a 300 px, quindi 2,4x), con una riga su chi sono. Le colonne sono Prodotti, Distilleria e Seguici (solo Instagram, Facebook e LinkedIn, che esistono davvero, scritti a parole). C'è la newsletter "Lettere dalla distilleria" con email, bottone e casella del consenso. Ha senso perché ci sono il centenario, i cofanetti delle feste, le fiere e i clienti privati dello spaccio. In fondo la riga legale: ragione sociale, indirizzo, P.IVA, PEC, Privacy e Cookie. REA e capitale non ci sono, perché non sono pubblici. A 768 e 390 le colonne si impilano in ordine.

## Caratteri e colori

- **Zodiak** 300 e 400 (Indian Type Foundry, Fontshare) per titoli, nomi delle etichette, anni, numeri delle legende e telefono. È un serif dritto ad alto contrasto, mai corsivo, che ricorda le lettere dello scudo RIZZI. Riferimenti: Fernet-Branca (la bottiglia storica accanto a un titolo grande e sicuro) e Marzadro (bianco e serif), qui senza effetti.
- **Switzer** 400 e 500 (stessa fonderia) per testi, legende e piede. Il difetto del prototipo ("ricett e", "scritt e") veniva dal file ridotto delle API Fontshare. Ora la pagina usa i woff2 del pacchetto completo (download del 23/10/2026), con la crenatura giusta. Controllato a 1440 e a 390 su "ricette", "scritte", "delicato", "quattro" ed "etichette". Le cifre di Switzer sono tabellari di serie (larghezza unica): gradi, orari, P.IVA e formati sono incolonnati.
- Licenza: ITF Free Font License 2.0, uso commerciale gratuito anche in self-hosting. Il testo è in `sito/fonts/LICENZA-ITF-FFL.txt`.
- Colori: carta #F3EEE6, inchiostro #1C1815 (15,3:1), grigio testi #5B524A (6,6:1 sulla carta, 6,2:1 sul piede #ECE6DC), rosso etichetta #B8231C solo per il nome scelto, il campo del centenario (carta su rosso 5,5:1) e il passaggio sui link. Il segnaposto del campo email è #6F665E (4,5:1).

## Interazione (un solo gesto)

I sei nomi formano un gruppo di scelta (role radio). Si usano il tocco, il clic, le frecce, Home e Fine; il fuoco si vede con un contorno rosso. Al cambio la bottiglia si scambia di netto, senza dissolvenza: le immagini sono precaricate. Cambiano anche le tre legende e la riga con grado, uso e formato. Le uniche transizioni, di 0,12 s, riguardano il colore dei nomi e del bottone della newsletter. Non ci sono animazioni allo scorrere né effetti sul cursore. Sotto i 1000 px le legende spariscono e resta la riga dei dati. Il menu a 1000 px e sotto è un vero bottone con aria-expanded, e da telefono contiene anche il numero da chiamare.

## Foto, origine e licenza

- Bottiglie Felsina, Fernet, Garofano, Pinalpe, Prugna e Punch Arancio (`assets/originali/2024-02-*.png`) e Alchermes (`2023-02-bott-alchermes.png`): sono di Distilleria Rizzi, dalla libreria media del loro sito. Le ho scontornate di nuovo (bordo stretto di 1-2 px), ammorbidite appena e messe su una tela fissa 1000x2000 con la stessa luce e la stessa ombra. All'Alchermes ho riportato la saturazione al 74 %. Sono esportate in WebP a 480, 760 e 1000 px. I diritti sono da confermare con l'azienda.
- Spezie: Sedanur Kunuk, Pexels, licenza Pexels (https://www.pexels.com/photo/culinary-spices-and-orange-slices-on-white-background-30004632/). Taglio 18:7, fondale bilanciato verso la carta, srcset 800, 1200 e 1600.
- Chiusura: Mathias Reding, Pexels, licenza Pexels (https://www.pexels.com/photo/bottle-and-drinking-glasses-with-alcohol-11560692/). Taglio sui bicchieri e sulla bottiglia, scaldata, con le ombre sollevate sul lato del testo; srcset 800, 1200 e 1840.
- Logo: PNG ricolorati in inchiostro, cioè la scritta a pennello nella testata e calice più scritta nel piede. Non li ho ricostruiti in SVG perché il tratto a pennello non si rifà in modo fedele.
- Nessuna immagine è generata dall'IA e nessuna mostra marchi di terzi. Le foto Pexels sono state cercate per ID in tutti i `*-Sito/assets/CREDITI.md`: compaiono solo qui.

## Controlli

- Screenshot a 1440, 390, 320, 768, 1024 e 1920, guardati a pezzi. Nessuno scorrimento orizzontale (scrollWidth uguale alla larghezza a tutte le misure) e nessuna sovrapposizione. A 1024 e 768 la bottiglia non copre più testo, nomi e riga dei dati (corretto in questo giro). Provato anche il gesto da tastiera a 1440 (Garofano e Pinalpe) e al tocco a 390 (Prugna), più il menu aperto a 390.
- Altezza a 1440: 5039 px, dentro la forbice 5000-5600.
- Carattere U+2014: nessuno in pagina, negli script e in questa nota.
- Segnali da IA: nessun carattere delle liste, niente Inter, niente gradiente, niente emoji, nessuna etichetta sopra i titoli, nessuna card, nessuna icona Lucide, niente dissolvenze allo scorrere, nessun effetto sul cursore. `segnali.sh` sulla pagina finale passa 17 soglie su 18. Resta fuori l'area coperta da foto: 29,6 % contro un minimo del 35 %. È una scelta voluta, non una svista. Il giudice ha chiesto di ridurre l'Alchermes e le spezie perché non facciano concorrenza al "solo oggetto". Lo strumento conta solo in parte le bottiglie scontornate, che sono oggetti su carta e non foto in riquadro. Non ho aggiunto altre immagini per alzare la percentuale.
