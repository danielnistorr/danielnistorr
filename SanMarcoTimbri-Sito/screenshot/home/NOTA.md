# San Marco Timbri, home: livello professionale (3 novembre 2026)

## Livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///, nessuna risorsa esterna). La home com'era prima di questo passaggio ("L'impronta", fondo blu e leone LEO) è copiata in `_prova/versione-1-originale/` (sito e screenshot). Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari), sezione B (difetti delle nostre home), sezione C (15 regole); scheda d'uso e d'identità `_prova/uso/SCHEDA.md`. Riferimenti guardati: le prime schermate a 1440 di tutti e 14 (`riferimenti.jpg`), le pagine intere di Union, Joseph Brot e Poilâne a pezzi, e la prova già vista dal committente (`_invio/zona/home/livello-professionale.jpg`, colonna di destra; note di Unicar e Panificio Fornasiero).

Rifare tutto: `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, pagina da `index.sorgente.html`, caratteri, screenshot con `fin_shoot.mjs`, poi `pro_controlli.mjs`). Elementi che escono di lato: `node _prova/script/pro_largo.mjs <url> <larghezze...>`.

Screenshot (stessi nomi di prima): `home-1440.jpg` (7359 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (11875 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Dove siamo" al piede). Guardati a pezzi a 1440 e 390 accanto ai riferimenti, e a 320, 768, 1024 e 1920.

### Che cosa è cambiato, in breve

- **Prima l'uso.** La vecchia apertura non aveva né WhatsApp, né indirizzo, né orari, né "come arrivare": l'unica azione grande era il gioco "Prova la tua impronta". Ora:
  - a 1440 la prima schermata ha il mestiere, il luogo, una prova e le tre azioni del visitatore 1 sulla stessa riga: "Chiama 049 776126" (pieno), "Mandaci testo o foto su WhatsApp" e "Scrivi a info@sanmarcotimbri.it" (con il solo bordo, email con oggetto "Richiesta timbro" e le voci già scritte). Sotto, via Longhin 91 con "Indicazioni" e "Prima di passare chiamateci". In fondo alla schermata compare già "Che timbro vi serve?" (a 849 px su 900);
  - a 390 ci sono logo, "Menu" e "Chiama" in testata, il titolo, tre bottoni a tutta larghezza alti 52 px ("Chiama 049 776126", "Mandaci testo o foto su WhatsApp", "Indicazioni per via Longhin 91") e la riga "Prima di passare chiamateci allo 049 776126". Nessun elemento fisso copre i bottoni. Subito dopo la foto del punzone vengono i lavori su misura con le foto (visitatore 3), poi i timbri (l'ordine cambia solo sotto i 700 px).
- **Identità.**
  - In testata c'è il logo vero, intero (scritta e leone di San Marco con il libro "TARGHE"), nero su bianco come nel loro JPEG. Il leone traforato LEO (un lavoro per un cliente) non c'è più.
  - Il titolo è il loro: "Personalizziamo timbri e targhe", in maiuscolo come sul sito di oggi, senza il punto esclamativo.
  - I colori sono quelli del marchio, nero e rosso: il blu #26389C, che non è mai stato loro, è tolto.
  - Le frasi vengono dal loro sito, con il voi: "Timbri per qualsiasi esigenza, sia in gomma che in metallo", "I file ed i loghi li elaboriamo noi per la migliore resa possibile", "colori originali a tabella RAL o PANTONE", "su disegno del cliente".
  - Trodat è detto in parole ("Autoinchiostranti Trodat"), senza le foto del catalogo.
- **Struttura della famiglia B adattata.**
  1. Testata con "Dove siamo" come prima voce e il bottone "Chiama 049 776126".
  2. Apertura con la foto loro a tutta altezza.
  3. "Che timbro vi serve?" (gomma, metallo, sigilli e presse a secco) con il riquadro "Per ordinare un timbro, mandateci": quattro righe, WhatsApp con il messaggio già avviato, email con le voci.
  4. "Targhe e lavori su misura": sei schede con foto loro, nome, riga loro e preventivo su WhatsApp, con il messaggio già scritto per quel lavoro.
  5. Blocco nero con il manifesto (la loro presentazione), "Come funziona un lavoro su misura" in quattro passi e quattro numeri.
  6. "Per uffici, studi ed enti", con i dati per l'ordine, la gara MEPA del 2018 e i comuni serviti.
  7. Modulo con il tipo di richiesta.
  8. "Dove siamo e come raggiungerci", blocco rosso con il telefono a 120 px.
  9. Piede in quattro colonne.
- **Foto, decisione "niente".**
  - Nessuna foto di repertorio, nessuna illustrazione, nessun "Foto indicativa".
  - Restano solo foto loro dalla libreria del sito, tutte alla loro misura o più piccole e con lo stesso trattamento (`pro_img.py`: colore 90 %, contrasto 105 %, nitidezza leggera). L'apertura è il punzone W.E. con l'ovale EUR 120x80: taglio verticale 760x960 mostrato a 460 px a 1440, striscia 2:1 sul telefono. Nelle sei schede, tutte 4:3, ci sono la pulsantiera in pietra, la targa TOILETTES 101, le lettere in ottone brunito, l'insegna traforata, la targa in corten e il trofeo su disegno.
  - Tolti il leone LEO, le lettere brunite grandi e la targa in corten della chiusura, insieme ai loro file in `sito/img`.

### Esito regola per regola (controlli di `_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile**: PASSA. La testata resta in alto (`position:sticky`). A 1440 c'è il bottone "Chiama 049 776126"; a 390, scorrendo a metà pagina, il bottone "Chiama" è a 12 px, alto 44 px e si tocca. "Dove siamo" è la prima voce del menu. I link `tel:` sono 7.
2. **Prima schermata con mestiere, luogo, prova e azione**: PASSA a 1440x900 e 390x844. Occhiello "Laboratorio di timbri e targhe a Padova", H1 "Personalizziamo timbri e targhe". La prova sta nella riga sotto: "fatti nel nostro laboratorio di via Longhin con fresa, laser e controllo numerico. Per privati, aziende e strutture pubbliche". Il bottone "Chiama" è pieno e, a 390, a tutta larghezza (346 su 346 px). La prova è debole perché non hanno anni, voti né certificazioni pubblici (LEGGIMI).
3. **Immagine vera nell'apertura**: PASSA CON IL LIMITE DELLE FOTO CHE HANNO. È una loro foto vera, non scontornata: il punzone in ottone, il loro mestiere, a tutta altezza accanto al testo. Non esiste nessuna foto loro di persone, del banco o della sede, quindi non c'è "chi lavora e dove": va fatta (LEGGIMI).
4. **Zero repertorio**: PASSA. "indicativ" compare 0 volte e nessuna immagine viene da una banca d'immagini.
5. **Foto in serie**: PASSA NEL CONTROLLO, CON RISERVA A VISTA. Ci sono due formati (apertura verticale, schede 4:3; il logo escluso) e 0 didascalie su 7 immagini; il nome sotto ogni scheda fa da titolo, non da didascalia. Il trattamento è comune, ma le foto sono scatti da banco con luci e fondi diversi (pietra bianca, legno grigio, esterno col sole): una vera serie si ottiene solo con la giornata di still life (LEGGIMI).
6. **Palette dal marchio**: PASSA. Nero #161616 e rosso #B8261D (il #FF0000 del loro sito, scaldato), più bianco #FFFFFF, grigio #EEEEEC dei blocchi chiari (neutro, non beige), grigio del testo secondario #55554F e filetti #D6D6D2. Bianco su rosso 6,3:1, nero su grigio 15:1.
7. **Scala corta e leggibile**: PASSA. A 1440 ci sono otto misure: 120, 87, 56, 44, 24, 19, 16, 14 px. A 390 sono otto: 56, 40, 30, 21, 17, 16, 14 px, più il titolo a 39,8 px. Il testo corrente è 19 px (390: 17 px); a 14 px ci sono solo la riga legale e le note legali; il titolo è a 87 px in maiuscolo con interlinea 0,98. Sotto i 700 px il titolo stringe la larghezza del carattere (85 %), così "PERSONALIZZIAMO" sta su una riga da 320 px in su.
8. **Due famiglie al massimo**: PASSA, con una sola famiglia, Encode Sans, in due ruoli: titoli in 700 un poco larghi (108 %), testo e interfaccia in 400. Era già il carattere della versione 1.
9. **Servizi in schede con foto**: PASSA. Una griglia di 3 colonne a 1440 e 1024 (2 a 768, 1 sul telefono) con sei schede, tutte cliccabili: foto 4:3, nome a 24 px, la loro riga e "Chiedete il preventivo su WhatsApp", che apre WhatsApp con il messaggio per quel lavoro. Casellari, vetrinistica e plexiglass sono in una riga sotto, perché non hanno foto loro che reggano (i casellari sono foto di catalogo).
10. **Almeno tre tipi di prove**: NON PASSA, PER LIMITE DELLE FONTI. Due tipi su quattro:
    - quattro numeri contati dai loro elenchi (10 lavorazioni, 4 tecniche in laboratorio, 4 tipi di timbro in gomma, 5 materiali per targhe e pulsantiere);
    - un ente con il nome: Agenzia delle Entrate, che nel 2018 li ha invitati alla gara MEPA per i timbri (dalla SCHEDA, fonte il PDF di agenziaentrate.gov.it).
    Recensioni e certificazioni non ce ne sono (Maps 429, Facebook solo con login, 2gis e Yelp senza recensioni); non sono inventate (LEGGIMI).
