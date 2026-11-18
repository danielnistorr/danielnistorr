# Lavoro & Salute: cosa c'è e cosa confermare con la struttura

## Cosa c'è

- `sito/`: versione finale statica. `index.html` (le due porte), `lavoro.html` (aziende), `salute.html` (poliambulatorio), `note-legali.html`, `stile.css`, `font/` (Hind, OFL), `img/`. Si apre con un doppio clic su `index.html`. Non è pubblicato da nessuna parte.
- `screenshot/`: per home, lavoro e salute, pagina intera e prima schermata a 1440 e a 390 (JPEG qualità 85), con `NOTA.md` (idea, contenuti, caratteri, colori, foto, controlli).
- Sorgenti: `_prova/script/sito_build.py` (compone le pagine: testata, piede e arco comuni), `sito_ritratti.py` (ritratti 4:5 con fondo uniforme), `sito_foto.py` (foto di repertorio), `sito_scatti.sh` (screenshot), `sito_controlli.mjs` (sbordamenti, immagini, ancore). Dopo una modifica: `python3 -I _prova/script/sito_build.py sito` e poi gli screenshot.
- Analisi, riferimenti e norme: `01-analisi-sito-attuale.md`, `02-riferimenti.md`, `03-norme-comunicazione-sanitaria.md`. Crediti delle immagini: `assets/CREDITI.md`.
- Le pagine non contengono segnaposto a vista: tutto ciò che non è confermato è stato tolto dalla pagina ed è elencato qui.

## Da confermare prima di pubblicare (obblighi di legge, vedi 03)

1. **Direttore sanitario.** Nel piede di ogni pagina c'è "Dott. Marco Lo Savio, specialista in medicina del lavoro, iscritto all'Ordine dei Medici di Padova n. PD-8617". Il ruolo viene da un PDF del 2016 del sito attuale, il numero dal suo curriculum. [DA CONFERMARE che sia in carica oggi e il numero sull'albo FNOMCeO.]
2. **Autorizzazione all'esercizio.** Il piede dice "Poliambulatorio privato autorizzato all'esercizio dal 2006" (frase del sito attuale). Vanno aggiunti ente, numero e data: "autorizzato dal Comune di Limena, aut. n. [DA CONFERMARE] del [DA CONFERMARE]" (L.R. Veneto 22/2002; D.Lgs 70/2003, art. 7). E l'elenco delle specialità autorizzate dopo il 2006.
3. **Dati societari.** Mancano nel piede: numero REA PD [DA CONFERMARE], capitale sociale versato (il PDF 2016 dice 40.000,00 euro; va scritto "interamente versato" o la somma versata) [DA CONFERMARE], socio unico sì o no [DA CONFERMARE], PEC [DA CONFERMARE]. Ufficio del Registro imprese scritto come Padova (sede a Limena): [DA CONFERMARE].
4. **Trasparenza (L. 24/2017).** Serve una pagina collegata dal piede con la compagnia e il contratto di assicurazione RC, i risarcimenti degli ultimi cinque anni (anche "nessuno") e la relazione annuale sugli eventi avversi. Non c'è nel sito perché mancano i dati [DA FORNIRE].
5. **Privacy.** In `note-legali.html` ci sono solo il titolare e l'uso dei moduli. Serve l'informativa completa (artt. 13-14 GDPR): finalità, base giuridica, conservazione, destinatari, diritti [DA FORNIRE].
6. **Moduli.** Preventivo e appuntamento non inviano nulla (`data-prova`, invio bloccato). Da decidere: indirizzo di destinazione, servizio di invio, tempi di conservazione. Nessun campo chiede dati sanitari: va mantenuto così.

## Specialità e medici

