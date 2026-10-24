# Home finale di Stefano Aiti, "Comunicazione silenziosa"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con PIL, pagina dal modello `_prova/script/finale_index.html`, screenshot e controlli con `_prova/script/finale_shoot.mjs`).

Misure: 5539 px a 1440 piede compreso, 5568 px a 390, 6582 px a 1920.

## L'idea

La home di un fotografo mostra la fotografia come fotografia. La prima schermata è una sua foto intera, rettangolare, con la sua luce, da margine a margine. Sopra c'è una sua frase su una riga: "Le foto sono comunicazione silenziosa" (sa.com/about). Sotto, l'indice dei clienti: ogni nome cambia la fotografia intera.

La chiusura è l'altra metà della stessa frase: "È il passaparola della qualità a creare il gran rumore".

Con il nome di un altro fotografo la pagina non regge: le foto sono sue, per i suoi clienti, e l'indice porta i loro nomi.

## Prime due schermate

1. **Apertura, 1440x900.** Fondo carta chiaro.
   - In alto il titolo su una riga, largo quanto la griglia (Switzer 500, circa 78 px a 1440, che cresce con la finestra).
   - Sotto, la foto 2:1 da margine a margine (1328 px a 1440): le tre ciotole in argento smaltato di Calegaro al sole radente.
   - Sotto la foto, l'indice: Calegaro, Marijke, Artufficio, Gregorianum; a destra la didascalia "Calegaro, ciotole in argento smaltato 1/4".
   - Nessun testo accanto alla foto, nessuno scontorno.
   - **A 390**: testata con logo, "Chiama" (tel:) e "Menu"; titolo su tre righe; foto quadrata a tutta larghezza (tagli propri per il telefono); indice su una riga e didascalia. Sotto la prima schermata vengono chi è, i fatti, telefono ed email.
2. **Chi è e Architettura.**
   - Una frase su chi è e cosa fa, e a destra 1995, 2008, le due lauree Iuav, telefono ed email.
   - Architettura e contract: titolo e una frase, la parete curva della Banca Prealpi a tutta larghezza in 2:1 (a 390 verticale 4:5), poi la coppia quadrata della scala a chiocciola e della ciminiera della Fornace Morandi.

Il resto della pagina:
- Industria e cantieri: il titolo sulla carta, lo Scania all'alba a tutta larghezza senza testo sopra e con la didascalia sotto; poi i servizi a sinistra (colonne 1-6) e la citazione sull'attrezzatura a destra (colonne 8-12).
- Per aziende orgogliose di ciò che fanno: il titolo e i clienti composti come testo grande.
- La chiusura con foto.
- Il piede.

## Caratteri e colori

- **Switzer** (Indian Type Foundry, da Fontshare), pesi 400 e 500, una sola famiglia per tutta la pagina.
  - Titolo d'apertura in 500 con spaziatura -0,032em e word-spacing 0,04em, così "Le foto sono" non si legge come una parola sola. H2 a 60 e 52 px; testo in 400 a 18-19 px; didascalie a 14 px con cifre tabellari.
  - Titoletti del piede a 12 px in maiuscolo spaziato (0,16em): riprendono le lettere "STUDIO" del logo.
  - Riferimenti: il grottesco neutro e preciso di Hélène Binet (Neue Haas Grotesk) e di Marco Cappelletti (Styrene).
- **Licenza**: ITF Free Font License (Fontshare la indica come `itf_ffl`), gratuita anche per uso commerciale. I file woff2 sono serviti dalla pagina, da `sito/fonts/`. Prima della messa online va riletto il testo della licenza sul punto dell'incorporazione nel sito.
- **Colori**:
  - carta #F6F5F2, fondo di tutta la pagina;
  - inchiostro #141414 (17:1);
  - grigio dei testi secondari e del piede #5C5F5E (6,1:1 sulla carta, AA);
  - grigio del logo #A9ADAC, solo per i filetti.
  - Nessun colore d'accento: il colore viene dalle foto.

## Interazione

Un solo gesto, quello del fotografo che mostra il suo lavoro: scegliere la fotografia.
- I quattro nomi sotto la foto sono bottoni veri con `aria-pressed`, alti 44 px. Al clic o al tocco cambiano la foto intera, il testo alternativo e la didascalia (per esempio "Marijke, vaso di cubetti metallici 2/4"), con un cambio netto e senza dissolvenza.
- Con la tastiera: Tab arriva ai nomi, le frecce destra e sinistra li scorrono in giro, la didascalia è `aria-live`.
- Le altre foto si scaricano solo quando il dito o il puntatore si avvicinano all'indice.
- L'unica transizione è il colore dei link al passaggio (0,15 s). Nessuna animazione allo scorrere, niente che segua il cursore.
- A 768 e 390 il menu si apre con un bottone "Menu" / "Chiudi".

## Foto, origine e licenza

Sono tutte fotografie di Stefano Aiti, prese dal portfolio di stefanoaiti.com e da aitistudio.it. I soggetti sono dei suoi clienti e i diritti d'uso vanno confermati (vedi LEGGIMI). Nessuna foto di repertorio e nessuna immagine generata.

