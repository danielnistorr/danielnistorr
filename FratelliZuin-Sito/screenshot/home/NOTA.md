# Fratelli Zuin, home finale: "Il risucchio"

## Idea

Il mezzo che li distingue, l'escavatore a risucchio con la cabina gialla e l'allestimento rosso, scontornato e posato su un fondo color polvere di cava come un prodotto di catalogo, il modo in cui RSP (il costruttore di questi mezzi) fotografa le sue macchine. Il titolo è già scritto sulla fiancata del mezzo, "a risucchio controllato": "Scavi controllati, dal 1946". Con il nome di un concorrente la pagina non regge: mezzo, scritta, timbro e indirizzo dipinto sono loro. Sotto, poche sezioni chiare: i nove lavori in una frase che si tocca, la storia in due date e "Oggi", la chiusura con la loro frase, quattro righe di recapiti e una foto, il piede completo.

## Prime due schermate

- **1440x900**: testata con il timbro del logo in inchiostro, tre voci di menu e il telefono. Titolo Archivo 500, larghezza 116 %, 112 px su due righe in alto a sinistra. Il mezzo è intero, cabina e specchietto compresi, largo 1090 px (il ritaglio ne ha 1331, quindi non è mai ingrandito), posato in basso a destra. Resta a filo del bordo destro perché la foto originale taglia il muso: così il taglio coincide con il bordo della pagina e non sembra un errore. Ombra disegnata sotto le ruote. Sotto le ruote una sola didascalia, allineata al mezzo: "Escavatore a risucchio su MAN TGA 35.410, il nostro mezzo in Via Bassette". In basso a sinistra tre righe su chi sono, il bottone rosso "Chiama 049 625336" e l'email, sulla stessa riga, che poggia sulla linea di terra della ruota anteriore. In alto a destra non c'è niente: è aria. Niente più pallini numerati né legenda.
- **Seconda schermata**: "Nove lavori, per enti pubblici e privati" e le nove voci del sito scritte come una frase a 32 px. Ogni voce è in inchiostro con una sottolineatura sottile sempre visibile, così si capisce che si tocca; la voce scelta ha la sottolineatura rossa da 2 px. Sotto, una foto 2:1 larga 1296 px, con nome, frase vera, "n di 9" e, per i segnaposto, "Foto indicativa" in fondo alla riga. All'apertura è scelta la voce degli escavatori a risucchio, con una foto loro.
- **390x844**: titolo a 54 px su tre righe, il mezzo intero a tutta larghezza a filo destro, la didascalia, tre righe, il bottone e l'email; menu con un bottone vero.
- **Altezze**: 4818 px a 1440, 4356 px a 390 (piede compreso).

## Caratteri e colori

- **Archivo** (Omnibus-Type, Google Fonts, SIL Open Font License 1.1, uso commerciale libero), un solo file variabile servito da `sito/fonts`. Titoli 500 larghi 112-116 %, testo 400 a 18 px, enfasi 500-600; cifre tabellari per telefono, date, codici e "da 2 a 25 m³". La larghezza richiama le scritte dipinte sui mezzi e i nomi dei modelli nei siti di RSP e Sennebogen; il peso 500 segue i titoli leggeri dei riferimenti (Van Oord).
- **Colori**: fondo #F3F1EC (polvere di cava), piede #E8E4DB, inchiostro #1B1B19, testo secondario #45433E, note e virgole #6F6B63 (4,7:1 sul fondo), note del piede #625E57 (5,1:1), sottolineature #B4B0A6. Un solo accento: il rosso cassone #B42620, misurato sulla fiancata del risucchio (bianco sul rosso 6,5:1). Il timbro è in inchiostro anche nel piede.
- **Riferimenti**: RSP (il mezzo intero su fondo chiaro, nome grande), Van Oord (un mezzo solo, titolo sicuro, menu corto), Sennebogen (luce di giorno, un colore di marca), KIBAG (l'anno di fondazione come prova).

## Interazione

Un gesto solo: le nove voci dei lavori sono bottoni dentro una frase. Al clic o al tocco cambiano la foto (cambio netto, la nuova compare quando è caricata), il nome, la frase e "n di 9". Da tastiera: Tab, Invio o Spazio, frecce per passare alla voce vicina; stato in `aria-pressed`, area con `aria-live`. Unica transizione: il colore della voce, 0,12 s. Niente animazioni allo scorrere, niente effetti sul cursore. Sul telefono il menu e le colonne del piede si aprono con bottoni veri (`aria-expanded`). Provato con clic e frecce (risucchio, fognature, cassoni) e col tocco sulla fisarmonica.

## Foto

- **Loro** (sito di oggi): gallery3 scontornata (apertura), gallery4, gallery1 e lavori-stradali-1000x800 (tre lavori), gallery5 (Oggi), pagina-iniziale-1 tagliata 2,4:1 sul carico del DAF (chiusura, alta 600 px a 1440), logo ricolorato. Nessuna foto ripetuta: il movimento terra non usa più la scena della chiusura.
- **Segnaposto Unsplash** (licenza Unsplash verificata il 24/10/2026, autori in `assets/CREDITI.md`, nessuno usato in altre home della campagna): Bruno BD, Iain, Wolfgang Weiser, Shane McLendon, Brandon Mowinkel, Eduard Delputte. In pagina portano "Foto indicativa".
- Lavorazione in `_prova/script/finale_img.py`: un solo trattamento per tutte, una sola maschera di nitidezza sullo scontorno, più larghezze con srcset, mai oltre la misura dell'originale. Quali foto rifare e come: `LEGGIMI.md`.

## Piede

Fondo chiaro #E8E4DB, timbro in inchiostro (PNG a 2x) con una riga su chi sono; tre colonne: Azienda (Chi siamo, La storia dal 1946, Dove siamo, Preventivi), Lavori (sei voci), Contatti (telefono con tel:, fax, email con mailto:, sede operativa con il link alla mappa, sede legale). Riga legale: F.lli Zuin & C. snc, P.IVA e C.F. 00259210284, REA PD 82662, Privacy, Cookie. A 768 tre colonne, a 390 fisarmonica. Niente newsletter: l'azienda non ha novità, fiere o cataloghi da comunicare e i clienti chiamano per un preventivo. Niente Seguici: non hanno social.

## Controlli

- Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1440 e 1920; nessuna sovrapposizione (misurate le posizioni di titolo, mezzo, testo e didascalia a 1440). Screenshot guardati a pezzi.
- Segnali da IA (`segnali.sh`): 0 soglie bloccanti su 10; foto al 39,3 % della pagina; una sola famiglia; nessun titolo nero, niente monospazio, niente etichette maiuscole. Un "da guardare": due misure di H2 (56 e 64 px), scelta voluta.
- Contrasto AA per tutti i testi; nessun carattere U+2014 in pagina, nota e LEGGIMI; nessun segnaposto in pagina.
- Dati: ogni fatto viene da `01-analisi.md`; "1968-69" come la fonte; 1946 contro 1977, MAN TGA 35.410 e la provenienza delle foto sono nel LEGGIMI tra le cose da confermare.