- **Pubblicate** solo le specialità con il nome e il titolo del responsabile (L. 175/1992, art. 4, c.1): dermatologia e venereologia (Dott.ssa Stefania Bano), fisiatria (Dott.ssa Raffaella Riviezzo, Dott.ssa Loreta Greco), medicina aeronautica (Dott. Marco Lo Savio), medicina legale (Dott. Arcangelo Di Nino), otorinolaringoiatria (Dott. Ivan Turco). [DA CONFERMARE che ricevano tutti oggi e in quali giorni.]
- **Tolte finché non arriva nome e titolo del responsabile**: chirurgia ambulatoriale, diagnostica ecografica ed eco doppler, ginecologia e ostetricia, ortopedia, psicologia e psicoterapia, oculistica (la Dott.ssa Vuga Ana Grgic c'è ancora?), scienze dell'alimentazione (il Dott. Salvatore Iacopetta c'è ancora?). **Medicina estetica** tolta: se resta, va riscritta secondo 03 (niente marchi di farmaci, niente promesse, niente immagini di volti). Per rimetterle basta aggiungere una voce alla lista `SPEC` in `sito_build.py` con responsabile e prestazioni.
- **Prestazioni elencate** (al massimo cinque per specialità, dal sito attuale): [DA CONFERMARE che siano svolte oggi]. La riabilitazione del pavimento pelvico viene dal curriculum della Dott.ssa Greco e da iDoctors.
- **Schede dei medici**: specializzazioni dalle pagine del sito attuale. Numero d'iscrizione all'Ordine pubblicato solo dove il sito lo riporta (Lo Savio PD-8617, Turco 09272, Riviezzo 8842). Mancano i numeri di Bano (Padova), Di Nino (Venezia) e Greco (Padova) [DA CONFERMARE]. Tutti i nomi e i titoli vanno verificati sull'albo FNOMCeO.
- "Elenco nazionale dei medici competenti n. 16735" (didascalia del Dott. Lo Savio nella pagina Lavoro) e "esaminatore aeromedico ENAC IT-1012-AME": dal suo curriculum [DA CONFERMARE].
- **Ritratti**: consenso scritto di ogni medico [DA CONFERMARE]. Ai fondi di Turco, Di Nino e Greco è stato sostituito lo sfondo (poltrone arancio, parete marrone) con un grigio chiaro: da dire ai medici. Meglio un servizio di ritratti nuovi tutti uguali (stesso fondo chiaro, stessa luce, camice). Il ritratto del Dott. Lo Savio apre la pagina Lavoro: consenso anche per questo uso.

## Orari, tariffe, convenzioni

- **Orari**: in tutto il sito "Lunedì-venerdì 9.00-12.30 e 14.30-19.00, sabato e domenica chiuso" (testata Lavoro e testo delle prenotazioni del sito attuale). La testata Salute del sito attuale dice 9-19 continuato. [DA CONFERMARE quale vale, ed eventuali aperture il sabato o chiusure estive.]
- **Tariffe**: nessuna pubblicata. Le uniche del sito attuale (medicina aeronautica "Tipo 1-3 Euro 90,00 / tipo 2 Euro 65,00") vanno riscritte in chiaro (quale certificato, prima visita o rinnovo, IVA o esenzione) e confermate prima di pubblicarle.
- **Convenzioni**: in Lavoro c'è una riga sulla convenzione per dipendenti e familiari delle aziende seguite, "alle condizioni del contratto", senza vantaggi economici (03: niente agevolazioni pubblicizzate) [DA APPROVARE]. Nessuna convenzione con il Servizio sanitario o con assicurazioni è dichiarata [DA CONFERMARE].

## Area Lavoro

- Servizi presi dal sito attuale [DA CONFERMARE che siano ancora offerti]: rilievi fonometrici, stress lavoro-correlato, DUVRI, PIMUS, corsi carrellisti, test per alcol e droghe, visite in azienda, scadenzario delle visite periodiche.
- Formazione: solo i nomi dei corsi. Durate e validità non pubblicate finché non si verifica l'Accordo Stato-Regioni del 2025; il PDF dell'Accordo 2011 non va ripreso. Rapporto con "L&S Formazione e Sicurezza" [DA CONFERMARE].
- Non inclusi (da confermare se offerti): tarature, verifiche di messa a terra, SOA, modello 231, sistemi ISO, servizio medico per strutture turistiche, formazione finanziata.
- Zona servita "province di Padova e Vicenza": dalle pagine del sito attuale [DA CONFERMARE].

## Foto da sostituire

- [DA SOSTITUIRE con foto della struttura] tipografo alla macchina da stampa (porta Lavoro, Pexels 6621000) e falegname alla sega circolare (home e pagina Lavoro, Pexels 28513061). Sono di repertorio, con licenza Pexels "Free" verificata: non sono la struttura né un'azienda cliente.
- Brief delle foto da fare: facciata e ingresso di Via S. Felice e Fortunato 26, segreteria, sala d'attesa, ambulatori (cabina audiometrica, ecografo, poltrona ORL), aula di formazione, un sopralluogo vero in un'azienda cliente (con il suo permesso; mani, dispositivi di protezione, nessun volto riconoscibile senza liberatoria), ritratti nuovi dei medici. Con le foto vere anche le pagine Lavoro e Salute supereranno la soglia di area foto (oggi 17,9 % e 12,1 %).
- Mappa: disegnata da OpenStreetMap; il civico 26 non è in OSM e la via è evidenziata per intero [DA CONFERMARE la posizione esatta]. Logo in vettoriale [DA CONFERMARE].

## Testi da far approvare

Tutti i testi sono nuovi e brevi, scritti secondo 03; vanno letti e approvati dalla struttura, in particolare:
- le righe delle porte ("Medicina del lavoro e sicurezza per le aziende di Padova e Vicenza", "Visite specialistiche su appuntamento a Limena") e la frase "Stesso indirizzo e stesso telefono per le aziende e per i pazienti";
- i tre passi per le aziende ("Sopralluogo: il medico vede reparti e mansioni", "Protocollo sanitario: sulla base del documento di valutazione dei rischi", "Visite e giudizio di idoneità: in sede o in azienda, con lo scadenzario delle visite periodiche");
- le righe delle specialità e il modo di prenotare ("la segreteria ti richiama per fissare giorno e ora");
- la nota sui cookie (vera solo finché il sito non aggiunge statistiche, mappe incorporate o altri servizi di terzi).