Sono lavorate con PIL (`_prova/script/finale_img.py`) ed esportate in 2-4 larghezze per `srcset`:
- **apertura**: Calegaro (inventario 207), Marijke (638), Artufficio, oblò del Credito Cooperativo di Brendola (67), Gregorianum, frangisole in mattoni (232). Tutte copertine da 1900 px: taglio 2:1 per lo schermo largo e quadrato per telefono e tablet, senza ritocchi di colore.
- **architettura**: Banca Prealpi (13, largo 2:1 e verticale 4:5), scala Studio 4 Marmicolor (819, quadrata), Fornace Morandi (195, quadrata).
- **cantiere**: Salima, Scania all'alba (a3), con la saturazione all'82 % e il contrasto al 96 % per calmare l'HDR.
- **chiusura**: gioielli Superoro in oro rosa (828), in 16:10. Non compaiono altrove nella pagina né in altre home della campagna.

## Chiusura e piede

**Chiusura** ("b con foto"): la foto Superoro è a filo del bordo sinistro, larga il 55 %. A destra:
- la frase grande;
- il telefono a 32 px sottolineato (`tel:+393487485871`);
- stefano@stefanoaiti.com e info@aitistudio.it (`mailto:`);
- l'indirizzo con il link a Google Maps.

**Piede**:
- il logo SVG completo, tracciato fedele dal favicon, a 96 px, con una riga su chi è;
- tre colonne con titoletti in maiuscolo spaziato:
  - LAVORI: Still life (`still-life/`), Architettura e contract e Industria e cantieri (sezioni della home), Corporate (`corporate/`);
  - STUDIO: `studio/`, `costruzioni/`, `clienti/`;
  - CONTATTI: il telefono, "Scrivere a Stefano" (mailto) e "Come arrivare a Mestrino" (mappa), così nessuna riga ripete alla lettera la chiusura, a parte il telefono;
- la riga legale: "Stefano Aiti Fotografo, ditta individuale, P.IVA 04257170284, PEC", poi Privacy e Cookie.

A 390 le colonne si impilano nell'ordine Lavori, Studio, Contatti.

Cose escluse:
- **Seguici**: nessun social trovato sui tre siti.
- **Newsletter**: lavora su commessa per le aziende, non ha novità, fiere, cataloghi o collezioni da comunicare, e i privati (i matrimoni) passano da Weddgraphy.

## Cosa è cambiato nell'ultima rifinitura (giudizio cieco del 24/10)

- **Apertura** (bloccante): via lo scontorno dell'antenna su carta con il titolo a sinistra. Ora c'è una fotografia intera 2:1 da margine a margine, il titolo sopra su una riga e l'indice sotto, che cambia la fotografia intera. Il primo scatto è Calegaro, con la sua luce; seguono Marijke, Artufficio e Gregorianum.
- **Risoluzione**: il Marijke da 625 px è uscito; tutte le foto d'apertura vengono da file da 1900 px e a 1x non sono mai ingrandite (1328 px mostrati da un file da 1600 a 1440; 1808 da 1900 a 1920). Per i 2x servono gli originali (LEGGIMI).
- **Filetto e margine destro**: con le foto intere non c'è più la linea d'appoggio; la foto finisce esattamente sul margine (1384 a 1440, 984 a 1024).
- **Ritmo a metà pagina**: servizi e citazione affiancati sulla griglia a 12 colonne; la sezione Clienti è solo titolo ed elenco; 1995, 2008 e le lauree stanno nell'intro.
- **Testo dei cantieri**: "dove si costruiscono strade e infrastrutture: reportage di cantiere e fotografia aziendale"; livree, video e siti vanno nella pagina `costruzioni/`.
- **Cantiere**: il titolo è sulla carta sopra la foto, nessun testo sopra le foto in tutta la pagina.
- **Logo in testata**: il solo segno AIT, senza la riga STUDIO illeggibile; il logo completo resta nel piede.
- **Titolo**: spaziatura -0,032em e word-spacing 0,04em.
- **Piede**: nella colonna Contatti telefono, una email e la mappa; il link Weddgraphy è tolto finché non lo conferma il titolare.
- **Chiusura**: foto Superoro al posto della ciotola, mai usata altrove in pagina.
- **head**: tolto il preload del carattere (errore CORS aperto come file://).
- `sizes` della foto d'apertura corretto per 1024 e oltre 1920.

## Controlli

- Screenshot guardati a pezzi a 1440 e 390 (intera e prima schermata), più le prime schermate a 320, 768, 1024, 1280, 1920 e 2560. Guardati i tre cambi dell'indice a 1440, il cambio al tocco e il menu aperto a 390.
- Scorrimento orizzontale: nessuno a 320, 390, 768, 1024, 1280, 1440, 1920 e 2560 (`scrollWidth` uguale a `innerWidth`).
- Nessun testo fuori dalla finestra né sovrapposto alle foto.
- Interazione provata con Playwright: clic su tre nomi a 1440; con la tastiera freccia destra dall'ultimo nome torna a Calegaro 1/4, due frecce sinistre portano ad Artufficio 3/4 con `aria-pressed` giusto; a 390 il tocco su Marijke carica `ap-marijke-m-600.jpg` e aggiorna la didascalia.
- Collegamenti: `tel:+393487485871` in testata, intro, chiusura e piede; `mailto:` per stefano@stefanoaiti.com, info@aitistudio.it e la PEC; l'indirizzo apre Google Maps su Via Galileo Galilei 40, 35035 Mestrino.
- U+2014: nessuno, nella pagina, in questa NOTA e nel LEGGIMI.
- `_metodo/kit/segnali.sh`: 0 soglie bloccanti. Foto al 54,8 % della pagina, Switzer al 100 %, nessun monospazio, nessuna etichetta sopra i titoli, nessun titolo a sinistra con paragrafo a destra. Resta "da guardare" la soglia delle misure degli H2 (60 e 52 px): la terza voce grande è l'elenco dei clienti da 44 px, va bene così.
