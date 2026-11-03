# Etichettificio Veneto: proposta di nuova homepage

È una proposta non richiesta: c'è solo la home. Non è pubblicata, l'azienda non è stata contattata e non è stato inviato nessun modulo.

Versione di oggi: **livello professionale** (3 novembre 2026), con il ritocco finale dopo il controllore (facciata a tutta larghezza, apertura più asciutta, schede senza il "segno", tecniche prima della Stamperia, numeri del mestiere al posto degli anni, certificati in PDF, modulo più completo). La home precedente (etichetta in lamina oro, settori a schede, foto di repertorio) è copiata com'era in `_prova/versione-1-originale/` (sito e screenshot).

## Dove sono le cose

- `sito/index.html`: la home, statica (si apre anche con doppio clic). Accanto ci sono `sito/img/` (solo la facciata della sede in WebP, 8:3 a tutta larghezza e 4:3 per il telefono, il logo con la cornice e la favicon), `sito/doc/` (i due certificati TÜV NORD in PDF, ISO 9001 e FSC, presi dal loro sito) e `sito/fonts/` (Mona Sans con la sua licenza).
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (contatti e piede) e la `NOTA.md`, con l'esito delle 15 regole nella sezione "Livello professionale".
- `_prova/script/build_finale.sh`: rifà caratteri, immagini (`pro_img.py`), screenshot e controlli (`pro_controlli.mjs`, esito in `_prova/pro_controlli.json`). `etichetta_oro.py`, `immagini_finale.py` e `bobina_neutra.py` erano della versione 1 e non si usano più.
- `_prova/uso/SCHEDA.md`: chi apre il sito, che cosa viene a fare, le prove dei tre visitatori. `01-analisi.md`: i fatti con le fonti. `assets/CREDITI.md`: provenienza e licenze delle immagini.

## Il modulo del preventivo va collegato a un servizio

Il modulo in home (nome, azienda o "privato", email, telefono, settore, materiale, bobina o foglio, misure, quantità, varianti, consegna desiderata, colori e finiture, avvolgimento e anima, applicazione manuale o automatica, file grafico, note) oggi **non invia nulla**: controlla nome, azienda e un recapito, poi compone un'email a info@eveneto.com con oggetto "Richiesta di preventivo: <azienda>" e tutti i campi nel testo. Il file scelto non parte dal modulo: l'email scrive "File da allegare: <nome>" e chi scrive lo allega a mano (lo dice anche la pagina). Con una webmail senza gestore dei link mailto il clic non apre niente: per questo l'esito mostra anche l'indirizzo, ma è un ripiego.

