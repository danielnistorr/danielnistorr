# Home Belletti

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh`: immagini con `pro_img.py`, controllo dei testi e delle immagini citate, screenshot con `shot_finale.mjs`, poi `pro_controlli.mjs` (le 15 regole, esito anche in `_prova/pro_controlli.json`) e `pro_prova.mjs` (menu, ancore, modulo). Le modifiche del ritocco finale alla pagina sono in `_prova/script/ritocco_css.py` e `ritocco_html.py` (sostituzioni esatte, già applicate).

La home di prima ("Il carattere dell'edificio", con la sua NOTA e i suoi screenshot) è copiata com'era in `_prova/versione-1-originale/`.

Screenshot, stessi nomi di prima: `home-1440.jpg` (10878 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (15581 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (contatti e piede). Guardati a pezzi a 1440 e 390 accanto ai riferimenti (prime schermate di tutti e 14, pagine intere di Wilson ed Eggentaler); prime schermate e pagine intere anche a 320, 768, 1024 e 1920 (PNG cancellati dopo la lettura).

## Livello professionale, ritocco finale (3/11/2026)

Richieste del committente: "ancora troppo poco professionale e di design, e design funzionale all'attività"; per le foto "niente" (nessun repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia S (servizi tecnici e imprese). Scheda d'uso: `_prova/uso/SCHEDA.md`. Il ritocco parte dal controllo del livello professionale (voto 6, regole 5, 11, 12 e 14 non passate) e dalle due prove con i clienti tipo (voti 8 e 7,5).

### Che cosa è cambiato in questo ritocco

- **L'apertura ha un gesto suo.** Prima: titolo a sinistra, foto con il raggio a destra su fondo bianco, lo schema delle altre home della campagna. Ora l'apertura è un blocco antracite alto quanto lo schermo (fino a 812 px); la foto della sede di sera con il furgone (`d-027`) è al vivo nella metà destra, senza raggio, e sfuma nel fondo con un gradiente, così il notturno diventa atmosfera invece di un rettangolo nero. Sul telefono è una fascia che chiude lo schermo, sfumata dall'alto. Tolta la didascalia; dei tre link sotto i bottoni ne restano due ("Cosa succede dopo la chiamata", "Progettisti: i lavori con i dati tecnici").
- **Le garanzie continuano il blocco scuro**: quattro invece di tre, con "Qualità certificata dal 1997" (ISO 9001 dal 4 novembre 1997, Allegato XI dal 1999, link a "Qualità e norme"), separate dall'apertura da un filetto. Testo a 19 px. Sul telefono restano una fascia scura propria dopo l'assistenza, così il caso "fuori orario" resta entro uno scorrimento.
- **Assistenza**: il titolo è "Cosa succede dopo la chiamata" (prima "La marcia in più di Belletti", uno slogan), con le stesse parole del link della prima schermata; il link porta al titolo e sul telefono i tre casi stanno interi nello schermo (313-796 px su 844). I numeri dei casi sono a 48 px, il cambio di scala che mancava. Il caso 03 è detto più piano ("il tecnico interviene alla ripresa del normale orario di lavoro", da confermare). Nuova riga "Volete cambiare manutentore?". La zona dice "Per un sopralluogo fuori zona chiamate gli uffici... Per un guasto chiamate sempre lo 049 900 5131". Il tecnico sul telefono è in 4:5, con la testa (prima tagliata).
- **Testata**: il bottone verde dice "Guasti" anche sul telefono ("Guasti 049 900 5131", 48 px); il Menu sul telefono è un'icona di 48 px con l'etichetta per i lettori di schermo. A 320 px resta il solo numero.
- **Foto in serie.** Un solo trattamento in `pro_img.py`: bilanciamento del bianco a mondo grigio con una forza per foto (poca sui notturni, molta sul neon delle gallerie e sul tungsteno della scala d'epoca), poi la stessa curva per tutte (autocontrasto, saturazione 0,85, contrasto 1,04). Nelle schede la cabina tonda delle gallerie è sostituita dalla torre nell'atrio del depliant (`d-026`), la scala mobile con le stelle di Natale da una scala mobile senza addobbi (`fn000171`), la piattaforma è tagliata senza la sedia. Le schede sono più piccole (al massimo 270 px), così nessuna foto delle gallerie viene ingrandita.
- **Una persona di Belletti in più**: in "Chi siamo" l'ufficio tecnico di Mestrino con le impiegate (`d-043`, 4:3, 424 px, senza ingrandire).
- **Impianti nuovi**: titolo e testo a sinistra (fermi mentre si scorre), sei schede in tre colonne a destra. Titolo "Impianti nuovi, da 12 kg a 100 persone"; la loro frase "L'ascensore rispecchia il carattere dell'edificio" apre il paragrafo. Sul telefono una scheda per riga con la miniatura 4:3 di 120 px, il nome a 20 px e la descrizione visibile (prima due colonne da 167 px senza descrizione).
- **Chi siamo**: titolo "Un'impresa di famiglia, con i suoi tecnici" (prima "Ascensoristi da quattro generazioni": "dal 1908" e "4 generazioni" tornavano tre volte); i quattro numeri sono una fascia a tutta larghezza a 96 px.
- **Lavori**: "Committente: Comune di Padova" in grassetto bianco sotto il luogo di Cavour, "Progetto:" su una riga propria per tutti e tre, "ing. A. Viel" come nei redazionali. Ca' Michiel in 4:5 (737x921 da 790x988), così il vano verticale si legge intero.
- **Modulo**: cinque campi in vista (nome, telefono, comune e indirizzo, che cosa serve, quando), le note a scomparsa; il riquadro "Foto della targa in cabina o del vano" sopra il bottone; dopo il clic il testo pronto con "Copia il testo" e il numero degli uffici, per chi usa la posta via web.
- **Piede**: la colonna si chiama "Contatti" (gli orari degli uffici non sono pubblicati); i numeri sono bersagli di 48 px.

### Uso: i compiti della SCHEDA (par. 8), prima e dopo il ritocco

- **Visitatore 1, telefono 390x844.** Senza scorrere: testata con "Guasti 049 900 5131" (48 px, tel:+390499005131, a metà pagina si vede e si tocca); "Guasto o persona bloccata in cabina? L'assistenza risponde 24 ore su 24, 365 giorni all'anno."; bottone a tutta larghezza "Assistenza 24 ore 049 900 5131" (350x56 px, a 493 px), sotto il bottone bordato degli uffici. "Qualsiasi marca" nell'H1 (289 px). Il caso fuori orario è a 1535 px (prima 1564), dentro il primo scorrimento; con il link "Dopo la chiamata" i tre casi stanno interi nello schermo. Nessun compito peggiora.
- **Visitatore 2, computer 1440x900.** Nella prima schermata: manutenzione e ammodernamento nell'H1, i due numeri. Zona per esteso nell'H1 e nelle garanzie (da 901 px), elenco delle province a 1814 px; ISO 9001 dal 1997 ora nelle garanzie, a 901 px (prima a 8318). Piattaforme e servoscala nell'H1 e nella loro sezione (2475 px). Sopralluogo in un passo: tel: uffici nella prima schermata, mailto: con oggetto e traccia, oppure il modulo, ora di cinque campi più le note facoltative, con il testo da copiare se la posta non si apre. Il link "Chiedete un sopralluogo" della prima schermata è tolto: il modulo resta a un clic da "Contatti" nel menu e dai bottoni delle sezioni.
- **Visitatore 3, progettista.** "Progettisti: i lavori con i dati tecnici" nella prima schermata porta alla sezione con un clic; la prima scheda tecnica completa (Galleria Cavour) è a 437-990 px dopo il clic. Scorrendo a mano è a 3978 px, oltre i due scorrimenti, come prima. L'email all'ufficio tecnico è scritta per intero, con cosa allegare. Certificati: niente link a copie scadute, c'è la richiesta delle copie aggiornate.
- Provato con `pro_prova.mjs`: menu aperto e chiuso al tocco; ancore sotto la testata; "Dopo la chiamata" con i tre casi nello schermo; "Chiedete un sopralluogo" e la scheda Montauto scelgono il tipo nel modulo; invio vuoto fermato con l'avviso e il fuoco sul nome; cinque campi in vista; email composta con oggetto "Richiesta: Impianto nuovo: montauto, Selvazzano Dentro" e corpo completo, letta e non inviata; testo pronto da copiare visibile dopo l'invio; nessun errore di script.

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs`, più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa di 89 px a 1440 e 73 a 390. "Guasti 24 ore 049 900 5131" (a 390 "Guasti 049 900 5131") di 48 px; a metà pagina si vede e si tocca a 1440 e a 390. 16 link `tel:`, solo `+390499005131` e `+390495082430`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** Il mestiere nell'H1, Mestrino e "dal 1908" nell'occhiello, il bottone dei guasti (a 390 largo quanto la colonna, 350 px; a 320, 280 px). Nessuna sovrapposizione tra il testo e la foto a 1440.
3. **Immagine vera nell'apertura: passa.** La sede Belletti di sera con il furgone bianco e verde e il logo sulla fiancata, al vivo su fondo antracite (617x812 a 1440 da 869x1086, mai ingrandita). Riserva: è del 2008 e non mostra la squadra (foto da rifare nel LEGGIMI).
4. **Zero repertorio: passa.** `indicativ` 0 volte, Unsplash e Pexels 0; nessuna immagine da `assets/esterne/`.
5. **Foto in serie: passa** (prima non passava). Tre formati (4:5, 4:3, la striscia del telefono); nessuna didascalia su 13 foto; un solo trattamento con il bianco corretto foto per foto; nelle schede tre foto del depliant 2008 e tre delle gallerie tagliate strette, senza addobbi né arredi in primo piano. Riserva: restano tre servizi diversi (depliant, gallerie, DiBaio) e la sera dei notturni accanto al giorno di Ca' della Nave; la serie vera viene solo dalle foto nuove.
6. **Palette dal marchio: passa.** Un solo colore, il verde del logo in tre toni (#007A43 bottoni e contatti, #009A54 sui fondi scuri, #00603A al passaggio del mouse), più antracite, il grigio del logo e neutri freddi. Nessun colore fuori da `:root`. Niente beige.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 19, 24, 32, 48, 72, 96) e 7 a 390 (14, 17, 20, 24, 30, 40, 48). Testo corrente 19 px a 1440 e 17 a 390. Niente sotto i 14 px. H1 72 px (390: 40).
8. **Due famiglie al massimo: passa.** Una sola, Radio Canada, pesi 400 e 700; titoli e cifre in larghezza 88 %.
9. **Servizi in schede con la foto: passa.** Sei schede in tre colonne a 1440, 1024 e 768, tutte 4:3, con foto vera, nome, una riga e "Sopralluogo e preventivo"; tutta la scheda è un link. Riserva: il lavoro di ogni giorno (manutenzione, verifiche, riparazioni) resta un elenco nella sezione assistenza, perché ha la sua sezione con i tre casi della chiamata e non ci sono foto vere di quel lavoro oltre al tecnico.
10. **Almeno tre tipi di prova: passa (3 su 4).** Quattro numeri in fascia a 96 px (4, 35, 20+, 1997); "Qualità e norme" con didascalia, e ISO 9001 anche nelle garanzie; clienti e progettisti con il nome (Committente: Comune di Padova, in grassetto; Progetto: Zambusi, Danzi, Rigo). Le recensioni mancano: non ce ne sono nelle fonti (LEGGIMI, punto 10).
11. **Lavori con un nome: non passa.** Tre lavori con luogo, cinque dati e foto larga il 51 % della pagina (Ca' Michiel ora in 4:5). L'anno c'è solo per Cavour (ottobre 2007): per Ca' Michiel e Ca' della Nave le fonti non lo danno e non è inventato (LEGGIMI, punto 14).
12. **Ritmo a blocchi: passa** (prima non passava). Blocchi pieni oltre al piede: apertura e garanzie su antracite (un blocco solo a 1440), lavori su antracite, contatti su verde; assistenza e impianti su grigio chiaro. Spazio tra le sezioni 120 px a 1440 e 72 a 390; le garanzie chiudono con 96 px a 1440 e 64 a 390 (prima 64/72 e 40/48). Margini 80 px a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno verde e bordato (bianco sul fondo scuro), raggio 4 px ovunque, 56 px (48 in testata), testo a 17 px; i bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: passa in parte.** Ci sono tipo di intervento (10 voci), comune e indirizzo dell'impianto, urgenza (Appena possibile, Entro un mese, Senza fretta) e, per le foto, il riquadro sopra il bottone che dice di allegarle all'email; nessun iframe. Non c'è un vero campo foto (un mailto non porta allegati: va messo quando si collega il servizio, LEGGIMI) e la zona è per province, non per comuni (le fonti non danno comuni, LEGGIMI punto 3).
15. **Piede completo: passa.** Quattro colonne, testo di almeno 14 px: ragione sociale, P.IVA e C.F., REA, indirizzo con le indicazioni, i due telefoni (bersagli di 48 px) e l'email, l'orario che c'è (assistenza 24 ore su 24), le province, le certificazioni, YouTube con il sottotitolo, Privacy e Cookie, lo sponsor.

### Caratteri e licenze

- **Radio Canada** (The Radio-Canada Project Authors), Google Fonts, SIL Open Font License 1.1, uso commerciale libero. Servita dalla pagina (`sito/fonts/radio-canada-latin.woff2` e `-latin-ext.woff2`), licenza in `sito/fonts/OFL.txt`. Una famiglia sola, la stessa della home di prima.
- **Foto**: solo materiale di Belletti (depliant 2008, gallerie del sito, redazionale DiBaio), con i diritti da chiedere (LEGGIMI). Nessuna foto di repertorio, nessuna immagine generata, nessun disegno. Il logo è il vettoriale vero del depliant.

### Foto in pagina

| File in `sito/img/` | Soggetto | Origine | Mostrata al massimo |
|---|---|---|---|
| `apertura-sede-*` | sede di Mestrino di sera con il furgone | depliant, `d-027` (869x1263), targa sfocata | 617x812 su 869x1086 |
| `apertura-sede-striscia-*` | lo stesso, fascia per il telefono | `d-027`, taglio 869x420 | 390-900 px su 869 |
| `assistenza-tecnico-347` | tecnico al quadro | depliant, `d-033` (347x553), 4:5 | 347 px |
| `ammodernamento-scala-470` | scala del palazzo con la cabina d'epoca | depliant, `d-036` (470x704), 4:5 | 470 px |
| `ufficio-mestrino-424` | l'ufficio tecnico con le impiegate | depliant, `d-043` (633x318), 4:3 | 424 px |
| `lavoro-cavour-*` | Galleria Cavour di sera | depliant, `d-037` (948x1263), 4:3 | 737 px su 948 |
| `lavoro-camichiel-*` | Ca' Michiel, il vano col mosaico | depliant, `d-020` (790x1263), 4:5 | 737 px su 790 |
| `lavoro-cadellanave-*` | Ca' della Nave dalla corte | `01_DiBaio_Martellago.pdf` (942x694), senza le panchine, 4:3 | 737 px su 789 |
| `impianto-*` | torre nell'atrio, torre in vetro, montacarichi, montauto, piattaforma, scala mobile | depliant `d-026`, `d-002`, `d-030`; gallerie `fn000053`, `fn000257`, `fn000171` | 270 px (390: 120) su 335-600 |

### Respinti o fatti in parte, con il motivo

- **Togliere la Pallavolo Padova dal piede** (cliente tipo 2): la SCHEDA (par. 5) chiede di tenerla, perché ne vanno fieri; resta piccola e nel LEGGIMI c'è la domanda se lo sponsor è ancora attivo.
- **Cambiare il titolo dei lavori in "Tre lavori, con i dati tecnici"** (cliente tipo 2): la SCHEDA (par. 6, punto 4) chiede che la loro frase "Pensiamo che per presentarci bastino i lavori che abbiamo eseguito" resti come titolo. Il titolo degli impianti invece è cambiato, e la loro frase apre il paragrafo.
- **Togliere "Quando" per stare nei cinque campi**: la regola 14 chiede l'urgenza; sono le note facoltative a stare a scomparsa, così in vista restano cinque campi.
- **Un solo link sotto i bottoni** (controllore): ne restano due, perché "Progettisti: i lavori" è la strada del visitatore 3 verso le schede tecniche (che a mano stanno oltre due scorrimenti).
- **Pagina più corta sul telefono** (cliente tipo 1, minore): non fatto. Le schede degli impianti leggibili e la foto dell'ufficio allungano la pagina (15581 px, prima 14175); i compiti urgenti stanno tutti nei primi due schermi.
- **Recensioni, squadra con nomi, comuni serviti, anni di due lavori, vero campo foto**: non ci sono nelle fonti o richiedono il servizio d'invio; niente inventato, tutto nel LEGGIMI.
- **Scheda fotografica per la manutenzione**: non c'è una foto vera di quel lavoro oltre al tecnico già in pagina.

### Controlli fatti (3/11/2026)

- `pro_controlli.mjs`: regole 1-10 e 12-15 superate nelle misure; 11 no (l'anno di due lavori); la 14 va letta con la riserva sopra. Nessuna ancora senza destinazione; nessun errore in console.
- Scorrimento orizzontale: nessuno a 320, 360, 390, 768, 1024, 1280, 1440 e 1920 (scrollWidth uguale alla finestra).
- Collegamenti: `tel:+390499005131` (assistenza) e `tel:+390495082430` (uffici); `mailto:info@bellettiascensori.it` con oggetto e traccia per sopralluogo, ufficio tecnico, certificati e modulo; Google Maps con Via della Tecnica 29, 35035 Mestrino; YouTube @BellettiAscensori.
- Contrasti sul fondo antracite: verde del logo 4,6:1 (solo occhielli in maiuscolo), grigio chiaro 8,8:1, bianco sul verde dei bottoni 5,4:1.
- Nessun U+2014 nella pagina, negli script, nella NOTA, nel LEGGIMI, nei CREDITI e in 01-analisi.
