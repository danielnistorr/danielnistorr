# Overdrive Customs, home finale: nota

Proposta non richiesta di nuova homepage (solo la home). Pagina in `sito/index.html`, immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `_prova/script/build_finale.sh`.

## L'idea
Una moto sola, sul bianco calce, con le legende che dicono chi ha fatto ogni pezzo: è Hagane, la chopper che ha vinto la categoria Metric al Biker Fest 2024 ed è finita in copertina su Kustom World e su Bigtwin. Il titolo è **Special, dal telaio in su**: viene dal loro post del 20/06/2024 ("Frame, front fork, etc.. built by us") e dalla loro parola per queste moto ("costruire special", post del 07/10/2023). Le tre legende fanno il resto: telaio e forcella di Overdrive Customs, motore e ruote da una Suzuki DR650, sella di Cisco Leather. Con il nome di un'altra officina la pagina non regge: la moto, le legende, il titolo e la chiusura sono loro.

Direzione A del prototipo ("La moto sul bianco"), scelta dal giudice; dalla B restano solo la voce (la frase dei mostri, l'H2 "Dal tagliando alla moto da concorso") e la foto vera dell'officina, ora in chiusura.

## Le prime due schermate
- **1440x900**: testata con il logo vero (SVG), menu (Officina, Le moto, Riviste, Dove siamo) e il telefono. Titolo su una riga a 100 px. Sotto, a destra, Hagane scontornata (immagine 867 px compresa l'ombra) con le tre legende in una fila sola, sulla stessa linea di base, e i fili verticali che scendono sui pezzi. A sinistra tre righe su chi sono, il bottone rosso "Chiama 340 251 0434", "Su appuntamento, da martedì a venerdì"; la didascalia di Hagane chiude all'altezza delle gomme.
- **Seconda schermata**: "Dal tagliando alla moto da concorso", la data di apertura (2 maggio 2015), due elenchi brevi (In officina, Su progetto); poi "Le moto premiate".
- **1024 e 768**: la pagina passa alla disposizione del telefono già a 1180 px: titolo, moto larga quanto il contenuto (920 px a 1024), i numeri sui pezzi con l'elenco sotto, poi testo e bottone.
- **390x844**: titolo su due righe a 50 px, Hagane a tutta larghezza con i numeri sui pezzi, l'elenco delle legende subito sotto, poi testo e bottone. Testata con logo, telefono e bottone "Menu".
- Pagina: 5092 px a 1440 (piede compreso), 5595 px a 390.

## Come è fatto lo scontorno
Script `_prova/script/finale_taglio.py`, solo pixel della foto originale (Instagram, 1080 px), niente generato:
- gomme e cerchi come ellissi vettoriali misurate sulla foto (`fit_ruote.py`), con sfumatura di 1 px;
- ruota davanti: ogni raggio è trovato sulla foto tra la flangia del mozzo e il cerchio, assestato al decimo di pixel e reso come linea piena e continua, del rosso bruno misurato sui raggi veri (prima erano puntinati);
- ruota dietro: disco, corona e catena tenuti per colore; i fori dell'erba hanno ora bordi tondi e puliti;
- gomme: il riflesso grigio sul fianco destro della gomma dietro è abbassato al tono della gomma; nella parte bassa delle due gomme, dove passava l'erba, il colore resta scuro e neutro; i puntini scuri sui cerchi rossi sono chiusi col rosso vicino;
- telaio: il tubo verticale dietro il motore, bucato dalla catena, è chiuso con i bordi misurati sulla foto;
- bordo del corpo levigato a doppia misura, colori del bordo presi dall'interno; bordo alto del serbatoio come curva liscia; tono: rosso meno saturo, neri più profondi, HDR attenuato; ombre morbide di contatto.
È ancora una foto da 1080 px: a 867 px regge, da vicino si vede il limite del file. La strada vera è nel LEGGIMI (originale del fotografo o scatto in studio).

## Caratteri e colori
- **Archivo** (Omnibus-Type, Google Fonts), un solo file variabile con gli assi di peso e larghezza, servito da `sito/fonts/` (woff2 latin e latin-ext). Licenza **SIL Open Font License 1.1** (`sito/fonts/OFL-Archivo.txt`): uso commerciale libero, si può incorporare e ridistribuire con il sito. Titoli a larghezza 106 % in peso 500, spaziatura da -0,03 a -0,035em; testo 400 a 17-19 px, interlinea 1,55; etichette e bottoni 600; cifre tabellari per telefono, anni e orari. Niente monospazio, niente corsivo, nessun secondo carattere. Riferimento: il grottesco largo dei marchi del mondo custom (Revival Cycles, la scheda "THE RELOAD 650" di Roland Sands) e i caratteri piccoli e ordinati di Auto Fabrica; il corsivo resta solo nel logo.
- **Colori**: bianco calce `#F3F1EC` (fondo), inchiostro `#151515`, grigio delle note `#5F6267` (5,4:1 sul calce), un solo accento rosso officina `#B3261E` sul bottone, sul punto della moto scelta e sul fuoco da tastiera; piede `#151515` con testo `#ECE9E2` e note `#AEABA4` (8:1), segnaposto della newsletter `#9C998F` (6,4:1), filo del campo `#8A8780` (5,1:1); bianco sul rosso del bottone 6,5:1. Tutto sopra AA.

## Interazione
Un gesto solo, in "Le moto premiate": quattro schede (Envy 2019, Drakkar 2021, Special K 2022, 883 Old Style 2023) cambiano la foto e il testo del premio con un cambio netto, senza dissolvenza. Si apre su Special K (foto in studio, chiara come l'apertura; la Envy è già nella foto della chiusura). Tablist vero: clic, dito, frecce, Home e Fine; con Tab si entra solo nella scheda attiva; il testo del premio è annunciato agli screen reader; il fuoco si vede (bordo rosso). I nomi delle moto nel piede aprono la scheda giusta.
Sotto i 900 px la testata ha un bottone "Menu" vero (`aria-expanded`, `aria-controls`): apre i quattro link a 66 px d'altezza l'uno, si chiude con un tocco su un link, con "Chiudi" o con Esc (il fuoco torna sul bottone). Le transizioni (0,15 s) sono solo cambi di colore su ciò che si tocca: nessuna animazione allo scorrere, nessun effetto sul cursore, nessun elemento che sbiadisce.

## Foto: origine e licenza
Solo foto dell'azienda, dal sito e dal profilo Instagram @overdrive_customs (`assets/originali/`, voti in `_prova/inventario-immagini.json`). Nessun segnaposto di repertorio, nessuna foto nuova scaricata, nessuna immagine generata dall'IA. Lavorate con PIL e OpenCV ed esportate in WebP a più larghezze con `srcset`, mai oltre la misura del file (tranne l'apertura, a doppia misura levigata dallo scontorno).
- Apertura: Hagane nel campo, `feed/20240522_C7QjkJVIRt0.jpg` (post del 22/05/2024, autore non indicato), scontornata.
- Selettore, riquadro fisso 3:2 largo al massimo 720 px. Envy `feed/20181121_BqcLrvEgKvp.jpg` e Drakkar `feed/20210816_CSo4M02INbn.jpg`, tutte e due di fianco davanti alla stessa lamiera grigia, con l'HDR attenuato e un filo più chiare; la Drakkar era 1080x617, la lamiera sopra il manubrio è allungata di 103 px specchiando e allungando le sue prime 50 righe (la moto non è toccata). Special K `feed/20230828_Cwfiz3-oi3b.jpg` e 883 Old Style con Matteo `feed/20231202_C0Wverwo_GZ.jpg` (foto @boemphoto), servizio in studio su fondo bianco, a 720 e 704 px.
- Copertine: Kustom World agosto 2024 (`feed/20240819_C-20QVBoqJR.jpg`) e Bigtwin aprile 2025 (`feed/20250327_DHsQHfYN4bp.jpg`).
- Chiusura: la copertina del sito di oggi, `copertina-sito-original.jpg` (2560x1440, Matteo in officina con la Envy e una Sportster, autore da chiedere), a tutta larghezza in 16:10, a 1440 mostrata a 1440 px CSS.
- Ogni moto compare una volta sola, tranne Hagane (apertura e le due copertine, che sono la prova) e la Envy (selettore e foto dell'officina, lontane).
- Licenza: sono foto dell'azienda e di fotografi terzi; le copertine sono delle riviste. Prima di pubblicare servono i permessi (vedi LEGGIMI).

## Chiusura e piede
- Chiusura "b con foto", testo sopra e foto a tutta larghezza sotto: a sinistra la frase loro, "I mostri non sono nella vostra testa: li creo io" (post del 07/10/2023, "I mostri non sono nella vostra testa.... Li creo io!", punteggiatura adattata), e sotto "Sempre tanta voglia di fare e costruire special." (stesso post); a destra i recapiti: numero grande con `tel:`, WhatsApp, indirizzo con il link a Google Maps, orari e "Solo su appuntamento", email con `mailto:`. Sotto, la foto dell'officina con una didascalia.
- Piede: logo SVG ricostruito (fedele) con una riga su chi sono; colonne Officina, Le moto, Contatti, tutte della stessa misura; newsletter "Fiere e moto nuove" con email, bottone e consenso privacy, perché l'officina ha fiere fisse ogni anno, moto nuove presentate lì e clienti privati; sotto, "Seguici" con il solo Instagram (Facebook tolto finché non è confermato). Non invia nulla finché non si collega a un servizio (LEGGIMI). Ultima riga: nome, indirizzo, Privacy (`/privacy`), Cookie (`/cookie`); ragione sociale, P.IVA e REA non sono pubblici e vanno aggiunti appena Matteo li dà. A 768 le tre colonne in fila e la newsletter sotto; a 390 Officina e Le moto in due colonne, poi Contatti, poi la newsletter.

## Rifinitura dopo il giudizio cieco (ultimo passaggio)
Giudizio: K0 7, K6 6, non passava. Difetti, uno per uno:
1. **Titolo** (bloccante): "Il telaio lo facciamo noi" ricalcava la formula di Recinzioni Formentin. Ora "Special, dal telaio in su"; "facciamo noi" non c'è più in pagina.
2. **Scontorno** (bloccante): raggi davanti come linee piene, riflesso della gomma dietro abbassato, tubo del telaio chiuso (già avviati nel passaggio interrotto, verificati e tenuti); in più fori della ruota dietro puliti, parte bassa delle gomme ripulita, puntini sui cerchi chiusi. Resta il limite del file da 1080 px.
3. **Foto della chiusura** (importante): via la foto da 640 px; ora la copertina del sito da 2560 px a tutta larghezza.
4. **Envy doppia e fascia dell'officina** (importante): la fascia dopo "Dal tagliando alla moto da concorso" è tolta (la foto è andata in chiusura); il selettore si apre su Special K.
5. **Menu sotto i 900 px** (importante): bottone "Menu" con `aria-expanded` e `aria-controls`, provato con tocco, Invio, Tab ed Esc a 390 e 768.
6. **Foto del selettore disomogenee** (importante): la Drakkar nel negozio con le insegne è sostituita da una foto di fianco davanti alla lamiera; Envy e Drakkar con HDR attenuato. Ora due coppie coerenti (lamiera, studio); il servizio unico da rifare è nel LEGGIMI.
7. **Legende** (minore): tre legende con un fatto ciascuna (chi ha fatto il pezzo), nessuna ripete il titolo.
8. **La Morelia** (minore): tolta dai primi posti (resta da confermare nel LEGGIMI).
9. **Didascalia di Hagane** (minore): "Prima nella categoria Metric al Biker Fest di Lignano".
10. **1024** (minore): da 901 a 1180 px la disposizione impilata, moto a 920 px.
11. **Piede** (minore): Facebook tolto, Seguici sotto la newsletter, colonne della stessa altezza, Privacy e Cookie su `/privacy` e `/cookie`.
12. **"Le moto premiate"** (minore): titolo a sinistra e testo a destra sulla stessa riga, foto e schede che partono alla stessa altezza; niente più vuoto sopra la lista.
Per la soglia delle foto (paragrafo f) le copertine sono un po' più grandi (8 colonne) e la foto della chiusura è in 16:10: area coperta da foto 36 %.

## Controlli
- `_metodo/kit/segnali.sh` sulla pagina finale: 0 soglie bloccanti su 10, 0 da guardare su 8. Foto 36 % dell'area, Archivo 100 %, monospazio 0 %, 2 filetti, 0 frecce, 0 titoli col punto, 3 misure di H2, 2 fasce di fondo, date presenti.
- `_prova/script/finale_prove.mjs` (dentro `build_finale.sh`): larghezza del documento uguale alla finestra a 320, 360, 390, 414, 560, 600, 768, 900, 901, 1024, 1180, 1181, 1280, 1366, 1440, 1680, 1920 e 2560; selettore provato con frecce, Home, Fine e Tab, e con il tocco a 390; menu provato con tocco, Invio, Tab ed Esc; i nomi del piede aprono la scheda giusta; nessuna ancora rotta.
- Collegamenti: `tel:+393402510434`, `https://wa.me/393402510434`, `mailto:overdrivecustoms@live.com`, Google Maps su "Via San Francesco 8/a 30030 Vigonovo VE", Instagram.
- Risoluzione: a DPR 1 nessuna immagine è mostrata oltre la sua misura. A DPR 2 e 3 restano morbide le foto del selettore (file da 720 px) e un poco le copertine e la foto della chiusura a 1440x2 (2880 px chiesti, 2560 nel file): servono gli originali (LEGGIMI).
- Screenshot guardati a pezzi a 1440 e 390, più le prime schermate a 320, 768, 1024 e 1920 e il menu aperto a 390.
- Nessun U+2014 nella pagina, in questa nota e nel LEGGIMI; nessun segnaposto in pagina; nessun dato senza fonte in `01-analisi.md`.
- Divieti: niente gradienti viola, testo in gradiente, emoji, Inter, card con bordo colorato, vetro, badge, tre box con icona, Lucide, shadcn, dissolvenze, effetti sul cursore, bottoni che sbiadiscono, lineette lunghe, parole da brochure, corsivi d'accento.
