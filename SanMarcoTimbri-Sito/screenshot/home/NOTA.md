# San Marco Timbri, home: livello professionale, ritocco finale (3 novembre 2026)

## Livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///, nessuna risorsa esterna). La home com'era prima del livello professionale ("L'impronta", fondo blu e leone LEO) è copiata in `_prova/versione-1-originale/`. Regole seguite: `_metodo/professionale/REGOLE.md` (sezione A per la famiglia B, botteghe artigiane e alimentari; sezione B, difetti delle nostre home; sezione C, 15 regole), la scheda d'uso `_prova/uso/SCHEDA.md`, il controllo del livello professionale e le due prove con i clienti tipo (`_prova/pro-controllo/`, `_prova/pro-prova-0/`, `_prova/pro-prova-1/`). Riferimenti guardati: le prime schermate di tutti e 14 e, a pezzi, le pagine intere di Union e Joseph Brot (famiglia B) e di barth e Holzrausch (home fatte di tipografia, la strada di A7 quando mancano le foto).

Rifare tutto: `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, pagina da `index.sorgente.html`, caratteri, screenshot con `fin_shoot.mjs`, poi `pro_controlli.mjs`). A parte: `node _prova/script/pro_largo.mjs <url> <larghezze...>` (scorrimento orizzontale) e `node _prova/script/pro_uso.mjs` (menu, WhatsApp in cima, bersagli del piede, invio del modulo, errori in console).

Screenshot (stessi nomi di prima): `home-1440.jpg` (8326 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (11308 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Dove siamo" al piede). Guardati a pezzi a 1440 e 390, e a 320, 768, 1024 e 1920.

### Che cosa è cambiato in questo ritocco

- **Apertura tipografica a tutta misura.** Tolti l'oggetto su fondo grigio a destra e la striscia del telefono (lo schema B1 e B2: titolo a sinistra e oggetto su fondo chiaro). Ora:
  - occhiello rosso "Laboratorio di timbri e targhe a Padova";
  - H1 su tutta la larghezza del contenitore, 120 px a 1440 con larghezza del carattere 116 %, in due righe: "PERSONALIZZIAMO" in nero e "TIMBRI E TARGHE" nel rosso del marchio, come l'inchiostro del timbro. È il gesto di scala in alto che mancava;
  - sotto, il testo d'attacco a sinistra e a destra l'indirizzo pieno "Via G. A. Longhin 91, 35129 Padova" con "Indicazioni" e "Prima di passare chiamateci" su una riga sola (la frase prima era spezzata in due colonne);
  - le tre azioni in fila;
  - una fascia di tre prove vere su un filetto nero: "Nel 2018 tra i fornitori invitati da Agenzia delle Entrate alla gara sul MEPA per i timbri", "Fresa, laser e controllo numerico e stampa digitale a colori, nel nostro laboratorio", "Il file lo prepariamo noi nei colori RAL o PANTONE, e ve lo mandiamo da approvare".
  A 390 la stessa cosa in colonna: occhiello corto ("Timbri e targhe a Padova", su una riga), H1 a 40 px, attacco, "Chiama 049 776126", WhatsApp, "Indicazioni per via Longhin 91", poi l'indirizzo pieno con il CAP e "Prima di passare chiamateci", poi le tre prove. Tutto dentro 844 px, tranne l'ultima riga della terza prova.
- **Il punzone W.E. passa nella sezione dei timbri**, accanto a "In gomma, In metallo, Sigilli e presse a secco", in un quadrato di al massimo 560 px (taglio 800x800 dell'originale 1000x1000) con l'unica didascalia della pagina, che dice che cos'è: "Punzoni in ottone per la marcatura a caldo: le iniziali W.E. e l'ovale EUR 120x80". Lì fa da prova del mestiere, non da apertura.
- **Fascia del fornitore Trodat** sotto i tipi di timbro: il nome "Trodat" scritto in testo, a 56 px, con la sopra-riga "Timbri autoinchiostranti" e la didascalia "Montiamo i timbri autoinchiostranti Trodat. Per rifarne uno uguale al vecchio basta il modello, che è scritto sotto il timbro, o la foto dell'impronta". È solo testo, non il logo, finché non c'è il permesso (LEGGIMI).
- **Per ordinare un timbro**: la promessa "I file ed i loghi li elaboriamo noi per la migliore resa possibile, e prima di produrre ve li mandiamo da approvare" passa dal grigio piccolo al testo pieno, in grassetto. Sotto i bottoni c'è la riga onesta sull'urgenza: "Vi serve con urgenza? Scrivetelo nel messaggio, o chiamate lo 049 776126 e chiedete se si fa in tempo." Non promette nessun tempo.
- **WhatsApp in cima** avvia lo stesso messaggio con le voci del riquadro "Per ordinare" (testo riga per riga, misura o modello, quantità, ritiro o spedizione). Prima i due bottoni avviavano testi diversi.
- **Foto in serie** (`pro_img.py`): per ogni foto il bianco è bilanciato su un punto neutro (la pietra, il muro, il fondo del banco, la pietra del pilastro), poi tutte vanno alla stessa luminanza media (L circa 0,62: misurate 0,59-0,63), con la stessa desaturazione (82 %), lo stesso contrasto e la stessa nitidezza. Via la dominante oliva dalle lettere brunite. La segnaletica è tagliata stretta su pilastro e targa, senza prato e cielo. Il trofeo è tagliato senza i fogli sulla scrivania.
- **Tolta la frase** "Ogni foto qui sotto è un lavoro uscito dal nostro laboratorio": le fonti non lo confermano per tutte (targa in corten, insegna, TOILETTES).
- **Numeri**: via "4 tipi di timbro in gomma" e "5 materiali". Restano 10 lavorazioni, 40 colori di ceralacca, 16 comuni (quelli elencati in "Dove lavoriamo", da Cittadella a Chioggia) e 2018 (gara MEPA di Agenzia delle Entrate).
- **Titoli di sezione** da 44 a 64 px (`clamp(32px, 4.45vw, 64px)`, larghezza 112 %). Il manifesto del blocco nero ("Una realtà artigiana da molti anni, per privati, aziende e strutture pubbliche.") è a quella misura anche a 390 (32 px); sotto, la riga sulle macchine e il titoletto "Come funziona un lavoro su misura".
- **Testata**: logo a 52 px a 1440 (prima 44), così si leggono il leone e il libro. A 390 la testata è alta 72 px, il menu è un bottone quadrato di 48x48 con tre linee (`aria-label` "Menu") e il bottone di chiamata, alto 48 px, mostra il numero "049 776126". Sotto i 360 px torna la parola "Chiama", perché il numero non ci sta.
- **Su misura a 390 in due colonne** (passo 16 px, 12 a 320): le sei foto finiscono a 1306, 1623 e 1917 px dalla cima. Il link si accorcia in "Preventivo".
- **Uffici ed enti**: nuova riga "PEC e codice destinatario: per la fattura elettronica chiedeteli allo 049 776126 o a info@sanmarcotimbri.it". Dopo il fatto del 2018 c'è "Per acquisti tramite MEPA o con affidamento diretto chiedeteci la situazione aggiornata". Non c'è nessuno stato attuale inventato. Sul telefono la tabella va su una colonna.
- **Piccoli**: il numero in "Scriveteci" (blocco rosso) è un link `tel:`; i link del piede sono blocchi alti 44 px; il telefono grande non va a capo a 320; `vatID` senza il prefisso IT nel JSON-LD (il VIES risponde valid:false); nel modulo, al posto di "Spedizione", c'è l'opzione "Da decidere con voi"; i 9 colori scritti a mano sono diventati token.

### Esito regola per regola (`pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile**: PASSA. Testata `position:sticky`, 88 px a 1440 e 72 px a 390. A 390, scorrendo a metà pagina, il bottone di chiamata della testata è a 12 px, alto 48 px, mostra "049 776126" e si tocca (elementFromPoint). 9 link `tel:`. "Dove siamo" è la prima voce del menu.
2. **Prima schermata con mestiere, luogo, prova e azione**: PASSA a 1440x900 e 390x844. Mestiere nell'occhiello e nell'H1, Padova e via G. A. Longhin 91 con il CAP. La prova è la fascia "Nel 2018 tra i fornitori invitati da Agenzia delle Entrate alla gara sul MEPA per i timbri", in vista in tutte e due. "Chiama 049 776126" è pieno; a 390 è largo 346 su 346 px.
3. **Immagine vera nell'apertura**: NON APPLICABILE NELLA FORMA DELLA REGOLA, RISOLTA CON LA STRADA DI A7. Non esiste nessuna foto del laboratorio, della sede o delle persone, e il committente ha escluso foto di repertorio e illustrazioni. L'apertura è quindi fatta di tipografia, come barth e Holzrausch: H1 a tutta misura, il rosso del marchio e la fascia delle prove, nessun oggetto su fondo chiaro. La foto dell'apertura resta la prima da fare (LEGGIMI).
4. **Zero repertorio**: PASSA. "indicativ" compare 0 volte, nessuna immagine viene da Unsplash, Pexels o altre banche, nessun file di `assets/esterne` è in pagina.
5. **Foto in serie**: PASSA. Due formati, 1:1 per il punzone e 4:3 per le sei schede (loghi esclusi). Una didascalia su 7 foto. Stesso bianco neutro, stessa luminanza media, stessa desaturazione e stessi tagli stretti. Restano scatti da banco a 1000 px: per una serie vera serve la giornata di still life (LEGGIMI).
6. **Palette dal marchio**: PASSA. Token: nero #161616 (logo), rosso #B8261D (il #FF0000 del loro sito, scaldato) e la sua variante #9A1F17, solo per il bottone toccato, più bianco e grigi neutri (#EEEEEC, #55554F, #D6D6D2, #D2D2CE, #4A4A46). Nessun beige. Fuori dai token non c'è più nessun colore scritto a mano.
7. **Scala corta e leggibile**: PASSA. 7 misure a 1440: 120 (H1 e telefono), 64, 56, 24, 19, 16, 14. 7 a 390: 56, 40, 32, 21, 17, 16, 14. Testo corrente 19 px (390: 17). A 14 px c'è solo la riga legale. H1 a 120 px maiuscolo con interlinea 0,94 (A4 per B: 85-90 px; qui è più grande perché è il gesto di scala di una home tipografica). A 390 l'H1 è 40 px, dentro i 40-46 di A4.
8. **Due famiglie al massimo**: PASSA, una sola: Encode Sans. Pesi 400 e 700. Ruoli fissi: titoli in 700, larghi 104-116 %; testo e interfaccia in 400. Sul telefono l'H1 è stretto all'84 %.
9. **Servizi in schede con foto**: PASSA. Griglia di 3 colonne a 1440 e 1024, 2 a 768, 390 e 320. Sei schede, tutte link: foto 4:3, nome, la loro riga e il preventivo su WhatsApp, con il messaggio per quel lavoro.
10. **Almeno tre tipi di prove**: NON PASSA, PER LIMITE DELLE FONTI. I tipi presenti sono 2 su 4: quattro numeri (10, 40, 16, 2018) e la fascia del fornitore Trodat con la didascalia. Recensioni: nessuna leggibile in nessuna fonte. Clienti con il nome: nessuno; l'invito di Agenzia delle Entrate è un invito e non va presentato come cliente. Niente è inventato; nel LEGGIMI c'è che cosa chiedere.
11. **Lavori con un nome**: NON SI APPLICA. Nelle fonti non c'è nessun lavoro con cliente o luogo e anno (LEGGIMI, regola 11).
12. **Ritmo a blocchi**: PASSA. Fondi: bianco (apertura), grigio (timbri), bianco (su misura), nero (come lavoriamo), bianco (enti), grigio (modulo), rosso (dove siamo), nero (piede). Fanno 2 blocchi pieni scuri oltre al piede. Spazio sopra le sezioni di 96-120 px a 1440 (96 sopra "Che timbro vi serve?", che così compare sul bordo della prima schermata a 891 px) e di 64 px a 390. Margini di 80 px a 1440 e 22 px a 390.
13. **Un solo sistema di bottoni**: PASSA. Pieno rosso e con il solo bordo (nero, o bianco sui blocchi scuri), raggio 4 px ovunque, altezza 48-52 px, testo a 16 px. Il bottone di chiamata contiene il numero: "Chiama 049 776126", e "049 776126" nella testata del telefono. Solo sotto i 360 px la testata dice "Chiama", con il numero nell'`aria-label`.
14. **Modulo e "dove e quando" per il mestiere**: PASSA PER IL MODULO E PER "INDICAZIONI" E "CHIAMA". Il modulo ha il tipo di richiesta in quattro caselle e i campi del mestiere. Compone un'email (mailto con oggetto "tipo, ragione sociale o nome" e tutte le voci); va collegato a un servizio (LEGGIMI). Provato con `pro_uso.mjs`: oggetto "Timbro in gomma, Studio Rossi", nessun errore. Nessun iframe. La tabella degli orari manca perché gli orari non sono confermati. Il meccanismo `ORARI` è pronto: provato su una copia con orari di esempio, poi cancellata, scrive "Aperto ora, oggi 08.30-12.30, 15.00-19.00" nell'apertura e la tabella della settimana in "Quando passare".
15. **Piede completo**: PASSA, senza certificazioni (non ne hanno). Quattro colonne a 1440: chi sono; Contatti (telefono e fax, WhatsApp, email, indirizzo con la mappa, "Prima di passare, chiamateci"); Lavorazioni; Per chi (enti, preventivo, zone). Riga legale con ragione sociale, indirizzo, P.IVA 04289090286, Privacy e Cookie. Testo a 16 px, la riga legale a 14 px, link alti 44 px.

