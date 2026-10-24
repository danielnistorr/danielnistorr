# Home finale di Stefano Aiti, "Comunicazione silenziosa"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con PIL, pagina dal modello `_prova/script/finale_index.html`, screenshot e controlli con `_prova/script/finale_shoot.mjs`).

Misure: 5534 px a 1440 piede compreso, 5515 px a 390. Base: il prototipo A, con tutte le indicazioni del giudice.

## L'idea

La pagina è il fondale dello studio. Il filetto grigio del logo attraversa la prima schermata da bordo a bordo, come l'orizzonte di un limbo. Sopra posa un oggetto fotografato da Stefano Aiti, grande e nitido, con la base appoggiata sulla linea.

Il titolo è una sua frase: "Le foto sono comunicazione silenziosa" (sa.com/about). La chiusura è l'altra metà della stessa frase: "È il passaparola della qualità a creare il gran rumore".

Con il nome di un altro fotografo la pagina non regge, perché gli oggetti sono suoi scatti per i suoi clienti e l'indice sotto l'orizzonte porta i loro nomi.

## Prime due schermate

1. **Apertura, 1440x900.** Fondo carta chiaro.
   - A sinistra il titolo da 104 px (Switzer 500), con subito sotto, a 44 px, una riga su chi è e cosa fa e due link sottolineati: telefono e email. Il bottone nero pieno non c'è più.
   - A destra l'antenna Calearo, larga il 58 % della pagina e alta quanto lo spazio sopra il filetto, con la base sulla linea.
   - Sotto l'orizzonte c'è l'indice: "Still life su fondo bianco", poi Calearo, Marijke, Superoro, Pianegonda, Lago, e a destra la didascalia "Calearo, antenna 1/5".
   - **A 390** la testata ha il logo, "Chiama" (tel:) e "Menu". Seguono il titolo su tre righe, l'oggetto intero a tutta larghezza e posato sul filetto, l'indice su una riga sola (cinque nomi a 15 px) e la didascalia. Sotto la prima schermata vengono il testo e i due link.
   - Per il telefono ci sono tagli propri, con l'oggetto pieno: a 390 l'anello Pianegonda non resta piccolo in mezzo al vuoto.
2. **Architettura e contract.**
   - Titolo e una frase: "Banche e casse rurali arredate da Artufficio, le scale in marmo di Studio 4 Marmicolor, la Fornace Morandi", più la laurea allo Iuav.
   - Poi la parete curva della Banca Prealpi a tutta larghezza, in 2:1. A 390 è un taglio verticale con la donna che passa.
   - Sotto, la coppia quadrata della stessa altezza: la scala a chiocciola in marmo e la ciminiera della Fornace Morandi.
   - La fascia sfocata della scala e l'oblò di Brendola sono stati tolti.

Il resto della pagina:
- Industria e cantieri: lo Scania all'alba a tutta larghezza, con il titolo sulla foto. Sotto, una colonna sola di 640 px con la frase dei servizi e la sua citazione sull'attrezzatura.
- Per aziende orgogliose di ciò che fanno: i clienti composti come testo grande, poi 1995, 2008 e le due lauree.
- La chiusura con foto.
- Il piede.

## Caratteri e colori

- **Switzer** (Indian Type Foundry, da Fontshare), pesi 400 e 500, una sola famiglia per tutta la pagina.
  - Titoli in 500 con spaziatura da -0,03 a -0,042em; testo in 400 a 18-19 px; didascalie a 14 px con cifre tabellari.
  - Titoletti del piede a 12 px in maiuscolo spaziato (0,16em): riprendono le lettere "STUDIO" del logo.
  - Riferimenti: il grottesco neutro e preciso di Hélène Binet (Neue Haas Grotesk) e di Marco Cappelletti (Styrene).
- **Licenza**: ITF Free Font License (Fontshare la indica come `itf_ffl`), gratuita anche per uso commerciale. I file woff2 sono serviti dalla pagina, da `sito/fonts/`. Prima della messa online va riletto il testo della licenza sul punto dell'incorporazione nel sito.
- **Colori**:
  - carta #F6F5F2: il fondo di tutta la pagina e degli still life;
  - inchiostro #141414 (17:1);
  - grigio dei testi secondari e del piede #5C5F5E (6,1:1 sulla carta, AA);
  - grigio del logo #A9ADAC, solo per i filetti.
  - Nessun colore d'accento: il colore viene dalle foto (oro rosa, legno, mattone, cielo, asfalto).

## Interazione

Un solo gesto, quello del fotografo: cambiare l'oggetto sul fondale.
- I cinque nomi sotto l'orizzonte sono bottoni veri con `aria-pressed`. Al clic o al tocco cambiano l'oggetto e la didascalia (per esempio "Pianegonda, anello in argento 4/5"), con un cambio netto e senza dissolvenza.
- Con la tastiera: Tab arriva ai nomi, le frecce destra e sinistra li scorrono in giro, e la didascalia è `aria-live`.
- Le altre foto dell'indice si scaricano solo quando il dito o il puntatore si avvicinano all'indice.
- L'unica transizione è il colore dei link al passaggio (0,15 s). Nessuna animazione allo scorrere, niente che segua il cursore.
- A 768 e 390 il menu si apre con un bottone "Menu" / "Chiudi".

