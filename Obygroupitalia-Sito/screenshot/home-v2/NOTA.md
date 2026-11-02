# Oby Group Italia, home v2 (scheda d'uso)

Pagina: `sito-v2/index.html` (statica, si apre con file:///). Costruita sulla scheda `_prova/uso/SCHEDA.md`, non sulla home precedente (`sito/`, che resta com'è). Si rifà tutto con `sh _prova/uso/script/build_v2.sh`.

Schermate in questa cartella: `home-1440.jpg` (5501 px di altezza, piede compreso; 8205 px a 390), `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, più `home-1024.jpg`, `home-768.jpg`, `home-320.jpg`. Nessuno scorrimento orizzontale da 320 a 1440 (misurato), nessun U+2014.

## Cosa trova ogni visitatore, e dove

**1. Il danneggiato, da telefono, la sera del danno.**
- Senza scorrere, a 390x844: il tasto rosso "Chiama" fisso nella testata (chiama il cellulare, resta visibile a ogni altezza di scorrimento); il loro claim "Quando il danno diventa serio, noi entriamo in azione"; una riga con cosa fanno e da dove (incendi, allagamenti, grandine, amianto; case, condomini e aziende; pratiche burocratiche comprese; da Longare, VI); due bottoni alti 62 px "Chiama il cellulare 340 834 9597" e "Chiama gli uffici 0444 1329022"; il link "Manda le foto del danno per mail" (mailto con oggetto "Foto del danno" e un testo già pronto: indirizzo, tipo di danno, nome e telefono, compagnia); il secondo cellulare 393 911 4656; quattro scorciatoie (Incendio, Allagamento, Grandine e tetti, Industria); sotto, la striscia della loro foto del condominio ponteggiato.
- Allo scorrimento successivo: i quattro danni, ognuno con la loro riga vera, una loro foto e cosa salvano; il richiamo "Hai un problema specifico? Chiamaci subito." con i due numeri.
- Poi il campo rosso "Nessuna incombenza burocratica, pensiamo noi a tutto": i nove passaggi del loro pronto intervento tutti in vista, in ordine, e di nuovo il link per mandare le foto.

**2. L'ufficio sinistri, da computer.**
- Nella prima schermata a 1440 l'accesso "Compagnie assicurative e Starflex" porta con un clic alla sezione; il PDF è il secondo clic.
- Nella sezione: la loro frase "Meno costi oggi. Meno sinistri domani.", tre righe su cos'è Copertura Sicura Starflex, i quattro punti tecnici (senza rimozione né smaltimento, posa a freddo, anche sul bagnato, 30 anni dichiarati da MPM), "Per la compagnia: risarcimenti più bassi e chiusura dei sinistri più veloce", il bottone della documentazione tecnica (il loro PDF di 10 pagine, copiato in `sito-v2/doc/`), mail e uffici.
- Ragione sociale, P.IVA, REA, sede operativa e legale sono in chiaro nella sezione "Chi siamo" e nel piede, testo selezionabile. "Esclusiva" non compare; le certificazioni di MPM non sono attribuite a Oby.

**3. Il tecnico d'azienda, da computer.**
- Accesso "Aziende e bonifiche industriali" nella prima schermata.
- La sezione ha l'elenco completo con le loro parole: le 14 voci della home di oggi più le righe della pagina Pronto intervento (ATEX, serbatoi, silos e cisterne, escavatori a risucchio, reti gas, fune, sabbiature, fotovoltaico, manti stradali, smaltimento rifiuti). Si trovano tutte con Ctrl+F.
- Il gesto della pagina è qui: si segnano i lavori che servono e il bottone "Prepara la mail di richiesta" apre una mail a info@ con l'elenco già scritto nell'oggetto e nel testo, pronta per allegare capitolato e foto. Funziona col dito e con la tastiera (sono caselle vere); senza JavaScript il bottone apre comunque una mail di richiesta. Accanto, il telefono degli uffici.
- La foto vera di cantiere: l'operatore nel cunicolo; in chiusura i due tecnici in fune sulla pala eolica.

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
- Pagina più corta: 5501 px a 1440 (prima 6890), 8205 a 390 (prima 10909); a 390 le schede danno hanno una miniatura di 88 px accanto al titolo e una riga di testo.

**Controlli dopo la rifinitura**: nessuno scorrimento orizzontale a 320, 390, 768, 1024 e 1440; nessuna U+2014; "esclusiva", "24 ore" e "Fig." assenti; 6 link `tel:+3904441329022`, 5 `tel:+393408349597`, 2 `tel:+393939114656`, mailto con oggetto e testo, mappa `google.com/maps/search/?api=1&query=Via+Ghizzole+41+36023+Longare+VI`. Prove dei salti e della barra: `_prova/uso/script/prova_rifinitura.mjs`; gesto: `prova_gesto_v2.mjs`.

**Respinto, con il motivo**
- Orari degli uffici e PEC: non sono pubblicati da nessuna parte; non si inventano. Restano tra le cose da confermare.
- "Iscrizione all'Albo gestori ambientali, categorie 4 e 5" scritta in pagina: viene dalla brochure 2022, che ha anche sede e anno sbagliati; al suo posto c'è la richiesta dei documenti per mail.
- Una riga di descrizione per le voci industriali che hanno solo il titolo (digestori, escavatori a risucchio, reti gas, smaltimento, manti stradali, fotovoltaico): nei loro testi non c'è altro e non si scrive al posto loro.
- Telo "Qui per voi" sul condominio come oggetto d'apertura: da vicino il telo porta un altro marchio a destra e non si legge come loro; senza conferma resta una foto di chiusura con didascalia neutra.
- Zero senza barra: il carattere (Atkinson Hyperlegible Next) non ha l'alternativa; lo zero barrato è parte della sua leggibilità e resta.
- Correggere il PDF Starflex ("esclusiva", "certificata", "Comagnie"): è un file di Oby e MPM, va rifatto da loro (vedi LEGGIMI).

## L'idea

Un'impresa d'azione che si chiama con un tocco. La pagina è prima di tutto un posto da cui telefonare, scritto con le loro frasi (il claim, "pensiamo noi a tutto", "Ti riconsegnamo il tuo bene nelle condizioni originarie", "Ripristiniamo a nuovo e tutto torna come prima"), con le loro foto vere a misura onesta e tre porte esplicite per i tre pubblici.

Scelte che non ci sono nelle altre home della campagna:
- **titolo d'apertura pieno, peso 800**, al posto dei titoli sottili: è il loro tono secco e il nero pieno della scritta del logo;
- **foto verticale a tutta altezza a filo del bordo destro e sotto la testata**, accanto a un elenco di tre porte impilate (non un oggetto scontornato con legende);
- **un campo pieno nel rosso del logo** (#E41D25) per il loro pronto intervento, l'unico cambio di fondo forte della pagina;
- **la richiesta che si compone segnando i lavori**, invece di un gesto dimostrativo.

Niente legende numerate sull'oggetto, niente didascalie "Fig.", niente righello: i nove passaggi si leggono tutti insieme.

## Caratteri e colori

- **Atkinson Hyperlegible Next** (Google Fonts, SIL Open Font License 1.1, testo della licenza in `sito-v2/fonts/OFL.txt`), un solo carattere variabile da 200 a 800, servito dalla pagina (`sito-v2/fonts/`, latin e latin-ext, 53 KB). È disegnato dal Braille Institute per essere letto da chi vede poco o ha fretta: ogni cifra e ogni lettera si distingue (lo zero barrato, la l e la I), ed è quello che serve a chi legge un numero di telefono la sera di un incendio. Ha le cifre tabellari, usate per tutti i numeri. Non è nelle liste della guida e non è usato in nessun'altra home della campagna. Titoli 700 e 800, testo 400, etichette 500 e 600.
- **Colori**: fondo #F2F4F3, un bianco freddo come le tute monouso e la membrana bianca di Starflex che compaiono nelle loro foto; inchiostro #231F20 (il nero del logo); grigio #575D5B per i testi secondari (5,5:1 sul fondo); rosso #E41D25 del logo per i bottoni di chiamata e il campo del pronto intervento (bianco sul rosso 4,7:1); rosso #C4161C per il numero grande della chiusura su fondo chiaro (5,5:1). Piede su bianco. Contrasto AA su tutti i testi.

## Foto: origine e licenza

Tutte le foto della pagina vengono dal sito di Oby (`assets/originali/`, scaricate il 24/10/2026), nessuna di repertorio, nessuna generata dall'IA. Lavorate con PIL (`_prova/uso/script/img_v2.py`: contrasto +5 %, saturazione -6 %, nitidezza leggera) e mai ingrandite oltre la loro misura in modo visibile.

| Dove | File | Soggetto | Note |
|---|---|---|---|
| Apertura | `9e96e5_719b9e17…jpg` 567x522 | tetto bruciato dall'alto con due operatori | a 1440 a 532 px, sotto la misura vera; a 390 una striscia |
| Incendio | `9e96e5_719b9e17…jpg` 567x522 | dettaglio delle travi bruciate | stesso scatto dell'apertura, altro taglio |
| Allagamento | `9e96e5_35be21fc…jpg` 850x585 | locale tecnico allagato | |
| Grandine e maltempo | `9e96e5_b269c5a1…jpg` 1155x1062 | mansarda con le macchie d'acqua | sul sito oggi sta sotto "ambienti confinati": va confermato che è un danno da infiltrazione |
| Amianto | `9e96e5_080feb51…jpg` 567x528 | tetto in fibrocemento | |
| Industria | `9e96e5_ec8a1c18…jpg` 450x496 | operatore in tuta bianca nel cunicolo | tagliato sotto la schiena, senza il logo da confermare |
| Starflex | `9e96e5_c7d17813…webp` 1701x1687 | fibrocemento rivestito accanto al fotovoltaico | forse foto di MPM: uso da confermare |
| Industria | `9e96e5_4e684abe…jpg` 582x584 | due tecnici in fune su una pala eolica | provenienza incerta |
| Chiusura | `9e96e5_2da1fe53…jpg` 733x774 | condominio di 11 piani ponteggiato | a filo del bordo sinistro, misura vera |

La foto Starflex con lo skyline di Milano non è usata. Le Pexels della home precedente non sono usate.

## Controlli

- `segnali.sh`: 16 soglie su 18 a posto. Restano due da correggere, con il motivo:
  - area coperta da foto 23,7 % contro il 35 %: le loro foto vere sono poche e piccole (da 450 a 1155 px) e la scheda chiede di non presentare repertorio come lavoro loro. Il rimedio è la giornata di fotografia scritta nel LEGGIMI, non le Pexels;
  - un titolo in due frasi, "Meno costi oggi. Meno sinistri domani.": è la frase della loro brochure 2026 per le assicurazioni, lasciata com'è.
- Prove della scheda a 390x844: due bottoni di chiamata con il numero scritto, interamente sopra y=844, alti 62 px; "Allagamento" a y=534 e "Longare (VI)" a y=202; il mailto delle foto a y=463; "pensiamo noi a tutto" nella seconda sezione; tasto Chiama visibile a metà pagina. A 1440: accesso "assicurazioni" e "Starflex" senza scorrere, PDF in due clic.
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
