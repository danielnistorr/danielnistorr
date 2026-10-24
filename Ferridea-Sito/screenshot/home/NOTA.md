# Ferridea, nuova home: versione finale "Ferro sul muro"

Pagina: `sito/index.html` (statica, si apre con file:///). Immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini, controlli, screenshot, segnali).

Misure: 5351 px a 1440 compreso il piede (prima 5928), 6160 px a 390 (prima 6818). Nessuno scorrimento orizzontale da 320 a 2560 (15 larghezze provate).

## L'idea

La pagina è il muro di calce, e sul muro c'è un lavoro loro: la scala a sbalzo di Ferridea (foto `P1020524` del loro sito).
- Ho scontornato i gradini a mano, con poligoni ricavati dagli spigoli veri, e ho tolto cucina, finestra, soffitto in legno e una piastra.
- Il muro intorno ora è esattamente il fondo della pagina, #F2F0EB. Sul muro restano solo le ombre vere sotto le testate dei gradini.
- La foto è raddrizzata di 2,6 gradi (le verticali della finestra pendevano). Le alte luci dei piani lucidi sono recuperate e la dominante blu è tolta.
- Cinque blocchi scuri escono dal muro uno sopra l'altro.
- **Le legende**, come nella versione chiara di Agnoletto: tre punti sui gradini e tre fili sottili fino alla colonna di destra, con le parole "Fissata solo al muro", "Niente montanti" e "Su misura per quel vano"; sopra, "Scala a sbalzo, lavoro Ferridea" a 16 px in ferro. Così il pezzo si legge come scala, e come una scala fatta da loro, nei primi secondi. I punti sono messi sulle testate vere dei gradini, misurate sull'immagine. Sotto i 1180 px restano le prime due legende, sotto i 380 px solo la didascalia, perché le parole non starebbero accanto ai gradini.

Il colore d'accento è il minio dell'antiruggine. In tutta la pagina non c'è nessuna foto di repertorio: sono tutte foto di lavori Ferridea.

## Le prime due schermate

- **1440, prima schermata.** In alto a destra la scala a sbalzo con le legende, a filo del bordo destro, senza riquadro; la larghezza è legata all'altezza della finestra, così a 1440x900 restano 50 px d'aria fra il gradino più basso e il titolo. In basso c'è una fascia sola di parole:
  - a sinistra il titolo "Ferro su misura, dal 1959" (Archivo semi-esteso 500, 110 px), con la data dentro il titolo come Capoferri;
  - a destra, colonne 9-12, sulla stessa linea di base, la riga su cosa fanno, il bottone "Chiama 049 879 2451" e l'email.
- **Seconda schermata.** "I lavori", con la riga sotto il titolo nella stessa colonna: quattro foto loro alte 520 px su due righe (7+5 e 5+7 colonne), ognuna con nome, una riga e il link alla pagina. Le foto sono Cancelli (un cancello a tre pannelli in lamiera, frontale), Parapetti e ringhiere, Scale e Capottine. Sotto c'è una riga per serramenti, serrature, saldature e riparazioni.
- **390.** La scala a tutta larghezza con due legende, la didascalia, il titolo su tre righe, la riga e il bottone del telefono a tutta larghezza. Sta tutto in 844 px.
- **1024x768.** Titolo e riga tornano affiancati (colonne 1-7 e 8-12), la foto è al 52 %: il bottone "Chiama" finisce a 611 px, sopra la piega.
- **Resto della pagina:**
  1. il selettore Ferro battuto / Lamiera / Inox;
  2. "Nel settore dal 1959": il titolo e una riga sola su chi sono e come lavorano, senza i tre passi;
  3. la chiusura;
  4. il piede.

## Caratteri e colori

- **Archivo** di Omnibus-Type (Google Fonts, licenza SIL Open Font License 1.1, uso commerciale libero). È variabile in larghezza (62-125) e peso. I file woff2 latin e latin-ext stanno in `sito/fonts/` e li serve la pagina.
  - Titoli: larghezza 112, peso 500, spaziatura da -0,03 a -0,04 em.
  - Testo: 400 a 19 px, interlinea 1,6.
  - Marchio: larghezza 125, peso 600, maiuscolo spaziato.
  - Telefoni: cifre tabellari.
- **Perché Archivo.** Il grottesco largo è quello delle targhe e delle insegne d'officina. È asciutto come il carattere di Secco Sistemi e come le didascalie di Bisca. Una famiglia sola, niente monospazio, niente etichette.
- **Colori**, con il contrasto misurato:

| Ruolo | Colore | Contrasto |
|---|---|---|
| Fondo | calce #F2F0EB | |
| Testo | ferro #222426 | 13,7:1 |
| Testo secondario | mica #5E6266 | 5,4:1 sulla calce, 4,9:1 sul piede |
| Accento: bottone, link, scheda scelta | minio #AD3C19 | 5,4:1 sulla calce, 4,9:1 sul piede |
| Bianco sul bottone minio | | 6,1:1 |
| Piede | #E8E5DE | |

- Il piede è l'unico cambio di fondo della pagina.
- **Riferimenti.** Per la prima schermata, Hambro e Mario Agnoletto in chiaro: un oggetto vero grande, sul fondo dello stesso colore, titolo grande, tanta aria. La data nel titolo viene da Capoferri ("since 1894"). Lo scontorno del metallo sul bianco con l'ombra viene da De Castelli. Nome e riga sotto le realizzazioni vengono da Secco Sistemi.

## Interazione

Il selettore "Ferro battuto, Lamiera, Inox" usa tre parole del loro testo ("cancelli in ferro battuto e lamiera", "acciaio inox"). Sono tre parole grandi che fanno da schede.
- Al clic o al tocco la foto a 2,6:1 e la riga sotto cambiano di netto, senza dissolvenza e senza salti (la riga ha un'altezza minima):
  - Ferro battuto: la fascia a volute del cancello della loro home;
  - Lamiera: il pannello traforato a raggiera;
  - Inox: il parapetto a cavi tesi e il corrimano della scala in marmo.
- Su telefono le foto sono tagli quadrati sul dettaglio, serviti con `<picture>`.
- È un tablist ARIA: si scorre con frecce, Home e Fine, il fuoco è visibile, e senza JavaScript resta la prima scheda.
- Le transizioni durano 0,12 s, solo su colore e sottolineatura. Nessuna animazione allo scorrere, nessun effetto sul cursore, nessun cambio di opacità.

## Foto: origine e licenza

Tutte le foto vengono dal sito attuale ferridea.com (`assets/originali/`) e sono lavori dell'azienda. L'uso va confermato con loro (vedi LEGGIMI).

| In pagina | File in `sito/img/` | Originale | Lavorazione |
|---|---|---|---|
| Apertura | `scala-sbalzo-*` | `scale--P1020524.jpg` | scontorno a poligoni, muro portato a #F2F0EB, ombre di contatto vere, raddrizzata, alte luci recuperate |
| Cancelli | `cancelli-*` | `cancelli--P1030320_.jpg` | cancello a tre pannelli, frontale; fuori quasi tutta la casa gialla sopra |
| Parapetti | `parapetti-*` | `parapetti--Parapetti-San-Giacomo-014.jpg` | bianco del muro neutralizzato a metà (il muro è color crema) |
| Scale | `scale-*` | `scale--Scala-Treviso-011.jpg` | raddrizzata di 0,4 gradi |
| Capottine | `capottine-*` | `capottine--P1030303.jpg` | ritaglio sulla struttura bianca: fuori la casa arancione e i bidoni |
| Ferro battuto | `ferro-battuto-*` | `home--P1030186.jpg` | fascia bassa a volute, 2,6:1 |
| Lamiera | `lamiera-*` | `parapetti--P1030315.jpg` | pannello a raggiera, 2,6:1 |
| Inox | `inox-*` | `parapetti--Sand-20-07-2008-007.jpg` | corrimano, montanti e cavi; fuori i quadri e il lume; muro crema portato alla calce |
| Chiusura | `chiusura-*` | `cancelli--P1030183.jpg` | da vicino: la lamiera forata a quadri e la superficie a vortici; bianco portato alla calce |

Ogni opera compare una volta sola. Prima quattro foto su nove erano scale; ora sono tre (apertura, tessera Scale e scheda Inox, dove però il soggetto è il parapetto).

- **Trattamento comune** (`_prova/script/build_img.py`), a colori e senza seppia:
  - il muro di riferimento diventa neutro e tende alla calce della pagina;
  - riduzione del rumore delle compatte, dimezzata in quest'ultimo passaggio, e una grana fine di luminanza (sigma 0,6 px) alla misura finale invece delle zone a cera;
  - i muri color crema portati verso la calce della pagina (b* fra 2 e 4 nei mezzitoni, come l'apertura);
  - curva a S leggera e alte luci compresse invece che bruciate;
  - saturazione all'80 % e contrasto 1,04 su tutte;
  - nitidezza leggera alla misura finale.
- Ogni foto è in JPEG in tre o quattro larghezze, con `srcset`.
- **Niente repertorio.** Le foto Unsplash di `assets/esterne/` (Wegelius, Gomez Angel, Prouzet, Henman e le altre) non sono usate nella versione finale. Niente immagini generate dall'IA, niente marchi.
- **Chiusura.** Il cancello in lamiera forata a quadri da vicino: una foto loro, frontale e chiara, con la superficie a vortici e la luce nei fori. È un'opera che non compare altrove. Non è la foto dell'officina: quella va scattata (LEGGIMI).

## Chiusura e piede

- **Chiusura** ("b con foto"):
  - a sinistra la frase loro "Dallo studio alla realizzazione, e anche dopo", da "a partire dallo studio e sviluppo di soluzioni personalizzate fino alla realizzazione delle stesse, e anche successivamente";
  - sotto, i recapiti: 049 879 2451 grande con `tel:` (telefono e fax), il cellulare con `tel:`, l'email con `mailto:`, l'indirizzo con "Apri la mappa";
  - a destra la foto fino al bordo;
  - niente orari, perché non sono pubblicati.
- **Piede:**
  - la scritta FERRIDEA, che è una proposta e non un logo, con la riga "Carpenterie metalliche e infissi a Saonara, nel settore dal 1959";
  - tre colonne con i titoletti a 15 px in grigio mica: Lavori (con "Saldature e riparazioni" come testo senza link, perché nessuna sezione ne parla), Ferridea ("Dal 1959" verso `/azienda/`, "L'officina", "Materiali") e Contatti (con `tel:`, `mailto:` e la mappa); "Contatti" non è più ripetuto come link nella colonna Ferridea;
  - la riga legale con ragione sociale, ditta individuale, indirizzo, P.IVA, Privacy e Cookie;
  - a 390 le colonne si impilano nell'ordine Lavori, Ferridea, Contatti.
- **Newsletter: no.** Ferridea non comunica novità, fiere, cataloghi né collezioni, e il sito è fermo al 2016. Chi compra un cancello o una scala lo fa una volta in vent'anni, quindi una newsletter resterebbe vuota. Niente Seguici, perché i social non esistono.

## Ultimo passaggio: cosa è cambiato

Dopo il giudizio cieco (K0 6, K1 7, totale 56 su 80):
1. **Apertura non trasferibile**: tre legende a filo sottile sulla scala e la didascalia a 16 px in ferro (vedi L'idea).
2. **Tolti i tre passi** Studio, Realizzazione, Assistenza: la frase della chiusura ora compare una volta sola. "Nel settore dal 1959" resta come titolo con una riga.
3. **Tolta la riga "E serramenti in alluminio."** sotto il selettore. "Serramenti" compare nell'apertura e nella riga sotto i lavori.
4. **Foto ripetute**: la scheda Inox non mostra più la stessa scala della tessera Scale; il portone ad arco (2006, 1200x1600) è uscito, al suo posto un cancello vero; la chiusura ha una foto nuova, il cancello forato da vicino.
5. **Foto ingrandite**: tessere a 520 px invece di 640, selettore a 2,6:1, rumore dimezzato e grana fine, bianco neutro uguale all'apertura.
6. **Prima schermata**: 50 px fra foto e titolo a 1440x900; a 1024x768 il bottone sta a 611 px.
7. **"I lavori"**: la riga sotto il titolo, nella stessa colonna, senza "Sono foto di lavori nostri."
8. **Piede**: "Contatti" non è più doppio, "Saldature e riparazioni" non punta più a un'ancora che non ne parla.
9. **Console**: tolto il preload del carattere; su file:// zero errori (nel LEGGIMI come rimetterlo in https).

## Controlli fatti

- **Screenshot** guardati a pezzi: 1440 (intera e prima schermata, anche con la scheda Inox), 390 (intera, prima schermata e scheda Inox), 320, 768, 1024 (anche 1024x768) e 1920. Ritagli al 100 % delle foto lavorate: nessuna zona a cera evidente.
- **Correzioni fatte durante i controlli:**
  - a 1024 la didascalia sale sopra la prima legenda, che altrimenti la toccava;
  - a 320 le legende si nascondono, perché le parole coprivano i gradini;
  - il taglio del ferro battuto scende sulle volute, a 2,6:1 e nel quadrato del telefono;
  - la riga sotto il selettore ha un'altezza minima, così cambiando scheda la pagina non salta.
- **Verifica automatica** (`_prova/script/verifica.mjs`, esito in `_prova/verifica-finale.txt`):
  - scrollWidth uguale a innerWidth a 320, 360, 390, 414, 600, 768, 900, 1024, 1180, 1280, 1366, 1440, 1680, 1920 e 2560;
  - selettore con la tastiera: frecce destra e sinistra (anche in giro), Home e Fine spostano scelta e fuoco, Tab porta al pannello; con il dito a 390 Lamiera e Inox si aprono, schede alte 47 px, foto già caricata;
  - collegamenti: `tel:+390498792451` (testata, bottone, chiusura, piede), `tel:+393355203918`, `mailto:info@ferridea.com`, la mappa di Google su "Viale Veneto 32 35020 Saonara PD"; tutte le ancore hanno una destinazione;
  - zero errori e zero avvisi in console su file://.
- **Segnali da IA** (`kit/segnali.sh`, uscita in `_prova/segnali-finale/`): 0 soglie da correggere e 0 da guardare.
  - Foto al 39,6 % della pagina, una sola famiglia di caratteri, nessuna etichetta maiuscola, nessuna numerazione 01/02.
  - Nessuna sezione con titolo a sinistra e paragrafo a destra.
- **Divieti del committente:** niente gradienti, niente card con bordo colorato, niente icone, niente badge, niente tre box in fila, niente dissolvenze, niente corsivo.
- **Testo:** nessun carattere U+2014 in pagina, negli script e nei .md della cartella.
- **Immagini:** quelle usate in pagina e quelle presenti in `sito/img/` coincidono (controllo in `build_finale.sh`).
- **Dati in pagina:** telefono, fax, cellulare, email, indirizzo, ragione sociale, ditta individuale, 1959, "padovana" e "impianti che lavorano di precisione" vengono da `01-analisi.md`. La P.IVA viene da un elenco pubblico ed è nella lista da confermare, come le tre legende e le descrizioni delle foto (LEGGIMI, punti 9 e 10).
