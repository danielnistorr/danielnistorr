# Finiture S.r.l.: proposta di nuova home

Proposta non richiesta, solo la home. Nulla è stato inviato all'azienda né pubblicato.

- Pagina: `sito/index.html` (si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`.
- Screenshot e nota di progetto, con l'esito delle 15 regole: `screenshot/home/` (`NOTA.md`, sezione "Livello professionale").
- Per rifare immagini, screenshot e controlli: `bash _prova/script/build_finale.sh` (usa `pro_img.py`, `pro_shoot.mjs`, `pro_controlli.mjs`). La pagina è scritta a mano: i vecchi `finale_pagina.py` e `finale_*.mjs` sono della versione 1 e non vanno rilanciati.
- Versione 1 (24/10/2026) com'era: `_prova/versione-1-originale/`. Scheda d'uso e d'identità: `_prova/uso/SCHEDA.md`. Analisi con le fonti: `01-analisi.md`.

## Da collegare prima di pubblicare

- **Modulo "Richiedi un progetto"** (sezione Contatti). Oggi controlla i campi obbligatori e compone un'email a info@finiture.it con oggetto e campi; i disegni scelti vengono solo elencati nel testo, perché un `mailto:` non porta allegati, e chi scrive deve aggiungerli a mano. Va collegato a un servizio che riceva il modulo con gli allegati (fino a qualche decina di MB per DWG e STEP), con l'informativa privacy, una risposta automatica nella lingua scelta e l'inoltro all'ufficio tecnico. Il codice ha già il punto di aggancio (`finitureMail` nello script in fondo alla pagina).
- **Stato "Assistenza aperta ora"**: calcolato nel browser in ora italiana, lun-ven 8:30-12:00 e 14:00-17:30, con i festivi nazionali e Pasquetta. Mancano il patrono di Saonara e le chiusure aziendali (agosto, Natale): vanno chiesti e aggiunti.
- **Newsletter**: tolta dal piede finché non c'è il servizio (oggi il modulo del sito vecchio non si sa se sia attivo). Quando c'è, torna nel piede con il doppio consenso.
- **Pagine a cui puntano i link**: Impianti (`impianti/finestre.html`, `porte.html`, `clt.html`, `sedie-mobili.html`), Macchine (`macchine.html`, `macchine/trasporto.html`, `impregnazione.html`, `robot.html`, `cabine.html`, `essiccazione.html`, `acqua.html`, `handling.html`), `azienda.html`, `area-test.html`, `assistenza.html`, `usato.html`, `notizie.html`, `privacy.html`, `cookie.html`, e le versioni `en/`, `de/`, `fr/`, che per questo pubblico vengono prima dell'italiana (scheda, par. 1). Social: LinkedIn e YouTube.

## Cosa chiedere all'azienda

1. **Clienti e testimonianze**: se si possono nominare in home Distner, Setz Fensterbau, Millet, Bruppacher, Malenfer e Arlt, e se le cinque frasi firmate (Wagner Fenster+Türen, Menuiserie Zimmermann, Huber & Sohn, Menuiserie Foray, Betz Fensterbau) si possono ripubblicare. La frase di Huber & Sohn è riportata come sul sito, senza l'inizio ("…per aver configurato i robot"): chiedere la frase intera.
2. **Anni e numeri delle linee**: l'anno di consegna di Setz, Millet, Bruppacher, Malenfer e Arlt (in pagina c'è solo Distner, ottobre 2026) e se barre, robot, colori e misure sono ancora quelli giusti. Millet viene da un post LinkedIn di circa febbraio 2026.
3. **Assistenza**: se esiste un numero o un'email di assistenza dedicati, cosa si fa fuori orario, chi risponde in tedesco e in francese. In pagina c'è info@finiture.it con la traccia "azienda, impianto, matricola, cosa succede".
4. **Area test**: confermare che è nella sede di Viale Veneto 13/15 a Villatora di Saonara e che l'attrezzatura (flow coating verticale, robot RAS, cabina, tunnel LDP, ventilatori assiali, lampade alogene) è quella di oggi; cosa conviene portare per una prova.
5. **Numeri dell'azienda**: le persone di oggi (in pagina "40", dalla notizia del 2024 "Adesso siamo in 40"; Atoka 39-41, LinkedIn 48 iscritti); il conteggio "51 macchine a catalogo" (25 schede di verniciatura e 26 di Handling & Assembling sul sito di oggi); se "oltre il 90% del mercato all'estero" è ancora vero.
6. **Ruoli**: Giovanni Sedino "oggi guidata da" (CEO o amministratore unico); se Marta Sedino va nominata.
7. **Certificazioni**: se ce ne sono (ISO, marchi di prodotto, attestati CE degli impianti) e i PDF da scaricare: oggi la pagina mostra solo i riconoscimenti (Exporter of the Year 2024, partner LegnoLegno per Finestra+).
8. **Fiere**: HOLZ-HANDWERK 2028 (Norimberga, padiglione 9, stand 9-212) e le fiere del 2027; non sono in pagina finché non le confermano.
9. **Usato**: se Finiture 5 e Finiture 6 sono ancora in vendita.
10. **Handling & Assembling**: se va presentata anche con il nome Tambone (oggi in pagina no).
11. **Dati legali**: il C.F. 02832330241 nel piede del sito di oggi, diverso dalla P.IVA 03569090289 (in pagina c'è solo la P.IVA, da verificare in visura); PEC non trovata.
12. **Permesso per foto e render** presi da finiture.it, nome del fotografo del servizio `*_R01` e logo vettoriale (AI, EPS, SVG o PDF).

## Foto da fare dal vero

Le foto in pagina sono tutte loro, ma vengono da tre fonti con luci diverse (servizio `*_R01` del 2016 a 1920 px, foto di cantiere da telefono, foto di gallerie prodotto). Per una serie sola, un fotografo, una giornata in sede e una in un cantiere:

1. **Apertura con persone**: un tecnico Finiture in tuta con il logo accanto al Power&Free rosso carico di pezzi laccati appena usciti dal tunnel, luce del giorno, orizzontale, almeno 6000 px. Tiene il pezzo verniciato (come la porta verde di oggi) e aggiunge chi lo fa.
2. **Squadra**: l'originale della foto davanti alla sede (online solo 1167x397), oppure una ripresa nuova, orizzontale 3:2, con le divise.
3. **Linee consegnate**: per ogni cliente nominato una foto della linea in funzione, stessa luce e stesso taglio 3:2 di quella di Distner, con il nome del cliente e l'anno.
4. **Area test**: la cabina con il robot scoperto, un pezzo di un cliente in prova e un tecnico al lavoro (oggi il robot è sotto il telo).
5. **Assistenza**: il tecnico al quadro o da remoto davanti al Supervisor, luce morbida, 3:2.
6. **Settori**: per ognuno un pezzo appena verniciato appeso alla macchina, luce radente, 4:3, niente HDR (le foto di oggi hanno un leggero effetto HDR).
7. **Macchine**: i render CAD reggono, ma sono di epoche diverse; BM30 e BVC30 hanno il fondo fotografico e per questo non sono nella griglia: servono render su fondo chiaro uniforme come gli altri.

## Licenze

- Caratteri: Archivo (Omnibus-Type), SIL Open Font License 1.1, da Google Fonts; licenza in `sito/fonts/OFL-Archivo.txt`. Uso commerciale libero.
- Foto e render: di Finiture S.r.l. (finiture.it), da confermare (sopra, punto 12). Nessuna foto di repertorio in pagina, per decisione del committente: le nove foto di `assets/esterne/` non si usano (`assets/CREDITI.md`).
- Nessuna immagine generata dall'IA, nessun disegno al posto delle foto.

## Logo

- Usato: ritaglio dall'avatar del canale YouTube (`assets/originali/logo-finiture-da-youtube-ritagliato.png`, 879x313), bianco reso trasparente, PNG a 300 e 400 px (`sito/img/logo-300.png`, `logo-400.png`); per il piede scuro una versione con le lettere schiarite e l'ellisse rossa com'è (`logo-chiaro-*.png`). Viene da un JPEG: i bordi della pennellata sono un po' morbidi. Serve il vettoriale.