11. **Lavori con un nome**: NON SI APPLICA. Nelle fonti non c'è nessun lavoro con cliente e anno: ogni scheda dice che cos'è e di che materiale.
12. **Ritmo a blocchi**: PASSA. Sequenza dei fondi: bianco, grigio (timbri), bianco (su misura), nero (come lavoriamo), bianco (enti), grigio (modulo), rosso (dove siamo), nero (piede). Spazi di 96-120 px a 1440 e 56-64 px a 390. I 96 px sopra "Che timbro vi serve?" servono perché si veda in fondo alla prima schermata; i 56 px a 390 sono sotto la soglia di 64 per la stessa ragione. Margini di 80 px a 1440 e 22 px a 390.
13. **Un solo sistema di bottoni**: PASSA. Bottone pieno rosso e bottone con il solo bordo (nero, o bianco sui blocchi scuri), raggio 4 px, alti 52 px (44 px solo nella testata del telefono, per stare in 68 px), testo a 16 px. Il bottone di chiamata contiene il numero (a 390, in testata, solo "Chiama" per lo spazio; il numero è nel primo bottone sotto il titolo).
14. **Modulo e "dove e quando" per il mestiere**: PASSA IN PARTE.
    - Il modulo in home ha il tipo di richiesta in quattro caselle (timbro in gomma, timbro in metallo o sigillo, targa o pulsantiera, altro lavoro su misura) e i campi nome, ragione sociale, telefono, email, testo riga per riga o descrizione, misura o modello, quantità, ritiro o spedizione. Compone un'email (mailto con oggetto "tipo, ragione sociale o nome" e tutte le voci); va collegato a un servizio (LEGGIMI).
    - Per il laboratorio ci sono indirizzo, "Indicazioni" (Google Maps con il percorso fino a via Giacinto Andrea Longhin 91; solo l'indirizzo, non il nome dell'attività, perché la scheda di Maps potrebbe essere ancora su via Turazza) e "Chiama". Nessun iframe.
    - La tabella degli orari manca: gli orari non sono confermati. Il meccanismo è pronto: con la costante `ORARI` in cima allo script, la pagina scrive "Aperto ora" o "Ora chiuso" con le fasce di oggi nell'apertura e la tabella della settimana in "Quando passare" (provato su una copia con orari di esempio, poi cancellata).