## Foto, origine e licenza

Sono tutte fotografie di Stefano Aiti, prese dal portfolio di stefanoaiti.com e da aitistudio.it. L'autore è lui; i soggetti sono dei suoi clienti, e i diritti d'uso vanno confermati (vedi LEGGIMI). Nessuna foto di repertorio e nessuna immagine generata.

Sono lavorate con PIL (`_prova/script/finale_img.py`) ed esportate in 2-4 larghezze per `srcset`:
- **apertura**, cinque still life (id dell'inventario 202, 641, 830, 748, 547).
  - I bianchi sono portati a 255 con i livelli e moltiplicati sul colore carta, così non c'è nessun riquadro. Il taglio è 7:6 con l'oggetto appoggiato in basso.
  - Ci sono due tagli: largo, con margini propri per stare lontano dal titolo, e stretto per telefono e tablet.
  - Il vaso Marijke ha il fondo grigio chiaro, sfumato nella carta.
  - L'antenna Calearo, nel file web, è uno scontorno su bianco puro senza ombra (misurato: dopo la base i pixel sono tutti a 255). L'ombra di contatto quindi non c'è e non l'ho disegnata: a fare da appoggio è il filetto. Va chiesto l'originale con l'ombra (vedi LEGGIMI).
- **architettura**: Banca Prealpi (13, largo 2:1 e verticale 4:5), scala Studio 4 Marmicolor (819, quadrata), Fornace Morandi (195, quadrata).
- **cantiere**: Salima, Scania all'alba (a3), con la saturazione all'82 % e il contrasto al 96 % per calmare l'HDR.
- **chiusura**: la ciotola d'argento di Calegaro al sole radente (220), in 16:10, schiarita del 4 % e un filo meno fredda. Chiude con uno still life come l'apertura. Non compare in nessun'altra parte della pagina né in altre home della campagna.

I segnaposto Pexels di `assets/esterne/` non sono più usati: la foto Pexels dei fari e la scritta "Foto indicativa" sono state tolte.

## Chiusura e piede

**Chiusura** ("b con foto"): la ciotola è a filo del bordo sinistro, larga il 55 %. A destra ci sono:
- la frase grande;
- il telefono a 32 px sottolineato (`tel:+393487485871`);
- stefano@stefanoaiti.com e info@aitistudio.it (`mailto:`);
- l'indirizzo con il link a Google Maps.

Niente riquadri. Tra la fine della foto e il filetto del piede ci sono 96 px, didascalia compresa.

**Piede**:
- il logo SVG tracciato fedele dal favicon, con una riga su chi è;
- tre colonne con titoletti in maiuscolo spaziato:
  - LAVORI: Still life, Architettura e contract, Industria e cantieri vanno alle sezioni; Corporate va a `corporate/`;
  - STUDIO: `studio/`, `costruzioni/`, `clienti/`, e Matrimoni che porta a weddgraphy.it;
  - CONTATTI, con i link sottolineati;
- la riga legale: "Stefano Aiti Fotografo, ditta individuale, P.IVA 04257170284, PEC", poi Privacy e Cookie.

A 390 le colonne si impilano nell'ordine Lavori, Studio, Contatti.

Cose escluse:
- **Seguici**: nessun social trovato sui tre siti.
- **Newsletter**: lavora su commessa per le aziende, non ha novità, fiere, cataloghi o collezioni da comunicare, e i privati (i matrimoni) passano da Weddgraphy.

## Controlli

- Screenshot guardati a pezzi a 1440 e 390 (intera e prima schermata), più 320, 768, 1024 e 1920. Guardati anche i quattro cambi dell'indice a 1440, il cambio e il menu aperto a 390.
- Scorrimento orizzontale: nessuno a nessuna larghezza (`scrollWidth` uguale alla finestra).
- Sovrapposizioni: nessuna. A 1440 gli oggetti restano a 40 px o più dalla riga "comunicazione".
- U+2014: nessuno, nella pagina e nei .md.
- `_metodo/kit/segnali.sh`: 0 soglie bloccanti. Foto al 52 % della pagina, Switzer al 100 %, nessun monospazio, nessuna etichetta sopra i titoli.
  - Resta "da guardare" la soglia delle misure degli H2 (60 e 52 px). La terza voce grande è l'elenco dei clienti da 44 px: va bene così.
  - La frase di aitistudio.it "non solo... ma anche" è stata lasciata fuori perché è un segnale della guida, e al suo posto c'è la citazione sull'attrezzatura.
- Testata e piede: `tel:` e `mailto:` controllati; l'indirizzo apre Google Maps.
