# Foralberg: proposta di nuova homepage

Proposta non richiesta, solo la home. Nulla è stato inviato all'azienda né pubblicato.

## Dove sono le cose

- `sito/index.html`: la home finale, statica (si apre con file:///). Immagini in `sito/img/` (JPEG in più larghezze, solo quelle usate, più il logo SVG), caratteri in `sito/fonts/` (Schibsted Grotesk, SIL Open Font License 1.1, `OFL.txt`).
- `screenshot/home/`: home-1440.jpg, home-1440-prima-schermata.jpg, home-390.jpg, home-390-prima-schermata.jpg, chiusura-1440.jpg e `NOTA.md` (idea, schermate, caratteri, colori, gesto, foto, controlli).
- `_prova/script/build_finale.sh`: rifà immagini (`finale_img.py`), pagina (da `index.sorgente.html`) e screenshot (`finale_shots.mjs`); `finale_gesto.mjs` prova l'indice del catalogo con clic e tastiera.
- `01-analisi.md`: fatti con le fonti, voti delle foto, direzioni, riferimenti. `assets/CREDITI.md`: licenze delle foto esterne. `_prova/home/{a,b}/`: i due prototipi da cui viene la finale (base B, indice del catalogo da A).

## Da confermare con l'azienda (in pagina non c'è nulla di dubbio)

- **Anno della 36a Fiera di Padova**: il sito dice 1953, il catalogo 1958. In pagina non compare; la 38a è data per il 1960 (timeline del sito e "1960" scritto a mano sulla foto), la 42a non ha anno in pagina (il sito dice 1964).
- **Anno e sede del furgone**: la timeline dice "1963 Prime consegne con OM Lupetto30 firmate Foralberg", sul cassone c'è "Padova, via Trieste 11", ma dal 1962 la sede era in via San Fermo. La didascalia non dice né luogo né anno dello scatto; la riga degli anni dice solo "1963 le prime consegne con l'OM Lupetto 30".
- **Diritti delle foto d'archivio**: le stampe portano "Foto Giordani". Servono il permesso d'uso (azienda ed eventuali eredi o archivio del fotografo) e gli originali a piena risoluzione; se esistono, anche le foto della sede di via Cile (1980) e dello showroom (2008).
- "Fratelli Desiderio, Luigi e Guerino": riportato alla lettera dal sito; chiarire se Desiderio è il cognome.
- Numeri: "oltre 30 collaboratori interni, 11 agenti e commerciali" (sito) contro 27 dipendenti (Atoka); 6.000 articoli in pronta consegna (catalogo); indirizzo e ruolo dell'ufficio di rappresentanza a Venezia.
- Che "molti modelli si personalizzano con il marchio del vostro locale" valga per la porcellana a catalogo (p. 103: "Il tuo biglietto da visita? Un piatto su misura").
- ldesiderio@foralberg.it come indirizzo pubblico per vendite e showroom (ricostruito dal cloaking della pagina Contatti).
- Il link #page=N presuppone che la numerazione del PDF coincida con quella stampata (verificato a campione).
- Riga legale: REA, PEC e capitale sociale (520.000 euro solo da Atoka) non messi finché non li confermano.
- Profili social di Foralberg (la maglietta del personale porta Facebook, Instagram e LinkedIn): nel piede c'è solo La Vetrinetta su Facebook, l'unico verificato. Se li danno, si aggiunge la colonna Seguici.
- File originale del logo (la distanza tra monogramma e firma nella versione orizzontale è rimisurata a occhio sul JPEG) e il blu ufficiale (#0082B9 dalla copertina, in pagina scurito a #00699A per il contrasto).

## Newsletter

Nel piede c'è "Novità e cataloghi" (email, bottone, casella del consenso). Ha senso: cataloghi annuali, clienti professionali e privati (La Vetrinetta), e la privacy di Foralberg prevede già la mailing list. **Non funziona finché non si collega a un servizio** (Brevo, Mailchimp o quello già usato dall'azienda, che la privacy cita come "sistemi per invio di newsletter ... con report"): oggi il modulo controlla email e consenso e risponde che l'iscrizione sarà attiva dopo il collegamento. Va scritto il testo del consenso con l'azienda e collegata la doppia conferma.

## Pagine del sito nuovo a cui puntano i link

Percorsi proposti (oggi non esistono): Prodotti `/prodotti/porcellana/`, `/prodotti/posateria/`, `/prodotti/vetro/`, `/prodotti/bar-e-mixology/`, `/prodotti/buffet-e-catering/`, `/prodotti/gastronorm/`, `/prodotti/cucina-e-pasticceria/`, `/cataloghi/`; Servizi `/progetti-su-misura/`, `/impianti-professionali/`, `/piatti-personalizzati/`, `/acquisti-pa/`, `/assistenza/`; Azienda `/chi-siamo/` (con la storia e l'archivio), `/showroom/`, `/marchi/` (Berto's, Cambro, Revol, Rona, Steelite, Wüsthof e le loro schede), `/lavora-con-noi/`; Contatti nella home e nella pagina Showroom; `/privacy/`, `/cookie/`, `/note-legali/` (da correggere: oggi le Note legali citano due volte "Selco"). Esterni: La Vetrinetta (lavetrinetta.foralberg.it) per i privati, il suo Facebook, i PDF dei cataloghi su foralberg.it. Nella home i link vanno alle sezioni (#catalogo, #progetti, #storia, #contatti) e al catalogo PDF.

## Foto da rifare dal vero

Le sei foto dell'indice del catalogo sono segnaposto Pexels: vanno sostituite con scatti nello showroom di via Cile, poi passati nello stesso viraggio (`finale_img.py`, bianco e nero neutro, luci sulla carta, neri a #2A2A2A).
- Una mezza giornata in luce naturale, macchina su cavalletto, ottica 50-90 mm, tutto in verticale 4:5 con il soggetto centrato e aria intorno (la foto si ritaglia anche in quadrato per il telefono e in 4:3 per il tablet).
- Porcellana: due mani del personale che posano un piatto della linea Foralberg o Steelite su una tovaglia di lino, dall'alto e di tre quarti. Posateria: una fila di posate da sala su fondo chiaro, dall'alto. Vetro: una distesa di calici Rona sul banco, all'altezza del piede. Bar: il banco con coppe e mixer, luce di lato. Buffet: un'alzata o un chafing dish apparecchiato, senza cibo finto. Gastronorm: vaschette inox con le posate, dall'alto.
- Lo showroom in largo, ripreso come gli stand degli anni Sessanta (la stessa inquadratura frontale con l'insegna), per una futura chiusura o per la pagina Showroom; il magazzino dei 6.000 articoli in pronta consegna; le persone al banco.
- L'archivio: scansione di tutte le stampe a 1200 dpi in scala di grigi, senza ritocchi; servono anche il retro (date, timbri) per fissare gli anni.

## Licenze e loghi

- Foto d'archivio (furgone, stand della 38a e della 42a Fiera): proprietà Foralberg, "Foto Giordani"; diritti da chiedere prima di qualsiasi pubblicazione.
- Foto Pexels (Nilov 6957563, Irina P 12021478, Nguyễn Thanh Ngọc 3992482, Sakelli 5676260, Ehlers 12255469, Filirovska 7140435): Pexels License, uso commerciale gratuito, verificata il 24/10/2026; dettagli in `assets/CREDITI.md`. Le foto Pexels nella cartella `assets/esterne/` non usate nella finale (Remark, Krukau, Kang, Çelik, Kovaleva) restano per i prototipi.
- Carattere: Schibsted Grotesk, Google Fonts, SIL Open Font License 1.1, servito dalla pagina.
- Logo: tracciati vettoriali estratti dalla copertina del Catalogo 2026/2027 (`_prova/script/logo_svg.py`), ricolorati #1D1D1B; da sostituire con il file originale appena l'azienda lo manda. I marchi dei fornitori dipinti sul furgone (Lagostina, Valsodo, Walküre, Duplex, Miele) fanno parte della foto d'archivio, non sono usati come loghi.
