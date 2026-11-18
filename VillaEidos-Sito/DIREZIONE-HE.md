# Villa Eidos, direzione artistica

Seconda direzione, 17 novembre 2026. La prima (serif Brygada 1918 su carta e pietra, fregio d'apertura, parole del luogo a 150 px) è stata scartata dal committente: "deve essere più professionale, moderno". Resta nel commit c33d072a come punto di ripristino. Restano anche la pipeline (una sola sorgente per anteprima e tema Elementor), i widget nativi, l'installatore, il modulo mailto, il lavoro sulle foto e sul logo, i limiti di peso e le prove. Valgono i vincoli della sezione 2 di `_metodo/highend/SISTEMA.md`; dove questa direzione chiede meno (movimento, scala) prevale la richiesta del committente.

**Fonti dei fatti**, le sole ammesse: il testo del cliente (`villaeidos.it.doc`), il logo e le cinque foto degli interni. Niente posti, metri quadri, servizi, orari, anni o nomi che il testo non dà.

## 1. La cosa vera e l'idea

Una villa storica e un'ampia barchessa in un giardino centenario, riqualificate per funzioni direzionali, a pochi minuti dalla Tangenziale di Padova e dal casello Padova Sud della A13: uffici e sedi di rappresentanza nella villa, sale riunioni e una grande sala conferenze nella barchessa.

L'idea: **una sede d'affari di cui un responsabile del personale o degli eventi si fida in cinque secondi.** Prima schermata divisa: a sinistra il titolo del cliente, la riga su A13 e tangenziale e le due azioni; a destra la sala conferenze con le finestre ad arco della barchessa. Sotto, una riga di fatti logistici, poi gli spazi in schede con la foto e un link "Richiedi" che sceglie lo spazio nel modulo.

## 2. Riferimenti

Sedi d'affari e centri congressi moderni italiani indicati dal committente: Copernico, Talent Garden, Kilometro Rosso. Kilometro Rosso l'ho guardato il 17/11/2026 ("Come raggiungerci" fra le prime voci, un solo colore forte); Copernico e Talent Garden non li ho riaperti in questo giro. In più dalla prima ricerca: The Office Group e Fora (foto in cornici medie, indirizzo sotto ogni sede, un invito chiaro), Villa Erba (la foto dal drone in apertura, che qui manca ed è la prima da chiedere).

Mosse prese: apertura divisa con un'azione piena e una a filo; riga di fatti in solo testo; schede degli spazi tutte uguali, con nome, una riga e un link; un solo campo scuro; testata che si compatta.

Da non prendere: titoli bianchi sopra foto di repertorio, schede con badge ed etichette, icone a tre colonne, numeri di posti che non abbiamo.

## 3. Carattere

**Fustat** (Kief Type Foundry, The Fustat Project Authors; SIL Open Font License 1.1, Google Fonts; file variabile da `@fontsource-variable/fustat` 5.3.0, 24 KB), una sola famiglia per tutto, nessun corsivo.
- 600 per i titoli: `h1` 66 px a 1440 e 38 a 390, interlinea 1,05, spaziatura -0,024em; `h2` 42 px; `h3` 21 px.
- 500 per bottoni, nomi e testata.
- 400 per il testo, 18 px (17 sul telefono), interlinea 1,6.
- Un grottesco neutro e contemporaneo, con cifre tabellari (telefono, indirizzi) e un'occhiata grande che si legge bene a 15 px.

Perché non i candidati suggeriti: Geist e Manrope sono nella lista b di `_metodo/CARATTERI-E-SEGNALI-IA.md` (caratteri di serie dei generatori e di Twenty Twenty-Five); Supreme ha una licenza chiusa che vieta di passare il file a terzi (un tema da consegnare lo farebbe); Cabinet Grotesk è in lista b e già in Foralberg. Fustat non è in nessuna lista né in nessun sito della campagna. Riga sostituita in `_metodo/professionale/alto/REGISTRO-CARATTERI.md`.

## 4. Colore

| Nome | Valore | Dove |
|---|---|---|
| Bianco | #FFFFFF | fondo della pagina |
| Superficie | #F4F5F3 | neutro chiaro e freddo: "Il complesso", la richiesta, il fondo delle foto mentre caricano |
| Inchiostro | #15191A | testo; fondo dell'unica sezione scura, "Per chi" (bianco sopra: 17,7:1) |
| Grigio | #5A615D | testi secondari (6,4:1 sul bianco, 5,8:1 sulla superficie) |
| Verde | #367534 | il verde del logo (#4A8C46, che sul bianco fa 4,1:1) scurito fino a 5,6:1: bottone principale, link, scelta nel modulo, fuoco della tastiera |
| Verde acqua | #5EC1C9 | solo dentro il logo |

Niente gradienti, vetro, ombre decorative o bordi colorati a sinistra. Angoli di 6 px su foto, bottoni e campi.

## 5. Movimento

Quasi niente:
- la testata si compatta scorrendo (da 84 a 64 px, il logo da 46 a 36 px);
- la foto d'apertura si scopre dal basso con un taglio netto quando la pagina si apre (CSS, 1 s, una volta);
- i bottoni si invertono di colpo al passaggio.

Niente dissolvenze, niente titoli che salgono, niente kit di animazione (GSAP non si carica più). Si spegne da *Aspetto > Personalizza > Movimenti*; con "riduci movimento" non c'è.

## 6. Ritmo

| Sezione | Fondo | Scheletro |
|---|---|---|
| Apertura | bianco | griglia divisa: titolo, riga A13 e tangenziale, "Richiedi disponibilità" (pieno) e "Chiama 049 0990550" (a filo) a sinistra; foto 4:5 a destra (480 px, 1,25 volte i suoi 384); al telefono la foto sotto le azioni |
| Fatti | bianco | cinque voci in riga, solo testo, fra due filetti |
| Gli spazi | bianco | titolo e frase; la sala conferenze più grande con il testo accanto; sotto tre schede uguali (sale riunioni, uffici e sedi di rappresentanza, reception e sale d'attesa), tutte 4:3 |
| Il complesso | superficie | titolo; Villa, Barchessa, Giardino, Parcheggi in quattro colonne a misura di `h3`; la riga sulla riqualificazione |
| Per chi | inchiostro | titolo a sinistra, i quattro usi in due colonne a destra |
| Come arrivare | bianco | tre colonne: titolo e link a Google Maps, i collegamenti, i tre ingressi |
| Richiesta | superficie | a sinistra titolo, nota, telefono a 32 px ed email; a destra il modulo su un pannello bianco |
| Piede | bianco | logo, indirizzi, contatti, sezioni, la riga legale da completare |