15. **Piede completo**: PASSA, senza certificazioni (non ne hanno). Logo verticale vero in bianco, poi quattro colonne: chi sono; Contatti (telefono e fax, WhatsApp, email, indirizzo con la mappa, "Prima di passare, chiamateci"); Lavorazioni; Per chi (enti, preventivo, zone). Riga legale "San Marco Timbri di Tosato Andrea, via G. A. Longhin 91, 35129 Padova, P.IVA 04289090286, Privacy, Cookie". Testo a 16 px, la riga legale a 14.

### Prove d'uso della scheda (par. 8), con `pro_controlli.mjs`

- **Visitatore 1, 1440x900**:
  - senza scorrere vede Chiama, WhatsApp, email, via Longhin e Indicazioni;
  - il clic su "Scrivi a" apre l'email con oggetto "Richiesta timbro" e le voci testo, misura o modello, quantità, ritiro o spedizione, nome;
  - con uno scorrimento trova "Autoinchiostranti Trodat", "datari", "In metallo" e la frase del file preparato da loro e mandato da approvare;
  - P.IVA in "Per uffici, studi ed enti" e nel piede.
- **Visitatore 2, 390x844**:
  - senza scorrere trova "Chiama 049 776126" (52 px, `tel:+39049776126`), "Indicazioni per via Longhin 91" e "Prima di passare chiamateci";
  - gli orari di oggi non ci sono (da confermare);
  - "Turazza" non compare in nessun punto;
  - nessun elemento fisso, nessuno scorrimento di lato a 320, 360, 390, 414, 768, 1024, 1100, 1101, 1280, 1440 e 1920 (`pro_largo.mjs`).