### Prove d'uso della scheda (par. 8), prima e dopo il ritocco

- **Visitatore 1, 1440x900** (come prima o meglio):
  - senza scorrere ha Chiama, WhatsApp ed email. L'email ha oggetto "Richiesta timbro" e le voci; il WhatsApp in cima ora ha le stesse voci;
  - con uno scorrimento trova "Autoinchiostranti Trodat", "datari", "In metallo" e ora anche la fascia "Trodat" con il modello sotto il timbro;
  - la promessa del file preparato da loro e della bozza da approvare è già nella prima schermata (fascia delle prove) e, in grassetto, nel riquadro "Per ordinare";
  - in "Per uffici, studi ed enti" ci sono la P.IVA e la riga per PEC e codice destinatario, con chi chiamare. La PEC vera non c'è ancora (da confermare).
- **Visitatore 2, 390x844** (come prima o meglio):
  - senza scorrere trova "Chiama 049 776126" (52 px), il numero anche nella testata, "Indicazioni per via Longhin 91", l'indirizzo pieno "Via G. A. Longhin 91, 35129 Padova" (prima nascosto) e "Prima di passare chiamateci";
  - gli orari non ci sono, perché non sono confermati;
  - "Turazza" non compare in nessun punto;
  - nessun elemento fisso copre i bottoni e nessuno scorrimento di lato a 320, 360, 390, 414, 768, 1024, 1100, 1101, 1280, 1440 e 1920.
