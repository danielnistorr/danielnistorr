# Tacchificio Riviera: proposta di nuova home

È una proposta non richiesta: riguarda solo la home e non è stata inviata né pubblicata.

- La pagina è in `sito/index.html`, con le immagini in `sito/img/` e i caratteri in `sito/fonts/`. Si apre con file:///.
- Gli screenshot e la nota di progetto sono in `screenshot/home/` (vedi `NOTA.md`).
- Per rifare tutto: `bash _prova/script/build_finale.sh`.
- Analisi e fonti in `01-analisi.md`; i prototipi A e B sono in `_prova/home/`.

## Dati da confermare con l'azienda

Fuori pagina finché non arriva una risposta:
- **ISO 9001**: il PDF in linea (IT23/00000845) è scaduto il 13/10/2026. C'è il rinnovo? Se arriva, va aggiunta come quarta riga dei certificati.
- **SA8000**: sul sito ci sono solo i documenti di sistema (Rev 00 del 20/11/2025). L'azienda è certificata? Nel piede il link "Segnalazioni SA8000" porta al loro modulo ME.04, accanto a "Procedura whistleblowing" e "Privacy whistleblowing" (i loro due .docx). Meglio pubblicarli come pagine o PDF.
- **ISO 50001**: il PDF dice "valido dal 11 dicembre 2026", una data futura. In pagina c'è solo il numero, senza date.
- **Numeri**: dipendenti (32 nel 2024) e fatturato (6,26 milioni nel 2025, da companyreports.it). Si possono citare?
- **Griffe**: quali si possono nominare. In pagina c'è solo "le grandi griffe".

In pagina, da confermare:
- **Le tre schede (Legno, Prototipo, Serie)** presentano i pezzi come tre stadi: il legno segnato a matita rossa come modello, il prototipo color avorio e il pezzo di serie. È giusto così? Lo stiletto nero è un pezzo di serie stampato in plastica?
- **Prototipo e stiletto**: il prototipo avorio (`tacco_17`) e lo stiletto nero (`tacco_11`) hanno una forma a calla simile. Se sono lo stesso modello, dal prototipo alla serie, la didascalia può dirlo ("Lo stesso tacco, stampato a iniezione") e diventa la prova più forte della pagina. Fino alla conferma, la pagina non lo dice.
- **Foto d'archivio** (`territorio/modal1.jpg`): chi è l'uomo con la pergamena e la statuetta? Sulla pergamena si legge 1972. Con nome e occasione, la didascalia "Dall'archivio dell'azienda" può diventare più precisa.
- **Lavorazioni in casa**: legno, metallo, plexiglas e incisione si fanno in casa o da fornitori? La frase sull'ottone dice solo "dalla galleria dei nostri pezzi".
- **Le fasi**: in pagina ci sono solo quelle verificate (disegno del cliente, progettazione, stampaggio a iniezione, finissaggio, imballaggio). Il progetto al CAD e la prova del prototipo sotto la scarpa, dedotti dalle foto, sono stati tolti: se li confermano, si possono aggiungere.
- **Ottone**: "RIVIERA" e "37" sono incisi sul piano. Il 37 è la misura? È ottone brunito? Fino alla conferma in pagina c'è solo "ottone" e "37".
- **Anno**: 1945 è l'anno del marchio, la società è del 1985. Chi guida oggi l'azienda: Fabio Boldrin?
- **2010**: "Fabio Boldrin inaugura una nuova sede, con macchinari nuovi." Riassume il loro testo storico.
- **Indirizzo**: "Viale" o "Via" Serenissima 30? Il sito e i certificati non coincidono. In pagina c'è "Viale".
- **Link**: per i cookie oggi esiste solo un link vuoto, quindi in pagina non c'è: serve una pagina vera. "Privacy" porta al loro privacy-policy.docx (meglio una pagina HTML). "English" porta a /en, che ha dei refusi.
- **Testo storico**: va corretto "De Sica gira 'Roma città aperta'" (il regista è Rossellini). Nella nuova home non è usato.

## Foto da rifare dal vero

Tutte le foto in pagina sono loro, ma sono piccole: 800x650 per gli still life, 1920 molto compresso per l'incisione, 488x562 per l'archivio. Lo stiletto e l'ottone sono già mostrati al limite (1,1x e 1,05x). Lo stiletto è stato ritoccato (macchia sul gambo, bordo del piano senza filo nero né gradini, puntini del rumore, neri aperti): è una toppa, non sostituisce lo scatto nuovo, e sullo schermo 2x resta un ingrandimento da 520 px.

1. **Prioritario: lo stesso still life dello stiletto a calice nero, a 3000 px o più (meglio 4000)**: prima di tutto si chiede all'azienda l'originale del servizio fotografico; se non c'è, va rifatto.
   - Stesso fondo chiaro e neutro (non lilla), luce morbida dall'alto a sinistra, un pannello bianco a destra per disegnare il filo di luce sul fianco, ombra corta in basso.
   - Pezzo in piedi, ripreso a 90 gradi a filo del piano d'appoggio, con un obiettivo lungo (100 mm o più) per non deformarlo.
   - Esposizione tarata per leggere il nero (texture e bordo del calice), non per farne una sagoma.
2. **Gli altri due pezzi delle schede**, alla stessa luce, distanza e altezza di camera, così che stiano alla stessa scala: il legno segnato a matita rossa e il prototipo color avorio. Se esiste il prototipo dello stesso modello dello stiletto, va fotografato accanto al pezzo di serie, nella stessa posa.
3. **L'ottone "RIVIERA 37"**, a 4000 px.
   - Tre quarti dall'alto come oggi, con luce radente sul piano per leggere bene l'incisione e un riflettore caldo sulle losanghe.
   - Una seconda foto in macro del solo piano inciso.
4. **L'incisione del fiore**, a 6000 px (oggi è mostrata ridotta e dentro i margini per non far vedere i blocchi JPEG).
   - Luce radente sullo stesso banco scuro, mano e punta a fuoco, diaframma 5,6-8 per tenere a fuoco tutto il fiore.
   - Serve anche un taglio verticale per il telefono.
5. Se possibile, **la pressa a iniezione e il controllo dei pezzi**, per una futura pagina sul processo (non in questa home). Serve il permesso delle persone ritratte.

Servono anche il nome del fotografo e il permesso d'uso delle foto attuali.

## Licenze

- **Foto**: tutte del Tacchificio Riviera, dal loro sito (compresa la foto d'archivio in bianco e nero). In questa home non c'è nessuna foto esterna. I segnaposto in `assets/esterne/` (licenze Unsplash e Pexels in `assets/CREDITI.md`) restano solo come materiale di studio e non sono usati.
- **Caratteri**: Imbue e Hanken Grotesk, da Google Fonts, sotto SIL Open Font License 1.1, serviti dalla pagina (`sito/fonts/LICENZE.txt`).

## Loghi

- Il timbro è il loro `logo.svg`, ricolorato in inchiostro (testata) e in chiaro (piede).
- Contiene il vecchio numero "TEL. 049.502.844" e la scritta "VENEZIA ITALY". Serve una versione senza telefono per l'uso piccolo in testata, ed eventualmente una a colori se esiste.
- La firma "Valentino Boldrin" è il marchio: va chiesto se è registrato e se si può usare così.