- **Visitatore 3, 390x844**:
  - le foto delle prime tre schede su misura (pulsantiere, targhe, incisioni e scritte) finiscono a 1477, 1919 e 2360 px dalla cima, entro due scorrimenti (2532 px), ognuna con il suo nome;
  - ogni scheda apre WhatsApp verso 376 167 3361 con il messaggio già avviato ("Buongiorno, vi mando foto e misure per il preventivo di una pulsantiera.");
  - "Come funziona un lavoro su misura" dice idea, file, RAL o PANTONE, bozza e campionatura;
  - i comuni serviti sono elencati uno per uno.
- **Collegamenti**: `tel:+39049776126`; `mailto:info@sanmarcotimbri.it` (con oggetto e testo); `https://wa.me/393761673361?text=...`; `https://www.google.com/maps/dir/?api=1&destination=Via Giacinto Andrea Longhin 91, 35129 Padova`. Nessuna ancora rotta e nessun errore in console (provato anche il menu, aperto con il tocco e chiuso con Esc, e l'invio del modulo).
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.

### Respinti o non applicati, con il motivo

- **Orari in pagina** (SCHEDA par. 4): l'unico dato è 2gis, sulla scheda della vecchia sede di via Turazza. Non è confermato, quindi non va a vista; c'è "Prima di passare chiamateci" e il meccanismo `ORARI` è pronto.
- **PEC e "ancora su MEPA"**: la PEC è vista solo in un riassunto di ricerca; l'iscrizione attuale al MEPA non è verificata. In pagina c'è solo il fatto del 2018.
- **Apertura a tutto schermo con il laboratorio** (famiglia B, punto 2) **e facciata del negozio** (punto 7): non esiste nessuna foto del laboratorio, del banco o dell'ingresso.
- **Novità di stagione e newsletter**: tolte. La pagina "Promozioni & News" è vuota e la newsletter non inviava nulla; c'è un solo modulo, quello delle richieste.
- **"Prova la tua impronta"**: tolto. La SCHEDA lo ammetteva solo se finiva nell'invio del testo, e ora quel compito lo fanno l'email con le voci e il modulo.
- **Didascalie sotto le foto**: nessuna. Il nome della scheda dice già che cosa è; cliente e anno non sono noti.
- **Timbri in gomma con foto**: non c'è nessuna foto loro di un timbro in gomma, solo foto del catalogo Trodat. La sezione dei timbri è fatta di tipografia.

### Caratteri e licenze

Encode Sans (Impallari Type, Andres Torresi, Jacques Le Bailly; Google Fonts), file variabile con peso 100-900 e larghezza 75-125 %, servito dalla pagina in `sito/fonts/` (latin e latin-ext). Licenza SIL Open Font License 1.1, uso commerciale libero; testo in `sito/fonts/OFL.txt`. Usati due pesi (400 e 700) e tre larghezze (100 % per testo e titolo d'apertura, 104-108 % per titoli e cifre, 85 % per il titolo sul telefono).

### Foto, origine

| Dove | Foto | Origine |
|---|---|---|
| Apertura | punzone in ottone per la stampa a caldo W.E. e ovale EUR 120x80 (`punzone-in-ottone-per-stampa-a-caldo.jpg`, 1000x1000) | libreria media del sito sanmarcotimbri.it, foto loro |
| Pulsantiere | pulsantiera in pietra con componenti in ottone lucido (1000x750) | idem |
| Targhe | targhe in ottone a rilievo TOILETTES e 101 (1000x750) | idem |
| Incisioni e scritte | lettere ritagliate a rilievo in ottone brunito (1000x1000, taglio 4:3) | idem |
| Insegne | insegna traforata in metallo con cavallo (1000x1000, taglio 4:3) | idem |
| Segnaletica | targa in acciaio corten su pilastro (1000x666, taglio 800x600 senza il cielo) | idem, che sia loro va confermato |
| Premiazioni | trofeo in ottone su base in legno intarsiato (1000x750) | idem |
| Testata e piede | logo orizzontale (JPEG 641x114) e logo verticale in bianco (dal PNG 256x200) | sito sanmarcotimbri.it |

Nessuna foto generata dall'IA, nessuna di repertorio, nessun marchio concorrente in primo piano. Diritti e consenso per i lavori fatti per clienti da confermare con l'azienda (LEGGIMI).

---

## Versione 1 originale, "L'impronta" (giro del 2 novembre), prima del livello professionale

Quello che segue descrive la versione copiata in `_prova/versione-1-originale/`.

Pagina: `sito/index.html` (si apre con file:///, nessuna risorsa esterna). Si rifà tutto con `bash _prova/script/build_finale.sh` (scontorno del leone, immagini, pagina, caratteri, screenshot).

### L'idea

La prima schermata è composta come un timbro tondo: una riga di testo sopra, il segno al centro, una riga sotto, tutto su un asse solo. Sopra c'è "Personalizziamo", al centro il loro leone traforato in ottone cromato, sotto "timbri e targhe". Il fondo è il blu dell'inchiostro da timbri, il colore che il loro lavoro lascia sulla carta; il resto della pagina è carta bianca da ufficio con il testo nello stesso blu.
L'impronta torna come gesto: chi visita scrive il suo testo, lo vede stampato in blu sulla carta e lo chiede per email così com'è.
Il piede torna sul blu, così la pagina si apre e si chiude come un foglio timbrato.

### Cosa è cambiato rispetto alla versione giudicata

Rispetto al giudizio cieco (`_prova/cieco.json`, 53/80) e alla richiesta del committente del 2 novembre ("più alta gamma, meno uguali tra loro"):
- **Apertura rifatta nell'impianto, non solo nell'oggetto.** Prima: carta beige, titolo a sinistra, timbro di repertorio scontornato a destra, impronta disegnata, "Foto indicativa" (lo schema di Hambro e Agnoletto). Ora: fondo blu inchiostro a tutta larghezza, asse centrale, titolo spezzato sopra e sotto il leone come la scritta di un timbro tondo, nessuna legenda e nessun "Foto indicativa". Confrontata con le prime schermate di Hambro, Agnoletto e della zona di Grisignano (`_invio/zona/home/copertine-est-grisignano.jpg`): nessuna ha un fondo di colore pieno con un oggetto centrato e il titolo diviso sopra e sotto.
- **L'oggetto è loro**: il leone traforato in ottone cromato della libreria media del sito (il leone lega nome, marchio e mestiere), scontornato dal cartone con `fin_leone.py` (maschera ristretta dentro il bordo, sfumatura di 1 px, il giallo del cartone tolto dal contorno), cromo reso neutro, ombra corta sul blu. Provato a deviceScaleFactor 2: nessun alone chiaro lungo il contorno.
- **Nessuna foto di repertorio in pagina**: via il sigillo di Pauline Raw e le presse di Dana Sredojevic. Tutte e tre le foto sono loro.
- **Colore di fondo dal mestiere**: blu inchiostro #26389C (apertura, piede, impronta) e carta bianca #FAFAF7 al posto del beige #F5F2EC.
- **Testata**: la sola scritta "sanmarcotimbri" in bianco, al centro sull'asse, a 30 px (il leone a tratto, illeggibile a quella misura, resta nel piede). Sotto i 1100 px il menu passa a un bottone vero.
- **Timbri e impronta**: le tre famiglie in tre colonne senza filetti, sopra; sotto due colonne, anteprima larga sette colonne su dodici (circa 690 px a 1440, 480 a 1024) e modulo a destra. Tolto `maxlength`: le righe lunghe si stringono nell'impronta e nell'email arriva il testo intero (provato con "Studio Notarile Bianchi Rossi & Associati S.r.l.").
- **Dieci lavorazioni**: indice senza numeri 01-10, nome e riga vera sulla stessa linea, accanto una sola foto loro alta quanto l'indice, a filo del bordo destro. È l'unico blocco a filetti della pagina (erano 26 filetti, ora 17 compresi quelli del piede).
- **Come lavoriamo**: niente più fascia di repertorio né passi numerati 1-3; titolo e due frasi loro (macchine, file, RAL o PANTONE, campionatura).
- **Chiusura**: frase loro "Su qualsiasi materiale, a fresa o a laser" (dalla riga "INCISIONI su qualsiasi materiale sia a fresa che laser", che ora compare solo qui; nell'indice Incisioni dice "A fresa e a laser"). Niente più tabella etichetta e valore: telefono grande, poi WhatsApp, email, indirizzo con la mappa e la zona in righe di testo semplici. La targa in corten è mostrata al massimo alla sua misura vera (624 px, prima 660 px ingranditi a 708), taglio senza il cielo bianco ai lati, foto a filo del bordo sinistro e testo a destra.
- **Piede**: newsletter in una fascia orizzontale sotto le colonne; Lavorazioni in due sottocolonne sotto un solo titolo; scarto tra le basi delle colonne sotto gli 80 px.
- Tolto il `<link rel=preload>` del carattere (errori CORS aperto da file://; `font-display:swap` basta).

### Le prime due schermate

- **1440 x 900.** Fondo blu fino a 890 px. Testata: quattro voci a sinistra, la scritta al centro, il telefono a destra, tutto in bianco. "Personalizziamo" a 103 px (Encode Sans largo 118 %, peso 330), il leone largo circa 610 px, "timbri e targhe" sotto; una riga ("Timbri in gomma e in metallo, targhe, insegne e segnaletica. Un laboratorio artigiano a Padova."), il bottone bianco "Prova la tua impronta" e l'email. In basso a destra, sul margine, la didascalia sobria "Leone traforato in ottone cromato".
- **Seconda schermata a 1440.** "Timbri in gomma e in metallo", le tre famiglie, l'impronta interattiva in blu e il modulo.
- **390 x 844.** Stesso asse: testata con scritta, telefono e "Menu"; "Personalizziamo" a 45 px, il leone quasi a tutta larghezza, "timbri e targhe", la frase, il bottone a tutta larghezza, l'email, la didascalia. Tutta l'apertura sta nella prima schermata.
- Altezze: 5024 px a 1440 (piede compreso), 6384 a 390, 6496 a 320, 6699 a 768, 4630 a 1024, 5114 a 1920.

### Sezioni

1. Apertura (sopra).
2. Timbri in gomma e in metallo, con "Prova la tua impronta".
3. "Dieci lavorazioni, dal timbro all'insegna": privati, aziende e strutture pubbliche; i timbri in metallo li chiedono soprattutto amministrazioni pubbliche, notai e avvocati (come dice la loro scheda); l'indice; le lettere in ottone brunito.
4. "I file li prepariamo noi".
5. Chiusura "b con foto" (foto a sinistra a filo del bordo, testo a destra). Niente orari: non sono pubblicati.
6. Piede.

### Caratteri e colori

- **Encode Sans** (Impallari Type, Andres Torresi, Jacques Le Bailly; Google Fonts), una sola famiglia, file variabile con assi di peso e di larghezza, servito dalla pagina in `sito/fonts/`. Licenza **SIL Open Font License 1.1** (uso commerciale libero), testo in `sito/fonts/OFL.txt`. Titolo d'apertura largo 118 % peso 330; titoli di sezione 112 % peso 420; voci dell'indice 110 % a 27 px; testo 100 % peso 400; cifre tabellari su telefoni e P.IVA.
- Perché: la scritta larga e calma è quella delle targhe incise e dei timbri da ufficio; la larghezza variabile dà al titolo il passo della targa e al testo una lettura normale con una famiglia sola. Encode Sans non è nelle liste b della guida.
- Colori: blu inchiostro #26389C (fondo di apertura e piede; bianco sopra 9,9:1, testi secondari #D2D7F0 6,9:1), carta #FAFAF7, testo #1C2A78 (12,2:1), grigio blu dei testi secondari #4F5674 (6,9:1), impronta #3443B0 (7,8:1), filetti #D5D8E3. Nessun rosso, nessun ottone di comodo: un timbro ha due colori, l'inchiostro e la carta.

### Interazione

Un solo gesto, "Prova la tua impronta", dentro la sezione dei timbri. Tre righe di testo e la scelta tra rettangolare e tondo: l'impronta si ridisegna subito in SVG con la grana dell'inchiostro blu e una leggera inclinazione, senza animazioni; i testi lunghi si stringono per stare nel timbro. "Chiedi questo timbro" apre un'email a info@sanmarcotimbri.it con forma e testo intero già scritti.
Provato con `node _prova/script/fin_gesto.mjs <url> <uscita.jpg>`:
- tastiera a 1440: Tab dalla testata ai campi nell'ordine giusto, freccia destra sulla forma passa a "Tondo", fuoco visibile;
- dito a 390: tocco su "Tondo", tocco su "Menu" (si apre, aria-expanded true), Esc lo chiude;
- bersagli alti 44-48 px.
Le uniche transizioni (120 ms) sono il colore dei bottoni toccati. Niente che compare allo scorrimento, niente che segue il cursore.

### Foto, origine e licenza

Trattamento comune con PIL: saturazione al 90-92 % sulle foto, cromo del leone quasi neutro (18 %), un filo di contrasto, nitidezza leggera all'uscita; più larghezze con srcset.

| Dove | Foto | Origine | Licenza |
|---|---|---|---|
| Apertura | leone traforato in ottone cromato, scontornato | sito sanmarcotimbri.it, libreria media (`traforato-in-ottone-cromato.jpg`, 1000x750) | dell'azienda, da confermare |
| Dieci lavorazioni | lettere ritagliate a rilievo in ottone brunito | sito sanmarcotimbri.it, libreria media | dell'azienda, da confermare |
| Chiusura | targa direzionale in acciaio corten su pilastro | sito sanmarcotimbri.it, libreria media | dell'azienda, da confermare |
| Testata e piede | scritta e logo verticale, bianco reso trasparente e ricolorato in bianco | sito sanmarcotimbri.it | dell'azienda |

Nessuna foto generata dall'IA, nessuna di repertorio, nessun marchio concorrente in primo piano. Il leone viene da uno scatto di 1000 px (il leone è largo circa 830 px nell'originale): a 1440 è mostrato largo circa 610 px, quindi a 1x è nitido, mentre su uno schermo 2x è ingrandito di circa 1,5 volte, morbido ma pulito; va rifatto in studio (LEGGIMI).

### Piede

Logo verticale vero (PNG originale 256x200, bianco reso trasparente, in bianco sul blu, mostrato a 120 px, quindi 2x; il leone non si ricostruisce in SVG senza l'originale vettoriale) e una riga su chi sono. Colonne: Lavorazioni (dieci voci in due sottocolonne), Idee regalo, Azienda (Chi siamo, Come lavoriamo, Promozioni e novità, Contatti), Contatti (telefono e fax, WhatsApp, email, indirizzo con mappa). Sotto, la fascia "Novità e promozioni" con campo, bottone e consenso; in fondo "San Marco Timbri di Tosato Andrea, via G. A. Longhin 91, 35129 Padova, P.IVA 04289090286", Privacy, Cookie. Niente REA né capitale (impresa individuale), niente "Seguici" (nessun profilo verificato). A 390 si impila: logo, Lavorazioni, Idee regalo e Azienda affiancate, Contatti, newsletter, riga legale.
La newsletter ha senso per la linea regalo (lauree, matrimoni, Natale) e per la pagina "Promozioni & News" che esiste già: controlla email e consenso ma non invia nulla finché non si collega a un servizio (LEGGIMI).

### Controlli (2 novembre)

- Screenshot guardati a pezzi a 1440, 390, 320, 768, 1024 e 1920; dettaglio del leone a deviceScaleFactor 2.
- scrollWidth uguale a innerWidth a 24 larghezze da 320 a 2560 (`_prova/script/fin_larghezze.mjs`).
- Collegamenti: `tel:+39049776126`, `mailto:info@sanmarcotimbri.it`, `https://wa.me/393761673361`, Google Maps su "Via Giacinto Andrea Longhin 91 35129 Padova"; nessuna ancora interna rotta.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI e negli script; voi ovunque.
- `segnali.sh` (cartella di uscita cancellata dopo la lettura):
  - OK: nessun carattere delle liste b, 0 etichette sopra i titoli, 0 titoli col punto, 3 fasce di fondo, 1 sola sezione titolo a sinistra e testo a destra, 17 filetti, 0 frecce, 0 numeri grandi con etichetta, 0 numerazioni, nessuna tabella, nessun divieto trovato, famiglia unica, nessun titolo nero.
  - "Monospazio 100 %": falso positivo, lo strumento legge "code" dentro il nome "Encode Sans"; in pagina non c'è nessun monospazio.
  - "Area foto 18,4 %" (soglia 35 %): voluto. Le foto loro sono da 1000 px e non reggono di più senza ingrandirle; la ricetta del committente chiede un solo oggetto con aria. Con la giornata di still life (LEGGIMI) si allargano.
  - Misure di H2: 60 px nelle sezioni e 13 px nei titoletti del piede.
  - Nessun contenuto con data o nome: anno di inizio e lavori con cliente non sono pubblici (LEGGIMI).
- Divieti del committente: nessun gradiente, nessuna emoji, niente Inter, niente card con bordo colorato, niente vetro, niente tre box con icona, niente badge, nessuna icona Lucide, niente dissolvenze allo scorrimento, niente effetti sul cursore, niente bottoni che sbiadiscono, niente serif corsivo, niente legende numerate sull'oggetto.