- **Visitatore 3, 390x844** (meglio): le foto delle sei schede finiscono entro 1917 px (prima le prime tre entro 2360). Ogni scheda apre WhatsApp con il messaggio per quel lavoro. I quattro passi e i comuni serviti sono come prima.
- **Collegamenti**: `tel:+39049776126`, `mailto:info@sanmarcotimbri.it` (con oggetto e testo), `https://wa.me/393761673361?text=...`, `https://www.google.com/maps/dir/?api=1&destination=Via Giacinto Andrea Longhin 91, 35129 Padova`. Nessuna ancora rotta. Nessun errore in console. Il menu si apre con il tocco e si chiude con Esc.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.

### Respinti o non applicati, con il motivo

- **Alternativa minima del controllore (punzone grande in apertura, almeno metà larghezza)**: respinta. L'originale è 1000x1000: a mezza pagina su 1440 andrebbe ingrandito, e resterebbe lo schema "oggetto su fondo chiaro" di B2. Il punzone è nella sezione dei timbri, alla sua misura.
- **H1 nella fascia 85-90 px di A4 per B**: superata di proposito. In una home senza foto il titolo a tutta misura (120 px) è il gesto di scala della pagina (A5, A7).
- **"Che timbro vi serve?" in vista intera nella prima schermata a 1440** (SCHEDA par. 4): se ne vede solo il bordo, a 891 px. Per farlo salire di più bisognerebbe scendere sotto i 96 px della regola 12, o rimpicciolire il titolo o la fascia delle prove. Il compito (Trodat con uno scorrimento) riesce comunque.
- **Prove in apertura sopra "Prima di passare" a 390**: non spostate. L'indirizzo pieno e "Prima di passare" servono al visitatore 2 senza scorrere, e devono stare sopra la fascia delle prove.
- **Logo Trodat**: solo il nome in testo, finché non c'è il permesso.
- **Orari, PEC, MEPA di oggi, tempi di consegna**: non confermati, quindi non a vista. Ci sono i ripieghi onesti ("Prima di passare chiamateci", "chiedeteli allo...", "chiedeteci la situazione aggiornata", "chiedete se si fa in tempo").
- **Foto di un timbro in gomma loro**: non esiste. Le foto dei timbri sono del catalogo Trodat e non si usano.
- **Novità di stagione, newsletter, "Prova la tua impronta"**: restano tolti, come nel passaggio precedente.

