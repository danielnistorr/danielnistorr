# Oby Group Italia, home v2 (scheda d'uso)

Pagina: `sito-v2/index.html` (statica, si apre con file:///). Costruita sulla scheda `_prova/uso/SCHEDA.md`, non sulla home precedente (`sito/`, che resta com'è). Si rifà tutto con `sh _prova/uso/script/build_v2.sh`.

Schermate in questa cartella: `home-1440.jpg` (6910 px di altezza, piede compreso; 8330 px a 390; giro dei caratteri e delle impaginazioni del 2 novembre, vedi sotto), `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, più `home-1024.jpg`, `home-768.jpg`, `home-320.jpg`. Nessuno scorrimento orizzontale da 320 a 1440 (misurato), nessun U+2014.

## Cosa trova ogni visitatore, e dove

**1. Il danneggiato, da telefono, la sera del danno.**
- Senza scorrere, a 390x844: il loro claim "Quando il danno diventa serio, noi entriamo in azione"; una riga con cosa fanno e dove (incendi, allagamenti, grandine, amianto; case, condomini e aziende; pratiche burocratiche comprese; da Longare, VI, in Veneto e fuori regione); due bottoni alti 62 px "Chiama il cellulare 340 834 9597" e "Chiama gli uffici 0444 1329022"; il bottone "Manda le foto del danno" (mailto con oggetto "Foto del danno" e un testo già pronto: indirizzo, tipo di danno, nome e telefono, compagnia); il secondo cellulare 393 911 4656 con un'area di tocco di 44 px; quattro scorciatoie (Incendio, Allagamento, Grandine, Amianto). Scorrendo, una barra fissa in basso con "Cellulare" e "Uffici", ognuno col suo numero.
- Allo scorrimento successivo: i quattro danni, ognuno con una loro foto (miniatura di 88 px sul telefono) e una riga su cosa fanno.
- Poi il campo rosso "Nessuna incombenza burocratica, pensiamo noi a tutto": tre passi per il cliente (chiamata o foto, sopralluogo, pratiche) e sotto gli otto lavori di cantiere del loro pronto intervento, tutti in vista.

**2. L'ufficio sinistri, da computer.**
- Nella prima schermata a 1440 l'accesso "Compagnie assicurative e Starflex" porta con un clic alla sezione; il PDF è il secondo clic.
- Nella sezione: la loro frase "Meno costi oggi. Meno sinistri domani.", tre righe su cos'è Copertura Sicura Starflex, i quattro punti tecnici (senza rimozione né smaltimento, posa a freddo, anche sul bagnato, 30 anni dichiarati da MPM), "Per la compagnia: risarcimenti più bassi e chiusura dei sinistri più veloce", il bottone della documentazione tecnica (il loro PDF di 10 pagine, copiato in `sito-v2/doc/`), mail e uffici.
- Ragione sociale, P.IVA, REA, sede operativa e legale sono in chiaro nella sezione "Chi siamo" e nel piede, testo selezionabile. "Esclusiva" non compare; le certificazioni di MPM non sono attribuite a Oby.

**3. Il tecnico d'azienda, da computer.**
- Accesso "Aziende e bonifiche industriali" nella prima schermata.
- La sezione ha l'elenco completo con le loro parole: le 14 voci della home di oggi più le righe della pagina Pronto intervento (ATEX, serbatoi, silos e cisterne, escavatori a risucchio, reti gas, fune, sabbiature, fotovoltaico, manti stradali, smaltimento rifiuti). Si trovano tutte con Ctrl+F.
- Il gesto della pagina è qui: si segnano i lavori che servono e il bottone "Prepara la mail di richiesta" apre una mail a info@ con l'elenco già scritto nell'oggetto e nel testo, pronta per allegare capitolato e foto. Funziona col dito e con la tastiera (sono caselle vere); senza JavaScript il bottone apre comunque una mail di richiesta. Accanto, il telefono degli uffici.
- Le foto vere di cantiere accanto all'elenco: i tecnici in fune sulla pala eolica e il cunicolo; sotto, attrezzature e la richiesta dei documenti dell'impresa.

## Dopo le prove con i clienti tipo (rifinitura del 2 novembre)

Tre clienti tipo hanno provato la v2 (danneggiato da telefono 7,5; ufficio sinistri 7,5; tecnico d'azienda 7) e il giudice d'identità l'ha fermata a 51 su 80 (apertura da modello, fondo grigio, pagina lunga, ripetizioni). Cosa è cambiato:

**Uso**
- Danneggiato, telefono: la mail delle foto è un bottone a tutta larghezza alto 52 px con la busta ("Manda le foto del danno"); il secondo cellulare ha un'area di tocco di 44 px e sta staccato dalla mail. La zona è nella riga d'apertura: "Da Longare (VI), in Veneto e fuori regione". Le scorciatoie sono Incendio, Allagamento, Grandine, Amianto (Industria è nel menu). Mentre si scorre compare in basso una barra fissa di due metà, "Cellulare 340 834 9597" e "Uffici 0444 1329022", alta 64 px; resta nascosta finché si vedono i bottoni dell'apertura, senza animazioni (senza JavaScript resta sempre visibile). Il tasto "Chiama" senza numero della testata non c'è più sul telefono.
- Dopo la chiamata: prima dei lavori di cantiere ci sono tre passi per il cliente (ci chiami o ci mandi le foto; veniamo a vedere e ti diciamo cosa serve; seguiamo noi le pratiche, e se il danno è assicurato ci dici compagnia e numero del sinistro). "pensiamo noi a tutto" a 390 è a y=1710 (prima 3593), a 1440 a y=1669.
- Ufficio sinistri: il salto "Compagnie assicurative" arriva sul testo, non su una foto: a 1440x900 si leggono titolo "Copertura Sicura Starflex, per le compagnie assicurative", la frase della brochure "Meno costi oggi. Meno sinistri domani.", i quattro vantaggi e il bottone del PDF (y 629-698) senza scorrere; la foto è a fianco, alta 360 px. Accanto al PDF c'è la brochure aziendale, ora copiata in `sito-v2/doc/brochure-aziendale-2022.pdf` (non più dal dominio Wix), con edizione, pagine e peso. La mail per le compagnie è precompilata ("Affidaci un sinistro per mail": compagnia, numero sinistro, indirizzo del rischio, perito, tipo di danno).
- Verifica dell'impresa: "Chi siamo" e i contatti sono un blocco solo, con la tabella una volta sola (cellulari, uffici, mail, sede con mappa, interventi, documenti, ragione sociale, P.IVA, REA, sede legale). La riga "Documenti" apre una mail precompilata per chiedere visura, iscrizioni e abilitazioni; nessuna abilitazione è scritta come certa.
- Tecnico d'azienda: l'indirizzo info@ nella frase d'invito è un link; sotto il bottone c'è "Se la posta non si apre, scrivi a info@obygroupitalia.com" con l'indirizzo selezionabile; le due voci civili stanno in fondo sotto "Dopo un danno, anche in azienda"; dopo il salto "Aziende" il bottone "Prepara la mail di richiesta" è a y 799-856, nella schermata. Accanto all'elenco ci sono i due cantieri: la fune sulla pala eolica (spostata qui dalla chiusura) e il cunicolo, più "Attrezzature" e "Documenti dell'impresa".

**Identità e alta gamma**
- Fondo bianco pieno (#FFFFFF): l'unico cambio di fondo è il campo rosso del logo per il pronto intervento.
- Apertura nuova: il loro claim a tutta riga in due righe, poi tre colonne: telefoni e mail, la loro foto del tetto bruciato con due operatori al lavoro a misura vera (532 px su 567) e non a filo del bordo, le tre porte. È l'oggetto che dice il claim, "quando il danno diventa serio, noi entriamo in azione". Il condominio ponteggiato passa alla chiusura, a sinistra a filo del bordo.
- Titolo d'apertura a 700 e 60 px (prima 800 e 68), titoli di sezione a 700. I numeri di telefono grandi usano le cifre proporzionali.
- La scheda "Grandine e maltempo" è diventata "Grandine, maltempo e infiltrazioni": la foto è un'infiltrazione in mansarda.
- Il cunicolo è tagliato sotto la schiena: il logo sulla tuta, che sembra applicato dopo, resta fuori finché non è confermato.
- La scheda incendio usa un dettaglio delle travi bruciate dello stesso tetto, per non ripetere l'apertura.
- Ripetizioni tolte: niente secondo numero degli uffici in testata, niente richiamo "Hai un problema specifico?" con i due numeri, niente "Altro cellulare" nell'apertura a computer, porte con una sola riga sotto il titolo.
- Pagina più corta: 5501 px a 1440 (prima 6890), 8205 a 390 (prima 10909; dopo il giro dei caratteri 6910 e 8330); a 390 le schede danno hanno una miniatura di 88 px accanto al titolo e una riga di testo.

**Controlli dopo la rifinitura**: nessuno scorrimento orizzontale a 320, 390, 768, 1024 e 1440; nessuna U+2014; "esclusiva", "24 ore" e "Fig." assenti; 6 link `tel:+3904441329022`, 5 `tel:+393408349597`, 2 `tel:+393939114656`, mailto con oggetto e testo, mappa `google.com/maps/search/?api=1&query=Via+Ghizzole+41+36023+Longare+VI`. Prove dei salti e della barra: `_prova/uso/script/prova_rifinitura.mjs`; gesto: `prova_gesto_v2.mjs`.

**Respinto, con il motivo**
- Orari degli uffici e PEC: non sono pubblicati da nessuna parte; non si inventano. Restano tra le cose da confermare.
- "Iscrizione all'Albo gestori ambientali, categorie 4 e 5" scritta in pagina: viene dalla brochure 2022, che ha anche sede e anno sbagliati; al suo posto c'è la richiesta dei documenti per mail.
- Una riga di descrizione per le voci industriali che hanno solo il titolo (digestori, escavatori a risucchio, reti gas, smaltimento, manti stradali, fotovoltaico): nei loro testi non c'è altro e non si scrive al posto loro.
- Telo "Qui per voi" sul condominio come oggetto d'apertura: da vicino il telo porta un altro marchio a destra e non si legge come loro; senza conferma resta una foto di chiusura con didascalia neutra.
- Zero senza barra: il carattere (Atkinson Hyperlegible Next) non ha l'alternativa; lo zero barrato è parte della sua leggibilità e resta.
- Correggere il PDF Starflex ("esclusiva", "certificata", "Comagnie"): è un file di Oby e MPM, va rifatto da loro (vedi LEGGIMI).

## Caratteri, scala e impaginazioni (giro del 2 novembre)

Richiesta del committente: "usa più accoppiate di font e grandezze e layout mescolati". Cosa è cambiato, senza toccare i compiti dei visitatori.

**L'accoppiata.**
- **Big Shoulders Display** (Google Fonts, SIL Open Font License 1.1, testo in `sito-v2/fonts/OFL-big-shoulders.txt`; Patric King e Xotype, disegnato per la segnaletica civica di Chicago), variabile, usato in 700 e 800, servito dalla pagina (`sito-v2/fonts/big-shoulders-display-latin.woff2` e `-latin-ext`, 65 KB). È il carattere dei titoli: un grottesco stretto da cartello, quello che si legge su un furgone d'emergenza, su un cartello di cantiere o su una segnalazione stradale. Dice il loro claim, "noi entriamo in azione", con il tono di un'impresa che arriva sul posto, non di una galleria: diritto, alto, senza giochi. Stretto, permette al claim di stare in due righe a 116 px e ai nomi dei danni di stare grandi in una colonna stretta. Non è nelle liste della guida e nessun'altra home della campagna lo usa (Sofia Sans Condensed e Extra Condensed sono già di BCM Enologia e Daisyplast; Barlow Condensed è un tic di casa; Antonio, League Gothic, Mohave, Asap Condensed e Smooch Sans provati e scartati).
- **Atkinson Hyperlegible Next** resta il carattere del testo (vedi sotto): bottoni, telefoni dei bottoni e della barra, tabelle, didascalie, menu, elenco dei lavori. I numeri da comporre con il dito restano nel carattere con lo zero barrato.
- Due famiglie, nessun monospazio: i numeri tecnici (P.IVA, REA) usano le cifre tabellari di Atkinson. Ruoli fissi: Big Shoulders per h1, h2, i nomi dei danni, i numeri 1, 2, 3 dei passi, le frasi grandi ("Ti riconsegnamo il tuo bene nelle condizioni originarie.", "Meno costi oggi. Meno sinistri domani."), il cellulare grande della chiusura, i titoletti del piede e di "Attrezzature" e "Documenti dell'impresa"; Atkinson per tutto il resto. Mai due caratteri nello stesso paragrafo, nessun corsivo (`font-synthesis:none` sui titoli).

**La scala (1440 / 1024 / 390).** Otto livelli, con salti forti voluti tra il grande e il piccolo:
1. claim, Big Shoulders 800: 116 / 76 / 40 px (interlinea 0,9);
2. numeri grandi (1, 2, 3 dei passi; il cellulare della chiusura), Big Shoulders 700: 88 / 68 / 56 px;
3. titolo della sezione industria, Big Shoulders 700: 72 / 54 / 36 px;
4. titoli di sezione e frasi sole, Big Shoulders 700: 60 / 46 / 36 px;
5. nomi dei danni e nome Starflex, Big Shoulders 700: 48 / 34 / 28 px;
6. testo d'apertura delle sezioni e dei passi, Atkinson: 21 / 19 / 18 px;
7. testo, Atkinson 400: 17 px (16,5 a 390); voci dell'elenco 16,5 px 700; telefoni dei bottoni 26 px 700 (21 a 390), in un corpo loro;
8. didascalie, descrizioni dell'elenco e dati legali, Atkinson: 13,5 / 14,5 px.
H2 in tre misure (60, 72, 48 px). Le misure sono variabili CSS (`--s1` ... `--s8`) ridefinite a 1240, 1100 e 900 px.

**Un impianto per sezione, mai due uguali di fila.**
1. *Apertura*: il claim a tutta riga, enorme, sopra tre colonne 4/5/3 (telefoni e mail, la foto vera del tetto bruciato a misura sua, le tre porte). Stesso ordine di prima.
2. *Danni*: un **indice a righe a tutta larghezza**: nome grande in Big Shoulders a sinistra, cosa facciamo al centro, la foto a destra; un solo filetto nero in testa. Prima erano quattro colonne uguali. A 390 resta l'elenco con la miniatura di 88 px.
3. *Dopo la chiamata*, campo rosso: **due colonne sbilanciate a scacchiera** (5 e 6 colonne): in alto a sinistra il titolo, in basso a sinistra gli otto lavori di cantiere in una colonna; a destra i tre passi con il numero grande da 88 px, e in basso la frase sola "Ti riconsegnamo il tuo bene nelle condizioni originarie." a 60 px.
4. *Industria*: **titolo a tutta riga** a 72 px, l'elenco da segnare su **tre colonne** a tutta larghezza (due a 1024, una a 390), il bottone della mail sotto; poi un **mosaico di misure diverse**: la fune quadrata grande (5 colonne), il cunicolo orizzontale più piccolo allineato in basso (4 colonne), "Attrezzature" e "Documenti dell'impresa" in alto a destra.
5. *Assicurazioni*: **due colonne sbilanciate** (nome Starflex e la loro frase in rosso a 60 px a sinistra; testo, vantaggi, PDF e mail a destra), poi la loro foto del colmo rivestito in una **fascia a tutta larghezza** (1701 px, la misura piena dell'originale; a 390 resta il taglio 4:3).
6. *Chi siamo e contatti*: **testo a sinistra e foto a destra fino al bordo** (il condominio), il cellulare a 88 px in Big Shoulders rosso sopra la tabella dei recapiti. Prima la foto era a sinistra: ora si alterna con la sezione Starflex.
7. *Piede*: logo e riga su chi sono, quattro colonne di link con i titoletti in Big Shoulders, riga legale.

**L'uso, misurato dopo il cambio** (`_prova/uso/script/prima_390.mjs`, `prova_rifinitura.mjs`, `prova_gesto_v2.mjs`, `misura_v2.mjs`):
- 390x844, prima e dopo: claim 81-184 / 79-189; riga 196-316 / 197-316; "Chiama il cellulare" 334-396 / **330-392**; "Chiama gli uffici" 406-468 / **402-464**; "Manda le foto del danno" 478-530 / **474-526**; "Altro cellulare" 534-578 / **530-574**; scorciatoie 588-696 / **584-692**. Tutto 4 px più in alto, niente tolto né rimpicciolito. A 320: cellulare 349-411 / **336-398**.
- 1440x900: i bottoni di chiamata (488-561 e 571-645), la mail delle foto (657-709) e le tre porte (358-623) restano nella prima schermata; la foto finisce a 877.
- Salto "Compagnie assicurative": il PDF è a y 522-591 (prima 629-698). Salto "Aziende": "Prepara la mail di richiesta" a y 807-865 (prima 799-856), dentro la schermata. Il gesto funziona come prima, col dito e con la barra spaziatrice.
- "pensiamo noi a tutto": a 390 a y 1720 (prima 1710); a 1440 a y 2244 (prima 1669), perché l'indice dei danni è più alto; a 1440 si arriva con il menu "Dopo la chiamata".
- Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1440; nessuna sovrapposizione vista nelle schermate a pezzi; nessuna U+2014.
- Pagina: 6910 px a 1440 (prima 5501), 8331 a 390 (prima 8205), dentro il limite di 7000.
- `segnali.sh`: 17 soglie su 18, filetti 28 (alcuni filetti tolti: lavori di cantiere, vantaggi Starflex, righe dei danni), famiglie "OK" (Atkinson 91,5 %, Big Shoulders 8,5 %). Resta "da correggere" l'area coperta da foto (21,1 %, prima 23,7 %): la tipografia più grande allunga la pagina più di quanto la fascia Starflex aggiunga; il rimedio resta la giornata di fotografia del LEGGIMI, non le foto di repertorio. "Da guardare": i numeri 1, 2, 3 (sono i passi veri del cliente) e i titoli in 700-800 (un grottesco stretto da cartello regge il nero; il claim è uno solo).

**Respinto in questo giro, con il motivo**
- Un terzo carattere monospaziato per dati e didascalie: la guida lo sconsiglia (14 riferimenti su 15 non lo hanno) e Atkinson ha già le cifre tabellari e lo zero barrato.
- Telefoni dei bottoni e della barra in Big Shoulders: restano in Atkinson, il carattere disegnato per distinguere ogni cifra. Solo il cellulare grande della chiusura, a 88 px, passa al carattere dei titoli.
- Claim in maiuscolo: il loro claim è una frase, e il maiuscolo stretto diventerebbe un cartello di divieto.
- La fascia Starflex prima del testo: il salto "Compagnie assicurative" deve arrivare sul titolo e sul PDF, quindi la foto viene dopo.

## L'idea

Un'impresa d'azione che si chiama con un tocco. La pagina è prima di tutto un posto da cui telefonare, scritto con le loro frasi (il claim, "pensiamo noi a tutto", "Ti riconsegnamo il tuo bene nelle condizioni originarie", "Ripristiniamo a nuovo e tutto torna come prima"), con le loro foto vere a misura onesta e tre porte esplicite per i tre pubblici.

Scelte che non ci sono nelle altre home della campagna:
- **il claim a tutta riga sopra tre colonne** (telefoni, la foto vera a misura sua, le tre porte), su bianco pieno: la foto non è a filo del bordo e non è scontornata;
- **la chiusura che fonde chi siamo e contatti** in una sola tabella, con il condominio a destra fino al bordo;
- **un campo pieno nel rosso del logo** (#E41D25) per il loro pronto intervento, l'unico cambio di fondo forte della pagina;
- **la richiesta che si compone segnando i lavori**, invece di un gesto dimostrativo.

Niente legende numerate sull'oggetto, niente didascalie "Fig.", niente righello: i nove passaggi si leggono tutti insieme.

## Caratteri e colori

- **Big Shoulders Display** per i titoli (vedi "Caratteri, scala e impaginazioni"), SIL Open Font License 1.1, `sito-v2/fonts/OFL-big-shoulders.txt`.
- **Atkinson Hyperlegible Next** per il testo (Google Fonts, SIL Open Font License 1.1, testo della licenza in `sito-v2/fonts/OFL.txt`), variabile da 200 a 800, servito dalla pagina (`sito-v2/fonts/`, latin e latin-ext, 53 KB). È disegnato dal Braille Institute per essere letto da chi vede poco o ha fretta: ogni cifra e ogni lettera si distingue (lo zero barrato, la l e la I), ed è quello che serve a chi legge un numero di telefono la sera di un incendio. Cifre proporzionali per i telefoni, tabellari solo per P.IVA e REA. Non è nelle liste della guida e non è usato in nessun'altra home della campagna. Testo 400, etichette 500 e 600, voci e bottoni 700.
- **Colori**: fondo bianco #FFFFFF; inchiostro #231F20 (il nero del logo, 16,3:1); grigio #575D5B per i testi secondari (6,7:1); rosso #E41D25 del logo per i bottoni di chiamata, la barra del telefono e il campo del pronto intervento (bianco sul rosso 4,7:1); rosso #C4161C per il numero grande della chiusura e la frase Starflex (6,0:1). Contrasto AA su tutti i testi.

## Foto: origine e licenza

Tutte le foto della pagina vengono dal sito di Oby (`assets/originali/`, scaricate il 24/10/2026), nessuna di repertorio, nessuna generata dall'IA. Lavorate con PIL (`_prova/uso/script/img_v2.py`: contrasto +5 %, saturazione -6 %, nitidezza leggera) e mai ingrandite oltre la loro misura in modo visibile.

| Dove | File | Soggetto | Note |
|---|---|---|---|
| Apertura | `9e96e5_719b9e17…jpg` 567x522 | tetto bruciato dall'alto con due operatori | a 1440 a 532 px, sotto la misura vera; a 390 una striscia |
| Incendio | `9e96e5_719b9e17…jpg` 567x522 | dettaglio delle travi bruciate | stesso scatto dell'apertura, altro taglio |
| Allagamento | `9e96e5_35be21fc…jpg` 850x585 | locale tecnico allagato | |
| Grandine, maltempo e infiltrazioni | `9e96e5_b269c5a1…jpg` 1155x1062 | mansarda con le macchie d'acqua | sul sito oggi sta sotto "ambienti confinati": va confermato che è un danno da infiltrazione |
| Amianto | `9e96e5_080feb51…jpg` 567x528 | tetto in fibrocemento | |
| Industria | `9e96e5_ec8a1c18…jpg` 450x496 | operatore in tuta bianca nel cunicolo | tagliato sotto la schiena, senza il logo da confermare |
| Starflex | `9e96e5_c7d17813…webp` 1701x1687 | fibrocemento rivestito accanto al fotovoltaico, con le colline | fascia a tutta larghezza a 1440 (taglio 1701x630, `starflex-banda-*`), 4:3 a 390; forse foto di MPM: uso da confermare |
| Industria | `9e96e5_4e684abe…jpg` 582x584 | due tecnici in fune su una pala eolica | a 1440 a 533 px, sotto la misura vera; provenienza incerta |
| Chiusura | `9e96e5_2da1fe53…jpg` 733x774 | condominio di 11 piani ponteggiato | a destra fino al bordo, sotto la misura vera |

La foto Starflex con lo skyline di Milano non è usata. Le Pexels della home precedente non sono usate.

## Controlli

- `segnali.sh` (prima della rifinitura): 16 soglie su 18. Restava l'area coperta da foto, bassa perché le loro foto vere sono poche e piccole: il rimedio è la giornata di fotografia scritta nel LEGGIMI, non le Pexels.
- Prove della scheda dopo la rifinitura, a 390x844: due bottoni di chiamata con il numero scritto, interamente sopra y=844, alti 62 px; "Allagamento" a y=588 e "Longare (VI)" a y=196; il bottone delle foto a y=478; "pensiamo noi a tutto" a y=1710; barra di chiamata visibile a metà pagina. A 1440: porte "Compagnie assicurative" e "Aziende e industria" senza scorrere, PDF in due clic, bottone della richiesta nella schermata dopo il salto.
- Gesto provato con il dito e con la barra spaziatrice (`_prova/uso/script/prova_gesto_v2.mjs`): due lavori segnati finiscono nell'oggetto e nel testo della mail.

## Niente newsletter

Oby è un servizio d'emergenza su chiamata e su incarico: chi lo cerca lo fa dopo un danno, e non ci sono novità, fiere o cataloghi periodici da comunicare. Per le compagnie basta il PDF Starflex scaricabile.

## Da confermare con l'azienda

1. Chi risponde fuori orario e se c'è reperibilità 24 ore su 24; gli orari degli uffici. In pagina oggi ci sono solo i due numeri con il loro nome ("Cellulare", "Uffici") e nessun orario.
2. Si può aggiungere WhatsApp sul cellulare per le foto del danno?
3. La zona servita: in pagina c'è solo "in Veneto e fuori regione" (la brochure 2022 elenca sedi operative in Veneto, Lombardia, Emilia Romagna, Toscana, Friuli Venezia Giulia). Qual è l'elenco giusto oggi?
4. La riga "Pratiche burocratiche comprese" e "segue anche le pratiche": comprendono il rapporto con l'assicurazione o il perito?
5. Le foto: quali sono di loro cantieri (condominio, pala eolica, cunicolo con il logo sulla tuta, mansarda); le due Starflex sono di Oby o di MPM e si possono usare?
6. "Robot certificati ATEX" ed "escavatori a risucchio": sono mezzi loro o a noleggio? Le abilitazioni (Albo gestori ambientali, categoria per l'amianto, ATEX, fune, ambienti confinati) non sono pubblicate e non sono in pagina.
7. Starflex: uso del marchio STARFLEX® e del nome MPM; i 30 anni sono scritti come dichiarazione di MPM; la polizza postuma decennale non è in pagina finché non si sa chi la rilascia.
8. L'anno di nascita (2018 sul sito, 2011 nella brochure 2022): non è in pagina.
9. La brochure aziendale 2022 ha ancora Grisignano e il 2011: ora è copiata in `sito-v2/doc/` con l'etichetta "edizione 2022", ma va rifatta con Longare. Anche il PDF Starflex scrive "esclusiva", "durabilità certificata" e "Comagnie": va corretto da Oby e MPM prima di metterlo in linea. Il PDF Starflex va caricato sul sito nuovo (nella proposta è in `sito-v2/doc/`).
10. Privacy e Cookie vanno scritte (l'informativa di oggi è di uno studio legale); la pagina Facebook è attiva?
11. Il telo sul ponteggio del condominio (Q ad anello rosso, "Qui per voi") è loro? Che lavoro hanno fatto su quel condominio, e dove? La didascalia oggi è neutra.
12. Il tetto bruciato dell'apertura è un loro cantiere, e i due operatori sul tetto sono loro?
13. Chi tiene i rapporti con la compagnia e il perito dopo un sinistro (il terzo passo dice solo "seguiamo noi le pratiche burocratiche")?
14. Orari degli uffici e PEC, da scrivere accanto al numero degli uffici e nella tabella dei contatti.
15. Iscrizioni e abilitazioni con numero ed ente (Albo gestori ambientali con le categorie, amianto, ambienti confinati, lavori in fune, ATEX), da scrivere nella riga "Documenti" al posto della richiesta per mail.