Prima della pubblicazione va collegato a un servizio di invio vero, che accetti gli allegati (PDF, AI, EPS, JPG, fino a qualche decina di MB): per esempio il modulo del sito WordPress con caricamento file, o un servizio come Formspree o Basin, con la casella che riceve le richieste, l'avviso di ricezione a chi scrive con il riepilogo, e il link all'informativa privacy (la riga accanto al bottone c'è già). Il mailto resta solo come ripiego. I bottoni "Manda il file" restano email con oggetto "Ordine o invio file" e una traccia (azienda, referente, lavoro nuovo o ristampa, quantità, consegna).

## Da chiedere all'azienda (in pagina non c'è niente di inventato)

1. **Orari dell'ufficio.** In pagina c'è lunedì-venerdì 8-12 e 13.30-17.30, preso da 2GIS (dato vecchio, del 2012), con lo stato "Aperto ora / Chiuso" calcolato sull'ora di Roma, i festivi nazionali e Pasquetta. Vanno confermati prima di pubblicare, con le chiusure estive e di Natale, i ponti e il patrono di Saonara: lo script ha un elenco `CHIUSURE` (in fondo a `sito/index.html`, oggi vuoto) dove si scrivono i periodi, per esempio `['2027-08-09','2027-08-20']`, e in quei giorni la pagina dice "Chiuso per ferie, riapre lunedì 23 alle 8". Se l'orario non viene confermato, meglio togliere la riga "Aperto ora" e lasciare solo l'orario scritto.
2. **Email.** In pagina c'è solo info@eveneto.com (l'unica nell'informativa privacy; il dominio ha un server di posta attivo, ma il sito eveneto.com dice "SITO IN COSTRUZIONE"). Va confermato che la casella funziona, se per i file e gli ordini c'è un indirizzo diverso, e fino a che misura la posta accetta gli allegati: se c'è un limite, sotto "Manda il file" va una riga del tipo "file pesanti: un link di trasferimento nella stessa email" (non scritta in pagina finché non lo dicono loro). Per i solleciti di consegna: c'è un referente o un interno da indicare? Sul sito di oggi c'è anche etveneto@tin.it.
3. **Fax 049 644547.** È ancora attivo? Se no, va tolto dai contatti e dal piede.
4. **La Stamperia di Padova.** In pagina ci sono 049 640459, info@lastamperiadipadova.com e il sito, con le loro frasi (basse tirature, varianti, campionature, dorate e plastificate, consulenza grafica). Va confermato che la home dell'etichettificio può mandare lì i piccoli clienti, e se la Stamperia ha un indirizzo o un orario suo da scrivere.
5. **Recensioni (regola 10).** Non ne è stata trovata nessuna pubblica (Google Maps e Pagine Gialle non si leggono in automatico). Se hanno recensioni Google o lettere di clienti citabili, con nome e comune, vanno aggiunte.
6. **Clienti con il nome (regole 10 e 11).** Il sito dice "clienti in tutto il Nord Italia" ma non ne nomina nessuno. Servono 4-8 clienti citabili (nome e città, con il permesso) e almeno 3 lavori da mostrare: cliente o prodotto, anno, due o tre dati (tecnica, colori, supporto, tiratura). I 3 lavori entrano come sezione "Lavori" tra le tecniche e "Dal vostro file alla consegna", ognuno con la foto larga almeno metà pagina, il cliente o il prodotto, l'anno e 2-3 dati (tecnica, colori, supporto).
7. **Numeri aziendali.** In pagina ci sono solo numeri del mestiere (8 colori, 4 tecniche, 3 e 5 pagine, 1200 dpi del digitale della Stamperia, dalla SCHEDA: da confermare). Persone, metri quadri, macchine, anni di attività ("dal 1985" solo dopo la visura) e consegne all'anno vanno chiesti; le fonti oggi non concordano sulle persone (da 10 a 49).
8. **Parco macchine.** Quante flexo e quante digitali, che larghezza, se cold foil e stampa a caldo sono in linea: "fino a 8 colori" va legato a una macchina. La stampa a caldo (Europages) non è in pagina finché non la confermano.
9. **Certificati.** In pagina: UNI EN ISO 9001:2015 con TÜV NORD e la prima certificazione del 30 luglio 2009, FSC Chain-of-Custody con la licenza FSC-C146871 dal 2024. Il numero del certificato ISO e le scadenze non sono scritti in pagina, ma le schede hanno "Il certificato, in PDF": sono i due PDF già pubblicati sul loro sito (`wp-content/uploads/2026/07/Certificato-ISO-9001_ITA.pdf` e il certificato FSC di `wp-content/uploads/2024/05/`), copiati in `sito/doc/` perché il prototipo funzioni da file. Va confermato che vadano bene in home (e aggiornati alla scadenza: ISO 29/07/2027, FSC 03/03/2029), se si può usare il marchio FSC (servono le sue regole d'uso) e se mettere il link alla verifica della licenza nella banca dati pubblica FSC (indirizzo da prendere dal loro referente FSC, non scritto a caso).
10. **Consegna "con mezzi propri" e "clienti in tutto il Nord Italia".** Sono frasi del loro sito: va confermato che valgono ancora, e quali sono le "tratte" delle consegne periodiche.
11. **Vino e abbigliamento.** Il sito non parla di vino; "abbigliamento" è solo nella meta description, Europages cita "etichette e cartellini per abbigliamento". Restano fuori finché non li confermano.
12. **Pagine interne.** La home punta ai percorsi di oggi (`prodotti/...`, `servizi/...`, `azienda/certificazioni/`). "Non adesive e cartellini" e "Dorate e argentate" non hanno una pagina propria e puntano a `prodotti/` ("Tutti i prodotti") e alla pagina della cosmesi (link "Etichette per cosmesi, con cold foil"): conviene farne due pagine. Nel prototipo da file queste sottopagine non esistono: vanno controllate prima della pubblicazione.
13. **Logo vettoriale.** In pagina c'è il PNG del sito (337x187, con la cornice, il filo arancio e l'angolo sollevato), a circa 3x in testata. Per il sito vero serve il file originale.

## Foto da fare dal vero

In pagina c'è una sola foto, l'unica loro: la facciata della sede (6 su 10, 1920x720, cielo ritoccato, riflessi arancio sul ricciolo), ora a tutta larghezza nel suo 8:3 (4:3 sul telefono). A 1440 px su schermi retina servirebbe un file di 2880 px: è un motivo in più per rifarla. Niente repertorio, per decisione del committente: dove manca la foto, la pagina si regge su tipografia e fatti. Per arrivare al livello dei riferimenti servono, con un solo fotografo e la stessa luce:

1. **Facciata** (apertura, a tutta larghezza). In alta risoluzione, almeno 5000 px, orizzontale larga (va tagliata 8:3 a 1440 e 4:3 sul telefono, con la scritta al centro), con luce di fine giornata radente sulla lastra dorata, cielo pulito, senza i riflessi arancio. Meglio con un furgone dell'azienda davanti e una o due persone all'ingresso.
2. **Reparto** (una per ognuno dei sei settori, stesso taglio 4:3, regola 9): la flexo in stampa con il nastro che esce, mani sul nastro, la bobina stampata vista di taglio, un'etichetta multipagina aperta, il dettaglio in cold foil a luce radente, una striscia di bar code numerati, un sottobusta. Luce del posto, nessun flash diretto, colori neutri.
3. **Prestampa e cliché**: mani sul cliché, il tecnico al file grafico (per "Come lavoriamo").
4. **Le persone**: un ritratto della squadra davanti alla sede, e chi risponde al telefono (per i contatti).
5. **Il furgone** con il logo (per "Consegna rapida con mezzi propri").
6. **Lavori fatti** (regola 11): tre etichette dall'archivio, con il permesso dei clienti, fotografate sullo stesso fondo.

## Licenze

- **Mona Sans** (GitHub), da Google Fonts, SIL Open Font License 1.1. Uso commerciale libero. Servita dalla pagina (`sito/fonts/`), con il testo della licenza in `sito/fonts/OFL.txt`.
- **Facciata, loghi e certificati in PDF**: dell'azienda, presi dal suo sito.
- Nessuna foto di repertorio in pagina. Le foto Unsplash e Pexels della versione 1 sono elencate in `assets/CREDITI.md` e non sono più usate.

## Pagine del sito nuovo a cui punta la home

I percorsi sono gli stessi del sito di oggi, quindi non servono redirect: `azienda/`, `azienda/certificazioni/`, `prodotti/`, i quattro `prodotti/etichette-...`, i quattro `servizi/...`, `termini-duso-e-informative/informativa-privacy/`, `termini-duso-e-informative/#cookie`, `informativa-sullaccessibilita/`. Ancore della home: `#etichette`, `#tecniche`, `#lavoro`, `#stamperia`, `#qualita`, `#preventivo`, `#contatti`. Il preventivo è in home (`#preventivo`): la pagina `preventivo/` di oggi può restare con lo stesso modulo.

## Newsletter e social

Non ci sono. È un fornitore B2B su commessa e non ha profili social (nessun link nel codice, nessun risultato nelle ricerche). Se aprissero un profilo, nel piede va una colonna "Seguici" con i soli social che esistono.