### Caratteri e licenze

Encode Sans (Impallari Type, Andres Torresi, Jacques Le Bailly; Google Fonts), file variabile con peso 100-900 e larghezza 75-125 %, servito dalla pagina in `sito/fonts/` (latin e latin-ext). Licenza SIL Open Font License 1.1, uso commerciale libero; testo in `sito/fonts/OFL.txt`. Usati due pesi (400 e 700) e le larghezze 100 % (testo), 104-116 % (titoli, cifre, H1) e 84 % (H1 sul telefono).

### Foto, origine

| Dove | Foto | Origine |
|---|---|---|
| Che timbro vi serve | punzone in ottone per la stampa a caldo W.E. e ovale EUR 120x80 (`punzone-in-ottone-per-stampa-a-caldo.jpg`, 1000x1000, taglio 800x800) | libreria media del sito sanmarcotimbri.it, foto loro |
| Pulsantiere | pulsantiera in pietra con componenti in ottone lucido (1000x750) | idem |
| Targhe | targhe in ottone a rilievo TOILETTES e 101 (1000x750) | idem |
| Incisioni e scritte | lettere ritagliate a rilievo in ottone brunito (1000x1000, taglio 4:3, bianco neutro) | idem |
| Insegne | insegna traforata in metallo con cavallo (1000x1000, taglio 4:3) | idem |
| Segnaletica | targa in acciaio corten su pilastro (1000x666, taglio 648x486 senza prato e cielo) | idem; che sia loro va confermato |
| Premiazioni | trofeo in ottone su base in legno intarsiato (1000x750, taglio 800x600 senza i fogli) | idem |
| Testata e piede | logo orizzontale (JPEG 641x114) e logo verticale in bianco (dal PNG 256x200) | sito sanmarcotimbri.it |

Nessuna foto generata dall'IA, nessuna di repertorio, nessun marchio concorrente in primo piano. Diritti e consenso per i lavori fatti per clienti sono da confermare con l'azienda (LEGGIMI).

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
